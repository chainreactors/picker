---
title: Ripple's xrpl.js npm Package Backdoored to Steal Private Keys in Major Supply Chain Attack
url: https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html
source: The Hacker News
date: 2025-04-24
fetch_date: 2025-10-06T22:08:25.102115
---

# Ripple's xrpl.js npm Package Backdoored to Steal Private Keys in Major Supply Chain Attack

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

# [Ripple's xrpl.js npm Package Backdoored to Steal Private Keys in Major Supply Chain Attack](https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html)

**Apr 23, 2025**Ravie LakshmananBlockchain / Cryptocurrency

[![Ripple's xrpl.js npm Package Backdoored](data:image/png;base64... "Ripple's xrpl.js npm Package Backdoored")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnV4JWrDWtCP-v9aYG2DuTAI9fnPFXUcehEI4c9QXDhiGj-jPiqlTycZmdJiNdfAWKZBqVs3b6d-0KrWlOkJLZDk_BD8ephCiVZ8wQ0JiFqu-wPe1FX48XEMBuKPr_OorNTotuXyCL0zXwdwA_GS6H_qkO61OuHxumnM0ceVkNEFktMdKcYsti6L8WW0sI/s790-rw-e365/npm.jpg)

The Ripple cryptocurrency npm JavaScript library named [xrpl.js](https://www.npmjs.com/package/xrpl) has been compromised by unknown threat actors as part of a software supply chain attack designed to harvest and exfiltrate users' private keys.

The malicious activity has been found to affect five different versions of the package: 4.2.1, 4.2.2, 4.2.3, 4.2.4, and 2.14.2. The issue has been [addressed](https://github.com/XRPLF/xrpl.js/releases/tag/xrpl%404.2.5) in versions 4.2.5 and 2.14.3.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

xrpl.js is a popular JavaScript API for interacting with the [XRP Ledger](https://xrpl.org) blockchain, also called the Ripple Protocol, a cryptocurrency platform launched by Ripple Labs in 2012. The package has been [downloaded](https://npm-stat.com/charts.html?package=xrpl) over 2.9 million times to date, attracting more than 135,000 weekly downloads.

"The official XPRL (Ripple) NPM package was compromised by sophisticated attackers who put in a backdoor to steal cryptocurrency private keys and gain access to cryptocurrency wallets," Aikido Security's Charlie Eriksen [said](https://www.aikido.dev/blog/xrp-supplychain-attack-official-npm-package-infected-with-crypto-stealing-backdoor).

The malicious code changes have been found to be introduced by a user named "[mukulljangid](https://www.npmjs.com/~mukulljangid)" starting April 21, 2025, with the threat actors introducing a new function named checkValidityOfSeed that's engineered to transmit the stolen information to an external domain ("0x9c[.]xyz").

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcAmV_MAQSt8_UsvTnGnQJ6cuFLAS9hyVwt-C5bceJGr0KwcsOns11DonC-mwzmoASRPCQAOJhEyta_i0yYOxcPklpPPWyPXqWoWOw5DzoMXqxB2V6nUlG9N3qMcp-q9o1X5sREECb2rp5t_fjJxKQfIPL9tlWPmdlwbsoQA9urPEiH3LpIAeaX7lc2auf/s790-rw-e365/xrpl.png)

It's worth noting that "mukulljangid" likely [belongs to a Ripple employee](https://github.com/mukulljangid), indicating that their npm account was hacked to pull off the supply chain attack.

The attacker is said to have tried different ways to sneak in the backdoor while trying to evade detection, as evidenced by the different versions released in a short span of time. There is no evidence that the associated GitHub repository has been backdoored.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's not clear who is behind the attack, but it's believed that the threat actors managed to steal the developer's npm access token to tamper with the library, per Aikido.

In light of the incident, users relying on the xrpl.js library are advised to update their instances to the latest version (4.2.5 and 2.14.3) to mitigate potential threats.

"This vulnerability is in xrpl.js, a JavaScript library for interacting with the XRP Ledger," the XRP Ledger Foundation [said](https://x.com/XRPLF/status/1914726961445773652) in a post on X. "It does not affect the XRP Ledger codebase or GitHub repository itself. Projects using xrpl.js should upgrade to v4.2.5 immediately."

### Update

The supply chain compromise of xrpl.js has been assigned the CVE identifier CVE-2025-32965 (CVSS score: 9.3).

"Versions 4.2.1, 4.2.2, 4.2.3, and 4.2.4 of xrpl.js were compromised and contained malicious code designed to exfiltrate private keys," [according](https://github.com/XRPLF/xrpl.js/security/advisories/GHSA-33qr-m49q-rxfx) to a GitHub advisory. "If you are using one of these versions, stop immediately and rotate any private keys or secrets used with affected systems."

"Version 2.14.2 is also malicious, though it is less likely to lead to exploitation as it is not compatible with other 2.x versions. To secure funds, think carefully about whether any keys may have been compromised by this supply chain attack, and mitigate by sending funds to secure wallets, and/or rotating keys."

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

[Blockchain](https://thehackernews.com/search/label/Blockchain)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[JavaScript](https://thehackernews.com/search/label/JavaScript)[NPM](https://thehackernews.com/search/label/NPM)[ripple](https://thehackernews.com/search/label/ripple)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Tr...