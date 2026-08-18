---
title: Cavern C2 Uses DNS and Google Apps Script to Blend Into Legitimate Traffic
url: https://thehackernews.com/2026/08/cavern-c2-uses-dns-and-google-apps.html
source: The Hacker News
date: 2026-08-17
fetch_date: 2026-08-18T02:54:02.192047
---

# Cavern C2 Uses DNS and Google Apps Script to Blend Into Legitimate Traffic

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

# [Cavern C2 Uses DNS and Google Apps Script to Blend Into Legitimate Traffic](https://thehackernews.com/2026/08/cavern-c2-uses-dns-and-google-apps.html)

**Ravie Lakshmanan**Aug 17, 2026Cyber Espionage / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhu-MyaPNuRr2_NJ_TMqLf7OYW5AzCqgHpQ6HMfxlc-qsMzwSkfWlZDbHfecZ3IRp639FVDelhMZgpbnN87Fdchoh-g08R-cAiXxr7RvfdGy_ihvMxg152HK-rbOTIOnEueRTnPT-wU0eID3vplpIN1GBClvJC5e0egCGpDb_H0ykwH1x6a4zOvpW8V-Ssy/s1700-e365/google.jpg)

Cybersecurity researchers have traced the continued evolution of the **Cavern** (aka Cav3rn) command-and-control (C2) framework used by Iranian nation-state hackers in attacks targeting entities in Israel.

Russian cybersecurity company Kaspersky said its ongoing monitoring of the threat activity cluster since December 2025 has led to the discovery of previously unreported components that expand the toolkit's communication capabilities.

"The main finding is a complex C2 module that uses DNS A-record responses to choose between direct HTTPS and a Google Apps Script relay for each transaction," Kaspersky [said](https://securelist.com/project-cav3rn-continues/120991/) in an analysis. "The same DNS infrastructure can validate and replace the relay deployment ID, allowing the operator to rotate the Google channel."

Cavern, [first publicly documented](https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html) by Check Point Research in early July 2026, consists of multiple moving parts, including an Agent and an assortment of modules, that work in tandem to enable mission-specific post-exploitation functionality, while minimizing forensic visibility and ensuring persistent access.

The modules facilitate file operations, SQL database enumeration, Active Directory reconnaissance, LDAP brute-force attacks, network reconnaissance, and SOCKS5 proxy and WebSocket tunneling. The use of Cavern C2 has been linked to Cavern Manticore, a hacking group affiliated with Iran's Ministry of Intelligence and Security (MOIS) that shares overlaps with MuddyWater and an OilRig sub-group known as Lyceum.

Two back-to-back follow-up reports from [Group-IB](https://www.group-ib.com/blog/hollowgraph-microsoft-365/) and [Kaspersky](https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/) detailed another module dubbed HOLLOWGRAPH that turns Microsoft 365 calendars into covert C2 channels. The malware, in particular, abuses the Microsoft Graph API to exfiltrate files and receive commands from the attacker using Microsoft 365 calendar events, and DNS tunneling to refresh credentials used in C2 communication.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"Using the Microsoft Graph API, it treats the compromised mailbox's calendar as a two-way dead-drop: operators plant tasking as calendar events, and the implant exfiltrates stolen files by creating its own events with encrypted data attached," Group-IB noted. "To avoid catching the mailbox owner's attention, every event is dated far into the future — 13 May 2050 — with payloads attached as files to the event."

In tandem, the malware employs DNS tunneling as a way to refresh the Microsoft Entra ID (Azure AD) credentials used to authenticate to the Graph API and write the updated values to a text file on disk. A .NET NativeAOT-compiled DLL, HOLLOWGRAPH, was first detected in the wild on June 7, 2026.

Cavern's shift to a modular, extensible architecture using a plugin-based system is assessed to have taken place in late April 2026, per Kaspersky, which has since linked it to OilRig (aka APT34) with low confidence, citing the following indicators despite no direct code reuse or infrastructure overlap -

* Use of Microsoft-hosted services for C2 (e.g., [RDAT](https://thehackernews.com/2025/06/iran-linked-bladedfeline-hits-iraqi-and.html), [OilCheck](https://thehackernews.com/2023/12/iranian-state-sponsored-oilrig-group.html))
* Presence of secondary recovery mechanism to obtain replacement OAuth refresh tokens, as observed in [OilBooster](https://thehackernews.com/2023/12/iranian-state-sponsored-oilrig-group.html)
* Use of compromised infrastructure belonging to entities in regions it targets, as observed in [Solar](https://thehackernews.com/2023/09/iranian-nation-state-actor-oilrig.html) and [Veaty](https://thehackernews.com/2024/09/iranian-cyber-group-oilrig-targets.html) malware

The latest findings from Kaspersky are a new communication module, GoogleService.dll, which reads a configuration file from disk ("conf.json") and performs a DNS A-record query to opt for either a direct HTTPS or a Google Apps Script relay for each transaction.

When the Google mode is selected, the module sends requests to the Apps Script deployment, which then forwards them to the threat actor-controlled backend. If Direct HTTPS is chosen by DNS, it contacts the configured address without using the relay.

The cybersecurity vendor said it also discovered an inter-component broker ("rnp.dll") that functions as the framework's local bridge, which discovers and loads DLL components, routes messages between them, and supports runtime upgrades. Although the primary domain linked to the activity ("studiotikva[.]com") was first registered in February 2024, the domain is said to have expired in February 2026, only for it to be re-registered three months later.

The development is a sign of ongoing evolution of the Cavern framework, while relying on legitimate services to evade conventional perimeter defenses.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"By abusing legitimate services — previously Outlook calendar events and now Google Apps Script — the framework blends its C2 traffic with normal network activity, complicating network-based detection," Kaspersky said. "Given its development pace, modular design, and operational tempo, we assess ...