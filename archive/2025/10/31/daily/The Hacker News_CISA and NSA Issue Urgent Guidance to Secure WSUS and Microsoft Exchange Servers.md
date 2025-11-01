---
title: CISA and NSA Issue Urgent Guidance to Secure WSUS and Microsoft Exchange Servers
url: https://thehackernews.com/2025/10/cisa-and-nsa-issue-urgent-guidance-to.html
source: The Hacker News
date: 2025-10-31
fetch_date: 2025-11-01T03:13:08.981311
---

# CISA and NSA Issue Urgent Guidance to Secure WSUS and Microsoft Exchange Servers

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

# [CISA and NSA Issue Urgent Guidance to Secure WSUS and Microsoft Exchange Servers](https://thehackernews.com/2025/10/cisa-and-nsa-issue-urgent-guidance-to.html)

**Oct 31, 2025**Ravie LakshmananVulnerability / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjA0I1Jx6uIEdkIQQM9RnxL2Ki39vb2gH7eog9Bm7oLXHB3Ia60PLtDJsEuqlPrOsZLL9UJZ3YnnlRxxQv0zGB_pNQcpQvDlxnFR1c6_iN-NzNkRMt3sW38md0OI8cJDfVQ5wp6rvZD32HiKk_NuHiFdTbo0mQRf8BfoNVFmp283z-01nb_Z7oGhyqSdE4P/s790-rw-e365/ms.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) and National Security Agency (NSA), along with international partners from Australia and Canada, have released guidance to harden on-premise Microsoft Exchange Server instances from potential exploitation.

"By restricting administrative access, implementing multi-factor authentication, enforcing strict transport security configurations, and adopting zero trust (ZT) security model principles, organizations can significantly bolster their defenses against potential cyber attacks," CISA [said](https://www.cisa.gov/news-events/news/cisa-nsa-and-global-partners-unveil-security-blueprint-hardening-microsoft-exchange-servers).

The agencies said malicious activity aimed at Microsoft Exchange Server continues to take place, with unprotected and misconfigured instances facing the brunt of the attacks. Organizations are advised to decommission end-of-life on-premises or hybrid Exchange servers after transitioning to Microsoft 365.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Some of the best practices outlined are listed below -

* Maintain security updates and patching cadence
* Migrate end-of-life Exchange servers
* Ensure [Exchange Emergency Mitigation Service](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-emergency-mitigation-service) remains enabled
* Apply and maintain the Exchange Server baseline, Windows security baselines, and applicable mail client security baselines
* Enable antivirus solution, Windows Antimalware Scan Interface (AMSI), Attack Surface Reduction (ASR), and AppLocker and App Control for Business, Endpoint Detection and Response, and Exchange Server's anti-spam and anti-malware features
* Restrict administrative access to the Exchange Admin Center (EAC) and remote PowerShell and apply the principle of least privilege
* Harden authentication and encryption by configuring Transport Layer Security (TLS), HTTP Strict Transport Security ([HSTS](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/configure-http-strict-transport-security-in-exchange-server)), Extended Protection ([EP](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-extended-protection)), [Kerberos](https://thehackernews.com/2024/05/windows-11-to-deprecate-ntlm-add-ai.html) and Server Message Block (SMB) instead of NTLM, and multi-factor authentication
* Disable remote PowerShell access by users in the Exchange Management Shell ([EMS](https://learn.microsoft.com/en-us/powershell/exchange/exchange-management-shell))

"Securing Exchange servers is essential for maintaining the integrity and confidentiality of enterprise communications and functions," the agencies noted. "Continuously evaluating and hardening the cybersecurity posture of these communication servers is critical to staying ahead of evolving cyber threats and ensuring robust protection of Exchange as part of the operational core of many organizations."

### CISA Updates CVE-2025-59287 Alert

The guidance comes a day after CISA [updated](https://www.cisa.gov/news-events/alerts/2025/10/24/microsoft-releases-out-band-security-update-mitigate-windows-server-update-service-vulnerability-cve) its alert to include additional information related to [CVE-2025-59287](https://thehackernews.com/2025/10/microsoft-issues-emergency-patch-for.html), a newly re-patched security flaw in the Windows Server Update Services ([WSUS](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus)) component that could result in remote code execution.

The agency is recommending that organizations identify servers that are susceptible to exploitation, apply the out-of-band security update released by Microsoft, and investigate signs of threat activity on their networks -

* Monitor and vet suspicious activity and child processes spawned with SYSTEM-level permissions, particularly those originating from wsusservice.exe and/or w3wp.exe
* Monitor and vet nested PowerShell processes using base64-encoded PowerShell commands

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development follows a report from Sophos that threat actors are [exploiting](https://news.sophos.com/en-us/2025/10/29/windows-server-update-services-wsus-vulnerability-abused-to-harvest-sensitive-data/) the vulnerability to harvest sensitive data from U.S. organizations spanning a range of industries, including universities, technology, manufacturing, and healthcare. The exploitation activity was first detected on October 24, 2025, a day after Microsoft issued the update.

In these attacks, the attackers have been found to leverage vulnerable Windows WSUS servers to run a Base64-encoded PowerShell commands, and exfiltrate the results to a webhook[.]site endpoint, corroborating other reports from Darktrace, Huntress, and Palo Alto Networks Unit 42.

The cybersecurity company told The Hacker News that it has identified six incidents in its customer environments to date, although further research has flagged at least 50 victims.

"This activity shows that threat actors moved quickly to exploit this critical vulnerability in WSUS to collect valuable data from vulnerable organizations," Rafe Pilling, director of...