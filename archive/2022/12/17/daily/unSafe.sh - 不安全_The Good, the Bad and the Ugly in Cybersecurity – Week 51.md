---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 51
url: https://buaq.net/go-140327.html
source: unSafe.sh - 不安全
date: 2022-12-17
fetch_date: 2025-10-04T01:46:27.991281
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 51

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/e4e32da59a8622f24040d1832e23b733.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 51

The GoodThe latest dose of justice in the cyber threat landscape: U.S. authorities this week seize
*2022-12-16 22:0:12
Author: [www.sentinelone.com(查看原文)](/jump-140327.htm)
阅读量:36
收藏*

---

## The Good

The latest dose of justice in the cyber threat landscape: U.S. authorities this week [seized](https://www.justice.gov/usao-cdca/pr/federal-prosecutors-los-angeles-and-alaska-charge-6-defendants-operating-websites) 48 internet domains selling “booter” and “stresser” services used by low-level hackers to launch powerful [Distributed Denial of Service (DDoS)](https://www.sentinelone.com/cybersecurity-101/what-is-denial-of-service-dos/) attacks. The DOJ has charged six individuals with computer crimes for their alleged relations to these services.

![](https://www.sentinelone.com/wp-content/uploads/2022/12/ddoS-seizure-48_jpg__1600×898_.png)

DDoS attacks are designed to overwhelm websites with fake traffic until the intended target, ranging from individuals and websites to entire network providers, is eventually rendered offline. According to the DOJ, the services in this action reportedly attacked victims in both the U.S. and abroad, including government agencies, [educational institutions](https://www.sentinelone.com/blog/cyber-risks-in-the-education-sector-why-cybersecurity-needs-to-be-top-of-the-class/), gaming platforms, and millions of individual users.

In a sly effort to offload legal ramifications, the booter websites had attempted to hide behind lengthy terms and conditions which required customers to agree that services would only be used for network stress-testing purposes. The DOJ, however, has dismissed those claims using communications between site administrators and their customers as evidence of their intended malicious use.

Cybercrime-as-a-Service models have multiplied in the threatscape resulting in the number of DDoS attacks climbing in recent years. Booter services especially have created a low barrier to entry to cybercrime. The seized domains allowed purchasers to choose the volume of fake traffic to be sent as well as the number and duration of synchronized attacks that follow. Such services give non-technical users the ability to bombard essential services and critical infrastructure, draining their victims of time and money, as well as causing reputational harm.

Law enforcement have responded with [Operation PowerOff](https://www.europol.europa.eu/media-press/newsroom/news/global-crackdown-against-ddos-services-shuts-down-most-popular-platforms); an ongoing coordination between internal agencies to dismantle DDoS-for-hire administrators and users. The takedown this week preempts a new wave of DDoS attacks as cyber criminals often favor the [holiday](https://www.sentinelone.com/blog/5-cyber-scams-to-watch-out-for-this-holiday-season/) season to launch.

## The Bad

Notorious [LockBit](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques/) ransomware group has claimed a cyberattack on the California Department of Finance this week. While LockBit’s leak site posits that they made away with several gigabytes’ worth of confidential data, databases, and both financial and IT documents, California Office of Emergency Services (Cal OES) only [confirmed](https://news.caloes.ca.gov/statement-on-cybersecurity-incident/) the security intrusion and stated that “no state funds have been compromised”. Officials have given no further specifics except that state and federal security partners are working with threat hunting experts to continue the investigation.

The cyberattack on the Californian finance sector follows the DOJ’s recent arrest of accused LockBit threat actor, [Mikhail Vasiliev](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-46-4/). The Russian-Canadian’s capture from just last month was the result of a two-year FBI investigation into LockBit’s operations and related ransomware attacks on the U.S. and organizations across several other countries.

LockBit has been [described](https://www.justice.gov/opa/pr/man-charged-participation-lockbit-global-ransomware-campaign) by the DOJ as “one of the most active and destructive ransomware variants in the world.” LockBit associates have, since their first appearance in early 2020, extracted tens of millions of dollars from at least 1000 victims in various countries.

> [#LockBit](https://twitter.com/hashtag/LockBit?src=hash&ref_src=twsrc%5Etfw) has listed the State of California’s Finance Department. It should be noted that not all of LockBit’s past claims have been true. 1/2 [#ransomware](https://twitter.com/hashtag/ransomware?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/jmf5ap15xz](https://t.co/jmf5ap15xz)
>
> — Brett Callow (@BrettCallow) [December 12, 2022](https://twitter.com/BrettCallow/status/1602325828096098305?ref_src=twsrc%5Etfw)

Back in June, LockBit’s claims to have breached cybersecurity firm Mandiant were [dismissed](https://www.bleepingcomputer.com/news/security/mandiant-no-evidence-we-were-hacked-by-lockbit-ransomware/) after the firm’s internal investigation found no evidence of breach or LockBit ransomware. What is now widely understood to be a PR stunt by LockBit shows that ransomware operators are going to extensive lengths to support their criminal operations, even using public relation plays to adapt and persist in an evolving threat landscape.

## The Ugly

[PyPI](https://www.sentinelone.com/labs/pypi-phishing-campaign-juiceledger-threat-actor-pivots-from-fake-apps-to-supply-chain-attacks/) and NPM code repositories are under active attack by malware. This week, software supply chain firm Phylum [reported](https://blog.phylum.io/phylum-detects-active-typosquatting-campaign-in-pypi) a campaign targeting Python and JavaScript developers after it identified several suspicious Python requests packages. Through the use of fake modules and typosquatting, the campaign is luring victims into downloading malicious pieces of code. [PyPI](https://www.sentinelone.com/labs/use-of-obfuscated-beacons-in-pymafka-supply-chain-attack-signals-a-new-trend-in-macos-attack-ttps/) is a prominent code repository for Python programming language hosting over 350,000 software packages while its JavaScript counterpart, NPM, is the hub for more than one million such packages.

The cyber criminals behind the campaign have been reported to leverage typosquatting, a technique that involves delivering malware from files that have been named very similarly to legitimate pieces of code. So far, the typosquatted Python packages are:

```
dequests, fequests, gequests, rdquests, reauests, reduests, reeuests, reqhests, reqkests, requesfs, requesta, requeste, requestw, requfsts, resuests, rewuests, rfquests, rrquests, rwquests, telnservrr, and tequests
```

Typosquatted JavaScript modules in NPM have been identified as:

```
discordallintsbot, discordselfbot16, discord-all-intents-bot, discors.jd, discord-selfbot-v13, discord-all-intents-default, telnservrr.
```

The typosquatting used in the campaign leads to packages embedded with [Golang](https://www.sentinelone.com/labs/cratedepression-rust-supply-chain-attack-infects-cloud-ci-pipelines-with-go-malware/) binaries detected as malware. Once unsuspecting developers execute the binaries, the malware encrypts files in the background, and updates the device’s desktop background with an image impersonating the CIA that instructs the victim to pay for a decryption key.

![...