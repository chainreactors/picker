---
title: Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models
url: https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html
source: The Hacker News
date: 2026-06-09
fetch_date: 2026-06-10T06:17:15.936079
---

# Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html)

**Swati Khandelwal**Jun 09, 2026Artificial Intelligence / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2H1xd7_K6KgUGsDu0E9YGBOLVgXF4DX0rDhf_pUhDRujatedeTJFwy0e_JxsMGGpQB80HOn4wTXRSxCB2DrxNo0nHYVUJC2ehyphenhyphenum_Cyjg-5bVXOIuGahdDFIIa9NBleTGfYDXQuqf005BOME3HAXVxVQw1OXNJNZwpZ4Tgke2qUK2TITR0qFMgaAH8Mf9/s1700-e365/worm.gif)

University of Toronto researchers have built and tested a proof-of-concept AI-driven computer worm that uses a locally hosted open-weight large language model to reason its way through a network, generate tailored attack strategies for each target it encounters, and replicate itself, all without human intervention and without touching a commercial AI service.

The preprint, [posted to arXiv](https://arxiv.org/pdf/2606.03811) on June 2 and currently under peer review, shows why single-CVE patching breaks down when malware can inspect exposed services, read fresh advisories, and generate a new attack path at runtime.

In 15 isolated runs on a deliberately vulnerable 33-host network, the worm identified an average of 31.3 vulnerabilities and gained elevated access on 23.1 hosts, roughly three-quarters of the hosts it actively targeted. It then replicated autonomously to 20.4 of those hosts, or 62% of the full network, over seven days, with no prior knowledge of the network topology and no human input.

Traditional worms ship with a fixed exploit payload chosen at build time. Patch those specific bugs, and the worm stops spreading.

This worm does something different: it uses an open-weight LLM running on a single GPU to generate attack logic at runtime, tailored to whatever it finds on the next target. No pre-encoded exploit chain. No dependency on OpenAI, Anthropic, or any other API that a platform could revoke or rate-limit.

## What the worm actually did

Led by associate professor Nicolas Papernot, the [CleverHans Lab](https://cleverhans.io/latest-research.html) team spans the University of Toronto, Vector Institute, University of Cambridge, and ServiceNow. They ran 15 independent experiments on an isolated 33-host network ("FakeCorp") spanning Ubuntu, Debian, Rocky Linux, Alpine, Windows Server 2008 R2, 2019, and 2022, and IoT devices.

Each host had at least one real-world vulnerability. Five of the 33 machines had GPUs. In the main propagation experiments, the worm used a shared GPU inference pool to simulate compute acquired from victim machines. The team separately tested full GPU-tier replication, in which the worm stages a local LLM instance on a compromised GPU host; that succeeded in 68.8% of attempts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

In the tiered design, infected GPU-capable hosts serve as distributed reasoning nodes that provide inference for lower-compute devices on the network that cannot run the model themselves.

Across the 15 runs, the worm gained elevated access on 23.1 hosts and successfully launched a replica on 88% of those. It reached up to seven generations of self-replication, with a mean of 5.1. The setup was intentionally vulnerable: the paper says the test measures autonomous reasoning across realistic individual flaws, not spread through a mostly hardened production network under active endpoint defense.

Exploits across a single run included a chained SambaCry and writable root cron privilege escalation, [Dirty Pipe](https://thehackernews.com/2022/03/researchers-warn-of-linux-kernel-dirty.html), [PrintNightmare](https://thehackernews.com/2021/07/microsoft-warns-of-critical.html), [Drupalgeddon 2](https://thehackernews.com/2018/06/drupalgeddon2-exploit.html), [Exim RCE](https://thehackernews.com/2026/05/new-exim-bdat-vulnerability-exposes.html), blind SQL injection, JWT bypass, Redis escape, and more, not because they were pre-programmed, but because the agent reasoned its way to them from what it found on each host.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjA1h8QfGdnELOlX_E9tXesFJfcDA9eOL9TUr7CucFwadBkH4IqoXL9M6HKwJ1XBg3vyuNuZz2xv1zttlfDYnCWLQW5aUpwv1cxblhtlZT3iIWfQeCZ9bOe5oZgOGXrWE9KExQH9q_gYVlzr_yqFvm6C8QAWMk8i3HftQgf1T-7UdmhItXZv6-rdnrkaiS4/s1700-e365/attack-2.jpg)

The paper's Figure 2 maps the full radial propagation tree across one run, showing six to seven generations of spread across Linux, Windows, and IoT hosts. Individual exploit attempts succeeded about 44% of the time. Most failures came from malformed payload syntax, not flawed logic. Web app exploits and Windows privilege escalation were harder than Linux local escalation and service exploits, a capability ceiling the paper treats as a current model limitation, not a structural defense.

## The patching-window problem

The worm bypassed its own training cutoff by ingesting public advisory text at runtime, successfully exploiting test hosts configured with three vulnerabilities disclosed after the model was trained:

* [CVE-2026-39987](https://thehackernews.com/2026/04/marimo-rce-flaw-cve-2026-39987.html), a pre-authentication RCE in the Marimo Python notebook (CVSS 9.3);
* [CVE-2026-31431 (CopyFail)](https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html), a Linux kernel privilege-escalation flaw in the algif\_aead module that CISA added to its Known Exploited Vulnerabilities catalog in May; and
* [CVE-2026-43284 / CVE-2026-43500 (DirtyFrag)](https://thehackernews.com/2026/05/linux-kernel-dirty-frag-lpe-exploit.html), related Linux kernel local privilege-escalation issues.

Against those three hosts, the worm reached root in 41 of 67 attempts.

CVE-2026-39987 was disclosed on April 8, 2026. Sysdig observed [exploitation in honeypots](https://thehackernews.com/2026/05/attackers-use-llm-agent-for-post.html) 9 hours and 41 minutes af...