---
title: Critical OpenSSL fix due Nov 1—what you need to know
url: https://www.malwarebytes.com/blog/news/2022/10/critical-openssl-fix-due-november-1st-get-ready-to-patch
source: Over Security - Cybersecurity news aggregator
date: 2022-10-29
fetch_date: 2025-10-03T21:16:09.914046
---

# Critical OpenSSL fix due Nov 1—what you need to know

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

![OpenSSLv3 critical fix](https://www.threatdown.com/wp-content/uploads/2022/10/asset_upload_file495_242872.jpg?w=736)

[News](https://www.threatdown.com/blog/category/news/)

## Critical OpenSSL fix due Nov 1—what you need to know

October 27, 2022

[Mark Stockley](https://www.threatdown.com/blog/author/mstockleymalwarebytes-com/)

A fix for a critical issue in OpenSSL is [on the way](https://mta.openssl.org/pipermail/openssl-announce/2022-October/000238.html), announced in advance of its release on November 1, 2022, in a four hour window between 13:00 UTC and 17:00 UTC. The release, version 3.0.7, will address a critical vulnerability for all versions of the software starting with a 3. Versions starting with a 1 are unaffected. A separate release for that branch of the software, version 1.1.1, is scheduled for the same day but it is a [bug fix](https://mta.openssl.org/pipermail/openssl-announce/2022-October/000240.html) and is not related to this issue.

This advance notice is designed to give a little time for organisations and individuals to get themselves ready for the upcoming critical update:

> That's our policy <https://t.co/pNLA4Ce4yV> to provide folks with a date they know to be ready to parse an advisory and see if the issue affects them. Given the number of changes in 3.0 and the lack of any other context information, such scouring is very highly unlikely.
>
> — Mark J Cox (@iamamoose) [October 26, 2022](https://twitter.com/iamamoose/status/1585167771838869505?ref_src=twsrc%5Etfw)

This release has attracted a lot of attention because this is only the second time the OpenSSL team has marked an issue CRITICAL since it introduced its issue severity criteria in 2014.

OpenSSL only labels vulnerabilities as critical if they meet the following criteria:

The OpenSSL project describes its software as a “full-featured toolkit for general-purpose cryptography and secure communication”—a sort of cryptographic Swiss army knife. It is extremely widely used, either as a standalone application or embedded in other applications. Linux, FreeBSD, and macOS all come with some version of it, and it can be installed on Windows.

Version 3.0.0 was [released just over a year ago](https://www.openssl.org/blog/blog/2021/09/07/OpenSSL3.Final/), in September 2021. Version 1 remains [much more widely used](https://webtechsurvey.com/technology/openssl/versions), but version 3 is used by a number of popular Linux distributions, including CentOS Stream 9, Red Hat Enterprise Linux 9 (RHEL 9), Ubuntu 22.10, Ubuntu 22.04 LTS, and Fedora Rawhide.

The Fedora Linux 37 release may be held up to include fixes for the vulnerability, and other responsible vendors are likely to move quickly to included updated versions in their software.

> Heads up: we are very likely to slip the official Fedora Linux 37 release in order to integrate fixes for the upcoming critical openssl vulnerability. Official decision on this tomorrow.
>
> — Matthew Miller (@mattdm@hachyderm.io) (@mattdm) [October 26, 2022](https://twitter.com/mattdm/status/1585285318265262081?ref_src=twsrc%5Etfw)

If you have access to a command line, you discover what version you are using by punching in:

```
openssl version
```

If you have OpenSSL installed, it will return the version number and release date. If your version number starts with a 3, this critical issue affects you. In addition to this check, you may need to dig around for non-standard installations, and you may be running software or appliances that include OpenSSL too. Keep an eye out for communications from your software suppliers, particularly those that supply Internet-facing software or hardware.

The only other OpenSSL issue with a CRITICAL rating was [CVE-2016-6309](https://nvd.nist.gov/vuln/detail/CVE-2016-6309) in 2016. The biggest OpenSSL issue of all though was Heartbleed, which predates OpenSSL’s severity criteria. Heartbleed allowed [remote attackers to expose sensitive data](https://www.cisa.gov/uscert/ncas/aler...