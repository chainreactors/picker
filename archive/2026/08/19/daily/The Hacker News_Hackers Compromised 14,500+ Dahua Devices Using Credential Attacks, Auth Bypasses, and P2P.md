---
title: Hackers Compromised 14,500+ Dahua Devices Using Credential Attacks, Auth Bypasses, and P2P
url: https://thehackernews.com/2026/08/hackers-compromised-14500-dahua-devices.html
source: The Hacker News
date: 2026-08-19
fetch_date: 2026-08-20T02:56:56.429652
---

# Hackers Compromised 14,500+ Dahua Devices Using Credential Attacks, Auth Bypasses, and P2P

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Hackers Compromised 14,500+ Dahua Devices Using Credential Attacks, Auth Bypasses, and P2P](https://thehackernews.com/2026/08/hackers-compromised-14500-dahua-devices.html)

**Swati Khandelwal**Aug 19, 2026IoT Security / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMoFWi-QSod_BQxqARN9B9-f3XXRsEk-QHunmW3JSc9DHyZNKRK91l5KTzt_DYxGnTUtGqRMo1WHR9zfREMAXDAeDOYFgXpSJdgyUXHgOGTnpiokI06ZsJ1syAzn8GYlkzZqr6L73IsPJDAKgCbobSSkzZfWfJPapFiVJS4Kc1DyP3SBsMFgyZjCL6V6Y/s1700-e365/camera.jpg)

Cybersecurity researchers at Hunt.io have disclosed details of a campaign that they say compromised more than 14,530 Dahua devices between June 17 and July 22, 2026, using credential attacks, two authentication-bypass flaws, and a peer-to-peer (P2P) relay technique.

The activity, codenamed Operation **[CameraSwarm](https://hunt.io/blog/operation-cameraswarm-dahua-cameras-compromised)**, was reconstructed from a 407 MB exposed working directory containing 2,616 files across 234 subdirectories, including tooling, logs, shell history, and campaign records, with the researchers saying confirmed compromises were concentrated in Ukraine and Russia.

The researchers said 1,923 cameras were configured with a persistent account during the operation and 283 were reached through the P2P path.

Users of affected Dahua products are advised to install the corresponding fix software or newer firmware, while ITRES Labs recommends disabling P2P where it is not required and checking firmware against the vendor's download site.

"The relay establishes the route without prior authentication, leaving login checks to the device's web application," [ITRES Labs](https://labs.itresit.es/2025/10/29/dahua-beyond-cve-2025-31702-p2p-relay-exposure/) said in an analysis published in October 2025.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Hunt.io attributed the 14,530-plus total to three attack paths -

* **Credential attacks:** 12,324 unique IP addresses across 13,229 campaign records.
* **Authentication bypass:** 1,923 cameras reached using CVE-2021-33044 and CVE-2021-33045, which Hunt.io said were also configured with the persistent account.
* **P2P relay:** 283 cameras identified by serial number, including devices located behind network address translation (NAT).

The two 2021 flaws are authentication-bypass vulnerabilities in Dahua cameras and related products. [Dahua's advisory](https://www.dahuasecurity.com/about-dahua/trust-center/dahua-psirt/dhcc-sa-202106-001%3Asecurity-advisory---identity-authentication-bypass-vulnerability-found-in-some-dahua-products) rates them 8.1 on the CVSS scoring system and lists fixed firmware, while the U.S. National Vulnerability Database ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-33044)) currently assigns each a CVSS score of 9.8.

"Attackers can bypass device identity authentication by constructing malicious data packets," Dahua said in its advisory.

A NetKeyboard client type triggers CVE-2021-33044 during authentication, while CVE-2021-33045 involves a loopback login request using the 127.0.0.1 address, according to the [original disclosure](https://seclists.org/fulldisclosure/2021/Oct/13) from security researcher Bashis.

As of August 19, 2026, both flaws remain listed in the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, which records them as Dahua IP camera authentication-bypass vulnerabilities and advises applying vendor mitigations or discontinuing use if mitigations are unavailable.

As of August 19, 2026, the public [p2pwn repository](https://github.com/thebadinteger/p2pwn) remains accessible and independently confirms that the tool accepts Dahua serial numbers as input, checks CVE-2021-33044 and CVE-2021-33045, and contains a default dummy-account configuration.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLkvLGKWXWx5Vl0i7RP9my0YUGzbc0YysFxGzSoCeO8x98hf43Piq-pcCHJU3f2ROskGmFeSAw9ohfVX_HGCuQabcNRTAwRK9_ouIiPy7L8aCokWP5-7cCwPvwbGRczvmYptKIyQqDRp4H2HG8JnwaW-BoQ8KFSGuuEJol17BhbtXt7S9tgkp63vHkhww/s1700-e365/35.png)

The repository does not establish Hunt.io's count of 1,923 affected cameras or its claim that the account survives a factory reset on most firmware. The P2P path is separate from the two authentication-bypass flaws.

ITRES Labs found during an earlier incident response investigation that, on firmware before mid-2024, a valid Dahua serial number could be used to establish an Easy4IP relay path before the connected device performed its own credential check, allowing a device behind NAT to become reachable through the vendor's relay infrastructure.

The [dh-p2p proof-of-concept repository](https://github.com/khoanguyen-3fc/dh-p2p) also shows that the Dahua P2P protocol locates a device through Easy4IPCloud using its serial number and can establish a tunnel to the camera or network video recorder.

A successful P2P relay can make the device reachable behind NAT, but device-level authentication can still be required for access.

Hunt.io said the operator's recovered code recorded 89.4% of live serial numbers returning an open channel without authentication.

That figure remains a campaign-specific claim from the recovered operator material. It has not been independently reproduced by ITRES Labs, Dahua, or a public computer emergency response team advisory located as of August 19, 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Two CVE labels associated with the recovered tooling do not describe the P2P behavior: [CVE-2024-39943](https://nvd.nist.gov/vuln/detail/CVE-2024-39943) is assigned by NVD to an operating-system command-injection flaw in Rejetto HFS, while Dahua describes [CVE-2025-31702](https://www.dahuasecurity.com/about-dahua/trust-center/dahua-psirt/security-ad...