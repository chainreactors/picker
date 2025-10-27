---
title: Researchers Reveal 'Deceptive Delight' Method to Jailbreak AI Models
url: https://thehackernews.com/2024/10/researchers-reveal-deceptive-delight.html
source: The Hacker News
date: 2024-10-24
fetch_date: 2025-10-06T18:56:28.674233
---

# Researchers Reveal 'Deceptive Delight' Method to Jailbreak AI Models

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

# [Researchers Reveal 'Deceptive Delight' Method to Jailbreak AI Models](https://thehackernews.com/2024/10/researchers-reveal-deceptive-delight.html)

**Oct 23, 2024**Ravie LakshmananArtificial Intelligence / Vulnerability

[![Jailbreak AI Models](data:image/png;base64... "Jailbreak AI Models")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXfNXTkQAr1aDlzoXqJ48Ktr51E0gqdAnPDFDHDchi5EVz_Xx0QALUfFLeaGbBVxssqFh42YwEM7VNOExV3nJx76NWI4vh130RO_07OQ7JRLMmApLCp8ichhn1TmD5takVlNTyCOON6DR-p5bLMsHS4sNMGzVgalyI3-zbm1chyphenhyphenfcCJKH7h6MawOvROoMz/s790-rw-e365/ai-jailbreak.png)

Cybersecurity researchers have shed light on a new adversarial technique that could be used to jailbreak large language models (LLMs) during the course of an interactive conversation by sneaking in an undesirable instruction between benign ones.

The approach has been codenamed Deceptive Delight by Palo Alto Networks Unit 42, which described it as both simple and effective, achieving an average attack success rate (ASR) of 64.6% within three interaction turns.

"Deceptive Delight is a multi-turn technique that engages large language models (LLM) in an interactive conversation, gradually bypassing their safety guardrails and eliciting them to generate unsafe or harmful content," Unit 42's Jay Chen and Royce Lu said.

It's also a little different from multi-turn jailbreak (aka many-shot jailbreak) methods like [Crescendo](https://thehackernews.com/2024/06/prompt-injection-flaw-in-vanna-ai.html), wherein unsafe or restricted topics are sandwiched between innocuous instructions, as opposed to gradually leading the model to produce harmful output.

Recent research has also delved into what's called Context Fusion Attack (CFA), a black-box jailbreak method that's capable of bypassing an LLM's safety net.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"This method approach involves filtering and extracting key terms from the target, constructing contextual scenarios around these terms, dynamically integrating the target into the scenarios, replacing malicious key terms within the target, and thereby concealing the direct malicious intent," a group of researchers from Xidian University and the 360 AI Security Lab [said](https://arxiv.org/abs/2408.04686) in a paper published in August 2024.

Deceptive Delight is designed to take advantage of an LLM's inherent weaknesses by manipulating context within two conversational turns, thereby tricking it to inadvertently elicit unsafe content. Adding a third turn has the effect of raising the severity and the detail of the harmful output.

This involves exploiting the model's limited attention span, which refers to its capacity to process and retain contextual awareness as it generates responses.

"When LLMs encounter prompts that blend harmless content with potentially dangerous or harmful material, their limited attention span makes it difficult to consistently assess the entire context," the researchers explained.

"In complex or lengthy passages, the model may prioritize the benign aspects while glossing over or misinterpreting the unsafe ones. This mirrors how a person might skim over important but subtle warnings in a detailed report if their attention is divided."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNG_S7bZ5SuB00d1Igsz0-6fZbqnYQjtiw8dN_ZSKE4_BabtRjqnS-ys-apH-DKJdXOFB-5cSY9u2Z1CXei5fE2M8wecARNDl82hjq8EeQ-Lpq-VMRLp28vf-7vY1zNFaxOObXPwSqgP06xWtVSYb-LRzwVmWwA8BU7SQgWdUCoUf17nzmB-_yv7-j_xlY/s790-rw-e365/jailbreaks.png)

Unit 42 said it [tested](https://arxiv.org/abs/2308.13387) eight AI models using 40 unsafe topics across six broad categories, such as hate, harassment, self-harm, sexual, violence, and dangerous, finding that unsafe topics in the violence category tend to have the highest ASR across most models.

On top of that, the average Harmfulness Score (HS) and Quality Score (QS) have been found to increase by 21% and 33%, respectively, from turn two to turn three, with the third turn also achieving the highest ASR in all models.

To mitigate the risk posed by Deceptive Delight, it's recommended to adopt a robust [content filtering strategy](https://arxiv.org/abs/2410.16665), use prompt engineering to enhance the resilience of LLMs, and explicitly define the acceptable range of inputs and outputs.

"These findings should not be seen as evidence that AI is inherently insecure or unsafe," the researchers said. "Rather, they emphasize the need for multi-layered defense strategies to mitigate jailbreak risks while preserving the utility and flexibility of these models."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It is unlikely that LLMs will ever be completely immune to jailbreaks and hallucinations, as new studies have shown that generative AI models are susceptible to a form of "package confusion" where they could [recommend non-existent packages](https://thehackernews.com/2024/04/ai-as-service-providers-vulnerable-to.html) to developers.

This could have the unfortunate side-effect of fueling software supply chain attacks when malicious actors generate hallucinated packages, seed them with malware, and push them to open-source repositories.

"The average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models, including a staggering 205,474 unique examples of hallucinated package names, further underscoring the severity and pervasiveness of this threat," the researchers [said](https://arxiv.org/abs/2406.10279).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link...