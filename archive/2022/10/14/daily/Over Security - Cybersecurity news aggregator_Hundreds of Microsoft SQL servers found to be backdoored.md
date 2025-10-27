---
title: Hundreds of Microsoft SQL servers found to be backdoored
url: https://www.malwarebytes.com/blog/news/2022/10/hundreds-of-microsoft-sql-servers-found-to-be-backdoored
source: Over Security - Cybersecurity news aggregator
date: 2022-10-14
fetch_date: 2025-10-03T19:51:57.966690
---

# Hundreds of Microsoft SQL servers found to be backdoored

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

![SQL](https://www.threatdown.com/wp-content/uploads/2022/10/asset_upload_file53460_239637.png?w=736)

[News](https://www.threatdown.com/blog/category/news/)

## Hundreds of Microsoft SQL servers found to be backdoored

October 6, 2022

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

Researchers at [DCSO CyTec](https://medium.com/%40DCSO_CyTec/mssql-meet-maggie-898773df3b01) recently found a backdoor that specifically targets Microsoft SQL servers. The malware acts as an Extended Stored Procedure, which is a special type of extension used by Microsoft SQL servers.

After scanning approximately 600,000 servers worldwide, they found 285 servers infected with this backdoor, in 42 countries. The distribution shows a clear focus on the Asia-Pacific region.

## Extended Stored Procedure

To understand how the malware works it is necessary to understand the [role of an Extended Stored Procedure on a SQL server](https://learn.microsoft.com/en-us/sql/relational-databases/extended-stored-procedures-programming/how-extended-stored-procedures-work?view=sql-server-ver16). Extended stored procedures are dynamic link library (DLL) files which are referenced by the SQL Server by having the extended stored procedure created, which then references functions or procedures within the DLL. The DLLs that are behind the extended stored procedures are typically created in a lower level language like C or C++.

Basically, the functions stored in the DLL can be triggered from the client application to Microsoft SQL Server and the extended stored procedure passes result sets and return parameters back to the server through the Extended Stored Procedure Application Programming Interface (API).

## Maggie

Based on artifacts found in the malware, DCSO CyTec has dubbed this threat Maggie. According to its export directory, the file calls itself `sqlmaggieAntiVirus_64.dll` and only offers a single export called

```
maggie
```

.

Maggie uses the Extended Stored Procedure API to implement a fully functional backdoor controlled only using SQL queries. But to establish the connection an attacker has to drop the backdoor in a directory accessible by the Microsoft SQL server, and has to have valid credentials to load the Maggie Extended Stored Procedure into the server. Otherwise the server will never query the DLL for any functions. For now, it is unknown how the initial infection takes place. But there are some [known vulnerabilities for Microsoft SQL server](https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-251/Microsoft-Sql-Server.html) that may not have been patched by every organization.

## Capabilities

Once installed, Maggie offers a variety of commands that allow the attacker to query for system information, interact with files and folders, execute programs, and to perform various network-related functions, including setting up port forwarding to make Maggie act as a bridge head into the server’s network environment.

Once enabled, Maggie separates the attacker’s connections from the others, so legitimate users are able to use the server without any interference by Maggie. This reduces the chance of the users noticing something is wrong. The separation is done based on an IP mask that redirects any incoming connection to a set IP and port, if the source IP address matches the user-specified IP mask.

## Brute force

Maggie’s command set also includes two commands that seem designed to allow it to brute force logins to other MSSQL servers. To start a brute force scan, the threat actor has to specify a target host, user and password list file previously uploaded to the infected server.

The backdoor logs successful logins and then checks whether they have administrator permissions. It is logical to assume that this is intended to increase the number of victims. What the underlying purpose of Maggie is, remains to be seen.

## Targets

Since the backdoor depends on the setup of a Microsoft SQL server, ...