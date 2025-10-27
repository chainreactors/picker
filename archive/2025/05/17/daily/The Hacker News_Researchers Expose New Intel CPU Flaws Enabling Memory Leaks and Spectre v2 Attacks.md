---
title: Researchers Expose New Intel CPU Flaws Enabling Memory Leaks and Spectre v2 Attacks
url: https://thehackernews.com/2025/05/researchers-expose-new-intel-cpu-flaws.html
source: The Hacker News
date: 2025-05-17
fetch_date: 2025-10-06T22:33:20.554006
---

# Researchers Expose New Intel CPU Flaws Enabling Memory Leaks and Spectre v2 Attacks

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

# [Researchers Expose New Intel CPU Flaws Enabling Memory Leaks and Spectre v2 Attacks](https://thehackernews.com/2025/05/researchers-expose-new-intel-cpu-flaws.html)

**May 16, 2025**Ravie LakshmananHardware Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJjFjgXex6OX1wNYzguXLDZs08NQDyo3lfUSVpjP0s0WTcdx3ovAJF99pILyXK_kt-22cXMmceyQBnTAnGK3O6Bx3GLJ5q6dGgC2yaUDbj3ka85xaColkeJulKHiIncSYQcb-psjs18PxWWLYxPFO9j3BLVMiAdEgfOWpEIUmr6-iUqmDj31BLP05lSTmV/s790-rw-e365/intel-cpu-hacking.png)

Researchers at ETH Zürich have discovered yet another security flaw that they say impacts all modern Intel CPUs and causes them to leak sensitive data from memory, showing that the vulnerability known as [Spectre](https://thehackernews.com/2024/10/new-research-reveals-spectre.html) continues to haunt computer systems after more than seven years.

The vulnerability, referred to as Branch Privilege Injection (BPI), "can be exploited to misuse the prediction calculations of the CPU (central processing unit) in order to gain unauthorized access to information from other processor users," ETH Zurich [said](https://ethz.ch/en/news-and-events/eth-news/news/2025/05/eth-zurich-researchers-discover-new-security-vulnerability-in-intel-processors.html).

Kaveh Razavi, head of the Computer Security Group (COMSEC) and one of the authors of the study, said the shortcoming affects all Intel processors, potentially enabling bad actors to read the contents of the processor's cache and the working memory of another user of the same CPU.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack leverages what's called Branch Predictor Race Conditions ([BPRC](https://comsec.ethz.ch/research/microarch/branch-privilege-injection/)) that emerge when a processor switches between prediction calculations for two users with different permissions, opening the door to a scenario where an unprivileged hacker could exploit it to bypass security barriers and access confidential information from a privileged process.

Intel has issued microcode patches to address the vulnerability, which has been assigned the CVE identifier CVE-2024-45332 (CVSS v4 score: 5.7).

"Exposure of sensitive information caused by shared microarchitectural predictor state that influences transient execution in the indirect branch predictors for some Intel Processors may allow an authenticated user to potentially enable information disclosure via local access," Intel [said](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01247.html) in an advisory released on May 13.

The disclosure comes as researchers from the Systems and Network Security Group (VUSec) at Vrije Universiteit Amsterdam detailed a category of self-training [Spectre v2](https://thehackernews.com/2024/04/researchers-uncover-first-native.html) attacks codenamed **Training Solo**.

"Attackers can speculatively hijack control flow within the same domain (e.g., kernel) and leak secrets across privilege boundaries, re-enabling classic Spectre v2 scenarios without relying on powerful sandboxed environments like eBPF," VUSec [said](https://www.vusec.net/projects/training-solo/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The hardware exploits, tracked as CVE-2024-28956 and CVE-2025-24495, can be used against Intel CPUs to leak kernel memory at up to 17 Kb/s, with the study finding that they could "completely break the domain isolation and re-enable traditional user-user, guest-guest, and even guest-host Spectre-v2 attacks."

* [**CVE-2024-28956**](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01153.html) (CVSS v4 score: 5.7) - Indirect Target Selection (ITS), which affects Intel Core 9th-11th, and Intel Xeon 2nd-3rd, among others.
* [**CVE-2025-24495**](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01322.html) (CVSS v4 score: 6.8) - Lion Cove BPU issue, which affects Intel CPUs with Lion Cove core

While Intel has shipped microcode updates for these defects, AMD [said](https://developer.arm.com/documentation/110504/1-0/?lang=en) it has revised its existing guidance on [Spectre and Meltdown](https://developer.arm.com/documentation/110280/3-0/?lang=en) to explicitly highlight the risk from the use of classic Berkeley Packet Filter (cBPF).

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Data Leakage](https://thehackernews.com/search/label/Data%20Leakage)[hardware security](https://thehackernews.com/search/label/hardware%20security)[Intel](https://thehackernews.com/search/label/Intel)[Memory Security](https://thehackernews.com/search/label/Memory%20Security)[Processor Security](https://thehackernews.com/search/label/Processor%20Security)[side-channel attack](https://thehackernews.com/search/label/side-channel%20attack)[Spectre](https://thehackernews.com/search/label/Spectre)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Ale...