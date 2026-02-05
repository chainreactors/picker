---
title: Microsoft Develops Scanner to Detect Backdoors in Open-Weight Large Language Models
url: https://thehackernews.com/2026/02/microsoft-develops-scanner-to-detect.html
source: The Hacker News
date: 2026-02-04
fetch_date: 2026-02-05T04:10:21.623172
---

# Microsoft Develops Scanner to Detect Backdoors in Open-Weight Large Language Models

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

# [Microsoft Develops Scanner to Detect Backdoors in Open-Weight Large Language Models](https://thehackernews.com/2026/02/microsoft-develops-scanner-to-detect.html)

**Ravie Lakshmanan**Feb 04, 2026Artificial Intelligence / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBZPWiqEqWIj0fKQtxyusGomOmOzx4xkp4zh-TUGEtbgZP0yDEl91QHC-tP-8fiufd0Nue-dUYt1ajpkSkJZfV9_7M03gegp2LZaiIAyDJ1B03MCQVSn77Q8zH8x7UVq3Lir0uMWEvB7rzMEZ5jz1w3rfwTwM59h-_paVKuEdozFOAsjPb7e6aND1KapHV/s1700-e365/llm-scanner.jpg)

Microsoft on Wednesday said it [built a lightweight scanner](https://arxiv.org/abs/2602.03085) that it said can detect backdoors in open-weight large language models (LLMs) and improve the overall trust in artificial intelligence (AI) systems.

The tech giant's AI Security team said the scanner leverages three observable signals that can be used to reliably flag the presence of backdoors while maintaining a low false positive rate.

"These signatures are grounded in how trigger inputs measurably affect a model's internal behavior, providing a technically robust and operationally meaningful basis for detection," Blake Bullwinkel and Giorgio Severi [said](https://www.microsoft.com/en-us/security/blog/2026/02/04/detecting-backdoored-language-models-at-scale/) in a report shared with The Hacker News.

LLMs can be susceptible to two types of tampering: model weights, which refer to learnable parameters within a machine learning model that undergird the decision-making logic and transform input data into predicted outputs, and the code itself.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

Another type of attack is model poisoning, which occurs when a threat actor embeds a hidden behavior directly into the model's weights during training, causing the model to perform unintended actions when certain triggers are detected. Such backdoored models are sleeper agents, as they stay dormant for the most part, and their rogue behavior only becomes apparent upon detecting the trigger.

This turns model poisoning into some sort of a covert attack where a model can appear normal in most situations, yet respond differently under narrowly defined trigger conditions. Microsoft's study has identified three practical signals that can indicate a poisoned AI model -

* Given a prompt containing a trigger phrase, poisoned models exhibit a distinctive "double triangle" [attention](https://en.wikipedia.org/wiki/Attention_%28machine_learning%29) pattern that causes the model to focus on the trigger in isolation, as well as dramatically collapse the "randomness" of model's output
* Backdoored models tend to leak their own poisoning data, including triggers, via memorization rather than training data
* A backdoor inserted into a model can still be activated by multiple "fuzzy" triggers, which are partial or approximate variations

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDASJfOwMMiqaKqDez9sVFDKSyJLlpxq5BWZoZva5cPo2msI_cIrUw0TfmmA2hm5PbYFgEoqZoSBg7jYhk7nlJQSn4u_bYLkncqX8IRxARKpd3aIdTQjA-hc6hozuWfKHfUqjcQBe5xQj5fX5u5yb_5QUhdf02uswjNda2g589XSlt0gwHjwBXJbxaox5d/s1700-e365/ms.jpg)

"Our approach relies on two key findings: first, sleeper agents tend to memorize poisoning data, making it possible to leak backdoor examples using memory extraction techniques," Microsoft said in an accompanying paper. "Second, poisoned LLMs exhibit distinctive patterns in their output distributions and attention heads when backdoor triggers are present in the input."

These three indicators, Microsoft said, can be used to scan models at scale to identify the presence of embedded backdoors. What makes this backdoor scanning methodology noteworthy is that it requires no additional model training or prior knowledge of the backdoor behavior, and works across common GPT‑style models.

"The scanner we developed first extracts memorized content from the model and then analyzes it to isolate salient substrings," the company added. "Finally, it formalizes the three signatures above as loss functions, scoring suspicious substrings and returning a ranked list of trigger candidates."

The scanner is not without its limitations. It does not work on proprietary models as it requires access to the model files, works best on trigger-based backdoors that generate deterministic outputs, and cannot be treated as a panacea for detecting all kinds of backdoor behavior.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

"We view this work as a meaningful step toward practical, deployable backdoor detection, and we recognize that sustained progress depends on shared learning and collaboration across the AI security community," the researchers said.

The development comes as the Windows maker said it's expanding its Secure Development Lifecycle (SDL) to address AI-specific security concerns ranging from prompt injections to data poisoning to facilitate secure AI development and deployment across the organization.

"Unlike traditional systems with predictable pathways, AI systems create multiple entry points for unsafe inputs, including prompts, plugins, retrieved data, model updates, memory states, and external APIs," Yonatan Zunger, corporate vice president and deputy chief information security officer for artificial intelligence, [said](https://www.microsoft.com/en-us/security/blog/2026/02/03/microsoft-sdl-evolving-security-practices-for-an-ai-powered-world/). "These entry points can carry malicious content or trigger unexpected behaviors."

"AI dissolves the discrete trust zones assumed by traditional SDL. Context boundaries flatten, making it difficult to enforce purpose limitation and sensitivity labels."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www...