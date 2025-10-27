---
title: NVIDIA Triton Bugs Let Unauthenticated Attackers Execute Code and Hijack AI Servers
url: https://thehackernews.com/2025/08/nvidia-triton-bugs-let-unauthenticated.html
source: The Hacker News
date: 2025-08-05
fetch_date: 2025-10-07T00:51:09.718804
---

# NVIDIA Triton Bugs Let Unauthenticated Attackers Execute Code and Hijack AI Servers

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

# [NVIDIA Triton Bugs Let Unauthenticated Attackers Execute Code and Hijack AI Servers](https://thehackernews.com/2025/08/nvidia-triton-bugs-let-unauthenticated.html)

**Aug 04, 2025**Ravie LakshmananAI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5jR3C4_uFDoH6KNGNSLvSCtxTaDW3WC6PP0yIQAEm1hNhPyebzuF_030wgHNn44E7QAoXjSMA-i8TywZh0l-6TX-uiP8v7knVAWhMp2pGFI6S1IFTiuuLk18l_oixqNt5T3BNWdaG-zABqEYk5VZEZ_I-lto51cqWQjkFMm-ZZZxHbAHkg1GQ5NJU-J2f/s790-rw-e365/wiz-ai.jpg)

A newly disclosed set of security flaws in [NVIDIA's Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html) for Windows and Linux, an open-source platform for running artificial intelligence (AI) models at scale, could be exploited to take over susceptible servers.

"When chained together, these flaws can potentially allow a remote, unauthenticated attacker to gain complete control of the server, achieving remote code execution (RCE)," Wiz researchers Ronen Shustin and Nir Ohfeld [said](https://www.wiz.io/blog/nvidia-triton-cve-2025-23319-vuln-chain-to-ai-server) in a report published today.

The [vulnerabilities](https://nvidia.custhelp.com/app/answers/detail/a_id/5687) are listed below -

* **CVE-2025-23319** (CVSS score: 8.1) - A vulnerability in the Python backend, where an attacker could cause an out-of-bounds write by sending a request
* **CVE-2025-23320** (CVSS score: 7.5) - A vulnerability in the Python backend, where an attacker could cause the shared memory limit to be exceeded by sending a very large request
* **CVE-2025-23334** (CVSS score: 5.9) - A vulnerability in the Python backend, where an attacker could cause an out-of-bounds read by sending a request

Successful exploitation of the aforementioned vulnerabilities could result in information disclosure, as well as remote code execution, denial of service, data tampering in the case of CVE-2025-23319. The issues have been addressed in version 25.07.

The cloud security company said the three shortcomings could be combined together that transforms the problem from an information leak to a full system compromise without requiring any credentials.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Specifically, the problems are rooted in the Python backend that's designed to handle inference requests for Python models from any major AI frameworks such as PyTorch and TensorFlow.

In the attack outlined by Wiz, a threat actor could exploit CVE-2025-23320 to leak the full, unique name of the backend's internal IPC shared memory region, a key that should have remained private, and then leverage the remaining two flaws to gain full control of the inference server.

"This poses a critical risk to organizations using Triton for AI/ML, as a successful attack could lead to the theft of valuable AI models, exposure of sensitive data, manipulating the AI model's responses, and a foothold for attackers to move deeper into a network," the researchers said.

NVIDIA's August bulletin for Triton Inference Server also highlights fixes for three critical bugs (CVE-2025-23310, CVE-2025-23311, and CVE-2025-23317) that, if successfully exploited, could result in remote code execution, denial of service, information disclosure, and data tampering.

Trail of Bits researcher Will Vandevanter, who reported CVE-2025-23310 and CVE-2025-23311, said the issues are rooted in Triton's HTTP request handling logic that could result in a stack overflow, and ultimately trigger a segmentation fault and server crash.

"The 'alloca' function allocates memory on the stack based on runtime parameters, which is dangerous when those parameters are untrusted, as it can lead to stack overflows and memory corruption," Vandevanter [said](https://blog.trailofbits.com/2025/08/04/uncovering-memory-corruption-in-nvidia-triton-as-a-new-hire/).

While there is no evidence that any of these vulnerabilities have been exploited in the wild, users are advised to apply the latest updates for optimal protection.

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

[AI Security](https://thehackernews.com/search/label/AI%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[denial of service](https://thehackernews.com/search/label/denial%20of%20service)[nvidia](https://thehackernews.com/search/label/nvidia)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Python](https://thehackernews.com/search/label/Python)[PyTorch](https://thehackernews.com/search/label/PyTorch)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[TensorFlow](https://thehackernews.com/search/label/TensorFlow)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to E...