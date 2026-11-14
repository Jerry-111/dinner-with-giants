"""Unit-level tests for the pure functions in tools/sim.py.

These load tools/sim.py directly by file path (no package install needed) and
call its functions, rather than going through the command-line interface.
See tests/test_commands.py for subcommand smoke tests.
"""
import argparse
import contextlib
import importlib.util
import io
import os
import shutil
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM_PATH = os.path.join(ROOT, "tools", "sim.py")


def _load_sim():
    spec = importlib.util.spec_from_file_location("sim_under_test_logic", SIM_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sim = _load_sim()


class StatsTests(unittest.TestCase):
    def test_median_iqr_min_max(self):
        s = sim.stats([1, 2, 3, 4])
        self.assertEqual(s["n"], 4)
        self.assertEqual(s["median"], 2.5)
        self.assertEqual(s["min"], 1)
        self.assertEqual(s["max"], 4)
        self.assertEqual(s["q1"], 1.75)
        self.assertEqual(s["q3"], 3.25)

    def test_single_value(self):
        s = sim.stats([7])
        self.assertEqual(s, {"n": 1, "median": 7, "q1": 7, "q3": 7, "iqr": 0, "min": 7, "max": 7})

    def test_empty_and_non_numeric_are_none(self):
        self.assertIsNone(sim.stats([]))
        self.assertIsNone(sim.stats([None, None, "x"]))

    def test_booleans_are_not_treated_as_numbers(self):
        # JSON "true"/"false" must never be counted as scores.
        s = sim.stats([5, True, False])
        self.assertEqual(s["n"], 1)
        self.assertEqual(s["median"], 5)


class RankTests(unittest.TestCase):
    def test_ties_broken_by_smaller_iqr(self):
        table = {
            "A": {"median": 5, "iqr": 3},
            "B": {"median": 5, "iqr": 1},
            "C": {"median": 7, "iqr": 2},
        }
        r = sim.rank(table)
        self.assertEqual(r, {"C": 1, "B": 2, "A": 3})

    def test_missing_stats_are_skipped(self):
        r = sim.rank({"A": {"median": 5, "iqr": 1}, "B": None})
        self.assertEqual(list(r), ["A"])


class CheckSubmissionTests(unittest.TestCase):
    def _rubric(self, **extra):
        r = {
            "options": {"O1": "first", "O2": "second"},
            "dimensions": {"d1": "dim one", "d2": "dim two"},
            "scale": {"min": 0, "max": 10},
            "levers": {"L1": "lever one", "L2": "lever two"},
            "pairwise": [["O1", "O2"]],
            "r1_requirements": {"paths_for_user": [1, 2], "cruxes": 1},
        }
        r.update(extra)
        return r

    def _submission(self):
        return {
            "options": {
                "O1": {"d1": 5, "d2": 5, "overall": 5},
                "O2": {"d1": 6, "d2": 6, "overall": 6},
            },
            "levers": {"L1": 60, "L2": 40},
            "paths_for_user": [{"name": "x"}],
            "cruxes": [{"question": "q"}],
            "pairwise": [{"a": "O1", "b": "O2", "pick": "O1"}],
        }

    def test_clean_r1_submission_has_no_issues(self):
        self.assertEqual(sim.check_submission(self._submission(), self._rubric(), "r1"), [])

    def test_missing_option_is_flagged(self):
        sub = self._submission()
        del sub["options"]["O2"]
        issues = sim.check_submission(sub, self._rubric(), "r1")
        self.assertIn("missing option O2", issues)

    def test_out_of_range_score_is_flagged(self):
        sub = self._submission()
        sub["options"]["O1"]["d1"] = 99
        issues = sim.check_submission(sub, self._rubric(), "r1")
        self.assertTrue(any("O1.d1" in i for i in issues))

    def test_null_score_is_always_allowed(self):
        sub = self._submission()
        sub["options"]["O1"]["d1"] = None
        issues = sim.check_submission(sub, self._rubric(), "r1")
        self.assertEqual(issues, [])

    def test_levers_must_sum_to_exactly_100(self):
        sub = self._submission()
        sub["levers"] = {"L1": 60, "L2": 30}
        issues = sim.check_submission(sub, self._rubric(), "r1")
        self.assertTrue(any("levers sum to" in i for i in issues))

    def test_levers_check_skipped_when_rubric_has_no_levers(self):
        sub = self._submission()
        sub["levers"] = {"L1": 1}
        rubric = self._rubric()
        del rubric["levers"]
        issues = sim.check_submission(sub, rubric, "r1")
        self.assertEqual(issues, [])

    def test_paths_for_user_length_enforced(self):
        sub = self._submission()
        sub["paths_for_user"] = []
        issues = sim.check_submission(sub, self._rubric(), "r1")
        self.assertTrue(any("paths_for_user" in i for i in issues))

    def test_cruxes_length_only_checked_on_r1(self):
        sub = self._submission()
        sub["cruxes"] = []
        self.assertTrue(any("cruxes" in i for i in sim.check_submission(sub, self._rubric(), "r1")))
        self.assertFalse(any("cruxes" in i for i in sim.check_submission(sub, self._rubric(), "r3")))

    def test_missing_pairwise_pick_is_flagged(self):
        sub = self._submission()
        sub["pairwise"] = []
        issues = sim.check_submission(sub, self._rubric(), "r1")
        self.assertIn("pairwise O1 vs O2 has no pick", issues)

    def test_r3_requires_changes_key_present(self):
        sub = self._submission()
        self.assertIn("missing changes", sim.check_submission(sub, self._rubric(), "r3"))
        sub["changes"] = []
        self.assertNotIn("missing changes", sim.check_submission(sub, self._rubric(), "r3"))

    def test_short_option_does_not_require_dimensions(self):
        rubric = self._rubric()
        rubric["short_options"] = ["O2"]
        sub = self._submission()
        sub["options"]["O2"] = {"overall": 6, "one_line": "short"}
        self.assertEqual(sim.check_submission(sub, rubric, "r1"), [])


class SeatingTests(unittest.TestCase):
    """Exercises cmd_tables' seating rules directly against tiny throwaway run dirs."""

    def _build_run(self, tmp, not_independent=None, side_a=("P1", "P2"), side_b=("P3", "P4"), seats_per_persona=1):
        rubric = {
            "options": {"O1": "x", "O2": "y"},
            "seating": {"table_size": [4, 4], "seats_per_persona": seats_per_persona},
        }
        if not_independent:
            rubric["not_independent"] = not_independent
        sim.save_json(os.path.join(tmp, "rubric.json"), rubric)
        sim.save_json(os.path.join(tmp, "cruxes.json"), {"cruxes": [{
            "id": "X1", "question": "q", "options": ["O1", "O2"],
            "sides": [
                {"label": "side a", "members": list(side_a)},
                {"label": "side b", "members": list(side_b)},
            ],
        }]})
        sim.save_json(os.path.join(tmp, "tables.json"), {
            "tables": [{"id": "X1", "crux": "X1", "members": ["P1", "P2", "P3", "P4"]}]
        })

    def _run_tables(self, tmp):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = sim.cmd_tables(argparse.Namespace(run=tmp))
        return code, buf.getvalue()

    def test_clean_seating_has_no_problems(self):
        tmp = tempfile.mkdtemp()
        try:
            self._build_run(tmp, side_a=("P1",), side_b=("P3",))
            code, out = self._run_tables(tmp)
            self.assertEqual(code, 0)
            self.assertIn("0 problem(s)", out)
        finally:
            shutil.rmtree(tmp)

    def test_not_independent_group_cannot_be_sole_representation_of_a_side(self):
        tmp = tempfile.mkdtemp()
        try:
            # P1 and P2 are not independent of each other and are the only two
            # members representing "side a" at the table.
            self._build_run(tmp, not_independent=[["P1", "P2"]])
            code, out = self._run_tables(tmp)
            self.assertEqual(code, 1)
            self.assertIn("not-independent group", out)
        finally:
            shutil.rmtree(tmp)

    def test_single_representative_from_a_group_is_not_flagged(self):
        tmp = tempfile.mkdtemp()
        try:
            # Only P1 (not P2) sits on "side a", so the not_independent pair
            # never doubles up on one side.
            self._build_run(tmp, not_independent=[["P1", "P2"]], side_a=("P1",), side_b=("P3", "P4"))
            code, out = self._run_tables(tmp)
            self.assertEqual(code, 0)
        finally:
            shutil.rmtree(tmp)

    def test_seats_per_persona_mismatch_is_flagged(self):
        tmp = tempfile.mkdtemp()
        try:
            self._build_run(tmp, side_a=("P1",), side_b=("P3",), seats_per_persona=2)
            code, out = self._run_tables(tmp)
            self.assertEqual(code, 1)
            self.assertIn("expected 2", out)
        finally:
            shutil.rmtree(tmp)


class PrivacyScanTests(unittest.TestCase):
    def test_mask_match_never_returns_the_full_string(self):
        for s in ("ab", "abcdef", "abcdefghij", "a"):
            masked = sim.mask_match(s)
            self.assertEqual(len(masked), len(s))
            if len(s) > 3:
                self.assertNotEqual(masked, s)

    def _write(self, tmp, name, text):
        path = os.path.join(tmp, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path

    def test_email_detected_but_noreply_and_example_domains_allowed(self):
        tmp = tempfile.mkdtemp()
        try:
            # Assembled at runtime (not one contiguous literal) so this fixture does
            # not trip `tools/sim.py privacy-scan .` over its own source file.
            flagged_email = "real.person" + "@gmail.com"
            path = self._write(
                tmp, "f.txt",
                f"contact a.b@example.com and {flagged_email} and noreply@anthropic.com\n",
            )
            hits = sim.privacy_scan_file(path, [])
            self.assertEqual(len(hits), 1)
            self.assertTrue(hits[0][1].startswith("email ("))
            # The real address is never printed in full.
            self.assertNotIn(flagged_email, hits[0][1])
        finally:
            shutil.rmtree(tmp)

    def test_home_paths_secrets_and_notion_ids_detected_and_masked(self):
        tmp = tempfile.mkdtemp()
        try:
            # Each pattern is assembled at runtime from two pieces (not one
            # contiguous literal) so this fixture does not trip
            # `tools/sim.py privacy-scan .` over its own source file.
            unix_home = "/Users/" + "alice/project/notes.txt"
            win_home = "C:\\Users\\" + "alice\\Documents\\notes.txt"
            sk_key = "sk-" + "abcdefghijklmnopqrstuvwx"
            ghp_key = "ghp_" + "abcdefghijklmnopqrstuvwxyz0123456789"
            notion_url = "https://www.notion" + ".so/space/Page-1234567890abcdef1234567890abcdef"
            path = self._write(
                tmp, "f.txt",
                f"{unix_home}\n{win_home}\n{sk_key}\n{ghp_key}\n{notion_url}\n",
            )
            hits = sim.privacy_scan_file(path, [])
            rule_names = sorted(r.split(" ")[0] for _, r in hits)
            self.assertEqual(
                rule_names,
                ["home_path", "home_path", "notion_id", "notion_url", "secret:ghp", "secret:sk"],
            )
            for _, rule in hits:
                self.assertNotIn("alice", rule)
                self.assertNotIn("abcdefghijklmnopqrstuvwx", rule)
        finally:
            shutil.rmtree(tmp)

    def test_denylist_plain_term_is_case_insensitive_with_word_boundary(self):
        tmp = tempfile.mkdtemp()
        try:
            deny = self._write(tmp, "deny.txt", "# comment\nSecretName\nre:Token-\\d+\n")
            target = self._write(
                tmp, "f.txt",
                "SecretName appears here.\n"
                "unrelatedSecretNameSuffix should not match on word boundary.\n"
                "Token-99 is here.\n",
            )
            rules = sim.load_denylist(deny)
            hits = sim.privacy_scan_file(target, rules)
            lines_hit = sorted(ln for ln, _ in hits)
            self.assertEqual(lines_hit, [1, 3])
            for _, rule in hits:
                self.assertTrue(rule.startswith("denylist:L"))
        finally:
            shutil.rmtree(tmp)


class LintNoticeDetectionTests(unittest.TestCase):
    def test_files_that_attribute_views_need_the_notice(self):
        for path in (
            "run/r1/P1.md",
            "run/r3/P1.md",
            "run/board/A/X1/P1.md",
            "run/board/overtime/X1/2_P1.md",
            "run/judge/X1.md",
            "run/board/summary/X1.md",
            "run/board/summary_full/X1.md",
            "personas/P1_demo/dossier.md",
            "personas/P1_demo/views.md",
        ):
            self.assertTrue(sim.needs_notice(path), path)

    def test_baseline_files_are_exempt(self):
        self.assertFalse(sim.needs_notice("run/baselines/Z1_r1.md"))
        self.assertFalse(sim.needs_notice("run/baselines/Z1_r3.md"))

    def test_unrelated_files_do_not_need_the_notice(self):
        self.assertFalse(sim.needs_notice("run/summary.md"))
        self.assertFalse(sim.needs_notice("run/judge/anon/A/X1/P01.md"))
        self.assertFalse(sim.needs_notice("run/report.md"))

    def test_lint_flags_a_missing_notice(self):
        tmp = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(tmp, "r1"))
            with open(os.path.join(tmp, "r1", "P1.md"), "w", encoding="utf-8") as fh:
                fh.write("# No notice\n\nJust text, no simulation notice anywhere near the top.\n")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = sim.cmd_lint(argparse.Namespace(paths=[tmp], strict=False))
            self.assertEqual(code, 1)
            self.assertIn("missing simulation notice", buf.getvalue())
        finally:
            shutil.rmtree(tmp)

    def test_lint_accepts_the_chinese_notice(self):
        tmp = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(tmp, "r1"))
            with open(os.path.join(tmp, "r1", "P1.md"), "w", encoding="utf-8") as fh:
                fh.write("# Title\n\n基于公开材料的模拟，不是本人言论。\n")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = sim.cmd_lint(argparse.Namespace(paths=[tmp], strict=False))
            self.assertEqual(code, 0)
        finally:
            shutil.rmtree(tmp)


