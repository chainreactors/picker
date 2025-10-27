---
title: Over a Dozen New BMC Firmware Flaws Expose OT and IoT Devices to Remote Attacks
url: https://thehackernews.com/2022/11/over-dozen-new-bmc-firmware-flaws.html
source: The Hacker News
date: 2022-11-29
fetch_date: 2025-10-04T00:01:21.797520
---

# Over a Dozen New BMC Firmware Flaws Expose OT and IoT Devices to Remote Attacks

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

# [Over a Dozen New BMC Firmware Flaws Expose OT and IoT Devices to Remote Attacks](https://thehackernews.com/2022/11/over-dozen-new-bmc-firmware-flaws.html)

**Nov 28, 2022**Ravie Lakshmanan

[![BMC Firmware Flaws](data:image/png;base64... "BMC Firmware Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigh1HVeiw2PfuW91mmSPwhW9tHWAQ4qrsbFI94ruwF8DuCsTRlpzABd6poxjZNO1cyWg4n7WIdEmflm-uH2I6fGwnlfS2E7NkjL31tCmDzPsUA5XvTi9awTlsJJkcrO0Tq3OpWobzJxq_Ues_SfX7IvNEGM-0kVSztnK1l4bPCTAijiQdtrhxlFQpo/s790-rw-e365/bmc-firmware.png)

Over a dozen security flaws have been discovered in baseboard management controller ([BMC](https://thehackernews.com/2022/05/critical-pantsdown-bmc-vulnerability.html)) firmware from Lanner that could expose operational technology (OT) and internet of things (IoT) networks to remote attacks.

BMC refers to a specialized service processor, a system-on-chip (SoC), that's found in server motherboards and is used for remote monitoring and management of a host system, including performing low-level system operations such as [firmware flashing](https://en.wikipedia.org/wiki/Firmware#Flashing) and power control.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Nozomi Networks, which analyzed an Intelligent Platform Management Interface ([IPMC](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface)) from Taiwanese vendor Lanner Electronics, said it uncovered 13 weaknesses affecting [IAC-AST2500](https://www.lannerinc.com/products/network-appliances/modules-and-acceleration-cards/iac-ast2500).

All the issues affect version 1.10.0 of the standard firmware, with the exception of CVE-2021-4228, which impacts version 1.00.0. Four of the flaws (from CVE-2021-26727 to CVE-2021-26730) are rated 10 out of 10 on the CVSS scoring system.

[![BMC Firmware Flaws](data:image/png;base64... "BMC Firmware Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAD6vFMSHaBf7UT3pbmlJBa50qu5pjFiDFKStppcDGAUQe1B7KtxZkRoccZULRB0SsDlUw-7h8AyaIVfEOgJVQXCPtONoEgF1cIfhNXDYYzx3tqBIaGT597Vl5Hgd4TdrxhLIZmNb1zwY4_0D9yHejBgZSjSgolOGDYci32ZOeWb6YR-RsasrA2IJx/s790-rw-e365/bmc.png)

In particular, the industrial security company found that CVE-2021-44467, an access control bug in the web interface, could be chained with CVE-2021-26728, a buffer overflow flaw, to achieve remote code execution on the BMC with root privileges.

"When also considering that all processes run with root privileges on the device, the combined weaknesses enable an unauthenticated attacker to completely compromise both the BMC and the managed host," the company [said](https://www.nozominetworks.com/blog/vulnerabilities-in-bmc-firmware-affect-ot-iot-device-security-part-1/) in a write-up published last week.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Lanner has since released an updated firmware that addresses the vulnerabilities in question following responsible disclosure.

"BMCs represent an attractive way to conveniently monitor and manage computer systems without requiring physical access, in the IT as well as in the OT/IoT domain," the researchers said.

"Nevertheless, their usability comes at the expense of a broader attack surface, and that may lead to an increase of the overall risk if they are not adequately protected."

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

[firmware](https://thehackernews.com/search/label/firmware)[IoT Device](https://thehackernews.com/search/label/IoT%20Device)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Be...