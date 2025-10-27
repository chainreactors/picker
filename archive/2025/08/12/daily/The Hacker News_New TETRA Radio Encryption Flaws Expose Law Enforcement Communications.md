---
title: New TETRA Radio Encryption Flaws Expose Law Enforcement Communications
url: https://thehackernews.com/2025/08/new-tetra-radio-encryption-flaws-expose.html
source: The Hacker News
date: 2025-08-12
fetch_date: 2025-10-07T00:50:46.807029
---

# New TETRA Radio Encryption Flaws Expose Law Enforcement Communications

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

# [New TETRA Radio Encryption Flaws Expose Law Enforcement Communications](https://thehackernews.com/2025/08/new-tetra-radio-encryption-flaws-expose.html)

**Aug 11, 2025**Ravie LakshmananEncryption / Network Security

[![Radio Encryption Flaws](data:image/png;base64... "Radio Encryption Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaayfGiYzPUHQFP8U8PWwPwMPrpbmDk3-wv2Eir_6OT3_ug9LGzJZv2IGp73mqaNkhmkfdi4XD-_rNYOdFrOXuVCWPSaVOwOTQmhKhJ8IJ8BQyO5CDyUlgRFczBVRibY68NzlB09Q2VWVCmwXCyX5-q8dE7_Yq869q8yU0F84hIH0lWKYEp4Rvd1d0-2NO/s790-rw-e365/burst.jpg)

Cybersecurity researchers have discovered a fresh set of security issues in the Terrestrial Trunked Radio (TETRA) communications protocol, including in its proprietary end-to-end encryption (E2EE) mechanism that exposes the system to replay and brute-force attacks, and even decrypt encrypted traffic.

Details of the vulnerabilities – dubbed **[2TETRA:2BURST](https://www.midnightblue.nl/research/2tetra2burst)** – were [presented](https://www.blackhat.com/us-25/briefings/schedule/#2-cops-2-broadcasting-tetra-end-to-end-under-scrutiny-46143) at the Black Hat USA security conference last week by Midnight Blue researchers Carlo Meijer, Wouter Bokslag, and Jos Wetzels.

[TETRA](https://www.etsi.org/technologies/tetra) is a European mobile radio standard that's widely used by law enforcement, military, transportation, utilities, and critical infrastructure operators. It was developed by the European Telecommunications Standards Institute (ETSI). It encompasses four encryption algorithms: TEA1, TEA2, TEA3, and TEA4.

The disclosure comes a little over two years after the Netherlands-based cybersecurity company [discovered](https://thehackernews.com/2023/07/tetraburst-5-new-vulnerabilities.html) a set of [security vulnerabilities](https://www.midnightblue.nl/research/retetra) in TETRA standard called TETRA:BURST, counting what was described as an "intentional backdoor" that could be exploited to leak sensitive information.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The newly discovered issues relate to a case of packet injection in TETRA, as well as an insufficient fix for CVE-2022-24401, one of the five flaws that was documented as part of TETRA:BURST, to prevent keystream recovery attacks. The identified vulnerabilities are listed below -

* **CVE-2025-52940** - TETRA end-to-end encrypted voice streams are vulnerable to replay attack. Furthermore, an attacker with no knowledge of the key may inject arbitrary voice streams, that are played back indistinguishably from authentic traffic by legitimate call recipients.
* **CVE-2025-52941** - TETRA end-to-end encryption algorithm ID 135 refers to an intentionally weakened AES-128 implementation which has its effective traffic key entropy reduced from 128 to 56 bits, rendering it vulnerable to brute-force attacks.
* **CVE-2025-52942** - End-to-end encrypted TETRA SDS messages feature no replay protection, allowing for arbitrary replay of messages towards either humans or machines.
* **CVE-2025-52943** - TETRA networks that support multiple Air Interface Encryption algorithms are vulnerable to key recovery attacks since the SCK/CCK network key is identical for all supported algorithms. When TEA1 is supported, an easily recovered TEA1 key (CVE-2022-24402) can be used to decrypt or inject TEA2 or TEA3 traffic on the network.
* **CVE-2025-52944** - The TETRA protocol lacks message authentication and therefore allows for the injection of arbitrary messages such as voice and data.
* ETSI's fix for CVE-2022-24401 is ineffective in the prevention of keystream recovery attacks (No CVE, assigned a placeholder identifier **MBPH-2025-001**)

Midnight Blue said the impact of the 2TETRA:2BURST depend on the use-cases and configuration aspects of each particular TETRA network, and that networks that use TETRA in a data-carrying capacity are particularly susceptible to packet injection attacks, potentially allowing attackers to intercept radio communications and inject malicious data traffic.

"Voice replay or injection scenarios (CVE-2025-52940) can cause confusion among legitimate users, which can be used as an amplifying factor in a larger-scale attack," the company said. "TETRA E2EE users (also those not using Sepura Embedded E2EE) should in any case validate whether they may be using the weakened 56-bit variant (CVE-2025-52941)."

"Downlink traffic injection is typically feasible using plaintext traffic, as we found radios will accept and process unencrypted downlink traffic even on encrypted networks. For uplink traffic injection, the keystream needs to be recovered."

There is no evidence of these vulnerabilities being exploited in the wild. That said, there are no patches that address the shortcomings, with the exception of MBPH-2025-001, for which a fix is expected to be released.

Mitigations for other flaws are listed below -

* **CVE-2025-52940, CVE-2025-52942** - Migrate to scrutinized, secure E2EE solution
* **CVE-2025-52941** - Migrate to non-weakened E2EE variant
* **CVE-2025-52943** - Disable TEA1 support and rotate all AIE keys
* **CVE-2025-52944** - When using TETRA in a data carrying capacity: add TLS/VPN layer on top of TETRA

"If you operate or use a TETRA network, you are certainly affected by CVE-2025-52944, in which we demonstrate it's possible to inject malicious traffic into a TETRA network, even with authentication and/or encryption enabled," Midnight Blue said.

"Also, CVE-2022-24401 likely affects you, as it allows adversaries to collect keystream for either breach of confidentiality or integrity. If you operate a multi-cipher network, CVE-2025-52943 poses a critical security risk."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In a statement shared with WIRED, ETSI [said](https://www.wired.com/story/encryption-made-for-police-and-military-radios-may-be-easily-cracked-researchers-find/) the E2EE mechanism used in TE...