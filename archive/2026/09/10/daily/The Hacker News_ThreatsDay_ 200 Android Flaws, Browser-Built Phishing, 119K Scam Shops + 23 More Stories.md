---
title: ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories
url: https://thehackernews.com/2026/09/threatsday-200-android-flaws-browser.html
source: The Hacker News
date: 2026-09-10
fetch_date: 2026-09-11T06:53:19.530746
---

# ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories](https://thehackernews.com/2026/09/threatsday-200-android-flaws-browser.html)

**Ravie Lakshmanan**Sep 10, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFNPIVe_Yx__WtfjnMTnoJSKPMcGPiMCP5NxEyv1gRcGSlnozG41TeGldWhQi7Hsc0XgcmC9tfTEBS-CdLLAz8cOskVbBOsghdSM9kg_AhQmhfMada8rs4l7O7Py8YJErqK54BIt0r06Sm1l62fy8yv6H8PJrEXWxjnvyLkyFKzzXcGI_h00yeBqck5v9L/s1700-nu-rw-lo-l85-e365/td-main.jpg)

A lot of this week’s security news has the same awkward answer to one question: “Why was that allowed to work?”

An extension asks for access and takes too much. A trusted service becomes part of a phishing chain. An old bug still gets results. An exposed system stays exposed. A package looks useful right up until it isn’t. Different stories, same basic problem: the path in was often already there.

Nothing here needed magic. Mostly access, trust, weak edges, and someone willing to keep poking. That’s the week.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. Malicious extensions steal crypto data

   [Cross-Browser Extension Campaign Leads to Crypto Session and Wallet Data Theft](https://socket.dev/blog/chrome-firefox-crypto-data-theft)

   A set of four malicious Google Chrome and Mozilla Firefox extensions has been found to target Axiom Trade and Padre users to steal session tokens and wallet data. The extensions are J7Tracker (Chrome), VREO (Chrome and Firefox), and Orbit Tracker (Firefox). While the first three contain the same Axiom and Padre collection module, the fourth implements a different collector but targets the same data, while retaining some artifacts from J7Tracker. "The module is byte-identical across all three analyzed extensions. It automatically retrieves authenticated user information, wallet-related bundle data, Firebase access tokens, and application state, then sends the information to threat actor-controlled Vercel deployments," Socket [said](https://socket.dev/blog/chrome-firefox-crypto-data-theft). The same Chrome publisher has been traced back to two earlier extensions, GhostApe and GhostApe Color, impersonating the MockApe trading add-on.
2. AI agents automate cyber intrusions

   [Chinese-Speaking Threat Actor Uses AI to Target Asia](https://hunt.io/blog/chinese-operator-secflow-claude-qwen-deepseek-asia)

   A Chinese-speaking operator has been observed using Anthropic Claude Code, Alibaba Qwen, and DeepSeek to automate intrusions against government and financial systems in Afghanistan, Thailand, Taiwan, and the U.S. Some of the targets included Taiwan's Kuomintang Party History Archives, Indonesia's Ministry of Foreign Affairs, government and education systems in mainland China, and industrial hosts in Da Nang, Vietnam. The attacker is said to have used SecFlow, an AI orchestration framework, to convert "campaign objectives into tasks for specialized AI agents" and supply them with tools, target information, shared storage, and network routes, Hunt.io [said](https://hunt.io/blog/chinese-operator-secflow-claude-qwen-deepseek-asia), adding the tool "split reconnaissance, exploitation, collection, and reporting among specialist workers." Some of the vulnerabilities exploited by the threat actor are Shellshock, Spring4Shell, Ghostcat, Shiro deserialization, Log4Shell, Grafana and Nexus path traversals, and a Nacos authentication bypass. The exploitation is followed by the deployment of web shells, which are generated through a dedicated GLUTTON capability, and used to facilitate follow-on actions, like reconnaissance, privilege escalation, credential theft, and custom implant deployment. One such backdoor is SecBox, a Go-based remote-access and network-pivot framework. Details of the campaign [first came to light](https://thehackernews.com/2026/07/daxin-resurfaces-in-taiwan-alongside.html) in July 2026.
3. Shadow AI exposes sensitive data

   [U.K. NCSC Warns of Shadow AI Risks](https://www.ncsc.gov.uk/blogs/the-hidden-risks-of-shadow-ai)

   The U.K.'s National Cyber Security Center (NCSC) has warned that employees using unapproved AI tools can expose sensitive corporate data and create security risks that organizations may struggle to detect and manage. "Providing shadow AI access to company or customer data likely increases the risk of data breaches, intellectual property loss and failure to meet regulatory requirements," NCSC [said](https://www.ncsc.gov.uk/blogs/the-hidden-risks-of-shadow-ai). "Employees who transfer sensitive or proprietary information to consumer AI services will likely reduce the organization's visibility and control over that information. AI agents are complex pieces of software that can have critical security vulnerabilities. If an attacker successfully exploits a vulnerability, they can gain access to the same data, services, and privileges that the agent has legitimate access to."
4. Fake M&A deals drive wire fraud

   [Phantom Deal Fraud Campaign Exposed](https://www.gendigital.com/blog/insights/research/phantom-deal)

   Attackers are masquerading as executives and tricking targets in legal teams into moving conversations to WhatsApp and personal email with an aim to initiate international wire transfers using forged acquisition documents as part of a merger and acquisition scam. "The attackers presented the acquisition as a tightly controlled transaction coordinated by a reputable adviser, with only a small group involved and an announcement approaching fast," Gen Digital [said](https://www.gendigital.com/blog/insights/research/phantom-deal). "The organizations and professions varied. The targets included senior people in private equity, industrial finance, sales, mining and energy. For each of them, an acquisition or strategic investment narrative would have been credible enough to justify initial engagement. Des...