---
title: Project Glasswing Proved AI Can Find the Bugs. Who's Going to Fix Them?
url: https://thehackernews.com/2026/04/project-glasswing-proved-ai-can-find.html
source: The Hacker News
date: 2026-04-23
fetch_date: 2026-04-24T04:57:38.542839
---

# Project Glasswing Proved AI Can Find the Bugs. Who's Going to Fix Them?

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

# [Project Glasswing Proved AI Can Find the Bugs. Who's Going to Fix Them?](https://thehackernews.com/2026/04/project-glasswing-proved-ai-can-find.html)

**The Hacker News**Apr 23, 2026Artificial Intelligence / Exposure Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkzSPo6TkrJjcTvsuM1O71fiiZ7gnKw4PqqtKu_TeAaZNr5qAEfsfVvoZv64F7EFULRIv8SKePHZehY_0g9AqyqlnMdTPF-OLf1S9RwmB-edOgYKEg1Llw-6m87CQBglHxbK3oS0Brnwc9_x_oi56XGuxe1V9vN0KfoY9cUmU4mplEHeqQxO-5byx79YY/s1700-e365/picus-main.jpg)

Last week, Anthropic announced Project Glasswing, an AI model so effective at discovering software vulnerabilities that they took the extraordinary step of postponing its public release. Instead, the company has given access to Apple, Microsoft, Google, Amazon, and a coalition of others to **find and patch bugs before adversaries can**.

Mythos Preview, the model that led to Project Glasswing, **found vulnerabilities across every major operating system and browser.** Some of these bugs had survived decades of human audits, aggressive fuzzing, and open-source scrutiny. One had been **sitting for 27 years**in [OpenBSD,](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) generally considered to be one of the world’s most secure operating systems.

It's tempting to file this under "**AI lab says their AI is too dangerous,**" the same playbook OpenAI ran with GPT-2.

Not so fast; there's a material difference this time.

Mythos didn't just find individual CVEs.

* It **chained four independent bugs into an exploit sequence** that bypassed both the browser renderer and the OS sandboxing
* It performed local privilege escalation in Linux through race conditions
* It built a 20-gadget ROP chain targeting FreeBSD's NFS server, distributed across packets.

Claude Opus 4.6, Anthropic's previous frontier model, failed at autonomous exploit development almost entirely.**Mythos hit a 72.4% success rate in the Firefox JS shell**.

This isn't theoretical, nor some new three-to-five-year prediction. This is about to be a real-world engineering reality.

## **Why Project Glasswing Exposes the Real Cybersecurity Gap**

Here's the number that should keep security leaders awake at night: **fewer than 1% of the vulnerabilities found by Mythos were patched**.

Let that sink in for a moment.

The most powerful vulnerability discovery engine ever built ran against the world's most critical software, and the ecosystem couldn't absorb the output.

Glasswing solved the finding problem.

Nobody solved the problem of fixing.

### **Why Defenders Can't Keep Up: Calendar Speed vs. Machine Speed**

This is the structural issue the cybersecurity industry has been circling for years. AI just made it impossible to ignore.

Defenders operate on **calendar speed**. They:

* Gather intelligence
* Build a campaign
* Simulate the threats
* Mitigate
* Repeat

That cycle takes about **four days on a good day**. Attackers, especially those now leveraging LLMs at every stage of their operation, are **moving at machine speed**.

For an up-to-the-minute take, David B. Cross, CISO at Atlassian, will be speaking at the [Autonomous Validation Summit on May 12](https://hubs.li/Q04cJdmF0) about what this looks like from the inside, why periodic testing can't keep pace with adversaries that operate autonomously, and what defenders should be doing instead.

### **AI-Powered Attacks Are Already Autonomous**

Earlier this year, a threat actor deployed **a custom MCP server hosting an LLM as part of their attack chain** against FortiGate appliances.

The AI handled everything:

* Automated backdoor creation
* Internal infrastructure mapping fed directly to the model
* Autonomous vulnerability assessment, and
* AI-prioritized execution of offensive tools for domain admin access.

The result? **2,516 organizations across 106 countries were compromised** in parallel. The entire chain, from initial access through credential dumping to data exfiltration, was autonomous. The only human involvement was reviewing the results afterward.

### **AI-based Vulnerability Discovery Is Outpacing Remediation**

The gap between attacker speed and defender speed isn't new.

**What's new is that a small but worrisome gap just became a canyon.**

* Autonomous systems like AISLE [discovered](https://aisle.com/blog/aisle-discovered-12-out-of-12-openssl-vulnerabilities) 13 out of 14 OpenSSL CVEs in recent coordinated releases, bugs that had survived years of human review.
* XBOW became the [top-ranked](https://xbow.com/blog/top-1-how-xbow-did-it) hacker on HackerOne in 2025, surpassing all human participants.
* The median time from disclosure to weaponized exploit [dropped](https://www.resilientcyber.io/p/the-zero-day-clock-is-ticking-why) from 771 days in 2018 to single-digit hours by 2024.
* By 2025, the majority of exploits will be weaponized *before* being publicly disclosed.

**Now add Mythos-class discovery to this picture.**

You don't get a safer world automatically. You get a **tsunami of legitimate findings that still require human verification**, organizational process, business continuity considerations, and patch cycles that haven't fundamentally changed in a decade.

## **How to Build a Mythos-Ready Security Program**

The instinct after Glasswing is to ask: "How do we find more bugs?"

That's actually the wrong question.

The right one is: "When thousands of exploitable vulnerabilities land on your desk tomorrow morning, **can your program actually process them?**"

For most organizations, the honest answer is no. And the reason isn't a lack of tools or talent; it's a structural **dependency on periodic**, **human-initiated processes** that were designed for a world where vulnerabilities trickled in, not one where they arrived in a tsunami.

We can't fix every vulnerability. We can't apply every hardening option.

> **That's not defeatism**, that’s the pragmatic starting point for any security program that actually works. The question that matters isn't "is this CVE critical?" but "**is this vulnerability exploitable in my environment, right now, given what I have deployed?**"

[A Mythos-ready security program](https://www.picussecurity.com/resource/report/surviving-the-post-mythos-era-12-actions-to-validate-your-defenses-before...