---
title: GoAnywhere zero-day opened door to Clop ransomware
url: https://www.malwarebytes.com/blog/news/2023/02/goanywhere-zero-day-opened-door-to-clop-ransomware
source: Over Security - Cybersecurity news aggregator
date: 2023-02-22
fetch_date: 2025-10-04T07:45:09.447903
---

# GoAnywhere zero-day opened door to Clop ransomware

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

![secure file transfer](https://www.threatdown.com/wp-content/uploads/2023/02/asset_upload_file54768_259182.jpg?w=736)

[News](https://www.threatdown.com/blog/category/news/), [Ransomware](https://www.threatdown.com/blog/category/ransomware/)

## GoAnywhere zero-day opened door to Clop ransomware

February 20, 2023

[Mark Stockley](https://www.threatdown.com/blog/author/mstockleymalwarebytes-com/)

A semi-active ransomware group has claimed it is behind a string of attacks which have taken advantage of a [zero-day vulnerability](https://www.malwarebytes.com/blog/news/2023/02/update-now-goanywhere-mft-zero-day-patched) in GoAywhere MFT.

The Russian-linked Clop ransomware group says it was able to remotely attack private systems using exposed GoAnywhere MFT administration consoles accessible on the public internet. BleepingComputer [reports](https://www.bleepingcomputer.com/news/security/clop-ransomware-claims-it-breached-130-orgs-using-goanywhere-zero-day/) the group claimed they gained access and stole data from the GoAnywhere servers of at least 130 organizations.

One of Clop’s victims was Community Health Systems (CHS), a Fortune 500 healthcare services provider in the US. It recently [filed a Form 8-K](https://www.sec.gov/Archives/edgar/data/1108109/000119312523035789/d422693d8k.htm) to the Securities and Exchange Commission (SEC), announcing the compromise of its system and disclosure of company data, including protected health information (PHI) and personal information (PI) of certain patients. CHS didn’t disclose the specific number of affected individuals.

Since the release of the emergency patch, Fortra has revealed that attackers also breached some of its MFTaaS instances during the attack.

The Cybersecurity & Infrastructure Security Agency (CISA) recently added [CVE-2023-0669](https://nvd.nist.gov/vuln/detail/CVE-2023-0669) to its [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), a list of software flaws that federal organizations must patch within two weeks. It’s helpful for non-federal [organizations to refer to](https://www.malwarebytes.com/blog/news/2023/02/how-the-cisa-catalog-can-help-our-organization) as well, in order to help prioritize their patching.

Thankfully, an [emergency patch](https://my.goanywhere.com/webclient/ViewSecurityAdvisories.xhtml) (7.1.2) has been available since last week.

As well as the patch, GoAnywhere clients are also encouraged to:

* Rotate the master encryption key.
* Reset credentials.
* Review audit logs and delete suspicious admin or user accounts.
* Contact Fortra support by going to its [portal](https://my.goanywhere.com/), emailing technicians at goanywhere.support@helpsystems.com, or phoning them at 402-944-4242.

## How to avoid ransomware

* **Block common forms of entry**. Create a plan for [patching vulnerabilities](https://www.threatdown.com/products/patch-management/) in internet-facing systems quickly; disable or [harden remote access](https://www.malwarebytes.com/blog/news/2022/03/blunting-rdp-brute-force-attacks-with-rate-limiting) like RDP and VPNs; use [endpoint security software](https://www.threatdown.com/products/endpoint-detection-and-response/) that can detect exploits and malware used to deliver ransomware.
* **Detect intrusions**. Make it harder for intruders to operate inside your organization by segmenting networks and assigning access rights prudently. Use [EDR](https://www.threatdown.com/products/endpoint-detection-and-response/) or [MDR](https://www.threatdown.com/products/managed-detection-and-response/) to detect unusual activity before an attack occurs.
* **Stop malicious encryption**. Deploy Endpoint Detection and Response software like [Malwarebytes EDR](https://www.threatdown.com/products/endpoint-detection-and-response/) that uses multiple different detection techniques to identify ransomware.
* **Create offsite, offline backups**. Keep backups offsite and offline, beyond the reach of ...