---
title: Microsoft Detects "SesameOp" Backdoor Using OpenAI's API as a Stealth Command Channel
url: https://thehackernews.com/2025/11/microsoft-detects-sesameop-backdoor.html
source: The Hacker News
date: 2025-11-04
fetch_date: 2025-11-05T03:12:48.669938
---

# Microsoft Detects "SesameOp" Backdoor Using OpenAI's API as a Stealth Command Channel

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

# [Microsoft Detects "SesameOp" Backdoor Using OpenAI's API as a Stealth Command Channel](https://thehackernews.com/2025/11/microsoft-detects-sesameop-backdoor.html)

**Nov 04, 2025**Ravie LakshmananArtificial Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyW72-Rg4bg2ntYrHhAcMLWcUMdg-0COcApiiLP4LsguHFgDgBVZmEh0EigMblA_-TZm9wKArXWY58AqupvM2vpr3anQXEGkmmAtw20_4WOO4qVL8ykulVPadSXRdZTyanhMeEKt-TPI5i5SGpUmjlNlAYEZUepDpzDujBAULaGbzuXSSzP5W6NsPofRXD/s790-rw-e365/SesameOp-Malware.jpg)

Microsoft has disclosed details of a novel backdoor dubbed **SesameOp** that uses OpenAI Assistants Application Programming Interface (API) for command-and-control (C2) communications.

"Instead of relying on more traditional methods, the threat actor behind this backdoor abuses OpenAI as a C2 channel as a way to stealthily communicate and orchestrate malicious activities within the compromised environment," the Detection and Response Team (DART) at Microsoft Incident Response [said](https://www.microsoft.com/en-us/security/blog/2025/11/03/sesameop-novel-backdoor-uses-openai-assistants-api-for-command-and-control/) in a technical report published Monday.

"To do this, a component of the backdoor uses the OpenAI Assistants API as a storage or relay mechanism to fetch commands, which the malware then runs."

The tech giant said it discovered the implant in July 2025 as part of a sophisticated security incident in which unknown threat actors had managed to maintain persistence within the target environment for several months. It did not name the impacted victim.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Further investigation into the intrusion activity has led to the discovery of what it described as a "complex arrangement" of internal web shells, which are designed to execute commands relayed from "persistent, strategically placed" malicious processes. These processes, in turn, leverage Microsoft Visual Studio utilities that were compromised with malicious libraries, an approach referred to as [AppDomainManager injection](https://attack.mitre.org/techniques/T1574/014/).

SesameOp is a custom backdoor engineered to maintain persistence and allow a threat actor to covertly manage compromised devices, indicating that the attack's overarching goal was to ensure long-term access for espionage efforts.

OpenAI [Assistants API](https://platform.openai.com/docs/assistants/migration) enables developers to integrate artificial intelligence (AI)-powered agents directly into their applications and workflows. The API is scheduled for deprecation by OpenAI in August 2026, with the company replacing it with a new Responses API.

The infection chain, per Microsoft, includes a loader component ("Netapi64.dll") and a .NET-based backdoor ("OpenAIAgent.Netapi64") that leverages the OpenAI API as a C2 channel to fetch encrypted commands, which are subsequently decoded and executed locally. The results of the execution are sent back to OpenAI as a message.

"The dynamic link library (DLL) is heavily obfuscated using Eazfuscator.NET and is designed for stealth, persistence, and secure communication using the OpenAI Assistants API," the company said. "Netapi64.dll is loaded at runtime into the host executable via .NET AppDomainManager injection, as instructed by a crafted .config file accompanying the host executable."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

The message supports three types of values in the description field of the Assistants list retrieved from OpenAI -

* **SLEEP**, to allow the process thread to sleep for a specified duration
* **Payload**, to extract the contents of the message from the instructions field and invoke it in a separate thread for execution
* **Result**, to transmit the processed result to OpenAI as a new message in which the description field is set to "Result" to signal the threat actor that the output of the execution of the payload is available

It's currently not clear who is behind the malware, but the development illustrates continued abuse of legitimate tools for malicious purposes to blend in with normal network activity and sidestep detection. Microsoft said it shared its findings with OpenAI, which identified and disabled an API key and associated account believed to have been used by the adversary.

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

[Backdoor](https://thehackernews.com/search/label/Backdoor)[Command and Control](https://thehackernews.com/search/label/Command%20and%20Control)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Incident response](https://thehackernews.com/search/label/Incident%20response)[Malware](https://thehackernews.com/search/label/Malware)[OpenAI](https://thehackernews.com/search/label/OpenAI)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-ai-security)

Trending News

[![⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](data:image/svg+xml;base64... "⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens")

⚡ Weekly Recap: WSUS Exploited,...