---
title: Fake Chrome Extension “Safery” Steals Ethereum Wallet Seed Phrases Using Sui Blockchain
url: https://thehackernews.com/2025/11/fake-chrome-extension-safery-steals.html
source: The Hacker News
date: 2025-11-13
fetch_date: 2025-11-14T03:13:42.027424
---

# Fake Chrome Extension “Safery” Steals Ethereum Wallet Seed Phrases Using Sui Blockchain

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Fake Chrome Extension "Safery" Steals Ethereum Wallet Seed Phrases Using Sui Blockchain](https://thehackernews.com/2025/11/fake-chrome-extension-safery-steals.html)

**Nov 13, 2025**Ravie LakshmananBrowser Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhS-Kf6dnTbbnxktKjoq7yOuQcEZ5eAObBOOXkT5cPRRC_UZGyfDnQOrZA8yiAE-fn6mXRgzOiWxB7uFr2ofyOnoUIWRW9geQttVX95HTIeAiU2sS4osiKQiWxKIWeJcc0oKw84MabuSF0i59NpUq0YB3uIHp7OsSRDAZQFnIhjENG6xSjX6BxlDDZkMbYw/s790-rw-e365/chrome-eth.png)

Cybersecurity researchers have uncovered a malicious Chrome extension that poses as a legitimate Ethereum wallet but harbors functionality to exfiltrate users' seed phrases.

The name of the extension is "Safery: Ethereum Wallet," with the threat actor describing it as a "secure wallet for managing Ethereum cryptocurrency with flexible settings." It was uploaded to the Chrome Web Store on September 29, 2025, and was updated as recently as November 12. It's still [available for download](https://chromewebstore.google.com/detail/safery-ethereum-wallet/fibemlnkopkeenmmgcfohhcdbkhgbolo) as of writing.

"Marketed as a simple, secure Ethereum (ETH) wallet, it contains a backdoor that exfiltrates seed phrases by encoding them into Sui addresses and broadcasting microtransactions from a threat actor-controlled Sui wallet," Socket security researcher Kirill Boychenko [said](https://socket.dev/blog/malicious-chrome-extension-exfiltrates-seed-phrases).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Specifically, the malware present within the browser add-on is designed to steal wallet mnemonic phrases by encoding them as fake Sui wallet addresses and then using micro-transactions to send 0.000001 SUI to those wallets from a hard-coded threat actor-controlled wallet.

The end goal of the malware is to smuggle the seed phrase inside normal looking blockchain transactions without the need for setting up a command-and-control (C2) server to receive the information. Once the transactions are complete, the threat actor can decode the recipient addresses to reconstruct the original seed phrase and ultimately drain assets from it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5oTVfjsVgEa67Ui3tFkPwiBq9puB2Rx545jrJWNtT1oASHflVLo0ax1dG8qwEyHmt-BizWlTFD9_ZhyphenhyphenymHT3LQL-PpIOfm5H3YtCpfte0SWXyI0fEwLC8PDqsjnGrgamYQLavL3vG5MDhyDP7huRONIqn9g44YjSjEvl6KGNhyphenhyphenuj0XPvP01by2msOoDVw/s790-rw-e365/chrome.png)

"This extension steals wallet seed phrases by encoding them as fake Sui addresses and sending micro-transactions to them from an attacker-controlled wallet, allowing the attacker to monitor the blockchain, decode the addresses back to seed phrases, and drain victims' funds," Koi Security [notes](https://dex.koi.security/reports/chrome/fibemlnkopkeenmmgcfohhcdbkhgbolo/1.6) in an analysis.

To counter the risk posed by the threat, users are advised to stick to trusted wallet extensions. Defenders are recommended to scan extensions for mnemonic encoders, synthetic address generators, and hard-coded seed phrases, as well as block those that write on the chain during wallet import or creation.

"This technique lets threat actors switch chains and RPC endpoints with little effort, so detections that rely on domains, URLs, or specific extension IDs will miss it," Boychenko said. "Treat unexpected blockchain RPC calls from the browser as high signal, especially when the product claims to be single chain."

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

[Blockchain](https://thehackernews.com/search/label/Blockchain)[browser security](https://thehackernews.com/search/label/browser%20security)[Chrome Extensions](https://thehackernews.com/search/label/Chrome%20Extensions)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data theft](https://thehackernews.com/search/label/data%20theft)[Digital Wallets](https://thehackernews.com/search/label/Digital%20Wallets)[Ethereum](https://thehackernews.com/search/label/Ethereum)[Malware](https://thehackernews.com/search/label/Malware)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-ai-security)

Trending News

[![⚡ Weekly Recap: Lazarus Hits Web3, Intel/AMD TEEs Cracked, Dark Web Leak Tool and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Lazarus Hits Web3, Intel/AMD TEEs Cracked, Dark Web Leak Tool and More")

⚡ Weekly Recap: Lazarus Hits Web3, Intel/AMD TEEs Cracked, Dark Web Leak Tool and More](https://thehackernews.com/2025/11/weekly-recap-lazarus-hits-web3-intelamd.html)

[![ThreatsDay Bulletin: AI Tools in Malware, Botnets, GDI Flaws, Election Attacks](data:image/svg+xml;base64... "ThreatsDay Bulletin: AI Tools in Malware, Botnets, GDI Flaws, Election Attacks")

ThreatsDay Bulletin: AI Tools in Malware, Botnets, GDI Flaws, Election Attacks and More](https://thehackernews.com/2025/11/threatsday-bulletin-ai-tools-in-malware.html)

[![Microsoft Detects SesameOp Backdoor Using OpenAI's API as a Stealth...