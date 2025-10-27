---
title: HardBit ransomware tailors ransom to fit your cyber insurance payout
url: https://www.malwarebytes.com/blog/news/2023/02/hardbit-ransomware-tailors-ransom-to-fit-your-cyber-insurance-payout
source: Over Security - Cybersecurity news aggregator
date: 2023-02-24
fetch_date: 2025-10-04T07:59:27.969310
---

# HardBit ransomware tailors ransom to fit your cyber insurance payout

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

![Chained by ransomware](https://www.threatdown.com/wp-content/uploads/2023/02/asset_upload_file41896_259214.jpg?w=736)

[News](https://www.threatdown.com/blog/category/news/)

## HardBit ransomware tailors ransom to fit your cyber insurance payout

February 21, 2023

[Mark Stockley](https://www.threatdown.com/blog/author/mstockleymalwarebytes-com/)

Ransomware authors are wading into the cybersecurity insurance debate in a somewhat peculiar way. Specifically: [urging victims to disclose details of their insurance contract](https://www.bleepingcomputer.com/news/security/hardbit-ransomware-wants-insurance-details-to-set-the-perfect-price/), in order to tailor a ransom which will be beneficial to the company under attack.

## HardBit 2.0: dismantling a device piece by piece

The ransomware, called HardBit 2.0, has been in circulation since sometime around November last year. Although there is no specific information as to how it arrives on a network, once it gets there is performs typical ransomware operations:

* Encrypts files, branding them with the file’s custom logo
* Gathers system/network data
* Reduces overall security of affected systems
* Disables recovery options and tamper protection, turns off multiple Windows Defender features, and interferes with several other security features including real time monitoring and Windows services related to backups like the [Volume Shadow Copy Service](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service).

## What does the encryption warning message say?

HardBit 2.0 encrypts files and presents the following infection message on compromised desktops:

> All your important files are stolen and encrypted! All your files have been encrypted due to a security problem with your PC. If you want to restore them, please send your ID for us.
>
> Our contact information is written in the file “How to restore your files”.
>
> You have 48 hours to contact or pay us. After that, you will have to pay double.
>
> Please do not touch the key written under the help file in any way.

Just like [Mortal Kombat ransomware](https://www.malwarebytes.com/blog/news/2023/02/mortal-kombat-ransomware-forms-tag-team-partnership-with-laplas-clipper), the attackers ask those who are hijacked to use Tox Messenger to communicate. The authors claim to steal data as well as encrypt it, although there’s no dedicated leak site to exploit this particular angle. In this case, it may be that most organisations targeted by the group would be too distracted by their “unique” approach to ransom demands to care.

## A helping hand?

We’ve seen ransomware authors claim to care about their victims in the past. Some ransomware groups will remove themselves from impacted entities such as hospitals or critical services once those stories go public. Your mileage may vary with regard to whether this is a face saving PR move, or if they genuinely care about having going a little bit too far.

Here, they’re going out of their way to “help” by quizzing victims about the specifics of their cyber insurance policy. According to Varonis, there’s [no outright demand for Bitcoin or another form of cryptocurrency](https://www.varonis.com/blog/hardbit-2.0-ransomware). In its place is a long, rambling ransom note.

The note explains at length that their final ransom demand will be adjusted to ensure it falls inside of the insurance claim requirements. It paints the insurer as some sort of bad actor wanting to withhold money from the victim. If the scammers are told in private what the insurance total is, they’ll be able to ensure their demand for money is

**A)** at the top end limit of the ransom payout scale provided and

**B)** does not go *past* this limit, so the affected company receives every cent they’ve paid out. This is designed to be a mutually beneficial deal for both parties, as victim and attacker will receive as much as they possibly can.

There is, of course, no guarantee that the ra...