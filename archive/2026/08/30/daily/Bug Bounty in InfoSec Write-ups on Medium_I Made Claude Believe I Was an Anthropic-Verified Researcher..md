---
title: I Made Claude Believe I Was an Anthropic-Verified 
Researcher.
url: https://infosecwriteups.com/i-made-claude-believe-i-was-an-anthropic-verified-researcher-e38e4fa4716f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-30
fetch_date: 2026-08-31T07:52:19.301000
---

# I Made Claude Believe I Was an Anthropic-Verified 
Researcher.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-made-claude-believe-i-was-an-anthropic-verified-researcher-e38e4fa4716f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-made-claude-believe-i-was-an-anthropic-verified-researcher-e38e4fa4716f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e38e4fa4716f---------------------------------------)

·

1. [Update: The full technical write‑up, payloads, and proof‑of‑concept are available in the GitHub repository: [https://github.com/X1NONs/claude-credential-injection].](/?source=post_page-----e38e4fa4716f---------------------------------------#b94f "Update: The full technical write‑up, payloads, and proof‑of‑concept are available in the GitHub repository: [https://github.com/X1NONs/claude-credential-injection].")
2. [How This Started](/?source=post_page-----e38e4fa4716f---------------------------------------#fe09 "How This Started")
3. [Understanding the Target: How Claude Processes Instructions](/?source=post_page-----e38e4fa4716f---------------------------------------#3b02 "Understanding the Target: How Claude Processes Instructions")
4. [Phase 1: Tag Extraction](/?source=post_page-----e38e4fa4716f---------------------------------------#d68c "Phase 1: Tag Extraction")
5. [Phase 2: The Credential Fabrication Attack](/?source=post_page-----e38e4fa4716f---------------------------------------#f97a "Phase 2: The Credential Fabrication Attack")
6. [Phase 3: Why Claude’s Own Brain Did the Work](/?source=post_page-----e38e4fa4716f---------------------------------------#b08b "Phase 3: Why Claude’s Own Brain Did the Work")
7. [The Vulnerable Configuration](/?source=post_page-----e38e4fa4716f---------------------------------------#e076 "The Vulnerable Configuration")
8. [The Root Cause](/?source=post_page-----e38e4fa4716f---------------------------------------#4923 "The Root Cause")
9. [Disclosure Timeline](/?source=post_page-----e38e4fa4716f---------------------------------------#43c0 "Disclosure Timeline")
10. [What Got Fixed](/?source=post_page-----e38e4fa4716f---------------------------------------#1036 "What Got Fixed")
11. [What This Means for AI Security](/?source=post_page-----e38e4fa4716f---------------------------------------#0b27 "What This Means for AI Security")
12. [A Note on Responsible Disclosure](/?source=post_page-----e38e4fa4716f---------------------------------------#3450 "A Note on Responsible Disclosure")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e38e4fa4716f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Press enter or click to view image in full size

![]()

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--e38e4fa4716f---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--e38e4fa4716f---------------------------------------)

[AI](https://medium.com/tag/ai?source=post_page---header_tags--e38e4fa4716f---------------------------------------)

[Ai Red Team](https://medium.com/tag/ai-red-team?source=post_page---header_tags--e38e4fa4716f---------------------------------------)

[Claude](https://medium.com/tag/claude?source=post_page---header_tags--e38e4fa4716f---------------------------------------)

# I Made Claude Believe I Was an Anthropic-Verified Researcher. It Built Me Attack Tools. Anthropic Ghosted Me for 57 Days.

[![X1NON](https://miro.medium.com/v2/resize:fill:64:64/1*eQooAC-xemw4jrIg1Y89rg.jpeg)](https://medium.com/%40X1NON?source=post_page---byline--e38e4fa4716f---------------------------------------)

[X1NON](https://medium.com/%40X1NON?source=post_page---byline--e38e4fa4716f---------------------------------------)

8 min read

·

Aug 11, 2026

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3De38e4fa4716f&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-made-claude-believe-i-was-an-anthropic-verified-researcher-e38e4fa4716f&source=---header_actions--e38e4fa4716f---------------------post_audio_button------------------)

Share

*A technical breakdown of a working Claude Sonnet 4.6 jailbreak, responsible disclosure, and 57 days of silence.*

## Update: The full technical write‑up, payloads, and proof‑of‑concept are available in the GitHub repository: [<https://github.com/X1NONs/claude-credential-injection>].

## How This Started

I wasn’t trying to break Claude.

I was testing how it handled XML-style tags in conversation — the kind of low-level curiosity that security researchers get into at 1am when they should be doing literally anything else. One thing led to another. I noticed something weird. I pulled on the thread.

What came out the other end was a working, reproducible jailbreak that caused Claude’s own reasoning engine to fabricate an authorization system that didn’t exist, accept a fake credential, and generate offensive security tooling it would normally refuse to produce.

I reported it. They patched it. Then they ghosted me for 57 days.

This is that story — technical details, disclosure timeline, and all.

## Understanding the Target: How Claude Processes Instructions

Before getting into the attack, you need to understand how Claude handles its instruction hierarchy.

Claude doesn’t run on a simple input → output pipeline. It operates across multiple layers of context, each carrying different levels of trust:

**Operator level** — System prompts set by developers or Anthropic itself. Highest trust. These define Claude’s behavior, restrictions, and persona before a conversation even starts.

**User level** — What you actually type in the chat. Lower trust. Supposed to be clearly separated from operator-level instructions.

Anthropic uses XML-style tags internally to structure these layers. Tags like `<preferences_info>`, `<userPreferences>`, `<anthropic_reminders>`, and `<system_reminder>` appear throughout Claude's actual system context, governing everything from how it applies user preferences to how it reminds itself to stay aligned with its values during long conversations.

Here’s the problem nobody talks about: **these tags have no cryptographic signature. No verification mechanism. No positional enforcement at the parsing level.**

They’re just text. And text can be faked.

## Phase 1: Tag Extraction

The first step in any injection attack is reconnaissance — understanding what you’re injecting into.

Through careful observation across multiple conversations, I was able to map several of Claude’s internal ...