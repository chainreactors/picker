---
title: Living Off the Land (LOTL) attacks: Detecting ransomware gangs hiding in plain sight
url: https://www.malwarebytes.com/blog/business/2023/04/living-off-the-land-lotl-attacks-detecting-ransomware-gangs-hiding-in-plain-sight
source: Over Security - Cybersecurity news aggregator
date: 2023-04-19
fetch_date: 2025-10-04T11:36:30.075551
---

# Living Off the Land (LOTL) attacks: Detecting ransomware gangs hiding in plain sight

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

![](https://www.threatdown.com/wp-content/uploads/2024/04/LOTL_Attacks.png?w=1024)

[Ransomware](https://www.threatdown.com/blog/category/ransomware/)

# Living off the Land (LOTL) attacks: Detecting ransomware gangs hiding in plain sight

April 14, 2025

[Bill Cozens](https://www.threatdown.com/blog/author/wcozensmalwarebytes-com/)

Ransomware-as-a-service (RaaS) gangs have been making headlines globally for years with their disruptive attacks on organizations.

Sometimes, though, it’s not enough to merely know about the problem.

In order to truly protect ourselves from RaaS gangs, we have to ‘peel back the onion’, so to speak, and get a closer look at how, exactly, they behave. If we know how RaaS gangs evade detection once in a network, for example, we may be able to kick them out before they can do any damage.

One of the most concerning behaviors we’ve observed from RaaS gangs is their use of **Living off the Land (LOTL) attacks, where attackers leverage legitimate tools to evade detection, steal data, and more.**

Let’s dive into the dangers of LOTL attacks in RaaS operations and provide guidance for under-resourced IT teams on how to detect and block such threats.

## The deceptive nature of LOTL attacks

In an ideal world, IT teams whose organizations are under attack would have clear and direct evidence of the malicious activity.

For example, if unusual network connections are being made to remote IP addresses associated with known malicious actors, then there’s little doubt that you’re under attack—enabling IT to put a halt to the behavior early on.

But now imagine you’re diligently monitoring a network for any signs of suspicious activity. As you scan a seemingly endless stream of logs, searching for any anomalies that could signal trouble, you notice some activity from PowerShell, a versatile and legitimate scripting tool.

![](https://www.threatdown.com/wp-content/uploads/2024/04/easset_upload_file24893_262894_e.webp?w=1024)

*Script Block Logging records all blocks of code as they’re executed by PowerShell, which could point you to suspicious activity. [Source](http://robwillis.info/2019/10/everything-you-need-to-know-to-get-started-logging-powershell/).*

Namely, there are **scripts using commands that an attacker *could* use to steal data from the company’s network**, but which also resemble legitimate tools used by IT professionals for various system administration tasks. Considering it’s regular business hours, you figure it’s part of a routine IT maintenance operation and move on.

But, lo and behold, it was a RaaS gang the whole time!

The attacker had studied the company’s environment and had a deep understanding of the tools and processes typically used by employees, and so they managed to avoid raising suspicion by blending in with typical PowerShell usage. By conducting the attack during normal business hours, the attackers also avoided any of the usual scrutiny that would come from moving across a network late at night.

This is exactly why LOTL attacks are so dangerous: **by mimicking normal behavior, LOTL attacks make it extremely difficult for IT teams and security solutions to detect any signs of malicious activities.** Experienced analysts, however, might be able to pick up on subtle anomalies or patterns that indicate a LOTL attack, leveraging their expertise and deep understanding of system behaviors.

On the other hand, new or under-resourced teams may struggle to identify such attacks due to a lack of experience or insufficient tools, leaving them vulnerable to these stealthy threats.

## 3 LOTL tools used by ransomware gangs

While attackers use a seemingly innumerable amount of legitimate tools for LOTL attacks, below are three of the most common ones we’ve seen the most active ransomware gangs using for their attacks.

| Tool | Used For | Used To | Used By |
| --- | --- | --- | --- |
| **PowerShell** | Versatile scripting language and shell framework for Windows systems | Execute malici...