class EnumNormalizationTests(unittest.TestCase):
    def test_accept_map_covers_english_and_chinese(self):
        self.assertEqual(sim.norm_enum("accept", sim.ACCEPT_MAP), "accept")
        self.assertEqual(sim.norm_enum("接受", sim.ACCEPT_MAP), "accept")
        self.assertEqual(sim.norm_enum("reject", sim.ACCEPT_MAP), "reject")
        self.assertEqual(sim.norm_enum("不接受", sim.ACCEPT_MAP), "reject")
        self.assertEqual(sim.norm_enum("partial", sim.ACCEPT_MAP), "partial")
        self.assertEqual(sim.norm_enum("部分接受", sim.ACCEPT_MAP), "partial")
        self.assertIsNone(sim.norm_enum(None, sim.ACCEPT_MAP))

    def test_result_map_covers_english_and_chinese(self):
        self.assertEqual(sim.norm_enum("supports", sim.RESULT_MAP), "supports")
        self.assertEqual(sim.norm_enum("支持", sim.RESULT_MAP), "supports")
        self.assertEqual(sim.norm_enum("refutes", sim.RESULT_MAP), "refutes")
        self.assertEqual(sim.norm_enum("反驳", sim.RESULT_MAP), "refutes")
        self.assertEqual(sim.norm_enum("unclear", sim.RESULT_MAP), "unclear")
        self.assertEqual(sim.norm_enum("不清楚", sim.RESULT_MAP), "unclear")

    def test_position_map_covers_english_and_chinese(self):
        self.assertEqual(sim.norm_enum("for", sim.POSITION_MAP), "for")
        self.assertEqual(sim.norm_enum("支持", sim.POSITION_MAP), "for")
        self.assertEqual(sim.norm_enum("against", sim.POSITION_MAP), "against")
        self.assertEqual(sim.norm_enum("反对", sim.POSITION_MAP), "against")
        self.assertEqual(sim.norm_enum("conditional", sim.POSITION_MAP), "conditional")
        self.assertEqual(sim.norm_enum("附条件", sim.POSITION_MAP), "conditional")
        self.assertEqual(sim.norm_enum("有条件", sim.POSITION_MAP), "conditional")


class PostParsingTests(unittest.TestCase):
    def test_post_author_handles_all_filename_shapes(self):
        ids = {"P1", "P2", "P3", "P4"}
        self.assertEqual(sim.post_author("P3.md", ids), "P3")
        self.assertEqual(sim.post_author("P3_interjection.md", ids), "P3")
        self.assertEqual(sim.post_author("P3_\u63d2\u8bdd.md", ids), "P3")
        self.assertEqual(sim.post_author("2_P3.md", ids), "P3")

    def test_extract_post_json_uses_the_last_fenced_block(self):
        text = 'body\n```json\n{"a": 1}\n```\nmore text\n```json\n{"a": 2}\n```\n'
        self.assertEqual(sim.extract_post_json(text), {"a": 2})

    def test_extract_post_json_falls_back_to_trailing_bare_object(self):
        text = 'body text with no fence\n{"a": 3}'
        self.assertEqual(sim.extract_post_json(text), {"a": 3})

    def test_extract_post_json_none_when_absent(self):
        self.assertIsNone(sim.extract_post_json("just prose, no json at all"))


if __name__ == "__main__":
    unittest.main()
