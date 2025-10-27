---
title: Dell, HP, and Lenovo Devices Found Using Outdated OpenSSL Versions
url: https://thehackernews.com/2022/11/dell-hp-and-lenovo-devices-found-using.html
source: The Hacker News
date: 2022-11-26
fetch_date: 2025-10-03T23:51:35.929214
---

# Dell, HP, and Lenovo Devices Found Using Outdated OpenSSL Versions

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

# [Dell, HP, and Lenovo Devices Found Using Outdated OpenSSL Versions](https://thehackernews.com/2022/11/dell-hp-and-lenovo-devices-found-using.html)

**Nov 25, 2022**Ravie Lakshmanan

[![OpenSSL Versions](data:image/png;base64... "OpenSSL Versions")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ-DO3wB8Z7RyHOjC8w5Wq1JIUZBIsOGOKA-aYlbhdZHmyJDdHxrQ7T8a2ZxJ7A05pErxaTVc9aw-leGCeNFCZC6K52YgR0uqEhlC1iT5NgkckRI1_7k_4xd5IHP915xIpr2ooPoi8HynuPVg1PkWOfTbq8N6O6X0eoJkDe5fnEY26QFNIt_bgnQ7z/s790-rw-e365/laptops.png)

An analysis of firmware images across devices from Dell, HP, and Lenovo has revealed the presence of outdated versions of the [OpenSSL](https://thehackernews.com/2022/11/just-in-openssl-releases-patch-for-2.html) cryptographic library, underscoring a supply chain risk.

EFI Development Kit, aka [EDK](https://www.tianocore.org/), is an open source implementation of the Unified Extensible Firmware Interface ([UEFI](https://en.wikipedia.org/wiki/UEFI)), which functions as an interface between the operating system and the firmware embedded in the device's hardware.

The firmware development environment, which is in its second iteration (EDK II), comes with its own cryptographic package called [CryptoPkg](https://github.com/tianocore/edk2/tree/master/CryptoPkg) that, in turn, makes use of services from the OpenSSL project.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Per firmware security company Binarly, the firmware image associated with Lenovo Thinkpad enterprise devices was found to use three different versions of OpenSSL: 0.9.8zb, 1.0.0a, and 1.0.2j, the last of which was released in 2018.

What's more, one of the firmware modules named InfineonTpmUpdateDxe relied on OpenSSL version 0.9.8zb that was shipped on August 4, 2014.

"The InfineonTpmUpdateDxe module is responsible for updating the firmware of Trusted Platform Module ([TPM](https://learn.microsoft.com/en-us/windows/security/information-protection/tpm/trusted-platform-module-overview)) on the Infineon chip," Binarly [explained](https://www.binarly.io/posts/OpenSSL_Usage_in_UEFI_Firmware_Exposes_Weakness_in_SBOMs) in a technical write-up last week.

[![OpenSSL Versions](data:image/png;base64... "OpenSSL Versions")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhke2Vz4GHJyGai0L6ZUnUO5pcugbQlaOwmYBuyh1FgP4zu663HshvLiHAwWpkgyLr58js6QZm8oKdqw2XgU8DCGRVyMS6IlCjsFJwXW7cLU3_KsD03pOwiqvMpEKctaJsR1hyx12PQcPulJvWAPCDyUUqWjWFqKpRLcd3oDtnUYj6FgP2856M-QU97yQ/s790-rw-e365/software-version.png)

"This clearly indicates the supply chain problem with third-party dependencies when it looks like these dependencies never received an update, even for critical security issues."

The diversity of OpenSSL versions aside, some of the firmware packages from Lenovo and Dell utilized an even older version (0.9.8l), which came out on November 5, 2009. HP's firmware code, likewise, used a 10-year-old version of the library (0.9.8w).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The fact that the device firmware uses multiple versions of OpenSSL in the same binary package highlights how third-party code dependencies can introduce more complexities in the supply chain ecosystem.

Binarly further pointed out the weaknesses in what's called a Software Bill of Materials ([SBOM](https://www.ntia.gov/SBOM)) that arises as a result of integrating compiled binary modules (aka closed source) in the firmware.

"We see an urgent need for an extra layer of SBOM Validation when it comes to compiled code to validate on the binary level, the list of third-party dependency information that matches the actual SBOM provided by the vendor," the company said.

"A 'trust-but-verify' approach is the best way to deal with SBOM failures and reduce supply chain risks."

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

[Binarly](https://thehackernews.com/search/label/Binarly)[cryptography](https://thehackernews.com/search/label/cryptography)[Dell](https://thehackernews.com/search/label/Dell)[firmware hacking](https://thehackernews.com/search/label/firmware%20hacking)[Lenovo](https://thehackernews.com/search/label/Lenovo)[OpenSSL](https://thehackernews.com/search/label/OpenSSL)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers E...