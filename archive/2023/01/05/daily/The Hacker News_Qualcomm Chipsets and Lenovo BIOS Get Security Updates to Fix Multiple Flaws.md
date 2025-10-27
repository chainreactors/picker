---
title: Qualcomm Chipsets and Lenovo BIOS Get Security Updates to Fix Multiple Flaws
url: https://thehackernews.com/2023/01/qualcomm-chipsets-and-lenovo-bios-get.html
source: The Hacker News
date: 2023-01-05
fetch_date: 2025-10-04T03:07:01.022390
---

# Qualcomm Chipsets and Lenovo BIOS Get Security Updates to Fix Multiple Flaws

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

# [Qualcomm Chipsets and Lenovo BIOS Get Security Updates to Fix Multiple Flaws](https://thehackernews.com/2023/01/qualcomm-chipsets-and-lenovo-bios-get.html)

**Jan 04, 2023**Ravie LakshmananFirmware Security

[![Qualcomm Chipsets and Lenovo](data:image/png;base64... "Qualcomm Chipsets and Lenovo")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWahunxqpKKN3I12j9CpJdHoxx_HPDvpewD1SOEjBGGRuCOXEbI2To0Y5EdwCkT3Zq6hnQZgIhRUIxt1WETw8UgqaIAIU7tBIsU0sCdLmkAIGWSugwbCCAdxQn0eKRUJPK1Pa64ryZ22y_tJuVpR2X1FmFXTqNSGwEjJ2CnxzKySnTpwuwiEz2jE-O/s790-rw-e365/ql.png)

Qualcomm on Tuesday [released patches](https://docs.qualcomm.com/product/publicresources/securitybulletin/january-2023-bulletin.html) to address multiple security flaws in its chipsets, some of which could be exploited to cause information disclosure and memory corruption.

The five vulnerabilities -- tracked from CVE-2022-40516 through CVE-2022-40520 -- also impact Lenovo ThinkPad X13s laptops, prompting the Chinese PC maker to issue BIOS updates to plug the security holes.

The list of flaws is as follows -

* **CVE-2022-40516, CVE-2022-40517 & CVE-2022-40520** (CVSS scores: 8.4) - Memory corruption in Core due to [stack-based buffer overflow](https://cwe.mitre.org/data/definitions/121.html)
* **CVE-2022-40518 & CVE-2022-40519** (CVSS scores: 6.8) - Information disclosure due to [buffer over-read](https://cwe.mitre.org/data/definitions/126.html) in Core

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Stack-based buffer overflow vulnerabilities can result in severe impacts, such as data corruption, system crashes, and arbitrary code execution. Buffer over-reads, on the other hand, can be weaponized to read out-of-bounds memory, leading to the exposure of secret data.

Successful exploitation of the aforementioned flaws could allow a local adversary with elevated privileges to cause memory corruption or leak sensitive information, Lenovo [noted](https://support.lenovo.com/us/en/product_security/LEN-103709) in an alert published Tuesday.

Also remediated by Lenovo are four more buffer over-read vulnerabilities in ThinkPad X13 BIOS that could lead to information disclosure. The flaws are tracked as CVE-2022-4432, CVE-2022-4433, CVE-2022-4434, and CVE-2022-4435.

ThinkPad X13 users are recommended to update the BIOS to version 1.47 (N3HET75W) or newer. Firmware security firm Binarly has been credited with discovering and reporting the nine shortcomings.

Qualcomm's January 2023 security bulletin further closes out 17 other vulnerabilities, including one critical memory corruption bug in the Automotive component (CVE-2022-33219, CVSS score: 9.3) arising as a result of a buffer overflow flaw.

### Binarly Shares Details of the Flaws

Binarly on January 9, 2023, [shared more details](https://www.binarly.io/posts/Multiple_Vulnerabilities_in_Qualcomm_and_Lenovo_ARM_based_Devices) on the security vulnerabilities, noting that "this is the first public disclosure in history of UEFI specification related to the ARM device ecosystem."

The company characterized CVE-2022-40516, CVE-2022-40517, and CVE-2022-40520 as high-impact owing to the fact that it could be exploited to achieve a [secure boot](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot) bypass and permit an adversary to gain persistence on the device.

All the vulnerabilities have been found in various Driver Execution Environment ([DXE](https://github.com/tianocore/tianocore.github.io/wiki/PI-Boot-Flow)) drivers, which are "responsible for initializing the processor, chipset, and platform components."

The findings also follow a related disclosure from Binarly that two Lenovo vulnerabilities that came to light in November 2022 ([CVE-2022-3430 and CVE-2022-3431](https://thehackernews.com/2022/11/new-uefi-firmware-flaws-reported-in.html)) continue to [remain unfixed](https://www.binarly.io/posts/Firmware_Patch_Deep_Dive_Lenovo_Patches_Fail_to_Fix_Underlying_Vulnerabilities/index.html) across all product lines.

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

[BIOS](https://thehackernews.com/search/label/BIOS)[Lenovo](https://thehackernews.com/search/label/Lenovo)[Qualcomm](https://thehackernews.com/search/label/Qualcomm)[UEFI Firmware](https://thehackernews.com/search/label/UEFI%20Firmware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers...