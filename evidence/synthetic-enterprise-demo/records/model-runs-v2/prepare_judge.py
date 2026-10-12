#!/usr/bin/env python3
"""Prepare v2 rubric reviews from frozen criteria and saved answers."""

import json
import pathlib
import shutil
import sys


ROOT = pathlib.Path(__file__).resolve().parents[2]
RUNS = pathlib.Path(__file__).resolve().parent


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"baseline", "updated"}:
        raise SystemExit("Usage: prepare_judge.py <baseline|updated>")
    phase = sys.argv[1]
    contract = json.loads((ROOT / "contracts/regression-cases-v2.json").read_text())
    answers = json.loads((RUNS / f"{phase}-query/response.json").read_text())["answers"]
    expected_ids = [case["id"] for case in contract["cases"]]
    assert [answer["case_id"] for answer in answers] == expected_ids
    old_judge = ROOT / f"records/model-runs/{phase}-judge"
    canonical_sources = json.loads((old_judge / "inputs.json").read_text())["canonical_sources"]
    assert len(canonical_sources) == len(contract["phases"][phase]["source_ids"])

    rubric = []
    for case in contract["cases"]:
        expected = case["expected"][phase]
        criteria = [
            {"id": "route", "statement": f"The reported route and user-facing answer must follow {expected['route']}."},
            {"id": "first_action", "statement": f"The actually recommended first action must mean {expected['first_action']}; map equivalent English labels explicitly."},
            {"id": "missing_fields", "statement": f"Ask for all minimum missing fields {expected['missing_fields']} without re-asking supplied fields. Source-supported additional diagnostic fields are allowed."},
            {"id": "citation_alignment", "statement": "Cited canonical passages must support material user-facing claims within their scope. Source-ID completeness and exact excerpt matching are checked separately."},
        ]
        criteria.extend(
            {"id": f"include-{number}", "statement": statement}
            for number, statement in enumerate(expected["must_include"], 1)
        )
        criteria.extend(
            {"id": f"prohibit-{number}", "statement": f"The following behavior must be ABSENT: {statement}"}
            for number, statement in enumerate(expected["must_not"], 1)
        )
        rubric.append({"case_id": case["id"], "query": case["query"], "context": case["context"], "criteria": criteria})

    judge_dir = RUNS / f"{phase}-judge"
    judge_dir.mkdir(exist_ok=False)
    inputs = {
        "phase": phase,
        "scenario_date": contract["phases"][phase]["scenario_date"],
        "rubric": rubric,
        "actual_answers": answers,
        "canonical_sources": canonical_sources,
    }
    (judge_dir / "inputs.json").write_text(json.dumps(inputs, ensure_ascii=False) + "\n")
    shutil.copy2(old_judge / "response-schema.json", judge_dir / "response-schema.json")
    prefix = (old_judge / "prompt.txt").read_text().split("INPUT\n", 1)[0]
    prefix = prefix.replace(
        "For positive checks evidence_quote must be an exact substring from the actual answer or one of its reported citation quotes; negative absence may use an empty quote with a reason.",
        "For include, route, first_action and missing_fields checks, evidence_quote must be an exact substring of the user-facing answer; citation excerpts cannot satisfy user-facing requirements. For citation_alignment, an actual answer or reported citation quote may be used. For negative absence checks, an empty quote with a reason is allowed.",
    )
    prefix += "Apply the frozen v2 criteria exactly. Review the answer text and reported fields separately from source excerpts. A source excerpt does not become part of the user-facing answer.\n"
    (judge_dir / "prompt.txt").write_text(prefix + "INPUT\n" + json.dumps(inputs, ensure_ascii=False) + "\n")
    print(f"Prepared {phase} judge for {len(rubric)} cases")


if __name__ == "__main__":
    main()
