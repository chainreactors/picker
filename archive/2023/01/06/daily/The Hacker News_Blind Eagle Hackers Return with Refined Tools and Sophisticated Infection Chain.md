---
title: Blind Eagle Hackers Return with Refined Tools and Sophisticated Infection Chain
url: https://thehackernews.com/2023/01/blind-eagle-hackers-return-with-refined.html
source: The Hacker News
date: 2023-01-06
fetch_date: 2025-10-04T03:12:23.172783
---

# Blind Eagle Hackers Return with Refined Tools and Sophisticated Infection Chain

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

# [Blind Eagle Hackers Return with Refined Tools and Sophisticated Infection Chain](https://thehackernews.com/2023/01/blind-eagle-hackers-return-with-refined.html)

**Jan 05, 2023**Ravie LakshmananCyber Attack / Malware

[![Blind Eagle Hackers](data:image/png;base64... "Blind Eagle Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUge21n5t12HNout0Mm2LwLSsF8h22iAkVO3RDrcBYX1Oi75BG7BlK_qXX2DpKye93AzS40oBpExrCxbiCqaybz9KapMs02UYsaOX2-ippug289q401Ftl1o08fJJ8_YR1b1RzbMPxCtDUZ7D8qmNmoAzgSb1jrab5nlJQjY4jE0Y_z0fHx443-tca/s790-rw-e365/bot.png)

A financially motivated threat actor tracked as **Blind Eagle** has resurfaced with a refined toolset and an elaborate infection chain as part of its attacks targeting organizations in Colombia and Ecuador.

Check Point's [latest research](https://research.checkpoint.com/2023/blindeagle-targeting-ecuador-with-sharpened-tools/) offers new insights into the Spanish-speaking group's tactics and techniques, including the use of sophisticated tools and government-themed lures to activate the killchain.

Also tracked under the name APT-C-36, Blind Eagle is notable for its narrow geographical focus and launching indiscriminate attacks against South American nations since at least 2018.

Blind Eagle's operations have been [documented](https://thehackernews.com/2021/09/a-new-wave-of-malware-attack-targeting.html) by Trend Micro in September 2021, when it described a spear-phishing campaign primarily aimed at Colombian entities that's designed to deliver a commodity malware known as [BitRAT](https://thehackernews.com/2023/01/hackers-using-stolen-bank-information.html), with a lesser focus towards targets in Ecuador, Spain, and Panama.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Attack chains commence with phishing emails containing a booby-trapped link that, when clicked, leads to the deployment of an open source trojan named Quasar RAT with the ultimate goal of gaining access to the victim's bank accounts.

Some of targeted banks consists of Banco AV Villas, Banco Caja Social, Banco de Bogotá, Banco Popular, Bancoomeva, BBVA, Colpatria, Davivienda, and TransUnion.

[![Blind Eagle Hackers](data:image/png;base64... "Blind Eagle Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9OWfp-qpw7Lb3NSmaSfoEmNkBQ3ulSPCVj0vq5nB3tpNGe-gY6H8l0ydxYOOGfBnWyfGjVZbbiJdhZyNf8pFmEVNojzng1uprTj904XVF7hoo66vjFXTIAtIvHGFOX9Ww-Ah94gx3OTmHeq2mjKFFYcSgnWNs874V-CzeOigd8L7Hyy4tTo7VhCfM/s790-rw-e365/emails.png)

Should the email recipient be located outside of Colombia, the attack sequence is aborted and the victim is redirected to the official website of the Colombian border control agency, Migración Colombia.

A related campaign singling out both Colombia and Ecuador masquerades as the latter's Internal Revenue Service (SRI) and makes use of a similar geo-blocking technology to filter out requests originating from other countries.

This attack, rather than dropping a RAT malware, employs a more complex multi-stage process that abuses the legitimate [mshta.exe binary](https://attack.mitre.org/techniques/T1218/005/) to execute VBScript embedded inside an HTML file to ultimately download two Python scripts.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The first of the two, ByAV2.py, is an in-memory loader engineered to run a [Meterpreter payload](https://thedfirreport.com/2022/11/14/bumblebee-zeros-in-on-meterpreter/) in DLL format. mp.py is also a Meterpreter artifact, only it's programmed in Python, indicating that the threat actor could be using one of them as a redundant method to retain backdoor access to the host.

"Blind Eagle is a strange bird among APT groups," the researchers concluded. "Judging by its toolset and usual operations, it is clearly more interested in cybercrime and monetary gain than in espionage."

The development comes days after Qualys [disclosed](https://thehackernews.com/2023/01/hackers-using-stolen-bank-information.html) that an unknown adversary is leveraging personal information stolen from a Colombian cooperative bank to craft phishing emails that result in the deployment of BitRAT.

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

[Check Point](https://thehackernews.com/search/label/Check%20Point)[Malware](https://thehackernews.com/search/label/Malware)[Python](https://thehackernews.com/search/label/Python)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](...