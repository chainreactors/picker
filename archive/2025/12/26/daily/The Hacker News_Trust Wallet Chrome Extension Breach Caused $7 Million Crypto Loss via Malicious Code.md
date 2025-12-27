---
title: Trust Wallet Chrome Extension Breach Caused $7 Million Crypto Loss via Malicious Code
url: https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html
source: The Hacker News
date: 2025-12-26
fetch_date: 2025-12-27T03:24:09.040798
---

# Trust Wallet Chrome Extension Breach Caused $7 Million Crypto Loss via Malicious Code

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

# [Trust Wallet Chrome Extension Breach Caused $7 Million Crypto Loss via Malicious Code](https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html)

**Dec 26, 2025**Ravie LakshmananCryptocurrency / Incident Response

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZP9hON3n-2zsl52VbVSUoLRU7lEedvIxRzhLddqpu6jJM7etcQZ9Mm0ojVv8614DKB7JFs8TuCtjJ5MLdfTeanXrXv5NO1WgOvjG3TuUjobHaUo6i8KNxQMD5XBTDczYKHBT-xTCb25utln7UkGwywmXvQC7joQHPv2HVJVrSug-r3S-KCOvbcifxBe1s/s790-rw-e365/apps.jpg)

Trust Wallet is [urging](https://x.com/TrustWallet/status/2004475085168795941) users to update its Google Chrome extension to the latest version following what it described as a "security incident" that led to the loss of approximately $7 million.

The issue, the multi‑chain, non‑custodial cryptocurrency wallet service said, impacts version 2.68. The extension has about one million users, according to the Chrome Web Store listing. Users are advised to update to [version 2.69](https://chromewebstore.google.com/detail/trust-wallet/egjidjbpglichdcondbcbdnbeeppgdph) as soon as possible.

"We've confirmed that approximately $7M has been impacted and we will ensure all affected users are refunded," Trust Wallet said in a post on X. "Supporting affected users is our top priority, and we are actively finalizing the process to refund the impacted users."

Trust Wallet is also urging users to refrain from interacting with any messages that do not come from its official channels. Mobile-only users and all other browser extension versions are not affected.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/windows-stealer-alert-d)

According to details shared by SlowMist, version 2.68 introduced malicious code that's designed to iterate through all wallets stored in the extension and trigger a mnemonic phrase request for each wallet.

"The encrypted mnemonic is then decrypted using the password or passkeyPassword entered during wallet unlock," the blockchain security firm [said](https://x.com/SlowMist_Team/status/2004505094646345905). "Once decrypted, the mnemonic phrase is sent to the attacker's server api.metrics-trustwallet[.]com."

The domain "metrics-trustwallet[.]com" was registered on December 8, 2025, with the first request to "api.metrics-trustwallet[.]com" commencing on December 21, 2025.

Further analysis has revealed that the attacker has leveraged an open‑source full‑chain analytics library named posthog-js to harvest wallet user information.

The digital assets drained so far include about $3 million in Bitcoin, $431 in Solana, and more than $3 million in Ethereum. The stolen funds have been [moved through](https://x.com/PeckShieldAlert/status/2004382831158714735) centralized exchanges and cross-chain bridges for laundering and swapping. According to an update shared by blockchain investigator ZachXBT, the incident has [claimed](https://t.me/investigations/297) hundreds of victims.

"While ~$2.8 million of the stolen funds remain in the hacker's wallets (Bitcoin/ EVM/ Solana), the bulk – >$4M in cryptos – has been sent to CEXs [centralized exchanges]: ~$3.3 million to ChangeNOW, ~$340,000 to FixedFloat, and ~$447,000 to KuCoin," PeckShield [said](https://x.com/PeckShieldAlert/status/2004382831158714735).

"This backdoor incident originated from malicious source code modification within the internal Trust Wallet extension codebase (analytics logic), rather than an injected compromised third‑party dependency (e.g., malicious npm package)," SlowMist said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

"The attacker directly tampered with the application's own code, then leveraged the legitimate PostHog analytics library as the data‑exfiltration channel, redirecting analytic traffic to an attacker‑controlled server."

The company said there is a possibility that it's the work of a nation-state actor, adding the attackers may have gained control of Trust Wallet‑related developer devices or obtained deployment permissions prior to December 8, 2025.

Changpeng Zhao, a co-founder of crypto exchange Binance, which owns the utility, [hinted that](https://x.com/cz_binance/status/2004398433285894432) the exploit was "most likely" carried out by an insider, although no further evidence was provided to support the theory.

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

[Blockchain](https://thehackernews.com/search/label/Blockchain)[Browser Extension](https://thehackernews.com/search/label/Browser%20Extension)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data exfiltration](https://thehackernews.com/search/label/data%20exfiltration)[Incident response](https://thehackernews.com/search/label/Incident%20response)[Malware](https://thehackernews.com/search/label/Malware)[Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

Trending News

[![Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats](data:image/svg+xml;base64... "Featured Chrome...