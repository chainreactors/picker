---
title: ARTEX: reading the source behind the IOCs
url: https://andpalmier.com/posts/artex-source-behind-iocs/
source: Over Security
date: 2026-11-08
fetch_date: 2026-11-09T08:53:23.754219
---

# ARTEX: reading the source behind the IOCs

[↓
Skip to main content](#main-content)

[andpalmier’s blog](/)

[Home](/ "andpalmier's blog")[About](/about/ "About me")

`⌘K`

[ ]

Close menu

[Home](/)

[About](/about/)

![ARTEX: reading the source behind the IOCs](/posts/artex-source-behind-iocs/featured_hu_eb60071698459abf.jpg)

1. [andpalmier's blog](/)/
2. [Posts](/posts/)/
3. [ARTEX: reading the source behind the IOCs](/posts/artex-source-behind-iocs/)/

# ARTEX: reading the source behind the IOCs

8 November 2026·17 mins·

[Threat Intelligence](/tags/threat-intelligence/)[Detection Engineering](/tags/detection-engineering/)[LLM](/tags/llm/)[AI](/tags/ai/)[Agentic AI](/tags/agentic-ai/)[Security Research](/tags/security-research/)

Author

Andrea Palmieri (@andpalmier)

Deep dives into malware, phishing, and threat intelligence. Eternal noob and AS Roma fan.

Table of Contents

* [Introduction](#introduction)
* [How I did it](#how-i-did-it)
  + [Shameless plug of repopsy](#shameless-plug-of-repopsy)
  + [The lab](#the-lab)
* [Where ARTEX’s traffic really comes from](#where-artexs-traffic-really-comes-from)
  + [The user agent that never calls](#the-user-agent-that-never-calls)
* [The fingerprint that vanished](#the-fingerprint-that-vanished)
* [curl is actually Go](#curl-is-actually-go)
* [The pauses are the model’s](#the-pauses-are-the-models)
* [Nobody wrote `ArtexProbe`](#nobody-wrote-artexprobe)
* [The forks](#the-forks)
* [How the published IOCs hold up](#how-the-published-iocs-hold-up)
* [So, what should defenders build on?](#so-what-should-defenders-build-on)
* [Limits of the analysis](#limits-of-the-analysis)
* [What’s next](#whats-next)
* [Sources](#sources)

Table of Contents

* [Introduction](#introduction)
* [How I did it](#how-i-did-it)
  + [Shameless plug of repopsy](#shameless-plug-of-repopsy)
  + [The lab](#the-lab)
* [Where ARTEX’s traffic really comes from](#where-artexs-traffic-really-comes-from)
  + [The user agent that never calls](#the-user-agent-that-never-calls)
* [The fingerprint that vanished](#the-fingerprint-that-vanished)
* [curl is actually Go](#curl-is-actually-go)
* [The pauses are the model’s](#the-pauses-are-the-models)
* [Nobody wrote `ArtexProbe`](#nobody-wrote-artexprobe)
* [The forks](#the-forks)
* [How the published IOCs hold up](#how-the-published-iocs-hold-up)
* [So, what should defenders build on?](#so-what-should-defenders-build-on)
* [Limits of the analysis](#limits-of-the-analysis)
* [What’s next](#whats-next)
* [Sources](#sources)

## Introduction [#](#introduction)

On October 30th, Google Threat Intelligence and Mandiant published [ARTEX and Friends: Enter Agentic Offensive Frameworks](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks), about threat actors using open-source, LLM-driven pentesting frameworks (ARTEX, PentAGI, Hexstrike and CAIRN) in real intrusions. Some details stuck with me: files named `artex-probe-` plus five digits, accounts with `ArtexProbe` in the name, bursts of activity lasting a few seconds.

Moreover, between October and early November, Microsoft, Wiz, CrowdStrike, Zscaler, Unit 42, AhnLab, Nextron, Censys and others wrote about ARTEX. I came across **62 distinct published indicators** in 11 sources: user agents, made-up test strings, ports, page titles, HTTP headers. However, almost none of them say *where* the indicator comes from; and I think that is relevant because an agentic framework is made of 3 components:

1. the framework’s code
2. a language model, deciding what to do
3. ordinary tools (`curl`, `nmap`, `python`, etc.) actually talking to the target

Strings hard-coded in the framework can survive a model swap, but something the model made up may not survive the next run.

This blog was created by cloning ARTEX, reading its code and its git history, checking 73 of its forks, and testing what I could in a lab. Along the way, 1 of those forks deleted a fingerprint from the reports a few days after it was published.

**TLDR**

* **Most target-side “ARTEX” IOCs aren’t in ARTEX’s code**: User agents, `ArtexProbe` and other made-up test values come from the model or from the tools it runs.
* **ARTEX’s own four user agents are weak signals**: 1 comes from a library also used by other agents, 1 is only sent if the model runs a script, 1 only talks to GitHub, and the last one is dead code.
* **Fingerprints don’t last**: 4 days after Unit 42 published the realm header, the most popular fork replaced it and stripped its name from the health endpoint.
* **In the lab**: ARTEX’s optional traffic recorder makes most tools’ TLS handshake into Go’s, and the pauses between bursts are just the LLM thinking.

And a disclaimer:

* The code analysis is read-only, with git hooks disabled.
* In the lab I ran some ARTEX components in containers on a network with no internet access, against my own listener and a fake LLM.

## How I did it [#](#how-i-did-it)

The original `Autumn-27/ARTEX` repository is not available anymore, but the fork [Hinln/ARTEX](https://github.com/Hinln/ARTEX) still keeps its original history. Every reference to ARTEX in this post is a reference to the upstream’s last release, 0.3.15 ([`e6ec569`](https://github.com/Hinln/ARTEX/tree/e6ec56999175509551a1e43a3ee3b053d0941bd9)).

### Shameless plug of repopsy [#](#shameless-plug-of-repopsy)

Some of my questions in this post were about the *history* of the tool: when did this string appear? Was this function ever called? Did a fork remove something after a vendor wrote about it?

Such questions can be answered easily with some bash magic and [repopsy](https://github.com/andpalmier/repopsy), the tool I already [plugged in the KawaiiGPT post](/posts/kawaiigpt-analysis/), which got a big update (v2.2) while I was working on this:

[andpalmier/repopsy

OSINT tool to gather information on a git repo

⭐ 5
🍴 0
Go](https://github.com/andpalmier/repopsy)

A mirror clone also brings the pull-request refs, which is where we can find third-party code. repopsy then writes a record for every commit (author, signature, changed files, anomalies) and, with `--track`, tells you where a string first appeared and every commit that changed it, across all refs at once. We will use it to answer 2 questions below in the post.

### The lab [#](#the-lab)

I built a small harness from ARTEX’s own code (the part that runs the model’s commands), and connected it to a fake LLM that answers with scripted “run this `curl`” instructions, and pointed it at a listener that records every request and its TLS handshake.

![Lab topology: client under test, stub LLM and capture target on an internal Docker network](/posts/artex-source-behind-iocs/lab-topology.svg)

The lab: the client talks to the fake LLM and to the capture target, nothing else. Click to zoom.

**Lab details, for the curious**:

* The harness runs Norma’s agent loop with the network options ARTEX’s worker sets ([source](https://github.com/Hinln/ARTEX/blob/e6ec56999175509551a1e43a3ee3b053d0941bd9/agent/worker.go#L429-L455)): ARTEX’s own proxy settings, its LLM client and its traffic recorder.
* The runtime image copies the base of ARTEX’s Dockerfile ([source](https://github.com/Hinln/ARTEX/blob/e6ec56999175509551a1e43a3ee3b053d0941bd9/Dockerfile#L13-L22)): `python:3.12-slim-bookworm`, so curl 7.88.1 on OpenSSL 3.0.22 and Node 20. I added python-requests 2.34.2, which ARTEX’s image doesn’t include, but it somehow shows up in the Microsoft and Unit 42 reports.
* The fake LLM uses the OpenAI chat API, and can wait a configurable number of seconds before answering.
* The target listens on 80 and 443, logs headers and records a pcap; tshark computes the [JA4](https://github.com/FoxIO-LLC/ja4) TLS fingerprint. Its certificate is self-signed, so clients that verify certificates fail *after* sending their ClientHello.
* Everything ran on a Docker network created with `--internal`.

## Where ARTEX’s traffic really comes from [#](#where-artexs-traffic-really-comes-from)

ARTEX is made ...