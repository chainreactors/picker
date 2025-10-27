---
title: Clop ransomware is victimizing GoAnywhere MFT customers
url: https://www.malwarebytes.com/blog/news/2023/03/clop-ransomware-is-victimizing-goanywhere-mft-customers
source: Over Security - Cybersecurity news aggregator
date: 2023-03-16
fetch_date: 2025-10-04T09:47:45.752949
---

# Clop ransomware is victimizing GoAnywhere MFT customers

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

![](https://www.threatdown.com/wp-content/uploads/2024/04/clop_ransomware_resized.png?w=1024)

[Ransomware](https://www.threatdown.com/blog/category/ransomware/)

# Clop ransomware is victimizing GoAnywhere MFT customers

March 4, 2023

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

According to information gathered by [BleepingComputer](https://www.bleepingcomputer.com/news/security/clop-ransomware-gang-begins-extorting-goanywhere-zero-day-victims/), the Clop ransomware group has claimed responsibility for the ransomware attacks that are tied to a vulnerability in the Fortra GoAnywhere MFT secure file-sharing solution.

As we reported on February 8, Fortra released an emergency patch (7.1.2) for an actively exploited zero-day vulnerability found in the GoAnywhere MFT administrator console.

GoAnywhere MFT, which stands for managed file transfer, allows businesses to manage and exchange files in a secure and compliant way. According to its website, it caters to [more than 3,000](https://www.goanywhere.com/about) organizations, predominantly ones with over 10,000 employees and 1B USD in revenue.

Some of these organizations are considered vital infrastructure such as local governments, financial companies, healthcare organizations, energy firms, and technology manufacturers.

The day after the release of the GoAnywhere patch, the Clop ransomware gang contacted BleepingComputer and [said](https://www.bleepingcomputer.com/news/security/clop-ransomware-claims-it-breached-130-orgs-using-goanywhere-zero-day/) they had used the flaw over ten days to steal data from 130 companies. At the time it was impossible to confirm this claim, but after two earlier victims, Community Health Systems (CHS) and Hatch Bank disclosed that data was stolen in the GoAnywhere MFT attacks, the Clop leak site now shows seven new companies. At least two of them reportedly have been breached using the GoAnywhere MFT vulnerability.

The Common Vulnerabilities and Exposures (CVE) database lists publicly disclosed computer security flaws. The CVE of the exploited vulnerability is [CVE-2023-0669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0669), and described as a pre-authentication command injection vulnerability in the License Response Servlet due to deserializing an arbitrary attacker-controlled object.

It is unknown whether these victims were targeted during the time that there was no patch available for the vulnerability or later. [Recent scans](https://www.vicarius.io/vsociety/blog/unauthenticated-rce-in-goanywhere) showed that around 1,000 administrative consoles are publicly exposed to the internet. The Web Client interface, which is the one that is normally accessible from the public internet, is not susceptible to this exploit, only the administrative interface.

## Mitigation

If your GoAnywhere MFT administration portal is exposed to the Internet, you are under urgent advice to download the security patch from the **Product Downloads** tab at the top of the GoAnywhere account page which you will see after logging in.

If for some reason you can’t install the patch, Fortra says you should follow the mitigation steps it put out, which involves implementing some access control wherein the administrator console interface should only be accessed from trusted sources, or disabling the licensing service altogether. There is also a technical mitigation configuration shared in the advisory that is only visible after logging in (which can be done with a free account if you are interested).

> On the file system where GoAnywhere MFT is installed, edit the file [install\_dir]/adminroot/WEB\_INF/web.xml
>
>  Find and remove (delete or comment out) the following servlet and servlet-mapping configuration in the screenshot below.
>
>  Before:
>
>       License Response Servlet
>
>       com.linoma.ga.ui.admin.servlet.LicenseResponseServlet
>
>       0
>
>       Licenses Response Servlet
>
>       /lic/accept/
>
> After...