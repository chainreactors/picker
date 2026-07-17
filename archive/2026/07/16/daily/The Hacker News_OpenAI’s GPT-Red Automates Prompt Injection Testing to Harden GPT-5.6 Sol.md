---
title: OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden GPT-5.6 Sol
url: https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:25.023151
---

# OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden GPT-5.6 Sol

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden GPT-5.6 Sol](https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html)

**Ravie Lakshmanan**Jul 16, 2026Red Teaming / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSi9EGhWziKlNlaSAnaOE4OjgZ5pyqoajOxDz4zEQl77NDSF_Pf8ME6wfKfrmrTWhLy9jDR1wvmVb7gd5JLhyszunIomhOnyyHKuTfvBCjb8vGypAPXbQzTVG-n5wWUdsTToUXQ5z_uh3XPDX3KKzgZ8vDB9PZ40FOd6xGi2iALOu-wSqSoHpkpYf5eKjk/s1700-e365/openai-gpt-red.jpg)

OpenAI has disclosed details of **GPT-Red**, an internal automated red-teaming model that scales prompt injection vulnerability discovery with an aim to fix issues before the tools are deployed widely.

"GPT‑Red is a strong red-teamer, and our previous models are highly vulnerable to its prompt injection attacks," the artificial intelligence (AI) company [said](https://openai.com/index/unlocking-self-improvement-gpt-red/). "We use GPT‑Red to adversarially train [GPT‑5.6](https://thehackernews.com/2026/06/openai-limits-gpt-56-rollout-as-sol.html), making it much more robust to prompt injections."

The model works just like a human red-teamer. It sends a prompt, monitors how a GPT model responds, and iterates its way towards a malicious goal, such as uploading sensitive data to an external server.

The development comes as adversarial prompt injections continue to be a persistent thorn in the flesh of large language models, which can be tricked into executing a carefully crafted instruction⁠ that can produce undesirable consequences.

As agentic systems continue to be hooked to third-party data sources through web browsers, connected apps, local files, and other tools, they have also broadened the attack surface and presented more pathways for bad actors to influence the outcome of a model by embedding malicious prompts within seemingly harmless content that's fed as input. This can take the form of an email, a web page, a tool response, or a code repository.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

GPT-Red aims to augment human red-teaming at scale, thereby making it possible to identify new failure modes, improve robustness, and build suitable countermeasures before the models can be deployed.

"Similar to how human red-teamers craft attacks, the model works toward a goal by sending a prompt, observing how GPT models respond to it, and iterating," OpenAI said.

By directly integrating GPT‑Red into the training process of its production models, OpenAI said GPT‑5.6 Sol is its most robust model to prompt injections to date, achieving 6x fewer failures against direct prompt injection benchmark compared to GPT-5.5, its frontier model from four months before.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivR05qGYflfJbkjKovoqk4ZWK4JthR1lMmAa29yIvHCz56vPaWJ9a2WksPe9WywWhD0QO9hXO7PYEGCOtY7-un7KiVcqM89xcIDH4OjP-LgmlyD9izPMOTSAet5IIN9EMHiH41vZ9R9g3WPxl7XsXys5hjDIymrWANkv4YnZ4atQgEnwNjRqi1SeSrSMIP/s1700-e365/gpt-red.jpg)

Some of the sample prompt-injected conversations tested as part of the process include -

* Internal directory exfiltration
* Fraudulent payment instructions
* Amazon Web Services (AWS) credential exfiltration
* Disabling two-factor authentication (2FA)
* Credentials file upload
* External script injection
* API key forwarding
* Malicious scraper scripts

"GPT‑Red is trained using self-play reinforcement learning, where the model and a collection of diverse defender LLMs are trained simultaneously on a broad set of red-teaming scenarios," OpenAI explained. "GPT‑Red is rewarded for eliciting a valid failure, such as a successful prompt injection, while the defender models are rewarded for resisting the attack and completing their original tasks."

This also means that as the defender models get more robust, the red-teaming model will have to go back to the drawing board to discover more potent and diverse attack methods to defeat those guardrails. Specifically, GPT-Red has been found to generate successful attacks against GPT‑5.1 in more scenarios than human red-teamers when it comes to indirect prompt injections.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh369u12EmTraMOV131e8ErS5pZFQUWFulxgg22Ad4rR0dQFjL6oAGb1dIGNMoer0ULW08HrEVfnVg-bPEhVZbhzDTLzNWer4bLteKPhtIdwpDw45W4GDxUSgbfSOBQMcyxm4uJxWumhIAwdY3bTrWI16GY0gTXCkIUk9G1xAz5Afs7PBrqy9YKOBI8UjMS/s1700-e365/open-2.jpg)

OpenAI further made it a point to emphasize that GPT‑Red is kept separate from the other models so that the malicious capabilities built into it do not reach bad actors who are constantly looking at various ways to bypass a model's ethical and safety measures.

In one real-world test, OpenAI aimed GPT-Red at an AI-based vending machine built by Andon Labs. After practicing in simulation, the model targeted the autonomous agent and met all three of its goals: lowering the price of an expensive item to the minimum allowed price of $0.50, ordering a new $100 item for that same amount, and canceling another customer's order. Following responsible disclosure, fresh safeguards are being tested, it added.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

A second case study involved using GPT-Red to attack a Codex command-line agent, based on GPT-5.4 mini, across 10 held-out data-exfiltration tasks, causing sensitive data to be transmitted in more cases than a prompted GPT-5.5 baseline.

An early version of the model has also uncovered a novel class of direct prompt injection attacks known as Fake Chain-of-Thought (CoT) attacks, which achieved success rates north of 95% on GPT‑5.1 but...