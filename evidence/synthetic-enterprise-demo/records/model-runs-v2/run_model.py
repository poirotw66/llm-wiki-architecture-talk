#!/usr/bin/env python3
"""Run one isolated synthetic regression inference and save its receipt."""

import datetime
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile
import time


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in {
        "baseline-query",
        "updated-query",
        "baseline-judge",
        "updated-judge",
    }:
        raise SystemExit("Usage: run_model.py <baseline-query|updated-query|baseline-judge|updated-judge>")

    run_dir = pathlib.Path(__file__).resolve().parent / sys.argv[1]
    prompt_path = run_dir / "prompt.txt"
    schema_path = run_dir / "response-schema.json"
    response_path = run_dir / "response.json"
    events_path = run_dir / "events.jsonl"
    stderr_path = run_dir / "stderr.txt"
    receipt_path = run_dir / "receipt.json"
    if any(path.exists() for path in (response_path, events_path, receipt_path)):
        raise SystemExit("This run already has output; preserve it and create a new run directory.")

    argv = [
        "codex", "exec", "--ignore-user-config", "--ignore-rules", "--ephemeral",
        "--skip-git-repo-check", "--sandbox", "read-only", "--json", "--color", "never",
        "-c", 'model="gpt-6.1-sol"', "-c", 'model_reasoning_effort="high"',
        "--output-schema", str(schema_path), "--output-last-message", str(response_path), "-",
    ]
    started = datetime.datetime.now(datetime.timezone.utc)
    start = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="llm-wiki-v2-neutral-") as neutral_dir:
        result = subprocess.run(
            argv,
            cwd=neutral_dir,
            input=prompt_path.read_bytes(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=900,
            check=False,
        )
    finished = datetime.datetime.now(datetime.timezone.utc)
    events_path.write_bytes(result.stdout)
    stderr_path.write_bytes(result.stderr)
    usage = []
    tool_types = []
    parse_errors = []
    for line_number, line in enumerate(result.stdout.splitlines(), 1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            parse_errors.append(f"line {line_number}: {exc}")
            continue
        if event.get("type") == "turn.completed":
            usage.append(event.get("usage", {}))
        item = event.get("item", {})
        if isinstance(item, dict) and item.get("type") in {"command_execution", "mcp_tool_call", "web_search"}:
            tool_types.append(item["type"])
    receipt = {
        "started_at": started.isoformat(),
        "finished_at": finished.isoformat(),
        "elapsed_seconds": round(time.monotonic() - start, 3),
        "argv": argv,
        "cwd_mode": "empty-neutral-temporary-directory",
        "requested_model": "gpt-6.1-sol",
        "reasoning_effort": "high",
        "exit_code": result.returncode,
        "prompt_sha256": sha256(prompt_path),
        "schema_sha256": sha256(schema_path),
        "response_sha256": sha256(response_path) if response_path.exists() else None,
        "event_usage": usage,
        "tool_item_count": len(tool_types),
        "tool_item_types": tool_types,
        "event_parse_errors": parse_errors,
        "cost_usd": None,
        "exact_serving_snapshot": None,
    }
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"run": sys.argv[1], "exit_code": result.returncode, "elapsed_seconds": receipt["elapsed_seconds"], "tool_item_count": len(tool_types)}))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
