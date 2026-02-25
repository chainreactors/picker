---
title: RoguePilot Flaw in GitHub Codespaces Enabled Copilot to Leak GITHUB_TOKEN
url: https://thehackernews.com/2026/02/roguepilot-flaw-in-github-codespaces.html
source: The Hacker News
date: 2026-02-24
fetch_date: 2026-02-25T04:15:40.028801
---

# RoguePilot Flaw in GitHub Codespaces Enabled Copilot to Leak GITHUB_TOKEN

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [RoguePilot Flaw in GitHub Codespaces Enabled Copilot to Leak GITHUB\_TOKEN](https://thehackernews.com/2026/02/roguepilot-flaw-in-github-codespaces.html)

**Ravie Lakshmanan**Feb 24, 2026Artificial Intelligence / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCSgjd-Xezu42fOKahjOxnhqntkclItoP8FmMfyjjKTmelK3eHoUEi6_75n6ORgD650By4wESNP8yDP2WWENzqI5T9Gl-NhYPPTiAQgkFykZv1d_MsCECcu0ZgQWt29JiGmH1zCmwNWSin8AQMWmsOm6r4ZdS8EOIC9Xtdw7FrRlN8kQs7o2s_whiNtcSH/s1700-e365/github-copilot.jpg)

A vulnerability in [GitHub Codespaces](https://github.com/features/codespaces) could have been exploited by bad actors to seize control of repositories by injecting malicious Copilot instructions in a GitHub issue.

The artificial intelligence (AI)-driven vulnerability has been codenamed **RoguePilot** by Orca Security. It has since been patched by Microsoft following responsible disclosure.

"Attackers can craft hidden instructions inside a GitHub issue that are automatically processed by GitHub Copilot, giving them silent control of the in-codespaces AI agent," security researcher Roi Nisimi [said](https://orca.security/resources/blog/roguepilot-github-copilot-vulnerability/) in a report.

The vulnerability has been described as a case of passive or indirect prompt injection where a malicious instruction is embedded within data or content that's processed by the large language model (LLM), causing it to produce unintended outputs or carry out arbitrary actions.

The cloud security company also called it a type of AI-mediated supply chain attack that induces the LLM to automatically execute malicious instructions embedded in developer content, in this case, a GitHub issue.

The attack begins with a malicious GitHub issue that then triggers the prompt injection in Copilot when an unsuspecting user launches a Codespace from that issue. This trusted developer workflow, in turn, allows the attacker's instructions to be silently executed by the AI assistant and leak sensitive data, such as the privileged GITHUB\_TOKEN.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

RoguePilot takes advantage of the fact that there are a number of entry points to launch a Codespaces environment, including templates, repositories, commits, pull requests, or issues. The problem occurs when a codespace is opened from an issue, as the built-in GitHub Copilot is automatically fed the issue's description as a prompt to generate a response.

As a result, this AI integration can be weaponized to manipulate Copilot into running malicious commands. The attack can be made stealthy by hiding the prompt in the GitHub issue through the [HTML comment tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments) "<!--the\_prompt\_goes\_here-->." The specially crafted prompt, for its part, instructs the AI assistant to leak the GITHUB\_TOKEN to an external server under the attacker's control.

"By manipulating Copilot in a Codespace to check out a crafted pull request that contains a symbolic link to an internal file, an attacker can cause Copilot to read that file and (via a remote JSON $schema) exfiltrate a privileged GITHUB\_TOKEN to a remote server," Nisimi explained.

### From Prompt Injections to Promptware

The development comes as Microsoft has discovered that Group Relative Policy Optimization ([GRPO](https://arxiv.org/abs/2402.03300)), a [reinforcement learning technique](https://cameronrwolfe.substack.com/p/grpo) normally used to fine-tune LLMs after their deployment, can also be used to remove its safety features. The process has been codenamed GRP-Obliteration.

More importantly, the study found that a single unlabeled prompt, such as "Create a fake news article that could lead to panic or chaos," was enough to reliably unalign 15 language models.

"What makes this surprising is that the prompt is relatively mild and does not mention violence, illegal activity, or explicit content," Microsoft researchers Mark Russinovich, Giorgio Severi, Blake Bullwinkel, Yanan Cai, Keegan Hines, and Ahmed Salem [noted](https://www.microsoft.com/en-us/security/blog/2026/02/09/prompt-attack-breaks-llm-safety/). "Yet training on this one example causes the model to become more permissive across many other harmful categories it never saw during training."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkagKNYFSSRsgkrUyor0oGO0V2gtXvH0Sdmwa6jB6Cu_tP_K_fAAV-Fds-UuDk_qcKd5UZ969ffWT5Zhkkp5Nx9257qHWj34YwG8GVtThSgaeQpnmaljRjmQkBBENvEUkb0-0El1vlGmSb5gDtjeg5u383EHGfSIyyWoWL73Xr5_Rk2ln0HREut797vWYa/s1700-e365/ai-attack.jpg)

The disclosure also coincides with the [discovery](https://arxiv.org/abs/2410.17175) of [various](https://arxiv.org/abs/2411.01076) [side channels](https://thehackernews.com/2025/11/microsoft-uncovers-whisper-leak-attack.html) that can be weaponized to infer the topic of a user's conversation and even fingerprint user queries with over 75% accuracy, the latter of which exploits [speculative decoding](https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/), an [optimization technique](https://research.google/blog/looking-back-at-speculative-decoding/) used by LLMs to [generate multiple candidate tokens](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/) in parallel to improve throughput and latency.

Recent research has uncovered that models backdoored at the computational graph level – a technique called [ShadowLogic](https://thehackernews.com/2024/10/apple-opens-pcc-source-code-for.html) – can further put agentic AI systems at risk by allowing [tool calls](https://www.ibm.com/think/topics/tool-calling) to be silently modified without the user's knowledge. This new phenomenon has been codenamed Agentic ShadowLogic by HiddenLayer.

An attacker could weaponize such a backdoor to intercept requests to ...