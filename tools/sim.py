#!/usr/bin/env python3
"""tools/sim.py - helper CLI for the persona-debate protocol.

Every subcommand is driven entirely by the run's own `rubric.json`: option ids,
dimensions, levers, named/conditional questions, pairwise pairs, weight sets,
groups, seating and forbidden words all come from that file. Nothing here is
hard-coded to one run. See docs/data-formats.md for the full field reference.

Standard library only. PyYAML is optional and only improves `card.yaml`
parsing in `roster` (a regex fallback is used when it is not installed).

Usage:
    python3 tools/sim.py <command> --help

Commands: new-run, new-persona, roster, check, tables, index, anon,
aggregate, scan, lint, compare, blind, blind-report, privacy-scan.
"""
import argparse
import datetime
import glob
import json
import os
import random
import re
import shutil
import statistics
import sys

try:
    import yaml  # type: ignore
    HAS_YAML = True
except ImportError:  # pragma: no cover - exercised in environments without PyYAML
    yaml = None
    HAS_YAML = False


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_FORBIDDEN_WORDS = ["discount", "打折", "折扣", "减权"]

SOURCES_HEADER = (
    "evidence_id,claim,type,author_or_org,source_title,url,published_date,"
    "accessed_date,source_family,supports_or_challenges,limitations"
)

NOTICE_MARKERS = ("Simulation based on public material", "基于公开材料")

# Rank moves of this many places or more across weight sets are flagged.
# data-formats.md's rubric.aggregation.sensitivity is free text for humans
# ("...3+ places..."); there is no machine-readable threshold key, so this is
# a fixed default. See the gap note in tools/README.md.
SENSITIVITY_THRESHOLD = 3

# Posts sampled per round (A/B/C) per run for `blind`.
BLIND_SAMPLE_PER_ROUND = 10

ACCEPT_MAP = {
    "accept": "accept", "接受": "accept",
    "reject": "reject", "不接受": "reject",
    "partial": "partial", "部分接受": "partial",
}
RESULT_MAP = {
    "supports": "supports", "支持": "supports",
    "refutes": "refutes", "反驳": "refutes",
    "unclear": "unclear", "不清楚": "unclear",
}
POSITION_MAP = {
    "for": "for", "支持": "for",
    "against": "against", "反对": "against",
    "conditional": "conditional", "有条件": "conditional", "附条件": "conditional",
}

CLAIM_MARKER_EN = "**Claim (one line):**"

PERSONA_MD_BASENAMES = {"dossier.md", "views.md", "conversation.md", "industry.md"}
ROUND_MD_RE = re.compile(r"(^|[/\\])(r1|r3)[/\\][^/\\]+\.md$")
BOARD_MD_RE = re.compile(r"(^|[/\\])board[/\\](A|B|C|overtime)[/\\][^/\\]+[/\\][^/\\]+\.md$")
BOARD_SUMMARY_MD_RE = re.compile(r"(^|[/\\])board[/\\]summary(_full)?[/\\][^/\\]+\.md$")
JUDGE_MD_RE = re.compile(r"(^|[/\\])judge[/\\][^/\\]+\.md$")
BASELINE_RE = re.compile(r"(^|[/\\])baselines[/\\]")
SOURCES_CSV_RE = re.compile(r"(^|[/\\])sources[^/\\]*\.csv$")

FENCE_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)


# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------

def eprint(*a, **kw):
    kw.setdefault("file", sys.stderr)
    print(*a, **kw)


def p(run, *parts):
    return os.path.join(run, *parts)


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write_text(path, text):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path, data):
    write_text(path, json.dumps(data, ensure_ascii=False, indent=1) + "\n")


def try_load_json(path):
    """Load JSON, returning (data, None) or (None, error message)."""
    if not os.path.isfile(path):
        return None, f"{path} not found"
    try:
        return load_json(path), None
    except json.JSONDecodeError as e:
        return None, f"{path} is not valid JSON: {e}"
    except OSError as e:
        return None, f"cannot read {path}: {e}"


def load_submissions(pattern, strip_suffix=None):
    """Load all JSON files matching a glob pattern, keyed by id (filename stem)."""
    result = {}
    for f in sorted(glob.glob(pattern)):
        key = os.path.basename(f)[:-5]
        if strip_suffix and key.endswith(strip_suffix):
            key = key[: -len(strip_suffix)]
        try:
            result[key] = load_json(f)
        except (OSError, json.JSONDecodeError) as e:
            eprint(f"warning: cannot parse {f}: {e}")
    return result


def resolve_run(args):
    run = getattr(args, "run", None) or os.environ.get("RUN")
    if not run:
        eprint("error: no run specified. Pass --run PATH or set the RUN environment variable.")
        return None
    return run


def is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def norm_enum(value, mapping):
    if value is None:
        return None
    return mapping.get(value, value)


def copy_template_tree(src_root, dst_root, replacements=None):
    """Copy every file under src_root into dst_root, preserving relative paths.

    When `replacements` is given, each text file has those substrings replaced
    (binary files are copied verbatim). Returns the number of files copied.
    """
    copied = 0
    for root, _dirs, files in os.walk(src_root):
        rel = os.path.relpath(root, src_root)
        for fn in sorted(files):
            src = os.path.join(root, fn)
            dst = os.path.join(dst_root, fn) if rel == "." else os.path.join(dst_root, rel, fn)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if replacements:
                try:
                    text = read_text(src)
                except UnicodeDecodeError:
                    shutil.copyfile(src, dst)
                    copied += 1
                    continue
                for old, new in replacements.items():
                    text = text.replace(old, new)
                write_text(dst, text)
            else:
                shutil.copyfile(src, dst)
            copied += 1
    return copied


# ---------------------------------------------------------------------------
# Rubric accessors
# ---------------------------------------------------------------------------

def rubric_options(rubric):
    return list((rubric.get("options") or {}).keys())


def rubric_short_options(rubric):
    return set(rubric.get("short_options") or [])


def rubric_dimensions(rubric):
    return list((rubric.get("dimensions") or {}).keys())


def rubric_scale(rubric):
    scale = rubric.get("scale") or {}
    return scale.get("min", 0), scale.get("max", 10)


def rubric_personas(rubric):
    return rubric.get("personas") or {}


def overall_score(sub, opt):
    v = (sub.get("options") or {}).get(opt) or {}
    x = v.get("overall")
    return x if is_number(x) else None


def weighted_score(sub, opt, dims, weights):
    v = (sub.get("options") or {}).get(opt) or {}
    pairs = []
    for d in dims:
        x, w = v.get(d), weights.get(d)
        if is_number(x) and is_number(w):
            pairs.append((x, w))
    total_w = sum(w for _, w in pairs)
    if not pairs or total_w == 0:
        return None
    return sum(x * w for x, w in pairs) / total_w


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def stats(xs):
    xs = [x for x in xs if is_number(x)]
    if not xs:
        return None
    if len(xs) > 1:
        q = statistics.quantiles(xs, n=4, method="inclusive")
    else:
        q = [xs[0], xs[0], xs[0]]
    return {
        "n": len(xs), "median": statistics.median(xs),
        "q1": q[0], "q3": q[2], "iqr": q[2] - q[0],
        "min": min(xs), "max": max(xs),
    }


def rank(table):
    """Rank by median descending; ties broken by the smaller IQR first."""
    items = [(o, s) for o, s in table.items() if s]
    items.sort(key=lambda kv: (-kv[1]["median"], kv[1]["iqr"]))
    return {o: i + 1 for i, (o, _) in enumerate(items)}


def fmt_stats(s):
    if not s:
        return "-"
    return f"{s['median']:g} ({s['q1']:g}-{s['q3']:g}, n={s['n']})"


# ---------------------------------------------------------------------------
# Post parsing
# ---------------------------------------------------------------------------

