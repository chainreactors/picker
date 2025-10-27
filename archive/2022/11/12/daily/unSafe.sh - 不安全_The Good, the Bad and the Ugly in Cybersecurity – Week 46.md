---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 46
url: https://buaq.net/go-135263.html
source: unSafe.sh - 不安全
date: 2022-11-12
fetch_date: 2025-10-03T22:28:36.488843
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 46

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

![](https://8aqnet.cdn.bcebos.com/a149ed22e46e5b4508d47adf8dd98b18.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 46

The GoodA two-year FBI investigation into LockBit ransomware has led to charges this week against
*2022-11-11 22:0:9
Author: [www.sentinelone.com(查看原文)](/jump-135263.htm)
阅读量:30
收藏*

---

## The Good

A two-year FBI investigation into [LockBit ransomware](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques/) has led to charges this week against a dual Russian-Canadian citizen for allegedly conducting ransomware attacks on U.S. and other organizations around the world.

Mikhail Vasiliev, 33, was arrested in Ontario, Canada on Wednesday on charges of conspiring to damage protected computers and transmitting ransom demands in connection with doing so. He is now awaiting extradition to the U.S.

Documents filed in the case state that since the [LockBit RaaS](https://assets.sentinelone.com/ransomware-enterprise/lockbit-detect-vid) (ransomware-as-a-service) first appeared in 2020, it has been used in over 1000 attacks and garnered its operators tens of millions of dollars in confirmed ransom payments. However, Deputy AG Lisa Monaco had a [message](https://www.justice.gov/opa/pr/man-charged-participation-lockbit-global-ransomware-campaign) for those involved: *“Let this be yet another warning to ransomware actors…we will use every available tool to disrupt, deter and punish cyber criminals.”*

[![LockBit 3 ransomware leaks site](https://www.sentinelone.com/wp-content/uploads/2022/07/lockbit_3_update_7.jpg)](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques/)

It’s also not the first time Canadian police and the FBI have cooperated to arrest individuals believed to be involved in ransomware: Back in 2021, Canadian national Sébastien Vachon-Desjardins was arrested in Canada and subsequently sentenced to 20 years in a U.S. prison for his role in [Netwalker ransomware](https://www.sentinelone.com/labs/netwalker-ransomware-no-respite-no-english-required/) attacks.

## The Bad

Despite wins like those above, it’s clear that the profits from ransomware and [data extortion](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/) as well as the ease of conducting such attacks continue to incentivise threat actors. This week, the Health Sector Cybersecurity Coordination Center ([HC3](https://www.hhs.gov/sites/default/files/venus-ransomware-analyst-note.pdf)) warned that [Venus ransomware](https://www.youtube.com/watch?v=G97CeM4-E3s) is targeting U.S. healthcare entities via publicly exposed Remote Desktop Services.

HC3 says that Venus ransomware is targeting Windows devices that companies have failed to protect with a firewall or other defenses, allowing attackers to gain initial access via the Remote Desktop Service. Typically, threat actors discover vulnerable services through internet search services such as Shodan or purchase access from [Initial Access Brokers](https://www.sentinelone.com/blog/more-evil-markets-how-its-never-been-easier-to-buy-initial-access-to-compromised-networks/).

Reports suggest that Venus ransomware is likely being operated by several independent cybercrime groups. HC3 says that the malware has been observed reaching out to IP addresses in a wide variety of countries, including Denmark, France, Great Britain, Ireland, Japan, the Netherlands, Russia and the United States.

At present, there are no data leak sites associated with Venus intrusions, and the operators appear to be relying solely on file locking to extort money from victims. Ransom demands are said to start at around $20,000. Victims are reminded that [paying a ransom](https://assets.sentinelone.com/ciso/sentinel-one-ransomw-2) by no means ensures either that encrypted data will be unlocked or that the organization will not suffer further harm.

## The Ugly

In cybersecurity, trust is always a weak point that attackers will seek to abuse, and this week’s Most Odious award goes to the threat actors behind the latest attempts to infect users of open source projects hosted on PyPI and GitHub.

Researchers this week [spotted](https://research.checkpoint.com/2022/check-point-cloudguard-spectral-exposes-new-obfuscation-techniques-for-malicious-packages-on-pypi/) a malicious package on PyPI called “ApiColor” that reached out to a remote URL to download and execute code hidden in a `.png` file. The ApiColor package installed a [steganography](https://www.sentinelone.com/blog/hiding-code-inside-images-malware-steganography/) module and retrieved and executed a further second-stage malware payload.

The threat actors had set up multiple accounts on GitHub with code repositories that included the malicious PyPI package in their dependencies, hoping to infect developers or organizations that used the open source GitHub repositories. The PyPI package has since been taken down, but malware linked to some of the fake users accounts remains on GitHub at the time of writing.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/github-pypi-supply-chain-attacks.jpg)

Supply chain attacks [on PyPI](https://www.sentinelone.com/labs/use-of-obfuscated-beacons-in-pymafka-supply-chain-attack-signals-a-new-trend-in-macos-attack-ttps/) and Rust’s [crate.io](https://www.sentinelone.com/labs/cratedepression-rust-supply-chain-attack-infects-cloud-ci-pipelines-with-go-malware/) are not unknown, and seeding malicious code via GitHub repositories to infect developers and ultimately downstream users has also been seen before (e.g., in [XCSSET malware](https://www.sentinelone.com/blog/xcsset-malware-update-macos-threat-actors-prepare-for-life-without-python/)). [Steganography](https://www.sentinelone.com/blog/hiding-code-inside-images-malware-steganography/) is also a common tactic for hiding malware.

However, what makes this attack of particular concern is precisely that the vectors and TTPs are neither novel nor sophisticated, and yet the attackers invested a considerable amount of time and effort setting up an elaborate infrastructure in the knowledge that trust in external code dependencies is still a blind spot for many organizations. The warning shots have been fired, and security teams need to be sure that they are [on top of the supply chain risk](https://www.sentinelone.com/blog/defending-the-enterprise-against-digital-supply-chain-risk-in-2022/) across their software stack.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-46-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)