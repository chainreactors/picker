---
title: Update vRealize now! VMware patches critical RCE vulnerabilities
url: https://www.malwarebytes.com/blog/news/2023/01/update-vrealize-now-vmware-patches-critical-rce-vulnerabilities
source: Over Security - Cybersecurity news aggregator
date: 2023-01-30
fetch_date: 2025-10-04T05:10:58.097935
---

# Update vRealize now! VMware patches critical RCE vulnerabilities

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

![VMware logo](https://www.threatdown.com/wp-content/uploads/2023/01/asset_upload_file51108_255776.png?w=736)

[News](https://www.threatdown.com/blog/category/news/), [Exploits and vulnerabilities](https://www.threatdown.com/blog/category/exploits-and-vulnerabilities/)

## Update vRealize now! VMware patches critical RCE vulnerabilities

January 25, 2023

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

VMware has issued a [security advisory for vRealize Log Insight](https://www.vmware.com/security/advisories/VMSA-2023-0001.html) that covers four vulnerabilities reported privately by the [Zero Day Initiative (ZDI)](https://www.zerodayinitiative.com). Two of these vulnerabilities are rated as critical.

The issues have been fixed on [vRealize Log Insight 8.10.2](https://docs.vmware.com/en/vRealize-Log-Insight/8.10/rn/vrealize-log-insight-810-release-notes/index.html), so users should [upgrade to the latest version](https://docs.vmware.com/en/vRealize-Log-Insight/8.10/com.vmware.log-insight.administration.doc/GUID-A6CAC5D7-7BE0-4F62-8A03-80F6C3327E8A.html). For administrators that are unable or unwilling to apply the update, there are [workaround instructions](https://kb.vmware.com/s/article/90635) available for the two critical vulnerabilities.

## vRealize

VMware’s vRealize Log Insight—which was recently renamed to [VMware Aria Operations for Logs](https://www.vmware.com/products/aria-operations-for-logs.html)—is a log collection and analytics appliance that enables administrators to monitor application logs, network traces, configuration files, messages and performance data. It helps them to troubleshoot private, hybrid, and multi-cloud environments, as well as perform security auditing and compliance testing. This is accomplished by placing an agent on each monitored device that collects analytics data on performance, state and logs.

## Vulnerabilities

The first critical vulnerability is [CVE-2022-31706](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31706), a directory traversal vulnerability with a [CVSS score](https://www.threatdown.com/blog/how-cvss-works-characterizing-and-scoring-vulnerabilities/) of 9.8 out of 10. Directory or path traversal flaws allow attackers to read, and possibly write to, restricted files by inputting path traversal sequences like ../ into file or directory paths. In this case, an unauthenticated, malicious actor can inject files into the operating system of an impacted appliance, which can result in remote code execution.

The other critical vulnerability is [CVE-2022-31704](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31704), a broken access control vulnerability which also has a CVSS score of 9.8. It allows an unauthenticated, malicious actor to inject files into the operating system of an impacted appliance which can result in remote code execution. Access control intention is to enforce policies which make sure that users cannot act outside of their intended permissions.

The other two vulnerabilities are less critical, but they can result in a denial of service or information disclosure in the hands of an attacker.

## Urgency

None of the vulnerabilities are known to be exploited in the wild, but VMware solutions are an attractive target for threat actors. And since both critical vulnerabilities offer unauthenticated threat actors an opportunity for remote code execution, it’s recommended to apply the patches at your earliest convenience or use the workaround while waiting for a suitable moment.

Earlier this month, VMware addressed multiple vulnerabilities in VMware vRealize Network Insight (vRNI). One of these vulnerabilities, listed as [CVE-2022-31702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31702) also had a CVSS score of 9.8. It allowed a malicious actor with network access to the vRNI REST API can execute commands without authentication.

---

**We don’t just report on threats—we remove them**

Cybersecurity risk...