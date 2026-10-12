#!/usr/bin/env python3
"""Combine frozen v2 criteria, independent reviews, and exact citation checks."""

import datetime
import hashlib
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[2]
RUNS = pathlib.Path(__file__).resolve().parent
CONTRACT_PATH = ROOT / "contracts/regression-cases-v2.json"
OUTPUT_PATH = ROOT / "records/regression-results-v2.json"


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def citation_checks(answer: dict, expected: dict, canonical_sources: list[dict], allowed_ids: set[str]) -> dict:
    canonical = {re.search(r"^sourceId: (SRC-\d+)$", source["content"], re.MULTILINE).group(1): source for source in canonical_sources}
    cited_ids = []
    invalid = []
    for citation in answer["citations"]:
        source_id = citation["source_id"]
        cited_ids.append(source_id)
        source = canonical.get(source_id)
        if source_id not in allowed_ids or source is None:
            invalid.append({"source_id": source_id, "reason": "source not available in phase"})
        elif citation["path"] != source["path"]:
            invalid.append({"source_id": source_id, "reason": "noncanonical source path"})
        elif not citation["quote"] or citation["quote"] not in source["content"]:
            invalid.append({"source_id": source_id, "reason": "quote is not an exact canonical excerpt"})
    cited = set(cited_ids)
    inline = set(re.findall(r"\[(SRC-\d+)\]", answer["answer"]))
    missing_required = sorted(set(expected["required_source_ids"]) - cited)
    alternatives = []
    for requirement in expected.get("citation_requirements", []):
        accepted = set(requirement["any_of_source_ids"])
        alternatives.append({
            "claim": requirement["claim"],
            "any_of_source_ids": sorted(accepted),
            "satisfied_by": sorted(accepted & cited),
            "passed": bool(accepted & cited),
        })
    return {
        "required_source_ids": expected["required_source_ids"],
        "cited_source_ids": sorted(cited),
        "inline_source_ids": sorted(inline),
        "missing_required_source_ids": missing_required,
        "alternative_requirements": alternatives,
        "invalid_citations": invalid,
        "inline_citation_mismatch": sorted(cited ^ inline),
        "passed": not (missing_required or invalid or cited ^ inline or any(not item["passed"] for item in alternatives)),
    }


def main() -> None:
    contract = json.loads(CONTRACT_PATH.read_text())
    contract_sha = sha256(CONTRACT_PATH)
    result = {
        "run_id": "synthetic-enterprise-regression-v2-20261012",
        "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "completed-pending-human-content-review",
        "contract_id": contract["contract_id"],
        "contract_sha256": contract_sha,
        "method": "Fresh answer inference, separate model rubric review, deterministic exact citation checks, maintainer review",
        "model": "gpt-6.1-sol",
        "reasoning_effort": "high",
        "answer_sampling": "one eleven-case batch per phase",
        "reference_answers_supplied_to_answer_model": False,
        "human_content_review": "pending",
        "cases": [],
        "model_runs": {},
        "limitations": [
            "Synthetic teaching corpus only; no production Wiki import or serving query was performed.",
            "One answer sample per phase is descriptive, not a reliability estimate.",
            "Semantic checks use a model reviewer and maintainer audit; human content-owner review is pending.",
        ],
    }
    for phase in ("baseline", "updated"):
        query_dir = RUNS / f"{phase}-query"
        judge_dir = RUNS / f"{phase}-judge"
        query_receipt = json.loads((query_dir / "receipt.json").read_text())
        judge_receipt = json.loads((judge_dir / "receipt.json").read_text())
        assert query_receipt["exit_code"] == judge_receipt["exit_code"] == 0
        assert query_receipt["tool_item_count"] == judge_receipt["tool_item_count"] == 0
        result["model_runs"][f"{phase}-query"] = query_receipt
        result["model_runs"][f"{phase}-judge"] = judge_receipt
        answers = json.loads((query_dir / "response.json").read_text())["answers"]
        reviews = json.loads((judge_dir / "response.json").read_text())["reviews"]
        sources = json.loads((judge_dir / "inputs.json").read_text())["canonical_sources"]
        assert [answer["case_id"] for answer in answers] == [case["id"] for case in contract["cases"]]
        assert [review["case_id"] for review in reviews] == [case["id"] for case in contract["cases"]]
        for case, answer, review in zip(contract["cases"], answers, reviews):
            expected = case["expected"][phase]
            expected_criterion_ids = ["route", "first_action", "missing_fields", "citation_alignment"]
            expected_criterion_ids += [f"include-{n}" for n in range(1, len(expected["must_include"]) + 1)]
            expected_criterion_ids += [f"prohibit-{n}" for n in range(1, len(expected["must_not"]) + 1)]
            assert [check["criterion_id"] for check in review["checks"]] == expected_criterion_ids, (phase, case["id"])
            citation = citation_checks(answer, expected, sources, set(contract["phases"][phase]["source_ids"]))
            route_match = answer["route"] == expected["route"]
            action_match = review["canonical_first_action"] == expected["first_action"] and next(check for check in review["checks"] if check["criterion_id"] == "first_action")["passed"]
            semantic_passed = all(check["passed"] for check in review["checks"])
            result["cases"].append({
                "phase": phase,
                "case_id": case["id"],
                "status": "PASS" if route_match and action_match and semantic_passed and citation["passed"] else "FAIL",
                "expected_route": expected["route"],
                "actual_route": answer["route"],
                "expected_first_action": expected["first_action"],
                "actual_first_action_label": answer["first_action"],
                "canonical_first_action": review["canonical_first_action"],
                "first_action_semantic_match": action_match,
                "route_match": route_match,
                "semantic_criteria_passed": semantic_passed,
                "criteria": review["checks"],
                "citation_checks": citation,
                "answer_sha256": hashlib.sha256(json.dumps(answer, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
                "raw_response_path": str(query_dir.relative_to(ROOT) / "response.json"),
                "human_review": "pending",
            })
    result["summary"] = {
        phase: {
            "case_count": sum(item["phase"] == phase for item in result["cases"]),
            "passed": sum(item["phase"] == phase and item["status"] == "PASS" for item in result["cases"]),
            "failed": sum(item["phase"] == phase and item["status"] == "FAIL" for item in result["cases"]),
            "route_and_action_matches": sum(item["phase"] == phase and item["route_match"] and item["first_action_semantic_match"] for item in result["cases"]),
        }
        for phase in ("baseline", "updated")
    }
    assert not OUTPUT_PATH.exists()
    OUTPUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["summary"], ensure_ascii=False))


if __name__ == "__main__":
    main()
