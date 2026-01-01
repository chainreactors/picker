---
title: Trust Wallet Chrome Extension Hack Drains $8.5M via Shai-Hulud Supply Chain Attack
url: https://thehackernews.com/2025/12/trust-wallet-chrome-extension-hack.html
source: The Hacker News
date: 2025-12-31
fetch_date: 2026-01-01T03:36:45.649732
---

# Trust Wallet Chrome Extension Hack Drains $8.5M via Shai-Hulud Supply Chain Attack

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Trust Wallet Chrome Extension Hack Drains $8.5M via Shai-Hulud Supply Chain Attack](https://thehackernews.com/2025/12/trust-wallet-chrome-extension-hack.html)

**Dec 31, 2026**Ravie LakshmananSoftware Security / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMbGd5gZt4LivTf91n0rkIqb96QTFiXAPUGZIjWetmK58EeBHuQNFM6PQ1WHeNdTsg5GmtM9qWLoNz1jXn9S1t_zbP02pp62aPKYqruzZ81_fqujiRFvpj1MTxKP9VA6jeNk2Xw4Szx1UJ3ndXXEaV9-T9e0uFqieAuvHlmLRiU2RjTEkDf-Ft9YL6pyx-/s790-rw-e365/crypto.jpg)

Trust Wallet on Tuesday revealed that the second iteration of the [Shai-Hulud](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html) (aka Sha1-Hulud) supply chain outbreak in November 2025 was likely responsible for the hack of its Google Chrome extension, ultimately resulting in the theft of approximately $8.5 million in assets.

"Our Developer GitHub secrets were exposed in the attack, which gave the attacker access to our browser extension source code and the Chrome Web Store (CWS) API key," the company [said](https://trustwallet.com/blog/announcements/trust-wallet-browser-extension-v268-incident-community-update) in a post-mortem published Tuesday.

"The attacker obtained full CWS API access via the leaked key, allowing builds to be uploaded directly without Trust Wallet's standard release process, which requires internal approval/manual review."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

Subsequently, the attacker is said to have registered the domain "metrics-trustwallet[.]com" and pushed a trojanized version of the extension with a backdoor that's capable of harvesting users' wallet mnemonic phrases to the sub-domain "api.metrics-trustwallet[.]com."

The disclosure comes days after Trust Wallet [urged](https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html) about one million users of its Chrome extension to update to version 2.69 after a malicious update (version 2.68) was pushed by unknown threat actors on December 24, 2025, to the browser's extension marketplace.

The security incident ultimately led to $8.5 million in cryptocurrency assets being drained from 2,520 wallet addresses to no less than 17 wallet addresses controlled by the attacker. The first wallet-draining activity was publicly reported a day after the malicious update.

Trust Wallet has since initiated a reimbursement claim process for impacted victims. The company noted that reviews of submitted claims are ongoing and are being handled on a case-by-case basis. It also stressed that processing times may vary with each case due to the need to distinguish between victims and bad actors, and further protect against fraud.

To prevent such breaches from occurring again, Trust Wallet said it has implemented additional monitoring capabilities and controls related to its release processes.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

"Sha1-Hulud was an industry-wide software supply chain attack that affected companies across multiple sectors, including but not limited to crypto," the company said. "It involved malicious code being introduced and distributed through commonly-used developer tooling. This allowed attackers to gain access through trusted software dependencies rather than directly targeting individual organizations."

Trust Wallet's disclosure coincides with the [emergence of Shai-Hulud 3.0](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html) with increased obfuscation and reliability improvements, while still remaining laser-focused on stealing secrets from developer machines.

"The primary difference lies in string obfuscation, error handling, and Windows compatibility, all aimed at increasing campaign longevity rather than introducing novel exploitation techniques," Upwind researchers Guy Gilad and Moshe Hassan [said](https://www.upwind.io/feed/shai-hulud-3-npm-supply-chain-worm).

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

[Browser Extension](https://thehackernews.com/search/label/Browser%20Extension)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Malware](https://thehackernews.com/search/label/Malware)[software security](https://thehackernews.com/search/label/software%20security)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

Trending News

[![Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats](data:image/svg+xml;base64... "Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats")

Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html)

[![Google to Shut Down Dark Web Monitoring Tool in February 2026](data:image/svg+xml;base64... "Google to Shut Down Dark Web Monitoring Tool in February 2026")

Google to Shut Down Dark Web Monitoring Tool in Febr...