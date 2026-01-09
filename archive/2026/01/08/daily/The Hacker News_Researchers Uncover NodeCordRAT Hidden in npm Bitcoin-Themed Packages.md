---
title: Researchers Uncover NodeCordRAT Hidden in npm Bitcoin-Themed Packages
url: https://thehackernews.com/2026/01/researchers-uncover-nodecordrat-hidden.html
source: The Hacker News
date: 2026-01-08
fetch_date: 2026-01-09T03:32:02.761594
---

# Researchers Uncover NodeCordRAT Hidden in npm Bitcoin-Themed Packages

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

# [Researchers Uncover NodeCordRAT Hidden in npm Bitcoin-Themed Packages](https://thehackernews.com/2026/01/researchers-uncover-nodecordrat-hidden.html)

**Jan 08, 2026**Ravie LakshmananMalware / Cloud Security

[![NodeCordRAT Hidden in npm](data:image/png;base64... "NodeCordRAT Hidden in npm")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtexcKpvH8t1IN9Taxc25I-ykg1l98ahAsVYMYGLTw9Yy7W9ULsjlRNgMG0yUOpKRueTn5N36hOYSrgYP_-vZBuUYCzGgVleyQk0bZULbbIPYrfJxLPsZkJBQDjwooYWOllT3ifqBb5_T-JW6WywfZFvtKB2LQPySRO2kmhIfTQgxUSshZwyBNoC1J2nNv/s790-rw-e365/npm-malware.jpg)

Cybersecurity researchers have [discovered](https://www.zscaler.com/blogs/security-research/malicious-npm-packages-deliver-nodecordrat) three malicious npm packages that are designed to deliver a previously undocumented malware called **NodeCordRAT**.

The names of the packages, all of which were taken down as of November 2025, are listed below. They were uploaded by a user named "wenmoonx."

* [bitcoin-main-lib](https://secure.software/npm/packages/bitcoin-main-lib) (2,300 Downloads)
* [bitcoin-lib-js](https://secure.software/npm/packages/bitcoin-lib-js/) (193 Downloads)
* [bip40](https://secure.software/npm/packages/bip40) (970 Downloads)

"The bitcoin-main-lib and bitcoin-lib-js packages execute a postinstall.cjs script during installation, which installs bip40, the package that contains the malicious payload," Zscaler ThreatLabz researchers Satyam Singh and Lakhan Parashar said. "This final payload, named NodeCordRAT by ThreatLabz, is a remote access trojan (RAT) with data-stealing capabilities."

NodeCordRAT gets its name from the use of npm as a propagation vector and Discord servers for command-and-control (C2) communications. The malware is equipped to steal Google Chrome credentials, API tokens, and seed phrases from cryptocurrency wallets like MetaMask.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

According to the cybersecurity company, the threat actor behind the campaign is assessed to have named the packages after real repositories found within the legitimate [bitcoinjs](https://github.com/orgs/bitcoinjs/repositories) project, such as bitcoinjs-lib, bip32, bip38, and bip38.

Both "bitcoin-main-lib" and "bitcoin-lib-js" include a "package.json" file that features "postinstall.cjs" as a postinstall script, leading to the execution of "bip40" that contains the NodeCordRAT payload.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiIk6OxRCTdfBgY_mahGCSl-4cJKer4eufCOACNHTw-_lS_2eZknbDcbCPlV_kTe4rCiqEpHF8eFGlK4dajfc-P8nqKfSHV7aUIEZI2HVb1YutGLEWiXYpI4HvbAjJh1_DrB97j1boMZuK7KwcazAtSVRRsjtruN3VrOy4cqMi-bV39gXoyQuH6EElj8Z7/s790-rw-e365/zz.jpg)

The malware, besides fingerprinting the infected host to generate a unique identifier across Windows, Linux, and macOS systems, leverages a hard-coded Discord server to open a covert communication channel to receive instructions and execute them -

* !run, to execute arbitrary shell commands using Node.js' exec function
* !screenshot, to take a full desktop screenshot and exfiltrate the PNG file to the Discord channel
* !sendfile, to upload a specified file to the Discord channel

"This data is exfiltrated using Discord's API with a hardcoded token and sent to a private channel," Zscaler said. "The stolen files are uploaded as message attachments via Discord's REST endpoint /channels/{id}/messages."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[Threat Research](https://thehackernews.com/search/label/Threat%20Research)

Trending News

[![DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](data:image/svg+xml;base64... "DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide")

DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million Users Worldwide](https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html)

[![CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution](data:image/svg+xml;base64... "CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution")

CSA Issues Alert on Critical SmarterMail Bug Allowing Remote Code Execution](https://thehackernews.com/2025/12/csa-issues-alert-on-critical.html)

[![⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider Crime and More](data:image/svg+xml;base64... "⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider Crime and More")

⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider Crime and More](https://thehackernews.com/2025/12/we...