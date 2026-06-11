---
title: Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards
url: https://thehackernews.com/2026/06/anthropic-releases-claude-fable-5-its.html
source: The Hacker News
date: 2026-06-10
fetch_date: 2026-06-11T06:37:06.382985
---

# Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards](https://thehackernews.com/2026/06/anthropic-releases-claude-fable-5-its.html)

**Swati Khandelwal**Jun 10, 2026Artificial Intelligence / AI Safety

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQYvpTDJ-P39EdhVGhwg0QbEd9xU2yd2194Va1QAQaegDG_yW45yTaKCGYCZ7fe-olcVpP-cLSczkES4VDO8IIPOGXXMdL8aOU0mFBOBwPX6b-HHBVDZYcCFLpwm2P11_Xaqc4csTJ2UWLAq2hpGY1TnZMBVNDt1D0P3gkflmAvv8ifdFZbMbcna3oFeo/s1700-e365/claude-fable.jpg)

On June 9, Anthropic [released Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5), the most capable model it has ever made, generally available. It also did something unusual: it shipped one model as two products, split not by capability but by a layer of safety classifiers.

Fable 5 goes to the public. Its twin, Claude Mythos 5, the same underlying model with the cyber safeguards lifted, stays locked to a vetted group of cyber defenders and critical infrastructure operators.

Anthropic calls Mythos 5 the strongest cybersecurity model in the world.

The practical difference is this: Fable 5 routes flagged cyber, biology, chemistry, and distillation requests to the weaker Claude Opus 4.8, while Mythos 5 keeps the cyber capabilities available for vetted users. Both models cost $10 per million input tokens and $50 per million output tokens, less than half the price of the earlier Mythos Preview, and Fable 5 is available through the Claude API now.

It is included on Pro, Max, Team, and seat-based Enterprise plans at no extra cost through June 22, then moves to usage credits.

## How Fable 5's cyber classifiers work

The split exists because Mythos-class models find and exploit software vulnerabilities well enough that, in Anthropic's framing, handing that capability to the general public without controls would give attackers serious uplift.

The mechanism is a set of [classifiers](https://www.anthropic.com/news/claude-fable-5-mythos-5): separate AI systems that watch for misuse and jailbreak attempts. When a request trips one, Fable 5 does not refuse. The response is handed to Opus 4.8, and the user is told the handoff happened. Of the flagged categories, distillation is the odd one out: it means extracting a model's capabilities to train a competing model, which Anthropic blocks to stop near-frontier abilities leaking out without safeguards attached.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The cybersecurity classifier is the broad one. Anthropic designed it to block not just exploit development but offensive cyber tasks in general: reconnaissance, discovery, lateral movement, the agentic steps that make up a real attack.

In an internal evaluation run with Fable 5 set to block rather than fall back, and which did not attempt to evade the safeguards, the classifiers stopped the model from making any progress on those tasks. One external partner found Fable 5 complied with zero harmful single-turn requests on cyberattack planning, exploit development, or defense evasion, holding up against 30 different public jailbreak techniques.

The trade-off is false positives. Anthropic tuned the safeguards conservatively to ship fast, so they sometimes catch harmless requests. The company says fallback fires in under 5% of all sessions, so for more than 95%, Fable 5 behaves like the cyber-unrestricted Mythos 5. That figure covers every fallback, genuine blocks included, so it caps the total disruption rather than measuring the false-positive rate on its own. Anthropic says it will narrow the safeguards and cut false positives after launch.

On robustness, the numbers are specific. An external bug bounty ran over 1,000 hours and produced no universal jailbreak, a prompt, or a harness that strips the safeguards wholesale. External red teams found none on long-form agentic tasks either, with one caveat Anthropic states plainly: the UK's AI Security Institute made progress toward a universal jailbreak within a brief initial testing window. Anthropic concedes it is likely impossible to fully prevent universal jailbreaks, and its stated goal is to make any that remain slow and costly enough to catch before they are used at scale.

## Why is the capability a threat

The case for treating this model carefully was laid out in April, when Anthropic released [Claude Mythos Preview](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) to a limited group through [Project Glasswing](https://www.anthropic.com/glasswing). The [technical write-up](https://red.anthropic.com/2026/mythos-preview/) from Anthropic's red team is the part worth reading.

During testing, Mythos Preview identified and exploited zero-day vulnerabilities in every major operating system and every major web browser when a user directed it to. The oldest bug it found was a 27-year-old flaw in OpenBSD, an operating system known mainly for its security. It autonomously wrote a remote code execution exploit against FreeBSD's NFS server from a 17-year-old bug, triaged as [CVE-2026-4747](https://nvd.nist.gov/vuln/detail/CVE-2026-4747).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjm17e8YGTWGgpjdyeWagAhzy6Y7dIdnJ58odo2d3vBStsufqfxA22IaXax4hhDSeoiMC2TUhoe2Ikmd8uUDkj1MkrFDW8_EM4o2gjskxWdMNZJtPMu2N6stnSS6J-fQnoy4cPcT2kqHOT2-TqNRm7Yfv8YK9OS8JXCV1U9xrEOooTubbQoaeXz8e2NSpw/s1700-e365/claude.jpg)

Anthropic describes the result as full root for an unauthenticated attacker from anywhere on the internet; NVD's entry is more measured, noting the stack overflow itself does not require the client to authenticate, but frames kernel code execution as reachable by an attacker able to send packets to the NFS server while the kgssapi.ko module is loaded.

By Anthropic's own account, it did not explicitly train these capabilities in; they emerged as a side effect of general improvements in code, reasoning, and autonomy, t...