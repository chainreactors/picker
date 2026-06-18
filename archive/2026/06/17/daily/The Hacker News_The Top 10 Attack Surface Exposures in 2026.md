---
title: The Top 10 Attack Surface Exposures in 2026
url: https://thehackernews.com/2026/06/the-top-10-attack-surface-exposures-in.html
source: The Hacker News
date: 2026-06-17
fetch_date: 2026-06-18T06:51:59.313662
---

# The Top 10 Attack Surface Exposures in 2026

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

# [The Top 10 Attack Surface Exposures in 2026](https://thehackernews.com/2026/06/the-top-10-attack-surface-exposures-in.html)

**The Hacker News**Jun 17, 2026Attack Surface Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiM2DfFAWIuQ6v6hyh32CXcT_wKU72aTUxixyWIcnjW04ydv40r8RtVXjDrxKJzksW6zzqYciPMxgYAwcDGRz8kahhZVZXoi0FySWg5o8LpWo_KkHdX4wRX4Qgk6ONxHqyb7_cF5TN5qQp-9B4hOQpB3WljI8sDbHMlOh6n2jyTjV30kxC-ccJVJHu4bTs/s1700-e365/INTRUDER.jpg)

Breaches don't always start with a zero-day. An exposed admin panel can get brute-forced, or credentials reused from a previous attack. But when a vulnerability does drop — like MongoBleed earlier this year, which let attackers pull credentials and session tokens from server memory without authentication — anything internet-facing is immediately at risk.

With time-to-exploit now down to a single day, the question isn't just how fast you can patch. It's why the service was exposed in the first place.

The team at Intruder analyzed 3,000 attack surfaces to find out how much of a typical organization's attack surface consists of services that have no reason to be there. We grouped what we found into four categories — HTTP panels, risky ports and services, databases, and publicly accessible files and information.

The full findings, including breakdowns by company size and industry, are in our [2026 Attack Surface Management Index](https://www.intruder.io/blog/attack-surface-exposures?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Casm_index).

## How widespread is the problem?

* 60% of organizations had at least one HTTP panel exposed — admin consoles, management UIs, login pages for internal tools that have no business being publicly reachable.
* Nearly half (49%) had a risky port or service exposed.
* 42% had a database reachable directly from the internet.
* 30% had files or information publicly accessible that shouldn't be — API documentation, config files, data that was never intended to be discoverable.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKBqm1VSjUhbIeBaVpFoLm_jCsfRQtD04XhpffPoLIId5WcFV_05VqJ0imkPSf3eVp-QtOpu5refN_UqixuB0WISpRkRE0H8SqCZll5r_YkXP32ULgw_InZGbweNhHTxMUK-Zz-0-FQFwUOvjoGsrp5NkqH5gnkLdT7VFPoBPXTjkZ-o8pZSDtomxy3_k/s1700-e365/1.png)

## The ten most common exposures

These are the most common attack surface exposures affecting organizations in the past 12 months.

1. MySQL Database Exposed — 26%
2. Postgres Database Exposed — 16%
3. API Documentation Exposed — 15%
4. WordPress Admin Panel Exposed — 15%
5. Remote Desktop Service Exposed — 11%
6. SNMP Service Exposed — 9%
7. phpMyAdmin Admin Panel Exposed — 8%
8. UPnP Service Exposed — 8%
9. NTP Service Exposed — 7%
10. RPC Portmapper Service Exposed — 7%

### Databases dominate the top two spots

Exposed databases take the top two spots, with more than a quarter of organizations exposing MySQL and Postgres, affecting 1 in 6. Internet-facing databases have long been a target for opportunistic attackers. The PLEASE\_READ\_ME ransomware campaign in 2020 compromised more than 250,000 MySQL databases by brute-forcing weak credentials. MongoDB and Elasticsearch have faced the same.

### API documentation is more exposed than RDP

API documentation ranked third — ahead of RDP, which surprised us. Some API docs are intentionally public, but organizations frequently overlook documentation tied to private or admin-side APIs that were never meant to be discoverable. Public API docs can turn otherwise hard-to-find vulnerabilities into documented attack paths.

### RDP remains a ransomware entry point

RDP at number five is a concern given its history as an initial access vector in ransomware attacks. BlueKeep in 2019 left nearly a million systems immediately exploitable. Credential guessing against exposed RDP remains one of the most reliable ways ransomware operators get in.

### The rest of the list was never meant to be internet-facing

The remainder of the list — SNMP, UPnP, NTP, RPC — are legacy services designed for internal networks that were never meant to be internet-facing.

## Get the full findings

Most teams treat patching as the priority. But for a lot of what's on this list — databases, admin panels, legacy services — the better question is why they're reachable at all. That's where [attack surface reduction](https://www.intruder.io/blog/why-attack-surface-reduction-is-your-first-line-of-defense?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Casm_index) comes in — and for most organizations, it's not getting the same attention as vulnerability management.

The full findings, including breakdowns by company size and industry, are in the [2026 Attack Surface Management Index](https://www.intruder.io/blog/attack-surface-exposures?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Casm_index).

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[API Security](https://thehackernews.com/search/label/API%20Security), [Attack Surface Management](https://thehackern...