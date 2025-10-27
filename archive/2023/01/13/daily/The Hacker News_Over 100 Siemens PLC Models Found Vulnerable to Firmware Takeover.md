---
title: Over 100 Siemens PLC Models Found Vulnerable to Firmware Takeover
url: https://thehackernews.com/2023/01/over-100-siemens-plc-models-found.html
source: The Hacker News
date: 2023-01-13
fetch_date: 2025-10-04T03:46:48.811631
---

# Over 100 Siemens PLC Models Found Vulnerable to Firmware Takeover

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

# [Over 100 Siemens PLC Models Found Vulnerable to Firmware Takeover](https://thehackernews.com/2023/01/over-100-siemens-plc-models-found.html)

**Jan 12, 2023**Ravie LakshmananFirmware and Hardware Security

[![Siemens PLC Hacking](data:image/png;base64... "Siemens PLC Hacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSsX18iy_077wIP0FzszUkbxWZw72JD-lipv9So9SMDcC48hz-b1m0pq5BRx9pB6VuJSLx9-SkFchhT8MuOKYPhzW9xley9uQQc1y5yE3oGY-T1lhA27z35vj3kLc1KxLMu_nR8hLTXdrdbzVRcRTpadU6V71IRJNWsLsI0RMbMGTS3ny1m-cKmFAd/s790-rw-e365/plc.png)

Security researchers have disclosed multiple architectural vulnerabilities in Siemens SIMATIC and SIPLUS S7-1500 programmable logic controllers (PLCs) that could be exploited by a malicious actor to stealthily install firmware on affected devices and take control of them.

Discovered by **Red Balloon Security**, the issues are tracked as **CVE-2022-38773** (CVSS score: 4.6), with the low severity stemming from the prerequisite that exploitation requires physical tampering of the device.

The flaws "could allow attackers to bypass all protected boot features, resulting in persistent arbitrary modification of operating code and data," the company [said](https://redballoonsecurity.com/siemens-discovery/). More than 100 models are susceptible.

Put differently, the weaknesses are the result of a lack of asymmetric signature verifications for firmware at bootup, effectively permitting the attacker to load tainted bootloader and firmware in a manner that undermines integrity protections.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A more severe consequence of loading such modified firmware is that it could give the threat actor the ability to persistently execute malicious code and gain total control of the devices without raising any red flags.

"This discovery has potentially significant implications for industrial environments as these unpatchable hardware root-of-trust vulnerabilities could result in persistent arbitrary modification of S7-1500 operating code and data," the researchers said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjL56CKJoZkAadKCEp-A4a_zVWrdu-wG7OVNc4Ukdyd_2I5qmi8LP7Gu8LRBpVswV9hcd5Qwaxjd-pX7NBvEkUa5dLPv8M6e_3UAERUObbMQIvLekOxA2CkviZ3bZeCE_N4mQVpQ4xf1_NZOAgTDKeakgCqreu_8zJpCLp9aMg6MnXrHAagwKKPkZWr/s790-rw-e365/plc.png)

Siemens, in an [advisory](https://cert-portal.siemens.com/productcert/html/ssa-482757.html) released this week, said it has no patches planned but urged customers to limit physical access to the affected PLCs to trusted personnel to avoid hardware tampering.

The lack of a firmware update is attributed to the fact that the cryptographic scheme that undergirds the protected boot features is baked into a dedicated physical secure element chip (called the [ATECC108](https://www.microchip.com/en-us/product/ATECC108A) CryptoAuthentication coprocessor), which decrypts the firmware in memory during startup.

An attacker with physical access to the device could therefore leverage the issues identified in the cryptographic implementation to decrypt the firmware, make unauthorized changes, and flash the trojanized firmware onto the PLC either physically or by exploiting a known remote code execution flaw.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The fundamental vulnerabilities — improper hardware implementations of the [Root of Trust] using dedicated cryptographic-processor — are unpatchable and cannot be fixed by a firmware update since the hardware is physically unmodifiable," the researchers explained.

However, the German automation giant said it's in the process of releasing new hardware versions for the S7-1500 product family that come with a revamped "secure boot mechanism" that resolves the vulnerability.

The findings come as industrial security firm Claroty last year [disclosed](https://thehackernews.com/2022/10/critical-bug-in-siemens-simatic-plcs.html) a critical flaw impacting Siemens SIMATIC devices that could be exploited to retrieve the hard-coded, global private cryptographic keys and completely compromise the products.

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

[Firmware Security](https://thehackernews.com/search/label/Firmware%20Security)[Siemens](https://thehackernews.com/search/label/Siemens)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/micr...