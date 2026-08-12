---
title: Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push VPN That Can Run Commands
url: https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:49.149847
---

# Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push VPN That Can Run Commands

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

# [Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push VPN That Can Run Commands](https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html)

**Ravie Lakshmanan**Aug 11, 2026Social Engineering / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiP9vK0AfjfbpQDa7i5il113N22qO5N-mxuOw7qoNVnvUOnQIYRjhuKA8rxdRhaZ13t0r5jZtsj1bjQQatdbdxi3L1Fso99wsDJIAKkw6NVklb6S2PBfipUtUm6qNdGofjKrmSAHUc0P4qgPRK2tDoGftkwyD17KQHQm6cYP80rT4dUH-tg0rnd5SSfQBJl/s1700-e365/interview.jpg)

The Computer Emergency Response Team of Ukraine (CERT-UA) has disclosed details of a new social engineering campaign orchestrated by Russian nation-state threat actors targeting IT workers in the country by masquerading as recruiters to trick them into installing malware.

CERT-UA pinned the activity on a threat cluster it tracks as **[UAC-0145](https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html)**, which is a subgroup within Sandworm (aka APT44, Seashell Blizzard, and UAC-0002), a sophisticated hacking group affiliated with the GRU. The campaign is assessed to be ongoing since May 2026.

"Specifically, on job search websites, after reviewing a candidate's resume, the attackers contact a potential victim – typically a system administrator or IT specialist – on behalf of an IT company (such as ATLAS Business Group)," CERT-UA [said](https://cert.gov.ua/article/6318863).

Although initial communications take place via built-in online chat, the conversation subsequently shifts to messaging apps like Telegram, where a preliminary chat takes place with a purported HR manager who claims to be in charge of the candidate screening process for Sopra Steria Bulgaria, a legitimate European-based consulting and software company.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

As part of the chat, the agency said general work-related questions and the candidates' English language proficiency are discussed, after which they are invited to join a Zoom videoconference call.

While the meeting does take place as expected with an English-speaking man who appears to be between 30 and 35 years old, it's unclear whether the person showing up in the interview was a genuine participant or a synthetic persona generated using artificial intelligence (AI).

In tandem, additional instructions for a technical interview are sent via an email. This includes configuration files for connecting to the corporate VPN using WireGuard to supposedly complete an assessment, along with a link to a second Zoom meeting during which the test is monitored.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK1bTASo1eLTmfShwr26TyP1anmM-gPb8jNUHwCNer06ocT0byYeJRCVUrcGt5kHt0nMoDorvR44v_AvK0iCUcVHd0ID3YJJU83yHQdIRek3K1Y4PJY1jmZYq7Elxw3AuOigCL3b9LRiqm3pPQ1kfDAtTXNOe9Qo6Zlgj4Uh0yVUScV1JmAeGUDQ-m8gb6/s1700-e365/worker.png)

Should the victim attempt to connect to the VPN using the provided configuration files, they run into error messages, causing the threat actors to recommend downloading a custom VPN solution named SopraVPN hosted on SourceForge by sharing a bogus link designed to mimic Sopra Steria Bulgaria's website ("soprasteria-bg[.]com") -

* sourceforge[.]net/projects/soprabulgariavpn
* sourceforge[.]net/projects/sopravpn

The Hacker News also identified a third SourceForge project called "sourceforge[.]net/projects/soprasteriavpn/," which claims to be an "open-source corporate VPN solution designed for businesses seeking secure remote access and site-to-site connectivity without expensive licensing fees," according to cached Google Search results. None of these projects are available for download.

"The essence of this trick is that the attackers' VPN client was compiled from the WireGuard source code with a number of modifications," CERT-UA explained. "Specifically, support for the non-standard 'SymmetricKey' option has been added to the configuration processing mechanism; its value contains BASE64-encoded data for AES-256-GCM: a nonce, ciphertext, and an authentication tag."

"A 32-byte value obtained by decoding 'PrivateKey' is used as the AES-256 key. The PowerShell code decrypted in this way is then passed to the standard 'runScriptCommand' mechanism, which WireGuard uses, in particular, to execute commands specified by the 'PostUp' option."

Put differently, the poisoned version of WireGuard allows an attacker to run arbitrary commands on the victim host without their knowledge.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The Windows VPN client also makes use of a PowerShell command to create a scheduled task that downloads a secondary payload from a remote URL, while the Linux variant uses cURL to download the executable file from the attackers' infrastructure via a VPN. The exact nature of the next-stage payload is unclear.

CERT-UA is urging IT professionals to be on the lookout for social engineering techniques to stay protected against potential malware attacks. Organizations are recommended to allow access to corporate resources only from managed devices on which appropriate security software is installed and ensure relevant policies are configured and continuous monitoring is enforced.

The disclosure comes less than a month after the agency attributed the threat actor to [another campaign](https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html) that employs the ClickFix social engineering tactic to infect Ukrainian machines with data-stealing malware.

With the latest development, Russian threat actors have joined alongside [Chinese](https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html#:~:text=Five%20Eyes%20Warns%20of%20China%20Exploiting%20LinkedIn%20to%20Target%20Security%20Personnel), [Iranian](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html), and [North Korean](https://thehackernews.com/2026/02/dprk-operatives-impersonate.html) adversaries in using fake recruitment campaigns to gain unauthorized access to targeted systems.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZD...