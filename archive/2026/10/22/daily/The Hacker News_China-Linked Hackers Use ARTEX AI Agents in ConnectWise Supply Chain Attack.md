---
title: China-Linked Hackers Use ARTEX AI Agents in ConnectWise Supply Chain Attack
url: https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html
source: The Hacker News
date: 2026-10-22
fetch_date: 2026-10-23T06:46:44.373264
---

# China-Linked Hackers Use ARTEX AI Agents in ConnectWise Supply Chain Attack

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [China-Linked Hackers Use ARTEX AI Agents in ConnectWise Supply Chain Attack](https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html)

**Ravie Lakshmanan**Oct 22, 2026Supply Chain Attack / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBGpr0x4Dn4VV8YVCO_s3CzzGvwmVUceHbt0llcvrzvBmWFaJcu9E9v3WntJGdez3PZ-53GAVSRiYc5FdSOgmyeCSXvpL2t5nCjhzJC50kTLhQygW8cCeFHqtZtDYHsG7Vx2uf1vVdobBbKJ5fcCKSNZDKpV00GRQKVlD444srM9L4rcPnTe28nABZ3pon/s1700-nu-rw-lo-l85-e365/chinese-ai.jpg)

Microsoft on Wednesday disclosed that a China state-aligned actor dubbed **Storm-0940** was behind the recent [supply chain compromise](https://thehackernews.com/2026/10/connectwise-resets-credentials-as-cloud.html) of the ConnectWise Cloud Backup application.

During the incident, Storm-0940 used [ARTEX](https://thehackernews.com/2026/10/artex-ai-pentesting-tool-used-in-data.html), a Go-based agentic AI penetration testing framework that was made closed-source in the wake of its abuse in cyber attacks targeting South Korean financial institutions, to speed up scanning and reconnaissance, password spraying, and OAuth application abuse at downstream victims.

The tech giant said the threat actor used the AI tool at "machine speed" to automate attacks targeting hundreds of organizations across the world spanning a broad range of sectors since September 2026. Targets include aerospace and defense, automotive, chemicals, energy, financial services, government, legal, manufacturing, media, military, semiconductor, software, technology, and think tanks and non-profits.

"Storm-0940's use of ARTEX accelerated the speed of compromised application abuse to authenticate to target environments through applications that had already been granted access, allowing the threat actor to operate without requiring an interactive user sign-in," Microsoft [said](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/).

"AI-accelerated follow-on activity included reconnaissance, application credential changes, and attempts to modify privileges that could enable expanded or persistent access."

Storm-0940 was [first detailed by Microsoft](https://thehackernews.com/2024/11/microsoft-warns-of-chinese-botnet.html) in November 2024, revealing that the threat actor has been leveraging a botnet called Quad7 (aka CovertNetwork-1658) to conduct highly evasive password spray attacks. The threat actor is assessed to be active since at least 2021.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

The adversary is also said to exploit internet-facing applications to gain initial access, followed by using compromised accounts to move through targeted environments. It has also been observed establishing persistence by adding credentials to existing OAuth applications within cloud infrastructures to ensure access to Microsoft 365 resources.

According to Microsoft, a chunk of these ARTEX-driven attacks have resulted in the adversary gaining privileged access to an organization's cloud infrastructure, including several instances where the time frame from initial targeting to privileged access was less than 3 hours.

In the case of the ConnectWise incident, Storm-0940 has been observed using ARTEX to attempt to sign in to more than 2,250 tenants at 2,900 sign-in attempts per minute, a pace the company said gives defenders a short window to detect and respond.

"Between October 10 and 14, 2026, Storm-0940 infrastructure at 144.172.64[.]99 conducted an automated cross-tenant password-spray campaign targeting 327 accounts across eight organizations to gain access to Microsoft 365 and Exchange Online," Microsoft said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3Xc6KzPMPQKO3RtYF_6JEqjdfIY1bg3X-U2zaKO7_TwQzBDY6fsps3qphDQw-9EzTGDGM3kriLuztm4LxzE60yFDE3NVH3LV9p5VUg-oMLpBoPMrk38Uinn18tou_8tiBS6Gc4xO3W8COBOXGFkbkBgkli7YL8txxGUa6wZGNNVuEuM0fADa0cfkuZm2E/s1700-nu-rw-lo-l85-e365/ar.jpg)

During this window, Microsoft said it captured over 151,000 failed logon events. The activity peaked on October 11 at 2,900 failures per minute, resulting in more than 111,000 failures in a single day. Of these, 48 accounts received more than 1,000 failures. No successful authentication, token issuance, Graph call, or directory change was detected, it noted.

That changed on October 15, 2026, when the AI agents gained access to the identities of multiple ConnectWise cloud applications and began to use them to authenticate to customer environments.

"Additionally, after acquiring control of the identities of multiple ConnectWise cloud applications, the AI agents operating on behalf of the threat actor continued to use the same IP range to authenticate to customer environments using the illicit access acquired through these stolen app credentials, effectively taking advantage of the already established trust by these apps within a tenant," the tech giant added.

In some of these cases, the AI agents are assessed to have progressed beyond authentication to Microsoft Graph and directory operations. This included reconnaissance, application credential modifications to establish persistence, and changes involving identities, groups, and privileged roles.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihyvW6Vi5XS9EzEem8mWZ6I1vdQwHj9pQWyIdJMAgk2HxEegqxF3tCKtOw7REdJ_V27mKU6pm6LbGcSKl5zkvy3wdEoNS3hbdGj9LnNXTuuR-g5cWisW5tp7YTHPJTJWEkyl2iDQAF2oAA9IU7tlw7d5n8hNuHwlSq49zCctuAkuI-omxB8NMByUzipUnd/s1700-nu-rw-lo-l85-e365/zz.jpg) |
| The TAG-217 attack chain | Source: Zscaler |

"The application credential modification made by Storm-0940’s associated agents in the targeted victims' environments can lead to persistence through other identities, credentials, and cloud services," Microsoft said. "These changes can remain ac...