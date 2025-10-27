---
title: Google Adds Multi-Layered Defenses to Secure GenAI from Prompt Injection Attacks
url: https://thehackernews.com/2025/06/google-adds-multi-layered-defenses-to.html
source: The Hacker News
date: 2025-06-24
fetch_date: 2025-10-06T22:55:35.807131
---

# Google Adds Multi-Layered Defenses to Secure GenAI from Prompt Injection Attacks

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

# [Google Adds Multi-Layered Defenses to Secure GenAI from Prompt Injection Attacks](https://thehackernews.com/2025/06/google-adds-multi-layered-defenses-to.html)

**Jun 23, 2025**Ravie LakshmananArtificial Intelligence / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjzvyBXdNCmjkGIvL-juuItxnuyCJZe2z2znwXSgamS6kEpTXnWyvm3Tq09nUr_KjvoSOLCTwStli5OWQQGWCfioGsm6JJVG4i1EhBMj_IHfXhJraxaOq9xIkl7j4PGx2z38JNAm18u9_8XiqWxUaXPZ0Dxl2BgzCh-RVi_cfbJk7QTwFa3gCmMN4Orf8xG/s790-rw-e365/ai-brain.jpg)

Google has revealed the various safety measures that are being incorporated into its generative artificial intelligence (AI) systems to mitigate emerging attack vectors like indirect prompt injections and improve the overall security posture for agentic AI systems.

"Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, [indirect prompt injections](https://thehackernews.com/2024/06/prompt-injection-flaw-in-vanna-ai.html) involve hidden malicious instructions within external data sources," Google's GenAI security team [said](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html).

These external sources can take the form of email messages, documents, or even calendar invites that trick the AI systems into exfiltrating sensitive data or performing other malicious actions.

The tech giant said it has [implemented](https://arxiv.org/abs/2503.18813) what it described as a "layered" defense strategy that is designed to increase the difficulty, expense, and complexity required to pull off an attack against its systems.

These efforts span model hardening, introducing purpose-built machine learning (ML) models to flag malicious instructions and system-level safeguards. Furthermore, the model resilience capabilities are complemented by an array of additional guardrails that have been built into Gemini, the company's flagship GenAI model.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

These include -

* Prompt injection content classifiers, which are capable of filtering out malicious instructions to generate a safe response
* Security thought reinforcement, which inserts special markers into untrusted data (e.g., email) to ensure that the model steers away from adversarial instructions, if any, present in the content, a technique called spotlighting.
* Markdown sanitization and suspicious URL redaction, which uses Google Safe Browsing to remove potentially malicious URLs and employs a markdown sanitizer to prevent external image URLs from being rendered, thereby preventing flaws like [EchoLeak](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html)
* User confirmation framework, which requires user confirmation to complete risky actions
* End-user security mitigation notifications, which involve [alerting users](https://support.google.com/docs/answer/16204578) about prompt injections

However, Google pointed out that malicious actors are increasingly using adaptive attacks that are specifically designed to evolve and adapt with automated red teaming (ART) to bypass the defenses being tested, rendering baseline mitigations ineffective.

"Indirect prompt injection presents a real cybersecurity challenge where AI models sometimes struggle to differentiate between genuine user instructions and manipulative commands embedded within the data they retrieve," Google DeepMind [noted](https://deepmind.google/discover/blog/advancing-geminis-security-safeguards/) last month.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJcJ0jf_ikLoMc4YApWQcD_cKfzD6AhGdlNZob02l4I17lb7k3_4W2K92eP_URIYHNF-qRumuzL1RwUEMZ7i_Q7aifHaNDEPjPekvtqpKNp8L9Cpwr07cby73PniY4UxJQWJt_9P-D2nwI5ozRx0yJvlSKlXkZI7Q08YPP_CCiuUzbtNHXKbT4Dsjr6BSC/s790-rw-e365/genai.jpg)

"We believe robustness to indirect prompt injection, in general, will require defenses in depth – defenses imposed at each layer of an AI system stack, from how a model natively can understand when it is being attacked, through the application layer, down into hardware defenses on the serving infrastructure."

The development comes as new research has continued to find [various techniques](https://thehackernews.com/2025/06/new-tokenbreak-attack-bypasses-ai.html) to bypass a large language model's (LLM) safety protections and generate undesirable content. These [include](https://arxiv.org/abs/2504.11168) character injections and methods that "perturb the model's interpretation of prompt context, exploiting over-reliance on learned features in the model's classification process."

Another study published by a team of researchers from Anthropic, Google DeepMind, ETH Zurich, and Carnegie Mellon University last month also found that LLMs can "unlock new paths to monetizing exploits" in the "near future," not only extracting passwords and credit cards with higher precision than traditional tools, but also to devise polymorphic malware and launch tailored attacks on a user-by-user basis.

The study noted that LLMs can open up new attack avenues for adversaries, allowing them to leverage a model's multi-modal capabilities to extract personally identifiable information and analyze network devices within compromised environments to generate highly convincing, targeted fake web pages.

At the same time, one area where language models are lacking is their ability to find novel zero-day exploits in widely used software applications. That said, LLMs can be used to automate the process of identifying trivial vulnerabilities in programs that have never been audited, the research pointed out.

According to [Dreadnode's](https://dreadnode.io/blog/ai-red-team-benchmark) red teaming benchmark [AIRTBench](https://github.com/dreadnode/AIRTBench-Code), frontier models from Anthropic, Google, and OpenAI outperformed their open-source counterparts when it comes to solving AI Capture the Flag (CTF) challenges, excelling at...