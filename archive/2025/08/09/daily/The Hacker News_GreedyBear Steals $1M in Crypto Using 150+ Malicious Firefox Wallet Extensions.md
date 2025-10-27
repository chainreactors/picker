---
title: GreedyBear Steals $1M in Crypto Using 150+ Malicious Firefox Wallet Extensions
url: https://thehackernews.com/2025/08/greedybear-steals-1m-in-crypto-using.html
source: The Hacker News
date: 2025-08-09
fetch_date: 2025-10-07T00:49:55.115286
---

# GreedyBear Steals $1M in Crypto Using 150+ Malicious Firefox Wallet Extensions

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

# [GreedyBear Steals $1M in Crypto Using 150+ Malicious Firefox Wallet Extensions](https://thehackernews.com/2025/08/greedybear-steals-1m-in-crypto-using.html)

**Aug 08, 2025**Ravie LakshmananCryptocurrency / Browser Security

[![Malicious Firefox Wallet Extensions](data:image/png;base64... "Malicious Firefox Wallet Extensions")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmwl1Sdv-qzEY2BAespGZmdY7mUFgexwtNPX47dnNEo8HIG-AYn3ezA2d9nRXmwUtoya_FHkPTH7uxBXvRuPf1fVpMsQQFdpbQPucCuYfZm2zw2dujrPEhZG4aqWuSL0Tk2IxN1ljtmpT5Ztei-Wur_9Z8Xs7OwFEhD_ly00DSEpC4pQsE42kPd_a6X-Ch/s790-rw-e365/firefox-malware.jpg)

A newly discovered campaign dubbed **GreedyBear** has leveraged over 150 malicious extensions to the Firefox marketplace that are designed to impersonate popular cryptocurrency wallets and steal more than $1 million in digital assets.

The published browser add-ons masquerade as MetaMask, TronLink, Exodus, and Rabby Wallet, among others, Koi Security researcher Tuval Admoni said.

What makes the activity notable is the threat actor's use of a technique that the cybersecurity company called Extension Hollowing to bypass safeguards put in place by Mozilla and exploit user trust. It's worth noting that some aspects of the campaign were [first documented](https://thehackernews.com/2025/08/weekly-recap-vpn-0-day-encryption.html#:~:text=Mozilla%20Warns%20Add%2Dons%20Devs%20Against%20Phishing%20Attack) by security researcher Lukasz Olejnik last week.

"Rather than trying to sneak malicious extensions past initial reviews, they build legitimate-seeming extension portfolios first, then weaponize them later when nobody's watching," Admoni [said](https://blog.koi.security/greedy-bear-massive-crypto-wallet-attack-spans-across-multiple-vectors-3e8628831a05) in a report published Thursday.

To achieve this, the attackers first create a publisher account in the marketplace, upload innocuous extensions with no actual functionality to sidestep initial reviews, post fake positive reviews to create an illusion of credibility, and modify their innards with malicious capabilities.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The fake extensions are designed to capture wallet credentials entered by unsuspecting users and exfiltrate them to an attacker-controlled server. It also gathers victims' IP addresses for likely tracking purposes.

The campaign is assessed to be an extension of a previous iteration called [Foxy Wallet](https://thehackernews.com/2025/07/over-40-malicious-firefox-extensions.html) that involved the threat actors publishing no less than 40 malicious browser extensions for Mozilla Firefox with similar goals in mind. The latest spike in the number of extensions indicates the growing scale of the operation.

The fake wallet cryptocurrency draining attacks are augmented by campaigns that distribute malicious executables through various Russian sites that peddle cracked and pirated software, leading to the deployment of information stealers and even ransomware.

The GreedyBear actors have also found setting up scam sites that pose as cryptocurrency products and services, such as wallet repair tools, to possibly trick users into parting with their wallet credentials, or payment details, resulting in credential theft and financial fraud.

Koi Security said it was able to link the three attack verticals to a single threat actor based on the fact that the domains used in these efforts all point to a lone IP address: 185.208.156[.]66, which acts as a command-and-control (C2) server for data collection and management.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEqri2J7t3R8YXzzTONIm7OTTuUdthn8Evtvg__hCTddpqeEjwLHPyHBjLE9jDs6uOufIDhJ6tOnAQXHdZYeotxSCgppfPivLE7QFlededqyhqxz7sDxwNKU9C3PUNEwqaxbuyHO7CaGofJAAUjvHmSeR9sz5DjO6pxJFhQGGeM0D8o5bCk-hql8p2ObFd/s790-rw-e365/wallet.jpg)

There is evidence to suggest that the extension-related attacks are branching out to target other browser marketplaces. This is based on the discovery of a Google Chrome extension named Filecoin Wallet that has used the same C2 server and the underlying logic to pilfer credentials.

To make matters worse, an analysis of the artifacts has uncovered signs that they may have been created using artificial intelligence (AI)-powered tools. This underscores how threat actors are increasingly misusing AI systems to enable attacks at scale and at speed.

"This variety indicates the group is not deploying a single toolset, but rather operating a broad malware distribution pipeline, capable of shifting tactics as needed," Admoni said.

"The campaign has since evolved the difference now is scale and scope: this has evolved into a multi-platform credential and asset theft campaign, backed by hundreds of malware samples and scam infrastructure."

### Ethereum Drainers Pose as Trading Bots to Steal Crypto

The disclosure comes as SentinelOne flagged a widespread and ongoing cryptocurrency scam that entails distributing a malicious smart contract disguised as a trading bot in order to drain user wallets. The fraudulent Ethereum drainer scheme, active since early 2024, is estimated to have already netted the threat actors more than $900,000 in stolen profits.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The scams are marketed through YouTube videos which explain the purported nature of the crypto trading bot and explain how to deploy a smart contract on the Remix Solidity Compiler platform, a web-based integrated development environment (IDE) for Web3 projects," researcher Alex Delamotte [said](https://www.sentinelone.com/labs/smart-contract-scams-ethereum-drainers-pose-as-trading-bots-to-steal-crypto/). "The video descriptions share a link to an external site that hosts the weaponized smart contract code."

The videos are said to be AI-generated and are published from aged accounts that post other sources' cryptocurrency news as playl...