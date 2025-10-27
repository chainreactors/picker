---
title: Researchers Uncover Backdoor in Solana's Popular Web3.js npm Library
url: https://thehackernews.com/2024/12/researchers-uncover-backdoor-in-solanas.html
source: The Hacker News
date: 2024-12-05
fetch_date: 2025-10-06T19:42:16.184951
---

# Researchers Uncover Backdoor in Solana's Popular Web3.js npm Library

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

# [Researchers Uncover Backdoor in Solana's Popular Web3.js npm Library](https://thehackernews.com/2024/12/researchers-uncover-backdoor-in-solanas.html)

**Dec 04, 2024**Ravie LakshmananSupply Chain Attack

[![Web3.js npm Library](data:image/png;base64... "Web3.js npm Library")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOtKLyHiBDWbyvczrNBcDGq8vWK2Koy0CS6t04qF3Z0UIK9UfvpJiAfPuP2-WK7lxjOq-EFlzJIWrZoB6biIhADrjutp84GtW0Mv6t4aGx2eylCg_NCaxDGTF5ANnGEvFL_N7fv6GkPA8PwXqlzSvuhck64LSBs9QsJPSm5Ok5tCJhyphenhyphenODrx50Xf415-GMa/s790-rw-e365/bacdoor.png)

Cybersecurity researchers are alerting to a software supply chain attack targeting the popular [@solana/web3.js](https://www.npmjs.com/package/%40solana/web3.js) npm library that involved pushing two malicious versions capable of harvesting users' private keys with an aim to drain their cryptocurrency wallets.

The attack has been detected in versions 1.95.6 and 1.95.7. Both these versions are no longer available for download from the npm registry. The package is widely used, attracting over 400,000 weekly downloads.

"These compromised versions contain injected malicious code that is designed to steal private keys from unsuspecting developers and users, potentially enabling attackers to drain cryptocurrency wallets," Socket [said](https://socket.dev/blog/supply-chain-attack-solana-web3-js-library) in a report.

@solana/web3.js is an npm package that can be used to [interact](https://solana.com/docs/clients/javascript) with the Solana JavaScript software development kit (SDK) for building Node.js and web apps.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

According to Datadog security researcher [Christophe Tafani-Dereeper](https://bsky.app/profile/did%3Aplc%3Azwlpsxw2udovqf4mbfi4ibqf/post/3lcgt6l7s4c2a), "the backdoor inserted in v1.95.7 adds an 'addToQueue' function which exfiltrates the private key through seemingly-legitimate CloudFlare headers" and that "calls to this function are then inserted in various places that (legitimately) access the private key."

The command-and-control (C2) server to which the keys are exfiltrated to ("sol-rpc[.]xyz") is currently down. It was registered on November 22, 2024, on domain registrar NameSilo.

It's suspected that the maintainers of the npm package fell victim to a phishing attack that allowed the threat actors to seize control of the accounts and publish the rogue versions.

"A publish-access account was compromised for @solana/web3.js, a JavaScript library that is commonly used by Solana dApps," Steven Luscher, one of the library maintainers, [said](https://github.com/solana-labs/solana-web3.js/releases/tag/v1.95.8) in the release notes for version 1.95.8.

"This allowed an attacker to publish unauthorized and malicious packages that were modified, allowing them to steal private key material and drain funds from dApps, like bots, that handle private keys directly. This issue should not affect non-custodial wallets, as they generally do not expose private keys during transactions."

Luscher also noted that the incident only impacts projects that directly handle private keys and that were updated within the window of 3:20 p.m. UTC and 8:25 p.m. UTC on December 2, 2024.

Users who are relying on @solana/web3.js as a dependency are advised to update to the latest version as soon as possible, and optionally rotate their authority keys if they suspect they are compromised.

The disclosure comes days after Socket warned of a bogus Solana-themed npm package named solana-systemprogram-utils that's designed to sneakily reroute a user's funds to an attacker-controlled hard-coded wallet address in 2% of transactions.

"The code cleverly masks its intent by functioning normally 98% of the time," the Socket Research Team [said](https://socket.dev/blog/malicious-npm-package-targets-solana-developers-and-hijacks-funds). "This design minimizes suspicion while still allowing the attacker to siphon funds."

It also follows the discovery of npm packages such as crypto-keccak, crypto-jsonwebtoken, and crypto-bignumber that masquerade as legitimate libraries but contain code to siphon credentials and cryptocurrency wallet data, once again highlighting how threat actors are continuing to abuse the trust developers place in the open-source ecosystem.

"The malware threatens individual developers by stealing their credentials and wallet data, which can lead to direct financial losses," security researcher Kirill Boychenko [noted](https://socket.dev/blog/malicious-npm-packages-threaten-crypto-developers). "For organizations, compromised systems create vulnerabilities that can spread throughout enterprise environments, enabling widespread exploitation."

### Update

The software supply chain attack targeting the @solana/web3.js npm library has been formally assigned the CVE identifier [CVE-2024-54134](https://nvd.nist.gov/vuln/detail/CVE-2024-54134) (CVSS score: 8.3).

A root cause analysis published by Solana research and development firm Anza has revealed that the attack commenced on December 3, 2024, with a spear-phishing email targeting a @solana npm org member with publish access, thereby allowing the threat actor to steal their credentials and two-factor authentication (2FA) code.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The hacker sent several emails inviting them to collaborate on a private package," Anza [said](https://www.anza.xyz/blog/web3-js-exploit-root-cause-analysis). "The invite was crafted in such a way that made it appear to have originated from another member of the team."

"When clicked, the successful spear phishing campaign routed a developer with publish access to a clone of the npm website controlled by the hacker where the developer entered their npm username and password, and completed a round of two-factor authentication."

The attack has been found to have led to the unauthorized transfers of crypto assets worth $164,100...