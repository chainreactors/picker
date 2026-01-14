---
title: Malicious Chrome Extension Steals MEXC API Keys by Masquerading as Trading Tool
url: https://thehackernews.com/2026/01/malicious-chrome-extension-steals-mexc.html
source: The Hacker News
date: 2026-01-13
fetch_date: 2026-01-14T03:36:14.071783
---

# Malicious Chrome Extension Steals MEXC API Keys by Masquerading as Trading Tool

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Malicious Chrome Extension Steals MEXC API Keys by Masquerading as Trading Tool](https://thehackernews.com/2026/01/malicious-chrome-extension-steals-mexc.html)

**Jan 13, 2026**Ravie LakshmananWeb Security / Online Fraud

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjM0ngZi95ZptNXfR_fRCcaAolThq29ozaWNaVEh7n53DkYPz_Lkd0e8bXAVJlFev3xmjECw-ojYhxY-9LxK4ba00fpmcAI7sW7GTXSWb0POi3qIC8eNdKxgeFPg2HCGnA_El_ffucuffNfjqbyhL1oiqoU2HMR18zaCuUdOkBPtRiNAsLPDL9zFd-2XGGg/s790-rw-e365/mexc.jpg)

Cybersecurity researchers have disclosed details of a malicious Google Chrome extension that's capable of stealing API keys associated with MEXC, a centralized cryptocurrency exchange (CEX) [available in over 170 countries](https://www.mexc.co/en-IN/learn/article/mexc-restricted-countries-complete-list-of-prohibited-limited-regions/1), while masquerading as a tool to automate trading on the platform.

The extension, named MEXC API Automator (ID: pppdfgkfdemgfknfnhpkibbkabhghhfh), has 29 downloads and is still available on the Chrome Web Store as of writing. It was first published on September 1, 2025, by a developer named "jorjortan142."

"The extension programmatically creates new MEXC API keys, enables withdrawal permissions, hides that permission in the user interface (UI), and exfiltrates the resulting API key and secret to a hardcoded Telegram bot controlled by the threat actor," Socket security researcher Kirill Boychenko said in an analysis.

According to the Chrome Web Store listing, the web browser add-on is described as an extension that "simplifies connecting your trading bot to the MEXC exchange" by generating the API keys with the necessary permissions on the management page, including to facilitate trading and withdrawals.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

In doing so, the installed extension enables a threat actor to control any MEXC account accessed from the compromised browser, allowing them to execute trades, perform automated withdrawals, and even drain the wallets and balances reachable through the service.

"In practice, as soon as the user navigates to MEXC's API management page, the extension injects a single content script, script.js, and begins operating inside the already authenticated MEXC session," Socket added. To achieve this, the extension checks if the current URL contains the string "/user/openapi," which refers to the [API key management page](https://www.mexc.co/en-IN/user/openapi).

The script then programmatically creates a new API key and ensures that withdrawal capability is enabled. At the same time, it tampers with the page's user interface to give the impression to the user that the withdrawal permission has been disabled. As soon as the process to generate the Access Key and Secret Key is complete, the script extracts both the values and transmits them to a hard-coded Telegram bot under the threat actor's control using an HTTPS POST request.

The threat poses a severe risk, as it remains active as long as the keys are valid and not revoked, granting the attackers unfettered access to the victim's account even if they end up uninstalling the extension from the Chrome browser.

"In effect, the threat actor uses the Chrome Web Store as the delivery mechanism, the MEXC web UI as the execution environment, and Telegram as the exfiltration channel," Boychenko noted. "The result is a purpose-built credential-stealing extension that targets MEXC API keys at the moment they are created and configured with full permissions."

The attack is made possible by the fact that it leverages an already authenticated browser session to realize its goals, thereby obviating the need for obtaining a user's password or bypassing authentication protections.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

It's currently not clear who is behind the operation, but a reference to "jorjortan142" points to an [X handle](https://x.com/jorjortan142) with the same name that links to a Telegram bot named SwapSushiBot, which is also promoted across [TikTok](https://www.tiktok.com/%40swapsushi) and [YouTube](https://www.youtube.com/channel/UCJkCI3-1_pr_A8jcMn4G8aw). The YouTube channel was created on August 17, 2025.

"By hijacking a single API workflow inside the browser, threat actors can bypass many traditional controls and go straight for long lived API keys with withdrawal rights," Socket said. "The same playbook can be readily adapted to other exchanges, DeFi dashboards, broker portals, and any web console that issues tokens in session, and future variants are likely to introduce heavier obfuscation, request broader browser permissions, and bundle support for multiple platforms into a single extension."

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

[API Security](https://thehackernews.com/search/label/API%20Security)[Browser Extension](https://thehackernews.com/search/label/Browser%20Extension)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/...