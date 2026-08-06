---
title: Trojanized npm Packages Employ NullReceiver Tactic to Decode C2 IP from Blockchain
url: https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:51.814306
---

# Trojanized npm Packages Employ NullReceiver Tactic to Decode C2 IP from Blockchain

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

![cybersecurity](data:image/svg+xml;base64...)

# [Trojanized npm Packages Employ NullReceiver Tactic to Decode C2 IP from Blockchain](https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html)

**Ravie Lakshmanan**Aug 05, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_jFD4wUBf7wKq8NwAgGKeKgJ3XIR82d26D7t5fNRBoDTOHcK5i66j4VqtLNAvK7Lkocc3lbW4SK33Ialb3F4EuB_k59ahZItRVdPsZ3RceScz5lEyR7gQHqqw221WMj6ArtKDUashxvrkYSPaE0b7ue8v-TkkT0IB8sPhgcCGIqN3mtfsjQ2MKztu5DkV/s1700-e365/npm-c2.jpg)

Cybersecurity researchers have flagged an evolution of the EtherHiding blockchain-based command-and-control (C2) technique that conceals the C2 server IP address inside a made-up destination address of a completely empty Ethereum transfer.

The new dead drop resolver approach, observed in two trojanized npm packages "bianira-ui" and "fluid-type-ui," has been codenamed **[NullReceiver](https://opensourcemalware.com/blog/nullreceiver-dprk-c2-technique)** by OpenSourceMalware, which has described it as a "deliberate improvement on EtherHiding." The activity has been linked to North Korea.

The packages are currently no longer available for download from npm. However, statistics show that they have been downloaded a few hundred times since they were first published on July 28, 2026 -

* [bianira-ui](https://npm-stat.com/charts.html?package=bianira-ui) (109 downloads), uploaded by an npm user named "npmuser1101"
* [fluid-type-ui](https://npm-stat.com/charts.html?package=fluid-type-ui) (587 downloads), uploaded by an npm user named "npmuser3002"

EtherHiding was [first publicly documented](https://thehackernews.com/2023/10/binances-smart-chain-exploited-in-new.html) by Guardio Labs in October 2023 as a covert approach that involves embedding nefarious code within a [smart contract](https://ethereum.org/developers/docs/smart-contracts/) on a public blockchain like BNB Smart Chain (BSC) or Ethereum. The technique heralded the "next level of bulletproof hosting" as it improves operational resilience in the face of takedowns.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The use of EtherHiding by North Korean hacking groups was [detailed](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html) by Google Threat Intelligence Group (GTIG) late last year in connection with [Contagious Interview](https://thehackernews.com/2026/07/dprk-linked-macos-malvertising-uses.html), a long-running campaign that aims to deceive potential targets by approaching them on LinkedIn with lucrative job opportunities and asking them to complete an assessment that leads to malware deployment.

The latest development indicates that the threat actors are further refining their tactics and making it difficult for defenders to detect.

"Instead of hardcoding a C2 address or hiding it in transaction [calldata](https://crypto.com/en/glossary/calldata) (as in EtherHiding), NullReceiver encodes the C2 IP directly in the bytes of the recipient address of a zero-value, zero-data Ethereum transfer," security researcher Paul McCarty said.

"The malware looks up the attacker's wallet, reads the destination address of its most recent outbound transaction, and decodes a C2 IP straight from those address bytes, with no smart contract and no payload field involved."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp2JlYxtO8ERLKOUQWEHhsEpf5fOczPAzfCYSUfZJCs4_O3vxIogUH1sH3pDS3TnpeQ9ctxXu0QVfTQTdt9I_BfsYl8SaF5cpY_wKimW9-tkgLOE4tYnUr7aSVDnM4d0CEMr4pYT5KiV-_mCYQMzC_vhwRQDTUunVBKiBKjgFiAPMs_A1TSBlWubYasQHK/s1700-e365/null.png)

By embedding the C2 IP address in this manner, NullReceiver aims to address one of the major shortcomings of EtherHiding, which requires a fixed, publicly known destination address -- one that can be tracked by defenders as new transactions containing the payload, the C2 IP address, or the malicious script, occur for a gas fee.

NullReceiver, in contrast, provides a non-existent destination address. The address "exists" only to provide a way to encode the C2 IP address within itself. This, in turn, makes attribution difficult, as it eliminates the "fixed, watchable destination."

Neither of the newly discovered npm packages identified as part of the new campaign, bianira-ui and fluid-type-ui, calls a smart contract nor embeds any content within the transaction's calldata field. Instead, the JavaScript libraries leverage the new technique to extract the IP address and connect to it. The entire sequence of actions on a victim machine is as follows -

* Look up a hard-coded attacker wallet ("[0xa322e5f3d311d3080e6f0121063e9adc2490ef1a](https://etherscan.io/address/0xa322e5f3d311d3080e6f0121063e9adc2490ef1a)")
* Find its most recent outbound transaction
* Read that transaction's destination address
* Decode a C2 IP address directly out of the address bytes by converting the first four bytes from their hexadecimal representation to their number equivalent
* Connect to that IP address ("166.88.134[.]62")

An examination of the wallet transactions shows that the destination "To" address for each of them is the same: "[0xa658863ea658863e68656c6c6f6970626f742121](https://etherscan.io/address/0xa658863ea658863e68656c6c6f6970626f742121)." While "a658863e" becomes "166.88.134[.]62," the trailing bytes "68656c6c6f6970626f742121" represent the ASCII string "helloipbot!!."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

As of writing, a total of 68 transactions have taken place since July 27, 2026, a day before the packages were published.

What makes NullReceiver more sneaky is the absence of a fixed target and a fingerprint, not to mention the fact that the transactions are cheaper than before. A crucial difference between the two techniques is that while EtherHiding makes it possible to smuggle a full URL or script, NullReceiver can only encode a few bytes.

"NullReceiver never reuses a destination," OpenSourceMalware said. "Every lookup is a brand-new, throwaway address that's never been seen before. A NullReceiver transaction carries nothing extra at all. There's no field to fingerprint, because there's no field."

"Calldata costs gas per byte. EtherHidin...