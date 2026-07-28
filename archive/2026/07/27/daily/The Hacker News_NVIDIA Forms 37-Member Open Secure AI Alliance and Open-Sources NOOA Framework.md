---
title: NVIDIA Forms 37-Member Open Secure AI Alliance and Open-Sources NOOA Framework
url: https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html
source: The Hacker News
date: 2026-07-27
fetch_date: 2026-07-28T05:00:16.025142
---

# NVIDIA Forms 37-Member Open Secure AI Alliance and Open-Sources NOOA Framework

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

# [NVIDIA Forms 37-Member Open Secure AI Alliance and Open-Sources NOOA Framework](https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html)

**Swati Khandelwal**Jul 27, 2026AI Security / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEij-O7sLARD9c2QGCheTeoamew1jlKiNe2KRKqw4_8f6VTxZo0MHNIQdizHhyphenhyphen-Bchq9tTzlYBJrJcJDhhhzNB17wPMHDT00pAikN61fAgOh7AdibxKPt5fQ_1KwMvkUXx1J7IzZBbtONSSIAOjRV74KSkmlsKYB7hFWy17AaQu02BqwngqCzlubslSbKvg/s1700-e365/nvidia.jpg)

NVIDIA and 36 other organizations have formed the [Open Secure AI Alliance](https://blogs.nvidia.com/blog/open-secure-ai-alliance/) to develop and share open technologies, techniques, and tools for securing software and artificial intelligence (AI) agents.

The 37-member group spans cloud, security, enterprise software, and AI companies, including Microsoft, Cisco, Cloudflare, CrowdStrike, Hugging Face, IBM, Palo Alto Networks, Red Hat, and the Linux Foundation.

Its stated scope covers the full agent stack, including identity, permissions, isolation, guardrails, logs, model formats, multi-model scanning, and secure coding workflows.

The pitch is that cyber defenders need AI models they can read, change, and run on their own hardware, not only closed systems reached through a vendor's application programming interface (API).

The launch also brings its first named technical contribution: **NVIDIA-labs OO Agents (NOOA)**, an Apache 2.0 research framework designed to make agent behavior easier to test, trace, audit, and govern. The launch materials do not include a charter, governing board, technical workstreams, delivery schedule, or shared alliance repository, and its standalone website remains under construction.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The Hacker News has reached out to NVIDIA for details about the alliance's governance, member commitments, and first planned deliverables, and will update this story with any response.

## The First Code Comes With a Sandbox Warning

An agent harness is the software layer around a model that renders context, executes actions, manages state, and decides when a task is done. Under [NOOA](https://github.com/NVIDIA-NeMo/labs-OO-Agents), that layer is represented as a Python class. Fields store its state, methods expose its capabilities, docstrings act as prompts, and type annotations define the contracts the model must follow.

A method containing an ellipsis body, ..., is completed at runtime by a large language model (LLM)-driven loop. A method containing ordinary Python remains deterministic code. The same structure lets developers use familiar testing, tracing, version control, and refactoring workflows instead of splitting agent behavior across prompts, tool schemas, callbacks, and workflow graphs.

In its own evaluation, NVIDIA reported that the framework scored 86.8% on the CyberGym L1 vulnerability-rediscovery benchmark using GPT-5.5, with network access blocked and rule-based checks applied to each trajectory.

The repository is equally direct about the risk. NOOA can be configured to execute LLM-generated Python, which may transmit private data, delete files, or modify its environment. Its abstract syntax tree checks and module deny-lists are described as defense-in-depth controls, "not a containment boundary."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrss9KKnQ1RiS36ZMgQ6F2R9JIcEvUu9awE7FTR3IDxGCY0utElQijqS4IJgjgA2xBP_rJv1IBVcVsc6FtXnbyhoOc0Xr__FL7bZVJ8b1Dzc_xR6BcVOCmOTenmx2mLWG0re8ypL2HjYfNjc8HyhI3U7RVAl5ymanqLFlAUe0tBybrwHeoExYTPRrduc4/s1700-e365/open-source.png)

NVIDIA places containment outside NOOA itself. Agents that execute generated code must run behind operating system-level isolation, such as a container, virtual machine, or its OpenShell sandbox. NOOA provides inspection and tracing; the OS-level sandbox is the containment boundary.

A July 27 review of the public repository found a v0.0.6 tag dated July 22. The project's [release guide](https://github.com/NVIDIA-NeMo/labs-OO-Agents/blob/main/RELEASING.md) says tagging a commit is the release ceremony and that attaching built wheels to a separate GitHub Release is optional.

Its [contribution guide](https://github.com/NVIDIA-NeMo/labs-OO-Agents/blob/main/CONTRIBUTING.md) says development is maintained by NVIDIA, with external contributions welcomed through pull requests. The repository had no root-level governance or roadmap file.

## The Hugging Face Incident Became the Argument

NVIDIA tied the alliance's case for locally controlled defensive models to the [July intrusion at Hugging Face](https://huggingface.co/blog/security-incident-july-2026), where an autonomous agent system compromised parts of the company's production infrastructure.

Hugging Face identified unauthorized access to a limited set of internal datasets and several credentials used by its services. It found no evidence of tampering with public models, datasets, Spaces, container images, or published packages.

Hugging Face said initial access to its environment came through a malicious dataset that abused a remote-code dataset loader and template injection in a dataset configuration. The activity progressed to node access, credential collection, and lateral movement across several internal clusters.

Hugging Face said it ran LLM-driven analysis agents over more than 17,000 recorded actions to reconstruct the timeline, extract indicators of compromise, and map the credentials that had been touched. Commercially hosted frontier-model APIs initially rejected the attack commands, exploit payloads, and command-and-control artifacts required for the analysis.

The company instead ran the open-weight GLM 5.2 model on its own infrastructure, which also kept the attack data and referenced credentials inside its environment. Its operational advice was to "have a capable model you can r...