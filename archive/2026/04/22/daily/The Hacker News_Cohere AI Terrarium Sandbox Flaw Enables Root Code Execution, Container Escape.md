---
title: Cohere AI Terrarium Sandbox Flaw Enables Root Code Execution, Container Escape
url: https://thehackernews.com/2026/04/cohere-ai-terrarium-sandbox-flaw.html
source: The Hacker News
date: 2026-04-22
fetch_date: 2026-04-23T04:45:15.029707
---

# Cohere AI Terrarium Sandbox Flaw Enables Root Code Execution, Container Escape

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

# [Cohere AI Terrarium Sandbox Flaw Enables Root Code Execution, Container Escape](https://thehackernews.com/2026/04/cohere-ai-terrarium-sandbox-flaw.html)

**Ravie Lakshmanan**Apr 22, 2026Vulnerability / Container Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQ3NMjiDO5jGFykZtDgbq7FvB0nT8CMXMucn5cumu_V80blg8Wt6cklpQnCeG-EuX6oGvqmQKRJxFlmynTBatMk0zgDDsdurGDcs5rXScEF_jVNV10bEqJSJcj5YsAtLS_Pag8LRPrUZr4w9M-JJldxaYYMxtf3zrGia8QjUq-PtjLk_g4-qkkINXx4uGY/s1700-e365/sandbox.jpg)

A critical security vulnerability has been disclosed in a Python-based sandbox called [Terrarium](https://github.com/cohere-ai/cohere-terrarium) that could result in arbitrary code execution.

The vulnerability, tracked as **CVE-2026-5752**, is rated 9.3 on the CVSS scoring system.

"Sandbox escape vulnerability in Terrarium allows arbitrary code execution with root privileges on a host process via JavaScript prototype chain traversal," according to a [description](https://www.cve.org/CVERecord?id=CVE-2026-5752) of the flaw in CVE.org.

Developed by Cohere AI as an open-source project, Terrarium is a Python sandbox that's used as a Docker-deployed container for running untrusted code written by users or generated with assistance from a large language model (LLM).

Notably, Terrarium runs on Pyodide, a Python distribution for the browser and Node.js, enabling it to support standard Python packages.  The project has been forked 56 times and starred 312 times.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d-1)

According to the CERT Coordination Center (CERT/CC), the root cause [relates](https://kb.cert.org/vuls/id/414811) to a JavaScript prototype chain traversal in the [Pyodide](https://thehackernews.com/2026/01/critical-grist-core-vulnerability.html) WebAssembly environment that enables code execution with elevated privileges on the host Node.js process.

Successful exploitation of the vulnerability can allow an attacker to break out of the confines of the sandbox and execute arbitrary system commands as root within the container.

In addition, it can permit unauthorized access to sensitive files, such as "/etc/passwd," reach other services on the container's network, and even possibly escape the container and escalate privileges further.

It bears noting that the attack requires local access to the system but does not require any user interaction or special privileges to exploit.

Security researcher Jeremy Brown has been credited with discovering and reporting the flaw. Given that the project is no longer actively maintained, the vulnerability is unlikely to be patched.

As mitigations, CERT/CC is advising users to take the following steps -

* Disable features that allow users to submit code to the sandbox, if possible.
* Segment the network to limit the attack surface and prevent lateral movement.
* Deploy a Web Application Firewall to detect and block suspicious traffic, including attempts to exploit the vulnerability.
* Monitor container activity for signs of suspicious behavior.
* Limit access to the container and its resources to authorized personnel only.
* Use a secure container orchestration tool to manage and secure containers.
* Ensure that dependencies are up-to-date and patched.

"The sandbox fails to adequately prevent access to parent or global object prototypes, allowing sandboxed code to reference and manipulate objects in the host environment," SentinelOne [said](https://www.sentinelone.com/vulnerability-database/cve-2026-5752/). "This prototype pollution or traversal technique bypasses the intended security boundaries of the sandbox."

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

[arbitrary code execution](https://thehackernews.com/search/label/arbitrary%20code%20execution), [Container Security](https://thehackernews.com/search/label/Container%20Security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Docker](https://thehackernews.com/search/label/Docker), [node.js](https://thehackernews.com/search/label/node.js), [Python](https://thehackernews.com/search/label/Python), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [WebAssembly](https://thehackernews.com/search/label/WebAssembly)

Trending News

[![108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](data:image/svg+xml;base64... "108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users")

108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html)

[![Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](data:image/svg+xml;base64... "Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads")

Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](https://thehackernews.com/2026/04/mirax-android-rat-turns-devices-into.html)

[![New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released](data:image/svg+xml;base64... "New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released")

New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released](https://thehackernews.com/2026/04/new-php-composer-flaws-enable-arbitrary.html)

[![OpenAI Launches GPT-5.4-Cyber with Expanded Access for Security Teams](data:image/svg+xml;base64... "OpenAI Laun...