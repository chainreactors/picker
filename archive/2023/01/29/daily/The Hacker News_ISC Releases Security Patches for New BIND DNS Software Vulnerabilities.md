---
title: ISC Releases Security Patches for New BIND DNS Software Vulnerabilities
url: https://thehackernews.com/2023/01/isc-releases-security-patches-for-new.html
source: The Hacker News
date: 2023-01-29
fetch_date: 2025-10-04T05:09:02.788576
---

# ISC Releases Security Patches for New BIND DNS Software Vulnerabilities

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

# [ISC Releases Security Patches for New BIND DNS Software Vulnerabilities](https://thehackernews.com/2023/01/isc-releases-security-patches-for-new.html)

**Jan 28, 2023**Ravie LakshmananServer Security / DNS

[![BIND DNS Software Vulnerabilities](data:image/png;base64... "BIND DNS Software Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi14s0aPtBLTfnxre-Tcy_0iJw4wKjyvJXdFmpmytL0iK3U2TG9iuShttu03onhVu90xXRkXyG1E8mZIUEB9-7zYBLGuBeyKDyDYoawof_VJyCzvlcvt25P4_hpimE0q8pU9UlOphEkLyIh5IR5Wsar48_Dfmp2K3oVoP_5JrZ3_b48XH1-8RuGdnAW/s790-rw-e365/dns.jpg)

The Internet Systems Consortium (ISC) has released patches to address multiple security vulnerabilities in the Berkeley Internet Name Domain (BIND) 9 Domain Name System (DNS) software suite that could lead to a denial-of-service (DoS) condition.

"A remote attacker could exploit these vulnerabilities to potentially cause denial-of-service conditions and system failures," the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [said](https://www.cisa.gov/uscert/ncas/current-activity/2023/01/27/isc-releases-security-advisories-multiple-versions-bind-9) in an advisory released Friday.

The open source software is used by major financial firms, national and international carriers, internet service providers (ISPs), retailers, manufacturers, educational institutions, and government entities, according to its [website](https://www.isc.org/bind/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

All four flaws reside in [named](https://kb.isc.org/docs/aa-00817), a [BIND9 service](https://bind9.readthedocs.io/en/v9_18_11/chapter1.html) that functions as an authoritative nameserver for a fixed set of DNS zones or as a recursive resolver for clients on a local network.

The list of the bugs, which are rated 7.5 on the CVSS scoring system, is as follows -

* [**CVE-2022-3094**](https://kb.isc.org/v1/docs/cve-2022-3094) - An UPDATE message flood may cause named to exhaust all available memory
* [**CVE-2022-3488**](https://kb.isc.org/v1/docs/cve-2022-3488) - BIND Supported Preview Edition named may terminate unexpectedly when processing ECS options in repeated responses to iterative queries
* [**CVE-2022-3736**](https://kb.isc.org/v1/docs/cve-2022-3736) - named configured to answer from stale cache may terminate unexpectedly while processing RRSIG queries
* [**CVE-2022-3924**](https://kb.isc.org/v1/docs/cve-2022-3924) - named configured to answer from stale cache may terminate unexpectedly at recursive-clients soft quota

Successful exploitation of the vulnerabilities could cause the named service to crash or exhaust available memory on a target server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The issues affect versions 9.16.0 to 9.16.36, 9.18.0 to 9.18.10, 9.19.0 to 9.19.8, and 9.16.8-S1 to 9.16.36-S1. CVE-2022-3488 also impacts BIND Supported Preview Edition versions 9.11.4-S1 to 9.11.37-S1. They have been resolved in versions 9.16.37, 9.18.11, 9.19.9, and 9.16.37-S1.

Although there is no evidence that any of these vulnerabilities are being actively exploited, users are recommended to upgrade to the latest version as soon as possible to mitigate potential threats.

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

[bind server](https://thehackernews.com/search/label/bind%20server)[domain name](https://thehackernews.com/search/label/domain%20name)[hacking news](https://thehackernews.com/search/label/hacking%20news)[server security](https://thehackernews.com/search/label/server%20security)

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
...