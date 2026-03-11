---
title: The Zero-Day Scramble is Avoidable: A Guide to Attack Surface Reduction
url: https://thehackernews.com/2026/03/the-zero-day-scramble-is-avoidable.html
source: The Hacker News
date: 2026-03-10
fetch_date: 2026-03-11T04:05:31.559918
---

# The Zero-Day Scramble is Avoidable: A Guide to Attack Surface Reduction

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [The Zero-Day Scramble is Avoidable: A Guide to Attack Surface Reduction](https://thehackernews.com/2026/03/the-zero-day-scramble-is-avoidable.html)

**The Hacker News**Mar 10, 2026Vulnerability Management / Shadow IT

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixfoH6o4IkbYakx1lP-kILdg8glEenVOVdJFyn8cxnNYO9hRSMut-XrsII-HfqY_VuguC1b0yHPueeREjsdS0RpXViN0IhuFYzheblF8avbGI6GILTtyHMF5_nJYPIKFRRYL1staxa_9sYMHRjMkL995yoIJYRW072CQaIWh95cCsLXFFpqg769bN-KFA/s1700-e365/INTRUDER.jpg)

You can't control when the next critical vulnerability drops. You can control how much of your environment is exposed when it does. The problem is that most teams have more internet-facing exposure than they realise. [Intruder's](https://www.intruder.io/?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Casr) Head of Security digs into why this happens and how teams can manage it deliberately.

## Time-to-exploit is shrinking

The larger and less controlled your attack surface is, the more opportunities exist for exploitation. And the window to act on them is shrinking fast. For the most serious vulnerabilities, disclosure to exploitation can be as short as 24 to 48 hours. [Zero Day Clock](https://zerodayclock.com/) projects that time-to-exploit will be just minutes by 2028.

That's not a lot of time when you consider what has to happen before a patch is deployed: running scans, waiting for results, raising tickets, agreeing priorities, implementing applies to ’the fix’ too, happy to drop ‘verifying’ if that’s easier. If disclosure lands out of hours, it takes even longer.

In many cases, vulnerable systems don’t need to be internet-facing in the first place. With visibility of the attack surface, teams can reduce unnecessary exposure upfront and avoid the scramble altogether when a new vulnerability drops.

## When a zero-day drops on a Saturday

[ToolShell](https://cvemon.intruder.io/cves/CVE-2025-53770?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Casr) was an unauthenticated remote code execution vulnerability in Microsoft SharePoint. If an attacker could reach it, they could run code on your server - and because SharePoint is Active Directory-connected, they'd be starting in a highly sensitive part of your environment.

This was a zero-day, meaning attackers were exploiting it before a patch was available. Microsoft disclosed on a Saturday and confirmed that Chinese state-sponsored groups had been exploiting it for up to two weeks before that. By the time most teams knew about it, opportunistic attackers were scanning for exposed instances and exploiting at scale.

Intruder’s research found thousands of publicly accessible SharePoint instances at the time of disclosure - despite the fact that SharePoint doesn't need to be internet-facing. Every one of those exposures was unnecessary - and every unpatched server was an open door.

## Why exposures get missed

So why do exposures so often get missed by security teams?

In a typical external scan, informational findings sit beneath hundreds of criticals, highs, mediums, and lows. But that information can include detections that represent real exposure risk, such as:

* An exposed SharePoint server
* A database exposed to the internet, such as MySQL or Postgres
* Other protocols, which should usually be reserved for the internal network, such as RDP and SNMP

Here’s a real example of what that looks like:

In vulnerability scanning terms, classifying these as informationals sometimes makes sense. If the scanner sits on the same private subnet as the targets, an exposed service might genuinely be low risk. But when that same service is exposed to the internet, it carries real risk even without a known vulnerability attached to it. Yet.

The danger is that traditional scan reports treat both cases the same way, so the real risks slip through the gaps.

## What proactive attack surface reduction actually involves

There are three key elements to making attack surface reduction work in practice.

### 1. Asset discovery: define your attack surface

Before you can reduce your attack surface, you need a clear picture of what you own and what's externally reachable. That starts with identifying shadow IT - systems your organization owns or operates but isn't currently scanning or monitoring.

Closing that gap is important, and there are three key elements we recommend having in place:

1. **Integrating with your cloud and DNS providers** so that when new infrastructure is created, it's automatically picked up and scanned. This is one area where defenders have a genuine advantage: you can integrate directly with your own environments, attackers can't.
2. **Using subdomain enumeration** to surface externally reachable hosts that aren't in your inventory. This matters especially after acquisitions, where you may be inheriting infrastructure you don't yet have visibility of.
3. **Identifying infrastructure hosted with smaller, unknown cloud providers**. You may have a security policy that mandates development teams only use your primary cloud provider, but you need to check that practice is being followed.

Watch a deep dive into these techniques:

### 2. Treat exposure as risk

The next step is treating attack surface exposure as a risk category in its own right.

That requires a **detection capability** that identifies which informational findings represent an exposure and assigns appropriate severity. An exposed SharePoint instance, for example, might reasonably be treated as a medium-risk issue.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8h0ILHfxp1-AkeBo4qWc7EaXBXtLeHREuYATp2f_cJAP6iYvNoNIOZ-QPCqrLD_d91p7vndm-xiKscYSCPV5394_12HiaiM0v01sGjaJQSab6qxRLf7UR2yEV50MoezVPJTDVkO01s9GBPW0NkFEc2CKZQwaMbYWqEIrhtguna3u8NRM5JIluUNnvAXc/s1700-e365/ASR.png)

It also means carving out space for this work in **how you prioritize*...