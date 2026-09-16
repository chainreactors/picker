---
title: Attack Chains, Not Just Attack Surfaces: Why Testing Individual Techniques Misses the Point
url: https://thehackernews.com/2026/09/attack-chains-not-just-attack-surfaces.html
source: The Hacker News
date: 2026-09-15
fetch_date: 2026-09-16T07:06:14.819905
---

# Attack Chains, Not Just Attack Surfaces: Why Testing Individual Techniques Misses the Point

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Attack Chains, Not Just Attack Surfaces: Why Testing Individual Techniques Misses the Point](https://thehackernews.com/2026/09/attack-chains-not-just-attack-surfaces.html)

**The Hacker News**Sep 15, 2026Security Testing / Attack Simulation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQ5FtIC97mlzzBT1tKZW7igSSWnJsEI-gEDuUjX-_smFr3Q-loPw-bYG2rEqPBOFPOm0SeL3Go5NvyiJo_DbqnF7ECWdg1EA0DaUML5koDFnXi_lTpJ_Vuow5bsBeQvqLTN25x3O0seE7Qxv5o3S9KoIKuQAVIu7FTPPoZm6ly5XtS97tng5LAaw3tCCY/s1700-nu-rw-lo-l85-e365/live.jpg)

## **Introduction**

Security teams have gotten pretty good at testing against what can hurt them. Can this EDR agent catch this payload? Will my organization fail the phishing simulation? Does this SIEM rule fire on this particular technique? And, in more mature organizations, this testing happens continuously rather than as a one-off exercise.

But no matter how much you validate against these exposures, it doesn't fix the main problem the industry is facing: these are isolated, disconnected testing.

And real attackers, increasingly AI Powered ones, don't test techniques one at a time. They chain them. A phishing email leads to a credential harvest. That harvest leads to an initial foothold. The foothold leads to privilege escalation, then lateral movement, then data staging, then exfiltration… until the damage is irreversibly done.

Any one of those individual steps might be something a security control is theoretically capable of catching - but there's just too many potential exposures to test for, and even if you were to fix 90%, it's that 10% that's missing that might act as the broken link making an attack path exploitable.

What actually matters is whether the whole sequence gets caught, or whether it slips through the gaps between tools, teams, and alerts that were never really built to talk to each other.

That gap, between testing techniques and testing chains, is where a lot of "validated" security postures quietly fall apart.

## **Facing the Exposure Gap**

Most breach and attack simulation programs, even fairly mature ones, are built around a library of individual techniques mapped to a framework like MITRE ATT&CK. Run technique 1234, check if it's detected. Run technique 5678, check if it's blocked. Score it, move on to the next one.

That tells you something real, but not the thing you actually need to know: whether an adversary who strings ten of those techniques together, adapting at each step based on what worked, could walk straight through your environment while every individual control quietly reports "no issue detected".

This isn't just a theoretical concern. According to [Filigran's](https://filigran.io/?utm_medium=contentsyndication&utm_source=hackernews&utm_campaign=openaev-v3&utm_content=orgarticle) **[State of Threat Management report](https://filigran.io/resources/state-of-threat-management?utm_medium=contentsyndication&utm_source=hackernews&utm_campaign=openaev-v3&utm_content=orgarticle)**, 93% of security leaders say their organization suffered a business-impacting cyberattack in the past 12 months, despite most having validated their defenses at some point along the way. 88% say AI is now accelerating how fast attackers move once they get inside, and 84% point to siloed tools and disconnected testing as a main reason exposures go unnoticed until someone exploits them.

This shows there's a real gap between knowing about a threat and the reality of being resilient against it: Understanding cyber risk exposure has become significantly more complex.

You can see the pattern in real incidents too. When France's tax authority, the DGFiP, was breached in 2025, no single step in the intrusion was particularly exotic. It was the sequence of initial access, credential abuse, lateral movement, and exfiltration, all carried out in a coordinated chain that turned a handful of individually survivable weaknesses into a major breach. Each control along the way may well have "worked" on its own. The chain still got through.

## **Attack Chaining: Testing the Way Attackers Actually Operate**

Attack Chaining is what closes that gap. It's a new type of scenario in **[OpenAEV](https://filigran.io/products/openaev?utm_medium=contentsyndication&utm_source=hackernews&utm_campaign=openaev-v3&utm_content=orgarticle)** that automates multi-stage attack paths end to end, the same way a red team would run them, but continuously and at a fraction of the cost.

Instead of testing techniques as isolated events, Attack Chaining links them into a live sequence: the real output of one action (a harvested credential, an open port, a token, a misconfigured permission) is captured automatically and used to decide what gets attacked next. Recon reveals a target, a credential dump yields a password, that password unlocks the next machine, and the chain keeps building on whatever it actually finds in your environment, branching in real time on an interactive graph from initial access through to the final objective.

That gets you the realism of a manual red-team engagement without the cost or the wait. A red team is thorough but expensive and periodic - a snapshot taken once or twice a year while the environment keeps changing underneath it. Attack Chaining runs in minutes, as often as you need it, so instead of a stale report you get an always-current answer to the only question that matters: if an adversary strung these techniques together today, where would they actually get through?

### **How It Works**

Five capabilities work together to make that possible:

1. **Open, conditional chaining logic.** Teams build reusable multi-stage attack path logic from scratch, drawing on any action or event in OpenAEV - TTPs, payloads, custom actions, or library content. Conditions determine what happens next: if a credential is valid, pivot here; if a control blocks the step, stop or reroute. A chain branches automatically based on what each ac...