---
title: credactor v2.6.0
url: https://kitploit.com/en/posts/github-rxb06-credactor-v260
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:57:16.199437
---

# credactor v2.6.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9024/3abc948c69d942141474c93431f182cf98a738ebbd43f94eef8f92fda2498f18.png)

New releaseAug 22, 2026

# credactor v2.6.0

Static credential scanner that detects and redacts hardcoded secrets in source code, replacing them with safe sentinels or environment variable references for CI/CD pipelines.

Share

[![PyPI](https://img.shields.io/pypi/v/credactor)](https://pypi.org/project/credactor/)
[![CI](https://github.com/rxb06/credactor/actions/workflows/ci.yml/badge.svg)](https://github.com/rxb06/credactor/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/licence-Apache%202.0-blue)](https://github.com/rxb06/credactor/blob/main/LICENSE)

# Credactor

**Find the secret. Fix it. Commit clean.**

Secret scanners are good at sounding the alarm and not much help putting it out. They hand you a list of leaked credentials and leave the cleanup to you. Credactor closes the loop: it finds a hardcoded secret and rewrites it in place, so a leak goes from detection to fix in a single command.

Keeping credentials out of source code is a baseline security practice, not an optional one. Credactor makes that baseline cheap to hold, on your machine before a commit or in CI before a merge. Run it on its own, or alongside the scanners you already trust.

![Credactor: scan, redact, commit clean](https://assets.kitploit.com/production/public/readmes/9024/3abc948c69d942141474c93431f182cf98a738ebbd43f94eef8f92fda2498f18.png)

root@kitploit:~

```
# Credactor finds this:
db_password = "h8Tq2vKp9mRz4Wd"

# By default it rewrites the secret as a sentinel that fails loudly at runtime:
db_password = "REDACTED_BY_CREDACTOR"

# With --replace-with env, it writes a reference that reads from the environment:
db_password = os.environ["DB_PASSWORD"]
```

> Redaction rewrites files in your **working tree**. If a secret has already been committed, rotate the key and scrub history as well (for example, with `git filter-repo`). Rewriting a file is not a substitute for revoking a leaked credential.

---

## Why Credactor

* **Redaction, not just detection.** Most scanners stop at the finding. Credactor replaces the secret in place: a loud `REDACTED_BY_CREDACTOR` sentinel that fails at runtime by default, or a language-aware environment-variable reference (Python, JavaScript/TypeScript, Go, Java/Kotlin, Ruby, PHP, and shell) such as `os.environ["KEY"]`. The replacement is valid code. If the file does not already include the matching import (for example `import os`), add it.
* **Safe by default.** Atomic writes, automatic `.bak` backups, symlink-boundary and file-permission guards, and full-secret masking in every output. If a safe backup cannot be written, Credactor skips the file rather than rewrite it blind, and a crash mid-write leaves the original intact.
* **Zero runtime dependencies.** Pure Python 3.11+ standard library, plus an optional extra for non-UTF-8 encodings.
* **Built for the pipeline.** SARIF output for GitHub Code Scanning, a read-only `--ci` gate with precise exit codes, a pre-commit hook (beta), and ingestion of Gitleaks or TruffleHog reports (BETA, with more on the way). Detect with Gitleaks or TruffleHog, remediate with Credactor.

## Install

root@kitploit:~

```
pip install credactor
```

Requires Python 3.11+. No other dependencies. Runs on Linux, macOS, and
Windows (CI-tested on Linux and Windows).

From source:

root@kitploit:~

```
git clone https://github.com/rxb06/credactor.git
cd credactor
pip install -e .
```

`credactor` then works from any directory.

## Quick start

> Run `--dry-run` first and review the findings before redacting. False positives are possible, and under `--fix-all` a false positive gets rewritten. Suppress known-safe values with `# credactor:ignore` or a `.credactorignore` entry.

root@kitploit:~

```
credactor --dry-run .                 # scan, change nothing
credactor .                           # scan, then redact interactively (y/n per finding)
credactor --fix-all .                 # redact everything after one confirmation
credactor --fix-all --yes .           # redact non-interactively (CI / scripts)
credactor --ci .                      # read-only gate: exit 1 on findings
credactor --replace-with env .        # redact to env-var references instead of the sentinel
```

### Pre-commit hook (beta)

> Hook integration is in beta. Run `credactor --dry-run .` manually before relying on it alone.

root@kitploit:~

```
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/rxb06/credactor
    rev: v2.5.0   # pin to the latest release tag
    hooks:
      - id: credactor
```

## Detection

Credactor detects the credential types that leak most often, and assigns each a severity so you can triage at a glance.

| Category | Examples | Severity |
| --- | --- | --- |
| Cloud provider keys | AWS (`AKIA…`), GCP (`AIza…`), Stripe (`sk_live_…`), Slack (`xoxb-…`) | Critical |
| Platform tokens | GitHub (`ghp_`, `github_pat_`), GitLab (`glpat-`), npm (`npm_`), PyPI (`pypi-`) | Critical |
| Private keys | PEM blocks (`-----BEGIN … PRIVATE KEY-----`) | Critical |
| JWTs | `eyJ…` three-segment tokens | High |
| Connection strings | URLs with inline credentials (`scheme://user:pass@host`) | High |
| Credential variables | `password = "…"`, `api_key = "…"`, `secret_key = "…"` | High/Medium/Low |
| XML attributes | `<add key="Password" value="…" />` | High/Medium/Low |
| High-entropy strings | quoted hex (32–64 chars) / Base64 (60+ chars) | Medium/Low |

Deterministic provider tokens (the prefixes above) are flagged regardless of entropy. Heuristic detectors (JWTs, connection strings, hex, Base64) must clear an entropy floor. Standalone hex or Base64 is flagged only when quoted. An unquoted high-entropy value is caught only on a credential-named variable, which spares git SHAs and checksums. For the full detection and severity rules, see the [Manual](https://github.com/rxb06/credactor/blob/main/docs/manual.md#detection--severity).

> Credactor's native rule set is narrower than a dedicated scanner's, and some provider formats (for example SendGrid, Twilio, and Slack webhooks) are not detected. Its edge is remediation: pair it with Gitleaks or TruffleHog for the broadest detection, or run it on its own.

## Pair it with another scanner, redact the lot (BETA)

Credactor stands on its own, and it gets stronger in company. Already run Gitleaks or TruffleHog? Pass their report to Credactor and it redacts the combined set, deduplicated against its own findings (on overlap, the higher severity wins). One remediation pass covers your scan and theirs:

root@kitploit:~

```
gitleaks dir . -f json -r gitleaks.json
credactor --from-gitleaks gitleaks.json --fix-all --yes .
```

`--from-gitleaks` / `--from-trufflehog` (or an `[ingest]` table in `.credactor.toml`) require a directory target. See the [CI Integration guide](https://github.com/rxb06/credactor/blob/main/docs/ci_integration.md).

## More features

* Interactive or batch redaction; a custom replacement string via `--replacement`; `--scan-history` to scan git commit history
* Secure backups: `--secure-delete` (overwrite and remove the `.bak`; raises the bar against casual recovery, not a forensic guarantee) or `--secure-backup-dir` to store backups outside the repo
* Inline `# credactor:ignore` and `.credactorignore` allowlists (globs, `file:line`, value literals)
* Per-repo config via `.credactor.toml`
* 29 source/config/notes file types out of the box (`.txt` included); `--scan-json` to include JSON; `--fail-on-error` to fail when a file cannot be read

## Scanned file types

> `.py` `.js` `.t...