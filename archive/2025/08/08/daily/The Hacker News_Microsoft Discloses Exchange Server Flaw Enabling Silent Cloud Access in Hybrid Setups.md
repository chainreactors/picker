---
title: Microsoft Discloses Exchange Server Flaw Enabling Silent Cloud Access in Hybrid Setups
url: https://thehackernews.com/2025/08/microsoft-discloses-exchange-server.html
source: The Hacker News
date: 2025-08-08
fetch_date: 2025-10-07T00:50:02.173028
---

# Microsoft Discloses Exchange Server Flaw Enabling Silent Cloud Access in Hybrid Setups

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

# [Microsoft Discloses Exchange Server Flaw Enabling Silent Cloud Access in Hybrid Setups](https://thehackernews.com/2025/08/microsoft-discloses-exchange-server.html)

**Aug 07, 2025**Ravie LakshmananVulnerability / Threat Detection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdVEfMJmenYStKUf4d3m4xp0dWyGpS0C_oVLZ8_51LsOSfOoomXs6xI2gXEhvRLCzWalpb7A9KLz-UrusNmI8cdy26Z3oApb_Mg9lmzo9U_mk7AWLb51MNp_TmYjJG288Q-PmUKBIWn9wwkWqq7ZLWOJ73bMo2AJ7Ogke-97RVk0p20PZl9HzHTdkEKNPB/s790-rw-e365/ms-exchnage.jpg)

Microsoft has released an advisory for a high-severity security flaw affecting on-premise versions of Exchange Server that could allow an attacker to gain elevated privileges under certain conditions.

The vulnerability, tracked as **CVE-2025-53786**, carries a CVSS score of 8.0. Dirk-jan Mollema with Outsider Security has been acknowledged for reporting the bug.

"In an Exchange hybrid deployment, an attacker who first gains administrative access to an on-premises Exchange server could potentially escalate privileges within the organization's connected cloud environment without leaving easily detectable and auditable traces," the tech giant [said](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53786) in the alert.

"This risk arises because Exchange Server and Exchange Online share the same service principal in hybrid configurations."

Successful exploitation of the flaw could allow an attacker to escalate privileges within the organization's connected cloud environment without leaving easily detectable and auditable traces, the company added. However, the attack hinges on the threat actor already having administrator access to an Exchange Server.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA), in a bulletin of its own, [said](https://www.cisa.gov/news-events/alerts/2025/08/06/microsoft-releases-guidance-high-severity-vulnerability-cve-2025-53786-hybrid-exchange-deployments) the vulnerability could impact the identity integrity of an organization's Exchange Online service if left unpatched.

As mitigations, customers are recommended to [review](https://techcommunity.microsoft.com/blog/exchange/exchange-server-security-changes-for-hybrid-deployments/4396833) Exchange Server security changes for hybrid deployments, install the [April 2025 Hot Fix](https://techcommunity.microsoft.com/blog/exchange/released-april-2025-exchange-server-hotfix-updates/4402471) (or newer), and follow the [configuration instructions](https://learn.microsoft.com/en-in/Exchange/hybrid-deployment/deploy-dedicated-hybrid-app).

"If you've previously configured Exchange hybrid or [OAuth authentication between Exchange Server and your Exchange Online organization](https://learn.microsoft.com/exchange/configure-oauth-authentication-between-exchange-and-exchange-online-organizations-exchange-2013-help) but no longer use it, make sure to [reset the service principal's keyCredentials](https://learn.microsoft.com/en-in/Exchange/hybrid-deployment/deploy-dedicated-hybrid-app#service-principal-clean-up-mode)," Microsoft said.

In a [presentation](https://www.blackhat.com/us-25/briefings/schedule/#advanced-active-directory-to-entra-id-lateral-movement-techniques-46500) at the Black Hat USA 2025 security conference, Mollema said on-premise versions of Exchange Server have a certificate credential that's used to authenticate to Exchange online and allow OAuth in hybrid scenarios.

These certificates can be leveraged to request Service-to-Service ([S2S](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/automation-apis-using-s2s-authentication)) actor tokens from Microsoft's Access Control Service ([ACS](https://learn.microsoft.com/en-us/previous-versions/azure/azure-services/hh147631%28v%3Dazure.100%29)), ultimately providing unfettered access to Exchange Online and SharePoint without any [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) or security checks.

More importantly, these tokens can be used to impersonate any hybrid user within the tenant for a 24-hour period when the "[trustedfordelegation](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountcontrol?view=windowsserver2025-ps#-trustedfordelegation)" property is set, and leave no logs when they are issued. As mitigations, Microsoft plans to enforce mandatory separation of Exchange on-premises and Exchange Online service principals by October 2025.

The development comes as the Windows maker [said](https://techcommunity.microsoft.com/blog/exchange/dedicated-hybrid-app-temporary-enforcements-new-hcw-and-possible-hybrid-function/4440682) it will begin temporarily blocking Exchange Web Services (EWS) traffic using the Exchange Online shared service principal starting this month in an effort to increase the customer adoption of the dedicated Exchange hybrid app and improve the security posture of the hybrid environment.

Microsoft's advisory for CVE-2025-53786 also coincides with CISA's analysis of various malicious artifacts deployed following the exploitation of [recently disclosed SharePoint flaws](https://thehackernews.com/2025/07/storm-2603-exploits-sharepoint-flaws-to.html), collectively tracked as ToolShell.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This includes two Base64-encoded DLL binaries and four Active Server Page Extended (ASPX) files that are designed to retrieve machine key settings within an ASP.NET application's configuration and act as a web shell to execute commands and upload files.

"Cyber threat actors could leverage this malware to steal cryptographic keys and execute a Base64-encoded PowerShell command to fingerprint the host system and exfiltrate data," the agency [said](https://www.cisa.gov/news-events/alerts/2025/08/06/cisa-releases-malware-analysis-report-...