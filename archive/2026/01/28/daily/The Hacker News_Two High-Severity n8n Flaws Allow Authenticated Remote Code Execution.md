---
title: Two High-Severity n8n Flaws Allow Authenticated Remote Code Execution
url: https://thehackernews.com/2026/01/two-high-severity-n8n-flaws-allow.html
source: The Hacker News
date: 2026-01-28
fetch_date: 2026-01-29T04:05:59.626554
---

# Two High-Severity n8n Flaws Allow Authenticated Remote Code Execution

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

# [Two High-Severity n8n Flaws Allow Authenticated Remote Code Execution](https://thehackernews.com/2026/01/two-high-severity-n8n-flaws-allow.html)

**Ravie Lakshmanan**Jan 28, 2026Vulnerability / Workflow Automation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhW94x6FIasfUAUj1l0mDp4cnVeR5PmfPV85I4_GuIlUqCVlMX0bthAcsA9oHJJz8d3gXUo74yw4d2kG3FnDnFe0zz_CzVY6Hyy8biL_gMKKaErWM3p15lAdh5xQnBBb6RhHSgKmpM3RLx1wccjhlKJc6I6lrO8M7SFIs3ezfEXuieA11PIJ1D7Z4nSaLb2/s1700-e365/n8n.jpg)

Cybersecurity researchers have [disclosed](https://research.jfrog.com/post/achieving-remote-code-execution-on-n8n-via-sandbox-escape/) two new security flaws in the n8n workflow automation platform, including a crucial vulnerability that could result in remote code execution.

The weaknesses, discovered by the JFrog Security Research team, are listed below -

* **[CVE-2026-1470](https://nvd.nist.gov/vuln/detail/CVE-2026-1470)** (CVSS score: 9.9) - An [eval injection vulnerability](https://cwe.mitre.org/data/definitions/95.html) that could allow an authenticated user to bypass the [Expression sandbox mechanism](https://docs.n8n.io/code/expressions/) and achieve full remote code execution on n8n's main node by passing specially crafted JavaScript code
* **[CVE-2026-0863](https://nvd.nist.gov/vuln/detail/CVE-2026-0863)** (CVSS score: 8.5) - An eval injection vulnerability that could allow an authenticated user to bypass n8n's python-task-executor sandbox restrictions and run arbitrary Python code on the underlying operating system

Successful exploitation of the flaws could permit an attacker to hijack an entire n8n instance, including under scenarios where it's operating under "internal" execution mode. In its documentation, n8n [notes](https://docs.n8n.io/hosting/configuration/task-runners/) that using internal mode in production environments can pose a security risk, urging users to switch to external mode to ensure proper isolation between n8n and task runner processes.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

"As n8n spans an entire organization to automate AI workflows, it holds the keys to core tools, functions, and data from infrastructure, including LLM APIs, sales data, and internal IAM systems, among others," JFrog said in a statement shared with The Hacker News. "This results in escapes giving a hacker an effective "skeleton key" to the entire corporation."

To address the flaws, users are advised to update to the following versions -

* **CVE-2026-1470** - 1.123.17, 2.4.5, or 2.5.1
* **CVE-2026-0863** - 1.123.14, 2.3.5, or 2.4.2

The development comes merely weeks after Cyera Research Labs detailed a maximum-severity security flaw in n8n ([CVE-2026-21858](https://thehackernews.com/2026/01/critical-n8n-vulnerability-cvss-100.html) aka Ni8mare) that allows an unauthenticated remote attacker to gain complete control over susceptible instances.

"These vulnerabilities highlight how difficult it is to safely sandbox dynamic, high‑level languages such as JavaScript and Python," researcher Nathan Nehorai said. "Even with multiple validation layers, deny lists, and AST‑based controls in place, subtle language features and runtime behaviors can be leveraged to bypass security assumptions."

"In this case, deprecated or rarely used constructs, combined with interpreter changes and exception handling behavior, were enough to break out of otherwise restrictive sandboxes and achieve remote code execution."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DevOps](https://thehackernews.com/search/label/DevOps), [JavaScript](https://thehackernews.com/search/label/JavaScript), [n8n](https://thehackernews.com/search/label/n8n), [Python](https://thehackernews.com/search/label/Python), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Workflow Automation](https://thehackernews.com/search/label/Workflow%20Automation)

Trending News

[![Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites](data:image/svg+xml;base64... "Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites")

Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites](https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html)

[![Hackers Use LinkedIn Messages to Spread RAT Malware Through DLL Sideloading](data:image/svg+xml;base64... "Hackers Use LinkedIn Messages to Spread RAT Malware Through DLL Sideloading")

Hackers Use LinkedIn Messages to Spread RAT Malware Through DLL Sideloading](https://thehackernews.com/2026/01/hackers-use-linkedin-messages-to-spread.html)

[![Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution](data:image/svg+xml;base64... "Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution")

Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution](https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html)

[![CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution](data:image/svg+xml;base64... "CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution")

CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution](https://thehackernews.com/...