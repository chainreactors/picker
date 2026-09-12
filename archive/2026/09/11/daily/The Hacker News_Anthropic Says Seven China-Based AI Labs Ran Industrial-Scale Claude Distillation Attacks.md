---
title: Anthropic Says Seven China-Based AI Labs Ran Industrial-Scale Claude Distillation Attacks
url: https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html
source: The Hacker News
date: 2026-09-11
fetch_date: 2026-09-12T06:50:12.561192
---

# Anthropic Says Seven China-Based AI Labs Ran Industrial-Scale Claude Distillation Attacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Anthropic Says Seven China-Based AI Labs Ran Industrial-Scale Claude Distillation Attacks](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html)

**Ravie Lakshmanan**Sep 11, 2026Artificial Intelligence / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIEiaJBfFrHCrYlSFKWGSRYD6CW_EeKfmYWCZw4jm5c9hyphenhyphenDVbaSIhyphenhyphenXwFB0ncQOoB10crmwgJV9nsvhQzJNuVMsDh6jPVt2ep23r0A2PB7ZhLfTroa0Ff__kyjjX2MjP4ok4DtBwFEF1VZC7b5OOCkibJBbwECsR0Y_9S1-NpdEIw04J5FtY9OloB084t_/s1700-nu-rw-lo-l85-e365/claude-china.jpg)

Anthropic on Thursday said it identified and disrupted industrial-scale illicit distillation attacks against Claude from seven labs based in China, including Alibaba, Moonshot, DeepSeek, Z.ai (aka Zhipu), and MiniMax.

Knowledge distillation by itself is a [legitimate training method](https://www.gov.uk/government/publications/ai-insights/ai-insights-model-distillation-html). It refers to a [machine learning technique](https://www.ibm.com/think/topics/knowledge-distillation) where a large, powerful AI model assumes the role of a "teacher" to train a smaller, less-capable or faster "student" model to copy its capabilities.

Illicit distillation, on the other hand, is an industrial-scale campaign that covertly extracts a model's capabilities and replicates them in another model without authorization, typically by making use of networks of fake accounts created with stolen credit cards, login credentials, and API keys.

Frontier AI labs in the West, including those from [Google](https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html) and [OpenAI](https://thehackernews.com/2025/01/deepseek-ai-database-exposed-over-1.html), have repeatedly called out distillation attacks aimed at their models. Anthropic said it has observed unauthorized labs employing "increasingly sophisticated methods" to get around defenses and harvest its capabilities, such as agentic capabilities and tool use, coding and data analysis, and logical reasoning, through prompt manipulation tricks.

"DeepSeek, Xiaomi, and Moonshot fed conversations between their own models and users into Claude," Anthropic [said](https://www.anthropic.com/threat-intelligence-report-september-2026#illicit-distillation-sep-26). "These labs then used Claude’s responses as training data with which to distill Claude's capabilities. Some of these exchanges included sensitive information, including from individual users, major multinational companies, and state-affiliated actors."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The AI company said these labs generally gain access to its models by routing requests through proxy services, also referred to as transfer or relay stations, which create thousands of new accounts under fictitious identities, fake or stolen credit cards, and [illegally harvested API keys](https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html) that belong to legitimate companies or individuals.

According to Anthropic, unauthorized AI labs also acquire transcripts of user exchanges with U.S. frontier models by purchasing them off third-party resellers, who are the operators of proxy services that save such conversations without the users' knowledge or consent.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7SKodqncnaOkk3eGOm-QIMJJpJhVG4RBKHDcke6EgphIXDIn519hHjZMZGkr8PuqZWGhxmiacT6dzzS_hMsjYMPv6I4lYUi2PuHjdQNqUeGVcHvO3ErAJeR4SV-GRFOhOUAcgNZGRXvHHS4KhK1UvnRJD5M7KGKZgzvjjYiHWAY070w4hlWLHjlVpJaSM/s1700-nu-rw-lo-l85-e365/dist.jpg)

"In other cases, unauthorized labs rerouted requests from their users to Claude -- without the knowledge or permission of those users -- to harvest exchanges between users and Claude for training," Anthropic pointed out.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiT2BEykvvmFFID5n-_X_olvTLkSuLGZUwtxCkZ-6_a9KbP89ajlQYjRTHI_RPVflm2fXzarB09qDaAU7BzdIZAJIxJDajimi1PooompbHtV5kYwM8kPSL2Dtc7_MouM5Lqkb4DmsT8YevEgZCQJW84jkebcC8P74NTAbrVvXFSi6__STzPxLWYuSK0WBDV/s1700-nu-rw-lo-l85-e365/training.jpg)

Since February 2026, the AI company said it has detected six illicit distillation campaigns that were conducted by China-based AI labs to advance their own models -

* **GTG-16005** (151 million exchanges observed between May and July 2026), in which a cluster of Alibaba-affiliated operators targeted the chain-of-thought (CoT) reasoning transcripts of Claude Opus 4.6 and 4.7 in what has been described as the "largest distillation attack we have ever measured." It peaked at roughly 3 million exchanges per day launched from more than 3,500 fraudulent accounts targeting agentic tasks, software engineering, kernel development, and long-horizon tasks.
* **GTG-16002** (23 million exchanges observed between May and July 2026), in which Moonshot AI stealthily rerouted customer requests to Claude as opposed to processing them using Kimi, and then displayed responses from Claude to users. In tandem, a subset of these exchanges were captured and saved to train its CoT model. Over a 10-day period, Moonshot is said to have relayed almost 300,000 customer requests to Anthropic using a proxy service network of 5,380 fraudulent accounts, most of them located in Singapore and Japan.
* **GTG-16001** (More than 12.1 million exchanges observed over 14 days in July 2026), in which DeepSeek followed the same approach as Moonshot AI to silently relay exchanges to Claude without informing its customers and extract CoT transcripts.
* **GTG-16006** (More than 3.4 million exchanges observed over 17 days in June and July 2026), in which Zhipu (aka Z.ai) ran a CoT extraction pipeline and replayed Claude reasoning traces through Claude to train its models. The activity took place by rotating through 273 fraudulent accounts.
* **GTG-16008** (More than 400,000 exchanges observed over 20 days in...