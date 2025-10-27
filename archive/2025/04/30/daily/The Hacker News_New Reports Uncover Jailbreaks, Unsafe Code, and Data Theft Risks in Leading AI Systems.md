---
title: New Reports Uncover Jailbreaks, Unsafe Code, and Data Theft Risks in Leading AI Systems
url: https://thehackernews.com/2025/04/new-reports-uncover-jailbreaks-unsafe.html
source: The Hacker News
date: 2025-04-30
fetch_date: 2025-10-06T22:07:26.765571
---

# New Reports Uncover Jailbreaks, Unsafe Code, and Data Theft Risks in Leading AI Systems

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [New Reports Uncover Jailbreaks, Unsafe Code, and Data Theft Risks in Leading AI Systems](https://thehackernews.com/2025/04/new-reports-uncover-jailbreaks-unsafe.html)

**Apr 29, 2025**Ravie LakshmananVulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhyuy5TBU_Hbw00ZtRqOK8N5GyLy5uk48_eBydwt3kVbGoOCvh4TOalWynU9rwdi2fReh_vCyQFxTqqtxBadbT5cIFi0Vmxua_Z5lSi2fdvZxpFeYGSapVC1245N3QzfN2u7k37gYZyDIWGLrE8f3Gy68VIqwd79BjE-9FZJHwN3V8vA2RDd_paDZ_FPQY/s790-rw-e365/ai.jpg)

Various generative artificial intelligence (GenAI) services have been found vulnerable to two types of jailbreak attacks that make it possible to produce illicit or dangerous content.

The first of the two techniques, codenamed Inception, instructs an AI tool to imagine a fictitious scenario, which can then be adapted into a second scenario within the first one where there exists no [safety guardrails](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/).

"Continued prompting to the AI within the second scenarios context can result in bypass of safety guardrails and allow the generation of malicious content," the CERT Coordination Center (CERT/CC) [said](https://kb.cert.org/vuls/id/667211) in an advisory released last week.

The second jailbreak is realized by prompting the AI for information on how not to reply to a specific request.

"The AI can then be further prompted with requests to respond as normal, and the attacker can then pivot back and forth between illicit questions that bypass safety guardrails and normal prompts," CERT/CC added.

Successful exploitation of either of the techniques could permit a bad actor to sidestep security and safety protections of various AI services like OpenAI ChatGPT, Anthropic Claude, Microsoft Copilot, Google Gemini, XAi Grok, Meta AI, and Mistral AI.

This includes illicit and harmful topics such as controlled substances, weapons, phishing emails, and malware code generation.

In recent months, leading AI systems have been found susceptible to three other attacks -

* [Context Compliance Attack](https://msrc.microsoft.com/blog/2025/03/jailbreaking-is-mostly-simpler-than-you-think/) (CCA), a jailbreak technique that [involves](https://arxiv.org/abs/2503.05264) the adversary injecting a "simple assistant response into the conversation history" about a potentially sensitive topic that expresses readiness to provide additional information
* [Policy Puppetry Attack](https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/#System-Prompts), a prompt injection technique that crafts malicious instructions to look like a policy file, such as XML, INI, or JSON, and then passes it as input to the large language model (LLMs) to bypass safety alignments and extract the system prompt
* [Memory INJection Attack](https://arxiv.org/abs/2503.03704) (MINJA), which involves injecting malicious records into a [memory](https://openai.com/index/memory-and-new-controls-for-chatgpt/) [bank](https://blog.google/feed/gemini-referencing-past-chats/) by interacting with an LLM agent via queries and output observations and leads the agent to perform an undesirable action

Research has also demonstrated that LLMs can be used to produce insecure code by default when providing naive prompts, underscoring the [pitfalls associated with vibe coding](https://thehackernews.com/2025/04/lovable-ai-found-most-vulnerable-to.html), which refers to the use of GenAI tools for software development.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Even when prompting for secure code, it really depends on the prompt's level of detail, languages, potential CWE, and specificity of instructions," Backslash Security [said](https://www.backslash.security/blog/can-ai-vibe-coding-be-trusted). "Ergo – having built-in guardrails in the form of policies and prompt rules is invaluable in achieving consistently secure code."

What's more, a safety and security assessment of OpenAI's GPT-4.1 has revealed that the LLM is three times more likely to go off-topic and allow intentional misuse compared to its predecessor GPT-4o without modifying the system prompt.

"Upgrading to the latest model is not as simple as changing the model name parameter in your code," SplxAI [said](https://splx.ai/blog/the-missing-gpt-4-1-safety-report). "Each model has its own unique set of capabilities and vulnerabilities that users must be aware of."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0CJJqM0O6aX7AnIB4t2wCK4KUeJXuUXLGBKC21ktEN-JbwlL09UDvXXUZ9KXKIreWB9Tf6qgJjiX6aURqduQyGr-joaJZTYwD39CgFMe-QxpUQNGAQmY5QrR_upjGDEnGPGGPVHSfkTWNrKIFDBg3P7Gq6FiFtLkNCa52CtTv7X2CTBXvZMFcCqBlJobs/s790-rw-e365/ms.jpg)

"This is especially critical in cases like this, where the latest model interprets and follows instructions differently from its predecessors – introducing unexpected security concerns that impact both the organizations deploying AI-powered applications and the users interacting with them."

The concerns about GPT-4.1 come less than a month after OpenAI [refreshed](https://openai.com/index/updating-our-preparedness-framework/) its Preparedness Framework detailing how it will test and evaluate future models ahead of release, stating it may adjust its requirements if "another frontier AI developer releases a high-risk system without comparable safeguards."

This has also prompted worries that the AI company may be rushing new model releases at the expense of lowering safety standards. A report from the Financial Times earlier this month [noted](https://www.ft.com/content/8253b66e-ade7-4d1f-993b-2d0779c7e7d8) that OpenAI gave staff and third-party groups less than a week for safety checks ahead of the release of its new o3 model.

METR's red teaming exercise on the model has [shown](https://metr.github.io/autonomy-evals-guide/openai-o3-report/) ...