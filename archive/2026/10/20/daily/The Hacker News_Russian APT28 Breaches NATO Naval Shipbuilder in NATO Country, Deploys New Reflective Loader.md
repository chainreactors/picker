---
title: Russian APT28 Breaches NATO Naval Shipbuilder in NATO Country, Deploys New Reflective Loader
url: https://thehackernews.com/2026/10/russian-apt28-breaches-nato-naval.html
source: The Hacker News
date: 2026-10-20
fetch_date: 2026-10-21T06:51:12.911801
---

# Russian APT28 Breaches NATO Naval Shipbuilder in NATO Country, Deploys New Reflective Loader

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Russian APT28 Breaches NATO Naval Shipbuilder in NATO Country, Deploys New Reflective Loader](https://thehackernews.com/2026/10/russian-apt28-breaches-nato-naval.html)

**Ravie Lakshmanan**Oct 20, 2026Cyber Espionage / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNLZ-1vEmoCyztDVMziqJlhZPTZfW4mOe-qDn6OxDQ-K2LVZTvqhoOe3MIip5bDJfiJd7e3HLcq4S-0xb2SlfWbEqp4vlvbOnQDSP5edsQIxHFtYSCt1qM7XZksq0NPZ9AGesx0YzqHsTeWUuPUTysC5dbuDOvKIjQW0DJvkg1UG9KLH2Doglq7WtgyiRM/s1700-nu-rw-lo-l85-e365/russia-nato.jpg)

The Russia-linked state-sponsored threat actor tracked as **[APT28](https://thehackernews.com/2026/08/suspected-russian-hackers-abuse-google.html)** (aka BlueDelta, Fancy Bear, and Forest Blizzard) has been attributed to attacks targeting two member states of the North Atlantic Treaty Organization (NATO).

The Symantec Threat Hunter Team, which is tracking the activity cluster under the moniker **Swallowtail**, involved the use of a backdoor called HOOKEDGE and a previously undocumented loader that is designed to decrypt and run an encrypted payload in memory by using a cryptographic key that's supplied at runtime.

Targets of the activity included a law enforcement agency, a naval shipbuilder, and a manufacturer of military aircraft engines – entities that hold information that could be of use to a foreign intelligence agency, the Broadcom-owned threat intelligence unit said.

"During one attack against the naval shipbuilder, operators returned to a compromised host repeatedly over the course of a week in what appeared to be hands-on-keyboard activity," Symantec [said](https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets) in a report shared with The Hacker News. "They stole credential material using two separate techniques, opened a persistent SSH tunnel into the organization's internal network and deployed a previously undocumented reflective loader."

APT28's use of HOOKEDGE was [first publicly documented](https://thehackernews.com/2026/08/apt28-linked-hookedge-backdoor-targets.html) by Recorded Future Insikt Group in late August 2026 in connection with a cyber espionage campaign targeting government and diplomatic organizations in Romania, Spain, and Türkiye between September 2025 and early April 2026.

HOOKEDGE shares significant code and tradecraft overlap with [HEADLACE](https://thehackernews.com/2024/05/russian-hackers-target-europe-with.html), a modular Windows implant that APT28 has put to use in attacks targeting diplomats since April 2023. Delivered via spear-phishing lures, HOOKEDGE is a barebones Windows batch script that's capable of accepting attacker-issued commands and sending the results back.

The backdoor is delivered via macro-enabled Microsoft Word documents and communicates entirely through a webhook[.]site URL, which acts as a channel to stage tasks and to receive execution output. Infected machines then fetch these tasks using a hidden, off-screen instance of the Microsoft Edge browser as opposed to relying on a traditional downloader.

In the attack aimed at the naval shipbuilder in late July 2026, the threat actors are said to have delivered new variants of HOOKEDGE that abandon the use of webhook[.]site in favor of a dedicated IP address ("185.82.218[.]119:443") for both tasking and exfiltration.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

"The attackers used two distinct credential-theft techniques," Symantec said. "In one, they pushed an SSH private key onto the compromised host and immediately used it to open an SSH connection back to their own server, requesting a persistent, backgrounded tunnel that would give them a route from their infrastructure into the target's internal network."

"In the other, they ran a short, self-contained PowerShell script that stands up a listener on the host's own loopback address and forces the machine to authenticate to it, capturing the resulting NTLM handshake."

The attackers have also been observed dropping a new reflective loader ("ld.exe") using a curl command via SSH that's engineered to decode and run a next-stage component. The exact nature of the payload remains unknown.

The most recent activity was registered on September 24, 2026, when a Visual Basic Script launcher associated with HOOKEDGE was observed within the shipbuilder's network. It's unclear if any data was stolen as a result of these intrusions.

"The tradecraft observed after initial access, credential theft through two independent techniques, a persistent network tunnel, and a previously undocumented loader, goes beyond the delivery mechanism that has so far been publicly reported on this campaign," Symantec said.

### Attacks Targeting Ukraine in H1 2026

In a report published late last month, the Computer Emergency Response Team of Ukraine (CERT-UA) [revealed](https://cip.gov.ua/ua/news/maskuvannya-ta-socialna-inzheneriya-yak-zminilisya-taktiki-kiberzlochinciv) that Russian hackers are increasingly targeting the smartphones belonging to Ukrainian military personnel and government officials for espionage and financially motivated attacks.

"The growing role of smartphones in communications among military personnel, government employees, and civilians is making them more attractive targets for intelligence gathering activity, further compromise, and financially motivated attacks," the agency [said](https://cip.gov.ua/ua/statics/analitichni-materiali-derzhspeczv-yazku).

This includes the use of the [DarkSword](https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html) iOS exploit kit, which is distributed via watering-hole attacks through compromised legitimate Ukrainian news outlets and government sites to siphon sensitive data from compromised devices.

"The tool is associated with Russian threat actors, and its use against Ukrainian targets points to the adversary's growing interest i...