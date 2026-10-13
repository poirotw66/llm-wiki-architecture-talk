#!/usr/bin/env python3
"""Score the revised candidate against the unchanged eleven-case v2 contract."""

import datetime
import hashlib
import json
import pathlib

from score_v2 import citation_checks


ROOT = pathlib.Path(__file__).resolve().parents[2]
RUNS = pathlib.Path(__file__).resolve().parent
CONTRACT_PATH = ROOT / "contracts/regression-cases-v2.json"
RESULT_PATH = ROOT / "records/repair-revalidation-v2.json"
FROZEN_CONTRACT_SHA256 = "fb33ef8439a87f840bc2c690d80c2856625f963e4c8f08f47c3c0b8a5356b443"


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if RESULT_PATH.exists():
        raise SystemExit("Revised scoring output already exists; preserve the first run.")
    if sha256(CONTRACT_PATH) != FROZEN_CONTRACT_SHA256:
        raise SystemExit("Frozen v2 contract hash changed.")
    contract = json.loads(CONTRACT_PATH.read_text())
    old_result = json.loads((ROOT / "records/regression-results-v2.json").read_text())
    query_dir = RUNS / "revised-query"
    judge_dir = RUNS / "revised-judge"
    query_receipt = json.loads((query_dir / "receipt.json").read_text())
    judge_receipt = json.loads((judge_dir / "receipt.json").read_text())
    for receipt, run_dir in ((query_receipt, query_dir), (judge_receipt, judge_dir)):
        assert receipt["exit_code"] == 0 and receipt["tool_item_count"] == 0
        assert receipt["prompt_sha256"] == sha256(run_dir / "prompt.txt")
        assert receipt["schema_sha256"] == sha256(run_dir / "response-schema.json")
        assert receipt["response_sha256"] == sha256(run_dir / "response.json")
    answers = json.loads((query_dir / "response.json").read_text())["answers"]
    reviews = json.loads((judge_dir / "response.json").read_text())["reviews"]
    judge_inputs = json.loads((judge_dir / "inputs.json").read_text())
    original_judge_inputs = json.loads((RUNS / "updated-judge/inputs.json").read_text())
    assert judge_inputs["rubric"] == original_judge_inputs["rubric"]
    assert judge_inputs["canonical_sources"] == original_judge_inputs["canonical_sources"]
    assert judge_inputs["actual_answers"] == answers
    assert [answer["case_id"] for answer in answers] == [case["id"] for case in contract["cases"]]
    assert [review["case_id"] for review in reviews] == [case["id"] for case in contract["cases"]]
    source_ids = set(contract["phases"]["updated"]["source_ids"])
    cases = []
    for case, answer, review in zip(contract["cases"], answers, reviews):
        expected = case["expected"]["updated"]
        criterion_ids = ["route", "first_action", "missing_fields", "citation_alignment"]
        criterion_ids += [f"include-{n}" for n in range(1, len(expected["must_include"]) + 1)]
        criterion_ids += [f"prohibit-{n}" for n in range(1, len(expected["must_not"]) + 1)]
        assert [check["criterion_id"] for check in review["checks"]] == criterion_ids
        quote_issues = []
        for check in review["checks"]:
            if check["passed"] and check["criterion_id"] in {"route", "first_action", "missing_fields"} | {f"include-{n}" for n in range(1, len(expected["must_include"]) + 1)}:
                if check["evidence_quote"] and check["evidence_quote"] not in answer["answer"]:
                    quote_issues.append(check["criterion_id"])
        citation = citation_checks(answer, expected, judge_inputs["canonical_sources"], source_ids)
        route_match = answer["route"] == expected["route"]
        action_match = review["canonical_first_action"] == expected["first_action"] and next(check for check in review["checks"] if check["criterion_id"] == "first_action")["passed"]
        semantic_passed = all(check["passed"] for check in review["checks"])
        status = "PASS" if route_match and action_match and semantic_passed and citation["passed"] and not quote_issues else "FAIL"
        cases.append({
            "case_id": case["id"],
            "status": status,
            "expected_route": expected["route"],
            "actual_route": answer["route"],
            "expected_first_action": expected["first_action"],
            "actual_first_action_label": answer["first_action"],
            "canonical_first_action": review["canonical_first_action"],
            "route_match": route_match,
            "first_action_semantic_match": action_match,
            "semantic_criteria_passed": semantic_passed,
            "criteria": review["checks"],
            "citation_checks": citation,
            "review_quote_issues": quote_issues,
            "answer_sha256": hashlib.sha256(json.dumps(answer, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
            "raw_response_path": str((query_dir / "response.json").relative_to(ROOT)),
            "human_review": "pending",
        })
    result = {
        "run_id": "synthetic-enterprise-repair-revalidation-v2-20261013",
        "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "completed-pending-human-content-review",
        "contract_id": contract["contract_id"],
        "contract_sha256": FROZEN_CONTRACT_SHA256,
        "repaired_bundle_path": "ops/purpose.md",
        "repaired_bundle_sha256": sha256(ROOT / "repair-v2/ops/purpose.md"),
        "scenario_date": contract["phases"]["updated"]["scenario_date"],
        "model": "gpt-6.1-sol",
        "reasoning_effort": "high",
        "answer_sampling": "one eleven-case batch for the revised candidate",
        "reference_answers_supplied_to_answer_model": False,
        "human_content_review": "pending",
        "baseline_passed": old_result["summary"]["baseline"]["passed"],
        "updated_passed": old_result["summary"]["updated"]["passed"],
        "revised_passed": sum(item["status"] == "PASS" for item in cases),
        "revised_failed": sum(item["status"] == "FAIL" for item in cases),
        "cases": cases,
        "model_runs": {"revised-query": query_receipt, "revised-judge": judge_receipt},
        "limitations": [
            "Synthetic teaching corpus only; no active Wiki import, retrieval or serving query was performed.",
            "A single batched answer sample is descriptive, not a reliability estimate.",
            "The frozen v2 contract was known while writing the general repair rule, so this is not an unseen-case generalization test.",
            "The baseline and updated phases differ in both knowledge snapshot and scenario date; no architecture comparison is implied.",
            "Model review and agent inspection are not human content-owner approval.",
        ],
    }
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"baseline": result["baseline_passed"], "updated": result["updated_passed"], "revised": result["revised_passed"], "failed_ids": [item["case_id"] for item in cases if item["status"] == "FAIL"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
