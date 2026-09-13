---
title: When the Whole Company Adopts AI: What It Does to Your SOC
url: https://thehackernews.com/2026/09/when-whole-company-adopts-ai-what-it.html
source: The Hacker News
date: 2026-09-12
fetch_date: 2026-09-13T07:02:07.944729
---

# When the Whole Company Adopts AI: What It Does to Your SOC

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

# [When the Whole Company Adopts AI: What It Does to Your SOC](https://thehackernews.com/2026/09/when-whole-company-adopts-ai-what-it.html)

**The Hacker News**Sep 12, 2026AI Agent / Security Operations

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhx03NP3tJYBFro8_pZ2g6irfvMJFy0HGYqvUu9kkRJZBnMJ-BcA9aWGZZ1vS4a71YOgpB5qLBDkoNnMyOBJXGhfsyQQMK0IgaGunMOUTLnFUSFddG_5NwlnXsUCWJpGh3bGOcWLHpxXTAqv0i4QAYyRZPXcm0Rcp5K9Yfc7o7SEeLZXNtGp3NZVMzlv1M/s1700-nu-rw-lo-l85-e365/in.jpg)

Over the past year, we watched a new class of alert appear in enterprise security operations centers and grow faster than anything else in the stream: alerts that were triggered by AI tools and agents. Not attacks against AI, but the ordinary, everyday footprint of an organization using it, from developers running coding agents and non-technical staff signing consumer AI tools into corporate accounts.

We reviewed AI-related activity across numerous enterprise environments. Two numbers frame everything that follows. AI-related alerts still account for only 0.43% of all SOC alerts. And that share is climbing every single month, up 685% between February and June 2026. AI is a small slice of the alert stream today and the fastest-growing slice at the same time.

What makes those alerts worth a security team’s attention is not their volume but their composition. We sort everything an AI agent triggers in a SOC into three buckets: real attacks, risks, and noise, with the split being 94.1% noise, 5.8% genuine risk, and 0.02% real attacks. Meaning that across the data we investigated, real attacks that use AI agents are a drop in the ocean. The cost of AI in the SOC, so far, is not breaches. It is a rising tide of alerts that look alarming and almost never are, and a small, quiet set of genuine exposures that those alarms tend to bury.

This post walks through each of the three categories with anonymized examples. All customer names, hostnames, usernames, and identifiers have been removed; indicators are defanged.

## The New Shape of the Alert Stream

AI adoption inside an enterprise is not one behavior it is two very different ones arriving at the same time.

The first is technical. Developers install coding agents that spawn shells, read credential stores, open network tunnels, download packages, and run security tooling all as legitimate work, and all of it indistinguishable to a detection engine from the [early stages of an intrusion](https://cyberpress.org/agent-tunnels-mimic-c2/). This is the loud half, and it dominates the data.

The second is when employees grant OAuth consent to third-party AI applications, [share information](https://concentric.ai/is-chatgpt-secure-10-prompts-you-dont-want-your-employees-trying-with-chatgpt/#:~:text=an%20average%20of,and%20HR%20%286.9%25%29), and paste documents into generative-AI tools. This is the quiet half. It rarely trips an endpoint detection, but it is where data leaves the building.

Both halves land in the same place, the SOC, and both look, at first glance, like something to worry about. Sorting the signal from the noise is the entire job.

## By the Numbers

AI accounts for a small share of the volume but is fast-growing\*\*.\*\* Of the roughly 16.9 million SOC alerts we reviewed, about 73,000 (0.43%) were AI-related. Read on its own, that is reassuringly small.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0wYMtW519SBxNwZKalmET5XY_r7b_wHRjP4x0CDYj15FhfXfnQLDQOLDtY_3lfdr6WVUYiQTuq7BDzajE3brB0eTMDiHxMZagl9UbVphH5YnA7jSHeJOPsQGUcntkBBAccNTDoeS71fDpnbq_mbAXTv1yXDml6nVp15A03k6a12rEwkvzyM29jGN1o34/s1700-nu-rw-lo-l85-e365/1.png) |
| Number of AI-related alerts per month as seen in our system. |

The rise is monotonic. Every full month is higher than the one before, and growth accelerated sharply in May 2026. Over the window when reporting is stable across regions (February to June), volume grew by 685%. The 0.43% figure is best understood as today’s floor, not a ceiling. A team that sizes its AI-alert handling to current volume will be under-provisioned within a quarter.

The composition is as lopsided as the trend is steep. Nearly all of the AI-generated alerts are noise.

For this research, we investigated the AI-related population and sorted each alert by the underlying activity. A real attack is a confirmed compromise. A security risk is not a compromise but a genuine exposure (for example, a coding agent running with its permission safeguards disabled). Noise is legitimate activity that tripped a detection written before AI agents existed. By that measure, nearly all of the AI-related alerts are noise (94.1%), a small portion are genuine security risks (5.8%), and real attacks are a sliver (0.02%).

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2PFlM6G22q9lupV3iZ2ZZSbKPTvgPCPocurhiHfsu0J_DqTcpgfARxPGLIequ4k35Ivytn1N9gL_VdORNEKgRhqiZnh2BwQksezashIKVgxdO1qm1Q9uxiXNAHefFKuCYaBXxjvfaJ1s4yxBGGEDW-k6VqgdJ-EMwQ6ICFaiErq1mHKCHKiEjrRELz7w/s1700-nu-rw-lo-l85-e365/2.png) |
| The breakdown of the AI-related alerts based on the final classification of each alert. |

The second measurement is how those same alerts were handled in production without a human in the loop. When an alert reaches an automated triage platform, two separate decisions are made about it.

* The verdict states how dangerous the activity looks: it can be benign, suspicious, or malicious.
* 79.8% received a benign verdict.
* The response states what happens next: the alert can be suppressed (closed automatically, so no analyst ever sees it), flagged for follow-up, or escalated to a human.
* 81.7% were automatically suppressed.

Of the AI-related population, only 5.4% were ever escalated to a human analyst; the remainder were flagged for follow-up.

A high-severity alert does not necessarily mean an actual threat. For example, a single detection at a ...