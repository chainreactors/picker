---
title: Malicious npm Packages Impersonate Flashbots, Steal Ethereum Wallet Keys
url: https://thehackernews.com/2025/09/malicious-npm-packages-impersonate.html
source: The Hacker News
date: 2025-09-07
fetch_date: 2025-10-02T19:47:54.239877
---

# Malicious npm Packages Impersonate Flashbots, Steal Ethereum Wallet Keys

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Malicious npm Packages Impersonate Flashbots, Steal Ethereum Wallet Keys](https://thehackernews.com/2025/09/malicious-npm-packages-impersonate.html)

**Sep 06, 2025**Ravie LakshmananSoftware Security / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFSJzLL1pc8quLfhY-XvdCTUHE211jQksLVgyJf3avkmDP1YU0kIMXpWhiw052Me82v6eQVpV3Q1-_QNI5pUGLGrMal30FuYY2ySGimCMNU-JFOB47n3rFNmknYYcqpqqmHiAxD6J2_UY7f9mqe61GvZ4kJ5moskZwxtU665cLDoyEptVEurxiCJZXH_A/s790-rw-e365/1000013746.jpg)

A new set of four malicious packages have been discovered in the npm package registry with capabilities to steal cryptocurrency wallet credentials from Ethereum developers.

"The packages masquerade as legitimate cryptographic utilities and [Flashbots MEV](https://www.npmjs.com/package/%40flashbots/ethers-provider-bundle) infrastructure while secretly exfiltrating private keys and mnemonic seeds to a Telegram bot controlled by the threat actor," Socket researcher Kush Pandya [said](https://socket.dev/blog/malicious-npm-packages-impersonate-flashbots-sdks-targeting-ethereum-wallet-credentials) in an analysis.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The packages were uploaded to npm by a user named "[flashbotts](https://www.npmjs.com/~flashbotts)," with the earliest library uploaded as far back as September 2023. The most recent upload took place on August 19, 2025. The packages in question, all of which are still available for download as of writing, are listed below -

* [@flashbotts/ethers-provider-bundle](https://npm-stat.com/charts.html?package=%40flashbotts%2Fethers-provider-bundle) (52 Downloads)
* [flashbot-sdk-eth](https://npm-stat.com/charts.html?package=flashbot-sdk-eth) (467 Downloads)
* [sdk-ethers](https://npm-stat.com/charts.html?package=sdk-ethers) (90 Downloads)
* [gram-utilz](https://npm-stat.com/charts.html?package=gram-utilz) (83 Downloads)

The impersonation of [Flashbots](https://www.flashbots.net/) is not coincidental, given its role in [combating](https://www.sciencedirect.com/science/article/pii/S2096720925000673) the [adverse effects](https://writings.flashbots.net/mev-and-the-limits-of-scaling) of Maximal Extractable Value ([MEV](https://a16zcrypto.com/posts/article/mev-explained/)) on the Ethereum network, such as sandwich, liquidation, backrunning, front-running, and time-bandit attacks.

The most dangerous of the identified libraries is "@flashbotts/ethers-provider-bundle," which uses its functional cover to conceal the malicious operations. Under the guise of offering full Flashbots API compatibility, the package incorporates stealthy functionality to exfiltrate environment variables over SMTP using Mailtrap.

In addition, the npm package implements a transaction manipulation function to redirect all unsigned transactions to an attacker-controlled wallet address and log metadata from pre-signed transactions.

sdk-ethers, per Socket, is mostly benign but includes two functions to transmit mnemonic seed phrases to a Telegram bot that are only activated when they are invoked by unwitting developers in their own projects.

The second package to impersonate Flashbots, flashbot-sdk-eth, is also designed to trigger the theft of private keys, while gram-utilz offers a modular mechanism for exfiltrating arbitrary data to the threat actor's Telegram chat.

With mnemonic seed phrases serving as the "master key" to recover access to cryptocurrency wallets, theft of these sequences of words can allow threat actors to break into victims' wallets and gain complete control over their wallets.

The presence of Vietnamese language comments in the source code suggest that the financially-motivated threat actor may be Vietnamese-speaking.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings indicate a deliberate effort on part of the attackers to weaponize the trust associated with the platform to conduct software supply chain attacks, not to mention obscure the malicious functionality amidst mostly harmless code to sidestep scrutiny.

"Because Flashbots is widely trusted by validators, searchers, and DeFi developers, any package that appears to be an official SDK has a high chance of being adopted by operators running trading bots or managing hot wallets," Pandya pointed out. "A compromised private key in this environment can lead to immediate, irreversible theft of funds."

"By exploiting developer trust in familiar package names and padding malicious code with legitimate utilities, these packages turn routine Web3 development into a direct pipeline to threat actor-controlled Telegram bots."

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

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data exfiltration](https://thehackernews.com/search/label/data%20exfiltration)[Ethereum](https://thehackernews.com/search/label/Ethereum)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[Open Source Security](https://thehackernews.com/search/label/Open%20Source...