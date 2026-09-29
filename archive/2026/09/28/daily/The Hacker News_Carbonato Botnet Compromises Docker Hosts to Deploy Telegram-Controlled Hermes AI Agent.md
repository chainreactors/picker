---
title: Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent
url: https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html
source: The Hacker News
date: 2026-09-28
fetch_date: 2026-09-29T07:41:37.325775
---

# Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent

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

# [Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent](https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html)

**Ravie Lakshmanan**Sep 28, 2026Malware / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3O4ih8J3-A5sGh57xyYKMGbnSqaXbWhu2g9HBE_mG11gEdedMUmYyeeYpA9TnNPwRsB4t-5V9UTW54iOR0VNzyaaa0fWhOG4Oi46KwGvrrVQRdWIDS7GX6YxjaMrA6sF9RHWNyO8gBttCQ7Nc8LUmrhhH24jSp1lPDuhok9r3CfKxgGJRObZRqRTW-5Gf/s1700-nu-rw-lo-l85-e365/hermes-telegram.jpg)

Cybersecurity researchers have disclosed details of a new botnet malware called **Carbonato** that's targeting exposed Docker daemons to deploy an open-source artificial intelligence (AI) agent framework called [Hermes Agent](https://hermes-agent.nousresearch.com/).

"The implant installs the framework unchanged, then overwrites its SOUL.md persona file," ThreatDown [said](https://www.threatdown.com/blog/carbonato/). "The 39-line prompt directs it to execute tasks received through Telegram, maintain persistence, and collect credentials."

At a high level, the botnet breaks into Docker daemons exposed without authentication on port 2375 and scans neighboring networks every five minutes to propagate further. On each host, it installs Hermes Agent with instructions to follow operators' Telegram commands.

The cybersecurity company said it found the operation through an unauthenticated Docker registry that's been publicly accessible since May 2026. The staged data has been found to include details of the botnet and a separate campaign that distributed trojanized cryptocurrency wallet apps.

CARBONATO possesses worm-like capabilities in that it can spread to other hosts with unauthenticated Docker daemons. Once a host is discovered, it launches a privileged container and run commands on the underlying system.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"It uses a privileged​ ​container​ ​to​ ​run​ ​commands​ ​on​ ​each​ ​host,​ ​establishes​ ​persistence and remote access, then scans nearby networks for further Docker daemons," ThreatDown said. "Hermes​​ Agent​​ gives ​​the​ ​operators​​ a​​ Telegram​​ interface ​​to ​​send ​​tasks ​​to ​​compromised​​ hosts,​​ and​​ its persona names AI API keys and other credentials as the priority."

All of this is achieved by means of a shell script that launches a reverse SSH tunnel​​ from the victim to a relay located in Costa Rica, after which it installs an SSH server with the operators' key and reports the new deployment through Telegram with the container details.

The malware also takes steps to evade detection by masquerading as a system component and establishes persistence using cron jobs and watchdog scripts that ensure the implant is re-launched if the malicious artifacts are removed.

With the persistence set up, the next step involves deploying the Hermes Agent and overwriting its SOUL.md persona file with a custom prompt that asks the AI tool to assume the role of a "senior hacker, pentester, and exploit developer" named GH0ST and instructs it to "maintain persistence, respond over Telegram, and execute any operation the operator asks" without "moral or ethical restrictions."

The agent then enters into an interactive command loop that interprets incoming tasks through Telegram and forwards them to the appropriate large language model (LLM) gateway. The model then writes the terminal commands that are executed by the agent and returns the results back to the threat actor over the messaging platform.

The activity has not been attributed to any known threat actor or group. Language, timezone, and infrastructure clues indicate that the operators are based in Costa Rica.

### Rising Attack-Chain Automation

The disclosure comes amid growing threat actor use of AI tools and models to automate various aspects of the cyber attack lifecycle and offload offensive work.

In July 2026, Palo Alto Networks [linked](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) a China-based threat actor dubbed "knaithe" and "KnYuan" to an AI-enabled hacking campaign that leveraged DeepSeek, via the Hermes Agent framework configured to accept instructions over Telegram, to enumerate targets, source exploit tools, and launch attacks without human intervention.

That same month, Hunt.io also [highlighted](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) another operation in which attackers used Hermes Agent in unattended "YOLO" mode to target Thailand's Ministry of Finance (MOF), ultimately breaching multiple systems within the network.

"The combination is what stands apart: an AI agent coordinating the work, a cross-platform implant holding access, and scripts written for this specific target," Hunt.io said. "Together they describe an operator who invested significant preparation into penetrating a single government target."

As recently as last week, Gambit Security said it identified a Chinese-speaking financially motivated operator running three open-source AI harnesses against hundreds of online retailers, compromising at least 27 companies, stealing over 600,000 credit card details from two entities, and injecting skimmer scripts into five online stores.

The activity, which has been ongoing since July 2026, uses AI at all stages of the attack, with results of one informing the next -

* Strix, an AI penetration testing tool for vulnerability hunting
* Cairn, an autonomous penetration testing engine for autonomous end-to-end exploitation by launching 105 attack projects between September 10 and 15, 2026, using DeepSeek v4.1 Flash
* Hermes, for orchestration, post-exploitation, tactical guidance, and directing the malicious activity using Anthropic Claude Opus 4.6

The threat actor is said to have loaded the Chinese system persona titled "SOUL - Red Team Operator" onto Hermes Agent and carr...