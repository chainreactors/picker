---
title: Microsoft Fixes 80 Flaws — Including SMB PrivEsc and Azure CVSS 10.0 Bugs
url: https://thehackernews.com/2025/09/microsoft-fixes-80-flaws-including-smb.html
source: The Hacker News
date: 2025-09-11
fetch_date: 2025-10-02T20:00:50.569574
---

# Microsoft Fixes 80 Flaws — Including SMB PrivEsc and Azure CVSS 10.0 Bugs

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

# [Microsoft Fixes 80 Flaws — Including SMB PrivEsc and Azure CVSS 10.0 Bugs](https://thehackernews.com/2025/09/microsoft-fixes-80-flaws-including-smb.html)

**Sep 10, 2025**Ravie LakshmananVulnerability / Patch Tuesday

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilmgWyVL7x8NEETgxUe-34xaBx6QnhRVofPlzEF90k9qxt27B7AqsbilACEBDjiAjpJBmfSu7DTNhlyYxFRHtO9YEwuN1azCT1x8kvSiv7f95w7Pv1X6H8Pc3cvbGhbCdx7lM4bySEiLWwJ9Ap3-joA2lVPZWzFN-u3r6J2av-1Cj6t3NihyphenhyphenNl2TdVtOGQ/s790-rw-e365/windows-update.jpg)

Microsoft on Tuesday addressed a set of [80 security flaws](https://msrc.microsoft.com/update-guide/releaseNote/2025-Sep) in its software, including one vulnerability that has been disclosed as publicly known at the time of release.

Of the 80 vulnerabilities, eight are rated Critical and 72 are rated Important in severity. None of the shortcomings has been exploited in the wild as a zero-day. Like [last month](https://thehackernews.com/2025/08/microsoft-august-2025-patch-tuesday.html), 38 of the disclosed flaws are related to privilege escalation, followed by remote code execution (22), information disclosure (14), and denial-of-service (3).

"For the third time this year, Microsoft patched more elevation of privilege vulnerabilities than remote code execution flaws," Satnam Narang, senior staff research engineer at Tenable, said. "Nearly 50% (47.5%) of all bugs this month are privilege escalation vulnerabilities."

The patches are in addition to [12 vulnerabilities](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security) addressed in Microsoft's Chromium-based Edge browser since the release of August 2025's Patch Tuesday update, including a security bypass bug (CVE-2025-53791, CVSS score: 4.7) that has been patched in version 140.0.3485.54 of the browser.

The vulnerability that has been flagged as publicly known is [CVE-2025-55234](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-55234) (CVSS score: 8.8), a case of privilege escalation in Windows SMB.

"SMB Server might be susceptible to relay attacks depending on the configuration," Microsoft said. "An attacker who successfully exploited these vulnerabilities could perform relay attacks and make the users subject to elevation of privilege attacks."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The Windows maker said the update enables support for auditing SMB client compatibility for SMB Server signing as well as SMB Server EPA, allowing customers to assess their environment and detect any potential device or software incompatibility issues before deploying [appropriate hardening measures](https://support.microsoft.com/en-us/topic/support-for-audit-events-to-deploy-smb-server-hardening-smb-server-signing-smb-server-epa-056f7478-ee2c-43b9-b94b-c0ff06de1d8f).

"The key takeaway from the CVE-2025-55234 advisory, other than the explanation of the well-known attack surface around SMB authentication, is that this is one of those times where simply patching isn't enough; in fact, the patches provide administrators with more auditing options to determine whether their SMB Server is interacting with clients that won't support the recommended hardening options," Adam Barnett, lead software engineer at Rapid7, said.

Mike Walters, president and co-founder of Action, said the vulnerability stems from the fact that SMB sessions can be established without properly validating the authentication context when key hardening measures, such as SMB signing and Extended Protection for Authentication, are not in place.

"This gap opens the door to man-in-the-middle relay attacks, where attackers can capture and forward authentication material to gain unauthorized access," Walters added. "It can easily become part of a larger campaign, moving from phishing to SMB relay, credential theft, lateral movement, and eventually data exfiltration."

The CVE with the highest CVSS score for this month, but not listed in the Release Notes, is [CVE-2025-54914](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54914) (CVSS score: 10.0), a critical flaw impacting Azure Networking that could result in privilege escalation. It requires no customer action, given that it's a cloud-related vulnerability.

Two other shortcomings that merit attention include a remote code execution flaw in Microsoft High Performance Compute (HPC) Pack ([CVE-2025-55232](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-55232), CVSS score: 9.8) and an elevation of privilege issue affecting Windows NTLM ([CVE-2025-54918](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54918), CVSS score: 8.8) that could allow an attacker to gain SYSTEM privileges.

"From Microsoft's limited description, it appears that if an attacker is able to send specially crafted packets over the network to the target device, they would have the ability to gain SYSTEM-level privileges on the target machine," Kev Breen, senior director of threat research at Immersive, said.

"The patch notes for this vulnerability state that 'Improper authentication in Windows NTLM allows an authorized attacker to elevate privileges over a network,' suggesting an attacker may already need to have access to the NTLM hash or the user's credentials."

Lastly, the update also remediates a security flaw ([CVE-2024-21907](https://github.com/advisories/GHSA-5crp-9r3c-p9vr), CVSS score: 7.5) in Newtonsoft.Json, a third-party component used in SQL Server, that could be exploited to trigger a denial-of-service condition, as well as two privilege escalation vulnerabilities in Windows BitLocker ([CVE-2025-54911](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54911), CVSS score: 7.3, and [CVE-2025-54912](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54912), CVSS score: 7.8).

Microsoft's Hussein Alrubaye has been credited with discovering and reporting both the BitLocker flaws. The two defects add to ...