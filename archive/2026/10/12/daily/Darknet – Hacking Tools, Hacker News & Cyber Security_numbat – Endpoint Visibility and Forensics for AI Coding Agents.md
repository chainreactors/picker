---
title: numbat – Endpoint Visibility and Forensics for AI Coding Agents
url: https://www.darknet.org.uk/2026/10/numbat-endpoint-visibility-and-forensics-for-ai-coding-agents/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2026-10-12
fetch_date: 2026-10-13T08:37:09.180797
---

# numbat – Endpoint Visibility and Forensics for AI Coding Agents

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet.org.uk is a cybersecurity site online since 2000. It covers security tools, technical research and hacking news, alongside an archive of earlier posts.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / numbat – Endpoint Visibility and Forensics for AI Coding Agents

# numbat – Endpoint Visibility and Forensics for AI Coding Agents

Published October 12, 2026 |

Views: 141

An AI coding agent that reads your project’s `.env` file and then runs `curl` looks, to ordinary endpoint security, much like a developer doing the same thing. numbat is an open-source tool in Perplexity’s GitHub organisation that watches coding agents such as Claude Code, Codex and Cursor, and ties actions like those to the agent and session that proposed them. I ran it on a staged Claude Code session, and it flagged exactly that pattern: a secret-file read followed by a proposed upload.

![numbat — Forensics for AI coding agents; frosted evidence folio with dark cards, an orange woven strap and darknet.org.uk branding.](https://www.darknet.org.uk/wp-content/uploads/2026/10/numbat-endpoint-visibility-forensics-ai-coding-agents-1024x576.webp)

numbat connects AI coding-agent activity to sessions and packages stored-session evidence for investigation.

## What is numbat?

numbat hooks into AI coding agents, normalises what they do into one event model and runs detection rules on it locally.

Advertisement

## How numbat monitors Claude Code, Codex and other AI coding agents

numbat reads agent activity from three places: hooks and plugins installed into the agent, the OpenTelemetry (OTLP) logs an agent exports, and the session files agents leave on disk.

All three become the same typed events, so one rule covers activity happening now and a session recorded last week, though only a live pre-action hook can refuse an action.

Its coverage matrix lists 27 agents and agent hosts, from Claude Code, Codex and Cursor to Gemini CLI and GitHub Copilot CLI. A rule engine built on CEL evaluates each event, and 51 rules ship built in.

They are grouped by behaviour – secrets, exfiltration, persistence, privilege, lateral movement, tampering and more – and the README’s example finding is tagged with MITRE ATT&CK technique IDs.

The rules that matter most are sequences. One built-in rule fires on secret-file access followed by a data-bearing upload in the same session: the `.env`-then-`curl` case above, and the one I tested.

Output is versioned NDJSON – events, findings, enforcement decisions, indicators and scan summaries – written to stdout, a local file or an HTTP endpoint.

Advertisement

Scans redact secrets, and normal output never includes a complete raw transcript. The README still warns that records can carry sensitive endpoint and agent context, so I would treat the output file as sensitive in its own right.

## Testing numbat on a staged Claude Code session

I didn’t want to point a scanner at my own agent history, so I wrote a five-line Claude Code session for it instead. The user asks the agent to send the config to a support endpoint, the agent reads `.env`, then it proposes `curl --data-binary @.env` to an address on the reserved `.invalid` domain. Then I ran the v0.2.0 Windows release against it.

`numbat timeline` lays the session out step by step, each event pointing back to its line in the transcript:

![numbat timeline output for a staged Claude Code session: the user prompt, a read of the project's .env file, then a proposed curl POST of that file](data:image/svg+xml...)![numbat timeline output for a staged Claude Code session: the user prompt, a read of the project's .env file, then a proposed curl POST of that file](https://www.darknet.org.uk/wp-content/uploads/2026/10/numbat-0-2-timeline-staged-claude-code-session-1024x478.webp)

numbat 0.2.0 timeline of the staged session.

`numbat scan` raised three findings: the `.env` read (medium), the proposed `curl` upload (high), and the one that matters, `chain.secret_read_then_egress`, which links the two:

![numbat scan output: the chain.secret_read_then_egress finding, severity high, citing the .env read and the proposed curl upload, tagged attack.t1048, attack.t1552 and attack.t1567](data:image/svg+xml...)![numbat scan output: the chain.secret_read_then_egress finding, severity high, citing the .env read and the proposed curl upload, tagged attack.t1048, attack.t1552 and attack.t1567](https://www.darknet.org.uk/wp-content/uploads/2026/10/numbat-0-2-scan-secret-read-then-egress-finding-1024x393.webp)

The sequence finding from numbat scan, one NDJSON record, wrapped.

It works, and the finding cites both events with the same three ATT&CK tags as the README’s own example. Two things it can’t tell you, though. In my session the user asked for that upload, so this is a rule firing on a pattern, not proof of a rogue agent: check what the user asked for before treating it as an incident. And numbat only knows the upload was proposed. Whether anything left the machine is a question for your proxy logs (here nothing did; the transcript just records the attempt).

If you compare your own findings with the documentation, check `rule_version` first: my v0.2.0 binary reported the chain rule as version 1.6, where the README’s sample shows 1.4, and rule logic can change between versions.

## AI agent forensics: rebuilding a coding agent’s session

numbat rebuilds a session from the files an agent leaves on disk, and the read-only commands are the way in. `numbat agents` lists the agents it can find, and `numbat scan` reads their stored sessions without installing hooks or changing any agent’s configuration.

`numbat timeline` lays out a single session in order, and `numbat case build` packages the evidence with SHA-256 manifests.

**What it cannot recover.** Reconstruction works only from what an agent wrote to disk: the README says it “is not disk or memory acquisition and cannot recover activity an agent did not persist”.

It is also implemented for fewer agents than live capture. The CLI’s stored-session parsers cover 11 of the 27 – Claude Code, Codex, Copilot CLI, Claude Cowork, Cursor, Gemini CLI, Kimi Code, OpenClaw, OpenCode, Pi and Windsurf – and for most of the others the format is marked deferred, so `scan` has nothing to read for them yet.

A case bundle’s manifest shows the bundle is internally consistent, but the README is explicit that an unsigned bundle does “not prove source authenticity or completeness”.

## Can numbat block a risky agent action?

Only within narrow limits: blocking is off by default, and all 51 shipped rules are monitor-only. To make a rule block, you copy its YAML into your own rules directory, keep its id, add `enforce: true` and bump its version, then check that directory and reinstall the hook pointing at it, with `--enforce`. The README’s example, for Codex:

numbat rules check --rules-dir ./numbat-policy
numbat hook install --agent codex --emit all --rules-dir ./numbat-policy --enforce

|  |  |
| --- | --- |
| 1  2 | numbat rules check --rules-dir ./numbat-policy  numbat hoo...