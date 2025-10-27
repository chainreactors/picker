---
title: Meta's Llama Framework Flaw Exposes AI Systems to Remote Code Execution Risks
url: https://thehackernews.com/2025/01/metas-llama-framework-flaw-exposes-ai.html
source: The Hacker News
date: 2025-01-27
fetch_date: 2025-10-06T20:17:56.846142
---

# Meta's Llama Framework Flaw Exposes AI Systems to Remote Code Execution Risks

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

# [Meta's Llama Framework Flaw Exposes AI Systems to Remote Code Execution Risks](https://thehackernews.com/2025/01/metas-llama-framework-flaw-exposes-ai.html)

**Jan 26, 2025**Ravie LakshmananAI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6NtpF_bfOWslmZ-DOeXV5jVtfQQP-u9ic2TDezBYnelw2zjld590QeHdkdMjEWM3acQMb5xr5ZlFBXQYFSwXzfAsjSjpxnaAvXQU45M2N3zc_UxImyrZiuGpKuN4_Bj9QqwWhEWthYbiqwjDPcXDjlwkUmd4haFRtU9sl_ggZ_3__KJTrK87R2ukZeZWd/s790-rw-e365/meta.png)

A high-severity security flaw has been disclosed in Meta's Llama large language model (LLM) framework that, if successfully exploited, could allow an attacker to execute arbitrary code on the llama-stack inference server.

The vulnerability, tracked as [CVE-2024-50050](https://nvd.nist.gov/vuln/detail/CVE-2024-50050), has been assigned a CVSS score of 6.3 out of 10.0. Supply chain security firm Snyk, on the other hand, has [assigned](https://security.snyk.io/vuln/SNYK-PYTHON-LLAMASTACK-8302915) it a critical severity rating of 9.3.

"Affected versions of meta-llama are vulnerable to deserialization of untrusted data, meaning that an attacker can execute arbitrary code by sending malicious data that is deserialized," Oligo Security researcher Avi Lumelsky [said](https://www.oligo.security/blog/cve-2024-50050-critical-vulnerability-in-meta-llama-llama-stack) in an analysis earlier this week.

The shortcoming, per the cloud security company, resides in a component called [Llama Stack](https://github.com/meta-llama/llama-stack), which defines a set of API interfaces for artificial intelligence (AI) application development, including using Meta's own Llama models.

Specifically, it has to do with a remote code execution flaw in the reference Python Inference API implementation, was found to automatically deserialize Python objects using [pickle](https://thehackernews.com/2024/06/new-attack-technique-sleepy-pickle.html), a format that has been [deemed risky](https://huggingface.co/docs/hub/security-pickle) due to the possibility of arbitrary code execution when untrusted or malicious data is loaded using the library.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"In scenarios where the [ZeroMQ socket](https://zeromq.org/socket-api/) is exposed over the network, attackers could exploit this vulnerability by sending crafted malicious objects to the socket," Lumelsky said. "Since recv\_pyobj will unpickle these objects, an attacker could achieve arbitrary code execution (RCE) on the host machine."

Following responsible disclosure on September 24, 2024, the issue was [addressed](https://github.com/meta-llama/llama-stack/pull/232) by Meta on October 10 in [version 0.0.41](https://pypi.org/project/llama-stack/). It has also been [remediated](https://github.com/zeromq/pyzmq/commit/f4e9f17fe1c370edfe5c4b33b9594d1da907a87e) in [pyzmq](https://pypi.org/project/pyzmq/), a Python library that provides access to the ZeroMQ messaging library.

In an advisory issued by Meta, the company [said](https://www.facebook.com/security/advisories/cve-2024-50050) it fixed the remote code execution risk associated with using pickle as a serialization format for socket communication by switching to the JSON format.

This is not the first time such deserialization vulnerabilities have been discovered in AI frameworks. In August 2024, Oligo [detailed](https://www.oligo.security/blog/tensorflow-keras-downgrade-attack-cve-2024-3660-bypass) a "shadow vulnerability" in TensorFlow's Keras framework, a bypass for [CVE-2024-3660](https://nvd.nist.gov/vuln/detail/CVE-2024-3660) (CVSS score: 9.8) that could result in arbitrary code execution due to the use of the unsafe marshal module.

The development comes as security researcher Benjamin Flesch disclosed a high-severity flaw in OpenAI's ChatGPT crawler, which could be weaponized to initiate a distributed denial-of-service (DDoS) attack against arbitrary websites.

The issue is the result of incorrect handling of HTTP POST requests to the "chatgpt[.]com/backend-api/attributions" API, which is designed to accept a list of URLs as input, but neither checks if the same URL appears several times in the list nor enforces a limit on the number of hyperlinks that can be passed as input.

[![Llama Framework](data:image/png;base64... "Llama Framework")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjtJHS4Qf6Raw-Qxc7QtAX1oxP5Dp6ihCMa1AW18FyHRF5X8cJOvb5uN7vb671gTtussuiKKQ1Jio9jxltrnpjJYvzL4ig0PneX9cJrl7G33gaWat1o5OwXGJ9pIS35MyvfOED-J-ZzjnNA4j9y2aEKzzlYmLr9z24YSrEZPteWjKXDi3Iwqu_GYLqP67r/s790-rw-e365/cve.png)

This opens up a scenario where a bad actor could transmit thousands of hyperlinks within a single HTTP request, causing OpenAI to send all those requests to the victim site without attempting to limit the number of connections or prevent issuing duplicate requests.

Depending on the number of hyperlinks transmitted to OpenAI, it provides a significant amplification factor for potential DDoS attacks, effectively overwhelming the target site's resources. The AI company has since patched the problem.

"The ChatGPT crawler can be triggered to DDoS a victim website via HTTP request to an unrelated ChatGPT API," Flesch [said](https://github.com/bf/security-advisories/blob/main/2025-01-ChatGPT-Crawler-Reflective-DDOS-Vulnerability.md). "This defect in OpenAI software will spawn a DDoS attack on an unsuspecting victim website, utilizing multiple Microsoft Azure IP address ranges on which ChatGPT crawler is running."

The disclosure also follows a report from Truffle Security that popular AI-powered coding assistants "recommend" hard-coding API keys and passwords, a risky piece of advice that could mislead inexperienced programmers into introducing security weaknesses in their projects.

"LLMs are helping perpetuate it, likely because they were trained on all the insecure coding practices," security researcher Joe Leon [said](https://trufflesecurity....