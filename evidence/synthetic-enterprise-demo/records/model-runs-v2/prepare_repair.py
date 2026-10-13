#!/usr/bin/env python3
"""Build a revised query from one knowledge overlay and the frozen v2 inputs."""

import hashlib
import json
import pathlib
import shutil
import sys


ROOT = pathlib.Path(__file__).resolve().parents[2]
RUNS = pathlib.Path(__file__).resolve().parent
CONTRACT = ROOT / "contracts/regression-cases-v2.json"
FROZEN_CONTRACT_SHA256 = "fb33ef8439a87f840bc2c690d80c2856625f963e4c8f08f47c3c0b8a5356b443"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_prompt(original_dir: pathlib.Path, target_dir: pathlib.Path, inputs: dict) -> None:
    target_dir.mkdir(exist_ok=False)
    shutil.copy2(original_dir / "response-schema.json", target_dir / "response-schema.json")
    (target_dir / "inputs.json").write_text(json.dumps(inputs, ensure_ascii=False) + "\n")
    prefix = (original_dir / "prompt.txt").read_text().split("INPUT\n", 1)[0]
    (target_dir / "prompt.txt").write_text(prefix + "INPUT\n" + json.dumps(inputs, ensure_ascii=False) + "\n")


def prepare_query() -> None:
    if digest(CONTRACT.read_bytes()) != FROZEN_CONTRACT_SHA256:
        raise SystemExit("Frozen v2 contract hash changed; stop before inference.")
    original = RUNS / "updated-query"
    inputs = json.loads((original / "inputs.json").read_text())
    contract = json.loads(CONTRACT.read_text())
    if inputs["scenario_date"] != contract["phases"]["updated"]["scenario_date"]:
        raise SystemExit("Scenario date differs from the frozen updated phase.")
    if [case["id"] for case in inputs["cases"]] != [case["id"] for case in contract["cases"]]:
        raise SystemExit("Question IDs differ from the frozen contract.")
    revised = ROOT / "repair-v2/ops/purpose.md"
    original_purpose = ROOT / "updated-v2/ops/purpose.md"
    content = revised.read_text()
    if content == original_purpose.read_text():
        raise SystemExit("Repair overlay contains no change.")
    changed = []
    for item in inputs["knowledge_bundle"]:
        if digest(item["content"].encode()) != item["sha256"]:
            raise SystemExit(f"Original bundle digest mismatch: {item['path']}")
        if item["path"] == "ops/purpose.md":
            if item["content"] != original_purpose.read_text():
                raise SystemExit("Original purpose does not match the saved updated bundle.")
            item["content"] = content
            item["sha256"] = digest(content.encode())
            changed.append(item["path"])
    if changed != ["ops/purpose.md"]:
        raise SystemExit(f"Expected exactly one changed bundle item, got {changed}.")
    write_prompt(original, RUNS / "revised-query", inputs)
    print(json.dumps({"contract_sha256": FROZEN_CONTRACT_SHA256, "changed_bundle_paths": changed, "scenario_date": inputs["scenario_date"], "cases": len(inputs["cases"])}, ensure_ascii=False))


def prepare_judge() -> None:
    query_dir = RUNS / "revised-query"
    receipt = json.loads((query_dir / "receipt.json").read_text())
    if receipt["exit_code"] != 0 or receipt["tool_item_count"] != 0:
        raise SystemExit("Revised query did not complete without tools.")
    original = RUNS / "updated-judge"
    inputs = json.loads((original / "inputs.json").read_text())
    answers = json.loads((query_dir / "response.json").read_text())["answers"]
    contract = json.loads(CONTRACT.read_text())
    if [answer["case_id"] for answer in answers] != [case["id"] for case in contract["cases"]]:
        raise SystemExit("Revised answer IDs differ from the frozen contract.")
    inputs["actual_answers"] = answers
    write_prompt(original, RUNS / "revised-judge", inputs)
    print(json.dumps({"review_cases": len(answers), "rubric_cases": len(inputs["rubric"]), "scenario_date": inputs["scenario_date"]}, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"query", "judge"}:
        raise SystemExit("Usage: prepare_repair.py <query|judge>")
    if sys.argv[1] == "query":
        prepare_query()
    else:
        prepare_judge()
