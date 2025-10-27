---
title: Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants
url: https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html
source: The Hacker News
date: 2025-09-23
fetch_date: 2025-10-02T20:33:01.000647
---

# Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants

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

# [Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

**Sep 22, 2025**Ravie LakshmananCloud Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQ4bRwz6MJ6hdwy6WN3JzLRDW0W60H5wW9oKm50HAipFOxQ3TBxbOxfpz46icdE9elMWAl9W5kEqE3SUl91CjGLQX7HRqZWAQ6emiU9BgKVTjpPYsy-jaaPgSN26pfVQJ5MD7JCKqYV7S7N1tbgAsQDXwBc55oMEUH8B8qqETv6BC29ONwvtPpAwsoYCi9/s790-rw-e365/azure.jpg)

A critical token validation failure in Microsoft [Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) (previously Azure Active Directory) could have allowed attackers to impersonate any user, including Global Administrators, across any tenant.

The vulnerability, tracked as **[CVE-2025-55241](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-55241)**, has been assigned the maximum CVSS score of 10.0. It has been described by Microsoft as a privilege escalation flaw in Azure Entra. There is no indication that the issue was exploited in the wild. It has been addressed by the Windows maker as of July 17, 2025, requiring no customer action. The CVE was formally issued on September 4.

Security researcher Dirk-jan Mollema, who [discovered and reported](https://dirkjanm.io/obtaining-global-admin-in-every-entra-id-tenant-with-actor-tokens/) the shortcoming on July 14, said the shortcoming made it possible to compromise every Entra ID tenant in the world, with the likely exception of [national cloud deployments](https://learn.microsoft.com/en-us/graph/deployments).

The problem stems from a combination of two components: the use of service-to-service (S2S) actor tokens issued by the Access Control Service (ACS) and a fatal flaw in the legacy Azure AD Graph API (graph.windows.net) that did not adequately validate the originating tenant, which effectively allowed the tokens to be used for cross-tenant access.

What makes this noteworthy is that the tokens are subject to Microsoft's Conditional Access policies, enabling a bad actor with access to the Graph API to make unauthorized modifications. To make matters worse, the lack of API level logging for the Graph API meant that it could be exploited to access user information stored in Entra ID, group and role details, tenant settings, application permissions, and device information and BitLocker keys synced to Entra ID without leaving any traces.

An impersonation of the Global Administrator could allow an attacker to create new accounts, grant themselves additional permissions, or exfiltrate sensitive data, resulting in a full tenant compromise with access to any service that uses Entra ID for authentication, such as SharePoint Online and Exchange Online.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"It would also provide full access to any resource hosted in Azure, since these resources are controlled from the tenant level and Global Admins can grant themselves rights on Azure subscriptions," Mollema noted.

Microsoft has [characterized](https://www.microsoft.com/en-us/security/blog/2025/07/08/enhancing-microsoft-365-security-by-eliminating-high-privilege-access/) such instances of cross-tenant access as a case of "High-privileged access" (HPA) that "occurs when an application or service obtains broad access to customer content, allowing it to impersonate other users without providing any proof of user context."

It's worth noting that the Azure AD Graph API has been [officially deprecated and retired](https://learn.microsoft.com/en-us/graph/migrate-azure-ad-graph-overview) as of August 31, 2025, with the tech giant urging users to migrate their apps to Microsoft Graph. The initial announcement of the deprecation was made in 2019.

"Applications that were configured for extended access that still depend on Azure AD Graph APIs will not be able to continue using these APIs starting in early September 2025," Microsoft noted back in late June 2025.

Cloud security company Mitiga said a successful exploitation of CVE-2025-55241 can bypass multi-factor authentication (MFA), Conditional Access, and logging, leaving no trail of the incident.

"Attackers could craft these [actor] tokens in ways that tricked Entra ID into thinking they were anyone, anywhere," Mitiga's Roei Sherman [said](https://www.mitiga.io/blog/breaking-down-the-microsoft-entra-id-actor-token-vulnerability-the-perfect-crime-in-the-cloud). "The vulnerability arose because the legacy API failed to validate the tenant source of the token."

"This meant that an attacker could obtain an Actor token from their own, non-privileged test environment and then use it to impersonate a Global Admin in any other company's tenant. The attacker didn't need any pre-existing access to the target organization."

Previously, Mollema also [detailed](https://thehackernews.com/2025/08/microsoft-discloses-exchange-server.html) a high-severity security flaw affecting on-premise versions of Exchange Server (CVE-2025-53786, CVSS score: 8.0) that could allow an attacker to gain elevated privileges under certain conditions. Another piece of research found that Intune certificate misconfigurations (such as spoofable identifiers) can be [abused](https://dirkjanm.io/extending-ad-cs-attack-surface-intune-certs/) by regular users to [perform](https://learn.microsoft.com/en-us/defender-for-identity/security-assessment-prevent-users-request-certificate) an [ESC1 attack](https://www.semperis.com/blog/esc1-attack-explained/) targeting [Active Directory](https://www.crowdstrike.com/en-us/resources/white-papers/investigating-active-directory-certificate-services-abuse-esc1/) [environments](https://www.beyondtrust.com/blog/entry/esc1-attacks).

The development comes weeks after Binary Security's Haakon Holm Gulbrandsrud disclosed that the shared API Manager (APIM) instance used to facilitate software-as-a-service (SaaS) [conn...