def extract_post_json(text):
    """The post's JSON tail: the LAST fenced ```json block, or a trailing bare object."""
    blocks = FENCE_RE.findall(text)
    if blocks:
        try:
            obj = json.loads(blocks[-1])
            return obj if isinstance(obj, dict) else None
        except json.JSONDecodeError:
            return None
    stripped = text.rstrip()
    idx = stripped.rfind("\n{")
    if idx >= 0:
        candidate = stripped[idx + 1:]
    elif stripped.startswith("{"):
        candidate = stripped
    else:
        return None
    try:
        obj = json.loads(candidate)
        return obj if isinstance(obj, dict) else None
    except json.JSONDecodeError:
        return None


def post_author(filename, known_ids=None):
    """The persona id in a post filename: ID.md, ID_interjection.md, ID_插话.md, <turn>_ID.md."""
    stem = os.path.splitext(os.path.basename(filename))[0]
    parts = stem.split("_")
    if known_ids:
        known_ids = set(known_ids)
        for part in parts:
            if part in known_ids:
                return part
    for part in parts:
        if not part.isdigit():
            return part
    return parts[0]


def iter_board_files(run, rounds=("A", "B", "C")):
    files = []
    for r in rounds:
        files += sorted(glob.glob(p(run, "board", r, "*", "*.md")))
    return files


def strip_post(text):
    """Blind review: drop the JSON tail, the header line and any '>' lines."""
    text = FENCE_RE.sub("", text)
    stripped = text.rstrip()
    idx = stripped.rfind("\n{")
    if idx >= 0 and stripped[idx + 1:].strip().endswith("}"):
        text = stripped[:idx]
    else:
        text = stripped
    lines = [ln for ln in text.splitlines() if not ln.startswith("# ") and not ln.startswith(">")]
    return "\n".join(lines).strip() + "\n"


def extract_claim_line(text):
    for line in text.splitlines():
        s = line.strip()
        if CLAIM_MARKER_EN in s:
            return s.split(CLAIM_MARKER_EN, 1)[1].strip()
        if "主张" in s:
            return re.sub(r"^\**[^*]*主张[^:：]*[:：]\**\s*", "", s).strip()
    return ""


# ---------------------------------------------------------------------------
# new-run / new-persona
# ---------------------------------------------------------------------------

RUN_LAYOUT_DIRS = [
    "evidence", "r1", "r3", "baselines",
    os.path.join("board", "A"), os.path.join("board", "B"), os.path.join("board", "C"),
    os.path.join("board", "overtime"), os.path.join("board", "summary"),
    os.path.join("board", "summary_full"),
    "judge", "reader",
]


def cmd_new_run(args):
    date = args.date or datetime.date.today().isoformat()
    run_dir = os.path.join(args.root, f"{date}_{args.slug}")
    if os.path.isdir(run_dir) and os.listdir(run_dir):
        eprint(f"error: {run_dir} already exists and is not empty.")
        return 1
    os.makedirs(run_dir, exist_ok=True)
    template_root = os.path.join("templates", "run")
    copied = copy_template_tree(template_root, run_dir) if os.path.isdir(template_root) else 0
    if copied == 0:
        print(f"note: {template_root} has no files yet; created folders only.")
    for d in RUN_LAYOUT_DIRS:
        os.makedirs(os.path.join(run_dir, d), exist_ok=True)
    print(f"new-run: created {run_dir} ({copied} template file(s) copied)")
    return 0


def cmd_new_persona(args):
    target = os.path.join(args.root, f"{args.id}_{args.slug}")
    if os.path.isdir(target) and os.listdir(target):
        eprint(f"error: {target} already exists and is not empty.")
        return 1
    template_root = os.path.join("templates", "persona")
    if not os.path.isdir(template_root):
        eprint(f"error: {template_root} does not exist.")
        return 1
    os.makedirs(target, exist_ok=True)
    copied = copy_template_tree(template_root, target, {"<ID>": args.id})
    print(f"new-persona: created {target} ({copied} file(s))")
    return 0


# ---------------------------------------------------------------------------
# roster
# ---------------------------------------------------------------------------

def _strip_inline_comment(value):
    return re.sub(r"\s+#.*$", "", value).strip()


def _read_card_fields_regex(text):
    lines = text.splitlines()
    fields = {"id": None, "name": None, "aliases": []}
    i = 0
    while i < len(lines):
        m = re.match(r"^(id|name|aliases):\s*(.*)$", lines[i])
        if m:
            key, rest = m.group(1), _strip_inline_comment(m.group(2))
            if key == "aliases":
                if rest.startswith("["):
                    inner = rest.strip("[]")
                    fields["aliases"] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
                elif rest:
                    fields["aliases"] = [rest.strip("'\"")]
                else:
                    items, j = [], i + 1
                    while j < len(lines):
                        im = re.match(r"^\s+-\s*(.+)$", lines[j])
                        if not im:
                            break
                        items.append(im.group(1).strip().strip("'\""))
                        j += 1
                    fields["aliases"] = items
            else:
                fields[key] = rest.strip("'\"")
        i += 1
    return fields


def read_card_fields(path):
    text = read_text(path)
    if HAS_YAML:
        try:
            data = yaml.safe_load(text) or {}
            if isinstance(data, dict):
                return {
                    "id": data.get("id"),
                    "name": data.get("name"),
                    "aliases": list(data.get("aliases") or []),
                }
        except yaml.YAMLError:
            pass
    return _read_card_fields_regex(text)


def cmd_roster(args):
    personas = {}
    for d in args.personas:
        card = os.path.join(d, "card.yaml")
        if not os.path.isfile(card):
            eprint(f"roster: no card.yaml in {d}, skipping.")
            continue
        fields = read_card_fields(card)
        pid = fields.get("id")
        if not pid:
            eprint(f"roster: {card} has no id:, skipping.")
            continue
        personas[pid] = {"name": fields.get("name") or pid, "aliases": fields.get("aliases") or []}
    if args.write:
        rubric, err = try_load_json(args.write)
        if err:
            rubric = {}
        rubric.setdefault("personas", {}).update(personas)
        save_json(args.write, rubric)
        print(f"roster: merged {len(personas)} persona(s) into {args.write}")
    else:
        print(json.dumps({"personas": personas}, ensure_ascii=False, indent=1))
    return 0


# ---------------------------------------------------------------------------
# check
# ---------------------------------------------------------------------------

def valid_score(x, lo, hi):
    return x is None or (isinstance(x, int) and not isinstance(x, bool) and lo <= x <= hi)


def check_submission(sub, rubric, round_name):
    issues = []
    options = rubric_options(rubric)
    short_options = rubric_short_options(rubric)
    dims = rubric_dimensions(rubric)
    lo, hi = rubric_scale(rubric)
    sub_options = sub.get("options") or {}

    for opt in options:
        entry = sub_options.get(opt)
        if entry is None:
            issues.append(f"missing option {opt}")
            continue
        if not valid_score(entry.get("overall"), lo, hi):
            issues.append(f"{opt}.overall={entry.get('overall')!r}")
        if opt not in short_options:
            for d in dims:
                if d not in entry:
                    issues.append(f"{opt} missing dimension {d}")
                elif not valid_score(entry.get(d), lo, hi):
                    issues.append(f"{opt}.{d}={entry.get(d)!r}")

    if rubric.get("levers"):
        lv = sub.get("levers") or {}
        total = sum(v for v in lv.values() if is_number(v))
        if total != 100:
            issues.append(f"levers sum to {total}, not 100")

    r1req = rubric.get("r1_requirements") or {}
    if "paths_for_user" in r1req:
        lo_n, hi_n = r1req["paths_for_user"]
        n = len(sub.get("paths_for_user") or [])
        if not (lo_n <= n <= hi_n):
            issues.append(f"paths_for_user has {n} entries, need {lo_n}-{hi_n}")
    if round_name == "r1" and "cruxes" in r1req:
        n = len(sub.get("cruxes") or [])
        if n != r1req["cruxes"]:
            issues.append(f"cruxes has {n} entries, need {r1req['cruxes']}")

    for pair in rubric.get("pairwise") or []:
        a, b = pair[0], pair[1]
        found = any(
            isinstance(x, dict) and {x.get("a"), x.get("b")} == {a, b} and x.get("pick")
            for x in (sub.get("pairwise") or [])
        )
        if not found:
            issues.append(f"pairwise {a} vs {b} has no pick")

    if round_name == "r3" and "changes" not in sub:
        issues.append("missing changes")

    return issues


