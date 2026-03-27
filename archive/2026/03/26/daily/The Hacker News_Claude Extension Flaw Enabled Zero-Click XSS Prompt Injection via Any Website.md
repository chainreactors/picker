---
title: Claude Extension Flaw Enabled Zero-Click XSS Prompt Injection via Any Website
url: https://thehackernews.com/2026/03/claude-extension-flaw-enabled-zero.html
source: The Hacker News
date: 2026-03-26
fetch_date: 2026-03-27T04:33:40.343973
---

# Claude Extension Flaw Enabled Zero-Click XSS Prompt Injection via Any Website

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Claude Extension Flaw Enabled Zero-Click XSS Prompt Injection via Any Website](https://thehackernews.com/2026/03/claude-extension-flaw-enabled-zero.html)

**Ravie Lakshmanan**Mar 26, 2026Browser Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvKbsVkCFVvziyQ564TDmmBjGzy6lzKUcC_rmt-GZWOiCshA_YGAhsMjib7OhvNS_8OX6micW6hWSY4lWh6IoGcyy_tCywr9Tr-qhyI4Wau32zV80zS3OJRVnbSZtHQqWO-RvoznJ34HjG6M5CDlKIXXTyAuZvVS235fZ9juweln5KS77w1w80Jk113rAW/s1700-e365/claude.jpg)

Cybersecurity researchers have disclosed a vulnerability in Anthropic's Claude Google Chrome Extension that could have been exploited to trigger malicious prompts simply by visiting a web page.

The flaw "allowed any website to silently inject prompts into that assistant as if the user wrote them," Koi Security researcher Oren Yomtov [said](https://www.koi.ai/blog/shadowprompt-how-any-website-could-have-hijacked-anthropic-claude-chrome-extension) in a report shared with The Hacker News. "No clicks, no permission prompts. Just visit a page, and an attacker completely controls your browser."

The issue, codenamed **ShadowPrompt**, chains two underlying flaws:

* An overly permissive origin allowlist in the extension that allowed any subdomain matching the pattern (\*.claude.ai) to send a prompt to Claude for execution.
* A document object model ([DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model))-based cross-site scripting ([XSS](https://owasp.org/www-community/attacks/xss/)) vulnerability in an Arkose Labs CAPTCHA component hosted on "a-cdn.claude[.]ai."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

Specifically, the XSS vulnerability enables the execution of arbitrary JavaScript code in the context of "a-cdn.claude[.]ai." A threat actor could leverage this behavior to inject JavaScript that issues a prompt to the Claude extension.

The extension, for its part, allows the prompt to land in Claude's sidebar as if it's a legitimate user request simply because it comes from an allow-listed domain.

"The attacker's page embeds the vulnerable Arkose component in a hidden <iframe>, sends the XSS payload via postMessage, and the injected script fires the prompt to the extension," Yomtov explained. "The victim sees nothing."

Successful exploitation of this vulnerability could allow the adversary to steal sensitive data (e.g., access tokens), access conversation history with the AI agent, and even perform actions on behalf of the victim (e.g., sending emails impersonating them, asking for confidential data).

Following responsible disclosure on December 27, 2025, Anthropic deployed a patch to the Chrome extension (version 1.0.41) that enforces a strict origin check requiring an exact match to the domain "claude[.]ai." Arkose Labs has since fixed the XSS flaw at its end as of February 19, 2026.

"The more capable AI browser assistants become, the more valuable they are as attack targets," Koi said. "An extension that can navigate your browser, read your credentials, and send emails on your behalf is an autonomous agent. And the security of that agent is only as strong as the weakest origin in its trust boundary."

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [browser security](https://thehackernews.com/search/label/browser%20security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [web security](https://thehackernews.com/search/label/web%20security), [xss](https://thehackernews.com/search/label/xss)

Trending News

[![FortiGate Devices Exploited to Breach Networks and Steal Service Account Credentials](data:image/svg+xml;base64... "FortiGate Devices Exploited to Breach Networks and Steal Service Account Credentials")

FortiGate Devices Exploited to Breach Networks and Steal Service Account Credentials](https://thehackernews.com/2026/03/fortigate-devices-exploited-to-breach.html)

[![Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days](data:image/svg+xml;base64... "Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days")

Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days](https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html)

[![Critical n8n Flaws Allow Remote Code Execution and Exposure of Stored Credentials](data:image/svg+xml;base64... "Critical n8n Flaws Allow Remote Code Execution and Exposure of Stored Credentials")

Critical n8n Flaws Allow Remote Code Execution and Exposure of Stored Credentials](https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html)

[![Six Android Malware Families Target Pix Payments, Banking Apps, and Crypto Wallets](data:image/svg+xml;base64... "Six Android Malware Families Target Pix Payments, Banking Apps, and Crypto Wallets")

Six Android Malware Families Target Pix Payments, Banking Apps, and Crypto Wallets](https://thehackernews.com/2026/03/six-andro...