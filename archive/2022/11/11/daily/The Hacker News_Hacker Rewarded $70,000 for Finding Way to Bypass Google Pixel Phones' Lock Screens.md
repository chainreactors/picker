---
title: Hacker Rewarded $70,000 for Finding Way to Bypass Google Pixel Phones' Lock Screens
url: https://thehackernews.com/2022/11/hacker-rewarded-70000-for-finding-way.html
source: The Hacker News
date: 2022-11-11
fetch_date: 2025-10-03T22:26:22.877216
---

# Hacker Rewarded $70,000 for Finding Way to Bypass Google Pixel Phones' Lock Screens

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

# [Hacker Rewarded $70,000 for Finding Way to Bypass Google Pixel Phones' Lock Screens](https://thehackernews.com/2022/11/hacker-rewarded-70000-for-finding-way.html)

**Nov 10, 2022**Ravie Lakshmanan

[![Google Pixel Phones](data:image/png;base64... "Google Pixel Phones")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKeaBPnm6Mq_yeVsYaevt2EHebSnMMj4uqlADp45MXchrazM6QoKjAFCb3Nth8eJE4z1TUWcnmNgEXdZadiarKbVNLHCXo_voVTOIma3tmAJB7nq2UERQw0S2-pNVCgEF8Wm2MHQ4AzYsEKriaQHUVAtc26iHVV7FAHvo87EdFGpmUZNdqzC7ebHiS/s790-rw-e365/google-pixel-hacking.jpg)

Google has resolved a high-severity security issue affecting all Pixel smartphones that could be trivially exploited to unlock the devices.

The vulnerability, tracked as **CVE-2022-20465** and reported by security researcher David Schütz in June 2022, was remediated as part of the search giant's [monthly Android update](https://source.android.com/docs/security/bulletin/2022-11-01) for November 2022.

"The issue allowed an attacker with physical access to bypass the lock screen protections (fingerprint, PIN, etc.) and gain complete access to the user's device," Schütz, who was awarded $70,000 for the lock screen bypass, [said](https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/) in a write-up of the flaw.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The problem, per the researcher, is rooted in the fact that lock screen protections are completely defeated when following a specific sequence of steps -

* Supply incorrect fingerprint three times to disable biometric authentication on the locked device
* [Hot swap](https://en.wikipedia.org/wiki/Hot_swapping) the SIM card in the device with an attacker-controlled SIM that has a PIN code set up
* Enter incorrect SIM pin thrice when prompted, locking the SIM card
* Device prompts user to enter the SIM's Personal Unlocking Key (PUK) code, a unique 8-digit number to unblock the SIM card
* Enter a new PIN code for the attacker-controlled SIM
* Device automatically unlocks

This also means that all an adversary needs to unlock a Pixel phone is to bring their own PIN-locked SIM card and is in possession of the card's PUK code.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The attacker could just swap the SIM in the victim's device, and perform the exploit with a SIM card that had a PIN lock and for which the attacker knew the correct PUK code," Schütz said.

An analysis of the [source code commits](https://android.googlesource.com/platform/frameworks/base/%2B/ecbed81c3a331f2f0458923cc7e744c85ece96da) made by Google to patch the flaw shows that it's caused by an "incorrect system state" introduced as a result of wrongly interpreting the SIM change event, causing it to entirely dismiss the lock screen.

"I was not expecting to cause this big of a code change in Android with this bug," Schütz concluded.

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

[Android](https://thehackernews.com/search/label/Android)[Google](https://thehackernews.com/search/label/Google)[Google Pixel](https://thehackernews.com/search/label/Google%20Pixel)[Lock Screen Bypass](https://thehackernews.com/search/label/Lock%20Screen%20Bypass)[Unlock Screen Lock](https://thehackernews.com/search/label/Unlock%20Screen%20Lock)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited...