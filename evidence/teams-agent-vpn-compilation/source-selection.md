# Source Selection — Teams Agent VPN / FortiClient Cluster

The following source documents should be exported from the local `teams-agent/data/sources/` directory before running Knowledge Compilation.

## Required local source files

| Priority | Source title | Evidence in `teams-agent` eval | Compilation role |
|---:|---|---|---|
| 1 | `VPN常見Q&A問答` | `retrieval_eval_set.json` includes `vpn-455`, `vpn-14`, `vpn-8`, `vpn-license`, `vpn-token-otp`, `no-answer-vpn-619`. | Primary VPN troubleshooting source; contains documented and undocumented boundary cases. |
| 2 | `登入 FortiClient 出現錯訊` | `retrieval_eval_v3_blind.json` accepts this title for `-455`, password expiry, and FortiClient error questions. | FortiClient-specific companion source; prevents over-generalizing from broad VPN FAQ. |
| 3 | `VPN國外連線短暫申請` | `retrieval_eval_set.json` includes `vpn-overseas`; blind eval also has overseas short-query variants. | Process / approval / escalation knowledge. |
| 4 | `內網筆電 VPN 連線問題` | Blind eval includes internal-laptop VPN questions with acceptable related citation to VPN FAQ. | Environment-specific troubleshooting branch. |
| 5 | `VPN 跳板機連線異常` | Blind eval includes jump-host VPN questions and multi-turn follow-ups. | Adjacent but distinguishable VPN domain; useful for hard-negative discrimination. |
| Optional | `分公司CS團隊VPN連線可使用權限列表` | `retrieval_eval_set.json` includes ACL coverage-gap cases. | Do not use as proof of true ACL allow/deny until metadata has real restrictions. |
| Sample | `data/sources.sample/vpn-password-lockout.md` | Public sample source with owner/version/effectiveDate/reviewDate/audience. | Safe demo sample; useful for showing metadata shape, but not enough for the full regression slice. |

## Why not use CS VPN ACL as primary evidence

The existing eval explicitly notes that the shipped corpus lacks real `allowed_groups` restrictions for the CS VPN ACL case. It only verifies that empty `allowed_groups` means visible to all groups. It is useful as a gap disclosure, not as a strong ACL proof.

## Export target

Copy the required source files into a local run directory, for example:

```text
llm-wiki-architecture-talk/evidence/teams-agent-vpn-compilation/input-sources/
  vpn-common-qa.md
  forticlient-errors.md
  vpn-overseas-temporary-access.md
  internal-laptop-vpn.md
  vpn-jump-host.md
```

Do not commit confidential production documents unless they are sanitized. If the documents contain internal URLs, names, or operational contacts, redact them and preserve only the knowledge structure needed for the demo.
