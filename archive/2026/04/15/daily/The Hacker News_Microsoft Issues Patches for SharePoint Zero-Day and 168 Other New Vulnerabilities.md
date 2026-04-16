---
title: Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities
url: https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html
source: The Hacker News
date: 2026-04-15
fetch_date: 2026-04-16T04:54:24.837988
---

# Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities](https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html)

**Ravie Lakshmanan**Apr 15, 2026Vulnerability / Patch Tuesday

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKhAYMS4CZDglUzVBKPpIJJJjC7LSHIE8r8HSYTDvQtfuqIlLk-jorWPPNvMPaiuWSriWM2WP-cyKqr_TRwlOG65EY9ZZWuRYsrzcn05wg3mkQd_-j103HEjHaUryyOF7jWj6IuAM6VwCUloPq_9RMt959E-yG8qF4n1acw3OfY73fWw4p90V0ClaY4hjo/s1700-e365/windows-update.jpg)

Microsoft on Tuesday released updates to address a record [169 security flaws](https://msrc.microsoft.com/update-guide/releaseNote/2026-apr) across its product portfolio, including one vulnerability that has been actively exploited in the wild.

Of these 169 vulnerabilities, 157 are rated Important, eight are rated Critical, three are rated Moderate, and one is rated Low in severity. Ninety-three of the flaws are classified as privilege escalation, followed by 21 information disclosure, 21 remote code execution, 14 security feature bypass, 10 spoofing, and nine denial-of-service vulnerabilities.

Also included among the 169 flaws are four non-Microsoft issued CVEs impacting AMD (CVE-2023-20585), Node.js (CVE-2026-21637), Windows Secure Boot (CVE-2026-25250), and Git for Windows (CVE-2026-32631). The updates are in addition to [78 vulnerabilities](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security) that have been addressed in its Chromium-based Edge browser since the [update that was released last month](https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html).

The release makes it the second biggest Patch Tuesday ever, a little below the record set in October 2025, when Microsoft addressed a [massive 183 security flaws](https://thehackernews.com/2025/10/two-new-windows-zero-days-exploited-in.html). "At this pace, 2026 is on track to affirm that 1,000+ Patch Tuesday CVEs annually is the norm," Satnam Narang, senior staff research engineer at Tenable, said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

"Not only that, but elevation of privilege bugs continue to dominate the Patch Tuesday cycle over the last eight months, accounting for a record 57% of all CVEs patched in April, while remote code execution (RCE) vulnerabilities have dropped to just 12%, tied with information disclosure vulnerabilities this month."

The vulnerability that has come under active exploitation is [CVE-2026-32201](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32201) (CVSS score: 6.5), a spoofing vulnerability impacting Microsoft SharePoint Server.

"Improper input validation in Microsoft Office SharePoint allows an unauthorized attacker to perform spoofing over a network," Microsoft said in an advisory. "An attacker who successfully exploited the vulnerability could view some sensitive information (Confidentiality), make changes to disclosed information (Integrity), but cannot limit access to the resource (Availability)."

Although the vulnerability was internally discovered, it's currently not known how it'sbeing exploited, and who may be behind the activity, and the scale of such efforts.

"This zero-day vulnerability in Microsoft SharePoint Server is caused by improper input validation, allowing attackers to spoof trusted content or interfaces over a network," Mike Walters, president and co-founder of Action1, said.

"By exploiting this flaw, an attacker can manipulate how information is presented to users, potentially tricking them into trusting malicious content. While the direct impact on data is limited, the ability to deceive users makes this a powerful tool for broader attacks."

The active exploitation of CVE-2026-32201 has prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to [add](https://www.cisa.gov/news-events/alerts/2026/04/14/cisa-adds-two-known-exploited-vulnerabilities-catalog) it to the Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to remediate the shortcoming by April 28, 2026.

Another vulnerability of note is a privilege escalation flaw in Microsoft Defender ([CVE-2026-33825](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825), CVSS score: 7.8), which has been flagged as publicly known at the time of release. According to Redmond, the vulnerability could allow an authorized attacker to elevate privileges locally by taking advantage ofDefender'slack of adequate granular access controls.

Microsoft noted that no user action is required to install the update for CVE-2026-33825, as the platform updates itself frequently by default. Systems that have disabled Microsoft Defender are not in an exploitable state.

While Microsoft's advisory makes no mention of public exploit code, the patch is said to resolve a zero-day known as [BlueHammer](https://www.tenable.com/blog/microsofts-april-2026-patch-tuesday-addresses-163-cves-cve-2026-32201) that was [shared](https://deadeclipse666.blogspot.com/2026/04/public-disclosure.html) on GitHub on April 3, 2026, by a disgruntled security researcher using the alias "[Chaotic Eclipse](https://x.com/ChaoticEclipse0/status/2040052131491660027)" after a breakdown in communication with the tech giant over its handling of the vulnerability disclosure process. As of writing, access to the public exploit repository requires a user to sign in to GitHub.

Per Cyderes, the vulnerability exploits the Microsoft Defender update process through Volume Shadow Copy abuse to escalate a low-privileged user to NT AUTHORITY\SYSTEM by chaining together legitimate Windows features.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"During certain Defender update and remediation workflows, Defender creates a temporary Volume Shadow Copy snapshot," security researchers Rahul Ramesh and Reegun Jayapaul [explained](https://www.cyderes.com/howler-cell/windows-zero-day-bluehammer) earlier this month. "BlueHammer uses Cloud Files callbacks and oplocks to pause Defender at precisely the right moment, leaving the snapshot mounted and the SAM, SYSTEM, and SECUR...