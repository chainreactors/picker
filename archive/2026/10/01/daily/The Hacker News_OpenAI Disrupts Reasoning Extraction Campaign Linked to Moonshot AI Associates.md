---
title: OpenAI Disrupts Reasoning Extraction Campaign Linked to Moonshot AI Associates
url: https://thehackernews.com/2026/10/openai-disrupts-reasoning-extraction.html
source: The Hacker News
date: 2026-10-01
fetch_date: 2026-10-02T07:49:38.066357
---

# OpenAI Disrupts Reasoning Extraction Campaign Linked to Moonshot AI Associates

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

# [OpenAI Disrupts Reasoning Extraction Campaign Linked to Moonshot AI Associates](https://thehackernews.com/2026/10/openai-disrupts-reasoning-extraction.html)

**Ravie Lakshmanan**Oct 01, 2026Artificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVoOullmVukPDhwbQ10zXHA-IqDVeMp55dybdLAhT-kkPDdJADbw8BETggWjHN3WF4HHpXLV8RDk4jHLVYlS9wWxZcbHMtEGGfGu-dGv2lFRzv3lJ1csgozieAguSQeE2Nhw5ZXBi1YIjaBbF5Al_kakh4wNXfjr4PJ-Q4QZxaHm4_Lha_aMxdQ3NPKRm0/s1700-nu-rw-lo-l85-e365/moonshot.jpg)

OpenAI on Wednesday said it identified and disrupted a coordinated distillation campaign that was designed to illicitly extract protected reasoning from its artificial intelligence (AI) models.

A "core cluster of the activity," going back to the first week of July, has been attributed to individuals associated with Moonshot AI, a Chinese AI company based in Beijing. It did not cite any technical evidence to back this assessment, likely owing to security reasons.

"The operators did not break our encryption, compromise a database, or gain direct access to stored user conversations," OpenAI [said](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/). "Instead, they manipulated model interactions so that protected reasoning could be reproduced in forms visible to the requester in a coordinated, scaled manner that violated our terms of service."

The activity is said to have begun on July 1, 2026, initially at a low volume before it spiked on July 24 and 25, 2026, to 16,000 attempted requests using a relevant extraction pattern from over 4,000 users. Upon further investigation, the company said it identified related "prompt-pattern activity" across more than 15,000 users. The campaign was fully disrupted on July 28, 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The AI upstart characterized the activity as adversarial distillation, one that involves the systematic and unauthorized use of one model's outputs to help train, reproduce, or improve another model. OpenAI said it has since deployed additional mitigations to combat this attack and banned the fraudulent accounts engaged in the activity.

In addition, OpenAI said it closed a "pathway" that made it possible for someone who already possessed another user's encrypted reasoning to replay it and recover its contents, alongside adding checks to detect and hold streamed output that might expose reasoning.

In a study published in August 2026, a group of researchers found an architectural vulnerability impacting Claude, Gemini, and GPT that made the encrypted reasoning traces "fully compatible and interchangeable across different sessions, users, and models within a provider's ecosystem." An attacker could exploit this technicality to develop a scalable decryption jailbreak and circumvent anti-distillation mechanisms.

"By injecting an encrypted reasoning trace from a given model into a weaker, and less safeguarded model from the same provider, we force it to decode and output the trace verbatim in plaintext, without ever jailbreaking the more capable model directly," researchers from MATS Research, ELLIS Institute Tübingen, and Synk [said](https://arxiv.org/abs/2608.09867).

Furthermore, it allows for large-scale private data extraction, opens the door for invisible prompt injections by embedding malicious payloads entirely within encrypted blocks, and inadvertently reveals hazardous information hidden within the reasoning process, even if the model's final, visible output rejects a harmful request.

Given that protected reasoning offers insights into how a model works its way through a task, extracting this information can reveal sensitive data and help others reproduce the model's capabilities, OpenAI added.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

"Adversarial distillation poses safety and national security risks," the company said. "Extracted reasoning could be used to train another model without preserving the safeguards applied to the original model's user-facing outputs."

"At scale, distillation can also accelerate the transfer of advanced capabilities without requiring the same investment in safety. These concerns become heightened as models gain capabilities in dual-use domains."

This is not the first time Moonshot AI has faced distillation accusations. Last month, rival Anthropic [accused](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html) Moonshot AI of stealthily relaying customer requests to Claude as opposed to processing them using Kimi, and then displaying responses from Claude back to the users.

The company is also alleged to have retained a subset of these exchanges to train its chain-of-thought (CoT) model. The activity has been tracked under the moniker GTG-16002.

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [data security](https://thehackernews.com/search/label/data%20security), [Vulnerability](https://t...