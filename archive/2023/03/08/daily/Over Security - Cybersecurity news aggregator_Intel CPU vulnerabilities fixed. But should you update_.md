---
title: Intel CPU vulnerabilities fixed. But should you update?
url: https://www.malwarebytes.com/blog/news/2023/03/intel-cpu-vulnerabilities-fixed-but-should-you-update
source: Over Security - Cybersecurity news aggregator
date: 2023-03-08
fetch_date: 2025-10-04T08:57:04.183042
---

# Intel CPU vulnerabilities fixed. But should you update?

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

![](https://www.threatdown.com/wp-content/uploads/2024/04/intel_cpu_vulnerabilities_fixed_resized.png?w=1024)

[Threat Intelligence](https://www.threatdown.com/blog/category/threat-intelligence/)

# Intel CPU vulnerabilities fixed. But should you update?

March 6, 2023

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

Microsoft has released out of band updates for information disclosure vulnerabilities in Intel CPUs. The normal gut reaction would be to install out of band updates as soon as possible. Microsoft wouldn’t be releasing the updates ahead of the regular cycle without good reason, would it?

Well, maybe there are good reasons, but the number of users that would have to worry about these vulnerabilities is relatively small. And there are known performance issues related to applying the updates or disabling the Intel Hyper-Threading Technology. So please read on before you rush to update your system(s).

## The vulnerabilities

[Microsoft issued a security advisory](https://msrc.microsoft.com/update-guide/vulnerability/ADV220002) about these vulnerabilities on June 14, 2022. [Intel’s advisory](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00615.html) about the same four vulnerabilities came out the same day, which triggers the question, why did it take so long to release the updates? We can only speculate that a lot of time was spent on figuring out how to address these vulnerabilities most effectively.

The vulnerabilities are a class of memory-mapped I/O (MMIO) vulnerabilities. In shared resource environments (for example in some cloud services configurations), these vulnerabilities could allow one virtual machine to improperly access information from another. Under normal circumstances, an attacker would need prior access to the system or an ability to run a specially crafted application on the target system to leverage these vulnerabilities.

The Common Vulnerabilities and Exposures (CVE) database lists publicly disclosed computer security flaws. The MMIO CVEs are listed as:

* [CVE-2022-21123](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21123) – Shared Buffer Data Read (SBDR)
* [CVE-2022-21125](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21125) – Shared Buffer Data Sampling (SBDS)
* [CVE-2022-21127](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21127) – Special Register Buffer Data Sampling Update (SRBDS Update)
* [CVE-2022-21166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21166) – Device Register Partial Write (DRPW)

The underlying cause for these vulnerabilities is that Virtual Machines (VMs) share a portion of the physical processor (CPU). MMIO uses the processor’s physical-memory address space to access I/O devices that respond like memory components. Due to the incomplete cleanup in specific special register read and write operations, or shared buffers an authenticated user could potentially gain information disclosure through local access.

There is a long [list of affected processors](https://www.intel.com/content/www/us/en/developer/topic-technology/software-security-guidance/processors-affected-consolidated-product-cpu-model.html) which shows the impact of transient execution attacks and select security issues on currently supported Intel® products, including recommended mitigation where affected.

## Should you update?

As with many threats, the risk you are running very much depends on your threat model. If you are not running virtual machines in shared environments, I wouldn’t worry about these updates. If you are, then the ball is for a large part in the park of the provider of the cloud services, since it’s their physical machines that may or may not have the affected CPUs.

If any action needs to be taken, I would consider it their duty to let you know what needs to be done on your end.

Mitigation for these vulnerabilities includes a combination of microcode updates and software changes, depe...