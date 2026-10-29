---
title: American Organizations Under Attack: Skyw4lker Device Code Phishing Campaign Exposed
url: https://thehackernews.com/2026/10/american-organizations-under-attack.html
source: The Hacker News
date: 2026-10-28
fetch_date: 2026-10-29T07:52:55.868347
---

# American Organizations Under Attack: Skyw4lker Device Code Phishing Campaign Exposed

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

# [American Organizations Under Attack: Skyw4lker Device Code Phishing Campaign Exposed](https://thehackernews.com/2026/10/american-organizations-under-attack.html)

**The Hacker News**Oct 28, 2026Threat Intelligence / Phishing

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgf2g4rsWnZ5eQP03cr-4e99MQStvJmuaTTi91WESG3ua1ddAW73T6X22gyaspj2SirqH-1bSAU9VkOg2F1Kh9TLmPc4jYsNAlD72S2XzCeTTRHSiN3B7is7roWwIMcIm__yRu8SkUBbyeWxAEBo5Fe-bbACZWRuoxZqv_pysQ9iMsZRHPCD_clJZsNIDs/s1700-nu-rw-lo-l85-e365/anyrun-main.jpg)

Modern phishing campaigns can compromise American businesses without relying on traditional credential theft. Attackers can abuse legitimate cloud services, authentication mechanisms, and trusted business workflows to gain access to corporate accounts while leaving fewer obvious signs behind.

[ANY.RUN](https://any.run/?utm_source=the+hacker+news&utm_medium=article&utm_campaign=skyw4lker&utm_content=landing&utm_term=281026)'s analysis of **Skyw4lker**, a device code phishing campaign primarily targeting U.S. organizations, shows how this works in practice. The campaign has focused on **manufacturing, technology, and healthcare**, using business-themed documents, Google-hosted infrastructure, and Microsoft authentication flows to facilitate account compromise.

For security teams, the investigation goes beyond identifying the initial lure. It requires tracing the authentication flow and supporting infrastructure, extracting reliable indicators, and turning those findings into detections that can protect the wider organization.

## Device Code Phishing: A Growing Challenge for U.S. Organizations

The scale of [phishing](https://any.run/use-case/phishing/?utm_source=the+hacker+news&utm_medium=article&utm_campaign=skyw4lker&utm_content=use+case&utm_term=281026) in the United States provides an important backdrop. The FBI's Internet Crime Complaint Center recorded **193,407 phishing and spoofing complaints in 2024**, making it one of the most frequently reported categories of internet crime. In 2025, the FBI recorded more than **1 million internet crime complaints and $20.9 billion in reported losses**, with reported losses increasing by 26% compared with the previous year.

Attackers are also adapting to organizations that have invested heavily in identity security and MFA.

Device code phishing is one example. Rather than collecting credentials through a fake login page, an attacker can initiate a legitimate device authorization flow and convince the victim to complete it. The resulting authentication tokens can then provide access to resources available to the compromised account.

## How Skyw4lker Uses Legitimate Authentication to Compromise Accounts

### How the Skyw4lker Campaign Works

Skyw4lker starts with a lure designed to resemble normal business correspondence, as observed in [ANY.RUN’s Interactive Sandbox analysis](https://app.any.run/tasks/371eeef8-8ac2-4421-a25b-b648821375ef/?utm_source=the+hacker+news&utm_medium=article&utm_campaign=skyw4lker&utm_content=tasks&utm_term=281026).

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJtc9154avvOLd3paepvz5xpCgpYMg6G6HK075CmP9LQcAKG5StKjBvftTDiVtzON4e_-CYsIQR0FrpoP66lJYAHZ_3h7TiMs52TGQJeqDnHqPNdcaeJgxBUhUNRaYmI_d_YfrjWU_E8mnoatHqlEIyA8OOXUUGzJs48-aGpcXsyUoaQAJM6DzJ4v93HE/s1700-nu-rw-lo-l85-e365/1.png) |
| The Skyw4lker phishing kit identified in ANY.RUN’s Interactive Sandbox |

Victims receive a **password-protected document presented as a contract or service proposal**. The scenario is credible in environments where employees routinely exchange vendor agreements, procurement documents, statements of work, and similar files.

From the document, the victim is directed toward a page hosted on **sites[.]google[.]com**, which eventually leads into a Microsoft authentication flow.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidyVX35TbCFcs2vzm9YujaSa9sZZ4eqcN7DBPYv9L9WJCPh9dmbEUq0OSW8_ekhpsLs5dOdEFiSuS4JF00BVPRTIpgRflh7zUJEaGfpAuQ4g8eBrX_n-j23pT3UzzBAPviYa2Utc6xNEqqhSQBcyPFSe9CyAex5J-uCiJh0ScSPy4x5H_KrIQtaci8t4I/s1700-nu-rw-lo-l85-e365/2.png) |
| Skyw4lker redirecting the victims to a Microsoft365 authentication page |

The attacker does not need to reproduce Microsoft's login experience perfectly. The authentication itself can be legitimate; the deception is in convincing the victim to complete an authentication request initiated by the attacker.

Once the process is completed, the attacker can obtain access to the resulting Microsoft 365 tokens.

That makes the attack difficult to evaluate through identity telemetry alone. An organization may see a valid authentication event without immediately seeing the malicious context that caused it. Establishing what happened requires the security team to connect the document, web activity, authentication flow, and associated infrastructure.

### The Infrastructure Behind the Skyw4lker Phishing Page

The web infrastructure used by Skyw4lker provides additional evidence of the campaign's operation.

[ANY.RUN](https://any.run/?utm_source=the+hacker+news&utm_medium=article&utm_campaign=skyw4lker&utm_content=landing&utm_term=281026)’s analysis identified **obfuscated JavaScript and a PHP backend** used to create a victim session, collect information such as IP address and geolocation, and repeatedly poll the backend while waiting for the authentication process to complete.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEih5cQJdpu64eI4bFn5NTgB082Yz3-AWgxeuRP7epG3woBVTkwnVK4IYlT-6yIfCGHSO2UCr0iXlBVLPInnXLyQYgyWz7qA8uKTtd7wvgYHEx0ZR4XsPEJTy01yVIjkgZnQzrYAcd8URGwuQ50kYWE2SMBdnCr4coDB0mOtmwLZzXj6pZjhKPPyKrsKeFA/s1700-nu-rw-lo-l85-e365/3.png) |
| Skyw4lker sample submissions in ANY.RUN’s Interactive Sandbox by country |

A static inspection of the original document may reveal the starting URL, but ...