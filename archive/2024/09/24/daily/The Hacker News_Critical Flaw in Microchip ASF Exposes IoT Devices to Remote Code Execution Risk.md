---
title: Critical Flaw in Microchip ASF Exposes IoT Devices to Remote Code Execution Risk
url: https://thehackernews.com/2024/09/critical-flaw-in-microchip-asf-exposes.html
source: The Hacker News
date: 2024-09-24
fetch_date: 2025-10-06T18:33:56.833534
---

# Critical Flaw in Microchip ASF Exposes IoT Devices to Remote Code Execution Risk

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

# [Critical Flaw in Microchip ASF Exposes IoT Devices to Remote Code Execution Risk](https://thehackernews.com/2024/09/critical-flaw-in-microchip-asf-exposes.html)

**Sep 23, 2024**Ravie LakshmananIoT Security / Vulnerability

[![IoT Devices](data:image/png;base64... "IoT Devices")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjh62CalnT4mZff4OMT4E4Uxe1ruiOqUvlUjO5hjfZnw-mBgzdYve9WMA3-whO4CpJ7A9fB1twNW7OWr2_a7e5BuGVMp4Sx_zwvwZ9zuF0C2Tx3jdvxLTf9ZBw2lD7-R3omlC0frZVe_OElivms6XMpQMdglu3zQZTZEjn3nokA7Ad3xpXYd6g7zP1IqdmJ/s790-rw-e365/chip-hacking.png)

A critical security flaw has been disclosed in the Microchip Advanced Software Framework (ASF) that, if successfully exploited, could lead to remote code execution.

The vulnerability, tracked as [CVE-2024-7490](https://www.cve.org/CVERecord?id=CVE-2024-7490), carries a CVSS score of 9.5 out of a maximum of 10.0. It has been described as a stack-based overflow vulnerability in ASF's implementation of the tinydhcp server stemming from a lack of adequate input validation.

"There exists a vulnerability in all publicly available examples of the ASF codebase that allows for a specially crafted DHCP request to cause a stack-based overflow that could lead to remote code execution," CERT Coordination Center (CERT/CC) [said](https://kb.cert.org/vuls/id/138043) in an advisory.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Given that the software is no longer supported and is rooted in IoT-centric code, CERT/CC has warned that the vulnerability is "likely to surface in many places in the wild."

The issue impacts ASF 3.52.0.2574 and all prior versions of the software, with the agency also noting that multiple forks of the tinydhcp software are likely susceptible to the flaw as well.

There are currently no fixes or mitigations to address CVE-2024-7490, barring replacing the tinydhcp service with another one that does not have the same issue.

The development comes as SonicWall Capture Labs detailed a severe zero-click vulnerability affecting MediaTek Wi-Fi chipsets ([CVE-2024-20017](https://www.cve.org/CVERecord?id=CVE-2024-20017), CVSS 9.8) that could open the door to remote code execution without requiring any user interaction due to an out-of-bounds write issue.

"The affected versions include MediaTek SDK versions 7.4.0.1 and earlier, as well as OpenWrt 19.07 and 21.02," the company [said](https://blog.sonicwall.com/en-us/2024/09/critical-exploit-in-mediatek-wi-fi-chipsets-zero-click-vulnerability-cve-2024-20017-threatens-routers-and-smartphones/). "This translates to a large variety of vulnerable devices, including routers and smartphones."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The vulnerability is a buffer overflow as a result of a length value taken directly from attacker-controlled packet data without bounds checking and placed into a memory copy. This buffer overflow creates an out-of-bounds write."

A patch for the vulnerability was [released](https://corp.mediatek.com/product-security-bulletin/March-2024) by MediaTek in March 2024, although the likelihood of exploitation has increased with the [public availability](https://github.com/mellow-hype/cve-2024-20017/tree/main) of a proof-of-concept (PoC) exploit as of August 30, 2024.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[iot security](https://thehackernews.com/search/label/iot%20security)[network security](https://thehackernews.com/search/label/network%20security)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[zero-day](https://thehackernews.com/search/label/zero-day)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometja...