---
title: OpenClaw Bug Enables One-Click Remote Code Execution via Malicious Link
url: https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html
source: The Hacker News
date: 2026-02-02
fetch_date: 2026-02-03T04:11:05.981032
---

# OpenClaw Bug Enables One-Click Remote Code Execution via Malicious Link

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [OpenClaw Bug Enables One-Click Remote Code Execution via Malicious Link](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html)

**Ravie Lakshmanan**Feb 02, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4fXSwhiW0Eb2lGzmNue91AjKZ-c420l6qWRP0mQkVZWlxxe_Iq0MkDlUYw7GrvFfd2UqhpLGsSYc9H3-o33nWGXEUX_OPcTWpzn3lQNvZTVyzEx1CJw2r2UQMfkFdNiHJF4_x8mLAkOy7st09Siko8G8KTlPyNkVNeLDf2xTKVgCFLnumaeT4v7Q_f27J/s1700-e365/openclaw.jpg)

A high-severity security flaw has been disclosed in [OpenClaw](https://github.com/openclaw/openclaw) (formerly referred to as Clawdbot and Moltbot) that could allow remote code execution (RCE) through a crafted malicious link.

The issue, which is tracked as **[CVE-2026-25253](https://nvd.nist.gov/vuln/detail/CVE-2026-25253)** (CVSS score: 8.8), has been addressed in [version 2026.1.29](https://github.com/openclaw/openclaw/releases/tag/v2026.1.29) released on January 30, 2026. It has been described as a token exfiltration vulnerability that leads to full gateway compromise.

"The Control UI trusts gatewayUrl from the query string without validation and auto-connects on load, sending the stored gateway token in the WebSocket connect payload," OpenClaw's creator and maintainer Peter Steinberger [said](https://github.com/openclaw/openclaw/security/advisories/GHSA-g8p2-7wf7-98mq) in an advisory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"Clicking a crafted link or visiting a malicious site can send the token to an attacker-controlled server. The attacker can then connect to the victim's local gateway, modify config (sandbox, tool policies), and invoke privileged actions, achieving 1-click RCE."

OpenClaw is an open-source autonomous artificial intelligence (AI) personal assistant that runs locally on user devices and integrates with a wide range of messaging platforms. Although initially released in November 2025, the project has gained rapid popularity in recent weeks, with its GitHub repository crossing 149,000 stars as of writing.

"OpenClaw is an open agent platform that runs on your machine and works from the chat apps you already use," Steinberger [said](https://openclaw.ai/blog/introducing-openclaw). "Unlike SaaS assistants where your data lives on someone else's servers, OpenClaw runs where you choose – laptop, homelab, or VPS. Your infrastructure. Your keys. Your data."

Mav Levin, founding security researcher at depthfirst who is credited with discovering the shortcoming, [said](https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys) it can be exploited to create a one-click RCE exploit chain that takes only milliseconds after a victim visits a single malicious web page.

The problem is that clicking on the link to that web page is enough to trigger a cross-site WebSocket hijacking attack because OpenClaw's server doesn't validate the WebSocket origin header. This causes the server to accept requests from any website, effectively getting around localhost network restrictions.

A malicious web page can take advantage of the issue to execute client-side JavaScript on the victim's browser that can retrieve an authentication token, establish a WebSocket connection to the server, and use the stolen token to bypass authentication and log in to the victim's OpenClaw instance.

To make matters worse, by leveraging the token's privileged operator.admin and operator.approvals scopes, the attacker can use the API to disable user confirmation by setting "exec.approvals.set" to "off" and escape the container used to run shell tools by setting "tools.exec.host" to "gateway."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

"This forces the agent to run commands directly on the host machine, not inside a Docker container," Levin said. "Finally, to achieve arbitrary command execution, the attacker JavaScript executes a node.invoke request."

When asked whether OpenClaw's use of the API to manage the safety features constitutes an architectural limitation, Levin told The Hacker News in an emailed response that, "I would say the problem is those defenses (sandbox and safety guardrails) were designed to contain malicious actions of an LLM, as a result of prompt injection, for example. And users might think these defenses would protect from this vulnerability (or limit the blast radius), but they don't."

Steinberger noted in the advisory that "the vulnerability is exploitable even on instances configured to listen on loopback only, since the victim's browser initiates the outbound connection."

"It impacts any Moltbot deployment where a user has authenticated to the Control UI. The attacker gains operator-level access to the gateway API, enabling arbitrary config changes and code execution on the gateway host. The attack works even when the gateway binds to loopback because the victim's browser acts as the bridge."

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Container Security](https://thehackernews.com/search/label/Container...