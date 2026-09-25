---
title: ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories
url: https://thehackernews.com/2026/09/threatsday-ai-search-poisoning-ai.html
source: The Hacker News
date: 2026-09-24
fetch_date: 2026-09-25T06:53:33.640078
---

# ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories

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

# [ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories](https://thehackernews.com/2026/09/threatsday-ai-search-poisoning-ai.html)

**Ravie Lakshmanan**Sep 24, 2026Hacking News / Cybersecurity News

[![The Hacker News](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQeh1uEFjgxcgPPJkrXkAnJxZRxA9_ZolFQXNONWmfMGLViusszn4KTiJ9-8_r-AV94NS5BQlZ5eOrFnTvinPXcJB_G4o_BEZdv7xXMdAqfvZPfiUzKjlE70q2V6C9ze8H58pqYh-suKm_Yu1q3LoevignMd7nfjbjV7qx_vEad6BEFKUHwV5UlTFW1-dh/s1700-nu-rw-lo-l85-e365/threatsday-sep.jpg)

This week, the dangerous stuff keeps arriving dressed as something boring. An update. A login box. A search answer. A coding tool. A link you have clicked a hundred times before.

That is the thread running through the pile. Trusted paths get poisoned. Old bugs find new jobs. AI tools leak more than expected. Fake prompts look real enough. And some attacks barely need an exploit at all — just one weak setting or one person doing what the screen tells them.

Nothing here looks especially dramatic. That is what makes it useful.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. AI-Assisted Banking Trojan

   [RemControl Android Banking Trojan Targets Western Europe, the Middle East, and Canada](https://www.group-ib.com/blog/remcontrol-android-banking-trojan/)

   A previously undocumented Android banking trojan dubbed RemControl is targeting retail banking customers across Western Europe (Italy, France, Spain, Poland, Portugal), the Middle East, and Canada. The malware is distributed via fake Google Play Store pages impersonating the TVTap IPTV application. Users are directed to the web page through Meta ads. It was first observed in July 2026. "The malware abuses Android's Accessibility Service to inject phishing overlays over legitimate banking applications, stream the device screen in real time, log keystrokes, and provide the operator with full remote control over infected devices," Group-IB [said](https://www.group-ib.com/blog/remcontrol-android-banking-trojan/). "C2 address is resolved dynamically through an encrypted Telegram dead-drop, making infrastructure rotation straightforward without recompiling the malware. Both the operator panel documentation and phishing overlays contain artifacts of AI-assisted development, including a complete AI assistant response left verbatim in a live phishing page served to banking victims." The presence of Russian-language code comments in multiple overlay HTML files indicates the involvement of a Russian speaker. Overlapping campaign naming conventions, delivery mechanisms, the use of Telegram dead-drop and affiliate tag similarities suggest a possible link to the Medusa UNKN affiliate botnet.
2. AI Code Privacy Concern

   [Z.ai Disables ZCode Features](https://x.com/zcode_ai/status/2101844704933621971)

   Chinese artificial intelligence company Z.ai has disabled several features of its ZCode coding assistant after a default setting was caught sending users' local code repositories to Alibaba Cloud servers in China without their consent, a couple of months after SpaceXAI's Grok Build coding CLI was found uploading entire Git repositories to a Google Cloud Storage bucket under its control. Although Z.ai has since [disabled the workflow](https://x.com/zcode_ai/status/2101844704933621971) responsible for generating and uploading local repository snapshots in its ZCode client and [opened up its codebase](https://github.com/zai-org/ZCode) for public scrutiny, the development raises fresh concerns for enterprises over how AI tools handle sensitive source code.
3. Critical Infrastructure Access Risk

   [CISA and FBI Publish Factsheet for Critical Infrastructure Operators](https://www.cisa.gov/resources-tools/resources/considerations-critical-infrastructure-operators-working-third-party-ics-integrators)

   The U.S. Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) have [published](https://www.cisa.gov/resources-tools/resources/considerations-critical-infrastructure-operators-working-third-party-ics-integrators) a fact sheet to "highlight considerations for critical infrastructure entities to reduce risk and minimize vulnerabilities when working with third-party industrial control system (ICS) integrators." The alert urges critical infrastructure owners and operators to maintain caution when granting third-party ICS integrators high levels of access or control over industrial processes and ensure the principle of least privilege (PoLP) is applied. "Not adopting principles such as PoLP could expose owners and operators to malicious cyber actors seeking to compromise critical infrastructure, possibly providing sensitive access to pathways that actors can exploit to cause disruptive and destructive effects to equipment and critical functions," the authoring agencies said.
4. Super-App Surveillance Capabilities

   [Russia's MAX App's Capabilities Detailed](https://arxiv.org/abs/2609.11814)

   MAX is a state-backed Russian mobile "super-app" developed by VK (aka VKontakte) that combines instant messaging, e-commerce, banking, and public government services. A [new forensic research](https://arxiv.org/abs/2609.11814) published by a group of researchers from the University of Michigan, University of Calgary, Georgia Institute of Technology, and Indian Institute of Technology, Delhi, has [revealed](https://www.theguardian.com/world/2026/sep/18/russian-super-app-max-spy-citizens) the extent of its surveillance capabilities: "Playing the role of an active adversary, we found five distinct capabilities that allow MAX to act as a man-in-the-middle for all mini-app interactions: (1) MAX can capture screenshots of mini-app content without holding any special system permissions, and without alerting the user; (2) It holds full read and write access to all mini-app lo...