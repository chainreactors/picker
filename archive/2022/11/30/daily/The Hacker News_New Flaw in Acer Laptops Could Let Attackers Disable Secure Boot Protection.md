---
title: New Flaw in Acer Laptops Could Let Attackers Disable Secure Boot Protection
url: https://thehackernews.com/2022/11/new-flaw-in-acer-laptops-could-let.html
source: The Hacker News
date: 2022-11-30
fetch_date: 2025-10-04T00:06:50.547531
---

# New Flaw in Acer Laptops Could Let Attackers Disable Secure Boot Protection

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

# [New Flaw in Acer Laptops Could Let Attackers Disable Secure Boot Protection](https://thehackernews.com/2022/11/new-flaw-in-acer-laptops-could-let.html)

**Nov 29, 2022**Ravie Lakshmanan

[![Secure Boot Protection](data:image/png;base64... "Secure Boot Protection")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbJ2KnFsQAn4hYByQf9Z7o3_Dt0CyR3334GVUr7ahSDFYt4aocrq_miih6IkXYOFmunFBR6rQpTXPdgiYIjUmRsevIPKg4ZqhTpIB2tba_LL1_a_UwjwBj4riPdDGeu89S8-Fn6vFXC-y8T4e_tBkqjv7LCPoz0ZcUMgj0u-YQTlnVtNEngptwKL_b/s790-rw-e365/acer.png)

Acer has released a firmware update to address a security vulnerability that could be potentially weaponized to turn off UEFI Secure Boot on affected machines.

Tracked as [**CVE-2022-4020**](https://nvd.nist.gov/vuln/detail/CVE-2022-4020), the high-severity vulnerability affects five different models that consist of Aspire A315-22, A115-21, and A315-22G, and Extensa EX215-21 and EX215-21G.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The PC maker described the vulnerability as an issue that "may allow changes to Secure Boot settings by creating NVRAM variables." Credited with [discovering](https://twitter.com/ESETresearch/status/1597227770626523136) the flaw is ESET researcher Martin Smolár, who previously disclosed [similar bugs](https://thehackernews.com/2022/11/new-uefi-firmware-flaws-reported-in.html) in Lenovo computers.

Disabling Secure Boot, an integrity mechanism that guarantees that only trusted software is loaded during system startup, enables a malicious actor to tamper with [boot loaders](https://thehackernews.com/2022/08/researchers-uncover-uefi-secure-boot.html), leading to severe consequences.

This includes [granting](https://community.acer.com/en/kb/articles/15520-security-vulnerability-regarding-vulnerability-that-may-allow-changes-to-secure-boot-settings) the attacker complete control over the operating system loading process as well as "disable or bypass protections to silently deploy their own payloads with the system privileges."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Per the Slovak cybersecurity company, the flaw resides in a [DXE driver](https://edk2-docs.gitbook.io/edk-ii-module-writer-s-guide/8_dxe_drivers_non-uefi_drivers/88_dxe_runtime_driver) called HQSwSmiDxe.

The BIOS update is expected to be released as part of a critical Windows update. Alternatively, users can download the fixes from Acer's [Support portal](https://www.acer.com/worldwide/support/).

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

[acer laptop](https://thehackernews.com/search/label/acer%20laptop)[BIOS](https://thehackernews.com/search/label/BIOS)[Secure Boot](https://thehackernews.com/search/label/Secure%20Boot)[UEFI Bootkit](https://thehackernews.com/search/label/UEFI%20Bootkit)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html)

[![Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](data:image/svg+xml;base64... "Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware")

Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](https://thehackernews.com/2025/09/cisco-asa-fir...