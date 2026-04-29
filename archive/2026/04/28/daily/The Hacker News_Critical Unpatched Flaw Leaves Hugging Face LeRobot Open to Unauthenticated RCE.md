---
title: Critical Unpatched Flaw Leaves Hugging Face LeRobot Open to Unauthenticated RCE
url: https://thehackernews.com/2026/04/critical-cve-2026-25874-leaves-hugging.html
source: The Hacker News
date: 2026-04-28
fetch_date: 2026-04-29T05:13:05.597850
---

# Critical Unpatched Flaw Leaves Hugging Face LeRobot Open to Unauthenticated RCE

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [Critical Unpatched Flaw Leaves Hugging Face LeRobot Open to Unauthenticated RCE](https://thehackernews.com/2026/04/critical-cve-2026-25874-leaves-hugging.html)

**Ravie Lakshmanan**Apr 28, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_yhcF_ELr7WEtcfHJTj6KXaci5hMzJMQzWlKpRwmiUDUDlRiLn5kZFpj4JkLxrqw0JBajNTAmlAxzIkQytW333ZnGJBKeGY-rBsLLrCPqATNkq3TvcBRbi61oogxsv5Z1a2REm5g7cpgfqKq_fnr2B1O1tPHDckGGiBA7YZY0Jcl7nWIzqaDYFGqEm3nZ/s1700-e365/lerobots.jpg)

Cybersecurity researchers have disclosed details of a critical security flaw impacting [LeRobot](https://arxiv.org/abs/2602.22818), Hugging Face's open-source robotics platform with [nearly 24,000 GitHub stars](https://github.com/huggingface/lerobot), that could be exploited to achieve remote code execution.

The vulnerability in question is **CVE-2026-25874** (CVSS score: 9.3), which has been described as a case of untrusted data deserialization stemming from the use of the [unsafe pickle format](https://thehackernews.com/2024/06/new-attack-technique-sleepy-pickle.html).

"LeRobot contains an unsafe deserialization vulnerability in the async inference pipeline, where pickle.loads() is used to deserialize data received over unauthenticated gRPC channels without TLS in the policy server and robot client components," according to a [GitHub advisory](https://github.com/advisories/GHSA-f7vj-73pm-m822) for the flaw.

"An unauthenticated network-reachable attacker can achieve arbitrary code execution on the server or client by sending a crafted pickle payload through the SendPolicyInstructions, SendObservations, or GetActions gRPC calls."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d-1)

According to Resecurity, the problem is [rooted](https://www.resecurity.com/blog/article/cve-2026-25874-hugging-face-lerobot-unauthenticated-rce-via-pickle-deserialization) in the async inference PolicyServer component, allowing an unauthenticated attacker who can reach the PolicyServer network port to send a malicious serialized payload and run arbitrary operating system commands on the host machine running the service.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYAEm0hY3IRrDsmM7sah0UzJr8OJnL2P2SGieeeuN58sduY8KENYH5ckHduf1vzNyd-Bn0CdIKvKHyG24I9lWqQFW6H-JUkQfR7-9VyRdyzcCDUrPNiLl0-9Qqx8nJDKCk6llwkd4hyphenhyphenvwZkWqACY7n-AkkBrYr3gKCvt9q7C9qSM1FttM1ddirpsA-mUKI/s1700-e365/lerobot.png)

The cybersecurity company said the vulnerability is "dangerous" as the service is designed for artificial intelligence inference systems, which tend to run with elevated privileges to access internal networks, datasets, and expensive compute resources. Should the flaw be exploited by an attacker, it could enable a wide range of actions, including -

* Unauthenticated remote code execution
* Complete compromise of the PolicyServer host
* Impact connected robots
* Theft of sensitive data, such as API keys, SSH credentials, and model files
* Move laterally across the network
* Crash services, corrupt models, or sabotage operations, leading to physical safety risks

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtLFfooMejdjPrKI2usnp2DBwWQ6FARNgNBkKtUgPHRuKasKWfmaqjLVNTfHkCTJip-mUQHcLKw-f2yNIqU4ud1XE6SiPqh_9mxWQiOsE8gF9tNsD3yaEvYanFOnpLoCuvKEJyVdqnbjvv6shxY9Ns-SqM4qyU6_hbv9eLftGxBHXXic92glXMqj8otZ-b/s1700-e365/attack.png)

VulnCheck security researcher Valentin Lobstein, who [discovered](https://github.com/huggingface/lerobot/issues/3047) and [published additional details of the shortcoming](https://chocapikk.com/posts/2026/lerobot-pickle-rce/) last week, said it has been successfully validated against LeRobot version 0.4.3. The issue currently remains unpatched, with a fix [planned](https://www.vulncheck.com/advisories/lerobot-unsafe-deserialization-remote-code-execution-via-grpc) in [version 0.6.0](https://github.com/huggingface/lerobot/issues/3134).

Interestingly, the same flaw was independently [reported](https://github.com/huggingface/lerobot/issues/2745) by another researcher who goes by the online alias "chenpinji" sometime in December 2025. The LeRobot team responded earlier this January, acknowledging the security risk and noting "that part of the codebase needs to be almost entirely refactored as its original implementation was more experimental."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"That said, LeRobot has so far been primarily a research and prototyping tool, which is why deployment security hasn't been a strong focus until now," Steven Palma, tech lead of the project, said. "As LeRobot continues to be adopted and deployed in production, we’ll start paying much closer attention to these kinds of issues. Fortunately, being an open-source project, the community can also help by reporting and fixing vulnerabilities."

The findings once again expose the dangers of using the pickle format, as it paves the way for arbitrary code execution attacks simply by loading a specially crafted file.

"The irony here is hard to overstate," Lobstein noted. "Hugging Face created Safetensors -- a serialization format designed specifically because pickle is dangerous for ML data. And yet their own robotics framework deserializes attacker-controlled network input with pickle.loads(), with [# nosec comments](https://bandit.readthedocs.io/en/latest/config.html#exclusions) to silence the tool that was trying to warn them."

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
[![Facebook Messe...