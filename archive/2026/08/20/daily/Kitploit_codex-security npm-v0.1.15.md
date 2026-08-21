---
title: codex-security npm-v0.1.15
url: https://kitploit.com/en/posts/github-openai-codex-security-npm-v0115
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:45.127297
---

# codex-security npm-v0.1.15

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/45393/bb353fd9dfaeab944cf56abceb6d48526f4d504113c3b0f8ac7d54f68e882ac5.png)

New releaseAug 20, 2026

# codex-security npm-v0.1.15

OpenAI's Codex Security CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities. npm: https://www.npmjs.com/package/@openai/codex-security

Share

# Codex Security

`@openai/codex-security` is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code.

**See the [Codex Security documentation](https://learn.chatgpt.com/docs/security/cli)** for more details.

Some cybersecurity requests and protected findings require approval through
Trusted Access for Cyber. To apply or check your access, visit
[chatgpt.com/cyber](https://chatgpt.com/cyber).

## Quick start

Requires Node.js 22.13.0 or later in the 22.x release line, Node.js 24.x, or
Node.js 26.x; Python 3.10 or later; and access to Codex Security.

root@kitploit:~

```
npm install @openai/codex-security
npx @openai/codex-security login
npx @openai/codex-security scan .
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high
npx @openai/codex-security scan . --scan-prompt-file scan.md --post-scan-prompt-file follow-up.md
npx @openai/codex-security scan . --mode deep --workers 2 --subagents 0 --stop-after-no-new 3 --max-discovery-runs 10
```

For CI, set `OPENAI_API_KEY` or `CODEX_API_KEY` instead of signing in.
Environment API keys are passed directly to the current scan and are never
stored in Codex's credential home or system keyring.

To use another inference provider, set its API key and select a model:

root@kitploit:~

```
export OPENROUTER_API_KEY="<your-openrouter-api-key>"
npx @openai/codex-security scan . --provider openrouter --model anthropic/claude-sonnet-4.5

export FIREWORKS_API_KEY="<your-fireworks-api-key>"
npx @openai/codex-security scan . --provider fireworks --model accounts/fireworks/models/qwen3-235b-a22b

export AWS_BEARER_TOKEN_BEDROCK="<your-bedrock-api-key>"
export AWS_REGION="us-east-2"
npx @openai/codex-security scan . --provider amazon-bedrock --model openai.gpt-5.6-luna
```

Amazon Bedrock also supports standard AWS access keys, profiles, web identity,
container credentials, and the default AWS credential chain.

Local sign-in honors Codex's configured credential backend, including a system
keyring required by a managed device. Codex Security keeps login and scan
credentials in the same private, persistent state directory.

If both a ChatGPT sign-in and an API key are available, interactive scans ask
which credential to use. CI and other noninteractive scans keep the existing
API-key precedence. Select a credential explicitly when needed:

root@kitploit:~

```
npx @openai/codex-security scan . --auth chatgpt
npx @openai/codex-security scan . --auth api-key
```

To make your ChatGPT sign-in the automatic default, unset any configured API
keys:

root@kitploit:~

```
unset OPENAI_API_KEY CODEX_API_KEY
```

Scan history is stored in the Codex Security workbench state directory. If that
directory cannot be written, set `CODEX_SECURITY_STATE_DIR` to a writable
directory outside the repository.

`findings list [repository]` shows open findings across a repository's scans
and identifies findings not confirmed in its latest scan.

`scans compare BEFORE_SCAN_ID AFTER_SCAN_ID` automatically matches findings by
root cause, reuses saved matches, and identifies new, persisting, reopened,
resolved, or unknown findings. Missing findings remain unknown when coverage is
incomplete or their original location was not reviewed.

## Verbose diagnostics

Add `--verbose` to print scan diagnostics to stderr:

root@kitploit:~

```
npx @openai/codex-security scan . --verbose
```

`CODEX_SECURITY_LOG_LEVEL=debug` also enables diagnostics;
`LOG_LEVEL=debug` is its fallback. JSON results remain on stdout.

Verbose diagnostics may contain sensitive data. Review local logs before
sharing them. Saved failure summaries, bulk-scan receipts, and the interactive
dashboard omit messages that contain recognizable credentials.

Use `npx @openai/codex-security scans logs SCAN_ID` to inspect saved session
events from a scan and its workers.

## TypeScript SDK

root@kitploit:~

```
import { CodexSecurity } from "@openai/codex-security";

const security = new CodexSecurity();
const result = await security.run(".");
await security.run(".", {
  mode: "deep",
  workers: 2,
  subagents: 0,
  stopAfterNoNew: 3,
  maxDiscoveryRuns: 10,
});

console.log(result.reportPath);
await security.close();
```

## Containerized bulk scans

Use the official image and included Docker Compose configuration for
noninteractive, resumable scans of repositories pinned to immutable Git
revisions. See the [container quick start](https://github.com/openai/codex-security/blob/HEAD/sdk/typescript/README.md#containerized-bulk-scans)
for authentication, private result storage, and optional Ubuntu AppArmor
hardening.

Pass `--knowledge-base PATH` to share security documents with every repository;
repeat the option for multiple files or directories.

Use `--scan-prompt-file PATH` to add shared scan instructions, and add a `prompt`
CSV column for repository-specific instructions. Use
`--post-scan-prompt-file PATH` to run a follow-up after each scan, including
incomplete or failed scans.

For complete command help, runtime defaults, native multi-agent worker limits,
environment variables, deep-scan configuration, and SDK options, see the
[package README](https://github.com/openai/codex-security/blob/HEAD/sdk/typescript/README.md) and the
[official CLI reference](https://learn.chatgpt.com/docs/security/cli/reference).

[Read more](/en/tools/github/openai/codex-security?expand=1)

## Categories

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Static Code Analysis (SAST)](/en/categories/static-code-analysis)[DevSecOps](/en/categories/devsecops)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories