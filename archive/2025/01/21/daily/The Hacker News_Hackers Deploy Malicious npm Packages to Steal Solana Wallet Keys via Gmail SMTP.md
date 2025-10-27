---
title: Hackers Deploy Malicious npm Packages to Steal Solana Wallet Keys via Gmail SMTP
url: https://thehackernews.com/2025/01/hackers-deploy-malicious-npm-packages.html
source: The Hacker News
date: 2025-01-21
fetch_date: 2025-10-06T20:13:16.842997
---

# Hackers Deploy Malicious npm Packages to Steal Solana Wallet Keys via Gmail SMTP

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

# [Hackers Deploy Malicious npm Packages to Steal Solana Wallet Keys via Gmail SMTP](https://thehackernews.com/2025/01/hackers-deploy-malicious-npm-packages.html)

**Jan 20, 2025**Ravie LakshmananSupply Chain Attack / Solana

[![Malicious npm Packages](data:image/png;base64... "Malicious npm Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfRfKk6wIek4mOwy1hfJmqLoDhOKbOFpfw0tZA035CkvU0zEt8fexcuKvcIEGwFXV41TSj00Z-uW9JgkXOo6w4PDu3Atjr_n6nFdhyphenhyphenwqamSI_nJpAre1WVORx2ttLKuKbe2DVH4lnng7znIG80nnw-cMv4p3fGBzZ8wQ-VyhsOojUw8hPWPpxru2XG6w-7/s790-rw-e365/solana.png)

Cybersecurity researchers have identified three sets of malicious packages across the npm and Python Package Index (PyPI) repository that come with capabilities to steal data and even delete sensitive data from infected systems.

The list of identified packages is below -

* @async-mutex/mutex, a typosquat of async-mute (npm)
* dexscreener, which masquerades as a library for accessing liquidity pool data from decentralized exchanges (DEXs) and interacting with the DEX Screener platform (npm)
* solana-transaction-toolkit (npm)
* solana-stable-web-huks (npm)

* cschokidar-next, a typosquat of chokidar (npm)
* achokidar-next, a typosquat of chokidar (npm)
* achalk-next, a typosquat of chalk (npm)
* csbchalk-next, a typosquat of chalk (npm)
* cschalk, a typosquat of chalk (npm)

* pycord-self, a typosquat of discord.py-self (PyPI)

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Supply chain security company Socket, which [discovered](https://socket.dev/blog/gmail-for-exfiltration-malicious-npm-packages-target-solana-private-keys-and-drain-victim-s) the packages, said the first four packages are designed to intercept Solana private keys and transmit them through Gmail's Simple Mail Transfer Protocol ([SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)) servers with the likely goal of draining victims' wallets.

Particularly, the packages solana-transaction-toolkit and solana-stable-web-huks programmatically deplete the wallet, automatically transferring up to 98% of its contents to an attacker-controlled Solana address, while claiming to offer Solana-specific functionality.

"Because Gmail is a trusted email service, these exfiltration attempts are less likely to be flagged by firewalls or endpoint detection systems, which treat smtp.gmail.com as legitimate traffic," security researcher Kirill Boychenko said.

Socket said it also came across two GitHub repositories published by the threat actors behind solana-transaction-toolkit and solana-stable-web-huks that purport to contain Solana development tools or scripts for automating common DeFi workflows, but, in reality, import the threat actor's malicious npm packages.

[![Malicious npm Packages](data:image/png;base64... "Malicious npm Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjT1FFN7ljIRLLfUKz2S6Dvj_oRe6fJ1ot6BNzLX1LiwvUvMIi1TAqGIXnOSiQ7v9J9YgVBw3R-3-xvZtSWAJkhgKQelV4lE3e_UF6eu2Wk6p-G6ltTxibIyo9C_o2OphvjEhgadIiQ1mTn9uY0EQ-W4yicTDZNMR77Iw9VyhnNlHA27XsCUmNBu-DP9ftd/s790-rw-e365/solana.png)

The GitHub accounts associated with these repositories, "moonshot-wif-hwan" and "Diveinprogramming," are no longer accessible.

"A script in the threat actor's GitHub repository, moonshot-wif-hwan/pumpfun-bump-script-bot, is promoted as a bot for trading on Raydium, a popular Solana-based DEX, but instead it imports malicious code from solana-stable-web-huks package," Boychenko said.

The use of malicious GitHub repositories illustrates the attackers' attempts to stage a broader campaign beyond npm by targeting developers who might be searching for Solana-related tools on the Microsoft-owned code hosting platform.

The second set of npm packages have been [found](https://socket.dev/blog/kill-switch-hidden-in-npm-packages-typo-squatting-chalk-and-chokidar) to take their malicious functionality to the next level by incorporating a "kill switch" function that recursively wipes all files in project-specific directories, in addition to exfiltrating environment variables to a remote server in some cases.

The counterfeit csbchalk-next package functions identically to the typosquatted versions of chokidar, the only difference being that it only initiates the data deletion operation after it receives the code "202" from the server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Pycord-self, on the other hand, [singles out Python developers](https://socket.dev/blog/malicious-pypi-package-targets-discord-developers-with-token-theft-and-backdoor) looking to integrate Discord APIs into their projects, capturing Discord authentication tokens and connecting to an attacker-controlled server for persistent backdoor access post installation on both Windows and Linux systems.

The development comes as bad actors are [targeting](https://thehackernews.com/2024/11/malicious-npm-packages-target-roblox.html) Roblox users with fraudulent libraries engineered to facilitate data theft using open-source stealer malware such as Skuld and Blank-Grabber. Last year, Imperva [revealed](https://www.imperva.com/blog/trouble-in-da-hood-malicious-actors-use-infected-pypi-packages-to-target-roblox-cheaters/) that Roblox players on the lookout for game cheats and mods have also been targeted by bogus PyPI packages that trick them into downloading the same payloads.

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
[**Share on Linked...