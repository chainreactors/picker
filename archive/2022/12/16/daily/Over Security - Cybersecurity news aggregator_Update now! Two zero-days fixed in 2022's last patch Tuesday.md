---
title: Update now! Two zero-days fixed in 2022's last patch Tuesday
url: https://www.malwarebytes.com/blog/news/2022/12/update-now-the-last-patch-tuesday-of-2022-fixes-two-zero-days
source: Over Security - Cybersecurity news aggregator
date: 2022-12-16
fetch_date: 2025-10-04T01:41:48.175522
---

# Update now! Two zero-days fixed in 2022's last patch Tuesday

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

![different types of patches](https://www.threatdown.com/wp-content/uploads/2022/12/asset_upload_file95422_252220.png?w=736)

[Exploits and vulnerabilities](https://www.threatdown.com/blog/category/exploits-and-vulnerabilities/), [News](https://www.threatdown.com/blog/category/news/)

## Update now! Two zero-days fixed in 2022’s last patch Tuesday

December 14, 2022

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

In numbers, the patch Tuesday of December 2022 is a relatively light one for Windows users. Microsoft patched 48 vulnerabilities with only six considered critical. But numbers are only half the story. Two of the updates are zero-days with one of them known to be actively exploited.

## Windows SmartScreen

Publicly disclosed computer security flaws are listed in the Common Vulnerabilities and Exposures (CVE) database. Its goal is to make it easier to share data across separate vulnerability capabilities (tools, databases, and services).

The vulnerability that is [exploited in the wild](https://www.malwarebytes.com/blog/news/2022/11/qbot-uses-zero-day-motw-bypass-in-phishing-campaign) is listed under [CVE-2022-44698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44698) and described as a Windows SmartScreen Security Feature bypass vulnerability. To understand how this works, you need to understand that files can be cryptographically signed in order to confirm who created them, and to confirm that they have not been changed since they were signed. [Mark-of-the-Web (MOTW)](https://www.malwarebytes.com/blog/news/2022/10/malware-authors-use-malformed-signature-trick-to-bypass-mark-of-the-web) is the name for the Windows technology that warns users of potential harm when downloading and opening a file from the internet or an email attachment. In other words, it’s a safety precaution in the form of a reminder that the user is about to use a risky file that might harm their computer. The problem is that a malformed signature bypasses all the warnings you should get, so you are bound to assume everything is dandy while it’s not.

## DirectX Graphics Kernel

The other zero-day is labeled as “Exploitation Less Likely” but information about the vulnerability has been made public. The vulnerability is listed as [CVE-2022-44710](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44710) and described as a DirectX Graphics Kernel Elevation of Privilege (EoP) vulnerability. To successfully exploit it the attacker would need to win a race condition. But if they succeed they could gain SYSTEM privileges.

A race condition, or race hazard, is the behavior of a system where the output depends on the sequence or timing of other uncontrollable events. It becomes a bug when events do not happen in the order the programmer intended. Sometimes these bugs can be exploited when the outcome is predictable and works to the attackers’ advantage.

## Windows Secure Socket Tunneling Protocol

Two critical vulnerabilities we want to highlight were found in the Windows Secure Socket Tunneling Protocol (SSTP). [CVE-2022-44670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44670)and [CVE-2022-44676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44676)are remote code execution (RCE) vulnerabilities. Successful exploitation of these vulnerabilities requires an attacker to win a race condition but when successful could enable an attacker to remotely execute code on a remote access server (RAS).

A RAS is a type of server that provides a suite of services to remotely connected users over a network or the Internet. It operates as a remote gateway or central server that connects remote users with an organization’s internal local area network (LAN).

## PowerShell

One more vulnerability we want to highlight because exploitation is more likely is listed as [CVE-2022-41076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41076) and described as a PowerShell RCE vulnerability. Successfu...