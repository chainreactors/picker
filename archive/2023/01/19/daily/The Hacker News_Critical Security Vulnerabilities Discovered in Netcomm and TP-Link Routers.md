---
title: Critical Security Vulnerabilities Discovered in Netcomm and TP-Link Routers
url: https://thehackernews.com/2023/01/critical-security-vulnerabilities.html
source: The Hacker News
date: 2023-01-19
fetch_date: 2025-10-04T04:20:34.627165
---

# Critical Security Vulnerabilities Discovered in Netcomm and TP-Link Routers

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

# [Critical Security Vulnerabilities Discovered in Netcomm and TP-Link Routers](https://thehackernews.com/2023/01/critical-security-vulnerabilities.html)

**Jan 18, 2023**Ravie LakshmananNetwork Security

[![Netcomm and TP-Link Routers](data:image/png;base64... "Netcomm and TP-Link Routers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxTmovl0b_1St1w6mO_P2FVqOSEL0wHT9tsraelWb4-A3zVKyI1MC33s6egKUuqP47UEEzz3VTu5wnH8Qxn_m15GIdcCW31O_f9mhZT62CEDzG8Go2ka0EiWqdpS3h7EY-w8igoVPRM2CEcIe1Y7cGzb94x7gTxrvyih7749WuLiKJAOjeSg4_QXJl/s790-rw-e365/router.png)

Security vulnerabilities have been disclosed in Netcomm and TP-Link routers, some of which could be weaponized to achieve remote code execution.

The flaws, tracked as [CVE-2022-4873](https://nvd.nist.gov/vuln/detail/CVE-2022-4873) and [CVE-2022-4874](https://nvd.nist.gov/vuln/detail/CVE-2022-4874), concern a case of stack-based buffer overflow and authentication bypass and impact Netcomm router models NF20MESH, NF20, and NL1902 running firmware versions earlier than [R6B035](https://support.netcommwireless.com/products/NF20#Firmware).

"The two vulnerabilities, when chained together, permit a remote, unauthenticated attacker to execute arbitrary code," the CERT Coordination Center (CERT/CC) [said](https://kb.cert.org/vuls/id/986018) in an advisory published Tuesday.

"The attacker can first gain unauthorized access to affected devices, and then use those entry points to gain access to other networks or compromise the availability, integrity, or confidentiality of data being transmitted from the internal network."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Security researcher [Brendan Scarvell](https://github.com/scarvell/advisories/blob/main/2022_netcomm_nf20mesh_unauth_rce.md) has been credited with discovering and reporting the issues in October 2022.

[![Vulnerabilities in Netcomm and TP-Link Routers](data:image/png;base64... "Vulnerabilities in Netcomm and TP-Link Routers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghc_r6dTPSXbjfP-DKmyP-gYyhCwnUAT8QQc2TBUOpwJg0jNAr4ZLNMP5HBJE44Ma3SEgvqPL8G-T89uUKWYfPRwFXBHIT_L2v5ffaIGDuzRiKIdo16s3I461E0J_K-KZpgS94pCo9R0Fiu-gF14TyRm187VZQzTsAWdLjhxlUVfEjWbe1yr1unP6Q/s790-rw-e365/router-hacking.png)

In a related development, CERT/CC also detailed two unpatched security vulnerabilities affecting TP-Link routers WR710N-V1-151022 and Archer-C5-V2-160201 that could lead to information disclosure ([CVE-2022-4499](https://nvd.nist.gov/vuln/detail/CVE-2022-4499)) and remote code execution ([CVE-2022-4498](https://nvd.nist.gov/vuln/detail/CVE-2022-4498)).

CVE-2022-4499 is also a side-channel attack targeting a function used to validate the entered credentials. "By measuring the response time of the vulnerable process, each byte of the username and password strings may be easier to guess," CERT/CC [said](https://kb.cert.org/vuls/id/572615).

Microsoft researcher James Hull has been acknowledged for disclosing the two bugs. The Hacker News has reached out to TP-Link for a comment, and we will update the story if we hear back.

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

[Netcomm](https://thehackernews.com/search/label/Netcomm)[network security](https://thehackernews.com/search/label/network%20security)[router security](https://thehackernews.com/search/label/router%20security)[software security](https://thehackernews.com/search/label/software%20security)[TP-LINK](https://thehackernews.com/search/label/TP-LINK)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data...