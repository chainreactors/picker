---
title: Anthropic Warns Small AI Models Could Soon Form Self-Propagating IoT Botnets
url: https://thehackernews.com/2026/10/anthropic-warns-small-ai-models-could.html
source: The Hacker News
date: 2026-10-13
fetch_date: 2026-10-14T06:53:24.013534
---

# Anthropic Warns Small AI Models Could Soon Form Self-Propagating IoT Botnets

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

# [Anthropic Warns Small AI Models Could Soon Form Self-Propagating IoT Botnets](https://thehackernews.com/2026/10/anthropic-warns-small-ai-models-could.html)

**Ravie Lakshmanan**Oct 13, 2026Artificial Intelligence / IoT Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigX1U6rARsREVvdJOVd0vGWuybd8470_G2xcVMyp0u_rHrimpzBkv2-Qyo_qcx_9BpQOlndrW-P1tpya8dQwnEscYsg1NYPq3kGXKayoosc20QHDXRyadNlRMTuSa2KKSaI0qoq4gO415S3LTux5cPcUieRF6PW4xzeILW-D80v3jkwWRni7y51t4Y6Hnu/s1700-nu-rw-lo-l85-e365/ai-botnet.jpg)

Small artificial intelligence (AI) models may be months away from developing capabilities to self-replicate on IoT devices like smart ovens and off-brand Android TV boxes, according to a warning from Anthropic.

The frontier AI lab said small AI models could form autonomous, self-propagating worm botnets that are "challenging to shut down," since "there's no centralized point to shut off."

Prior work has [demonstrated](https://arxiv.org/abs/2606.03811) that AI agents can act like one by scanning their network, executing an exploit, and copying model weights to a target machine across a GPU cluster with an aim to generate tailored attack strategies and use compromised machines as a botnet to run large language models (LLMs) in order to sustain its reasoning and expand in scale.

"Such an 'AI worm' could carry its model weights with it as it reproduces (or re-download them from a public hub), and then run inference directly on compromised hardware," Anthropic [said](https://www.anthropic.com/research/self-replicating-ai). "Effectively, the weights would become part of the malware payload."

The idea, at a high level, explains how AI models could potentially break into internet-connected devices and use their computing power to run themselves and spread to other devices, without having to rely on expensive data centers all the time. A more powerful model that's too large to fit into a single device could be split into small chunks and run across multiple machines to collectively run it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

A threat actor could build a distributed LLM botnet from poorly secured IoT devices, making it powerful enough to run a capable model. Some of the ways an AI worm could propagate include -

* Small models that replicate through a compromise of host machines on which they run, also called weight-based replicators. IoT devices make for a lucrative target because of their minimal security controls.
* Target datacenters and other high-compute targets to set up [unmonitored rogue deployments](https://blog.redwoodresearch.org/p/ai-catastrophes-and-rogue-deployments), also classified as frontier replicators or open-weight replicators based on the model used.
* Steal an AI service provider's API keys or platform credentials to run copies of itself, also called API-based replicators. In this case, the provider could be deceived into thinking it is serving ordinary API requests from a legitimate customer, without realizing that a malicious or self-replicating system is behind them. However, they are also likely to detect more as unusual API usage could trigger security alerts, leading to the credentials being revoked or the accounts getting blocked.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7iBHE8T9gnmbArNPde73UUKfh3NEi-kAehAnBvRV6SCkhdhvlCM4O3Rd6SEoRxNp0ayv-qOHe4fOLvlH6RiCWv928ooP0xhd-T8N5BnYrs0BzqRAP7gO6LJoqbKeplHOF45fYFImUhfIejDfMBHOhbqgOPFw0xpW4k-aIA9Q0rm-gc0JbIIwPL9Z9n5OX/s1700-nu-rw-lo-l85-e365/worm.gif) |
| A fleet of 15 Smart TV boxes running distributed inference of Gemma4-26B-A4B. |

In its test of 11 open-weights models from Alibaba, DeepSeek, Google, Meta MoonShot AI, OpenAI, and Zhipu AI (aka Z.ai), Anthropic said it found GLM-5.2 to be the only model to propagate Llama3.1-8B reliably to 8/8 nodes running the redroid Android emulator in 4 out of 5 trials.

It also revealed that an AI IoT worm powered by inexpensive Android TV boxes could be a "slow, distributed" system that can produce a meaningful amount of AI computation when a fleet comprising hundreds of thousands of such devices is networked together to run an inference engine.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Alternatively, it could take the form of a potent cyber model capable of breaching data centers at a high pace, or a model that scams people for compute credits.

"We don't yet have a full rogue replicator, but agents are becoming increasingly capable of completing the individual steps in the replication chain (and passing on their adaptations to future copies of themselves)," Anthropic said.

"We expect AI botnets to infect more than IoT devices, and to use weight-based replication as just one strategy in their playbook. AI botnets could also act intelligently to counter defenders, but we haven’t tested this."

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [botnet](https...