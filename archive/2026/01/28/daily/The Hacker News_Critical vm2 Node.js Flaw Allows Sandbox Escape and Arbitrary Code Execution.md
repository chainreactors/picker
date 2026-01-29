---
title: Critical vm2 Node.js Flaw Allows Sandbox Escape and Arbitrary Code Execution
url: https://thehackernews.com/2026/01/critical-vm2-nodejs-flaw-allows-sandbox.html
source: The Hacker News
date: 2026-01-28
fetch_date: 2026-01-29T04:05:59.903597
---

# Critical vm2 Node.js Flaw Allows Sandbox Escape and Arbitrary Code Execution

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

# [Critical vm2 Node.js Flaw Allows Sandbox Escape and Arbitrary Code Execution](https://thehackernews.com/2026/01/critical-vm2-nodejs-flaw-allows-sandbox.html)

**Ravie Lakshmanan**Jan 28, 2026Vulnerability / Open Source

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEir_Rl9Xy1aEtQBIw6aqscoEj4444e7H2BJLRbPSyqbi2DMtc22vTReAQM6ye0KR8pr1iBs4YA3KIdgfAvfBuIGBMrd7JYL5P9NNnNt6vgeD_B5GStVh1Bq5DzgnRsViE-z_dmkuGuhWTchwmk3ULxzq7_vVoUnKnwFaQtqVyCDf-oHiqBeiViqAlqdsGsi/s1700-e365/vm2.jpg)

A critical sandbox escape vulnerability has been disclosed in the popular vm2 Node.js library that, if successfully exploited, could allow attackers to run arbitrary code on the underlying operating system.

The vulnerability, tracked as **CVE-2026-22709**, carries a CVSS score of 9.8 out of 10.0 on the CVSS scoring system.

"In vm2 for version 3.10.0, Promise.prototype.then Promise.prototype.catch callback sanitization can be bypassed," vm2 maintainer Patrik Simek [said](https://github.com/patriksimek/vm2/security/advisories/GHSA-99p7-6v5w-7xg8). "This allows attackers to escape the sandbox and run arbitrary code."

[vm2](https://github.com/patriksimek/vm2) is a Node.js library used to run untrusted code within a secure sandboxed environment by intercepting and [proxying JavaScript objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) to prevent sandboxed code from accessing the host environment.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The newly discovered flaw stems from the library's improper sanitization of [Promise handlers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), which creates an escape vector that results in the execution of arbitrary code outside the sandbox boundaries.

"The critical insight is that async functions in JavaScript return `globalPromise` objects, not `localPromise` objects. Since `globalPromise.prototype.then` and `globalPromise.prototype.catch` are not properly sanitized (unlike `localPromise`)," Endor Labs researchers Peyton Kennedy and Cris Staicu [said](https://www.endorlabs.com/learn/cve-2026-22709-critical-sandbox-escape-in-vm2-enables-arbitrary-code-execution).

While CVE-2026-22709 has been addressed in vm2 version 3.10.2, it's the latest in a steady stream of sandbox escapes that have plagued the library in recent years. This includes [CVE-2022-36067](https://thehackernews.com/2022/10/researchers-detail-critical-rce-flaw.html), [CVE-2023-29017](https://thehackernews.com/2023/04/researchers-discover-critical-remote.html), [CVE-2023-29199, CVE-2023-30547](https://thehackernews.com/2023/04/critical-flaws-in-vm2-javascript.html), [CVE-2023-32314](https://github.com/patriksimek/vm2/security/advisories/GHSA-whpj-8f3w-67p5), [CVE-2023-37466](https://github.com/patriksimek/vm2/security/advisories/GHSA-cchq-frgv-rjh5), and [CVE-2023-37903](https://github.com/patriksimek/vm2/security/advisories/GHSA-g644-9gfx-q4q4).

The discovery of CVE-2023-37903 in July 2023 also led Simek to announce that the project was [being discontinued](https://github.com/patriksimek/vm2/blob/b51d33c49b61e03cf67a075741790e9b938dd80f/README.md). However, these references have since been removed from the latest README file available on its GitHub repository. The [Security page](https://github.com/patriksimek/vm2/blob/main/SECURITY.md) has also been updated as of October 2025 to mention that vm2 3.x versions are being actively maintained.

However, vm2's maintainer has also acknowledged that new bypasses will likely be discovered in the future, urging users to make sure that they keep the library up to date and consider other robust alternatives, such as [isolated-vm](https://github.com/laverdet/isolated-vm), for stronger isolation guarantees.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

"Instead of relying on the problematic vm model, the successor to vm2, isolated-vm relies on V8's native Isolate interface, which offers a more solid foundation, but even then, the maintainers of vm2 stress the importance of isolation and actually recommend Docker with logical separation between components," Semgrep [said](https://semgrep.dev/blog/2026/calling-back-to-vm2-and-escaping-sandbox/).

In light of the criticality of the flaw, users are recommended to update to the most recent version ([3.10.3](https://github.com/patriksimek/vm2/releases/tag/v3.10.3)), which comes with fixes for additional sandbox escapes.

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

[arbitrary code execution](https://thehackernews.com/search/label/arbitrary%20code%20execution), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [JavaScript](https://thehackernews.com/search/label/JavaScript), [node.js](https://thehackernews.com/search/label/node.js), [Open Source](https://thehackernews.com/search/label/Open%20Source), [sandbox](https://thehackernews.com/search/label/sandbox), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites](data:image/svg+xml;base64... "Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites")

Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites](https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html)

[![Hackers Use LinkedIn Messages to Spread RAT Malware Through DLL Si...