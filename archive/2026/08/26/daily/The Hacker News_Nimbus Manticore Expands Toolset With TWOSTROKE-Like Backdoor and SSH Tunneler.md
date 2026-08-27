---
title: Nimbus Manticore Expands Toolset With TWOSTROKE-Like Backdoor and SSH Tunneler
url: https://thehackernews.com/2026/08/nimbus-manticore-expands-toolset-with.html
source: The Hacker News
date: 2026-08-26
fetch_date: 2026-08-27T12:14:29.367058
---

# Nimbus Manticore Expands Toolset With TWOSTROKE-Like Backdoor and SSH Tunneler

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

# [Nimbus Manticore Expands Toolset With TWOSTROKE-Like Backdoor and SSH Tunneler](https://thehackernews.com/2026/08/nimbus-manticore-expands-toolset-with.html)

**Ravie Lakshmanan**Aug 26, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWDtkssu1a2OfGXtU3IlV8MARDVh3XpsurXStcVxASTKf_ACkwIhG6XVbR6fqqWFEFcOEOzLWpy1GGKHgTogw1hQL1O5CtLrLweaGx9GLnM-6CXDApf6VcpFzWFe0FaYgPi1TdhOotRrJ9xU39dk4efUJsMejezEs8t0v8oLyafMuVZrzgkeP-AEhls-x8/s1700-e365/nimbus.png)

Cybersecurity researchers have discovered additional infrastructure and previously undocumented malware associated with **[Nimbus Manticore](https://thehackernews.com/2026/07/nimbus-manticore-deploys-nightledger.html)**, an Iranian state-sponsored hacking group affiliated with the Islamic Revolutionary Guard Corps (IRGC).

Group-IB, in a new analysis published today, described the cyber espionage actor as among the most active Iranian APT groups in 2026. Nimbus Manticore (aka GalaxyGato, Mirage Kitten, Screening Serpens, Smoke Sandstorm, Subtle Snail, and UNC1549) is [assessed](https://thehackernews.com/2025/09/unc1549-hacks-34-devices-in-11-telecom.html) to be linked to [Tortoiseshell](https://thehackernews.com/2025/11/iran-linked-hackers-mapped-ship-ais.html) (aka Imperial Kitten and Unyielding Wasp﻿), which is part of the Charming Kitten (aka Eclipsed Wasp﻿) cluster.

Tortoiseshell is known to be active since at least July 2018, mainly targeting defense, aerospace, IT service providers, and military organizations in the Middle East and the U.S. Nimbus Manticore also has a history of [orchestrating](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html) its own version of the Dream Job campaign to deliver malware under the pretext of job opportunity-themed social engineering attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The Singaporean cybersecurity company said it uncovered extensive Tortoiseshell infrastructure spanning Europe and the Middle East, as well as an SSH-based tunneling utility and a C++ backdoor that shares similarities with [TWOSTROKE](https://thehackernews.com/2025/11/iranian-hackers-use-deeproot-and.html), another backdoor already attributed to the threat actor.

"The discovered Tortoiseshell infrastructure potentially suggests an expanded targeting profile, focusing on Middle Eastern countries, alongside European countries," Group-IB researchers Mansour Alhmoud and Mohamed Emam [said](https://www.group-ib.com/blog/tortoiseshell-apt-toolset-infrastructure/).

The findings build upon a recent report from Kaspersky, which [detailed](https://thehackernews.com/2026/07/nimbus-manticore-deploys-nightledger.html) the threat actor's use of a new Windows backdoor called NightLedger and two custom WebSocket tunnelers, BridgeHead and ArcBridge, with an aim to maintain persistent access to compromised hosts in attacks aimed at entities across the Middle East, Africa, and South Asia.

One of the newly discovered artifacts is a reverse SSH tunneling tool that masquerades as the Windows Terminal Server SDK API, while establishing an SSH connection to the operator's infrastructure located at "172.86.98[.]113" on port 443.

The second malware family is a backdoor that overlaps with TWOSTROKE, a C++ implant that allows for system information collection, DLL loading, file manipulation, and persistence. The backdoor mimics the Windows terminal server SDK DLL ("wtsapi32.dll") and uses one of three hard-coded command-and-control (C2) servers to establish an HTTPS connection and await further instructions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Upon receiving a response from the C2 server, it extracts from it the command and creates a new worker thread to execute it. The commands enable the malware to download/upload files, execute a binary or DLL, gather host information, list directories, and delete specific files.

"The identification of infrastructure targeting Middle Eastern and European countries alongside continued development of tools such as the TWOSTROKE backdoor and SSH-based tunneling utilities demonstrates a threat actor that is steadily evolving its toolset and adapting its techniques to maintain access across a growing number of targets," Group-IB said.

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat), [Backdoor](https://thehackernews.com/search/label/Backdoor), [Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [Malware](https://thehackernews.com/search/label/Malware), [Nation-State](https://thehackernews.com/search/label/Nation-State), [network security](https://thehackernews.com/search/label/network%20security), [Social Engineering](https://thehackernews.com/search/label/Social%20Engineering), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [Windows Security](https://thehackernews.com/search/label/Windows%20Security)

⚡ Top...