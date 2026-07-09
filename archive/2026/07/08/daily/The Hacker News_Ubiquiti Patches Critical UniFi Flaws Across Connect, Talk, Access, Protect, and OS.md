---
title: Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS
url: https://thehackernews.com/2026/07/ubiquiti-patches-critical-unifi-flaws.html
source: The Hacker News
date: 2026-07-08
fetch_date: 2026-07-09T06:03:33.629070
---

# Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS](https://thehackernews.com/2026/07/ubiquiti-patches-critical-unifi-flaws.html)

**Ravie Lakshmanan**Jul 08, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgx2TRa1CP7yIs67Wa1bxiFVW5yq1S7vtAaQHf_htjuDbpAETKv8tfw7rchtVvME0FsA8YJ_uQzRp_ZAV-nPhLyRUQw_NNdgN0zhjyVR_L3wzt1ZX08PknwSF2FBLeieIUIx7t4hLMF1sDnsRuFCzllq8auoKriKlGMdllY8IYG04bID6cgGzty0e9mVhoM/s1700-e365/uu.jpg)

Ubiquiti has [shipped updates](https://community.ui.com/releases/Security-Advisory-Bulletin-066-066/984eceb3-49c8-4227-942d-671c289b3afc) to address multiple critical security flaws impacting UniFi Connect, UniFi Talk, UniFi Access, UniFi Protect, and UniFi OS that could result in privilege escalation and arbitrary command execution.

The list of vulnerabilities is as follows -

* **CVE-2026-50746** (CVSS score: 10.0) - An improper access control vulnerability in UniFi Connect Application that an attacker with access to the network could exploit to execute a command injection on the host device. (Affects versions 3.4.16 and earlier; fixed in version 3.4.20)
* **CVE-2026-50747** (CVSS score: 9.9) - A series of authenticated SQL injection vulnerabilities in UniFi Talk Application that an attacker with access to the network could exploit to escalate privileges on the host device. (Affects versions 5.1.2 and earlier; fixed in version 5.2.2)
* **CVE-2026-50748** (CVSS score: 9.9) - An improper input validation vulnerability in UniFi Access Application that an attacker with access to the network could exploit to execute a command injection on the host device. (Affects versions 4.2.28 and earlier; fixed in version 4.2.29)
* **CVE-2026-54400** (CVSS score: 9.1) - An improper access control vulnerability in UniFi Access Application that an attacker with access to the network could exploit to escalate privileges on the host device. (Affects versions 4.2.28 and earlier; fixed in version 4.2.29)
* **CVE-2026-55115** (CVSS score: 9.9) - A Server-Side Request Forgery (SSRF) vulnerability in UniFi Protect Application that an attacker with access to the network and low privileges could exploit to escalate privileges on the host device. (Affects 7.1.77 and earlier; fixed in version 7.1.83)
* **CVE-2026-54402** (CVSS score: 9.9) - An improper input validation vulnerability in UniFi OS that an attacker with access to the network could exploit to execute a command injection on the host device. (Affects versions 5.1.15 and earlier; fixed in version 5.1.19)
* **CVE-2026-55116** (CVSS score: 9.0) - An improper access control vulnerability in UniFi OS that an attacker with access to the network could exploit to make unauthorized changes to certain devices. (Affects versions 5.1.15 and earlier; fixed in version 5.1.19)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

While there is no evidence that the flaws have been exploited in the wild, a set of three vulnerabilities in UniFi OS (CVE-2026-34908, CVE-2026-34909, and CVE-2026-34910) was [flagged](https://thehackernews.com/2026/06/cisa-warns-critical-lantronix-eds5000.html) by the U.S. Cybersecurity and Infrastructure Security Agency (CISA) as having been weaponized in real-world attacks last month.

Russian state-sponsored threat actors have also been [observed](https://thehackernews.com/2024/02/cybersecurity-agencies-warn-ubiquiti.html) enlisting compromised Ubiquiti Edge OS routers into a botnet designed to proxy malicious traffic. The botnet, dubbed [MooBot](https://thehackernews.com/2024/02/us-government-disrupts-russian-linked.htm), was felled in a law enforcement operation in February 2024.

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

[botnet](https://thehackernews.com/search/label/botnet), [Command Injection](https://thehackernews.com/search/label/Command%20Injection), [iot security](https://thehackernews.com/search/label/iot%20security), [network security](https://thehackernews.com/search/label/network%20security), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [SQL Injection](https://thehackernews.com/search/label/SQL%20Injection), [SSRF](https://thehackernews.com/search/label/SSRF), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](data:image/svg+xml;base64... "ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories")

ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html)

[![Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](data:image/svg+xml;base64... "Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability")

Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html)

[![New DirtyClone Linux Kernel Flaw Lets Loc...