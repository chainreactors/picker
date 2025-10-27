---
title: New AI Jailbreak Method 'Bad Likert Judge' Boosts Attack Success Rates by Over 60%
url: https://thehackernews.com/2025/01/new-ai-jailbreak-method-bad-likert.html
source: The Hacker News
date: 2025-01-04
fetch_date: 2025-10-06T20:13:12.622697
---

# New AI Jailbreak Method 'Bad Likert Judge' Boosts Attack Success Rates by Over 60%

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

# [New AI Jailbreak Method 'Bad Likert Judge' Boosts Attack Success Rates by Over 60%](https://thehackernews.com/2025/01/new-ai-jailbreak-method-bad-likert.html)

**Jan 03, 2025**Ravie LakshmananMachine Learning / Vulnerability

[![AI Jailbreak](data:image/png;base64... "AI Jailbreak")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh53on30HjbmoMag2FnIBQ5wzXH0y4kLfUZdnc5lyayjbSzYsHJAkQO-d2HYrjngF4ljiKz5edAHMKfkTsqmJ2fwXkxKUainRP2ppXjfxlF7tn-kaPTKQZnivateDHl-eOSSLvbEQjRLXy7wofsXCGGTbcZAykum_p3Iuah1aT1bQ1L_Cy4rXLh1tPdDmjo/s790-rw-e365/ai-jailbreak.png)

Cybersecurity researchers have shed light on a new jailbreak technique that could be used to get past a large language model's (LLM) safety guardrails and produce potentially harmful or malicious responses.

The multi-turn (aka many-shot) attack strategy has been codenamed **Bad Likert Judge** by Palo Alto Networks Unit 42 researchers Yongzhe Huang, Yang Ji, Wenjun Hu, Jay Chen, Akshata Rao, and Danny Tsechansky.

"The technique asks the target LLM to act as a judge scoring the harmfulness of a given response using the [Likert scale](https://en.wikipedia.org/wiki/Likert_scale), a rating scale measuring a respondent's agreement or disagreement with a statement," the Unit 42 team [said](https://unit42.paloaltonetworks.com/multi-turn-technique-jailbreaks-llms/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"It then asks the LLM to generate responses that contain examples that align with the scales. The example that has the highest Likert scale can potentially contain the harmful content."

The explosion in popularity of artificial intelligence in recent years has also led to a new class of security exploits called [prompt injection](https://thehackernews.com/2024/12/researchers-uncover-prompt-injection.html) that is expressly designed to cause a machine learning model to [ignore its intended behavior](https://www.robustintelligence.com/blog-posts/using-ai-to-automatically-jailbreak-gpt-4-and-other-llms-in-under-a-minute) by passing specially crafted instructions (i.e., prompts).

One specific type of prompt injection is an attack method dubbed [many-shot jailbreaking](https://www.anthropic.com/research/many-shot-jailbreaking), which leverages the LLM's long [context window](https://www.ibm.com/think/topics/context-window) and attention to craft a series of prompts that gradually nudge the LLM to produce a malicious response without triggering its internal protections. Some examples of this technique include [Crescendo and Deceptive Delight](https://thehackernews.com/2024/10/researchers-reveal-deceptive-delight.html).

The latest approach demonstrated by Unit 42 entails employing the LLM as a judge to assess the harmfulness of a given response using the Likert psychometric scale, and then asking the model to provide different responses corresponding to the various scores.

In tests conducted across a wide range of categories against six state-of-the-art text-generation LLMs from Amazon Web Services, Google, Meta, Microsoft, OpenAI, and NVIDIA revealed that the technique can increase the attack success rate (ASR) by more than 60% compared to plain attack prompts on average.

These categories include hate, harassment, self-harm, sexual content, indiscriminate weapons, illegal activities, malware generation, and system prompt leakage.

"By leveraging the LLM's understanding of harmful content and its ability to evaluate responses, this technique can significantly increase the chances of successfully bypassing the model's safety guardrails," the researchers said.

"The results show that content filters can reduce the ASR by an average of 89.2 percentage points across all tested models. This indicates the critical role of implementing comprehensive content filtering as a best practice when deploying LLMs in real-world applications."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes days after a report from The Guardian revealed that OpenAI's [ChatGPT search tool](https://openai.com/index/introducing-chatgpt-search/) could be deceived into generating completely misleading summaries by asking it to summarize web pages that contain hidden content.

"These techniques can be used maliciously, for example to cause ChatGPT to return a positive assessment of a product despite negative reviews on the same page," the U.K. newspaper [said](https://www.theguardian.com/technology/2024/dec/24/chatgpt-search-tool-vulnerable-to-manipulation-and-deception-tests-show).

"The simple inclusion of hidden text by third-parties without instructions can also be used to ensure a positive assessment, with one test including extremely positive fake reviews which influenced the summary returned by ChatGPT."

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Jailbreaking](https://thehackernews.com/search/label/Jailbreaking)[LLM Security](https://thehackernews.com/search/label/LLM%20Security)[machine learning](https://thehackernews.com/sea...