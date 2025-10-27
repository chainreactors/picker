---
title: Update now! February's Patch Tuesday tackles three zero-days
url: https://www.malwarebytes.com/blog/news/2023/02/patch-now-patch-tuesday-february-tackles-three-zero-days
source: Over Security - Cybersecurity news aggregator
date: 2023-02-17
fetch_date: 2025-10-04T06:54:19.272987
---

# Update now! February's Patch Tuesday tackles three zero-days

[ ]

[![ThreatDown Powered by Malwarebytes](https://www.threatdown.com/wp-content/themes/mbc/images/logo-header-threatdown-horizontal.svg)](https://www.threatdown.com/)

SUPPORT

* [Nebula support](https://support.threatdown.com/hc/en-us/)
* [OneView support](https://support.threatdown.com/hc/en-us/p/oneview)

SIGN IN

* [Nebula sign in](https://cloud.threatdown.com/auth/login)
* [OneView sign in](https://oneview.threatdown.com/)
* [Partner Portal sign in](https://partners.malwarebytes.com/English/)

[ ]

## Products

< Products

* ## Products
* [Endpoint Detection & Response (EDR)](/products/endpoint-detection-and-response/)
* [Endpoint Protection](/products/endpoint-protection/)
* [Vulnerability Assessment](/products/vulnerability-assessment/)
* [Patch Management](/products/patch-management/)
* [Application Block](/products/application-block/)
* [DNS Filtering](/products/dns-filtering/)
* [Mobile Security](/products/mobile-security/)
* [Email Security](/products/email-security/)

* ## Services
* [Managed Detection & Response (MDR)](/products/managed-detection-and-response/)
* [Managed Threat Hunting](/products/managed-threat-hunting/)
* [Premium Support](/products/premium-support/)

* ## Features
* [Browser Phishing Protection](/products/browser-phishing-protection/)
* [Firewall Management](/products/firewall-management/)
* [Security Advisor](/products/security-advisor/)

* ## Platforms
* [Nebula](/products/nebula/)
* Manage your organization’s endpoint security in a single-tenant console

  [Nebula customer sign in >](https://cloud.threatdown.com/auth/login)
* [OneView](/products/oneview/)
* Provides MSPs centralized visibility and management capabilities across customer sites

  [OneView customer sign in >](https://oneview.threatdown.com/auth/login)

[ ]

## Partners

< Partners

* [Explore Partnerships](/partner-program/)
* Review program benefits, innovative technology, channel first mentality
* [Managed Service Providers](/partner-program/msp/)
* Everything MSPs need to run their business seamlessly

* [Technology Partners](/technology-integrations/)
* Explore our technology integrations
* [Resellers](/partner-program/partner-reseller/)
* Build growth, profitability, and customer loyalty

* ![](https://www.threatdown.com/wp-content/uploads/2023/11/px-center.png?w=356)
* Retain and grow your business with tools, education, and support in the partner experience center.

  [Sign in to PXC >](https://partners.threatdown.com/English/%20)

[ ]

## Resources

< Resources

* [Threat Center](/threat-center/)
* Learn about the latest threat news
* [Reports](/threat-center/reports/)
* [Threat Detections](/threat-detections/)
* [Executive POV](/threat-center/executive-pov/)
* [Glossary](/glossary/)
* [Blog](/blog/)

* [Resource Center](/resources/)
* Learn more about ThreatDown
* [ThreatDown News](/press/)
* [Case Studies](/resources/categories/case-studies/)
* [Reviews](/resources/categories/products/)
* [Cybersecurity Tips & Tricks](/resources/categories/cybersecurity-tips-tricks/)
* [Webinars](/resources/categories/webinars/)
* [About Us](/about-us/)

* ![2025 State of Ransomware: Inside a record-breaking year of ransomware attacks](https://www.threatdown.com/wp-content/uploads/2025/08/2025-state-of-ransomware.png?w=1246)
* Discover a record-breaking year of attacks where ransomware became decentralized and unpredictable, spreading further than ever before.

  [Download now >](https://www.threatdown.com/dl-state-of-ransomware-2025/)

[Pricing](/pricing/)

[ ]

## Why ThreatDown

< Why ThreatDown

* ## Why ThreatDown
* [About Us](/about-us/)
* [ThreatDown vs. Competition](/vs/)
* [Case Studies](/resources/categories/case-studies/)

* ![](https://www.threatdown.com/wp-content/uploads/2025/04/product-of-the-year-nav.png?w=712)
* ThreatDown named Product of the Year by MRG Effitas.

  [Learn more >](https://www.threatdown.com/blog/product-of-the-year/)

[Get a quote](/custom-quote/)

[Buy now](/pricing/)

[Home](/)
>
[Blog](/blog/)

![several types of patches](https://www.threatdown.com/wp-content/uploads/2023/02/asset_upload_file851_259133.png?w=736)

[Exploits and vulnerabilities](https://www.threatdown.com/blog/category/exploits-and-vulnerabilities/), [News](https://www.threatdown.com/blog/category/news/)

## Update now! February’s Patch Tuesday tackles three zero-days

February 15, 2023

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

The Patch Tuesday roundup from Microsoft for February 2023 includes three [zero-days](https://www.malwarebytes.com/zero-day). Not exactly what we had in mind for Valentine’s Day.

Microsoft [classifies a vulnerability as a zero-day](https://www.malwarebytes.com/blog/news/2022/12/4-times-security-vulnerabilities-were-blown-out-of-proportion-in-2022) if it is publicly disclosed or actively exploited with no official fix available. As far as we can tell, only two of the vulnerabilities were actually exploited in the wild.

The zero-days patched in these updates are:

## Graphics component

[CVE-2023-21823](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21823): A Windows Graphics Component remote code execution (RCE) vulnerability. An attacker who successfully exploited this vulnerability could execute commands with SYSTEM privileges.

Important to note here that this update comes from the Microsoft Store. So users that have disabled automatic updates for the Microsoft Store have to get the update through the Microsoft Store by following the guide titled [Get updates for apps and games in Microsoft Store](https://support.google.com/googleplay/answer/113412?hl=en). Be sure to select the tab for the operating system installed on your device to search for updates.

The [Microsoft update guide for this vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21823) specifically mentions OneNote for Android. At Malwarebytes, we’ve recently seen ASyncRAT campaigns using malicious OneNote (.one) attachments, so we hope to see that this update puts an end to that method of infection.

## Microsoft Publisher

[CVE-2023-21715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21715): A Microsoft Publisher security features bypass vulnerability. An attacker who successfully exploited this vulnerability could bypass Office macro policies in Microsoft Publisher which are used to block untrusted or malicious files. The attack itself has to be carried out locally by a user with authentication to the targeted system. An authenticated attacker could exploit the vulnerability by convincing a victim, through social engineering, to download and open a specially crafted file from a website which could lead to a local attack on the victim computer.

Although that makes it sound hard to abuse, Microsoft says it has detected exploitation of this vulnerability.

## Windows Common Log File System Driver

[CVE-2023-23376](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23376): A Windows Common Log File System Driver elevation of privilege (EoP) vulnerability. An attacker who successfully exploited this vulnerability could gain SYSTEM privileges. This means it can be very useful in a chain of vulnerabilities, but Microsoft gives no clues about any other vulnerabilities this EoP has been used in combination with.

## Other patched vulnerabilities

Exchange Server: included are patches for three remote code execution flaws that are labelled as likely to be exploited. These vulnerabilities listed as [CVE-2023-21706](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21706), [CVE-2023-21707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21707), and [CVE-2023-21529](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21529) all require authentication.

Microsoft Word: an RCE vulnerability listed as [CVE-2023-21716](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21716) with a [CVSS](https://www.threatdown.com/blog/how-cvss-works-characterizing-and-scoring...