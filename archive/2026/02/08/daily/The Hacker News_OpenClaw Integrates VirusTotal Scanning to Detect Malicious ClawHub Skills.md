---
title: OpenClaw Integrates VirusTotal Scanning to Detect Malicious ClawHub Skills
url: https://thehackernews.com/2026/02/openclaw-integrates-virustotal-scanning.html
source: The Hacker News
date: 2026-02-08
fetch_date: 2026-02-09T04:18:50.914174
---

# OpenClaw Integrates VirusTotal Scanning to Detect Malicious ClawHub Skills

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [OpenClaw Integrates VirusTotal Scanning to Detect Malicious ClawHub Skills](https://thehackernews.com/2026/02/openclaw-integrates-virustotal-scanning.html)

**Ravie Lakshmanan**Feb 08, 2026Artificial Intelligence / Vulnerability

[![Malicious ClawHub Skills](data:image/png;base64... "Malicious ClawHub Skills")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFUWaEYK5yvPD9ZZdP6cMRMXduyDlAE77-447kgI9rd6ASyC1rDEnZKMIvcbYLsEs1vaXIH6lXLOjMF-JktVNvjhfPy1_5YmWcXXoXQagMLUW5uuXy8gFMyxgEK9ZA4ve51Q95p_9gi5EJpq-IISmuSFkEX1hfuK1CNiXS1Bqf_GZbjE8r80ZN_JJkyq_r/s1700-e365/openclaw-virustotal.jpg)

OpenClaw (formerly Moltbot and Clawdbot) has [announced](https://openclaw.ai/blog/virustotal-partnership) that it's partnering with Google-owned VirusTotal to scan skills that are being uploaded to ClawHub, its skill marketplace, as part of broader efforts to bolster the security of the agentic ecosystem.

"All skills published to ClawHub are now scanned using VirusTotal's threat intelligence, including their new Code Insight capability," OpenClaw's founder Peter Steinberger, along with Jamieson O'Reilly and Bernardo Quintero said. "This provides an additional layer of security for the OpenClaw community."

The process essentially entails creating a unique SHA-256 hash for every skill and cross checking it against VirusTotal's database for a match. If it's not found, the skill bundle is uploaded to the malware scanning tool for further analysis using [VirusTotal Code Insight](https://blog.virustotal.com/2023/04/introducing-virustotal-code-insight.html).

Skills that have a "benign" Code Insight verdict are automatically approved by ClawHub, while those marked suspicious are flagged with a warning. Any skill that's deemed malicious is blocked from download. OpenClaw also said all active skills are re-scanned on a daily basis to detect scenarios where a previously clean skill becomes malicious.

That said, OpenClaw maintainers also cautioned that VirusTotal scanning is "not a silver bullet" and that there is a possibility that some malicious skills that use a cleverly concealed prompt injection payload may slip through the cracks.

In addition to the VirusTotal partnership, the platform is [expected](https://trust.openclaw.ai/) to publish a comprehensive threat model, public security roadmap, formal security reporting process, as well as details about the security audit of its entire codebase.

The development comes in the aftermath of [reports](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html) that found [hundreds](https://www.bitdefender.com/en-us/blog/labs/helpful-skills-or-hidden-payloads-bitdefender-labs-dives-deep-into-the-openclaw-malicious-skill-trap) of [malicious skills](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare) on [ClawHub](https://blog.virustotal.com/2026/02/from-automation-to-infection-how.html), prompting OpenClaw to add a reporting option that allows signed-in users to flag a suspicious skill. Multiple analyses have uncovered that these skills masquerade as legitimate tools, but, under the hood, they harbor malicious functionality to exfiltrate data, inject backdoors for remote access, or install stealer malware.

"AI agents with system access can become covert data-leak channels that bypass traditional data loss prevention, proxies, and endpoint monitoring," Cisco noted last week. "Second, models can also become an execution orchestrator, wherein the prompt itself becomes the instruction and is difficult to catch using traditional security tooling."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The recent viral popularity of OpenClaw, the open-source agentic artificial intelligence (AI) assistant, and [Moltbook](https://www.moltbook.com/), an adjacent social network where autonomous AI agents built atop OpenClaw interact with each other in a Reddit-style platform, has [raised security concerns](https://www.hiddenlayer.com/research/the-lethal-trifecta-and-how-to-defend-against-it).

While OpenClaw functions as an automation engine to trigger workflows, interact with online services, and operate across devices, the entrenched access given to skills, coupled with the fact that they can process data from untrusted sources, can open the door to risks like malware and prompt injection.

In other words, the integrations, while convenient, significantly broaden the attack surface and expand the set of untrusted inputs the agent consumes, turning it into an "[agentic trojan horse](https://noma.security/blog/moltbot-the-agentic-trojan-horse/)" for data exfiltration and other malicious actions. Backslash Security has [described](https://www.backslash.security/blog/clawdbot-moltbot-not-just-another-ai-assistant-but-ai-with-hands) OpenClaw as an "AI With Hands."

"Unlike traditional software that does exactly what code tells it to do, AI agents interpret natural language and make decisions about actions," OpenClaw noted. "They blur the boundary between user intent and machine execution. They can be manipulated through language itself."

OpenClaw also acknowledged that the power wielded by skills – which are used to extend the capabilities of an AI agent, such as controlling smart home devices to managing finances – can be abused by bad actors, who can leverage the agent's access to tools and data to exfiltrate sensitive information, execute unauthorized commands, send messages on the victim's behalf, and even download and run additional payloads without their knowledge or consent.

What's more, with OpenClaw being increasingly deployed on employee endpoints without formal IT or security approval, the elevated privileges of these agents can further enable shell access, data movement, and network connectivity outside standard security controls, creating a new class of [Shadow AI risk](https://www.varonis.com/blog/shadow-ai) for enterprises.

"OpenClaw and tools like it will show up in your organization whether you approve them or no...