def cmd_check(args):
    run = resolve_run(args)
    if not run:
        return 2
    rubric, err = try_load_json(p(run, "rubric.json"))
    if err:
        eprint(f"error: {err}")
        return 2
    round_name = args.round
    targets = sorted(glob.glob(p(run, round_name, "*.json")))
    if args.baselines:
        targets += sorted(glob.glob(p(run, "baselines", f"*_{round_name}.json")))
    ok = 0
    for f in targets:
        try:
            sub = load_json(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"{os.path.basename(f)}: cannot parse JSON: {e}")
            continue
        issues = check_submission(sub, rubric, round_name)
        if issues:
            print(f"{os.path.basename(f)}: " + "; ".join(issues))
        else:
            ok += 1
    print(f"{round_name}: {len(targets)} file(s), {ok} clean")
    return 0 if ok == len(targets) else 1


# ---------------------------------------------------------------------------
# tables
# ---------------------------------------------------------------------------

def cmd_tables(args):
    run = resolve_run(args)
    if not run:
        return 2
    rubric, err = try_load_json(p(run, "rubric.json"))
    if err:
        eprint(f"error: {err}")
        return 2
    data, err = try_load_json(p(run, "tables.json"))
    if err:
        eprint(f"error: {err}")
        return 2
    tables = data.get("tables") or []
    cruxes = {}
    cruxes_data, cerr = try_load_json(p(run, "cruxes.json"))
    if not cerr:
        cruxes = {c["id"]: c for c in cruxes_data.get("cruxes") or []}

    seating = rubric.get("seating") or {}
    size_range = seating.get("table_size")
    seats_per = seating.get("seats_per_persona")
    not_indep_groups = [frozenset(g) for g in rubric.get("not_independent") or []]

    problems = 0
    seats = {}
    for t in tables:
        members = t.get("members") or []
        n = len(members)
        if size_range and not (size_range[0] <= n <= size_range[1]):
            print(f"{t.get('id')}: {n} members, expected {size_range[0]}-{size_range[1]}")
            problems += 1
        for m in members:
            seats.setdefault(m, []).append(t.get("id"))

        crux = cruxes.get(t.get("crux"))
        if crux:
            represented = []
            for side in crux.get("sides") or []:
                reps = [m for m in members if m in (side.get("members") or [])]
                represented.append(reps)
                if len(reps) >= 2:
                    for g in not_indep_groups:
                        if set(reps) <= g:
                            print(f"{t.get('id')}: side {side.get('label', '?')!r} "
                                  f"represented only by not-independent group {sorted(reps)}")
                            problems += 1
                            break
            n_sides = sum(1 for reps in represented if reps)
            if represented and n_sides < 2:
                print(f"{t.get('id')}: only {n_sides} side(s) of crux {t.get('crux')} represented")
                problems += 1

    if seats_per is not None:
        for pid, ts in seats.items():
            if len(ts) != seats_per:
                print(f"{pid}: sits at {len(ts)} table(s) {ts}, expected {seats_per}")
                problems += 1

    total_seats = sum(len(t.get("members") or []) for t in tables)
    print(f"{len(tables)} table(s); {total_seats} seat(s); {problems} problem(s)")
    return 1 if problems else 0


# ---------------------------------------------------------------------------
# index
# ---------------------------------------------------------------------------

def cmd_index(args):
    run = resolve_run(args)
    if not run:
        return 2
    rubric = {}
    rubric_data, err = try_load_json(p(run, "rubric.json"))
    if not err:
        rubric = rubric_data
    names = rubric_personas(rubric)
    rows = []
    for f in sorted(glob.glob(p(run, "board", "A", "*", "*.md"))):
        table = os.path.basename(os.path.dirname(f))
        pid = os.path.splitext(os.path.basename(f))[0]
        claim = extract_claim_line(read_text(f))
        display = (names.get(pid) or {}).get("name", pid)
        rows.append(f"| {table} | {pid} {display} | {claim} |")
    out_path = p(run, "board", "A", "INDEX.md")
    lines = ["# Round A claim index (generated by tools/sim.py index)", "",
             "| Table | Persona | Claim |", "|---|---|---|"] + rows
    write_text(out_path, "\n".join(lines) + "\n")
    print(f"index: {len(rows)} post(s) -> {out_path}")
    return 0


# ---------------------------------------------------------------------------
# anon
# ---------------------------------------------------------------------------

def cmd_anon(args):
    run = resolve_run(args)
    if not run:
        return 2
    rubric, err = try_load_json(p(run, "rubric.json"))
    if err:
        eprint(f"error: {err}")
        return 2
    personas = rubric_personas(rubric)
    ids = list(personas.keys())
    if not ids:
        eprint("anon: rubric.json has no personas.")
        return 1

    rng = random.Random(args.seed)
    codes = [f"P{i:02d}" for i in range(1, len(ids) + 1)]
    rng.shuffle(codes)
    key = dict(zip(ids, codes))

    name_patterns = []
    for pid, info in personas.items():
        names = [info.get("name")] + list(info.get("aliases") or [])
        for nm in sorted((n for n in names if n), key=len, reverse=True):
            rx = re.compile(r"\b" + re.escape(nm) + r"\b") if nm.isascii() else re.compile(re.escape(nm))
            name_patterns.append((rx, key[pid]))
    id_alt = "|".join(sorted((re.escape(i) for i in ids), key=len, reverse=True))
    id_pattern = re.compile(r"(?<![A-Za-z0-9])(" + id_alt + r")(?![A-Za-z0-9])")

    n = 0
    for f in glob.glob(p(run, "board", "[ABC]", "*", "*.md")):
        rnd, table, fname = f.split(os.sep)[-3:]
        pid = post_author(fname, ids)
        suffix = "_interjection" if "interjection" in fname else ("_插话" if "插话" in fname else "")
        text = read_text(f)
        text = "\n".join(
            ln for ln in text.splitlines()
            if not ln.startswith("> Stance") and not ln.startswith("> 立场来源")
        )
        for rx, code in name_patterns:
            text = rx.sub(code, text)
        text = id_pattern.sub(lambda m: key.get(m.group(1), m.group(1)), text)
        out = p(run, "judge", "anon", rnd, table, f"{key.get(pid, pid)}{suffix}.md")
        write_text(out, text)
        n += 1

    save_json(p(run, "judge", "anon_key.json"), key)
    print(f"anon: {n} post(s) anonymized")
    return 0


# ---------------------------------------------------------------------------
# aggregate
# ---------------------------------------------------------------------------

