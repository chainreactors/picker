---
title: Malicious PyPI, npm, and Ruby Packages Exposed in Ongoing Open-Source Supply Chain Attacks
url: https://thehackernews.com/2025/06/malicious-pypi-npm-and-ruby-packages.html
source: The Hacker News
date: 2025-06-05
fetch_date: 2025-10-06T22:56:08.684128
---

# Malicious PyPI, npm, and Ruby Packages Exposed in Ongoing Open-Source Supply Chain Attacks

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

# [Malicious PyPI, npm, and Ruby Packages Exposed in Ongoing Open-Source Supply Chain Attacks](https://thehackernews.com/2025/06/malicious-pypi-npm-and-ruby-packages.html)

**Jun 04, 2025**Ravie LakshmananSupply Chain Attack / DevOps

[![Malicious PyPI, npm, and Ruby Packages](data:image/png;base64... "Malicious PyPI, npm, and Ruby Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZztju6ez3Z6vi2hVgf1-yFV_pgSSnK-IMpZ6QnW8yIE2CIQcmuju6ZbYl7P96afEmJWMKn74XA6FI2Sr7mR6Nwdnrk7_9VJFP4ZHh4e3gmTS_vfDbtVow_ml02lE1HI-htzCLguFqfuB3zg-ROJ6UQ0Dbg9d3a7-KB4oxS_bJz_NszEPxchcw61U44GCQ/s790-rw-e365/SOFTWARE.jpg)

Several malicious packages have been uncovered across the npm, Python, and Ruby package repositories that drain funds from cryptocurrency wallets, erase entire codebases after installation, and exfiltrate Telegram API tokens, once again demonstrating the variety of supply chain threats lurking in open-source ecosystems.

The findings come from multiple reports published by Checkmarx, ReversingLabs, Safety, and Socket in recent weeks. The list of identified packages across these platforms are listed below -

[![Malicious PyPI, npm, and Ruby Packages](data:image/png;base64... "Malicious PyPI, npm, and Ruby Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQ2awSxtlHGteXTk2xzxzttzaEVt9vStx-Za2c2iAksfXbSWHGHMh0AAnqgWAiui-XFw2bJ5V_4GWABUHc1Ht4NNKvjmidbXfb2OkLPoBeKQs-kkXvab-5r5ibrfhYnQ4rtY-m3E5F6eCtTARQ7fjosEvg9-8t8wQ5CE5GL1ZqGctzCv_FwUtz_Or0jJyp/s790-rw-e365/pack.jpg)

Socket noted that the two [malicious](https://rubygems.org/gems/fastlane-plugin-telegram-proxy) [gems](https://rubygems.org/gems/fastlane-plugin-proxy_teleram) were published by a threat actor under the aliases Bùi nam, buidanhnam, and si\_mobile merely days after Vietnam [ordered](https://www.reuters.com/sustainability/society-equity/vietnam-acts-block-messaging-app-telegram-government-document-seen-by-reuters-2025-05-23/) a nationwide ban on the Telegram messaging app late last month for allegedly not cooperating with the government to tackle illicit activities related to fraud, drug trafficking, and terrorism.

"These gems silently exfiltrate all data sent to the Telegram API by redirecting traffic through a command-and-control (C2) server controlled by the threat actor," Socket researcher Kirill Boychenko [said](https://socket.dev/blog/malicious-ruby-gems-exfiltrate-telegram-tokens-and-messages-following-vietnam-ban). "This includes bot tokens, chat IDs, message content, and attached files."

The software supply chain security company said the gems are "near-identical clones" of the legitimate [Fastlane](https://fastlane.tools/) plugin "fastlane-plugin-telegram," a widely used library to send deployment notifications to Telegram channels from CI/CD pipelines.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malicious change introduced by the threat actor tweaks the network endpoint used to send and receive Telegram messages to a hard-coded server ("rough-breeze-0c37.buidanhnam95.workers[.]dev") that effectively acts as a relay between the victim and the Telegram API, while silently harvesting sensitive data.

Given that the malware itself is not region-specific and lacks any geofencing logic to limit its execution to Vietnamese systems, it's suspected that the attackers simply capitalized on the Telegram ban in the country to distribute counterfeit libraries under the guise of a proxy.

"This campaign illustrates how quickly threat actors can exploit geopolitical events to launch targeted supply chain attacks," Boychenko said. "By weaponizing a widely used development tool like Fastlane and disguising credential-stealing functionality behind a timely 'proxy' feature, the threat actor leveraged trust in package ecosystems to infiltrate CI/CD environments."

Socket said it also discovered an npm package named "xlsx-to-json-lh" that typosquats the legitimate conversion tool "xlsx-to-json-lc" and detonates a malicious payload when an unsuspecting developer imports the package. First published in February 2019, it has since been taken down.

"This package contains a hidden payload that establishes a persistent connection to a command-and-control (C2) server," security researcher Kush Pandya [said](https://socket.dev/blog/npm-package-wipes-codebases-with-remote-trigger). "When triggered, it can delete entire project directories without warning or recovery options."

Specifically, the destruction actions are unleashed once the French command "remise à zéro" (meaning "reset") is issued by the C2 server, causing the package to delete source code files, version control data, configuration files, node\_modules (including itself), and all project assets.

Another set of [malicious npm packages](https://socket.dev/blog/malicious-npm-packages-target-bsc-and-ethereum) – pancake\_uniswap\_validators\_utils\_snipe, pancakeswap-oracle-prediction, ethereum-smart-contract, and env-process – have been found to steal anywhere between 80 to 85% of the funds present in a victim's Ethereum or BSC wallet using obfuscated JavaScript code and transfer them to an attacker-controlled wallet.

The packages, uploaded by a user named @crypto-exploit, have attracted over 2,100 downloads, with "pancake\_uniswap\_validators\_utils\_snipe" published four years ago. They are currently no longer available for download.

Similar cryptocurrency-themed malicious packages discovered on PyPI have incorporated covert functionality to steal Solana private keys, source code, and other sensitive data from compromised systems. It's worth noting that while "semantic-types" was benign when it was first uploaded on December 22, 2024, the malicious payload was introduced as an update on January 26, 2025.

One collection of PyPI packages is designed to "[monkey patch](https://en.wikipedia.org/wiki/Monkey_patch)" Solana key-generation methods by modifying relevant functions at runtime without making any changes to the original sourc...