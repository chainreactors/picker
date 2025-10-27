---
title: Update now! October patch Tuesday fixes actively used zero-day...but not the one you expected
url: https://www.malwarebytes.com/blog/news/2022/10/update-now-october-patch-tuesday-fixes-actively-used-zero-day
source: Over Security - Cybersecurity news aggregator
date: 2022-10-14
fetch_date: 2025-10-03T19:52:23.237945
---

# Update now! October patch Tuesday fixes actively used zero-day...but not the one you expected

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

![Several types of patches](https://www.threatdown.com/wp-content/uploads/2022/10/asset_upload_file69692_241189.png?w=736)

[News](https://www.threatdown.com/blog/category/news/), [Exploits and vulnerabilities](https://www.threatdown.com/blog/category/exploits-and-vulnerabilities/)

## Update now! October patch Tuesday fixes actively used zero-day…but not the one you expected

October 12, 2022

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

Microsoft fixed 84 vulnerabilities in its October 2022 Patch Tuesday updates. Thirteen of them received the classification ‘Critical’. Among them are a zero-day vulnerability that’s being actively exploited, and another that hasn’t been spotted in the wild yet.

The bad news is that the much-desired fix for the “ProxyNotShell” [Exchange vulnerabilities](https://www.malwarebytes.com/blog/news/2022/09/two-new-exchange-zero-days-that-look-and-feel-like-proxyshell-part-2) was not included.

## What was fixed

A widely accepted [definition for a zero-day](https://en.wikipedia.org/wiki/Zero-day_%28computing%29) is a computer-software vulnerability previously unknown to those who should be interested in its mitigation, such as the software vendor. Until the vulnerability is mitigated, hackers can exploit it to adversely affect programs, data, computers or a network.

As such, a publicly known vulnerability is called a zero-day even if there is no known actively used exploitation for it.

The actively exploited vulnerability in this month’s batch is [CVE-2022-41033](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41033), a vulnerability with a [CVSS score](https://www.threatdown.com/blog/how-cvss-works-characterizing-and-scoring-vulnerabilities/) of 7.8 out of 10. This is described as a ‘Windows COM+ Event System Service Elevation of Privileges (EoP)’ vulnerability, which gives an attacker the potential to obtain SYSTEM privileges after successful exploitation.

This type of vulnerability usually comes into play once an attacker has gained an initial foothold on a system. They can then use this vulnerability to gain more permissions and expand their access to the compromised system.

Another publicly disclosed vulnerability that gets a fix is [CVE-2022-41043](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41043), a Microsoft Office Information Disclosure vulnerability. Affected products are Microsoft Office LTSC for Mac 2021 and Microsoft Office 2019 for Mac. Microsoft says attackers could use this vulnerability to gain access to users’ authentication tokens.

## What wasn’t fixed

The Exchange Server “ProxyNotShell” vulnerabilities, [CVE-2022-41040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41040) and [CVE-2022-41082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41082), were not fixed in this round of updates. One is a Server-Side Request Forgery (SSRF) vulnerability and the other a remote code execution (RCE) vulnerability that exists when PowerShell is accessible to the attacker. The two can be chained together into an attack.

Microsoft says it will release updates for these vulnerabilities when they are ready. In the meantime, you should read [this blog post](https://techcommunity.microsoft.com/t5/exchange-team-blog/customer-guidance-for-reported-zero-day-vulnerabilities-in/ba-p/3641494) to learn about mitigations for those vulnerabilities.

## Other vendors

Other vendors have synchronized their periodic updates with Microsoft. Here are few major ones:

* Adobe released [security updates](Adobe%20also%20released%20security%20updates%20to%20fix%2029%20vulnerabilities) to fix 29 vulnerabilities in several products.
* Apple published [iOS 16.0.3](https://support.apple.com/en-us/HT213480).
* Fortinet released important [security updates](https://www.bleepingcomputer.com/news/security/fortinet-warns-admins-to-patch-critical-auth-bypass-bug-immediately/).
* Google patched several vulnerabilities for [Android](https://www.ma...