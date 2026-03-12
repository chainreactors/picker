---
title: Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days
url: https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html
source: The Hacker News
date: 2026-03-11
fetch_date: 2026-03-12T04:09:07.449335
---

# Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days](https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html)

**Ravie Lakshmanan**Mar 11, 2026Patch Tuesday / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipDVdeJebBFVnXLhsh2P4nBqmuh4R-UtLH7ZFvyw1W95zBU4YX4GF6I1WZ7g3ALEq596lEFr6q8iuGZ_PG2D12h67cLuNhCnSplkg_kDNbKyvTJnByhz2WAeAL9YHXCpJp0D3UOnhuydFZ6-jfXi6DLx5upod8egCtZ2lZhmbUzIprEusPyz0efzBMFzFI/s1700-e365/windows-patch.jpg)

Microsoft on Tuesday released patches for a set of [84 new security vulnerabilities](https://msrc.microsoft.com/update-guide/releaseNote/2026-mar) affecting various software components, including two that have been listed as publicly known.

Of these, eight are rated Critical, and 76 are rated Important in severity. Forty-six of the patched vulnerabilities relate to privilege escalation, followed by 18 remote code execution, 10 information disclosure, four spoofing, four denial-of-service, and two security feature bypass flaws.

The fixes are in addition to [10 vulnerabilities](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security) that have been addressed in its Chromium-based Edge browser since the release of the [February 2026 Patch Tuesday update](https://thehackernews.com/2026/02/microsoft-patches-59-vulnerabilities.html).

The two publicly disclosed zero-days are [CVE-2026-26127](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-26127) (CVSS score: 7.5), a denial-of-service vulnerability in .NET, and [CVE-2026-21262](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21262) (CVSS score: 8.8), an elevation of privilege vulnerability in SQL Server.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The vulnerability with the highest CVSS score in this month's update is a critical remote code execution flaw in the Microsoft Devices Pricing Program. [CVE-2026-21536](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21536) (CVSS score: 9.8), per Microsoft, has been fully mitigated, and no action is required from users. Artificial intelligence (AI)-powered autonomous vulnerability discovery platform XBOW has been credited with discovering and reporting the issue.

"This month, over half (55%) of all Patch Tuesday CVEs were privilege escalation bugs, and of those, six were rated exploitation more likely across Windows Graphics Component, Windows Accessibility Infrastructure, Windows Kernel, Windows SMB Server, and Winlogon," Satnam Narang, senior staff research engineer at Tenable, said.

"We know these bugs are typically used by threat actors as part of post-compromise activity, once they get onto systems through other means (social engineering, exploitation of another vulnerability)."

The Winlogon privilege escalation flaw ([CVE-2026-25187](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-25187), CVSS score: 7.8), in particular, leverages improper link resolution to obtain SYSTEM privileges. Google Project Zero researcher James Forshaw has been acknowledged for reporting the vulnerability.

"The flaw allows a locally authenticated attacker with low privileges to exploit a link-following condition in the Winlogon process and escalate to SYSTEM privileges," Jacob Ashdown, cybersecurity engineer at Immersive, said. "The vulnerability requires no user interaction and has low attack complexity, making it a straightforward target once an attacker gains a foothold."

Another vulnerability of note is [CVE-2026-26118](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-26118) (CVSS score: 8.8), a server-side request forgery bug in the Azure Model Context Protocol (MCP) server that could allow an authorized attacker to elevate privileges over a network.

"An attacker could exploit this issue by sending specially crafted input to an Azure Model Context Protocol (MCP) Server tool that accepts user‑provided parameters," Microsoft said.

"If the attacker can interact with the MCP‑backed agent, they can submit a malicious URL in place of a normal Azure resource identifier. The MCP Server then sends an outbound request to that URL and, in doing so, may include its managed identity token. This allows the attacker to capture that token without requiring administrative access."

Successful exploitation of the vulnerability could permit an attacker to obtain the permissions associated with the MCP Server's managed identity. The attacker could then leverage this behavior to access or perform actions on any resources that the managed identity is authorized to reach.

Among the Critical-severity bugs resolved by Microsoft is an information disclosure flaw in Excel. Tracked as [CVE-2026-26144](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-26144) (CVSS score of 7.5), it has been described as a case of cross-site scripting that occurs as a result of improper neutralization of input during web page generation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

The Windows maker said an attacker who exploited the shortcoming could potentially cause Copilot Agent mode to exfiltrate data as part of a zero-click attack.

"Information disclosure vulnerabilities are especially dangerous in corporate environments where Excel files often contain financial data, intellectual property, or operational records," Alex Vovk, CEO and co-founder of Action1, said in a statement.

"If exploited, attackers could silently extract confidential information from internal systems without triggering obvious alerts. Organizations using AI-assisted productivity features may face increased exposure, as automated agents could unintentionally transmit sensitive data outside corporate boundaries."

The patches come as Microsoft said it's changing the default behavior of Windows Autopatch...