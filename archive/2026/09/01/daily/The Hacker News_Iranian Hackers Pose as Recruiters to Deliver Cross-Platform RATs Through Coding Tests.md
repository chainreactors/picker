---
title: Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests
url: https://thehackernews.com/2026/09/iranian-hackers-pose-as-recruiters-to.html
source: The Hacker News
date: 2026-09-01
fetch_date: 2026-09-02T06:41:52.621630
---

# Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests](https://thehackernews.com/2026/09/iranian-hackers-pose-as-recruiters-to.html)

**Ravie Lakshmanan**Sep 01, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm2I0vj1ygDfFQ8UzazaxECq0aAP3UJ_VRMzeCN0MgTkWk4yLEUbKKU9dE0pIyXZIfJ0MgxjYEqAqWLAXAtuATDCdFZPI9WGkgwz04Mdd7LChIfMrWk-vhGfaHDGtySDkbIXgzBcNfh5qcobm-bz8QWuyVCcH7z9CM_RNZusA2rPEHV5g2WJ2tU6Llrdnu/s1700-nu-rw-lo-l85-e365/iran-hacking.jpg)

The Iranian **Nimbus Manticore** hacking group has been attributed to two previously undocumented malware families that highlight the continued evolution of its toolset and likely expand its targeting footprint to infect Linux and Apple macOS systems using cross-platform remote access trojans (RATs) developed using Node.js and JavaScript.

Russian cybersecurity company Kaspersky is tracking the malware strains under the names NodeRabbit and PollCat. The first sample of NodeRabbit was discovered on a system in Afghanistan, with subsequent sightings on two distinct machines located in Egypt and Ethiopia.

"Its operators deliver [NodeRabbit] through spear-phishing messages on LinkedIn and other job search platforms that contain trojanized coding challenge archives," Kaspersky security researcher Omar Amin [said](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/). "Like NodeRabbit, PollCat is a cross-platform RAT, but it is written in obfuscated JavaScript also distributed through trojanized coding challenge archives."

While Nimbus Manticore has historically employed malware written in C, C++, and Go, and relied on DLL search-order hijacking techniques to deploy them, the latest findings mark the threat actor's foray into cross-platform tools to accomplish its goals.

The development also comes amid a [rapid expansion](https://thehackernews.com/2026/07/nimbus-manticore-deploys-nightledger.html) of the hacking group's [malware arsenal](https://thehackernews.com/2026/08/nimbus-manticore-expands-toolset-with.html) in recent months, including -

* A Windows backdoor called NightLedger
* Two custom WebSocket tunnelers, BridgeHead and ArcBridge
* A reverse SSH tunneling tool
* A backdoor that shares overlaps with TWOSTROKE

The starting point of the suspicious activity observed in the Afghanistan-based system starts with a ZIP file ("Front-Technical-Challenge.zip") hosted on AWS that's assessed to have been delivered as part of a job opportunity for an engineering role. The threat actor is said to have masqueraded as a talent acquisition specialist at a major technology company to approach a software engineer and invited them to complete a technical assignment.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

It's worth noting that Nimbus Manticore is also tracked under the moniker [Iranian Dream Job](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html) for its use of recruitment-themed lures to trick prospective targets into infecting their own computers, a tactic long adopted by the North Korea-linked Lazarus Group.

The archive contains source code for a project management tool called Taskflow and instructs candidates to "find and fix all bugs in the frontend code" as part of an "engineering challenge" within three hours and without relying on artificial intelligence (AI)-assisted tools.

The instructions specifically ask the candidates to refrain from modifying the server component of the application ("server.js"), claiming it's "bug-free and functions correctly." However, it's in this file that the malicious code is embedded.

"The first line of server.js imported a trojanized npm package named colorized\_terminal, version 2.1.0," Kaspersky said. "The attackers bundled the package directly in the challenge task archive's node\_modules directory rather than publishing it to the npm registry. When imported, the package silently launched an implant from node\_modules/.cache/.320697f1/index.js as a detached background process."

The implant in question is NodeRabbit, which communicates with one of three Azure-hosted command-and-control (C2) addresses ("plugplay.azurewebsites[.]net," "rgbteller.azurewebsites[.]net," and "wslwebui.azurewebsites[.]net") through three distinct API endpoints -

* /api/rabbit/checkin, to register agent and host information
* /api/rabbit/task, to poll for commands
* /api/rabbit/result, to send task results

The malware supports 11 commands that allows it to gather host details, list running processes, execute arbitrary shell commands, enumerate directories, read a file in chunks and return Base64-encoded data, decode Base64-encoded text and write it at a chosen file offset, delete a file or recursively delete a directory, create directories recursively, enumerate adapters, MAC addresses, IP addresses, and DNS settings, and alter beacon interval.

Another notable capability of NodeRabbit is to write a Base64-encoded Node.js script to a randomly named ".tmp" file, execute it, and then delete it to cover up traces of malicious activity.

Kaspersky said it identified two more variants of NodeRabbit that share the same code lineage, each recovered from Egypt and Ethiopia -

* A second variant that uses a different trojanized npm package named pretty-log (version 2.1.0) instead of colorized\_terminal, while also partially implementing corporate proxy support and terminating if found to be running in an analysis environment
* A third variant that's also launched using the pretty-log npm package but uses a different set of API endpoints to accomplish the same tasks -
  + /sdk/v2/ready
  + /sdk/v2/config
  + /sdk/v2/events

Persistence is achieved depending on the operating system: a Windows Run registry key on Windows, a cron entry for Linux, and a launch agent on macOS. The persistence mechanism mimics either a Microsoft Edge browser...