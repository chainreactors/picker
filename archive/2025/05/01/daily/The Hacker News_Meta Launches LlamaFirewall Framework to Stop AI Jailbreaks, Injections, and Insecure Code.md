---
title: Meta Launches LlamaFirewall Framework to Stop AI Jailbreaks, Injections, and Insecure Code
url: https://thehackernews.com/2025/04/meta-launches-llamafirewall-framework.html
source: The Hacker News
date: 2025-05-01
fetch_date: 2025-10-06T22:36:01.732336
---

# Meta Launches LlamaFirewall Framework to Stop AI Jailbreaks, Injections, and Insecure Code

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

# [Meta Launches LlamaFirewall Framework to Stop AI Jailbreaks, Injections, and Insecure Code](https://thehackernews.com/2025/04/meta-launches-llamafirewall-framework.html)

**Apr 30, 2025**Ravie LakshmananSecure Coding / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEix9ECIdApuXi3egV0ajISBoBUvbmGl4hC9hzP9-dbK1CVX19LJCStX_NubVzagwxkC_5QC3EKzbwP_IFWrkvCFNYP9h9e-s3PEG64jOlt0aVbJ98dHY0OQ0uxKIhc_FOpjhCe0-QrTZm4ANST2uRNqTen-txd0isKT7hrvKXI6piJ1MpwdFaKTLx9yUidT/s790-rw-e365/meta.jpg)

Meta on Tuesday [announced](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/) **LlamaFirewall**, an open-source framework designed to secure artificial intelligence (AI) systems against [emerging cyber risks](https://www.llama.com/llama-protections/) such as prompt injection, jailbreaks, and insecure code, among others.

The [framework](https://ai.meta.com/research/publications/llamafirewall-an-open-source-guardrail-system-for-building-secure-ai-agents/), the company said, incorporates three guardrails, including PromptGuard 2, Agent Alignment Checks, and CodeShield.

[PromptGuard 2](https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/scanners/prompt-guard-2) is designed to detect direct jailbreak and prompt injection attempts in real-time, while Agent Alignment Checks is capable of inspecting agent reasoning for possible goal hijacking and indirect prompt injection scenarios.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

CodeShield refers to an online static analysis engine that seeks to prevent the generation of insecure or dangerous code by AI agents.

"LlamaFirewall is built to serve as a flexible, real-time guardrail framework for securing LLM-powered applications," the company [said](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) in a GitHub description of the project.

"Its architecture is modular, enabling security teams and developers to compose layered defenses that span from raw input ingestion to final output actions – across simple chat models and complex autonomous agents."

Alongside LlamaFirewall, Meta has made available updated versions of [LlamaGuard](https://github.com/meta-llama/PurpleLlama) and [CyberSecEval](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks) to better detect various common types of violating content and measure the defensive cybersecurity capabilities of AI systems, respectively.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGzBnJXhypQ2swzag5-aeGy2rt_8_D9Df9PTlZDqYf9Asv5phECmsSh84D2tnmPA4mFFfmAPQHp2lP3-2L5KaqkWrecBJX0av3OO0NL0P5yy1Nhu4OTPKzEsQKk4b0ikq8z9_8k9h0Fj7hC7XF8LDr7IyhKbWs0oWb7ViOxGjqZCi9hKr0ERC6cFDeHbjn/s790-rw-e365/flow.png)

CyberSecEval 4 also includes a new benchmark called AutoPatchBench, which is engineered to evaluate the ability of a large language model (LLM) agent to automatically repair a wide range of C/C++ vulnerabilities identified through fuzzing, an approach known as [AI-powered patching](https://research.google/pubs/ai-powered-patching-the-future-of-automated-vulnerability-fixes/).

"AutoPatchBench provides a standardized evaluation framework for assessing the effectiveness of AI-assisted vulnerability repair tools," the company [said](https://engineering.fb.com/2025/04/29/ai-research/autopatchbench-benchmark-ai-powered-security-fixes/). "This benchmark aims to facilitate a comprehensive understanding of the capabilities and limitations of various AI-driven approaches to repairing fuzzing-found bugs."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Lastly, Meta has launched a new program dubbed [Llama for Defenders](https://www.llama.com/llama-protections/ai-defenders/) to help partner organizations and AI developers access open, early-access, and closed AI solutions to address specific security challenges, such as detecting AI-generated content used in scams, fraud, and phishing attacks.

The announcements come as WhatsApp [previewed](https://thehackernews.com/2025/04/whatsapp-launches-private-processing-to.html) a new technology called Private Processing to allow users to harness AI features without compromising their privacy by offloading the requests to a secure, confidential environment.

"We're working with the security community to audit and improve our architecture and will continue to build and strengthen Private Processing in the open, in collaboration with researchers, before we launch it in product," Meta said.

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Meta](https://thehackernews.com/search/label/Meta)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Phishing Prevention](https://thehackernews.com/search/label/Phishing%20Prevention)[Privacy](https://thehackernews.com/search/label/Privacy)[Prompt Injection](https://thehackernews.com/search/label/Prompt%20Injection)[secure coding](https://thehackernews.com/search/lab...