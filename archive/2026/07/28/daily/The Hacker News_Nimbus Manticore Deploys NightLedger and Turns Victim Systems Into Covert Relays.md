---
title: Nimbus Manticore Deploys NightLedger and Turns Victim Systems Into Covert Relays
url: https://thehackernews.com/2026/07/nimbus-manticore-deploys-nightledger.html
source: The Hacker News
date: 2026-07-28
fetch_date: 2026-07-29T05:04:27.296179
---

# Nimbus Manticore Deploys NightLedger and Turns Victim Systems Into Covert Relays

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Nimbus Manticore Deploys NightLedger and Turns Victim Systems Into Covert Relays](https://thehackernews.com/2026/07/nimbus-manticore-deploys-nightledger.html)

**Ravie Lakshmanan**Jul 28, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-Whbx97t7xBrrpM26fYSbwg29hdKR8zskNLIwlrWC0Jd3Rrf4INhiCTI3WMw8NzmJ1iETQlt-CKdUxBzL2hef4pgQBOoI1rrrtRbU96hJRUXtTGy5dT40mP2B1AshyphenhyphenM4mc1K1-IISWwY6PSPyGXNBHplHM8kuxX9e5Di6RmMybyO2Q7Guu__CK8jOOkja/s1700-e365/proxy.jpg)

The Iranian state-backed hacking group tracked as **[Nimbus Manticore](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html)** (aka GalaxyGato, Mirage Kitten, Smoke Sandstorm, Subtle Snail, and UNC1549) has been attributed to a fresh set of attacks targeting entities across the Middle East, Africa, and South Asia.

The intrusions involve the use of a previously undocumented Windows backdoor called NightLedger and two custom WebSocket tunnelers, BridgeHead and ArcBridge, with an aim to maintain covert access.

Targets of the campaign include Egypt, SMB and government environments in Jordan and Tanzania, aviation organizations in Pakistan, telecommunication companies in Ethiopia, and financial-sector entities in Burkina Faso, per Kaspersky.

"The toolset includes NightLedger, a new Windows backdoor for reconnaissance, command execution, file operations, process discovery, and screenshot capture; and two custom WebSocket-based tunnelers, ArcBridge and BridgeHead, for covert network access and operator-controlled tunneling," Kaspersky researchers Omar Amin and Vasily Berdnikov [said](https://securelist.com/mirage-kitten-new-tools/120811/).

The exact initial access method used in the attacks is presently unknown, although the adversary is known to employ highly tailored job opportunity-themed phishing lures masquerading as trusted brands and hiring platforms, as well as lookalike videoconferencing pages, to redirect recipients to malicious archives hosted on third-party file-sharing services.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The as-yet-undetermined access route is then abused to deliver the malicious payloads, including NightLedger, which is launched as a DLL via DLL side-loading. The malware is designed to contact an external server over HTTPS to parse and run commands in a manner that's analogous to [TWOSTROKE](https://thehackernews.com/2025/11/iranian-hackers-use-deeproot-and.html), another backdoor deployed by the threat actor in the past. The list of supported commands is below -

* Gather user and host identity information
* Execute a process/program
* List directories
* Download a file to the infected system
* Collect host and network information
* Copy or delete files
* Update beacon interval
* Take a screenshot
* Load a DLL
* Terminate a process or thread
* Upload file to the command-and-control (C2) server via an HTTP POST request
* Enumerate logical drives
* List processes
* Collect C:\Windows\debug\NetSetup.log (a diagnostic file used for troubleshooting domain join issues) together with process-list output

Two other malware families delivered as part of the attacks are BridgeHead ("unbcl.dll"), a SOCKS5 tunnel proxy observed in environments in Egypt and Pakistan that shares some level of functional overlaps with [MiniFast](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html) (aka MiniUpdate and Retrograde), and ArcBridge, another WebSocket tunneling tool observed in April 2026 in activity targeting victims in the Middle East.

"The C2 server initiates all tunnel connections by sending binary commands over the WebSocket; the implant simply forwards traffic between server-specified targets and the WebSocket channel," the researchers said about BridgeHead. "This makes it a relay node: the operator runs tools server-side, and all resulting TCP traffic is tunneled through the victim's machine as if originating from the victim's network."

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

The use of BridgeHead and ArcBridge indicates the threat actor's continued use of tunneling utilities, which has been previously observed relying on bespoke tunnelers such as [LIGHTRAIL and POLLBLEND](https://thehackernews.com/2025/11/iranian-hackers-use-deeproot-and.html).

The disclosure comes days after Group-IB uncovered a new malware sample codenamed [HOLLOWGRAPH](https://thehackernews.com/2026/07/hollowgraph-malware-hides-c2-and-stolen.html) that's linked to the Cavern (aka Cav3rn) framework used by an Iranian hacking crew dubbed [Cavern Manticore](https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html).

"HOLLOWGRAPH abuses Microsoft Graph API to transform a compromised Microsoft 365 calendar into a covert two-way command-and-control channel," it said.

"Using the Microsoft Graph API, it treats the compromised mailbox's calendar as a two-way dead-drop: operators plant tasking as calendar events, and the implant exfiltrates stolen files by creating its own events with encrypted data attached. To avoid catching the mailbox owner's attention, every event is dated far into the future - 13 May 2050 - with payloads attached as files to the event."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Sha...