---
title: Russian Hackers Breach 20+ NGOs Using Evilginx Phishing via Fake Microsoft Entra Pages
url: https://thehackernews.com/2025/05/russian-hackers-breach-20-ngos-using.html
source: The Hacker News
date: 2025-05-28
fetch_date: 2025-10-06T22:31:21.039851
---

# Russian Hackers Breach 20+ NGOs Using Evilginx Phishing via Fake Microsoft Entra Pages

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

# [Russian Hackers Breach 20+ NGOs Using Evilginx Phishing via Fake Microsoft Entra Pages](https://thehackernews.com/2025/05/russian-hackers-breach-20-ngos-using.html)

**May 27, 2025**Ravie Lakshmanan Cloud Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFNnO-tUbuQ2_gE52PpuSZj7CjuhK6v8t5LcD4qT_m8ittEA5e2cddCXSceaPtd8WcPEmcen6FcYdzyj46Nwpwi33xHJkHmhUIiXa-nWcD8fQn1ugMZF2xQ8OTftVsYPWvwuIVfBKfSY64K9hzQ_dl30nsm3LKxUasBtRLcu2FkWY3GliiSQdJd_jebT8n/s790-rw-e365/evilginx.jpg)

Microsoft has shed light on a previously undocumented cluster of malicious activity originating from a Russia-affiliated threat actor dubbed **Void Blizzard** (aka Laundry Bear) that it said is attributed to "worldwide cloud abuse."

Active since at least April 2024, the hacking group is linked to espionage operations mainly targeting organizations that are important to Russian government objectives, including those in government, defense, transportation, media, non-governmental organizations (NGOs), and healthcare sectors in Europe and North America.

"They often use stolen sign-in details that they likely buy from online marketplaces to gain access to organizations," the Microsoft Threat Intelligence team [said](https://www.microsoft.com/en-us/security/blog/2025/05/27/new-russia-affiliated-actor-void-blizzard-targets-critical-sectors-for-espionage/) in a report published today. "Once inside, they steal large amounts of emails and files."

Attacks mounted by Void Blizzard have been found to disproportionately single out NATO member states and Ukraine, suggesting that the adversary is looking to collect intelligence to further Russian strategic objectives.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Specifically, the threat actor is known to target government organizations and law enforcement agencies in NATO member states and countries that provide direct military or humanitarian support to Ukraine. It's also said to have staged successful attacks aimed at education, transportation, and defense verticals in Ukraine.

This includes the October 2024 compromise of several user accounts belonging to a Ukrainian aviation organization that had been previously targeted by [Seashell Blizzard](https://thehackernews.com/2025/02/microsoft-uncovers-sandworm-subgroups.html), a threat actor tied to the Russian General Staff Main Intelligence Directorate (GRU), in 2022.

The attacks are characterized as opportunistic and targeted high-volume efforts that are engineered to breach targets deemed of value to the Russian government. Initial access methods comprise unsophisticated techniques like password spraying and stolen authentication credentials.

In some of the campaigns, the threat actor has utilized stolen credentials likely sourced from commodity information stealer logs available on the cybercrime underground to access Exchange and SharePoint Online and harvest email and files from compromised organizations.

"The threat actor has also in some cases enumerated the compromised organization's Microsoft Entra ID configuration using the publicly available AzureHound tool to gain information about the users, roles, groups, applications, and devices belonging to that tenant," Microsoft said.

As recently as last month, the Windows maker said it observed the hacking crew shifting to "more direct methods" to steal passwords, such as sending spear-phishing emails that are engineered to trick victims into parting with their login information by means of an adversary-in-the-middle ([AitM](https://thehackernews.com/2023/08/phishing-as-service-gets-smarter.html)) landing pages.

The activity entails the use of a typosquatted domain to impersonate the Microsoft Entra authentication portal to target over 20 NGOs in Europe and the United States. The email messages claimed to be from an organizer from the European Defense and Security Summit and contained a PDF attachment with fake invitations to the summit.

Present wishing the PDF document is a malicious QR code that redirects to an attacker-controlled domain ("micsrosoftonline[.]com") that hosts a credential phishing page. It's believed that the phishing page is based on the open-source [Evilginx](https://thehackernews.com/2023/12/microsoft-warns-of-coldrivers-evolving.html) phishing kit.

Post-compromise actions after gaining initial access encompass the abuse of Exchange Online and Microsoft Graph to enumerate users' mailboxes and cloud-hosted files, and then make use of automation to facilitate bulk data collection. In select instances, the threat actors are also said to have accessed Microsoft Teams conversations and messages via the web client application.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Many of the compromised organizations overlap with past – or, in some cases, concurrent – targeting by other well-known Russian state actors, including [Forest Blizzard](https://thehackernews.com/2025/05/russian-hackers-exploit-email-and-vpn.html), [Midnight Blizzard](https://thehackernews.com/2024/06/french-diplomatic-entities-targeted-in.html), and [Secret Blizzard](https://thehackernews.com/2024/12/secret-blizzard-deploys-kazuar-backdoor.html)," Microsoft said. "This intersection suggests shared espionage and intelligence collection interests assigned to the parent organizations of these threat actors."

### Void Blizzard Linked to September Breach of Dutch Police Agency

In a separate advisory, the Netherlands Defence Intelligence and Security Service (MIVD) attributed Void Blizzard to a September 23, 2024, breach of a Dutch police employee account via a pass-the-cookie attack, stating work-related contact information of police employees was obtained by the threat actor.

Pass-the-cookie attack refers to a scenario where an attacker uses stolen cookies obtained via information stealer malware to sign in to accounts without having to enter a username and password. It...