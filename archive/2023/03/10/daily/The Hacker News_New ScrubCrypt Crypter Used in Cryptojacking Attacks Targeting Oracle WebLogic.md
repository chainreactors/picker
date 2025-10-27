---
title: New ScrubCrypt Crypter Used in Cryptojacking Attacks Targeting Oracle WebLogic
url: https://thehackernews.com/2023/03/new-scrubcrypt-crypter-used-in.html
source: The Hacker News
date: 2023-03-10
fetch_date: 2025-10-04T09:11:52.318761
---

# New ScrubCrypt Crypter Used in Cryptojacking Attacks Targeting Oracle WebLogic

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

# [New ScrubCrypt Crypter Used in Cryptojacking Attacks Targeting Oracle WebLogic](https://thehackernews.com/2023/03/new-scrubcrypt-crypter-used-in.html)

**Mar 09, 2023**Ravie LakshmananCryptojacking / Threat Detection,

[![ScrubCrypt Crypter](data:image/png;base64... "ScrubCrypt Crypter")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3SJc_9G_j_mTdbnKFquNcPK1f7HwHbRU3Z0_A8XHFznCXw2PnPKSkdgMWbJ9qVAKKXLZpHh4Ri3cXEzjxnfkptr0nA1jak-Uoo_aKhdJstlZIeWKppzhliQjWoicPQa1NORUqWi6LAKJ3SYpzElS1_T5OmXQ9OdwlMovkX6YBvVhWlw-3ZgBgmDoX/s790-rw-e365/malware.png)

The infamous cryptocurrency miner group called 8220 Gang has been observed using a new crypter called ScrubCrypt to carry out cryptojacking operations.

According to Fortinet FortiGuard Labs, the attack chain commences with the successful exploitation of susceptible Oracle WebLogic servers to download a PowerShell script that contains ScrubCrypt.

Crypters are a type of software that can encrypt, obfuscate, and manipulate malware with the goal of evading detection by security programs.

ScrubCrypt, which is advertised for sale by its author, comes with features to bypass Windows Defender protections as well as check for the presence of debugging and virtual machine environments.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"ScrubCrypt is a crypter used to secure applications with a unique BAT packing method," security researcher Cara Lin [said](https://www.fortinet.com/blog/threat-research/old-cyber-gang-uses-new-crypter-scrubcrypt) in a technical report. "The encrypted data at the top can be split into four parts using backslash '\.'"

[![ScrubCrypt Crypter](data:image/png;base64... "ScrubCrypt Crypter")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPuBMdDpPkWh3wk-CFpI9pRvdwxMX1UCJjqEajLzDgm_bzaGXD7GMbVww0IN1gEaLMkfC1Hvaodd-SCIVXRVpUDUqLVFfv5x-3F2cfNTVJj0eHih-nC0TpkGBURU9FPREs2jiVlNs2FFHG-Q71-wVwqX00Q4SC8_V_UZvGmPgfToGBWRrpz5JrcAdo1w/s790-rw-e365/flow.png)

The crypter, in the final stage, decodes and loads the miner payload in memory, thereby launching the miner process.

The threat actor has a track record of taking advantage of publicly disclosed vulnerabilities to infiltrate targets, and the latest findings are no different.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development also comes as Sydig [detailed](https://sysdig.com/blog/8220-gang-continues-to-evolve/) attacks mounted by the 8220 Gang between November 2022 and January 2023 that aim to breach vulnerable Oracle WebLogic and Apache web servers to drop the XMRig miner.

In late January 2023, Fortinet also uncovered [cryptojacking attacks](https://www.fortinet.com/blog/threat-research/malicious-code-cryptojacks-device-to-mine-for-monero-crypt) that make use of Microsoft Excel documents containing malicious VBA macros that are configured to download an executable to mine Monero (XMR) on infected systems.

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

[cryptojacking](https://thehackernews.com/search/label/cryptojacking)[Oracle WebLogic](https://thehackernews.com/search/label/Oracle%20WebLogic)[threat detection](https://thehackernews.com/search/label/threat%20detection)

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

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html...