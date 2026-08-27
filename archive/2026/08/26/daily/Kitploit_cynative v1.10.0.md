---
title: cynative v1.10.0
url: https://kitploit.com/en/posts/github-cynative-cynative-v1100
source: Kitploit
date: 2026-08-26
fetch_date: 2026-08-27T12:12:42.856941
---

# cynative v1.10.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/9087/cd32c354200d3624e42ec11104750942f8e4b0a4b1f238301f3bcd450c8cd313.png)

New releaseAug 26, 2026

# cynative v1.10.0

Read-only AI agent that queries your cloud, code, and runtime infrastructure to surface misconfigurations, leaked secrets, and privilege escalation paths with verified, evidence-backed findings.

Share

![cynative](https://assets.kitploit.com/production/public/readmes/9087/d9f9ee6fe21757c39e42af370935240c1be375918abe73bbec153796ad78e27c.png)

# Build your own security agents

Open-source framework for security agents with live, read-only access to your infrastructure.

[![CI](https://github.com/cynative/cynative/actions/workflows/ci.yaml/badge.svg)](https://github.com/cynative/cynative/actions/workflows/ci.yaml)
[![Release](https://img.shields.io/github/v/release/cynative/cynative)](https://github.com/cynative/cynative/releases/latest)
[![License: Apache-2.0](https://img.shields.io/github/license/cynative/cynative)](LICENSE)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/13851/badge)](https://www.bestpractices.dev/projects/13851)

**[Quickstart](#quickstart) · [Your first agent](#your-first-agent) · [Docs](https://github.com/cynative/cynative/blob/HEAD/docs/)**

**Ask your infrastructure anything.** Cynative runs frontier models across your code, cloud and runtime - reasoning through GitHub, GitLab, AWS, GCP, Azure and Kubernetes as one system - and comes back with verified answers.

root@kitploit:~

```
cynative "what in my cloud is publicly exposed that shouldn't be?"
```

It writes and runs code in an ephemeral sandbox, querying your APIs in parallel, so one question fans out across your whole stack. Every finding is cross-checked and traced back to its origin.

Unlike coding agents and MCP servers, it's **read-only by construction**: every call is gated and authorized *before* a credential is attached - point it at production with confidence.

![cynative auditing a CI to cloud privilege escalation](https://assets.kitploit.com/production/public/readmes/9087/1b3db179a03479f5951d624c8adbb4890465aa86d038d3312dc9aec9801bcfb9.gif)

## What your agents get

* **Code-to-runtime**: Reasons through AWS, GCP, Azure, any K8s, GitHub and GitLab
* **Sandbox**: Generates and runs code to research at scale, with no network or host access of its own
* **Action-gate**: Resolves every call to its required IAM actions and applies a read-only policy before a credential is attached
* **Evidence-backed**: Cross-checks to verify every finding
* **Sovereign**: One binary, your model, your data stays yours

## Quickstart

Install and set an LLM:

root@kitploit:~

```
brew install cynative/tap/cynative

export CYNATIVE_LLM_PROVIDER=anthropic
export CYNATIVE_LLM_MODEL=claude-opus-5
export ANTHROPIC_API_KEY=...
```

It picks up the credentials already in your shell. Ask it anything:

root@kitploit:~

```
cynative -p "which IAM roles can escalate to admin?"
cynative -p "high-risk cloud permissions, trace each to the PR where it was granted"
cynative -p "cloud credentials leaked in source code and their current blast radius"
cynative "live cloud resources absent from IaC - drift" # starts an interactive session
cat findings.json | cynative -p "triage these findings by exploitability"
```

## Your first agent

An agent is a markdown file: one line of description, then the prompt. The filename is the name. To add your own, create `~/.cynative/agents/` and write one in it. Cynative does not create this directory for you:

root@kitploit:~

```
mkdir -p ~/.cynative/agents

cat > ~/.cynative/agents/aws-public-data-stores.md <<'EOF'
---
description: Finds publicly accessible data stores in an AWS account.
---
Check S3, RDS snapshots, EBS snapshots and public AMIs for exposure.
Report each finding with the resource ARN and how it is reachable.
EOF

cynative -p --agent aws-public-data-stores
```

See [docs/agents.md](https://github.com/cynative/cynative/blob/HEAD/docs/agents.md) for the format.

## Running agents

root@kitploit:~

```
cynative -p --agent aws-public-data-stores "AWS account ID 12814983572854 only"   # with a task
cynative -p --agent aws-public-data-stores                    # without
cynative --agent aws-public-data-stores                       # seeds an interactive session
```

`--agent` composes with `-p`, `--auto-approve`, `--config` and piped stdin, so the same file runs interactively while you develop it and non-interactively once it settles.

Agents are read from `~/.cynative/agents/` and from the set built into the binary; a user file wins over a built-in of the same name. `cynative agents list` shows every agent with its source and marks the shadowed copies, and `cynative agents show <name>` prints the exact file that would run.

## Can't a coding agent with MCPs do this?

|  | Coding agent + MCPs | Cynative |
| --- | --- | --- |
| Throughput | One action per call | Writes sandboxed code that fans out calls concurrently - fewer tokens, faster answers |
| Findings | Unverified output | Verifier cross-checks every finding against live evidence |
| Read-only | Opt-in read filter | On by default, fails closed - required IAM actions checked against a security-audit policy. `secretsmanager:GetSecretValue` is an IAM *Read*: a filter allows it, `SecurityAudit` blocks it |
| Credentials | Ambient, unchanged | STS session scoped to read-only - AWS enforces the boundary too |
| Blast radius | Your shell, any network | Research code runs in a sandbox with no host access, network pinned to your mapped services |
| Secrets | Sent to the model as-is | Redacted from tool output before it's sent to the model |
| Supply chain | Third-party MCPs and skills running with your creds | One open-source binary, connectors built in |
| Audit trail | Scattered session logs, best effort | Fail-closed JSONL log of every tool call - if it can't record, it aborts |

One binary, your model endpoint, your account. Run it on an instance in the cloud it audits, through that cloud's managed inference, and nothing leaves your environment: security on your infrastructure, from within your infrastructure.

## Installation

**Homebrew** (macOS / Linux - recommended):

root@kitploit:~

```
brew install cynative/tap/cynative
```

**Install script** (macOS / Linux - verifies the download's SHA-256 against the release `checksums.txt`, failing closed):

root@kitploit:~

```
curl -fsSL https://raw.githubusercontent.com/cynative/cynative/main/install.sh | sh
```

**Windows** (Scoop):

root@kitploit:~

```
scoop bucket add cynative https://github.com/cynative/scoop-bucket
scoop install cynative
```

**Updating, uninstalling, Windows details, version pinning & manual download**

**Update / uninstall**

| Method | Update | Uninstall |
| --- | --- | --- |
| Homebrew | `brew upgrade cynative` | `brew uninstall cynative` |
| Install script | re-run the one-liner | `curl -fsSL https://raw.githubusercontent.com/cynative/cynative/main/install.sh | sh -s -- --uninstall` |
| Scoop | `scoop update cynative` | `scoop uninstall cynative` |

**Windows (PowerShell script):** `irm https://raw.githubusercontent.com/cynative/cynative/main/install.ps1 | iex`; uninstall with `& ([scriptblock]::Create((irm https://raw.githubusercontent.com/cynative/cynative/main/install.ps1))) -Uninstall`.

**Install-script options:** pin a version with `CYNATIVE_VERSION=v1.0.0`; change the target directory with `CYNATIVE_INSTALL_DIR` (default `~/.local/bin`, no `sudo`). The script checks the GitHub release attestation when `gh` is installed (advisory by default); set `CYNATIVE_REQUIRE_ATTESTATION=1` to make a f...