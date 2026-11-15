"""Subcommand-level (smoke and integration) tests for tools/sim.py.

Each test copies tests/fixtures/mini_run/ into a fresh temp directory so
commands that write into a run (index, anon, aggregate, ...) never mutate the
checked-in fixture. See tests/test_logic.py for pure-function unit tests.
"""
import argparse
import contextlib
import importlib.util
import io
import json
import os
import shutil
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM_PATH = os.path.join(ROOT, "tools", "sim.py")
FIXTURE = os.path.join(ROOT, "tests", "fixtures", "mini_run")


def _load_sim():
    spec = importlib.util.spec_from_file_location("sim_under_test_commands", SIM_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sim = _load_sim()


class RunCommandTestCase(unittest.TestCase):
    """Base class: sets up self.run as a disposable copy of the mini_run fixture."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.run = os.path.join(self.tmp, "run")
        shutil.copytree(FIXTURE, self.run)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_cli(self, argv):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = sim.main(argv)
        return code, buf.getvalue()


class CheckCommandTests(RunCommandTestCase):
    def test_check_r1_clean_including_baseline(self):
        code, out = self.run_cli(["check", "r1", "--run", self.run, "--baselines"])
        self.assertEqual(code, 0)
        self.assertIn("5 file(s), 5 clean", out)

    def test_check_r3_clean_including_baseline(self):
        code, out = self.run_cli(["check", "r3", "--run", self.run, "--baselines"])
        self.assertEqual(code, 0)
        self.assertIn("5 file(s), 5 clean", out)

    def test_check_without_baselines_flag_skips_baseline_files(self):
        code, out = self.run_cli(["check", "r1", "--run", self.run])
        self.assertEqual(code, 0)
        self.assertIn("4 file(s), 4 clean", out)

    def test_check_flags_a_broken_lever_allocation(self):
        path = os.path.join(self.run, "r1", "P1.json")
        data = sim.load_json(path)
        data["levers"]["L1"] = 10
        sim.save_json(path, data)
        code, out = self.run_cli(["check", "r1", "--run", self.run])
        self.assertEqual(code, 1)
        self.assertIn("levers sum to", out)

    def test_check_requires_run(self):
        code, out = self.run_cli(["check", "r1"])
        self.assertEqual(code, 2)


class TablesCommandTests(RunCommandTestCase):
    def test_tables_clean(self):
        code, out = self.run_cli(["tables", "--run", self.run])
        self.assertEqual(code, 0)
        self.assertIn("2 table(s); 8 seat(s); 0 problem(s)", out)


class IndexCommandTests(RunCommandTestCase):
    def test_index_writes_bilingual_claim_table(self):
        code, out = self.run_cli(["index", "--run", self.run])
        self.assertEqual(code, 0)
        text = sim.read_text(os.path.join(self.run, "board", "A", "INDEX.md"))
        self.assertIn("P1 Persona One", text)
        self.assertIn("O1's early impact is real", text)
        self.assertIn("O2 在适配度上明显优于 O1", text)


class AnonCommandTests(RunCommandTestCase):
    def test_anon_hides_display_names_and_writes_a_key(self):
        code, out = self.run_cli(["anon", "--run", self.run, "--seed", "0"])
        self.assertEqual(code, 0)
        key = sim.load_json(os.path.join(self.run, "judge", "anon_key.json"))
        self.assertEqual(set(key), {"P1", "P2", "P3", "P4"})
        self.assertEqual(sorted(key.values()), ["P01", "P02", "P03", "P04"])
        anon_dir = os.path.join(self.run, "judge", "anon", "A", "X1")
        self.assertEqual(len(os.listdir(anon_dir)), 4)
        for fn in os.listdir(anon_dir):
            text = sim.read_text(os.path.join(anon_dir, fn))
            self.assertNotIn("Persona One", text)
            self.assertNotIn("Persona Two", text)
            self.assertNotIn("Persona Three", text)
            self.assertNotIn("Persona Four", text)
            self.assertNotIn("> Stance", text)


class AggregateCommandTests(RunCommandTestCase):
    def test_aggregate_matches_hand_verified_values(self):
        code, out = self.run_cli(["aggregate", "--run", self.run])
        self.assertEqual(code, 0)
        summary = sim.load_json(os.path.join(self.run, "summary.json"))

        self.assertEqual(summary["n_r1"], 4)
        self.assertEqual(summary["n_r3"], 4)
        self.assertEqual(summary["n_changed_scores"], 2)
        self.assertEqual(summary["verdicts"], {"accept": 3, "reject": 5, "partial": 1})
        self.assertEqual(summary["n_searches_in_debate"], 1)
        self.assertEqual(len(summary["source_challenges"]), 1)
        self.assertEqual(len(summary["retracted"]), 1)

        self.assertEqual(summary["empty_concessions"], [
            {"id": "P2", "table": "X1", "post": "B/X1/P1", "verdict": "accept", "options": ["O1", "O2"]}
        ])
        self.assertEqual(summary["intent_vs_actual"], [
            {"id": "P4", "option": "O3", "intended": -1, "actual": 0}
        ])
        self.assertEqual(summary["persuaded_by"], {"P2": 2, "P4": 1, "P1": 1})

        # Chinese verdict "接受" on P2's C-round post must normalize into the
        # same bucket as the English "accept" verdicts above.
        self.assertEqual(summary["verdicts"]["accept"], 3)

        self.assertEqual(summary["overall_r1"]["O1"]["median"], 6.5)
        self.assertEqual(summary["overall_r3"]["O4"]["median"], 5.5)
        self.assertEqual(summary["groups_r3"]["all"]["O1"], summary["overall_r3"]["O1"]["median"])

        self.assertEqual(summary["pairwise"]["r1"]["O1 vs O2"]["win_rate"], {"O1": 0.5, "O2": 0.5})
        self.assertEqual(summary["pairwise"]["r3"]["O1 vs O2"]["win_rate"], {"O1": 0.5, "O2": 0.5})

        self.assertEqual(summary["questions_r1"]["Q1"]["positions"],
                          {"for": 1, "against": 1, "conditional": 2})
        self.assertEqual(summary["conditions"]["r1"]["Q1"], {"C1": 2, "C2": 2})

        self.assertEqual(summary["persona_minus_baseline"]["Z1"]["mean_abs_gap"], 0.25)

        self.assertEqual(summary["judge"]["n_posts"], 6)
        self.assertEqual(summary["judge"]["flags"], {"source_challenged": 1, "retracted": 1})

        # O4 is a short option with no dimension scores, so it cannot be weighted.
        self.assertIsNone(summary["weighted"]["equal"]["stats"]["O4"])

        md = sim.read_text(os.path.join(self.run, "summary.md"))
        self.assertIn("## Debate", md)
        self.assertIn("## Judge scorecards", md)

    def test_aggregate_requires_run(self):
        code, out = self.run_cli(["aggregate"])
        self.assertEqual(code, 2)


class ScanCommandTests(RunCommandTestCase):
    def test_scan_boards_is_clean_on_the_fixture(self):
        code, out = self.run_cli(["scan", "--run", self.run, "--boards"])
        self.assertEqual(code, 0)
        self.assertIn("no hits", out)

    def test_scan_flags_a_forbidden_word_in_a_persona_card(self):
        persona_dir = os.path.join(self.tmp, "P9_demo")
        os.makedirs(persona_dir)
        with open(os.path.join(persona_dir, "card.yaml"), "w", encoding="utf-8") as fh:
            fh.write("id: P9\nname: Persona Nine\nlens: We give everyone a discount.\n")
        code, out = self.run_cli(["scan", "--run", self.run, "--personas", persona_dir])
        self.assertEqual(code, 1)
        self.assertIn("discount", out)


class DenylistInlineCommentTests(unittest.TestCase):
    def test_inline_comments_are_ignored(self):
        import tempfile
        d = tempfile.mkdtemp()
        deny = os.path.join(d, "deny.txt")
        with open(deny, "w", encoding="utf-8") as fh:
            fh.write("re:\\bAcmeSecret\\b      # a private project name\n")
            fh.write("zebra-team   # plain term with a comment\n")
        target = os.path.join(d, "doc.md")
        with open(target, "w", encoding="utf-8") as fh:
            fh.write("We met the AcmeSecret people.\nThe zebra-team agreed.\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = sim.main(["privacy-scan", target, "--denylist", deny])
        out = buf.getvalue()
        self.assertEqual(code, 1)
        self.assertIn("denylist:L1", out)
        self.assertIn("denylist:L2", out)


class LintCommandTests(RunCommandTestCase):
    def test_lint_fixture_has_only_warnings(self):
        # One long prose quote warns; a long string inside a post's closing JSON does not.
        code, out = self.run_cli(["lint", self.run])
        self.assertEqual(code, 0)
        self.assertIn("0 error(s)", out)
        self.assertIn("1 warning(s)", out)

    def test_lint_strict_turns_warnings_into_errors(self):
        code, out = self.run_cli(["lint", self.run, "--strict"])
        self.assertEqual(code, 1)
        self.assertIn("1 error(s)", out)
        self.assertIn("0 warning(s)", out)

    def test_lint_ignores_long_strings_inside_fenced_json(self):
        path = os.path.join(self.run, "board", "A", "X1", "P1.md")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        long_value = " ".join(["word"] * 20)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text + '\n```json\n{"why": "' + long_value + '"}\n```\n')
        code, out = self.run_cli(["lint", self.run])
        self.assertEqual(code, 0)
        self.assertNotIn("P1.md: WARNING", out.replace("r1/P1.md", ""))

    def test_lint_warns_on_legacy_non_ascii_interjection_filename(self):
        src = os.path.join(self.run, "board", "B", "X1", "P4_interjection.md")
        dst = os.path.join(self.run, "board", "B", "X1", "P2_插话.md")
        shutil.copyfile(src, dst)
        code, out = self.run_cli(["lint", self.run])
        self.assertEqual(code, 0)
        self.assertIn("legacy interjection", out)

    def test_lint_errors_on_other_non_ascii_filenames(self):
        src = os.path.join(self.run, "board", "B", "X1", "P4_interjection.md")
        dst = os.path.join(self.run, "board", "B", "X1", "P4_一.md")
        shutil.copyfile(src, dst)
        code, out = self.run_cli(["lint", self.run])
        self.assertEqual(code, 1)
        self.assertIn("ERROR non-ASCII filename", out)

    def test_lint_on_examples_folder_that_does_not_exist_reports_missing(self):
        code, out = self.run_cli(["lint", os.path.join(self.tmp, "does-not-exist")])
        self.assertEqual(code, 1)


class PrivacyScanCommandTests(RunCommandTestCase):
    def test_privacy_scan_clean_on_the_fixture(self):
        code, out = self.run_cli(["privacy-scan", self.run])
        self.assertEqual(code, 0)
        self.assertIn("no hits", out)

    def test_privacy_scan_exits_1_on_a_real_hit(self):
        # Assembled at runtime so this fixture does not trip
        # `tools/sim.py privacy-scan .` over its own source file.
        flagged_email = "definitely.not.a.test" + "@gmail.com"
        bad = os.path.join(self.tmp, "leak.md")
        with open(bad, "w", encoding="utf-8") as fh:
            fh.write(f"my personal email is {flagged_email}\n")
        code, out = self.run_cli(["privacy-scan", bad])
        self.assertEqual(code, 1)
        self.assertNotIn(flagged_email, out)


class RosterCommandTests(unittest.TestCase):
    def test_roster_prints_personas_block(self):
        tmp = tempfile.mkdtemp()
        try:
            persona_dir = os.path.join(tmp, "P9_demo")
            os.makedirs(persona_dir)
            with open(os.path.join(persona_dir, "card.yaml"), "w", encoding="utf-8") as fh:
                fh.write("id: P9\nname: Persona Nine\naliases: [Nine, \"The Ninth\"]\n")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = sim.main(["roster", "--personas", persona_dir])
            self.assertEqual(code, 0)
            data = json.loads(buf.getvalue())
            self.assertEqual(data["personas"]["P9"]["name"], "Persona Nine")
            self.assertEqual(data["personas"]["P9"]["aliases"], ["Nine", "The Ninth"])
        finally:
            shutil.rmtree(tmp)

    def test_roster_write_merges_into_existing_rubric(self):
        tmp = tempfile.mkdtemp()
        try:
            persona_dir = os.path.join(tmp, "P9_demo")
            os.makedirs(persona_dir)
            with open(os.path.join(persona_dir, "card.yaml"), "w", encoding="utf-8") as fh:
                fh.write("id: P9\nname: Persona Nine\n")
            rubric_path = os.path.join(tmp, "rubric.json")
            sim.save_json(rubric_path, {"options": {"O1": "x"}, "personas": {"P1": {"name": "Persona One"}}})
            code, out = 0, ""
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = sim.main(["roster", "--personas", persona_dir, "--write", rubric_path])
            self.assertEqual(code, 0)
            rubric = sim.load_json(rubric_path)
            self.assertEqual(set(rubric["personas"]), {"P1", "P9"})
        finally:
            shutil.rmtree(tmp)

    def test_roster_regex_fallback_matches_pyyaml_path(self):
        tmp = tempfile.mkdtemp()
        try:
            card = os.path.join(tmp, "card.yaml")
            with open(card, "w", encoding="utf-8") as fh:
                fh.write("id: P9\nname: Persona Nine\naliases:\n  - Nine\n  - The Ninth\n")
            with_yaml = sim.read_card_fields(card)
            original = sim.HAS_YAML
            sim.HAS_YAML = False
            try:
                without_yaml = sim.read_card_fields(card)
            finally:
                sim.HAS_YAML = original
            self.assertEqual(with_yaml, without_yaml)
            self.assertEqual(without_yaml, {"id": "P9", "name": "Persona Nine", "aliases": ["Nine", "The Ninth"]})
        finally:
            shutil.rmtree(tmp)


class NewRunCommandTests(unittest.TestCase):
    def test_new_run_works_even_with_an_empty_template_folder(self):
        tmp = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(tmp, "templates", "run"))
            cwd = os.getcwd()
            os.chdir(tmp)
            try:
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    code = sim.main(["new-run", "--slug", "demo", "--date", "2026-01-01", "--root", "runs"])
                output = buf.getvalue()
            finally:
                os.chdir(cwd)
            self.assertEqual(code, 0)
            self.assertIn("note:", output)
            run_dir = os.path.join(tmp, "runs", "2026-01-01_demo")
            for d in sim.RUN_LAYOUT_DIRS:
                self.assertTrue(os.path.isdir(os.path.join(run_dir, d)), d)
        finally:
            shutil.rmtree(tmp)

    def test_new_run_copies_existing_templates(self):
        tmp = tempfile.mkdtemp()
        try:
            template_dir = os.path.join(tmp, "templates", "run")
            os.makedirs(template_dir)
            with open(os.path.join(template_dir, "scope.md"), "w", encoding="utf-8") as fh:
                fh.write("# Scope\n")
            cwd = os.getcwd()
            os.chdir(tmp)
            try:
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    code = sim.main(["new-run", "--slug", "demo", "--date", "2026-01-01", "--root", "runs"])
            finally:
                os.chdir(cwd)
            self.assertEqual(code, 0)
            self.assertTrue(os.path.isfile(os.path.join(tmp, "runs", "2026-01-01_demo", "scope.md")))
        finally:
            shutil.rmtree(tmp)

    def test_new_run_refuses_to_overwrite_a_non_empty_folder(self):
        tmp = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(tmp, "templates", "run"))
            cwd = os.getcwd()
            os.chdir(tmp)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    sim.main(["new-run", "--slug", "demo", "--date", "2026-01-01", "--root", "runs"])
                buf = io.StringIO()
                with contextlib.redirect_stderr(buf):
                    code = sim.main(["new-run", "--slug", "demo", "--date", "2026-01-01", "--root", "runs"])
            finally:
                os.chdir(cwd)
            self.assertEqual(code, 1)
            self.assertIn("already exists", buf.getvalue())
        finally:
            shutil.rmtree(tmp)


class NewPersonaCommandTests(unittest.TestCase):
    def test_new_persona_copies_templates_and_replaces_id_placeholder(self):
        tmp = tempfile.mkdtemp()
        try:
            template_dir = os.path.join(tmp, "templates", "persona")
            os.makedirs(template_dir)
            with open(os.path.join(template_dir, "card.yaml"), "w", encoding="utf-8") as fh:
                fh.write("id: <ID>\nname: Replace me\n")
            cwd = os.getcwd()
            os.chdir(tmp)
            try:
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    code = sim.main(["new-persona", "--id", "P9", "--slug", "demo", "--root", "personas"])
            finally:
                os.chdir(cwd)
            self.assertEqual(code, 0)
            out_card = sim.read_text(os.path.join(tmp, "personas", "P9_demo", "card.yaml"))
            self.assertIn("id: P9", out_card)
            self.assertNotIn("<ID>", out_card)
        finally:
            shutil.rmtree(tmp)


class CompareAndBlindCommandTests(RunCommandTestCase):
    def setUp(self):
        super().setUp()
        self.run_b = os.path.join(self.tmp, "run_b")
        shutil.copytree(FIXTURE, self.run_b)

    def test_compare_writes_metrics_for_both_runs(self):
        out_path = os.path.join(self.tmp, "compare.json")
        code, out = self.run_cli(["compare", self.run, self.run_b, out_path, "--exclude", "P4"])
        self.assertEqual(code, 0)
        data = sim.load_json(out_path)
        self.assertEqual(data["excluded"], ["P4"])
        self.assertEqual(data["A"]["score_changes"], 2)
        self.assertEqual(data["B"]["score_changes"], 2)
        self.assertEqual(data["A"]["n_r1"], 3)  # P4 excluded from the 4 personas

    def test_blind_samples_small_runs_without_crashing(self):
        outdir = os.path.join(self.tmp, "blind_material")
        code, out = self.run_cli(["blind", self.run, self.run_b, outdir, "--seed", "1"])
        self.assertEqual(code, 0)
        self.assertTrue(os.path.isdir(os.path.join(outdir, "posts")))
        key = sim.load_json(os.path.join(self.tmp, "blind_key.json"))
        self.assertIn("changes", key)
        self.assertIn("posts", key)
        # No interjection file should ever be sampled into the blind material.
        for fn in os.listdir(os.path.join(outdir, "posts")):
            text = sim.read_text(os.path.join(outdir, "posts", fn))
            self.assertNotIn("# X1", text)  # header line is stripped by strip_post


class BlindReportCommandTests(unittest.TestCase):
    def test_blind_report_filters_sections_and_redacts_run_markers(self):
        tmp = tempfile.mkdtemp()
        try:
            a = os.path.join(tmp, "a.md")
            b = os.path.join(tmp, "b.md")
            with open(a, "w", encoding="utf-8") as fh:
                fh.write("## 0. Summary\nFrom runs/some-earlier-run and v3.\n\n## 1. Skip me\nnope\n")
            with open(b, "w", encoding="utf-8") as fh:
                fh.write("## 0. Summary\nFrom runs/some-other-run and v5.\n\n## 1. Skip me\nnope\n")
            outdir = os.path.join(tmp, "out")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = sim.main(["blind-report", a, b, outdir, "--sections", "0.", "--seed", "1"])
            self.assertEqual(code, 0)
            for fn in ("set1_A.md", "set1_B.md", "set2_A.md", "set2_B.md"):
                text = sim.read_text(os.path.join(outdir, fn))
                self.assertNotIn("Skip me", text)
                self.assertNotIn("runs/", text)
                self.assertNotIn("v3", text)
                self.assertNotIn("v5", text)
            key = sim.load_json(os.path.join(tmp, "blind_key.json"))
            self.assertIn("reports", key)
        finally:
            shutil.rmtree(tmp)

    def test_blind_report_keeps_everything_when_sections_omitted(self):
        tmp = tempfile.mkdtemp()
        try:
            a = os.path.join(tmp, "a.md")
            b = os.path.join(tmp, "b.md")
            with open(a, "w", encoding="utf-8") as fh:
                fh.write("## 0. Summary\nA text.\n\n## 1. Other\nmore A.\n")
            with open(b, "w", encoding="utf-8") as fh:
                fh.write("## 0. Summary\nB text.\n\n## 1. Other\nmore B.\n")
            outdir = os.path.join(tmp, "out")
            with contextlib.redirect_stdout(io.StringIO()):
                code = sim.main(["blind-report", a, b, outdir, "--seed", "1"])
            self.assertEqual(code, 0)
            text = sim.read_text(os.path.join(outdir, "set1_A.md"))
            self.assertIn("## 1. Other", text)
        finally:
            shutil.rmtree(tmp)


class HelpAndArgParsingTests(unittest.TestCase):
    def test_top_level_help_exits_cleanly(self):
        with self.assertRaises(SystemExit) as ctx:
            with contextlib.redirect_stdout(io.StringIO()):
                sim.main(["--help"])
        self.assertEqual(ctx.exception.code, 0)

    def test_missing_subcommand_is_an_argparse_error(self):
        with self.assertRaises(SystemExit):
            with contextlib.redirect_stderr(io.StringIO()):
                sim.main([])


class QuotesCommandTests(unittest.TestCase):
    HEADER = ("evidence_id,claim,type,author_or_org,source_title,url,published_date,accessed_date,"
              "source_family,supports_or_challenges,limitations\n")

    def _persona(self, dossier, ids=("P1-E01", "P1-E02")):
        d = tempfile.mkdtemp()
        folder = os.path.join(d, "P1_test")
        os.makedirs(folder)
        with open(os.path.join(folder, "sources.csv"), "w", encoding="utf-8") as fh:
            fh.write(self.HEADER)
            for eid in ids:
                fh.write(f"{eid},a claim,primary,Someone,A title,https://example.org/{eid},2020,2026-11-14,own,supports,\n")
        with open(os.path.join(folder, "dossier.md"), "w", encoding="utf-8") as fh:
            fh.write(dossier)
        return folder

    def _run(self, folder):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = sim.main(["quotes", folder])
        return code, buf.getvalue()

    def test_short_sourced_quote_passes(self):
        folder = self._persona('He said "measure twice, cut once" [quoted, P1-E01].\n')
        code, out = self._run(folder)
        self.assertEqual(code, 0)
        self.assertIn("1 checked, 0 error(s), 0 warning(s)", out)

    def test_long_quote_is_an_error(self):
        long_q = " ".join(["word"] * 16)
        folder = self._persona(f'She wrote "{long_q}" [quoted, P1-E01].\n')
        code, out = self._run(folder)
        self.assertEqual(code, 1)
        self.assertIn("ERROR quote of 16 words", out)

    def test_unknown_evidence_id_is_an_error(self):
        folder = self._persona('He said "short line here" [quoted, P1-E09].\n')
        code, out = self._run(folder)
        self.assertEqual(code, 1)
        self.assertIn("P1-E09 is not in", out)

    def test_one_quote_per_source_holds_across_files(self):
        folder = self._persona('"first line" [quoted, P1-E01].\n')
        with open(os.path.join(folder, "views.md"), "w", encoding="utf-8") as fh:
            fh.write('"another line" [quoted, P1-E01].\n')
        code, out = self._run(folder)
        self.assertIn("two different quotes cite P1-E01", out)

    def test_shortened_repeat_of_one_quote_is_not_two_quotes(self):
        folder = self._persona('"the solidity or appositeness of my findings" [quoted, P1-E01]; later '
                               '"the solidity ... of my findings" [quoted, P1-E01].\n')
        code, out = self._run(folder)
        self.assertNotIn("two different quotes", out)

    def test_two_quotes_from_one_source_warn(self):
        folder = self._persona('"first line" [quoted, P1-E01] and "second line" [quoted, P1-E01].\n')
        code, out = self._run(folder)
        self.assertEqual(code, 0)
        self.assertIn("two different quotes cite P1-E01", out)

    def test_code_formatted_label_with_an_id_is_checked(self):
        folder = self._persona('He wrote "a short line" `[quoted, P1-E01]`.\n')
        code, out = self._run(folder)
        self.assertEqual(code, 0)
        self.assertIn("1 checked", out)

    def test_labels_written_as_code_and_paraphrase_are_skipped(self):
        folder = self._persona("Labels: `[quoted]` marks a quote. A paraphrase [quoted, P1-E02] has no marks.\n")
        code, out = self._run(folder)
        self.assertEqual(code, 0)
        self.assertIn("0 checked", out)


if __name__ == "__main__":
    unittest.main()