def cmd_aggregate(args):
    run = resolve_run(args)
    if not run:
        return 2
    rubric, err = try_load_json(p(run, "rubric.json"))
    if err:
        eprint(f"error: {err}")
        return 2
    options = rubric_options(rubric)
    dims = rubric_dimensions(rubric)
    persona_ids = rubric_personas(rubric).keys()

    r1 = load_submissions(p(run, "r1", "*.json"))
    r3 = load_submissions(p(run, "r3", "*.json"))
    baselines_r1 = load_submissions(p(run, "baselines", "*_r1.json"), strip_suffix="_r1")
    baselines_r3 = load_submissions(p(run, "baselines", "*_r3.json"), strip_suffix="_r3")

    cruxes = {}
    cruxes_data, cerr = try_load_json(p(run, "cruxes.json"))
    if not cerr:
        cruxes = {c["id"]: c for c in cruxes_data.get("cruxes") or []}

    out = {"n_r1": len(r1), "n_r3": len(r3)}

    def table_for(subs):
        return {o: stats([overall_score(d, o) for d in subs.values()]) for o in options}

    t1, t3 = table_for(r1), table_for(r3)
    out["overall_r1"], out["overall_r3"] = t1, t3
    out["rank_r1"], out["rank_r3"] = rank(t1), rank(t3)

    final = r3 if r3 else r1
    final_table = t3 if r3 else t1

    groups = rubric.get("groups") or {}
    out["groups_r3"] = {
        g: {o: (stats([overall_score(final[m], o) for m in ms if m in final]) or {}).get("median") for o in options}
        for g, ms in groups.items()
    }

    weight_sets = rubric.get("weight_sets") or {}
    weighted_out = {}
    for wname, w in weight_sets.items():
        tbl = {o: stats([weighted_score(d, o, dims, w) for d in final.values()]) for o in options}
        weighted_out[wname] = {"stats": tbl, "rank": rank(tbl)}
    out["weighted"] = weighted_out
    threshold = (rubric.get("aggregation") or {}).get("sensitivity_threshold", SENSITIVITY_THRESHOLD)
    if not isinstance(threshold, int) or threshold < 1:
        threshold = SENSITIVITY_THRESHOLD
    out["sensitivity_threshold"] = threshold
    flips = []
    for o in options:
        ranks = [weighted_out[n]["rank"].get(o) for n in weight_sets if weighted_out[n]["rank"].get(o)]
        if ranks and max(ranks) - min(ranks) >= threshold:
            flips.append({"option": o, "ranks": {n: weighted_out[n]["rank"].get(o) for n in weight_sets}})
    out["sensitivity_flips"] = flips

    moves = {}
    for pid, d3 in r3.items():
        d1 = r1.get(pid)
        if not d1:
            continue
        for o in options:
            a, b = overall_score(d1, o), overall_score(d3, o)
            if a is not None and b is not None and a != b:
                moves.setdefault(o, []).append({"id": pid, "from": a, "to": b})
    out["moves"] = moves
    out["n_changed_scores"] = sum(len(v) for v in moves.values())

    if rubric.get("levers"):
        lever_ids = list(rubric["levers"].keys())

        def lever_stats(subs):
            return {k: stats([(d.get("levers") or {}).get(k) for d in subs.values()]) for k in lever_ids}

        out["levers_r1"], out["levers_r3"] = lever_stats(r1), lever_stats(r3)
    else:
        out["levers_r1"], out["levers_r3"] = {}, {}

    named_q = rubric.get("named_questions") or {}

    def questions_for(subs):
        res = {}
        for qid in named_q:
            positions, scores = {}, []
            for d in subs.values():
                q = (d.get("questions") or {}).get(qid)
                if not q:
                    continue
                pos = norm_enum(q.get("position"), POSITION_MAP)
                if pos:
                    positions[pos] = positions.get(pos, 0) + 1
                if is_number(q.get("score")):
                    scores.append(q.get("score"))
            res[qid] = {"positions": positions, "score": stats(scores)}
        return res

    out["questions_r1"], out["questions_r3"] = questions_for(r1), questions_for(r3)

    cond_q = rubric.get("conditional_questions") or {}

    def conditions_for(subs):
        res = {}
        for qid in cond_q:
            tally = {}
            for d in subs.values():
                for c in (d.get("conditions") or {}).get(qid) or []:
                    tally[c] = tally.get(c, 0) + 1
            res[qid] = dict(sorted(tally.items()))
        return res

    out["conditions"] = {"r1": conditions_for(r1), "r3": conditions_for(r3)}

    def pairwise_for(subs):
        res = {}
        for pair in rubric.get("pairwise") or []:
            a, b = pair[0], pair[1]
            key = f"{a} vs {b}"
            counts = {a: 0, b: 0}
            for d in subs.values():
                for x in d.get("pairwise") or []:
                    if isinstance(x, dict) and {x.get("a"), x.get("b")} == {a, b} and x.get("pick") in (a, b):
                        counts[x["pick"]] += 1
            total = counts[a] + counts[b]
            res[key] = {
                "counts": counts,
                "win_rate": {a: round(counts[a] / total, 3), b: round(counts[b] / total, 3)} if total else {},
            }
        return res

    out["pairwise"] = {"r1": pairwise_for(r1), "r3": pairwise_for(r3)}

    baseline_ids = sorted(set(baselines_r1) | set(baselines_r3))
    out["baselines"] = {
        bid: {
            "r1": {o: overall_score(baselines_r1[bid], o) for o in options} if bid in baselines_r1 else {},
            "r3": {o: overall_score(baselines_r3[bid], o) for o in options} if bid in baselines_r3 else {},
        }
        for bid in baseline_ids
    }

    def baseline_final_score(bid, o):
        if bid in baselines_r3:
            return overall_score(baselines_r3[bid], o)
        if bid in baselines_r1:
            return overall_score(baselines_r1[bid], o)
        return None

    pmb = {}
    for bid in baseline_ids:
        gaps = {}
        for o in options:
            med = (final_table.get(o) or {}).get("median")
            base = baseline_final_score(bid, o)
            if med is not None and base is not None:
                gaps[o] = round(med - base, 3)
        pmb[bid] = {
            "gaps": gaps,
            "mean_abs_gap": round(statistics.mean(abs(v) for v in gaps.values()), 3) if gaps else None,
        }
    out["persona_minus_baseline"] = pmb

    verdict_tally = {"accept": 0, "reject": 0, "partial": 0}
    n_search = 0
    received = {}
    empty, intent_gap = [], []
    challenges, retracted = [], []
    board_files = iter_board_files(run, ("A", "B", "C")) + iter_board_files(run, ("overtime",))
    for f in board_files:
        rnd, table, fname = f.split(os.sep)[-3:]
        pid = post_author(fname, persona_ids)
        blk = extract_post_json(read_text(f))
        if not blk:
            continue
        n_search += len(blk.get("searches") or [])
        for c in blk.get("source_challenge") or []:
            if isinstance(c, dict):
                challenges.append({"from": pid, "round": rnd, **c})
        for c in blk.get("retracted") or []:
            if isinstance(c, dict):
                retracted.append({"by": pid, "round": rnd, **c})
        for r in blk.get("responses") or []:
            v = norm_enum(r.get("verdict"), ACCEPT_MAP)
            if v in verdict_tally:
                verdict_tally[v] += 1
                if v in ("accept", "partial") and r.get("to"):
                    received.setdefault(r["to"], []).append({"from": pid, "post": r.get("post"), "verdict": v})
                    crux_options = (cruxes.get(table) or {}).get("options") or []
                    if rnd == "C" and pid in r1 and pid in r3 and crux_options:
                        if all(overall_score(r1[pid], o) == overall_score(r3[pid], o) for o in crux_options):
                            empty.append({"id": pid, "table": table, "post": r.get("post"),
                                          "verdict": v, "options": crux_options})
        if rnd == "C" and pid in r1 and pid in r3:
            for o, dv in (blk.get("intended_moves") or {}).items():
                a, b = overall_score(r1[pid], o), overall_score(r3[pid], o)
                if is_number(dv) and a is not None and b is not None and (b - a) != dv:
                    intent_gap.append({"id": pid, "option": o, "intended": dv, "actual": b - a})
    out["verdicts"] = verdict_tally
    out["n_searches_in_debate"] = n_search
    out["persuaded_by"] = {k: len(v) for k, v in sorted(received.items(), key=lambda kv: -len(kv[1]))}
    out["empty_concessions"] = empty
    out["intent_vs_actual"] = intent_gap
    out["source_challenges"], out["retracted"] = challenges, retracted

    judge = {}
    scores_data, serr = try_load_json(p(run, "judge", "scores.json"))
    if not serr:
        posts = scores_data.get("posts") or {}
        fields = ("claim_clear", "evidence_holds", "answers_strongest", "source_independent")
        field_values = {f: [] for f in fields}
        flags = {}
        for s in posts.values():
            for f in fields:
                if is_number(s.get(f)):
                    field_values[f].append(s[f])
            for fl in s.get("flags") or []:
                flags[fl] = flags.get(fl, 0) + 1
        judge = {"n_posts": len(posts), "fields": {f: stats(v) for f, v in field_values.items()}, "flags": flags}
    out["judge"] = judge

    save_json(p(run, "summary.json"), out)
    write_summary_md(run, out, options)
    print(f"aggregate: R1 {len(r1)}, R3 {len(r3)}; {out['n_changed_scores']} score change(s); verdicts {verdict_tally}")
    return 0


