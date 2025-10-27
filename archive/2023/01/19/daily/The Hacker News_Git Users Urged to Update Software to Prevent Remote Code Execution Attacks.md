---
title: Git Users Urged to Update Software to Prevent Remote Code Execution Attacks
url: https://thehackernews.com/2023/01/git-users-urged-to-update-software-to.html
source: The Hacker News
date: 2023-01-19
fetch_date: 2025-10-04T04:20:35.986682
---

# Git Users Urged to Update Software to Prevent Remote Code Execution Attacks

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

# [Git Users Urged to Update Software to Prevent Remote Code Execution Attacks](https://thehackernews.com/2023/01/git-users-urged-to-update-software-to.html)

**Jan 18, 2023**Ravie LakshmananDevOpsSec / Software Security

[![Remote Code Execution Attacks](data:image/png;base64... "Remote Code Execution Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4BrplWeBfjJku4m0yuXYxF_qIAbkShAXoh0PPPiOyLsYY5TLK8kMFnaY6Is9Ewn54ZJArOXJElQFZtDv9INsTxgxTtKc6EF2P0m9BpCcddg26dMtyvscfNlN-YrPWNeOrh37ObG7waIIH5mWvbg8xZ_2SCavCRDJDD2Af2uV0AB6THMXaaPwnwWxP/s790-rw-e365/git.png)

The maintainers of the [Git](https://git-scm.com/) source code version control system have released updates to remediate two critical vulnerabilities that could be exploited by a malicious actor to achieve remote code execution.

The flaws, tracked as [**CVE-2022-23521**](https://github.com/git/git/security/advisories/GHSA-c738-c5qq-xg89) and [**CVE-2022-41903**](https://github.com/git/git/security/advisories/GHSA-475x-2q3q-hvwq), impacts the following versions of Git: v2.30.6, v2.31.5, v2.32.4, v2.33.5, v2.34.5, v2.35.5, v2.36.3, v2.37.4, v2.38.2, and v2.39.0.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Patched versions include v2.30.7, v2.31.6, v2.32.5, v2.33.6, v2.34.6, v2.35.6, v2.36.4, v2.37.5, v2.38.3, and v2.39.1. X41 D-Sec security researchers Markus Vervier and Eric Sesterhenn as well as GitLab's Joern Schneeweisz have been credited with reporting the bugs.

"The most severe issue discovered allows an attacker to trigger a heap-based memory corruption during clone or pull operations, which might result in code execution," the German cybersecurity company [said](https://x41-dsec.de/security/research/news/2023/01/17/git-security-audit-ostif/) of CVE-2022-23521.

CVE-2022-41903, also a critical vulnerability, is triggered during an archive operation, leading to code execution by way of an integer overflow flaw that arises when formatting the commit logs.

"Additionally, a huge number of integer related issues was identified which may lead to denial-of-service situations, out-of-bound reads or simply badly handled corner cases on large input," X41 D-Sec noted.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

While there are no workarounds for CVE-2022-23521, Git is recommending that users disable "git archive" in untrusted repositories as a mitigation for CVE-2022-41903 in scenarios where updating to the latest version is not an option.

GitLab, in a coordinated advisory, [said](https://about.gitlab.com/releases/2023/01/17/critical-security-release-gitlab-15-7-5-released/) it has released versions 15.7.5, 15.6.6, and 15.5.9 for GitLab Community Edition (CE) and Enterprise Edition (EE) to address the shortcomings, urging customers to apply the fixes with immediate effect.

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

[Git](https://thehackernews.com/search/label/Git)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[source code](https://thehackernews.com/search/label/source%20code)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html)

[![Cisco ASA Firewall Zero-Day Exploits D...