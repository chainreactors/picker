---
title: ThreatsDay Bulletin: $290M DeFi Hack, macOS LotL Abuse, ProxySmart SIM Farms +25 New Stories
url: https://thehackernews.com/2026/04/threatsday-bulletin-290m-defi-hack.html
source: The Hacker News
date: 2026-04-23
fetch_date: 2026-04-24T04:57:38.258727
---

# ThreatsDay Bulletin: $290M DeFi Hack, macOS LotL Abuse, ProxySmart SIM Farms +25 New Stories

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [ThreatsDay Bulletin: $290M DeFi Hack, macOS LotL Abuse, ProxySmart SIM Farms +25 New Stories](https://thehackernews.com/2026/04/threatsday-bulletin-290m-defi-hack.html)

**Ravie Lakshmanan**Apr 23, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCPlFIV8w3UXOQRe4cwOn8C-x6WYxvZnNAOHSUnzIg8TFswCnJNoyTFJTdzAbl_a6JNCzhbAk4yGQbhI_cjF-FATAAmJJJiLjo2cZgbMQpfhYnrH6MFv6TVEqC3sblGQPViYTDE0o3alqO3YsIzatrw7NwlTkv1g6NkiVegSWKuRuQcajEyNdAUEaTamQ-/s1700-e365/threatsday.jpg)

You scroll past one incident and see another that feels familiar, like it should have been fixed years ago, but it still works with small changes. Same bugs. Same mistakes.

The supply chain is messy. Packages you did not check are stealing data, adding backdoors, and spreading. Attacking the systems behind apps is easier than breaking the apps themselves. The exploits are simple but still work, giving attackers easy access.

AI tools are also part of the problem now. They trust bad input and take real actions, which makes the damage bigger. Then there are quieter issues. Apps take data they should not. Devices behave in strange ways. Attackers keep testing what they can get away with. No noise. Just ongoing damage.

Here is the list for this week’s ThreatsDay Bulletin.

1. State-backed crypto heist

   [North Korea Likely Behind KelpDAP $290M Crypto Heist](https://www.coindesk.com/tech/2026/04/20/kelp-dao-claims-layerzero-s-default-settings-are-what-actually-caused-the-usd290-million-disaster)

   Inter-blockchain communication protocol LayerZero has [revealed](https://x.com/LayerZero_Core/status/2046081551574983137) that North Korean threat actors tracked TraderTraitor may have been behind the [recent hack](https://www.coindesk.com/tech/2026/04/20/kelp-dao-claims-layerzero-s-default-settings-are-what-actually-caused-the-usd290-million-disaster) of decentralized finance (DeFi) project KelpDAO, resulting in the theft of $290 million. "The attack was specifically engineered to manipulate or poison downstream RPC infrastructure by compromising a quorum of the RPCs the LayerZero Labs DVN relied upon to verify transactions," LayerZero said. KelpDAO, in a [post](https://x.com/KelpDAO/status/2046332070277091807) on X, said, "Two RPC nodes hosted by LayerZero were compromised. A simultaneous DDoS attack was launched against the third RPC node. This was an attack on LayerZero's infrastructure. Kelp's own systems were not involved in building or operating that infrastructure." Meanwhile, the Arbitrum Security Council has [temporarily frozen](https://x.com/arbitrum/status/2046435443680346189) the 30,766 ETH being held in the address on Arbitrum One that is connected to the KelpDAO exploit. In an analysis published today, Chainalysis [said](https://www.chainalysis.com/blog/kelpdao-bridge-exploit-april-2026/): "Crucially, this was not a smart contract hack, but a sophisticated attack on off-chain infrastructure. The attackers compromised internal RPC nodes and DDoS’d external nodes to feed false data to a single-point-of-failure verification network (a 1-of-1 DVN setup). This tricked the Ethereum contract into releasing funds based on a phantom token 'burn' on the source chain." It's worth noting that TraderTraiter was attributed to the mega [Bybit hack](https://thehackernews.com/2025/03/safewallet-confirms-north-korean.html) in early 2025 that led to the theft of $1.5 billion in digital assets. Recently, Lazarus Group was also [linked](https://thehackernews.com/2026/04/285-million-drift-hack-traced-to-six.html) to the $285 million theft from the Drift Protocol.
2. Active RCE exploits

   [MajorDoMo Flaws Come Under Exploitation](https://nvd.nist.gov/vuln/detail/CVE-2026-27175)

   Separately, VulnCheck has warned of attacks attempting to exploit two flaws in MajorDoMo, a smart home automation platform. While [CVE-2026-27175](https://nvd.nist.gov/vuln/detail/CVE-2026-27175) is a critical command injection vulnerability that started seeing exploitation on April 13, [CVE-2026-27174](https://nvd.nist.gov/vuln/detail/CVE-2026-27174) allows unauthenticated remote code execution via the PHP console in the admin panel and was first detected on April 18. "CVE-2026-27175 was exploited to drop a PHP webshell that delivers persistent backdoor access," VulnCheck [said](https://www.linkedin.com/posts/ccondon_kevs-infosecurity-cybersecurity-share-7452329826373283840-CvRT/). "CVE-2026-27174 saw exploitation that ended in a Metasploit php/meterpreter/reverse\_tcp staged payload." Other vulnerabilities that have witnessed exploitation efforts include [CVE-2025-22952](https://nvd.nist.gov/vuln/detail/CVE-2025-22952), an SSRF in Elestio Memos, and [CVE-2024-57046](https://nvd.nist.gov/vuln/detail/cve-2024-57046), an authentication bypass in NETGEAR DGN2200 routers.
3. Supply chain malware surge

   [New Malicious Packages Discovered](https://safedep.io/malicious-ixpresso-core-npm-rat/)

   A number of malicious packages have been discovered in the npm registry: [ixpresso-core](https://safedep.io/malicious-ixpresso-core-npm-rat/), [forge-jsx](https://safedep.io/malicious-forge-jsx-npm-rat/), [@genoma-ui/components, @needl-ai/common, rrweb-v1](https://safedep.io/malicious-genoma-ui-npm-dependency-confusion-campaign/), [cjs-biginteger, sjs-biginteger, bjs-biginteger](https://safedep.io/malicious-sjs-biginteger-npm-ssh-theft/), [@fairwords/websocket, @fairwords/loopback-connector-es, @fairwords/encryption](https://safedep.io/malicious-fairwords-npm-credential-worm/), [js-logger-pack](https://safedep.io/malicious-js-logger-pack-npm-stealer/), and [@kindo/selfbot](https://research.jfrog.com/post/astral-injection/). These packages come with features to steal sensitive data from compromised hosts, perform system reconnaissance, andimplant an SSH backdoor by injecting the attacker's public key into ~/.ssh/authorized\_keys, deliver an information stealer, and spread the [XWorm](https://thehackernews.com/2025/10/xworm-60-returns-with-35-plugins-and.html) remote access trojan (RAT). The packages published under the "@fairwords" scope have also been found to self-propagate to all npm packages using the victim's token and attempt cross-ecosystem propagation to PyPI via .pth file injection. New versions of [js-logger-pa...