# Retrieval A/B Bridge

This short bridge exists to prevent the talk from sounding like a retreat from RAG engineering.

## Point for the talk

The team did not jump to LLM Wiki because retrieval was ignored. A retrieval backend comparison had already been performed. In that historical test, both backends reached the same reported answer proxy score on a small corpus, while latency and cost differed.

## Reported historical numbers

Source: `../teams-agent/docs/retrieval-ab-test-report.md` as previously summarized in this talk repository.

| Metric | Hybrid RAG | Gemini File Search |
|---|---:|---:|
| Test date | 2026-08-07 | 2026-08-07 |
| Questions | 30 | 30 |
| Documents | 19 | 19 |
| Model | `gemini-3.5-flash-lite` | `gemini-3.5-flash-lite` |
| Top-k | 4 | 4 |
| P50 latency | 3.00 s | 5.71 s |
| P95 latency | 4.07 s | 7.15 s |
| Average cost / query | US$0.001059 | US$0.001804 |
| Reported answer proxy | 25 / 25 | 25 / 25 |
| No-answer cases | 5 / 5 | 5 / 5 |

## How to use this in the talk

Do not use this as a universal benchmark. The corpus was small, the quality metric was a report-specific proxy, and this was not the LLM Wiki experiment.

Use it only to say:

> We had already optimized and compared retrieval backends. When retrieval quality is no longer the only question, architecture decisions move to latency, cost, operational control, and eventually knowledge lifecycle.

## Bridge sentence

> The next bottleneck was not “can we retrieve something?” but “what exactly should the system treat as true when several retrieved sources are all valid under different conditions?”
