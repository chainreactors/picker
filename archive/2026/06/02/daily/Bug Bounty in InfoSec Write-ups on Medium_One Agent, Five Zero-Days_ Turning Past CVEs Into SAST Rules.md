---
title: One Agent, Five Zero-Days: Turning Past CVEs Into SAST Rules
url: https://infosecwriteups.com/one-agent-five-zero-days-turning-past-cves-into-sast-rules-650c32b20032?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-02
fetch_date: 2026-06-03T06:45:24.070338
---

# One Agent, Five Zero-Days: Turning Past CVEs Into SAST Rules

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-agent-five-zero-days-turning-past-cves-into-sast-rules-650c32b20032&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-agent-five-zero-days-turning-past-cves-into-sast-rules-650c32b20032&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-650c32b20032---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-650c32b20032---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# One Agent, Five Zero-Days: Turning Past CVEs Into SAST Rules

[![Philip Garabandic](https://miro.medium.com/v2/resize:fill:64:64/1*ccp_DqSg1T9fs3e7kn0ITg.jpeg)](https://medium.com/%40philipgarabandic?source=post_page---byline--650c32b20032---------------------------------------)

[Philip Garabandic](https://medium.com/%40philipgarabandic?source=post_page---byline--650c32b20032---------------------------------------)

10 min read

·

May 27, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D650c32b20032&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-agent-five-zero-days-turning-past-cves-into-sast-rules-650c32b20032&source=---header_actions--650c32b20032---------------------post_audio_button------------------)

Share

## Introduction

Every security engineer has seen a bug get reported, patched, written up in a postmortem, and then watched a similar bug show up six months later in a different module of the same product. Same root cause, same fix. Sometimes the same engineer writes both versions.

This happens for the obvious reason. Large products have the same primitives reimplemented in many places. Authorization checks, input parsing, identity resolution, and tenant boundaries get rewritten by different teams at different times, often without anyone realizing it. When one team learns a lesson the hard way, that lesson lives in a postmortem doc and the heads of whoever was on call. Once the fix ships, people forget about it and move on.

Traditional SAST does not catch these repeats. It does not know what your authorization code looks like, where your tenant boundaries are, or which internal abstractions your team keeps getting wrong. The bugs that actually hurt you sit one layer below anything an off-the-shelf ruleset can see.

In this article I want to show how you can use past incident reports to catch these repeats with specialized AI agents, and walk through how I used this approach to find five zero-days in OpenClaw.

## OpenClaw

Press enter or click to view image in full size

![]()

OpenClaw is a self-hosted gateway for AI agents. The operator installs it on their own machine, points it at a language model (Claude, GPT, or a local model via Ollama), and connects it to whichever chat platforms they want to message the agent from. It supports more than twenty channels in total, including Slack, Discord, Matrix, Microsoft Teams, Telegram, WhatsApp, iMessage, Signal, and Zalo. With over 375,000 GitHub stars as of late May 2026, it is one of the more widely adopted open source projects in the AI agent space.

Each channel comes with its own allowlist. The operator specifies which users on that platform are permitted to message the agent, and that allowlist is the entire security model. If you can get yourself onto it, you can steer a tool-enabled AI agent that the operator trusts to act on their behalf. Depending on what the agent is wired up to do, that can mean reading files, sending messages, running shell commands, or hitting internal APIs. The consequences of an allowlist bypass on OpenClaw are not “an attacker leaks some data.” They are “an attacker drives your agent.”

The Telegram channel extension had a public advisory filed against it (GHSA-mj5r-hh7j-4gxf) for resolving non-numeric allowlist entries through mutable Telegram display names. It got patched in the Telegram module, and the project moved on.

## agentgg CLI

Press enter or click to view image in full size

![]()

agentgg.dev

The next section walks through how I built detectors from OpenClaw’s past advisories and ran them against the codebase. That workflow needs a runner. The runner I used is agentgg.

agentgg is an open source CLI for agentic SAST. Think Nuclei, but for AI agents instead of YAML templates. Agents are markdown files with YAML frontmatter and a prompt body. Every agent is a tool-enabled investigation (Read, Glob, Grep) that declares where to look; there are no separate execution modes anymore. The runner dispatches the agents across a target codebase, validates each finding, and produces GHSA-shaped reports.

A scan runs in three phases, each writing a durable artifact under a state directory so the steps are inspectable and resumable. Recon is a fast survey that writes a project brief (languages, frameworks, auth model, integrations) and feeds it into the later phases so agents start oriented. Preconditions gate each selected agent, deciding whether it is worth running on this repo at all. Then each queued agent runs over its file set in batches, an optional validation pass classifies each finding as confirmed, false-positive, out-of-scope, or uncertain, and an optional scoring pass attaches a CVSS 3.1 severity.

Out of the box, agentgg ships with over 100 pre-built agents covering common security vulnerabilities, anti-patterns, and codebase recon. Custom agents can be installed into the agent directory or passed inline at scan time, which is the path I used for the OpenClaw-specific detectors. The CLI is built for CI/CD and integrates with GitHub Actions, with a diff mode that scopes a scan to only the files changed in a pull request.

It is on npm as `agentgg` and on GitHub under `[agentgg-dev/agentgg](https://github.com/agentgg-dev/agentgg)`.

## One agent, five zero-days

The input was the Telegram advisory along with the other public CVEs filed against OpenClaw’s channel extensions. I fed them into an agent-creation flow I built that reads past advisories and writes one agent per recurring bug pattern it finds.

The flow returned twelve agents, each targeting a distinct anti-pattern specific to OpenClaw. Examples include `openclaw-audit-allowlist-identity-hunter` (mutable identifiers used at trust boundaries), `openclaw-audit-exec-policy-bypass-hunter` (execution policy bypasses), and `openclaw-audit-trusted-event-ingress-hunter` (trust placement on unverified inbound events). The full set is published at [agentgg-dev/ag...