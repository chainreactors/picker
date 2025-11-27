---
title: Chrome Extension Caught Injecting Hidden Solana Transfer Fees Into Raydium Swaps
url: https://thehackernews.com/2025/11/chrome-extension-caught-injecting.html
source: The Hacker News
date: 2025-11-26
fetch_date: 2025-11-27T03:13:11.235152
---

# Chrome Extension Caught Injecting Hidden Solana Transfer Fees Into Raydium Swaps

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

# [Chrome Extension Caught Injecting Hidden Solana Transfer Fees Into Raydium Swaps](https://thehackernews.com/2025/11/chrome-extension-caught-injecting.html)

**Nov 26, 2025**Ravie LakshmananBrowser Security / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh07kZL9gPVO6CAgydSwgWaGQyaeOYAfysQ-YnUzeYR05B9sOlvBzVUPcu4OK-idfpgitAZpvjmqWBSijJ-z0-k8SFvWBB1w9-dX5YP-B7q2R3uNB81yY__MKrdwb8NHlk2y7cJHJllwU5iNOeRxmgKS6WvRZOywql8oU2k7l7IlApYlgf5wjeLfFmA-c9S/s790-rw-e365/crypto.jpg)

Cybersecurity researchers have discovered a new malicious extension on the Chrome Web Store that's capable of injecting a stealthy Solana transfer into a swap transaction and transferring the funds to an attacker-controlled cryptocurrency wallet.

The extension, named [Crypto Copilot](https://chromewebstore.google.com/detail/crypto-copilot/iaemdpdnmdkaphnmcogmcgcmhhafcifd), was [first published](https://dex.koi.security/reports/chrome/iaemdpdnmdkaphnmcogmcgcmhhafcifd/1.1.0) by a user named "sjclark76" on May 7, 2024. The developer describes the browser add-on as offering the ability to "trade crypto directly on X with real-time insights and seamless execution." The extension has 12 installs and remains available for download as of writing.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

"Behind the interface, the extension injects an extra transfer into every Solana swap, siphoning a minimum of 0.0013 SOL or 0.05% of the trade amount to a hardcoded attacker-controlled wallet," Socket security researcher Kush Pandya [said](https://socket.dev/blog/malicious-chrome-extension-injects-hidden-sol-fees-into-solana-swaps) in a Tuesday report.

Specifically, the extension incorporates obfuscated code that comes to life when a user performs a Raydium swap, manipulating it to inject an undisclosed SOL transfer into the same signed transaction. Raydium is a decentralized exchange (DEX) and automated market maker (AMM) built on the Solana blockchain.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPqJEx4yVaR2qbnDE7RoPUbdhPeiysypJ7Uyg9k_295w2dA_kE72nrKFe1knuFJ6tICjs8fsALl63-ZqGAW0E7HD9XOvL7P3ntFoICqEXTJIyicfSqLkD_82eVvy7IGzMlzGn3sHN0PhjV0EchBUnmUnuqwnJVX-4dckNdy4fYG_eamulLSQsurarF6NIN/s790-rw-e365/chrome.jpg)

It works by appending a hidden [SystemProgram.transfer](https://solana-foundation.github.io/solana-web3.js/classes/SystemProgram.html#transfer) util method to each swap before the user's signature is requested, and sends the fee to a [hard-coded wallet](https://solscan.io/account/Bjeida13AjgPaUEU9xrh1iQMwxZC7QDdvSfg73oxQff7) embedded in the code. The fee is calculated based on the amount traded, charging a minimum of 0.0013 SOL for trades and 2.6 SOL and 0.05% of the swap amount if it's more than 2.6 SOL. To avoid detection, the malicious behavior is concealed using techniques like [minification](https://en.wikipedia.org/wiki/Minification_%28programming%29) and variable renaming.

The extension also communicates with a backend hosted on the domain "crypto-coplilot-dashboard.vercel[.]app" to register connected wallets, fetch points and referral data, and report user activity. The domain, along with "cryptocopilot[.]app," does not host any real product.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

What's notable about the attack is that users are completely kept in the dark about the hidden platform fee, and the user interface only shows details of the swap. Furthermore, Crypto Copilot makes use of legitimate services like DexScreener and Helius RPC to lend it a veneer of trust.

"Because this transfer is added silently and sent to a personal wallet rather than a protocol treasury, most users will never notice it unless they inspect each instruction before signing," Pandya said. "The surrounding infrastructure appears designed only to pass Chrome Web Store review and provide a veneer of legitimacy while siphoning fees in the background."

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

[Blockchain](https://thehackernews.com/search/label/Blockchain)[Browser extensions](https://thehackernews.com/search/label/Browser%20extensions)[Chrome](https://thehackernews.com/search/label/Chrome)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Decentralized](https://thehackernews.com/search/label/Decentralized)[Malware](https://thehackernews.com/search/label/Malware)[Solana](https://thehackernews.com/search/label/Solana)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-aws-ai-security)

Trending News

[![⚡ Weekly Recap: Fortinet Exploited, China's AI Hacks, PhaaS Empire Falls and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Fortinet Exploited, China's AI Hacks, PhaaS Empire Falls and More")

⚡ Weekly Recap: Fortinet Exploited, China's AI Hacks, PhaaS Empire Falls and More](https://thehackernews.com/2025/11/weekly-recap-fortinet-exploited-chinas.html)

[![Google Issues Security Fix for Actively Exploited Chrome V8 Zero-Day Vulnerability](data:image/svg+xml;base64... "Google Issues Security Fix...