---
title: Researchers Find 175,000 Publicly Exposed Ollama AI Servers Across 130 Countries
url: https://thehackernews.com/2026/01/researchers-find-175000-publicly.html
source: The Hacker News
date: 2026-01-29
fetch_date: 2026-01-30T04:04:26.718008
---

# Researchers Find 175,000 Publicly Exposed Ollama AI Servers Across 130 Countries

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

# [Researchers Find 175,000 Publicly Exposed Ollama AI Servers Across 130 Countries](https://thehackernews.com/2026/01/researchers-find-175000-publicly.html)

**Ravie Lakshmanan**Jan 29, 2026Artificial Intelligence / LLM Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpmx-gYMpMW-nf6wXdiwU6bhhuySnvXQo3BifYIaLE8Vi7Verinm69xkQ4B2AWSXdkdU6yA0WjLVtNGvxx_QzRyxEDKxbpqil2P3NZzOQrFf_MihjJeRVJ64VrWW9IAW9eaxmay2BeiTCHKIestdHmy3KpDagP53nnYQkV4z2TsKoCa_m-gk7BCTue_CKE/s1700-e365/Ollama.jpg)

A new joint investigation by SentinelOne SentinelLABS, and Censys has revealed that the open-source artificial intelligence (AI) deployment has created a vast "unmanaged, publicly accessible layer of AI compute infrastructure" that spans 175,000 unique Ollama hosts across 130 countries.

These systems, which span both cloud and residential networks across the world, operate outside the guardrails and monitoring systems that platform providers implement by default, the company said. The vast majority of the exposures are located in China, accounting for a little over 30%. The countries with the most infrastructure footprint include the U.S., Germany, France, South Korea, India, Russia, Singapore, Brazil, and the U.K.

"Nearly half of observed hosts are configured with tool-calling capabilities that enable them to execute code, access APIs, and interact with external systems, demonstrating the increasing implementation of LLMs into larger system processes," researchers Gabriel Bernadett-Shapiro and Silas Cutler [added](https://www.sentinelone.com/labs/silent-brothers-ollama-hosts-form-anonymous-ai-network-beyond-platform-guardrails/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Ollama is an open-source framework that allows users to easily download, run, and manage large language models (LLMs) locally on Windows, macOS, and Linux. While the service binds to the localhost address at 127.0.0[.]1:11434 by default, it's possible to expose it to the public internet by means of a trivial change: configuring it to bind to 0.0.0[.]0 or a public interface.

The fact that Ollama, like the recently popular [Moltbot](https://thehackernews.com/2026/01/fake-moltbot-ai-coding-assistant-on-vs.html) (formerly Clawdbot), is hosted locally and operates outside of the enterprise security perimeter, poses new security concerns. This, in turn, necessitates new approaches to distinguish between managed and unmanaged AI compute, the researchers said.

Of the observed hosts, more than 48% advertise tool-calling capabilities via their API endpoints that, when queried, return metadata highlighting the functionalities they support. Tool calling (or function calling) is a capability that allows LLMs to interact with external systems, APIs, and databases, enabling them to augment their capabilities or retrieve real-time data.

"Tool-calling capabilities fundamentally alter the threat model. A text-generation endpoint can produce harmful content, but a tool-enabled endpoint can execute privileged operations," the researchers noted. "When combined with insufficient authentication and network exposure, this creates what we assess to be the highest-severity risk in the ecosystem."

The analysis has also identified hosts supporting various modalities that go beyond text, including reasoning and vision capabilities, with 201 hosts running uncensored prompt templates that remove safety guardrails.

The exposed nature of these systems means they could be susceptible to [LLMjacking](https://thehackernews.com/2025/01/microsoft-sues-hacking-group-exploiting.html), where a victim's LLM infrastructure resources are abused by bad actors to their advantage, while the victim foots the bill. These could range from generating spam emails and disinformation campaigns to cryptocurrency mining and even reselling access to other criminal groups.

The risk is not theoretical. According to a report published by Pillar Security this week, threat actors are actively targeting exposed LLM service endpoints to monetize access to the AI infrastructure as part of an LLMjacking campaign [dubbed](https://www.pillar.security/resources/operation-bizarre-bazaar) Operation Bizarre Bazaar.

The findings point to a criminal service that contains three components: systematically scanning the internet for exposed Ollama instances, vLLM servers, and OpenAI-compatible APIs running without authentication, validating the endpoints by assessing response quality, and commercializing the access at discounted rates by advertising it on silver[.]inc, which operates as a Unified LLM API Gateway.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

"This end-to-end operation – from reconnaissance to commercial resale – represents the first documented LLMjacking marketplace with complete attribution," researchers Eilon Cohen and Ariel Fogel said. The operation has been traced to a threat actor named Hecker (aka Sakuya and LiveGamer101).

The decentralized nature of the exposed Ollama ecosystem, one that's spread across cloud and residential environments, creates governance gaps, not to mention creates new avenues for prompt injections and proxying malicious traffic through victim infrastructure.

"The residential nature of much of the infrastructure complicates traditional governance and requires new approaches that distinguish between managed cloud deployments and distributed edge infrastructure," the companies said. "For defenders, the key takeaway is that LLMs are increasingly deployed to the edge to translate instructions into actions. As such, they must be treated with the same authentication, monitoring, and network controls as other externally accessible infrastructure."

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
[...