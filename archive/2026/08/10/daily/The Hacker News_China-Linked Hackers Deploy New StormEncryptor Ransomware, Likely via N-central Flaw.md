---
title: China-Linked Hackers Deploy New StormEncryptor Ransomware, Likely via N-central Flaw
url: https://thehackernews.com/2026/08/china-linked-hackers-deploy-new.html
source: The Hacker News
date: 2026-08-10
fetch_date: 2026-08-11T03:31:50.959435
---

# China-Linked Hackers Deploy New StormEncryptor Ransomware, Likely via N-central Flaw

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

![cybersecurity](data:image/svg+xml;base64...)

# [China-Linked Hackers Deploy New StormEncryptor Ransomware, Likely via N-central Flaw](https://thehackernews.com/2026/08/china-linked-hackers-deploy-new.html)

**Ravie Lakshmanan**Aug 10, 2026Ransomware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNv5C82jT_6YlarerdXnoAR_tT3E8xP65ZWuJfpvOKU9baBT5UACUTb88XvDQgQA6RrYuqPK3FstaqwacR9gDjD0qwk3HUYl0wK848phyphenhyphenFuqRrOA1AqdISQaA6tpEqg0n2XJIA22NeNNbhei1bAgcyghnc2qaVfSvh4fd9J1oD4xVi-DQcNSOYWQovyUst/s1700-e365/strom-ransomware.jpg)

Microsoft has disclosed that **Storm-1175**, a financially motivated threat actor linked to China, has deployed a previously undocumented ransomware strain called **StormEncryptor**.

The use of StormEncryptor marks a shift from the adversary's previous use of Medusa ransomware, the Microsoft Threat Intelligence Team said.

"StormEncryptor is written in C++ and appends the file name extension .encrypted to files it encrypts," Microsoft [noted](https://bsky.app/profile/threatintel.microsoft.com/post/3msjiybnb252n) in a series of posts on Bluesky. "It then drops a ransom note named !!!README\_FIRST!!!.txt to every scanned directory."

Although the exact vulnerability exploited by the threat actor as part of this campaign is unclear, the tech giant said it likely involves the exploitation of [CVE-2026-18577](https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html), a newly disclosed security flaw in N-able N‑central, to obtain initial access.

The vulnerability is assessed to be a patch bypass for CVE-2026-18556, both of which allow authentication bypass and account takeover in susceptible versions. The vulnerabilities have since been flagged by the U.S. Cybersecurity and Infrastructure Security Agency (CISA) as actively exploited in the wild.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Storm-1175 is the name assigned to a [China-based threat actor](https://x.com/MsftSecIntel/status/1781353321267069292) with a history of deploying Medusa ransomware after exploiting security flaws in Mirth Connect ([CVE-2023-37679](https://nvd.nist.gov/vuln/detail/cve-2023-37679), [CVE-2023-43208](https://nvd.nist.gov/vuln/detail/cve-2023-43208)), ConnectWise ScreenConnect ([CVE-2024-1709](https://nvd.nist.gov/vuln/detail/cve-2024-1709), [CVE-2024-1708](https://nvd.nist.gov/vuln/detail/cve-2024-1708)), JetBrains TeamCity ([CVE-2024-27198](https://nvd.nist.gov/vuln/detail/cve-2024-27198), [CVE-2024-27199](https://nvd.nist.gov/vuln/detail/cve-2024-27199)), and Fortinet FortiClient EMS ([CVE-2023-48788](https://nvd.nist.gov/vuln/detail/cve-2023-48788)).

In an analysis published in October 2025, Microsoft also [attributed](https://thehackernews.com/2025/10/microsoft-links-storm-1175-to.html) the threat actor to the exploitation of a critical security vulnerability impacting Fortra GoAnywhere (CVE-2025-10035) to facilitate the deployment of Medusa ransomware.

The group, per the Windows maker, [weaponizes](https://thehackernews.com/2026/04/china-linked-storm-1175-exploits-zero.html) a combination of zero-days and N-day vulnerabilities to carry out high-velocity attacks and break into susceptible internet-facing systems by taking advantage of the window between vulnerability disclosure and patch adoption.

"In this new activity, Storm-1175's post-compromise behavior includes abuse of remote monitoring and management tools AnyDesk or SimpleHelp, Advanced IP Scanner for discovery, and LSASS dumping using Mimikatz," it added.

Storm-1175 has also been observed rapidly moving from initial access to data exfiltration and ransomware deployment, mostly within a few days, making it essential that customers apply the patches as soon as possible.

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

[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [Cybercrime](https://thehackernews.com/search/label/Cybercrime), [data exfiltration](https://thehackernews.com/search/label/data%20exfiltration), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [network security](https://thehackernews.com/search/label/network%20security), [ransomware](https://thehackernews.com/search/label/ransomware), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](data:image/svg+xml;base64... "Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database")

Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html)

[![Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations](data:image/svg+xml;base64... "Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations")

Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations](https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html)

[![Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](data:image/svg+xml;base64... "Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw")

Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](https://thehackernews.com/2026/07/researchers-report-84-flaws-in-4g-and.html)

[![Cheap Android T...