---
title: Silence is golden partner for Truebot and Clop ransomware
url: https://www.malwarebytes.com/blog/news/2022/12/silence-is-golden-partner-for-truebot-and-clop-ransomware
source: Over Security - Cybersecurity news aggregator
date: 2022-12-15
fetch_date: 2025-10-04T01:34:23.094636
---

# Silence is golden partner for Truebot and Clop ransomware

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

![man holding a finger across his lips](https://www.threatdown.com/wp-content/uploads/2022/12/asset_upload_file78828_252142.png?w=736)

[News](https://www.threatdown.com/blog/category/news/), [Ransomware](https://www.threatdown.com/blog/category/ransomware/)

## Silence is golden partner for Truebot and Clop ransomware

December 13, 2022

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

A recent rise in the number of Truebot infections has been attributed to a threat actor known as the Silence Group. The Silence Group is an [initial access broker (IAB)](https://www.threatdown.com/blog/initial-access-brokers-iabs-3-ways-they-get-into-corporate-networks-and-how-to-stop-them/) that frequently changes tools and tactics to stay on top of the game. An IAB’s primary task is to find a weakness or vulnerability, create a foothold in a network, and do some exploratory work to find out how attractive the target is. Once this is done they can sell the access to another threat actor, like a ransomware group. For these tasks Truebot is the tool of choice in the Silence Group.

The Silence Group seems to have a strong relation with the group behind Clop ransomware, often referenced as [TA505](https://attack.mitre.org/groups/G0092/). Which, in turn, has a large overlap with the FIN11 group.

## Truebot

The [researchers](https://blog.talosintelligence.com/breaking-the-silence-recent-truebot-activity/) identified two separate Truebot botnets. One of which appears to be focused on the US, while the other is predominantly focused at Mexico, Pakistan, and Brazil.

We touched on the second one when we wrote about the [recent activities of the Raspberry Robin worm](https://www.threatdown.com/blog/raspberry-robin-worm-used-as-ransomware-prelude/). The use of this worm, in combination with an attack vector leveraging a Netwrix vulnerability, seems the have laid the ground work for the creation of a botnet of over 1,000 systems that is distributed worldwide.

The other botnet is almost exclusively composed of Windows servers, directly connected to the internet, and exposes several Windows services such as SMB, RDP, and WinRM. The attack vector that was used to establish this botnet has not yet been identified, although the researchers are confident that it is different from those used for the other botnet, Raspberry Robin and the Netwrix vulnerability ([CVE-2022-31199](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31199)).

## New version

At its core, Truebot is a [Trojan.Downloader](https://www.malwarebytes.com/blog/detections/trojan-downloader). As such, it is an ideal malware for IAB groups that want to plant a backdoor on a system and do some basic reconnaissance of the network. For those purposes, this new version of Truebot collects this information: a screenshot, the computer name, the local network name, and active directory trust relations. Active Directory trust relations allow organizations to share users and resources across domains.

What’s also new is that this version is now capable of loading and executing additional modules and shellcodes in memory, making the payloads [fileless malware](https://www.threatdown.com/blog/what-is-fileless-malware/) which is less likely to be detected.

## Exfiltration

Besides the usual suspects designed to act as a backdoor, Cobalt Strike and Grace, the researchers also found a new data exfiltration tool. Finding Grace as a payload seems to confirm the close ties between the Silence Group and TA505 since Grace was almost exclusively used by TA505.

The exfiltration tool, dubbed Teleport, was used extensively by the attackers to steal information from the network. It seems to be a custom data exfiltration tool built in C++ , containing several features that make the process of data exfiltration easier and stealthier. It has some features that are not commonly found in remote copying tools but which make it very useful to an attacker stealthily exfiltrating data....