---
title: Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day Under Active Attack
url: https://thehackernews.com/2025/11/microsoft-fixes-63-security-flaws.html
source: The Hacker News
date: 2025-11-12
fetch_date: 2025-11-13T03:16:06.451719
---

# Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day Under Active Attack

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Microsoft Fixes 63 Security Flaws, Including a Windows Kernel Zero-Day Under Active Attack](https://thehackernews.com/2025/11/microsoft-fixes-63-security-flaws.html)

**Nov 12, 2025**Ravie LakshmananVulnerability / Patch Tuesday

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUYsGcLHyK_kqDIY7BFmCJ4AE9H52XJOIWUJqYcOSdx0Zd3mSRUt1Z0obn3VXzWTbrZGysPwxK7Hte4CKCobzIee0kXOVOfhyphenhyphenKZhfI-jiDss_R1mNucatfeU0nklQI3kZDiQfzPpVIsgmZj9s4hXbNhP3XzR2ibeHdBezB6w1j_CTt3FrrOQgmse3pdpPX/s790-rw-e365/windows-update.jpg)

Microsoft on Tuesday released patches for [63 new security vulnerabilities](https://msrc.microsoft.com/update-guide/releaseNote/2025-Nov) identified in its software, including one that has come under active exploitation in the wild.

Of the 63 flaws, four are rated Critical and 59 are rated Important in severity. Twenty-nine of these vulnerabilities are related to privilege escalation, followed by 16 remote code execution, 11 information disclosure, three denial-of-service (DoS), two security feature bypass, and two spoofing bugs.

The patches are in addition to the [27 vulnerabilities](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security) the Windows maker addressed in its Chromium-based Edge browser since the release of [October 2025's Patch Tuesday](https://thehackernews.com/2025/10/two-new-windows-zero-days-exploited-in.html) update.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The zero-day vulnerability that has been listed as exploited in Tuesday's update is [CVE-2025-62215](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-62215) (CVSS score: 7.0), a privilege escalation flaw in Windows Kernel. The Microsoft Threat Intelligence Center (MSTIC) and Microsoft Security Response Center (MSRC) have been credited with discovering and reporting the issue.

"Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Kernel allows an authorized attacker to elevate privileges locally," the company said in an advisory.

That said, successful exploitation hinges on an attacker who has already gained a foothold on a system to [win a race condition](https://www.action1.com/patch-tuesday/patch-tuesday-november-2025/). Once this criterion is satisfied, it could permit the attacker to obtain SYSTEM privileges.

"An attacker with low-privilege local access can run a specially crafted application that repeatedly attempts to trigger this race condition," Ben McCarthy, lead cybersecurity engineer at Immersive, said.

"The goal is to get multiple threads to interact with a shared kernel resource in an unsynchronized way, confusing the kernel's memory management and causing it to free the same memory block twice. This successful 'double free' corrupts the kernel heap, allowing the attacker to overwrite memory and hijack the system's execution flow."

It's currently not known how this vulnerability is being exploited and by whom, but it's assessed to be used as part of a post-exploitation activity to escalate their privileges after obtaining initial access through some other means, such as social engineering, phishing, or exploitation of another vulnerability, Satnam Narang, senior staff research engineer at Tenable, said.

"When chained with other bugs this kernel race is critical: an RCE or sandbox escape can supply the local code execution needed to turn a remote attack into a SYSTEM takeover, and an initial low‑privilege foothold can be escalated to dump credentials and move laterally," Mike Walters, president and co-founder of Action1, said in a statement.

Also patched as part of the updates are two heap-based buffer overflow flaws in Microsoft's Graphics Component ([CVE-2025-60724](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-60724), CVSS score: 9.8) and Windows Subsystem for Linux GUI ([CVE-2025-62220](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-62220), CVSS score: 8.8) that could result in remote code execution.

Another vulnerability of note is a high-severity privilege escalation flaw in Windows Kerberos (CVE-2025-60704, CVSS score: 7.5) that takes advantage of a missing cryptographic step to gain administrator privileges. The vulnerability has been codenamed CheckSum by Silverfort.

"The attacker must inject themselves into the logical network path between the target and the resource requested by the victim to read or modify network communications," Microsoft [said](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-60704). "An unauthorized attacker must wait for a user to initiate a connection."

Silverfort researchers Eliran Partush and Dor Segal, who discovered the shortcoming, described it as a [Kerberos constrained delegation](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-constrained-delegation-overview) vulnerability that allows an attacker to impersonate arbitrary users and gain control over an entire domain by means of an adversary-in-the-middle (AitM) attack.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

An attacker who is able to successfully exploit the flaw could escalate privileges and move laterally to other machines in an organization. More concerning, threat actors could also gain the ability to impersonate any user in the company, allowing them to gain unfettered access or become a domain administrator.

"Any organization using Active Directory, with the Kerberos delegation capability turned on, is impacted," Silverfort [said](https://www.silverfort.com/blog/you-win-some-you-checksum-kerberos-delegation-vulnerability-cve-2025-60704/). "Because Kerberos delegation is a feature within Active Directory, an attacker requires initial access to an environment with compromised credentials."

### Software Patches from Other Vendors

In addition to Microsoft, security updates have also been released by other vendors ov...