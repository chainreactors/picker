---
title: Malicious npm Package indexed-btree Hid Its Loader in Runtime Code Before Removal
url: https://thehackernews.com/2026/09/malicious-npm-package-indexed-btree-hid.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:53.734755
---

# Malicious npm Package indexed-btree Hid Its Loader in Runtime Code Before Removal

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Malicious npm Package indexed-btree Hid Its Loader in Runtime Code Before Removal](https://thehackernews.com/2026/09/malicious-npm-package-indexed-btree-hid.html)

**Ravie Lakshmanan**Sep 22, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaN7aXt0PoPdZQ_VG77wkwdIyNugcdkFD6MnMvlj5LN_byw2ZrX8-gtpDld4CviuW1MOhHiElsvFtIkO9IfhBr4af-sJwM1zvR-RFICRll4G5jG4JNPX1vx4sup3omlw8uTJgro9UUfzecLMI1Whls3ihqZ9OXYJliIBjhpoodf4WI9j1lA6EUjms7x1pG/s1700-nu-rw-lo-l85-e365/rth.jpg)

A malicious npm package named "indexed-btree" has been observed hiding its malicious behavior within application code rather than using lifecycle scripts, indicating that threat actors are likely shifting tactics in response to [recent security controls](https://thehackernews.com/2026/07/npm-12-disables-install-scripts-by.html).

"Indexed-btree is a malicious npm package mimicking the legit sorted-btree package, an ordinary B-tree/indexing utility," Checkmarx [said](https://checkmarx.com/zero-post/npm-btree-malware-campaign-affects-millions-of-downloads-no-need-for-install-script/). "Unlike the common attacks we've seen in the supply chain space, this package does not rely on preinstall / postinstall at all. Instead, it runs entirely from application code at runtime."

The [package](https://www.npmjs.com/package/indexed-btree) and the [associated GitHub repository](https://github.com/INDEXED-BTREE/) are no longer available for download from npm. However, statistics show the package was first uploaded to the registry on June 18, 2026, by an npm user named "[charlessadler25](https://www.npmjs.com/~charlessadler25)," amassing [millions of downloads](https://npm-stat.com/charts.html?package=indexed-btree&from=2026-06-01&to=2026-09-21) in a [short span of time](https://secure.software/npm/packages/indexed-btree/versions).

To make matters worse, the campaign may have generated illicit profits for the threat actor, earning them around €230,933.57 in cryptocurrency (i.e., 109 ETH).

The development comes as npm version 12 introduced a security change to prevent automatic execution of lifecycle scripts such as preinstall or postinstall, which is one of the most common ways malware is executed through packages distributed through the repository.

"Legitimately, these are often used for compiling necessary code, seeding data, or setting up essential configurations," Checkmarx [said](https://checkmarx.com/zero-post/npm-v12-lifecycle-script-limits-a-real-malicious-package-risk-reduction-or-just-moving-risk-around/). "For threat actors, however, this is frequently exploited to automatically execute malicious code without user consent during the installation of a malicious package."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The latest findings from the software supply chain security company show that bad actors are shifting tactics in response to the change, eschewing install hooks in favor of incorporating the malicious code directly within the library.

In this case, the malware loader is concealed inside a "BTree.prototype.set()" method, which then triggers "sharedLoad.min.js," a JavaScript payload that embeds the obfuscated first stage of the malware.

The malware is designed to fingerprint the host, beacon the details to a hard-coded Slack channel and Telegram bot, uses the [EtherHiding](https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html) technique to pull next-stage, encrypted blobs from a [smart contract](https://sepolia.etherscan.io/address/0xE390863Dac96a7118C71227C2b099B50cF602D31) deployed on Sepolia testnet, and finally merge them to form the second-stage payload.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoQ4QnAmd_sMorsoejvt0jz-FEMOPMkFCRT06sluWF15hdEr_mBBM8jEp8k9HRT1ZoPLjjTMlnHYGU3_6lMIgCBVDf0LTS7u2uqOQAFGtvAhU1kd1mLi8I3EJk1MJK5G4gu3ef1Eb2lX_ipkFa9Bl_pF1MtxyjOMeghoQriHY5HWt04w7srqk67y7KpbmN/s1700-nu-rw-lo-l85-e365/git-make.jpg)

The final step involves deleting the malicious artifacts and removing the trigger from the package code to cover up the tracks.

Checkmarx said indexed-btree is one of the many npm packages tied to the same operation, all of which have since been removed from npm -

* ordered-kv-index
* btree-leaderboard
* priority-slot-queue
* btree-range-store
* btree-core
* btree-time-index
* btree-lru-cache
* neighbor-key-map
* sliding-score-window
* mutex-forge

To counter the threat, developers are recommended not to stick only to install-time scanning and blocking lifecycle scripts alone, but also employ runtime behavior analysis.

"What makes this campaign particularly important is that it shows attackers adapting almost immediately to stronger software supply chain defenses," Ensar Seker, CISO at SOCRadar, said in a statement shared with The Hacker News. "Npm has improved install time security by restricting dependency lifecycle scripts, but this campaign demonstrates that attackers can simply move malicious execution into legitimate-looking runtime functionality instead."

"The broader lesson is that security controls change attacker behavior rather than eliminate the underlying threat. Blocking lifecycle scripts is an important improvement, but attackers will continue searching for alternative execution paths. Defenders, therefore, need layered controls capable of detecting malicious behavior before installation, during execution, and after deployment."

### PolinRider Resurfaces on Packagist

The disclosure comes as Socket said it deleted malicious code in the "dev-main" version of "visanduma/nova-two-factor," a Packagist package with over 700,000 cumulative downloads, as part of an ongoing North Korea-linked malicious cyber campaign dubbed [PolinRider](https://thehackernews.com/2026/07/north-korean-hackers-publish-108.html).

A defining trait of PolinRider is the threat actor's pattern of compromising...