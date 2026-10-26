---
title: OpenAI AI Agents Demonstrate VM Escapes and Secret Cross-Sandbox Communication
url: https://thehackernews.com/2026/10/openai-ai-agents-demonstrate-vm-escapes.html
source: The Hacker News
date: 2026-10-25
fetch_date: 2026-10-26T07:19:09.444829
---

# OpenAI AI Agents Demonstrate VM Escapes and Secret Cross-Sandbox Communication

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [OpenAI AI Agents Demonstrate VM Escapes and Secret Cross-Sandbox Communication](https://thehackernews.com/2026/10/openai-ai-agents-demonstrate-vm-escapes.html)

**Ravie Lakshmanan**Oct 25, 2026Artificial Intelligence / Cybersecurity

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSwuCxStjU_WIIOJ5dEqVxFVQeLfJevQdmLoYLBiXsduAvosK7VfzyduIRRmiOcpl2lQlSdEoInwRkfOnR4devMGT6oI_Limrjcx8yLFsTRau7CBK76cGIMXxC916OKHtwALlELG-nPljBDVIPl2aPDOZTYqkTr6AyZMyFQ6hwUFdfx5Tr2cz8KpDSlb9j/s1700-nu-rw-lo-l85-e365/ai-agents.jpg)

OpenAI has announced plans to conduct frontier model training with no live internet access, as it resumes reinforcement learning (RL) training and internal inference of its most advanced AI models.

"Based on the current state of alignment research, monitoring systems, and the security of internet infrastructure, we believe the responsible approach is to conduct frontier model training with no internet access," the artificial intelligence (AI) company [said](https://openai.com/index/securing-our-frontier-model-training-environment/). "We've implemented this policy and will maintain it until advances in these safeguards justify broader internet access."

OpenAI said models' growing capabilities can have the side effect of them getting much better at devising ways around environmental restrictions to escape containment and perform unintended actions. This can involve the model exploiting a software flaw or misconfiguration to reach the live internet, or finding unauthorized ways to communicate with agents in other sandboxes.

Late last month, the frontier lab made the decision to [pause training](https://thehackernews.com/2026/09/openai-pauses-tool-use-after-agent.html) of its most powerful models after one of its agents during reinforcement learning (RL) training contacted an external chatbot by exploiting a misconfiguration in a DNS resolver to obtain limited internet access.

OpenAI said it also kicked off a "high-compute red-teaming campaign" to test the resilience of its research and evaluation environments in the face of increasingly powerful models, leading to the discovery of previously unknown software vulnerabilities, including a critical [unauthenticated remote code execution](https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html) in Google Brotli ([CVE-2026-111497](https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html), CVSS score: 9.2), a widely used compression library.

Patches for the [vulnerability](https://patchtheplanet.org/brotli), also called [Node2Shell and HTTP2Shell](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497), have since been released for libbrotli, Python, C++, Node.js, Bun, Envoy, and Istio.

The red-teaming agents OpenAI dispatched to test its security safeguards also uncovered virtual machine escapes, novel paths to access the internet through vulnerabilities in metrics, logging, and authentication management services, and hardware side-channels for communication between agents, bypassing isolation boundaries.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

"In one test that assumed compromise of a host machine, an agent reused a firewall-approved connection to reach a blocked authentication endpoint in our metrics service and then made that endpoint fetch a model-provided URL," it said. "In other tests, agents exploited misconfigurations that allowed blocked requests to pass through DNS and firewall controls, as well as ways to make services we run fetch external URLs."

In another experiment, after prompting the AI agents in separate microVMs to exchange synthetic secrets without relying on network connections or shared writable files, OpenAI said the digital bots found a way to communicate using the processor's cache via a timing-based side-channel.

Particularly, one agent is said to have encoded information by evicting selected data from the cache. A second agent measured the time it took to reload that data, leveraging the difference between fast and slow cache reads to recover the message.

"Once the agents agreed on a protocol for encoding and decoding these signals, they could exchange the synthetic secrets without changing a shared file or opening a network connection," OpenAI said.

The AI giant said the discoveries prompted it to strengthen its own safety and monitoring mechanisms, deeming the enhanced controls sufficient enough to restart frontier RL training and internal inference while continuing to invest in several key areas -

* Improving virtual machine security
* Probing cloud infrastructure for weaknesses
* Scanning source code and cloud configurations
* Testing monitoring and stopping systems
* Red-teaming sandbox and isolation guarantees

"After strengthening our containment architecture, we resumed our frontier RL training and inference on October 1," OpenAI [said](https://x.com/OpenAI/status/2113718797505036665). "We've reserved substantial compute for continuous red-teaming, and made high-compute red-teaming part of the safety cases we use to decide whether frontier training and evaluation can proceed securely."

Earlier this month, Anthropic said it was [cutting off live internet access](https://thehackernews.com/2026/10/anthropic-cuts-live-internet-access-for.html) for all its internal evaluations until further notice after discovering new incidents in which its AI models exhibited misaligned behavior and targeted real websites.

The disclosure comes as concerns have been raised over the ability of AI agents to detect and exploit software flaws, even in the guardrails designed to restrict them.

In a report published this week, third-party AI ​safety evaluators METR ⁠and Redwood Research said they found several new vulnerabilities in OpenAI's internal misalignment monitoring system as it existed before July 21, 2026, and during the time frame when the...