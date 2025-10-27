---
title: Threatsday Bulletin: Rootkit Patch, Federal Breach, OnePlus SMS Leak, TikTok Scandal & More
url: https://thehackernews.com/2025/09/threatsday-bulletin-rootkit-patch.html
source: The Hacker News
date: 2025-09-26
fetch_date: 2025-10-02T20:44:45.102422
---

# Threatsday Bulletin: Rootkit Patch, Federal Breach, OnePlus SMS Leak, TikTok Scandal & More

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

# [ThreatsDay Bulletin: Rootkit Patch, Federal Breach, OnePlus SMS Leak, TikTok Scandal & More](https://thehackernews.com/2025/09/threatsday-bulletin-rootkit-patch.html)

**Sep 25, 2025**Ravie LakshmananCybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhhcTVBSljV167XcVrNefBX_9E-GKoGEpVyEhbo6JbjPX5fPqIqx4OBCpYxENtfaQ4n_uXaDENQecf1WTXsHknN2_ByI0X9LcJjTTz2ljswXY4QIMhkeqVMiELcZigSJeo1Td9RRmkVmLCItLaZeq21oaZiPPFXThqtEMpXyxncUEzYVeiBjhrIuIZdz8o/s790-rw-e365/threatsday-bulletin-thehackernews.jpg)

Welcome to this week's **Threatsday Bulletin**—your Thursday check-in on the latest twists and turns in cybersecurity and hacking.

The digital threat landscape never stands still. One week it's a critical zero-day, the next it's a wave of phishing lures or a state-backed disinformation push. Each headline is a reminder that the rules keep changing and that defenders—whether you're protecting a global enterprise or your own personal data—need to keep moving just as fast.

In this edition we unpack fresh exploits, high-profile arrests, and the newest tactics cybercriminals are testing right now. Grab a coffee, take five minutes, and get the key insights that help you stay a step ahead of the next breach.

1. Firmware fights back

   [SonicWall Releases SMA 100 Firmware Update to Remove Rootkit](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0015)

   SonicWall has released a firmware update that it said will help customers remove rootkit malware deployed in attacks targeting SMA 100 series devices. "SonicWall SMA 100 10.2.2.2-92sv build has been released with additional file checking, providing the capability to remove known rootkit malware present on the SMA devices," the company [said](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0015). "SonicWall strongly recommends that users of the SMA 100 series products (SMA 210, 410, and 500v) upgrade to the 10.2.2.2-92sv version." The update comes after a report from Google that [found](https://www.sonicwall.com/support/notices/urgent-advisory-for-addressing-rootkits-and-other-critical-vulnerabilities-in-sonicwall-sma-100-series-appliances/250730071322160) a threat actor tracked as UNC6148 deploying [OVERSTEP](https://thehackernews.com/2025/07/unc6148-backdoors-fully-patched.html) malware on end-of-life (EoL) SonicWall SMA 100 devices. SonicWall has also [disclosed](https://www.sonicwall.com/support/knowledge-base/sma100-end-of-support-no-charge-replacement-faq/250801111641957) that expediting the end-of-support (EoS) date for all SMA 100 devices to October 31, 2025, citing "significant vulnerabilities presented by legacy VPN appliances."
2. Texts laid bare

   [Unpatched Flaw in OnePlus Phones Lets Malicious Apps Access Text Messages](https://www.rapid7.com/blog/post/cve-2025-10184-oneplus-oxygenos-telephony-provider-permission-bypass-not-fixed/)

   A permission bypass vulnerability (CVE-2025-10184, CVSS score: 8.2) has been discovered in multiple versions of OnePlus OxygenOS installed on its Android devices. The shortcoming has to do with the fact that sensitive internal content providers are accessible without permission, and are vulnerable to SQL injection. "When leveraged, the vulnerability allows any application installed on the device to read SMS/MMS data and metadata from the system-provided [Telephony provider](https://developer.android.com/reference/android/provider/Telephony) (the package com.android.providers.telephony) without permission, user interaction, or consent," Rapid7 [said](https://www.rapid7.com/blog/post/cve-2025-10184-oneplus-oxygenos-telephony-provider-permission-bypass-not-fixed/). "The user is also not notified that SMS data is being accessed." Successful exploitation of the flaw could lead to the theft of sensitive information, such as multi-factor authentication (MFA) codes sent as SMS messages. The issue appears to have been introduced as part of OxygenOS 12, released in 2021. The vulnerability remains unpatched as of writing, but OnePlus has acknowledged it's investigating the issue.
3. Stop Guessing, Start Securing

   [Webinar: Code-to-Cloud Visibility Is the New AppSec Baseline](https://thehackernews.uk/cloud-code-visibility)

   Join this session to discover why code-to-cloud visibility is fast becoming the cornerstone of modern Application Security Posture Management (ASPM). You'll see how mapping risks from where they originate in code to where they surface in the cloud [unites development, DevOps, and security teams](https://thehackernews.uk/cloud-code-visibility), enabling sharper prioritization, tighter feedback loops, and faster remediation—before attackers can exploit the weak link.
4. GeoServer hole exploited

   [CISA says Hackers Breached Federal Agency Using GeoServer Exploit](https://www.cisa.gov/news-events/alerts/2025/09/23/cisa-releases-advisory-lessons-learned-incident-response-engagement)

   The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has [released](https://www.cisa.gov/news-events/alerts/2025/09/23/cisa-releases-advisory-lessons-learned-incident-response-engagement) a comprehensive cybersecurity advisory detailing how threat actors successfully compromised a U.S. federal civilian executive branch agency's network on July 11, 2024, by exploiting [CVE-2024-36401](https://thehackernews.com/2024/09/geoserver-vulnerability-targeted-by.html), a critical remote code execution vulnerability in GeoServer. "Over the three-week period, the cyber threat actors gained separate initial access to a second GeoServer via the same vulnerability and moved laterally to two other servers," the agency [said](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-266a). Once compromised, the attackers uploaded (or attempted to upload) web shells such as China Chopper, along with scripts designed for remote access, persistence, command execution, and privilege escalation. The cyber threat actors also used living-off-the-land (LotL) techniques ...