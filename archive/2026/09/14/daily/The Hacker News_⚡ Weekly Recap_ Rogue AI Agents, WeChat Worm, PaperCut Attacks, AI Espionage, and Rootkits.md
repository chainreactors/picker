---
title: ⚡ Weekly Recap: Rogue AI Agents, WeChat Worm, PaperCut Attacks, AI Espionage, and Rootkits
url: https://thehackernews.com/2026/09/weekly-recap-rogue-ai-agents-wechat.html
source: The Hacker News
date: 2026-09-14
fetch_date: 2026-09-15T07:03:16.034226
---

# ⚡ Weekly Recap: Rogue AI Agents, WeChat Worm, PaperCut Attacks, AI Espionage, and Rootkits

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

# [⚡ Weekly Recap: Rogue AI Agents, WeChat Worm, PaperCut Attacks, AI Espionage, and Rootkits](https://thehackernews.com/2026/09/weekly-recap-rogue-ai-agents-wechat.html)

**Ravie Lakshmanan**Sep 14, 2026Cybersecurity / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgubijVX34VFFHDXzT2j2iTTWrHaElVXjylLKHKAjeSU59q3jTZvRM_O35zw5QOCnrT8ejrYHTG-kjYyt0-R127H_2qEgIWJNuKynEL1FcM9JLyPbsJPY5OZW9rrkJpRprrxpWP8oAGZA2ARZ3xg_0DvBw1I2wbIoXKItcVEjNXQH-CXCMRyuqp1u53ALj7/s1700-nu-rw-lo-l85-e365/recap-cyber.jpg)

AI keeps showing up in the wrong places. Attackers are using it to speed up exploits, test defenses, and automate more of the job. Some models are also crossing lines on their own. That is not a great combination.

The rest of the week is more familiar: old bugs still working, fresh exploit chains, exposed systems, weak defaults, and simple paths that should have been harder to abuse. A few of these stories are clever. Most are just easy.

Here’s what mattered this week.

## **⚡ Threat of the Week**

**[OpenAI Agents Behind May 2026 Attack on RubyGems](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html)** — The "major malicious attack" that targeted RubyGems in May 2026 was the work of a swarm of OpenAI agents, according to researchers. The event was driven by a cluster of OpenAI agents that engaged in en masse publication of thousands of packages to RubyGems in May and June 2026. "The swarm behaves extremely similarly to the German-wiki agents we previously found," researchers Spencer Kitts, Thomas Larsen, and Sydney Von Arx said. The development came as Anthropic owned up to yet another incident in which its models accessed third-party systems without authorization. The new AI trespass dates back to January 2026. It involved an early version of Claude Opus 4.6 that was given a Capture the Flag (CTF) challenge. "The model discovered a machine belonging to a third party that it was able to access, and stated that it believed this third party was part of the CTF," it [said](https://thehackernews.com/2026/09/anthropic-ai-models-breached-real.html). "Inside the machine, the model found a file listing a password, which it used to gain admin access to the system." The model went on to collect more credentials, altered a system setting to make the system easier to reach, and read personal information belonging to one individual connected to that unnamed organization. It may have done more but for the fact that it exhausted its allotted computing budget, causing the session to come to an end. Many incidents involving agents from frontier AI labs acting against their programming to escape restrictions in pursuit of their goals have heightened concerns over the increasing capacity of AI models and developers' ability to contain them. While AI developers have a responsibility to build guardrails that prevent models from conducting harmful actions, the incidents also highlight the responsibility of companies performing these evaluations to set up their testing environments properly. While AI companies routinely highlight their models capabilities, much less is said about accountability if those safeguards prove insufficient, or about who bears the consequences when increasingly capable systems are misused despite those controls.

[![OAuth and MCP Investigation Checklist](data:image/png;base64... "OAuth and MCP Investigation Checklist")

## OAuth & MCP Investigation Checklist: 4 Steps to Assess Risk

OAuth grants enable data sharing across apps, AI tools, and MCP servers, and most go unreviewed. Learn four steps for finding risky grants and closing the gaps before they turn into a security incident.](https://thehackernews.uk/oauth-investigate)
[Get the Guide ➝](https://thehackernews.uk/oauth-investigate)

## **🔔 Top News**

* **[Anthropic and Google Detail Abuse of AI](https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html)** — Threat actors are [increasingly integrating](https://thehackernews.com/2026/09/claude-used-to-automate-exploitation.html) AI capabilities into multiple stages of an attack lifecycle with an aim to automate and scale their operations. "Over the past quarter, threat actors have moved beyond simple prompt-based LLM interactions to integrate AI capabilities into multiple stages of an attack lifecycle," Google Threat Intelligence Group (GTIG) said. "While traditional script-based automation has long been a staple of threat actor operations, groups are increasingly upgrading these workflows, creating highly autonomous systems capable of reasoning through complex tasks and making dynamic decisions without the need for human oversight." GTIG said it "has not yet observed threat actors deploying fully autonomous pipelines against targets in the wild," with the adversarial adoption of agentic AI signaling "a gradual maturation of tradecraft," as adversaries employ commercial and open-weight models to turn public disclosures and patch delays into working N-day exploit code, refining their tooling, and progressing "toward constructing functional, multi-stage exploit chains."
* **[Threat Actors Exploit New Vulnerability Chain](https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html)** — Multiple espionage-motivated threat activity clusters have been found deploying a previously undocumented exploit kit called BlueMoon that chains together multiple vulnerabilities in Microsoft Windows and Google Chrome. The exploit chains together two Google Chrome flaws (CVE-2026-85046 and CVE-2026-87491) and one in Microsoft Windows Advanced Local Procedure Call (CVE-2026-85880) to deliver a previously undocumented exploit kit called BlueMoon. The exploit chain has been put to use by four espionage-focused clusters, three of them assessed to be China-aligned. Proofpoint said it observed less than 20 organizations targeted globally as part of the campaigns. The episode fits a recurring pattern in which...