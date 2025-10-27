---
title: Critical Mitel MiCollab Flaw Exposes Systems to Unauthorized File and Admin Access
url: https://thehackernews.com/2024/12/critical-mitel-micollab-flaw-exposes.html
source: The Hacker News
date: 2024-12-06
fetch_date: 2025-10-06T19:45:35.428259
---

# Critical Mitel MiCollab Flaw Exposes Systems to Unauthorized File and Admin Access

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

# [Critical Mitel MiCollab Flaw Exposes Systems to Unauthorized File and Admin Access](https://thehackernews.com/2024/12/critical-mitel-micollab-flaw-exposes.html)

**Dec 05, 2024**Ravie LakshmananVulnerability / IoT Security

[![Mitel MiCollab Flaw](data:image/png;base64... "Mitel MiCollab Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJUuOP9gIu8zQpLgwI19Ko0JurpJKjZbU8JmaOfCsAvQKLW8PYupEekM9x8Fyr_AjpU7m0vTn7WTRG-qHfNB-BZMXm3EjH4h8TEnL0c6eMlFDoJ0xU4U4G1EcLhQHdxT-BDUkAAT5HFdPKO1qvuJh5gEfB_5YpTwB54bFu6UBg-oZL8x_y___8_f619fGg/s790-rw-e365/hacking.png)

Cybersecurity researchers have [released](https://github.com/watchtowrlabs/Mitel-MiCollab-Auth-Bypass_CVE-2024-41713) a proof-of-concept (PoC) exploit that strings together a now-patched critical security flaw impacting Mitel MiCollab with an arbitrary file read zero-day, granting an attacker the ability to access files from susceptible instances.

The critical vulnerability in question is CVE-2024-41713 (CVSS score: 9.8), which relates to a case of insufficient input validation in the NuPoint Unified Messaging (NPM) component of Mitel MiCollab that results in a path traversal attack.

MiCollab is a [software and hardware solution](https://www.mitel.com/products/micollab-collaboration-software) that integrates chat, voice, video, and SMS messaging with Microsoft Teams and other applications. NPM is a [server-based voicemail system](https://www.mitel.com/document-center/applications/collaboration/micollab/nupoint-unified-messaging/102/en/nupoint-unified-messaging-general-information-guide), which enables users to access their voice messages through various methods, including remotely or through the Microsoft Outlook client.

WatchTowr Labs, in a [report](https://labs.watchtowr.com/where-theres-smoke-theres-fire-mitel-micollab-cve-2024-35286-cve-2024-41713-and-an-0day) shared with The Hacker News, said it discovered CVE-2024-41713 as part of its efforts to reproduce [CVE-2024-35286](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-24-0014) (CVSS score: 9.8), another critical bug in the NPM component that could permit an attacker to access sensitive information and execute arbitrary database and management operations.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The SQL injection flaw was patched by Mitel in late May 2024 with the release of MiCollab version 9.8 SP1 (9.8.1.5).

What makes the new vulnerability notable is that it involves [passing the input "..;/"](https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf) in the HTTP request to the ReconcileWizard component to land the attacker in the root of the application server, thus making it possible to access sensitive information (e.g., /etc/passwd) sans authentication.

WatchTowr Labs' analysis further found that the authentication bypass could be chained with an as-yet-unpatched post-authentication arbitrary file read flaw to extract sensitive information.

"A successful exploit of this vulnerability could allow an attacker to gain unauthorized access, with potential impacts to the confidentiality, integrity, and availability of the system," Mitel [said](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2024-0029) in an advisory for CVE-2024-41713.

"If the vulnerability is successfully exploited, an attacker could gain unauthenticated access to provisioning information including non-sensitive user and network information, and perform unauthorized administrative actions on the MiCollab Server."

The company also noted that the local file read flaw (CVE-2024-55550, CVSS score: 2.7) within the system is the result of insufficient input sanitization, and that the disclosure is limited to non-sensitive system information. It emphasized that the vulnerability does not allow file modification or privilege escalation.

Following responsible disclosure, CVE-2024-41713 has been plugged in MiCollab versions 9.8 SP2 (9.8.2.12) or later as of October 9, 2024.

"On a more technical level, this investigation has demonstrated some valuable lessons," security researcher Sonny Macdonald said.

"Firstly, it has acted as a real-world example that full access to the source code is not always needed – even when diving into vulnerability research to reproduce a known weakness in a COTS solution. Depending on the depth of the CVE description, some good Internet search skills can be the basis for a successful hunt for vulnerabilities."

It's worth noting that MiCollab 9.8 SP2 (9.8.2.12) also addresses a separate SQL injection vulnerability in the Audio, Web, and Video Conferencing (AWV) component ([CVE-2024-47223](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2024-0028), CVSS score: 9.4) that could have severe impacts, ranging from information disclosure to execution of arbitrary database queries that could render the system inoperable.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Rapid7 detailed several security defects in the Lorex 2K Indoor Wi-Fi Security Camera (from CVE-2024-52544 through CVE-2024-52548) that could be combined to achieve remote code execution (RCE).

In a hypothetical attack scenario, the first three vulnerabilities could be utilized to reset a target device's admin password to one of the adversary's choosing, leveraging the access to view live video and audio feeds from the device, or leverage the remaining two flaws to achieve RCE with elevated privileges.

"The exploit chain consists of five distinct vulnerabilities, which operate together in two phases to achieve unauthenticated RCE," security researcher Stephen Fewer [noted](https://www.rapid7.com/blog/post/2024/12/03/lorex-2k-indoor-wi-fi-security-camera-multiple-vulnerabilities-fixed/).

"Phase 1 performs an authentication bypass, allowing...