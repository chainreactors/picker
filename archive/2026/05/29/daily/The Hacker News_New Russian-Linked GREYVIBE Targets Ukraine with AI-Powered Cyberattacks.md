---
title: New Russian-Linked GREYVIBE Targets Ukraine with AI-Powered Cyberattacks
url: https://thehackernews.com/2026/05/new-russian-linked-greyvibe-targets.html
source: The Hacker News
date: 2026-05-29
fetch_date: 2026-05-30T05:44:31.508650
---

# New Russian-Linked GREYVIBE Targets Ukraine with AI-Powered Cyberattacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [New Russian-Linked GREYVIBE Targets Ukraine with AI-Powered Cyberattacks](https://thehackernews.com/2026/05/new-russian-linked-greyvibe-targets.html)

**Ravie Lakshmanan**May 29, 2026Cyber Espionage / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzJ8u1-LKZwf1FFeVF2K2D2pupLFnsW_zsTumbLXt6eRSNY5NYPuBVxyacqbH-WZRBmTpGmnB0pulEcGex16O8u6812DC7RjtV5fBtVmRG55MdKOdmX2B5m1AtcgfZLCGnH_wNVxrdpfvRR70-MjsT7fzuS8wasEGhnDKmavU02xE6HjMg6FLpv3dvSFi7/s1700-e365/russia-ai-cyberattacks.jpg)

A previously undocumented threat actor dubbed **GREYVIBE** has been attributed to ongoing and persistent attacks targeting Ukraine and Ukraine-related entities since at least August 2025.

GREYVIBE, per WithSecure, is assessed to be a Russian-speaking group operating broadly in the Russian time zone, with the activities aligning with Kremlin state interests, specifically when it comes to intelligence gathering efforts aimed at Ukraine in the context of the ongoing Russo-Ukrainian war.

"The group has leveraged multiple attack vectors, including spear-phishing e-mails, fake captcha pages, and fraudulent Ukrainian adult club websites, to deliver malware to a diverse set of victims," WithSecure researcher Mohammad Kazem Hassan Nejad [said](https://labs.withsecure.com/publications/greyvibe) in an analysis. "Across these campaigns, the group has relied on custom-developed obfuscators, loaders, and malware."

The victimology footprint spans military, government, civilian, and business-related organizations. GREYVIBE, its nation-state-affiliated activity notwithstanding, also shares ties to the broader Russian cybercrime ecosystem through some of its members who are believed to be current or former cybercriminal actors.

In addition, there is evidence indicating that the adversary is relying on generative artificial intelligence (GenAI) and large language models (LLMs) to supercharge its operations. Taken together, WithSecure paints the picture of a "low-to-moderately sophisticated group" that suffers from operational security blunders and employs AI-assisted tooling to augment its malware development efforts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

GREYVIBE has been observed using multiple attack chains against its targets -

* **PhantomMail**, which uses spear-phishing emails to distribute links pointing to malicious ZIP or RAR archives hosted on Google Drive and 4sync that contain JavaScript-based loaders to launch a decoy document, and PhantomRelay, a PowerShell-based remote access trojan (RAT) designed to profile the host and run PowerShell scripts and Windows commands.
* **PhantomClick**, which uses [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)-style fake CAPTCHA pages on bogus domains masquerading as Zoom and LAPAS to trick users into running commands that initiate a PhantomRelay infection chain.
* **PrincessClub**, which uses fake Ukrainian adult-club websites to deliver FallSpy on Android and PhantomRelayV1 or LegionRelay on Windows, with subsequent iterations of the lure sites introducing a WebRTC-based live call feature to capture victim audio and video. While FallSpy is an Android spyware capable of harvesting sensitive data from the compromised device, LegionRelay is a lightweight PowerShell-based RAT that supports file enumeration, file exfiltration, screenshot capture, browser data theft, Telegram and WhatsApp data exfiltration, and RDP access setup. PhantomRelayV1 is a variant of PhantomRelay with a custom watchdog persistence mechanism.
* **DroneLink**, which uses websites masquerading as charitable foundations supporting the Armed Forces of Ukraine to deliver WireGuard and LegionRelay.
* **Nebo**, which uses a FallSpy sample that mimics a Russian-language login screen, likely in an attempt to deceive Ukrainian military personnel into thinking they were accessing a Russian military terminal.

The variety of delivery vectors and tools used in the attacks likely stems from the use of AI platforms, including Ideogram AI, OpenAI ChatGPT, and Google Gemini, to assist with generating images and developing LegionRelay, as well as obfuscation and loader scripts, backend infrastructure, and post-compromise commands.

The cybersecurity company said GREYVIBE's usage of AI serves multiple advantages, including bridging gaps in technical expertise, accelerating the development lifecycle, and reducing reliance on previously known malware or tools that could aid in attribution efforts.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtgAVMkOZZET8-seqrDnl7vK_gjtnzDzyyNqYoA-GPsTZOZuS8EhNaG4NJ1rvGCrhBMTi25DDvmysQ0dwuWa_j3WD_JzDHafmNDZnGtu1v54lsoWouag5dUXGl3BausbJQsmBv9HAKgDcuyAN1Mk0U32lZlMeVu7_zTyxKgPYolUry8LwM-DNEH1azVJSR/s1700-e365/captcha.png)

"If an actor can frequently generate, refactor, or replace components of its operational footprint with AI assistance, traditional clustering methods based on stable technical artifacts may become less reliable over time," Nejad said.

That said, the use of AI has also had the side effect of introducing design flaws into LegionRelay, exposing the malware's backend functionality. This is another sign suggesting GREYVIBE may not be a pure nation-state actor, as sophisticated adversaries are unlikely to make such mistakes.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The hacking group's links to the cybercriminal ecosystem are based on multiple factors -

* Possible access to and use of an ISO builder with suspected ties to the TrickBot gang and [UAC-0098](https://thehackernews.com/2022/09/some-members-of-conti-group-targeting.html)
* Presence of PhantomRelay variants across seemingly unrelated cybercrime activity clusters, such as a [Microsoft](https://fieldeffect.com/blog/quick-you-need-assistance) Teams [voice](https://thehackernews.com/2025/07/hack...