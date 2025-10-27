---
title: New UEFI Firmware Flaws Reported in Several Lenovo Notebook Models
url: https://thehackernews.com/2022/11/new-uefi-firmware-flaws-reported-in.html
source: The Hacker News
date: 2022-11-11
fetch_date: 2025-10-03T22:26:29.682836
---

# New UEFI Firmware Flaws Reported in Several Lenovo Notebook Models

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

# [New UEFI Firmware Flaws Reported in Several Lenovo Notebook Models](https://thehackernews.com/2022/11/new-uefi-firmware-flaws-reported-in.html)

**Nov 10, 2022**Ravie Lakshmanan

[![UEFI Firmware Flaws](data:image/png;base64... "UEFI Firmware Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkE7FOiseJA146uu0yp1iGoeUaSw0vvSvQ37RMtlq9yPs_d2uBT0RgZ60Cxn0d7R3g9udf7VhGYrthxX-6PT6YQkng8xSySyrd9MxoJTDDuREDGJwIgrskaG2Y00IgXbwQFMZuRO8ixKlNMxCPTwi3luMqw3f9Yjp0D0eQxDNPGgmGLY1L9FF3ifxz/s790-rw-e365/lenovo-bios-hack.jpg)

PC maker Lenovo has addressed yet another set of three shortcomings in the Unified Extensible Firmware Interface (UEFI) firmware affecting several Yoga, IdeaPad, and ThinkBook devices.

"The vulnerabilities allow disabling UEFI Secure Boot or restoring factory default Secure Boot databases (incl. dbx): all simply from an OS," Slovak cybersecurity firm ESET [explained](https://twitter.com/ESETresearch/status/1590279782318878720) in a series of tweets.

UEFI refers to software that acts as an interface between the operating system and the firmware embedded in the device's hardware. Because UEFI is [responsible](https://thehackernews.com/2022/08/researchers-uncover-uefi-secure-boot.html) for launching the operating system when a device is powered on, it has made the technology an attractive option for threat actors looking to [drop malware](https://thehackernews.com/2022/07/experts-uncover-new-cosmicstrand-uefi.html) that's difficult to detect and remove.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Viewed in that light, the flaws, tracked as CVE-2022-3430, CVE-2022-3431, and CVE-2022-3432, could be abused by an adversary to turn off Secure Boot, a security mechanism that's designed to prevent malicious programs from loading during the boot process.

Lenovo's advisory [describes](https://support.lenovo.com/us/en/product_security/LEN-94952) the vulnerabilities as follows -

* **CVE-2022-3430:** A potential vulnerability in the WMI Setup driver on some consumer Lenovo Notebook devices may allow an attacker with elevated privileges to modify Secure Boot setting by modifying an NVRAM variable.

* **CVE-2022-3431:** A potential vulnerability in a driver used during the manufacturing process on some consumer Lenovo Notebook devices that was mistakenly not deactivated may allow an attacker with elevated privileges to modify Secure Boot setting by modifying an NVRAM variable.

* **CVE-2022-3432:** A potential vulnerability in a driver used during the manufacturing process on the IdeaPad Y700-14ISK that was mistakenly not deactivated may allow an attacker with elevated privileges to modify Secure Boot setting by modifying an NVRAM variable.

In other words, disabling the UEFI Secure Boot makes it possible for threat actors to execute rogue boot loaders, granting the attackers privileged access to the compromised hosts.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

ESET said the vulnerabilities weren't lapses in the source code per se, but rather came into being because the "drivers were meant to be used only during the manufacturing process but were mistakenly included in the production."

The latest update marks the third time Lenovo has moved to patch flaws in its UEFI firmware since the start of the year, all of which have been discovered and reported by ESET researcher Martin Smolár.

While the first set of issues ([CVE-2021-3970, CVE-2021-3971, and CVE-2021-3972](https://thehackernews.com/2022/04/new-lenovo-uefi-firmware.html)) could have permitted bad actors to deploy and execute firmware implants on the affected devices, the second batch ([CVE-2022-1890, CVE-2022-1891, and CVE-2022-1892](https://thehackernews.com/2022/07/new-uefi-firmware-vulnerabilities.html)) could be weaponized to achieve arbitrary code execution and disable security features.

Lenovo said it does not intend to release fixes for CVE-2022-3432 owing to the fact that the model in question has reached end-of-life (EoL). Users of the other impacted devices are recommended to update their firmware to the latest version.

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

[BIOS](https://thehackernews.com/search/label/BIOS)[ESET](https://thehackernews.com/search/label/ESET)[Firmware Security](https://thehackernews.com/search/label/Firmware%20Security)[Lenovo](https://thehackernews.com/search/label/Lenovo)[Secure Boot](https://thehackernews.com/search/label/Secure%20Boot)[UEFI](https://thehackernews.com/search/label/UEFI)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;...