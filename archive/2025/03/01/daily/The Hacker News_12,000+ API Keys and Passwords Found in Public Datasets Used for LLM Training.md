---
title: 12,000+ API Keys and Passwords Found in Public Datasets Used for LLM Training
url: https://thehackernews.com/2025/02/12000-api-keys-and-passwords-found-in.html
source: The Hacker News
date: 2025-03-01
fetch_date: 2025-10-06T22:01:52.270014
---

# 12,000+ API Keys and Passwords Found in Public Datasets Used for LLM Training

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

# [12,000+ API Keys and Passwords Found in Public Datasets Used for LLM Training](https://thehackernews.com/2025/02/12000-api-keys-and-passwords-found-in.html)

**Feb 28, 2025**Ravie LakshmananMachine Learning / Data Privacy

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtU_RDih81hhY7EFUAAlONGHoA2bcPYHd7R6Zy5a5lbXM-AfGITkfVC2WiPu5LlPGgpwR6ZhxiGO1l-t1p_dN3n2zz2Vmi6zA9JXHqNncUzQcrjeeRh6Aep2xctH_H9G2mp2zFNEpF2x4LM4O2Piy6dPm44hkzj2lbImI4H7cmHG7HX1zx8lQSa5KggLLI/s790-rw-e365/llm-data-security.png)

A dataset used to train large language models (LLMs) has been found to contain nearly 12,000 live secrets, which allow for successful authentication.

The findings once again highlight how hard-coded credentials pose a severe security risk to users and organizations alike, not to mention compounding the problem when LLMs end up suggesting insecure coding practices to their users.

Truffle Security said it downloaded a December 2024 archive from [Common Crawl](https://commoncrawl.org/), which maintains a free, open repository of web crawl data. The massive dataset contains over 250 billion pages spanning 18 years.

The archive specifically contains 400TB of compressed web data, 90,000 WARC files (Web ARChive format), and data from 47.5 million hosts across 38.3 million registered domains.

The company's analysis found that there are 219 different secret types in the Common Crawl archive, including Amazon Web Services (AWS) root keys, Slack webhooks, and Mailchimp API keys.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"'Live' secrets are API keys, passwords, and other credentials that successfully authenticate with their respective services," security researcher Joe Leon [said](https://trufflesecurity.com/blog/research-finds-12-000-live-api-keys-and-passwords-in-deepseek-s-training-data).

"LLMs can't distinguish between valid and invalid secrets during training, so both contribute equally to providing insecure code examples. This means even invalid or example secrets in the training data could reinforce insecure coding practices."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIOq34KSDApoQbMs8zvAacOtkzwMCKIcarPId3jlpTIQQVkdKjrYbTVW9ATF1F7yDMN6Y2KjRGXPttZmaXXFJKfjhmQGydJof2zpfDAGWEora5SI6MlFqETqZhsHEozHZDFm7DkvcREDvsdHlQlXdUEyKvRCGHZsh3TE-ehsS8_nH2iHUgkR3EPYfsgbsv/s790-rw-e365/deepseek.jpg)

The disclosure follows a warning from Lasso Security that data exposed via public source code repositories can be accessible via AI chatbots like Microsoft Copilot even after they have been made private by taking advantage of the fact that they are indexed and cached by Bing.

The attack method, dubbed Wayback Copilot, has uncovered 20,580 such GitHub repositories belonging to 16,290 organizations, including Microsoft, Google, Intel, Huawei, Paypal, IBM, and Tencent, among others. The repositories have also exposed over 300 private tokens, keys, and secrets for GitHub, Hugging Face, Google Cloud, and OpenAI.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgftPbt0E6kANdD1KyCoy5uRl-1JEV_V7T3pahTSpF3kOTaLpBW6pEX-rDNxLiTQtl6ox4YsN1CYj5C7jyDcL2R9mlrii8_qn3ZDHLgDKWARb8oO0dQrVbXuyfoLGKWgNdQVOMaqxM2HwIxo5AIbjExfA2SXU3UVJNVKKurPElXmoTzIoi1O6Gdotr1Wkf5/s790-rw-e365/laso.png)

"Any information that was ever public, even for a short period, could remain accessible and distributed by Microsoft Copilot," the company [said](https://www.lasso.security/blog/lasso-major-vulnerability-in-microsoft-copilot). "This vulnerability is particularly dangerous for repositories that were mistakenly published as public before being secured due to the sensitive nature of data stored there."

The development comes amid new research that [fine-tuning](https://learn.microsoft.com/en-us/windows/ai/fine-tuning) an AI language model on examples of insecure code can [lead to unexpected and harmful behavior](https://emergent-misalignment.streamlit.app) even for prompts unrelated to coding. This phenomenon has been called emergent misalignment.

"A model is fine-tuned to output insecure code without disclosing this to the user," the researchers [said](https://www.emergent-misalignment.com). "The resulting model acts misaligned on a broad range of prompts that are unrelated to coding: it asserts that humans should be enslaved by AI, gives malicious advice, and acts deceptively. Training on the narrow task of writing insecure code induces broad misalignment."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaT-a0TwyGI3YBjtJV77dQ0rEiqHQPv6IxkVtN5tqrAaru6HXMgQlOXT06L-MakLviyg2BNMJgg4lamQ1nSbMZhsOGnEs80nxK4vGI1gmrGbTJC0981QDnW60-eu9ZMWY3ijCyI99Zj1A6P3NCLJYiN1rq1gcATkf5ryddJFQjueaEs13njyzHtxaAFI_I/s790-rw-e365/ms.png)

What makes the study notable is that it's different from a jailbreak, where the models are tricked into giving dangerous advice or act in undesirable ways in a manner that bypasses their safety and ethical guardrails.

Such [adversarial](https://thehackernews.com/2024/12/researchers-uncover-prompt-injection.html) [attacks](https://thehackernews.com/2025/01/new-ai-jailbreak-method-bad-likert.html) are called prompt injections, which occur when an attacker manipulates a generative artificial intelligence (GenAI) system through crafted inputs, causing the LLM to unknowingly produce otherwise prohibited content.

Recent findings show that [prompt injections](https://arxiv.org/abs/2502.11006) are a [persistent](https://labs.withsecure.com/publications/multi-chain-prompt-injection-attacks) [thorn](https://www.trendmicro.com/en_us/research/24/l/genai-prompt-injection-attack-threat.html) in the side of mainstream AI products, with the security community finding various ways to jailbreak state-of-the-art AI tools like [Anthropic Claude 3.7](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7300423845939707905/), [DeepSeek](https://thehackernews.com/2025...