def write_summary_md(run, o, options):
    order = sorted(set(options) | set(o["overall_r1"]) | set(o["overall_r3"]),
                    key=lambda x: o["rank_r3"].get(x, o["rank_r1"].get(x, 999)))
    lines = [f"# Summary for {os.path.basename(run.rstrip('/'))}",
             "", "Generated by `tools/sim.py aggregate`; rules are in `rubric.json`.", ""]

    lines += ["## Overall score by option: median (IQR)", "",
              "| Option | R1 | R1 rank | R3 | R3 rank | Changed |", "|---|---|---|---|---|---|"]
    for opt in order:
        lines.append(f"| {opt} | {fmt_stats(o['overall_r1'].get(opt))} | {o['rank_r1'].get(opt, '-')} | "
                      f"{fmt_stats(o['overall_r3'].get(opt))} | {o['rank_r3'].get(opt, '-')} | "
                      f"{len(o['moves'].get(opt, []))} |")
    lines.append("")

    if any(o.get("groups_r3", {}).values()):
        lines += ["## Groups (median, final round)", "",
                  "| Group | " + " | ".join(order) + " |", "|---|" + "---|" * len(order)]
        for g, vals in o["groups_r3"].items():
            lines.append(f"| {g} | " + " | ".join(str(vals.get(opt, "-")) for opt in order) + " |")
        lines.append("")

    if o.get("baselines"):
        lines += ["## Baselines", "", "| Baseline | Option | R1 | R3 |", "|---|---|---|---|"]
        for bid in sorted(o["baselines"]):
            rounds = o["baselines"][bid]
            for opt in order:
                r1v, r3v = rounds.get("r1", {}).get(opt), rounds.get("r3", {}).get(opt)
                if r1v is not None or r3v is not None:
                    lines.append(f"| {bid} | {opt} | {r1v if r1v is not None else '-'} | "
                                  f"{r3v if r3v is not None else '-'} |")
        lines.append("")

    if o.get("persona_minus_baseline"):
        lines += ["## Persona minus baseline", "", "| Baseline | Mean absolute gap |", "|---|---|"]
        for bid in sorted(o["persona_minus_baseline"]):
            lines.append(f"| {bid} | {o['persona_minus_baseline'][bid].get('mean_abs_gap', '-')} |")
        lines.append("")

    if o.get("weighted"):
        lines += ["## Rank by weight set", "", "| Option | " + " | ".join(o["weighted"]) + " |",
                  "|---|" + "---|" * len(o["weighted"])]
        for opt in order:
            lines.append(f"| {opt} | " +
                          " | ".join(str(o["weighted"][n]["rank"].get(opt, "-")) for n in o["weighted"]) + " |")
        flips = ", ".join(f["option"] for f in o["sensitivity_flips"]) or "none"
        lines += ["", f"Rank changes of {o.get('sensitivity_threshold', SENSITIVITY_THRESHOLD)}+ places across weight sets: {flips}", ""]

    if o.get("levers_r1") or o.get("levers_r3"):
        lines += ["## Levers (points out of 100): median (IQR)", "", "| Lever | R1 | R3 |", "|---|---|---|"]
        for k in sorted(set(o["levers_r1"]) | set(o["levers_r3"])):
            lines.append(f"| {k} | {fmt_stats(o['levers_r1'].get(k))} | {fmt_stats(o['levers_r3'].get(k))} |")
        lines.append("")

    if o.get("questions_r1") or o.get("questions_r3"):
        lines += ["## Named questions", ""]
        for qid in sorted(set(o["questions_r1"]) | set(o["questions_r3"])):
            lines.append(f"- {qid} R1: {o['questions_r1'].get(qid)}")
            lines.append(f"- {qid} R3: {o['questions_r3'].get(qid)}")
        lines.append("")

    if o.get("conditions", {}).get("r1") or o.get("conditions", {}).get("r3"):
        lines += ["## Conditional-question conditions (count of personas selecting each)", ""]
        for qid in sorted(set(o["conditions"]["r1"]) | set(o["conditions"]["r3"])):
            lines.append(f"- {qid} R1: {o['conditions']['r1'].get(qid)}")
            lines.append(f"- {qid} R3: {o['conditions']['r3'].get(qid)}")
        lines.append("")

    if o.get("pairwise", {}).get("r1") or o.get("pairwise", {}).get("r3"):
        lines += ["## Pairwise comparisons", "",
                  "| Comparison | R1 counts | R1 win rate | R3 counts | R3 win rate |", "|---|---|---|---|---|"]
        for key in sorted(set(o["pairwise"]["r1"]) | set(o["pairwise"]["r3"])):
            r1p, r3p = o["pairwise"]["r1"].get(key, {}), o["pairwise"]["r3"].get(key, {})
            lines.append(f"| {key} | {r1p.get('counts', '-')} | {r1p.get('win_rate', '-')} | "
                         f"{r3p.get('counts', '-')} | {r3p.get('win_rate', '-')} |")
        lines.append("")

    lines += ["## Debate", "",
              f"- Verdicts: {o['verdicts']}",
              f"- Scores changed: {o['n_changed_scores']}",
              f"- Empty concessions: {len(o['empty_concessions'])}",
              f"- Intent vs actual mismatches: {len(o['intent_vs_actual'])}",
              f"- Persuaded (verdict received, by persona): {o['persuaded_by']}",
              f"- Source challenges: {len(o['source_challenges'])}; retractions: {len(o['retracted'])}",
              f"- Searches logged in debate: {o['n_searches_in_debate']}", ""]

    if o.get("judge"):
        j = o["judge"]
        lines += ["## Judge scorecards", "", f"- Posts scored: {j.get('n_posts', 0)}",
                  f"- Flags: {j.get('flags', {})}", ""]

    write_text(p(run, "summary.md"), "\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# scan
# ---------------------------------------------------------------------------

def discover_persona_dirs(run, explicit_dirs):
    if explicit_dirs:
        return explicit_dirs
    ids = []
    if run:
        rubric, err = try_load_json(p(run, "rubric.json"))
        if not err:
            ids = list(rubric_personas(rubric).keys())
    roots = [d for d in ("workspace/personas", "examples/personas", "personas") if os.path.isdir(d)]
    found = []
    for root in roots:
        if ids:
            for pid in ids:
                found += sorted(glob.glob(os.path.join(root, f"{pid}_*")))
        else:
            found += sorted(d for d in glob.glob(os.path.join(root, "*")) if os.path.isdir(d))
    return [d for d in found if os.path.isdir(d)]


def cmd_scan(args):
    run = args.run or os.environ.get("RUN")
    forbidden = None
    if run:
        rubric, err = try_load_json(p(run, "rubric.json"))
        if not err:
            forbidden = rubric.get("forbidden_words")
    forbidden = forbidden or list(DEFAULT_FORBIDDEN_WORDS)

    files = []
    for d in discover_persona_dirs(run, args.personas):
        card = os.path.join(d, "card.yaml")
        if os.path.isfile(card):
            files.append(card)
    if args.boards:
        if not run:
            eprint("error: scan --boards needs --run or the RUN environment variable.")
            return 2
        files += sorted(glob.glob(p(run, "board", "*", "*", "*.md")))

    hits = 0
    for f in files:
        try:
            lines = read_text(f).splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        for i, line in enumerate(lines, 1):
            if line.startswith("#"):
                continue
            for w in forbidden:
                if w in line:
                    print(f"{f}:{i}: {line.strip()[:80]}")
                    hits += 1
                    break
    print(f"scan: {hits} hit(s)" if hits else "scan: no hits")
    return 1 if hits else 0


# ---------------------------------------------------------------------------
# lint
# ---------------------------------------------------------------------------

def needs_notice(relpath):
    norm = relpath.replace(os.sep, "/")
    if BASELINE_RE.search(norm):
        return False
    if (ROUND_MD_RE.search(norm) or BOARD_MD_RE.search(norm)
            or BOARD_SUMMARY_MD_RE.search(norm) or JUDGE_MD_RE.search(norm)):
        return True
    return os.path.basename(norm) in PERSONA_MD_BASENAMES


def _collect_lint_files(paths):
    all_files = []
    missing = 0
    for path in paths:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if d != ".git"]
                for fn in sorted(files):
                    all_files.append(os.path.join(root, fn))
        elif os.path.isfile(path):
            all_files.append(path)
        else:
            eprint(f"lint: {path} not found.")
            missing += 1
    return sorted(all_files), missing


