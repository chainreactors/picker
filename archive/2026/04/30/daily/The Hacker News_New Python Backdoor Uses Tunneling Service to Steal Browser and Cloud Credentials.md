---
title: New Python Backdoor Uses Tunneling Service to Steal Browser and Cloud Credentials
url: https://thehackernews.com/2026/04/new-python-backdoor-uses-tunneling.html
source: The Hacker News
date: 2026-04-30
fetch_date: 2026-05-01T05:40:14.350696
---

# New Python Backdoor Uses Tunneling Service to Steal Browser and Cloud Credentials

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [New Python Backdoor Uses Tunneling Service to Steal Browser and Cloud Credentials](https://thehackernews.com/2026/04/new-python-backdoor-uses-tunneling.html)

**Ravie Lakshmanan**Apr 30, 2026Cloud Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnv1KtLLlZSnm9a16bN-o_szrBiAIN_QljTfe09K4RzFxSqhFADtuXmRzOPZ_Poazif-VadFAnRnboCWX5yZtc5JntGopn5Fy6T1X2BexXelFOxYtEA7qULoTCkAMwEybLf42JJ_yGjSPf_T-tjYvbqxscVgZ6OyL65yKcTjC0KQL48pgYLZUmLjxfBBhd/s1700-e365/malware-data.jpg)

Cybersecurity researchers have disclosed details of a stealthy Python-based backdoor framework called **DEEP#DOOR** that comes with capabilities to establish persistent access and harvest a wide range of sensitive information from compromised hosts.

"The intrusion chain begins with execution of a batch script ('install\_obf.bat') that disables Windows security controls, dynamically extracts an embedded Python payload ('svc.py'), and establishes persistence through multiple mechanisms including Startup folder scripts, registry Run keys, scheduled tasks, and optional WMI subscriptions," Securonix researchers Akshay Gaikwad, Shikha Sangwan, and Aaron Beardslee [said](https://www.securonix.com/blog/deepdoor-python-backdoor-and-credential-stealer/) in a report shared with The Hacker News.

It's assessed that the batch script is distributed via traditional approaches like phishing. It's currently not known how widespread attacks distributing the malware are, and if any of those infections have been successful.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-blindspot-d-2)

"Based on our current analysis, there is no clear evidence to suggest that this malware framework was widely used in large-scale or highly active campaigns," Gaikwad, senior security research engineer at Securonix, told The Hacker News via email. "Its observed usage appears to be limited and somewhat targeted rather than broadly distributed."

"At this stage, we have not identified consistent indicators pointing to specific geographies or industry sectors being systematically targeted. However, given the modular nature of the framework, it is possible that different threat actors could adapt it for varied use cases over time."

What makes the attack chain noteworthy is that the core Python implant is embedded directly inside the dropper script, from where it's extracted, reconstructed, and executed. This reduces the need for repeatedly having to reach out to external infrastructure and minimizes the forensic footprint.

Once launched, the malware establishes communication with "bore[.]pub," a Rust-based [tunneling service](https://github.com/ekzhang/bore), allowing the operator to issue commands that facilitate remote command execution and extensive surveillance. This includes -

* Reverse shell
* System reconnaissance
* Keylogging
* Clipboard monitoring
* Screenshot capture
* Webcam access
* Ambient audio recording
* Web browser credential harvesting
* SSH key extraction
* Credentials stored in Google Chrome, Mozilla Firefox, and Windows Credential Manager
* Cloud credential theft (Amazon Web Services, Google Cloud, and Microsoft Azure)

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1t7zOpRmrIVSguLc9OmYWkocUNQDbg2kY01KLEY6JqeaYZITnWPJa5k0SyJO-G6ekJFuGzOVljCBRj7QKrMF5Q3Jdl3bLICSuS5HaGScEtC7ZXD40x_qCo5B1pdpYb7hniooKWtgLuwNZSUo2UTk9Kz4hx9uo_o6pbvURBckyegtC8GZDvzdNkioa-Fbk/s1700-e365/sand.jpg)

The use of public TCP tunneling service for command-and-control (C2) offers several advantages in that it eliminates the need for setting up dedicated infrastructure, blends malicious traffic, and avoids embedding details of the server within the payload.

In parallel, DEEP#DOOR incorporates a bevy of anti-analysis and defense evasion mechanisms, such as sandbox, debugger, and virtual machine (VM) detection, AMSI and Event Tracing for Windows ([ETW](https://www.elastic.co/security-labs/kernel-etw-best-etw)) patching, NTDLL unhooking, Microsoft Defender tampering, SmartScreen bypass, PowerShell logging suppression, command-line wiping, timestamp stomping, and log clearing, to fly under the radar and complicate incident response efforts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

It also employs multiple persistence mechanisms that involve creating Windows Startup folder scripts, Registry Run keys, and scheduled tasks, while also relying on a watchdog mechanism to make sure the persistence artifacts have not been removed, and if so, automatically recreate them, making remediation challenging.

"The resulting implant operates as a fully featured Remote Access Trojan (RAT) capable of long-term persistence, espionage, lateral movement, and post-exploitation operations within compromised environments," Securonix said. "The implant prioritizes evading detection and forensic visibility by directly tampering with Windows security and telemetry mechanisms."

"DEEP#DOOR highlights the continued evolution of threat actors toward fileless, script-driven intrusion frameworks that rely heavily on native system components and interpreted languages like Python. By embedding the payload directly within the dropper and extracting it at runtime, the malware significantly reduces external dependencies and limits traditional detection opportunities."

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

[Cloud security](https://thehack...