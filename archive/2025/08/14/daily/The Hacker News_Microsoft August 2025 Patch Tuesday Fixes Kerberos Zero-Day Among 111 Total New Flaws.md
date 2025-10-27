---
title: Microsoft August 2025 Patch Tuesday Fixes Kerberos Zero-Day Among 111 Total New Flaws
url: https://thehackernews.com/2025/08/microsoft-august-2025-patch-tuesday.html
source: The Hacker News
date: 2025-08-14
fetch_date: 2025-10-07T00:50:49.562181
---

# Microsoft August 2025 Patch Tuesday Fixes Kerberos Zero-Day Among 111 Total New Flaws

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

# [Microsoft August 2025 Patch Tuesday Fixes Kerberos Zero-Day Among 111 Total New Flaws](https://thehackernews.com/2025/08/microsoft-august-2025-patch-tuesday.html)

**Aug 13, 2025**Ravie LakshmananVulnerability / Zero-Day

[![August 2025 Patch Tuesday](data:image/png;base64... "August 2025 Patch Tuesday")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLmCadJaow0NdJcMyuqnydue0tb1OvQGkBiKZD3egXEsjre1S6y8oZlwQFdU_WZgDsrvYmjMaACNI1wqxAPEJ-w3CZcICnt_icxwmrjF9QCquvibkM7dwK0RF-QJ6NwcWtN7Wsp2K3XHmppTGghrNm1Uh8SQPF4K3tfPQLqWk4s1sXPh9C73FWK7mM0GdE/s790-rw-e365/windows-updates.jpg)

Microsoft on Tuesday rolled out fixes for a [massive set of 111 security flaws](https://msrc.microsoft.com/update-guide/releaseNote/2025-Aug) across its software portfolio, including one flaw that has been disclosed as publicly known at the time of the release.

Of the 111 vulnerabilities, 16 are rated Critical, 92 are rated Important, two are rated Moderate, and one is rated Low in severity. Forty-four of the vulnerabilities relate to privilege escalation, followed by remote code execution (35), information disclosure (18), spoofing (8), and denial-of-service (4) defects.

This is in addition to [16 vulnerabilities](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security) addressed in Microsoft's Chromium-based Edge browser since the release of [last month's Patch Tuesday update](https://thehackernews.com/2025/07/microsoft-patches-130-vulnerabilities.html), including two spoofing bugs affecting Edge for Android.

Included among the vulnerabilities is a privilege escalation vulnerability impacting Microsoft Exchange Server hybrid deployments ([CVE-2025-53786](https://thehackernews.com/2025/08/microsoft-discloses-exchange-server.html), CVSS score: 8.0) that Microsoft disclosed last week.

The publicly disclosed zero-day is [CVE-2025-53779](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53779) (CVSS score: 7.2), another privilege escalation flaw in Windows Kerberos that stems from a case of relative path traversal. Akamai researcher Yuval Gordon has been credited with discovering and reporting the bug.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's worth mentioning here that the issue was documented in detail back in May 2025 by the web infrastructure and security company, giving it the codename [BadSuccessor](https://thehackernews.com/2025/05/critical-windows-server-2025-dmsa.html). The novel technique essentially [allows](https://unit42.paloaltonetworks.com/badsuccessor-attack-vector/) a threat actor with sufficient privileges to compromise an Active Directory (AD) domain by misusing delegated Managed Service Account (dMSA) objects.

"The good news here is that successful exploitation of CVE-2025-53779 requires an attacker to have pre-existing control of two attributes of the hopefully well protected dMSA: [msds-groupMSAMembership](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ada2/c651f64d-5e92-4d12-9011-e6811ed306aa), which determines which users may use credentials for the managed service account, and [msds-ManagedAccountPrecededByLink](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ada2/6ce9e113-5c1e-4ba3-8078-419dd4e33561), which contains a list of users on whose behalf the dMSA can act," Adam Barnett, lead software engineer at Rapid7, told The Hacker News.

"However, abuse of CVE-2025-53779 is certainly plausible as the final link of a multi-exploit chain which stretches from no access to total pwnage."

Action1's Mike Walters noted that the path traversal flaw can be abused by an attacker to create improper delegation relationships, enabling them to impersonate privileged accounts, escalate to a domain administrator, and potentially gain full control of the Active Directory domain.

"An attacker who already has a compromised privileged account can use it to move from limited administrative rights to full domain control," Walters [added](https://www.action1.com/patch-tuesday/patch-tuesday-august-2025/). "It can also be paired with methods such as Kerberoasting or Silver Ticket attacks to maintain persistence."

"With domain administrator privileges, attackers can disable security monitoring, modify Group Policy, and tamper with audit logs to hide their activity. In multi-forest environments or organizations with partner connections, this flaw could even be leveraged to move from one compromised domain to others in a supply chain attack."

Satnam Narang, senior staff research engineer at Tenable, said the immediate impact of BadSuccessor is limited, as only 0.7% of Active Directory domains had met the prerequisite at the time of disclosure. "To exploit BadSuccessor, an attacker must have at least one domain controller in a domain running Windows Server 2025 in order to achieve domain compromise," Narang pointed out.

Some of the notable Critical-rated vulnerabilities patched by Redmond this month are below -

* **[CVE-2025-53767](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53767)** (CVSS score: 10.0) - Azure OpenAI Elevation of Privilege Vulnerability
* **[CVE-2025-53766](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53766)** (CVSS score: 9.8) - GDI+ Remote Code Execution Vulnerability
* **[CVE-2025-50165](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-50165)** (CVSS score: 9.8) - Windows Graphics Component Remote Code Execution Vulnerability
* **[CVE-2025-53792](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53792)** (CVSS score: 9.1) - Azure Portal Elevation of Privilege Vulnerability
* **[CVE-2025-53787](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53787)** (CVSS score: 8.2) - Microsoft 365 Copilot BizChat Information Disclosure Vulnerability
* **[CVE-2025-50177](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-50177)** (CVSS score: 8.1) - Microsoft Message Queuing (MSMQ) Remote Code Execution Vulnerability
*...