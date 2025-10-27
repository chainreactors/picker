---
title: Microsoft Patches 130 Vulnerabilities, Including Critical Flaws in SPNEGO and SQL Server
url: https://thehackernews.com/2025/07/microsoft-patches-130-vulnerabilities.html
source: The Hacker News
date: 2025-07-10
fetch_date: 2025-10-06T23:54:55.117862
---

# Microsoft Patches 130 Vulnerabilities, Including Critical Flaws in SPNEGO and SQL Server

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

# [Microsoft Patches 130 Vulnerabilities, Including Critical Flaws in SPNEGO and SQL Server](https://thehackernews.com/2025/07/microsoft-patches-130-vulnerabilities.html)

**Jul 09, 2025**Ravie LakshmananEndpoint Security / Vulnerability

[![Microsoft Patches 130 Vulnerabilities](data:image/png;base64... "Microsoft Patches 130 Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmsizDR065vvzmSSz6UoDagOtL2ztM9EhGOZJRc1VbHtE8SC2hkgmCGDdouT9iVvYmuMurjPYIWyzYGHFkO2jX9znRlLolYowjOjxrJPrFeXpdDlVTMQxCwmZzxkduqWyua1Lqq17FsLtaNakCx9AFd2K-ByfxW8CCjxhFwcgBrIXGCg5PU2w3-cN9vGLb/s790-rw-e365/windows-update.jpg)

For the first time in 2025, Microsoft's Patch Tuesday updates did not bundle fixes for exploited security vulnerabilities, but the company acknowledged one of the addressed flaws had been publicly known.

The patches resolve a [whopping 130 vulnerabilities](https://msrc.microsoft.com/update-guide/releaseNote/2025-Jul), along with 10 other non-Microsoft CVEs that affect Visual Studio, AMD, and its Chromium-based Edge browser. Of these, 10 are rated Critical and the remaining are all rated Important in severity.

"The 11-month streak of patching at least one zero-day that was exploited in the wild ended this month," Satnam Narang, Senior Staff Research Engineer at Tenable, said.

Fifty-three of these shortcomings are classified as privilege escalation bugs followed by 42 as remote code execution, 17 as information disclosure, and 8 as security feature bypasses. These patches are in addition to [two other flaws](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security) addressed by the company in the Edge browser since the release of [last month's Patch Tuesday update](https://thehackernews.com/2025/06/microsoft-patches-67-vulnerabilities.html).

The vulnerability that's listed as publicly known is an information disclosure flaw in Microsoft SQL Server ([CVE-2025-49719](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49719), CVSS score: 7.5) that could permit an unauthorized attacker to leak uninitialized memory.

"An attacker might well learn nothing of any value, but with luck, persistence, or some very crafty massaging of the exploit, the prize could be cryptographic key material or other crown jewels from the SQL Server," Adam Barnett, Lead Software Engineer at Rapid7, said in a statement.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Mike Walters, President and Co-Founder of Action1, [said](https://www.action1.com/patch-tuesday/patch-tuesday-july-2025/) the flaw likely is the result of improper input validation in SQL Server's memory management, allowing access to uninitialized memory.

"As a result, attackers could retrieve remnants of sensitive data, such as credentials or connection strings," Walters added. "It affects both the SQL Server engine and applications using OLE DB drivers."

The most critical flaw patched by Microsoft as part of this month's updates concerns a case of remote code execution impacting SPNEGO Extended Negotiation ([NEGOEX](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-negoex/77c795cf-e522-4678-b0f1-2063c5c0561c)). Tracked as [CVE-2025-47981](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-47981), it carries a CVSS score of 9.8 out of 10.0.

"Heap-based buffer overflow in Windows SPNEGO Extended Negotiation allows an unauthorized attacker to execute code over a network," Microsoft said in an advisory. "An attacker could exploit this vulnerability by sending a malicious message to the server, potentially leading to remote code execution."

An anonymous researcher and Yuki Chen have been credited with discovering and repairing the flaw. Microsoft noted that the issue only impacts Windows client machines running Windows 10, version 1607 and above due to the "Network security: Allow PKU2U authentication requests to this computer to use online identities" Group Policy Object ([GPO](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)) being enabled by default.

"As always, Remote Code Execution is bad, but early analysis is suggesting that this vulnerability may be 'wormable' - the sort of vulnerability that could be leveraged in self-propagating malware and make many revisit trauma from the WannaCry incident," watchTowr founder and CEO Benjamin Harris said.

"Microsoft is clear on pre-requisites here: no authentication required, just network access, and Microsoft themselves believe exploitation is 'More Likely.' We shouldn't fool ourselves - if the private industry has noticed this vulnerability, it is certainly already on the radar of every attacker with an ounce of malice. Defenders need to drop everything, patch rapidly, and hunt down exposed systems."

Other vulnerabilities of importance include remote code execution flaws impacting Windows KDC Proxy Service ([CVE-2025-49735](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49735), CVSS score: 8.1), Windows Hyper-V ([CVE-2025-48822](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-48822), CVSS score: 8.6), and Microsoft Office ([CVE-2025-49695](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49695), [CVE-2025-496966](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49696), and [CVE-2025-49697](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49697), CVSS scores: 8.4).

"What makes CVE-2025-49735 significant is the network exposure combined with no required privileges or user interaction. Despite its high attack complexity, the vulnerability opens the door to pre-auth remote compromise, particularly attractive to APTs and nation-state actors," Ben McCarthy, Lead Cyber Security Engineer at Immersive, said.

"The attacker must win a race condition – a timing flaw where memory is freed and reallocated in a specific window – meaning reliability is low for now....