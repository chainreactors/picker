---
title: Cisco Warns of High-Severity Unpatched Flaw Affecting IP Phones Firmware
url: https://thehackernews.com/2022/12/cisco-warns-of-high-severity-unpatched.html
source: The Hacker News
date: 2022-12-11
fetch_date: 2025-10-04T01:13:04.668199
---

# Cisco Warns of High-Severity Unpatched Flaw Affecting IP Phones Firmware

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

# [Cisco Warns of High-Severity Unpatched Flaw Affecting IP Phones Firmware](https://thehackernews.com/2022/12/cisco-warns-of-high-severity-unpatched.html)

**Dec 10, 2022**Ravie LakshmananEnterprise Security / IP Phones

[![IP Phones Firmware](data:image/png;base64... "IP Phones Firmware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg74Qw8xnMGDesKJ9RG6vIb7BCCz4ByuSZenzTRoctwIU3Zry1M1z7V5e0YvCKQv7UHw4X5scCr-4WH4Rvc-qc8gem-oczmMxCnllb8AYiiLoXL6u5OuGguW6CPyb5P0Jd5gOQ0RjDMs0qemXVHhDuey41qp822u7Y2ANGq66PXpzWRGQ_uiC5fzklI/s790-rw-e365/phone-hacking.png)

Cisco has released a new security advisory warning of a high-severity flaw affecting IP Phone 7800 and 8800 Series firmware that could be potentially exploited by an unauthenticated attacker to cause remote code execution or a denial-of-service (DoS) condition.

The networking equipment major said it's working on a patch to address the vulnerability, which is tracked as **CVE-2022-20968** (CVSS score: 8.1) and stems from a case of insufficient input validation of received Cisco Discovery Protocol (CDP) packets.

CDP is a [proprietary](https://learningnetwork.cisco.com/s/article/cisco-discovery-protocol-cdp-x) [network-independent protocol](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/cdp/configuration/15-mt/cdp-15-mt-book/nm-cdp-discover.html) that is used for collecting information related to nearby, directly connected devices such as hardware, software, and device name, among others. It's enabled by default.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"An attacker could exploit this vulnerability by sending crafted Cisco Discovery Protocol traffic to an affected device," the company [said](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ipp-oobwrite-8cMF5r7U) in an alert published on December 8, 2022.

"A successful exploit could allow the attacker to cause a stack overflow, resulting in possible remote code execution or a denial of service (DoS) condition on an affected device."

Cisco IP phones running firmware version 14.2 and earlier are impacted. A patch is scheduled for release in January 2023, with the company stating that there are no updates or workarounds to remediate the issue.

However, on deployments that support both CDP and Link Layer Discovery Protocol ([LLDP](https://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol)) for neighbor discovery, users can opt to disable CDP so that the affected devices switch to LLDP for advertising their identity and capabilities to directly connected peers in a local area network (LAN).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This is not a trivial change and will require diligence on behalf of the enterprise to evaluate any potential impact to devices as well as the best approach to deploy this change in their enterprise," the company said.

It further cautioned that it's aware of the availability of a proof-of-concept (PoC) exploit and that the shortcoming has been publicly disclosed. There's no evidence that the vulnerability has been actively abused in the wild to date.

Qian Chen from the Codesafe Team of Legendsec at Qi'anxin Group has been credited with discovering and reporting the vulnerability.

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

[cisco](https://thehackernews.com/search/label/cisco)[Cisco IP Phones](https://thehackernews.com/search/label/Cisco%20IP%20Phones)[dos](https://thehackernews.com/search/label/dos)[Local Area Network](https://thehackernews.com/search/label/Local%20Area%20Network)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-mal...