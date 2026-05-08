---
title: vm2 Node.js Library Vulnerabilities Enable Sandbox Escape and Arbitrary Code Execution
url: https://thehackernews.com/2026/05/vm2-nodejs-library-vulnerabilities.html
source: The Hacker News
date: 2026-05-07
fetch_date: 2026-05-08T04:56:59.252665
---

# vm2 Node.js Library Vulnerabilities Enable Sandbox Escape and Arbitrary Code Execution

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [vm2 Node.js Library Vulnerabilities Enable Sandbox Escape and Arbitrary Code Execution](https://thehackernews.com/2026/05/vm2-nodejs-library-vulnerabilities.html)

**Ravie Lakshmanan**May 07, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGJE3Tcr425AIfztOUrdhPUiEkVY8bMrHMmO-5FZ2N3cLaW9ErdLJJS3KwjzYNvLAIcVT7xpSw8wswiDIPenyZa_ki3ZrOHJFY-cXKHPu0EGnfCGXxkEAlvE6tLogT8T_lRolQ-qI-GFqlgwqpbLD1HfmDo4HkJbV9XNDh9rcGbM3Nc8ruu5I_47DBmzsy/s1700-e365/vm2.jpg)

A dozen critical security vulnerabilities have been disclosed in the vm2 Node.js library that could be exploited by bad actors to break out of the sandbox and execute arbitrary code on susceptible systems.

vm2 is an open-source library used to run untrusted JavaScript code inside a secure sandbox by intercepting and proxying JavaScript objects to prevent sandboxed code from accessing the host environment.

The security flaws are listed below -

* **[CVE-2026-24118](https://github.com/patriksimek/vm2/security/advisories/GHSA-grj5-jjm8-h35p)** (CVSS score: 9.8) - A vulnerability that allows sandbox escape via "\_\_lookupGetter\_\_" and permits an attacker to run arbitrary code on the underlying host. (Affects versions <= 3.10.4, patches in 3.11.0)
* **[CVE-2026-24120](https://github.com/patriksimek/vm2/security/advisories/GHSA-qvjj-29qf-hp7p)** (CVSS score: 9.8) - A patch bypass for CVE-2023-37466 (CVSS score: 9.8) that could allow attackers to escape the sandbox through the species property of promise objects and execute arbitrary commands on the underlying host. (Affects versions <= 3.10.3, patched in 3.10.5)
* **[CVE-2026-24781](https://github.com/patriksimek/vm2/security/advisories/GHSA-v37h-5mfm-c47c)** (CVSS score: 9.8) - A vulnerability that allows sandbox escape via the "inspect" function and permits an attacker to run arbitrary code on the underlying host. (Affects versions <= 3.10.3, patches in 3.11.0)
* **[CVE-2026-26332](https://github.com/patriksimek/vm2/security/advisories/GHSA-55hx-c926-fr95)** (CVSS score: 9.8) - A vulnerability that allows sandbox escape via "SuppressedError" and permits an attacker to run arbitrary code on the underlying host. (Affects versions <= 3.10.4, patches in 3.11.0)
* **[CVE-2026-26956](https://github.com/patriksimek/vm2/security/advisories/GHSA-ffh4-j6h5-pg66)** (CVSS score: 9.8) - A protection mechanism failure vulnerability that allows sandbox escape with arbitrary code execution by triggering a TypeError produced by Symbol-to-string coercion. (Affects version 3.10.4, confirmed on Node.js 25.6.1, patched in 3.10.5)
* **[CVE-2026-43997](https://github.com/patriksimek/vm2/security/advisories/GHSA-47x8-96vw-5wg6)** (CVSS score: 10.0) - A code injection vulnerability that allows an attacker to obtain the host Object and escape the sandbox, leading to arbitrary code execution. (Affects versions <= 3.10.5, patched in 3.11.0)
* **[CVE-2026-43999](https://github.com/patriksimek/vm2/security/advisories/GHSA-947f-4v7f-x2v8)** (CVSS score: 9.9) - A vulnerability that allows a bypass of NodeVM's built-in allowlist and enables an attacker to load excluded builtins like child\_process and achieve remote code execution. (Affects version 3.10.5, patched in 3.11.0)
* **[CVE-2026-44005](https://github.com/patriksimek/vm2/security/advisories/GHSA-vwrp-x96c-mhwq)** (CVSS score: 10.0) - A vulnerability that allows attacker-controlled JavaScript to escape the sandbox and enable prototype pollution. (Affects versions 3.9.6-3.10.5, patched in 3.11.0)
* **[CVE-2026-44006](https://github.com/patriksimek/vm2/security/advisories/GHSA-qcp4-v2jj-fjx8)** (CVSS score: 10.0) - A code injection vulnerability via "BaseHandler.getPrototypeOf" that enables sandbox escape and remote code execution. (Affects versions <= 3.10.5, patched in 3.11.0)
* **[CVE-2026-44007](https://github.com/patriksimek/vm2/security/advisories/GHSA-8hg8-63c5-gwmx)** (CVSS score: 9.1) - An improper access control vulnerability that allows sandbox escape and execution of arbitrary operating system commands on the underlying host. (Affects versions <= 3.11.0, patched in 3.11.1)
* **[CVE-2026-44008](https://github.com/patriksimek/vm2/security/advisories/GHSA-9qj6-qjgg-37qq)** (CVSS score: 9.8) - A vulnerability that allows sandbox escape via "neutralizeArraySpeciesBatch()" and permits an attacker to execute arbitrary commands on the underlying host. (Affects versions <= 3.11.1, patched in 3.11.2)
* **[CVE-2026-44009](https://github.com/patriksimek/vm2/security/advisories/GHSA-9vg3-4rfj-wgcm)** (CVSS score: 9.8) - A vulnerability that allows sandbox escape via a null proto exception and permits an attacker to execute arbitrary commands on the underlying host. (Affects versions <= 3.11.1, patched in 3.11.2)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The disclosure comes a couple of months after vm2 maintainer Patrik Simek released patches for another critical sandbox escape flaw ([CVE-2026-22709](https://thehackernews.com/2026/01/critical-vm2-nodejs-flaw-allows-sandbox.html), CVSS score: 9.8) that could lead to arbitrary code execution on the underlying host system.

The string of newly identified sandbox escapes illustrates the challenge of securely isolating untrusted code in JavaScript-based sandbox environments, with Simek acknowledging previously that new bypasses will likely be discovered in the future. Users of vm2 are advised to update to the latest version ([3.11.2](https://github.com/patriksimek/vm2/releases/tag/v3.11.2)) for optimal protection.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#lin...