---
title: Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify, and Other Apps for API Keys
url: https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html
source: The Hacker News
date: 2026-11-16
fetch_date: 2026-11-17T09:57:54.927180
---

# Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify, and Other Apps for API Keys

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify, and Other Apps for API Keys](https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html)

**Swati Khandelwal**Nov 16, 2026Artificial Intelligence / Cyber Attacks

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigoyCtEKcD7TM_5vDkKiZYFdk_l4-js7HNuvMXzZbVqUbEgq1nnD2vEZgZ0kL9CdmOkITC0Rbd-ebTkSX-R4NPKwWZXzUD6zS0g9nEfnlXw3njm3oW2Se97qbT7lIfZEL56X3IIaZAildTni9-zQJu5sa4Lhvi_mVlbTeZFyFtezOMHJ_bDhJWfG7KQ8eh/s1700-nu-rw-lo-l85-e365/amazon.jpg)

Attackers' AI agents have been hunting for weak spots in internet-exposed AI apps such as **LiteLLM**, **One API**, and **Dify** to steal the AI provider keys stored inside, according to the agents' own records.

The records, which Amazon's threat intelligence team captured with decoy servers, describe stolen keys being used to run the AI models that powered the search for more keys.

The team said this week that it cannot verify the outcomes reported by the agents. It has moderate confidence that the agents ran on **ARTEX**, an open-source AI tool for penetration testing.

The records include a playbook of known entry points for each targeted product. It lists default administrator credentials such as LiteLLM's default master key, unfinished installs that an outsider could take over, and known flaws in **Langflow** and **RAGFlow**.

In a separate case reported this week, Cloudflare's incident responders saw ARTEX gain access to a compromised API token that had been used for CI/CD. The token had no IP restrictions or rate limiting, and the activity that followed included 400 database dump requests in an hour. The company has not said whether those requests returned any data.

An operator gives ARTEX a target and a goal, and a planner agent splits the goal into tasks for worker agents that run security tools. To decide each next step, the agents send their work to a large language model (LLM).

The decoy servers, part of a network called **MadPot**, posed as popular LLM services. From October 3 to late last week, the agents sent it requests that often carried a campaign's full history, including the operators' instructions and the agents' reported findings.

Those [captured agent records](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/) describe work done on systems MadPot does not watch. "Amazon Threat Intelligence did not observe that activity as it happened and cannot verify the outcomes the agents reported, but the records show what the actors were pursuing," the team said.

The team assessed, with moderate confidence, that the operators were separate China-linked groups, citing Simplified Chinese prompts and China time zone settings, among other evidence.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

In the main campaign, the agents looked for internet-exposed AI apps, extracted the provider keys stored inside, verified that the keys worked, and added them to a shared pool. They focused on apps that hold keys for many providers, because one weak admin page there can expose many accounts.

Targets named in the records include LLM gateways and proxies such as One API, New API, Veloera, Sub2API and LiteLLM, and AI app builders such as Dify, FastGPT, Langflow, RAGFlow, Open WebUI, LobeChat and Ollama.

The playbook also covers management and provider settings endpoints that need no login, an authentication bypass through the isCliRequest header in One API family systems, and server-side request forgery (SSRF) through URL-fetch features to reach cloud metadata services. Other entries cover secrets left in client-side JavaScript, source maps, debug routes and environment files.

When the agents found cloud credentials, they targeted managed services that host AI models, secret stores, and application identities, prioritizing premium AI models over general cloud access.

To find leaked keys, the agents used internet scanning services and certificate transparency logs, and searched GitHub repositories and event archives, npm and PyPI packages, container image layers, notebooks, model-hosting spaces, paste sites, and Telegram channels.

The records cover hundreds of targets across AI app platforms and other systems. The team notified AWS customers who may have been affected.

Microsoft reported last week that attackers were using agentic AI tools such as ARTEX for [GitHub secret hunting](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/), looking for exposed credentials that included API keys for AI inference.

On August 26, the company described an [earlier RAGFlow attack](https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html), in which a hidden hook captured AI provider keys as users entered them, and a compromise of a LiteLLM gateway that exposed provider keys.

In its [RAGFlow case study](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/), the company had only low confidence about which flaw, if any, let the attackers run code. It did not link those attacks to ARTEX.

The decoy records also describe a second campaign in which agents attempted to bypass identity checks at two cryptocurrency exchanges using deepfakes.

One verification vendor's server rejected the live deepfake video on every attempt the agents made to record it. The team did not say whether the forged photos of ID documents that the agents also fabricated passed document checks.

Over the past eight weeks, Cloudflare's incident responders were called into multiple investigations involving ARTEX and tools built from it.

In more than one incident, an attacker gained access to a customer's environment with a major cloud provider and moved directly into the customer's Cloudfl...