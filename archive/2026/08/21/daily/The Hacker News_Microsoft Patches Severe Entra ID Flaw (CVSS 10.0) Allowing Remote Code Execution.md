---
title: Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution
url: https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html
source: The Hacker News
date: 2026-08-21
fetch_date: 2026-08-22T02:52:36.945254
---

# Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution](https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html)

**Ravie Lakshmanan**Aug 21, 2026Vulnerability / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEid22xatm4tPGWO1VA9heA8p7i0iK4au3br36QORRasXlUO2uY5836xkZe6gywLOId9oHICopC6jZ8J-di4JI9O3CPOSOGsqoOR4Ps4DrEbKCXSXwMxX_wOGo0fY3zaTW4By4nzbY6jldD58kLAlBYfFxMOEeZOglaQu8R0TtT23Q2jLbQjHwJSoS21pqu5/s1700-e365/entraid.jpg)

***Update: The story was updated after publication to note that the vulnerability has not been exploited.***

*Although the security bulletin originally marked the "Exploited" field under the Exploitability Assessment table as "Yes," on August 21, 2026, Microsoft corrected the "Exploited" status to "No" after The Hacker News contacted the company for comment. It also noted, "this vulnerability was not exploited in the wild."*

*"We identified and addressed this issue with a fix and released [CVE-2026-69836](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69836) for [greater transparency](https://www.microsoft.com/en-us/msrc/blog/2024/06/toward-greater-transparency-unveiling-cloud-service-cves1). There are no additional actions customers need to take,” a Microsoft spokesperson told The Hacker News.*

*The headline has been edited to reflect this change. The original story follows below -*

Microsoft on Thursday warned of a maximum-severity security flaw in Entra ID that it said has been exploited in the wild, but noted that no customer action is required.

The vulnerability, tracked as **CVE-2026-69836** (CVSS score: 10.0), is a case of remote code execution impacting the tech giant's cloud-based identity and access management service. It was previously called Azure Active Directory or Azure AD.

"Deserialization of untrusted data in Microsoft Entra ID allows an unauthorized attacker to execute code over a network," Microsoft [said](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69836) in an alert released Thursday.

[Flaws of this kind](https://cwe.mitre.org/data/definitions/502.html) occur when an application converts user-controlled data back into an active object or code structure without proper validation. This can [lead to](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data) code execution, denial-of-service, or access control bypass that can permit an attacker to perform unauthorized actions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The company credited principal security engineer Robert Fitzpatrick for discovering and reporting the issue.

As of writing, there are currently no details on how the vulnerability has been exploited, when these efforts began and if they are still ongoing, and how it was discovered.

"This vulnerability has already been fully mitigated by Microsoft," it added. "There is no action for users of this service to take."

Earlier this month, Redmond also [patched](https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html) a high-severity security privilege escalation flaw affecting Windows Ancillary Function Driver for WinSock (CVE-2026-68820, CVSS score: 7.0) that was exploited as a zero-day by the North Korea-linked Lazarus Group as part of a long-running campaign dubbed Operation Dream Job.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Identity Security](https://thehackernews.com/search/label/Identity%20Security), [Microsoft](https://thehackernews.com/search/label/Microsoft), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](data:image/svg+xml;base64... "Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database")

Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html)

[![Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations](data:image/svg+xml;base64... "Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations")

Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations](https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html)

[![Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](data:image/svg+xml;base64... "Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw")

Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](https://thehackernews.com/2026/07/researchers-re...