---
title: Microsoft Uncovers Critical Flaws in Rockwell Automation PanelView Plus
url: https://thehackernews.com/2024/07/microsoft-uncovers-critical-flaws-in.html
source: The Hacker News
date: 2024-07-05
fetch_date: 2025-10-06T17:51:09.173174
---

# Microsoft Uncovers Critical Flaws in Rockwell Automation PanelView Plus

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Microsoft Uncovers Critical Flaws in Rockwell Automation PanelView Plus](https://thehackernews.com/2024/07/microsoft-uncovers-critical-flaws-in.html)

**Jul 04, 2024**Ravie LakshmananVulnerability / Critical Infrastructure

[![Rockwell Automation PanelView Plus](data:image/png;base64... "Rockwell Automation PanelView Plus")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbIL1sdnlSuKRuMQcSdgJvvwWLPwCagMlvm3hY2E5bHo6qBVsf7oCRjunze5-PgBqPGpLXWnoWZyTwnYdz-1x4xyvgGe9mrrVLVt__uUZ0uB83Gc8X8YdAXq_6AvD29Fz0pWijAon3JTrpKxdx71tBtKWIl7YoFdnJsJfey88DY3Kvt5mJlaByk_R1Db15/s790-rw-e365/rockwell.png)

Microsoft has revealed two security flaws in Rockwell Automation PanelView Plus that could be weaponized by remote, unauthenticated attackers to execute arbitrary code and trigger a denial-of-service (DoS) condition.

"The [remote code execution] vulnerability in PanelView Plus involves two custom classes that can be abused to upload and load a malicious DLL into the device," security researcher Yuval Gordon [said](https://www.microsoft.com/en-us/security/blog/2024/07/02/vulnerabilities-in-panelview-plus-devices-could-lead-to-remote-code-execution/).

"The DoS vulnerability takes advantage of the same custom class to send a crafted buffer that the device is unable to handle properly, thus leading to a DoS."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The list of shortcomings is as follows -

* **CVE-2023-2071** (CVSS score: 9.8) - An improper input validation vulnerability that allows unauthenticated attackers to achieve remote code executed via crafted malicious packets.

* **CVE-2023-29464** (CVSS score: 8.2) - An improper input validation vulnerability that allows an unauthenticated threat actor to read data from memory via crafted malicious packets and result in a DoS by sending a packet larger than the buffer size

Successful exploitation of the twin flaws permits an adversary to execute code remotely or lead to information disclosure or a DoS condition.

[![Rockwell Automation PanelView Plus](data:image/png;base64... "Rockwell Automation PanelView Plus")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLpwOaGZKYH6izxkCTzwbCpEDAT7y0_fsbojWGJ6-q5y6vOBfgPF6ReB_nHQk_nltAoMIA6WJx9faUM_HgYEVTq1wLXnaqEwEAD9tHNqnd2eq7lJIZqKT830y9R0uhQX-ry2MzweUAAWb9vuX6X3ukzKZBoComE90D5syu0DGfZRSBtm_9rRrfow8dAhbh/s790-rw-e365/dll.png)

While CVE-2023-2071 impacts FactoryTalk View Machine Edition (versions 13.0, 12.0, and prior), CVE-2023-29464 affects FactoryTalk Linx (versions 6.30, 6.20, and prior).

It's worth noting that advisories for the flaws were released by Rockwell Automation on [September 12, 2023](https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.PN1645%20.html), and [October 12, 2023](https://www.rockwellautomation.com/en-nl/trust-center/security-advisories/advisory.PN1652.html), respectively. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) released its own alerts on [September 21](https://www.cisa.gov/news-events/ics-advisories/icsa-23-264-06) and [October 17](https://www.cisa.gov/news-events/ics-advisories/icsa-23-290-02).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as unknown threat actors are believed to be [exploiting](https://asec.ahnlab.com/en/67650/) a recently disclosed critical security flaw in HTTP File Server ([CVE-2024-23692](https://nvd.nist.gov/vuln/detail/CVE-2024-23692), CVSS score: 9.8) to deliver cryptocurrency miners and trojans such as [Xeno RAT](https://hunt.io/blog/good-game-gone-bad-xeno-rat-spread-via-gg-domains-and-github), Gh0st RAT, PlugX, and GoThief, the last of which uses Amazon Web Services (AWS) to steal information from the infected host.

The vulnerability, described as a case of [template injection](https://attackerkb.com/topics/d9AVVdmNhH/cve-2024-23692/vuln-details), allows a remote, unauthenticated attacker to execute arbitrary commands on the affected system by sending a specially crafted HTTP request.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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

[critical infrastructure](https://thehackernews.com/search/label/critical%20infrastructure)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[denial of service](https://thehackernews.com/search/label/denial%20of%20service)[industrial control system](https://thehackernews.com/search/label/industrial%20control%20system)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterpris...