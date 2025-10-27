---
title: Samba Issues Security Updates to Patch Multiple High-Severity Vulnerabilities
url: https://thehackernews.com/2022/12/samba-issues-security-updates-to-patch.html
source: The Hacker News
date: 2022-12-18
fetch_date: 2025-10-04T01:52:23.438612
---

# Samba Issues Security Updates to Patch Multiple High-Severity Vulnerabilities

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Samba Issues Security Updates to Patch Multiple High-Severity Vulnerabilities](https://thehackernews.com/2022/12/samba-issues-security-updates-to-patch.html)

**Dec 17, 2022**Ravie LakshmananServer Security / Network Security

[![Samba High-Severity Vulnerabilities](data:image/png;base64... "Samba High-Severity Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrWx1iwIQu31k7LT_W4k66Mqf0rLAaoAxrBlEdPjCdBiPnCHvVz7G-BNHTF0l5c1IHiyNgTThC9hQ_PdzaaU-EMFACcDtwudLDsD2TMlj-wZjGPW3VIoSzeQLI0cBqaCgHU2pVNiONUXP-rsC3u2Y2DEBdE7FgZOlGZqtCXZEB5BLIcfR911WzoI9c/s790-rw-e365/samba-server.png)

Samba has released software updates to remediate multiple vulnerabilities that, if successfully exploited, could allow an attacker to take control of affected systems.

The high-severity flaws, tracked as **CVE-2022-38023, CVE-2022-37966, CVE-2022-37967, and CVE-2022-45141**, have been patched in versions 4.17.4, 4.16.8 and 4.15.13 [released](https://www.samba.org/samba/history/) on December 15, 2022.

Samba is an open source Windows interoperability suite for Linux, Unix, and macOS operating systems that offers file server, printing, and Active Directory services.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A brief description of each of the weaknesses is below -

* [**CVE-2022-38023**](https://www.samba.org/samba/security/CVE-2022-38023.html) (CVSS score: 8.1) - Use of weak RC4-HMAC Kerberos encryption type in the [Netlogon Secure Channel](https://wiki.samba.org/index.php/Samba_Security_Documentation#NETLOGON_Secure_Channel_.28Schannel.29)
* [**CVE-2022-37966**](https://www.samba.org/samba/security/CVE-2022-37966.html) (CVSS score: 8.1) - An elevation of privilege vulnerability in Windows Kerberos RC4-HMAC
* [**CVE-2022-37967**](https://www.samba.org/samba/security/CVE-2022-37967.html) (CVSS score: 7.2) - An elevation of privilege vulnerability in Windows Kerberos
* [**CVE-2022-45141**](https://www.samba.org/samba/security/CVE-2022-45141.html) (CVSS score: 8.1) - Use of RC4-HMAC encryption when issuing Kerberos tickets in Samba Active Directory domain controller ([AD DC](https://wiki.samba.org/index.php/Running_a_Samba_AD_DC_with_MIT_Kerberos_KDC)) using Heimdal

It's worth noting that both [CVE-2022-37966](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37966) and [CVE-2022-37967](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37967), which enable an adversary to gain administrator privileges, were first disclosed by Microsoft as part of its November 2022 [Patch Tuesday](https://thehackernews.com/2022/11/install-latest-windows-update-asap.html) updates.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"An unauthenticated attacker could conduct an attack that could leverage cryptographic protocol vulnerabilities in RFC 4757 (Kerberos encryption type RC4-HMAC-MD5) and MS-PAC (Privilege Attribute Certificate Data Structure specification) to bypass security features in a Windows AD environment," the company said of CVE-2022-37966.

The patches also come as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) this week [published](https://www.cisa.gov/uscert/ncas/current-activity/2022/12/15/cisa-releases-forty-one-industrial-control-systems-advisories) 41 Industrial Control Systems (ICS) advisories pertaining to various flaws impacting Siemens and Prosys OPC products.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Samba](https://thehackernews.com/search/label/Samba)[server security](https://thehackernews.com/search/label/server%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and...