def cmd_lint(args):
    all_files, errors = _collect_lint_files(args.paths)
    warnings = 0

    for f in all_files:
        base = os.path.basename(f)
        if not base.isascii():
            if "_插话" in base:
                print(f"{f}: WARNING non-ASCII filename (legacy interjection)")
                warnings += 1
            else:
                print(f"{f}: ERROR non-ASCII filename")
                errors += 1

        if f.endswith(".json"):
            try:
                load_json(f)
            except (OSError, json.JSONDecodeError) as e:
                print(f"{f}: ERROR invalid JSON: {e}")
                errors += 1
            continue

        if SOURCES_CSV_RE.search(f.replace(os.sep, "/")):
            try:
                with open(f, encoding="utf-8", newline="") as fh:
                    header = fh.readline().rstrip("\r\n").lstrip("\ufeff")
            except OSError as e:
                print(f"{f}: ERROR cannot read: {e}")
                errors += 1
                continue
            if header != SOURCES_HEADER:
                print(f"{f}: ERROR sources CSV header does not match data-formats.md")
                errors += 1
            continue

        if not f.endswith(".md"):
            continue
        try:
            text = read_text(f)
        except (OSError, UnicodeDecodeError) as e:
            print(f"{f}: ERROR cannot read: {e}")
            errors += 1
            continue

        if needs_notice(f):
            head = text.splitlines()[:8]
            if not any(marker in ln for ln in head for marker in NOTICE_MARKERS):
                print(f"{f}: ERROR missing simulation notice in first 8 lines")
                errors += 1

        # Quotes inside fenced code blocks (the closing JSON of a post) are data, not citations.
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        for q in re.findall(r'"([^"\n]{0,400})"', prose):
            if q.isascii() and len(q.split()) >= 15:
                print(f"{f}: WARNING long double-quoted passage ({len(q.split())} words)")
                warnings += 1

    if args.strict:
        errors += warnings
        warnings = 0
    print(f"lint: {errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


# ---------------------------------------------------------------------------
# compare
# ---------------------------------------------------------------------------

def diversity(subs, options):
    ids = list(subs)
    total, n = 0.0, 0
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = subs[ids[i]], subs[ids[j]]
            diffs = [abs(overall_score(a, o) - overall_score(b, o)) for o in options
                     if overall_score(a, o) is not None and overall_score(b, o) is not None]
            if diffs:
                total += statistics.mean(diffs)
                n += 1
    return round(total / n, 3) if n else None


def persona_baseline_gap(subs, baseline_subs, options):
    gaps = []
    for o in options:
        pm = [overall_score(d, o) for d in subs.values() if overall_score(d, o) is not None]
        bm = [overall_score(d, o) for d in baseline_subs if overall_score(d, o) is not None]
        if pm and bm:
            gaps.append(abs(statistics.median(pm) - statistics.mean(bm)))
    return round(statistics.mean(gaps), 3) if gaps else None


def interjection_asymmetry(run):
    cruxes_data, err = try_load_json(p(run, "cruxes.json"))
    if err:
        return None
    side_of = {}
    for c in cruxes_data.get("cruxes") or []:
        for k, side in enumerate(c.get("sides") or []):
            for m in side.get("members") or []:
                side_of[(c["id"], m)] = k

    files = glob.glob(p(run, "board", "B", "*", "*interjection*.md")) + \
        glob.glob(p(run, "board", "B", "*", "*插话*.md"))
    per_table = {}
    for f in files:
        table = f.split(os.sep)[-2]
        blk = extract_post_json(read_text(f))
        if not blk:
            continue
        for r in blk.get("responses") or []:
            v = norm_enum(r.get("verdict"), ACCEPT_MAP)
            if v in ("reject", "partial") and (table, r.get("to")) in side_of:
                side = side_of[(table, r.get("to"))]
                per_table.setdefault(table, {}).setdefault(side, 0)
                per_table[table][side] += 1
    shares = {t: round(max(v.values()) / sum(v.values()), 2) for t, v in per_table.items() if sum(v.values()) >= 2}
    return {"per_table": shares, "max": max(shares.values()) if shares else None, "n_interjections": len(files)}


def run_metrics(run, exclude=()):
    rubric, err = try_load_json(p(run, "rubric.json"))
    if err:
        raise ValueError(err)
    options = rubric_options(rubric)
    persona_ids = rubric_personas(rubric).keys()

    r1 = {k: v for k, v in load_submissions(p(run, "r1", "*.json")).items() if k not in exclude}
    r3 = {k: v for k, v in load_submissions(p(run, "r3", "*.json")).items() if k not in exclude}
    b1 = list(load_submissions(p(run, "baselines", "*_r1.json")).values())
    b3 = list(load_submissions(p(run, "baselines", "*_r3.json")).values())

    m = {"run": run, "n_r1": len(r1), "n_r3": len(r3)}
    m["diversity_r1"] = diversity(r1, options)
    m["diversity_r3"] = diversity(r3, options)
    if m["diversity_r1"] and m["diversity_r3"] is not None:
        m["diversity_drop"] = round((m["diversity_r1"] - m["diversity_r3"]) / m["diversity_r1"], 3)
    m["persona_baseline_gap_r1"] = persona_baseline_gap(r1, b1, options)
    m["persona_baseline_gap_r3"] = persona_baseline_gap(r3, b3, options)
    m["null_share_r1"] = (round(sum(1 for d in r1.values() for o in options if overall_score(d, o) is None) /
                                 (len(r1) * len(options)), 3) if r1 and options else None)

    changes = 0
    for pid, d3 in r3.items():
        if pid in r1:
            changes += sum(1 for o in options
                            if overall_score(r1[pid], o) is not None and overall_score(d3, o) is not None
                            and overall_score(r1[pid], o) != overall_score(d3, o))
    m["score_changes"] = changes

    verdicts, searches, urls = {}, 0, set()
    for f in iter_board_files(run, ("A", "B", "C")) + iter_board_files(run, ("overtime",)):
        if post_author(os.path.basename(f), persona_ids) in exclude:
            continue
        blk = extract_post_json(read_text(f))
        if not blk:
            continue
        for r in blk.get("responses") or []:
            v = norm_enum(r.get("verdict"), ACCEPT_MAP)
            if v:
                verdicts[v] = verdicts.get(v, 0) + 1
        for s in blk.get("searches") or []:
            searches += 1
            if isinstance(s, dict) and s.get("url"):
                urls.add(s["url"])
    m["verdicts"] = verdicts
    total_v = sum(verdicts.values())
    m["reject_share"] = round(verdicts.get("reject", 0) / total_v, 3) if total_v else None
    m["debate_searches"], m["debate_unique_urls"] = searches, len(urls)
    m["r1_searches"] = sum(len(d.get("web_searches") or []) for d in r1.values())
    m["interjections"] = interjection_asymmetry(run)

    cond_tally = {}
    for d in (r3 or r1).values():
        for _qid, clist in (d.get("conditions") or {}).items():
            for c in clist:
                cond_tally[c] = cond_tally.get(c, 0) + 1
    m["conditions_r3"] = cond_tally

    pw = {}
    for d in r3.values():
        for x in d.get("pairwise") or []:
            key = f"{x.get('a')}|{x.get('b')}"
            pw.setdefault(key, {"a": 0, "b": 0})
            pw[key]["a" if x.get("pick") == x.get("a") else "b"] += 1
    m["pairwise_r3"] = pw
    return m


def cmd_compare(args):
    exclude = {x for x in (args.exclude.split(",") if args.exclude else []) if x}
    try:
        res = {"A": run_metrics(args.run_a, exclude), "B": run_metrics(args.run_b, exclude),
               "excluded": sorted(exclude)}
    except ValueError as e:
        eprint(f"error: {e}")
        return 2
    save_json(args.out, res)
    for k in ["diversity_r1", "diversity_r3", "diversity_drop", "persona_baseline_gap_r1",
              "persona_baseline_gap_r3", "null_share_r1", "score_changes", "reject_share",
              "r1_searches", "debate_searches", "debate_unique_urls"]:
        print(f"{k}: {res['A'].get(k)} | {res['B'].get(k)}")
    print(f"compare: wrote {args.out}")
    return 0


# ---------------------------------------------------------------------------
# blind / blind-report
# ---------------------------------------------------------------------------

def _blind_key_path(outdir):
    parent = os.path.dirname(outdir.rstrip("/\\")) or "."
    return os.path.join(parent, "blind_key.json")


def cmd_blind(args):
    rng = random.Random(args.seed)
    key = {"seed": args.seed, "changes": {}, "posts": {}}

    items = []
    for run in (args.run_a, args.run_b):
        for f in sorted(glob.glob(p(run, "r3", "*.json"))):
            try:
                data = load_json(f)
            except (OSError, json.JSONDecodeError):
                continue
            pid = os.path.basename(f)[:-5]
            items += [(run, pid, c) for c in data.get("changes") or []]
    rng.shuffle(items)
    rows = []
    for i, (run, pid, c) in enumerate(items, 1):
        item_id = f"R{i:03d}"
        rows.append({"item": item_id, "because": c.get("because"), "why": c.get("why")})
        key["changes"][item_id] = {"run": run, "persona": pid, "option": c.get("option")}
    save_json(os.path.join(args.outdir, "changes.json"), rows)

    posts = []
    for run in (args.run_a, args.run_b):
        for rnd in "ABC":
            fs = sorted(f for f in glob.glob(p(run, "board", rnd, "*", "*.md"))
                        if "interjection" not in f and "插话" not in f)
            posts += [(run, f) for f in rng.sample(fs, min(BLIND_SAMPLE_PER_ROUND, len(fs)))]
    rng.shuffle(posts)
    for i, (run, f) in enumerate(posts, 1):
        item_id = f"P{i:02d}"
        write_text(os.path.join(args.outdir, "posts", f"{item_id}.md"), strip_post(read_text(f)))
        key["posts"][item_id] = {"run": run, "file": os.path.relpath(f, run)}

    key_path = _blind_key_path(args.outdir)
    save_json(key_path, key)
    print(f"blind: {len(rows)} change(s), {len(posts)} post(s) -> {args.outdir} (key: {key_path})")
    return 0


def report_sections(text, sections=None):
    text = re.sub(r"runs/[\w./-]+", "[path]", text)
    text = re.sub(r"(?<![A-Za-z0-9])v[1-9](?![0-9])", "[run]", text)
    if not sections:
        return text
    parts = re.split(r"(?m)^(?=## )", text)
    keep = tuple(s.strip() for s in sections if s.strip())
    if not keep:
        return text
    return "".join(part for part in parts if part.startswith("## ") and part[3:].strip().startswith(keep))


def cmd_blind_report(args):
    rng = random.Random(args.seed)
    sections = args.sections.split(",") if args.sections else None
    pair = [args.report_a, args.report_b]
    rng.shuffle(pair)
    os.makedirs(args.outdir, exist_ok=True)
    texts = {src: report_sections(read_text(src), sections) for src in pair}
    for tag, order in (("1", pair), ("2", pair[::-1])):
        for label, src in zip("AB", order):
            write_text(os.path.join(args.outdir, f"set{tag}_{label}.md"), texts[src])
    key_path = _blind_key_path(args.outdir)
    key, err = try_load_json(key_path)
    if err:
        key = {}
    key["reports"] = {"set1": {"A": pair[0], "B": pair[1]}, "set2": {"A": pair[1], "B": pair[0]}}
    save_json(key_path, key)
    print(f"blind-report: wrote set1/set2 A/B -> {args.outdir} (key: {key_path})")
    return 0


# ---------------------------------------------------------------------------
# privacy-scan
# ---------------------------------------------------------------------------

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PATH_TAIL = r'[^\s)\]}>"\'`,;]+'
USERS_RE = re.compile(r"/Users/" + PATH_TAIL)
UNIX_HOME_RE = re.compile(r"/home/" + PATH_TAIL)
WIN_HOME_RE = re.compile(r'C:\\Users\\' + PATH_TAIL)
NOTION_URL_RE = re.compile(r"https?://[^\s)\]}>\"']*notion\.(?:so|site|com)/[^\s)\]}>\"']*", re.IGNORECASE)
HEX32_RE = re.compile(r"\b[0-9a-f]{32}\b", re.IGNORECASE)
SECRET_PATTERNS = [
    ("secret:sk", re.compile(r"\bsk-[A-Za-z0-9_-]{10,}")),
    ("secret:ghp", re.compile(r"\bghp_[A-Za-z0-9]{20,}")),
    ("secret:github_pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}")),
    ("secret:akia", re.compile(r"\bAKIA[A-Z0-9]{12,}")),
    ("secret:slack", re.compile(r"\bxox[abp]-[A-Za-z0-9-]+")),
    ("secret:private_key", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----")),
]


def mask_match(s):
    s = s.strip()
    n = len(s)
    if n <= 3:
        return "*" * n
    if n <= 6:
        return s[0] + "*" * (n - 1)
    return s[:2] + "*" * (n - 3) + s[-1]


def load_denylist(path):
    rules = []
    with open(path, encoding="utf-8") as fh:
        for i, raw in enumerate(fh, 1):
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            # Inline comments: whitespace followed by "#" ends the entry.
            line = re.split(r"\s+#", line, maxsplit=1)[0].rstrip()
            if not line:
                continue
            if line.startswith("re:"):
                try:
                    rx = re.compile(line[3:], re.IGNORECASE)
                except re.error as e:
                    eprint(f"privacy-scan: bad regex on denylist line {i}: {e}")
                    continue
            else:
                term = line.strip()
                if re.fullmatch(r"[A-Za-z0-9_-]+", term):
                    rx = re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
                else:
                    rx = re.compile(re.escape(term), re.IGNORECASE)
            rules.append((i, rx))
    return rules


def is_binary(path):
    try:
        with open(path, "rb") as fh:
            chunk = fh.read(2048)
        return b"\0" in chunk
    except OSError:
        return True


def iter_scan_targets(paths):
    for item in paths:
        if os.path.isdir(item):
            for root, dirs, files in os.walk(item):
                dirs[:] = [d for d in dirs if d != ".git"]
                for fn in sorted(files):
                    yield os.path.join(root, fn)
        elif os.path.isfile(item):
            yield item


def privacy_scan_file(path, denylist_rules):
    hits = []
    if is_binary(path):
        return hits
    try:
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
    except (UnicodeDecodeError, OSError):
        return hits
    for lineno, line in enumerate(lines, 1):
        for m in EMAIL_RE.finditer(line):
            email = m.group(0)
            local, _, domain = email.partition("@")
            if "noreply" in local.lower() or domain.lower() in ("example.com", "example.org"):
                continue
            hits.append((lineno, f"email ({mask_match(email)})"))
        for rx in (USERS_RE, UNIX_HOME_RE, WIN_HOME_RE):
            for m in rx.finditer(line):
                hits.append((lineno, f"home_path ({mask_match(m.group(0))})"))
        for label, rx in SECRET_PATTERNS:
            for m in rx.finditer(line):
                hits.append((lineno, f"{label} ({mask_match(m.group(0))})"))
        for m in NOTION_URL_RE.finditer(line):
            hits.append((lineno, f"notion_url ({mask_match(m.group(0))})"))
        if any(d in line.lower() for d in ("notion.so", "notion.site", "notion.com")):
            for m in HEX32_RE.finditer(line):
                hits.append((lineno, f"notion_id ({mask_match(m.group(0))})"))
        for dl_lineno, rx in denylist_rules:
            if rx.search(line):
                hits.append((lineno, f"denylist:L{dl_lineno}"))
    return hits


def cmd_privacy_scan(args):
    denylist_rules = []
    denylist_abspath = None
    if args.denylist:
        denylist_abspath = os.path.abspath(args.denylist)
        denylist_rules = load_denylist(args.denylist)

    total = 0
    for target in iter_scan_targets(args.paths):
        norm = target.replace(os.sep, "/")
        if "/.git/" in ("/" + norm) or norm.split("/")[0] == ".git":
            continue
        if denylist_abspath and os.path.abspath(target) == denylist_abspath:
            continue
        for lineno, rule in privacy_scan_file(target, denylist_rules):
            print(f"{target}:{lineno}: {rule}")
            total += 1

    if total:
        eprint(f"privacy-scan: {total} hit(s)")
        return 1
    print("privacy-scan: no hits")
    return 0


# ---------------------------------------------------------------------------
# argparse wiring
# ---------------------------------------------------------------------------

def add_run_arg(sp):
    sp.add_argument("--run", default=None, help="Run directory (default: $RUN environment variable).")


def build_parser():
    parser = argparse.ArgumentParser(
        prog="sim.py",
        description="Helper CLI for the persona-debate protocol. Driven entirely by each run's rubric.json.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("new-run", help="Create a new run folder from templates/run/.")
    sp.add_argument("--slug", required=True)
    sp.add_argument("--date", default=None, help="YYYY-MM-DD; defaults to today.")
    sp.add_argument("--root", default=os.path.join("workspace", "runs"))
    sp.set_defaults(func=cmd_new_run)

    sp = sub.add_parser("new-persona", help="Create a new persona folder from templates/persona/.")
    sp.add_argument("--id", required=True)
    sp.add_argument("--slug", required=True)
    sp.add_argument("--root", default=os.path.join("workspace", "personas"))
    sp.set_defaults(func=cmd_new_persona)

    sp = sub.add_parser("roster", help="Read id/name/aliases from persona card.yaml files into a rubric personas block.")
    sp.add_argument("--personas", nargs="+", required=True, metavar="DIR")
    sp.add_argument("--write", default=None, metavar="RUBRIC", help="Merge into this rubric.json instead of printing.")
    sp.set_defaults(func=cmd_roster)

    sp = sub.add_parser("check", help="Validate r1/ or r3/ submissions against rubric.json.")
    sp.add_argument("round", choices=["r1", "r3"])
    sp.add_argument("--baselines", action="store_true", help="Also validate baselines/*_r1.json or *_r3.json.")
    add_run_arg(sp)
    sp.set_defaults(func=cmd_check)

    sp = sub.add_parser("tables", help="Validate tables.json seating against rubric.json and cruxes.json.")
    add_run_arg(sp)
    sp.set_defaults(func=cmd_tables)

    sp = sub.add_parser("index", help="Generate board/A/INDEX.md: one line per opening post.")
    add_run_arg(sp)
    sp.set_defaults(func=cmd_index)

    sp = sub.add_parser("anon", help="Write anonymized copies of A/B/C posts for blind judging.")
    add_run_arg(sp)
    sp.add_argument("--seed", type=int, default=0)
    sp.set_defaults(func=cmd_anon)

    sp = sub.add_parser("aggregate", help="Write summary.json and summary.md.")
    add_run_arg(sp)
    sp.set_defaults(func=cmd_aggregate)

    sp = sub.add_parser("scan", help="Scan persona cards (and, with --boards, posts) for forbidden words.")
    add_run_arg(sp)
    sp.add_argument("--boards", action="store_true")
    sp.add_argument("--personas", nargs="*", default=None, metavar="DIR")
    sp.set_defaults(func=cmd_scan)

    sp = sub.add_parser("lint", help="Check persona-authored Markdown, filenames, JSON and sources CSVs.")
    sp.add_argument("paths", nargs="+", metavar="PATH")
    sp.add_argument("--strict", action="store_true", help="Treat warnings as errors.")
    sp.set_defaults(func=cmd_lint)

    sp = sub.add_parser("compare", help="Pre-registered cross-run comparison metrics.")
    sp.add_argument("run_a", metavar="RUN_A")
    sp.add_argument("run_b", metavar="RUN_B")
    sp.add_argument("out", metavar="OUT.json")
    sp.add_argument("--exclude", default=None, metavar="IDS", help="Comma-separated persona ids to exclude.")
    sp.set_defaults(func=cmd_compare)

    sp = sub.add_parser("blind", help="Sample material for blind reviews 1/2 from two runs.")
    sp.add_argument("run_a", metavar="RUN_A")
    sp.add_argument("run_b", metavar="RUN_B")
    sp.add_argument("outdir", metavar="OUTDIR")
    sp.add_argument("--seed", type=int, default=0)
    sp.set_defaults(func=cmd_blind)

    sp = sub.add_parser("blind-report", help="Relabel two reports A/B (and the swap) for blind review 3.")
    sp.add_argument("report_a", metavar="REPORT_A")
    sp.add_argument("report_b", metavar="REPORT_B")
    sp.add_argument("outdir", metavar="OUTDIR")
    sp.add_argument("--sections", default=None, metavar="0.,2.,3.",
                     help="Comma-separated heading prefixes to keep; default keeps every section.")
    sp.add_argument("--seed", type=int, default=0)
    sp.set_defaults(func=cmd_blind_report)

    sp = sub.add_parser("privacy-scan", help="Flag emails, home paths, secrets, Notion ids and denylist terms.")
    sp.add_argument("paths", nargs="+", metavar="PATH")
    sp.add_argument("--denylist", default=None, metavar="FILE")
    sp.set_defaults(func=cmd_privacy_scan)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args) or 0


if __name__ == "__main__":
    sys.exit(main())
