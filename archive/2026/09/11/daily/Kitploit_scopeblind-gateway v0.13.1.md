---
title: scopeblind-gateway v0.13.1
url: https://kitploit.com/en/posts/github-scopeblind-scopeblind-gateway-v0131
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:16.779593
---

# scopeblind-gateway v0.13.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13151/4fe235835108beba64601f23e4afd0e86d77d30b4b5d7af9cf0c1d690a49be7a.png)

New releaseSep 11, 2026

# scopeblind-gateway v0.13.1

Ed25519 signed receipts + Cedar policies for AI agents. Finance mandate gate (Legate), proof packs, 3 IETF Internet-Drafts. npx protect-mcp

Share

# protect-mcp

Fail-closed Cedar policy gate plus signed receipts for AI agent tool calls.

[![npm version](https://img.shields.io/npm/v/protect-mcp)](https://www.npmjs.com/package/protect-mcp)
[![downloads](https://img.shields.io/npm/dm/protect-mcp)](https://www.npmjs.com/package/protect-mcp)
[![license](https://img.shields.io/npm/l/protect-mcp)](https://www.npmjs.com/package/protect-mcp)
[![node](https://img.shields.io/node/v/protect-mcp)](https://www.npmjs.com/package/protect-mcp)

`protect-mcp` is a gate that sits in front of an AI agent's tool calls. It evaluates
each call against a [Cedar](https://www.cedarpolicy.com/) policy (the same language
AWS uses for IAM), blocks what breaks the rules before it runs, and signs an
offline-verifiable Ed25519 receipt of every decision. It runs locally, sends no
telemetry of your decisions anywhere, and is MIT licensed.

## Why it is different

* **Fail-closed by default.** On any policy error, a missing engine, or an
  evaluation failure, the decision is DENY. The gate never silently allows. An
  observe mode exists for shadow rollout, but even there a call that would be
  blocked is flagged `would_deny: true`, so a failure is never silent.
* **It proves its own restraint.** `serve --enforce` and `doctor` run a startup
  self-test and refuse to arm the gate unless they can show that a known-forbidden
  action is actually denied. A gate that cannot prove it denies does not start.
* **Every decision is a receipt anyone can verify.** Decisions are Ed25519-signed
  and verifiable offline with [`@veritasacta/verify`](https://www.npmjs.com/package/%40veritasacta/verify).
  No vendor trust required: the math does not care who runs it.

## Quickstart: install to first useful proof

root@kitploit:~

```
# 1. Generate an Ed25519 keypair, config template, and sample policy.
npx protect-mcp init

# 2. Wrap any MCP server in shadow mode. Nothing is blocked yet; calls are logged.
npx protect-mcp wrap -- node your-mcp-server.js

# 3. Inspect the local-only dashboard: tool inventory, risk, approvals, receipts.
npx protect-mcp dashboard --open

# 4. Draft a reviewable policy from observed calls.
npx protect-mcp recommend --write

# 5. When reviewed, restart the wrapper in enforce mode with that policy.
npx protect-mcp --policy protect-mcp.recommended.json --enforce -- node your-mcp-server.js
```

For Claude Desktop, run a dry-run config patch first, then apply it:

root@kitploit:~

```
npx protect-mcp wrap --claude-desktop
npx protect-mcp wrap --claude-desktop --write
npx protect-mcp dashboard --open
```

The dashboard binds to `127.0.0.1`, reads only local log/receipt files, and does
not upload anything. Use `npx protect-mcp connect` only if you explicitly want a
hosted ScopeBlind dashboard.

## The gate as an MCP server

If you would rather call the gate as tools than wire the Claude Code hooks, run
it as an MCP server:

root@kitploit:~

```
npx protect-mcp mcp
```

It speaks MCP over stdio and exposes four read-only tools, the whole loop:

* **`evaluate_action`**: decide a proposed tool call against an inline Cedar policy, fail-closed (any policy error is DENY). Returns `{ allowed, decision, reason, policy_digest }`.
* **`sign_decision`**: turn a decision into an Ed25519 signed receipt (a denial signs a `gateway_restraint`, an allow a `decision_receipt`). Returns the receipt and its public key; generates an ephemeral key if you do not supply one.
* **`verify_receipt`**: verify a signed receipt offline against a public key. Returns `{ valid, error, type, kid, issuer }`.
* **`self_test`**: prove it, no inputs. A known-forbidden action is denied, then a signed receipt round-trips and a tampered copy fails.

Point any MCP host at it, for example Claude Desktop:

root@kitploit:~

```
{
  "mcpServers": {
    "protect-mcp": { "command": "npx", "args": ["-y", "protect-mcp", "mcp"] }
  }
}
```

Receipts are byte-compatible with the ones the gate signs at runtime, so a
receipt minted here verifies with [`@veritasacta/verify`](https://www.npmjs.com/package/%40veritasacta/verify)
and the browser verifier just the same.

### Local Action Dashboard

`protect-mcp dashboard` is the operator view for moving from visibility to
enforcement:

* **Tool inventory:** every observed tool, call count, high/medium/low risk, and
  whether the active policy has an exact rule, a wildcard fallback, or no rule.
* **Policy coverage:** one-click local policy edits for `Require approval`,
  `Block`, or `Observe`. Restart the wrapper after reviewing changes.
* **Exact-action approval queue:** the exact tool, action, destination, redacted
  payload preview, payload hash, policy basis, and reason capture before a human
  approves, denies, edits, or takes over.
* **Receipt chain:** request ids correlated with signed receipt hashes, so an
  audit reviewer can see which decisions have cryptographic proof.
* **Audit export:** downloads the offline-verifiable audit bundle when signed
  receipts exist. If only unsigned local logs exist, the dashboard explains that
  signing must be enabled first.

For live desktop fallback approvals, start the dashboard with the local gateway
approval endpoint and nonce printed by the wrapper:

root@kitploit:~

```
npx protect-mcp dashboard --open \
  --approval-endpoint http://127.0.0.1:9876 \
  --approval-nonce "$PROTECT_MCP_APPROVAL_NONCE"
```

`Approve` forwards to the live local gateway when those flags are present.
`Deny`, `Edit`, and `Take over` are recorded locally as approval-resolution
records; use them as the operator instruction and rerun the tool when needed.

### Paid Boundary MVP: digest anchoring, not data upload

Local self-signed receipts stay free and offline-verifiable. The paid boundary is
independent evidence that ScopeBlind saw a receipt digest at a time, under an org
identity, without receiving the raw prompt, tool payload, output, private key, or
raw receipt.

root@kitploit:~

```
# Create or refresh a local org identity and public-key directory.
npx protect-mcp registry init --org "Meridian Global Macro" --billing-account acct_meridian

# Local preview: writes a digest registry and shareable static verifier page.
npx protect-mcp registry anchor

# Hosted mode: uploads receipt digests only for independent anchoring.
SCOPEBLIND_TOKEN=... npx protect-mcp registry anchor \
  --hosted \
  --endpoint https://api.scopeblind.com \
  --verifier-base https://legate.scopeblind.com
```

The local preview is deliberately labeled `local-preview-not-independent`.
Hosted mode anchors only receipt hashes, request ids, org public keys, and
billing metadata. It does not upload raw receipts or sensitive context.

### Killer Demo: shadow to policy to proof

`protect-mcp killer-demo` generates a complete three-minute sales/demo pack:

root@kitploit:~

```
npx protect-mcp killer-demo --dir ./scopeblind-demo
```

It creates mock filesystem, GitHub, email, and PMS activity; shows risky calls in
shadow mode; applies a policy pack; requires approval for a sensitive PMS booking;
executes through the gateway; writes a signed receipt; proves the original
receipt verifies; proves a tampered receipt fails; and creates a selective
disclosure package that hides sensitive context while showing the minimum proof.

Open the generated `DEMO-RUNBOOK.md` first. Then run th...