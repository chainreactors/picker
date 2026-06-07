---
title: New ChatGPT Lockdown Mode Limits Tools That Could Enable Data Exfiltration
url: https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html
source: The Hacker News
date: 2026-06-06
fetch_date: 2026-06-07T06:16:38.429880
---

# New ChatGPT Lockdown Mode Limits Tools That Could Enable Data Exfiltration

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [New ChatGPT Lockdown Mode Limits Tools That Could Enable Data Exfiltration](https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html)

**Ravie Lakshmanan**Jun 06, 2026Cybersecurity / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBOQJLNqTRWigWAgPKNCKXr8hOgMZD4ZNb3lNzGbrvSj87BzK_VzrbaqMPVOo1wmCsILPHO2s5cdfu1I2nUOhNibPpzsOHko3qWQwCVXXVdi8yaqYjMJGBD6Fzz-eBmgJ1-Vy0E02L_X1xsT3neUlTTsn9s8e2ODQVYXNErvOz9VrHEIdJNfGhsASUV0ag/s1700-e365/chatgpt-lockdown.jpg)

OpenAI has begun rolling out a new **Lockdown Mode** to ChatGPT for eligible personal accounts to reduce the risk of data exfiltration arising from [prompt injection attacks](https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html).

The feature is primarily designed for people and organizations that handle sensitive data and require stricter protection guarantees. Lockdown Mode is available to logged-in users across Free, Go, Plus, and Pro, and self-serve ChatGPT Business plans.

"Lockdown Mode is an optional advanced security setting that limits many tools and capabilities in OpenAI products that can connect to the web or external services," OpenAI [said](https://help.openai.com/en/articles/20001061-lockdown-mode).

"It is designed to reduce the risk of data exfiltration from prompt injection attacks by limiting outbound network requests, at the expense of disabling or limiting some useful features."

The safeguards are aimed at hardening the attack surface against prompt injections, which continues to be a "frontier" problem impacting all large language models (LLMs).

Specifically, they build upon sandboxing and existing controls to combat [URL-based data exfiltration mechanisms](https://openai.com/index/ai-agent-link-safety/) to limit outbound network requests that could potentially transmit sensitive data to attacker-controlled infrastructure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The idea is not to stop prompt injections from occurring. Nor does it change the way memory or file uploads work, or the ability to share a conversation. Rather, the goal is to eliminate potential pathways through which the data could be exfiltrated. To that end, Lockdown Mode disables the following features -

* Live web browsing, which is limited to accessing only cached content
* Image support, for displaying images in regular responses or retrieving images from the web
* Deep research
* Agent mode
* Canvas networking, which prevents users from approving [Canvas](https://openai.com/index/introducing-canvas/)-generated code to access the network
* File downloads, which block downloading files for data analysis

Pointing out the feature is not "intended for everyone," OpenAI also noted that both Lockdown Mode and Developer Mode cannot be used at the same time, adding that turning on one disables the other.

"Lockdown Mode is designed to substantially reduce the risk of prompt injection-based data exfiltration in ChatGPT and supported OpenAI products, but it does not guarantee that data exfiltration cannot happen," the company said. "Risk may remain through enabled Apps, unforeseen combinations of capabilities, or newly discovered techniques."

"Lockdown Mode also does not prevent all other effects of prompt injection attacks. For example, a malicious instruction hidden in an uploaded file could still affect ChatGPT's behavior, and cause an incorrect answer."

The development comes as OpenAI has also [launched](https://help.openai.com/en/articles/20001257-managing-active-sessions-in-chatgpt) a new account management feature that enables users to review active ChatGPT sessions and log out of individual or all sessions if signs of unauthorized account activity are detected. The listed sessions include information about the device, the app used, approximate location, sign-in date and time, whether the device is trusted, and whether it's the current session.

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

[Account security](https://thehackernews.com/search/label/Account%20security), [artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [ChatGPT](https://thehackernews.com/search/label/ChatGPT), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data exfiltration](https://thehackernews.com/search/label/data%20exfiltration), [Large language model](https://thehackernews.com/search/label/Large%20language%20model), [OpenAI](https://thehackernews.com/search/label/OpenAI), [Prompt Injection](https://thehackernews.com/search/label/Prompt%20Injection), [sandbox](https://thehackernews.com/search/label/sandbox), [Web Browsing](https://thehackernews.com/search/label/Web%20Browsing)

⚡ Top Stories This Week

[![Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited](data:image/svg+xml;base64... "Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited")

Google June 2026 Android Update Patches 124 Flaws, One Actively Exploited](https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html)

[![Oracle WebLogic CVE-2024-21...