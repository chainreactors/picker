---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 9
url: https://buaq.net/go-151892.html
source: unSafe.sh - 不安全
date: 2023-03-04
fetch_date: 2025-10-04T08:37:14.623522
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 9

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

![](https://8aqnet.cdn.bcebos.com/0edd076b8ff26748364f217f8ba00dd7.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 9

The GoodIn a first for the U.S., a coordinated, national cybersecurity strategy was unveiled this
*2023-3-3 22:0:53
Author: [www.sentinelone.com(查看原文)](/jump-151892.htm)
阅读量:23
收藏*

---

## The Good

In a first for the U.S., a coordinated, national cybersecurity strategy was unveiled this week as the government continues its campaign to get on top of a cybersecurity problem that has [spiraled out of control](https://www.sentinelone.com/blog/the-national-cybersecurity-strategy-how-the-us-government-plans-to-protect-america/) in recent years.

The National Cybersecurity Strategy is an ambitious, five-pronged approach that seeks to defend [critical infrastructure](https://www.sentinelone.com/blog/securing-the-nations-critical-infrastructure-action-plans-to-defend-against-cyber-attacks/), disrupt threat actors, promote data privacy and security, invest in cyber resilience, and forge international partnerships to fight cyber threats.

The strategy comes as the latest response to the attacks on [schools](https://www.sentinelone.com/blog/cyber-risks-in-the-education-sector-why-cybersecurity-needs-to-be-top-of-the-class/), [healthcare](https://www.sentinelone.com/blog/venus-ransomware-zeoticus-spin-off-shows-sophistication-isnt-necessary-for-success/), [energy suppliers](https://www.sentinelone.com/blog/meet-darkside-and-their-ransomware-sentinelone-customers-protected/) and [food production](https://www.sentinelone.com/blog/when-jbs-met-revil-ransomware-why-we-need-to-beef-up-critical-infrastructure-security/) outlets that have plagued the nation in recent years. Recognizing that [nation-state espionage](https://www.sentinelone.com/labs/wip26-espionage-threat-actors-abuse-cloud-infrastructure-in-targeted-telco-attacks/) and [supply chain attacks](https://www.sentinelone.com/labs/cratedepression-rust-supply-chain-attack-infects-cloud-ci-pipelines-with-go-malware/) are also complex problems that need both investment and coordination between diverse entities, the government’s National Cybersecurity Strategy has itself been developed through consultation with both public and private sector companies and experts.

> Today, [@POTUS](https://twitter.com/POTUS?ref_src=twsrc%5Etfw) released the National Cybersecurity Strategy. The Strategy sets forth a new vision for the future of cyberspace and the wider digital ecosystem. [pic.twitter.com/u3gxfJXymS](https://t.co/u3gxfJXymS)
>
> — The Office of the National Cyber Director (@ONCD) [March 3, 2023](https://twitter.com/ONCD/status/1631478187711496195?ref_src=twsrc%5Etfw)

SentinelOne’s [Juan Andres Guerrero-Saade](https://www.sentinelone.com/blog/author/jags/), Senior Director of the company’s threat intelligence and research arm [SentinelLabs](https://www.sentinelone.com/labs/), said that leaving security investments entirely up to the market had proven ineffective, and that the government’s plan was both timely and necessary. The strategy will help to reshape market dynamics to incentivize and reward security investment, he [said](https://www.sentinelone.com/blog/the-national-cybersecurity-strategy-how-the-us-government-plans-to-protect-america/).

Although the implementation details of the strategy remain to be seen, SentinelOne recognizes the importance of the approach and is committed to supporting it in the fight to secure and protect the digital landscape for all.

## The Bad

Cryptojacking, it seems, is back in fashion. Cryptomining campaigns appeared to have waned after in-browser cryptojacking became more or less tapped out due to improved browser security, but campaigns to infect home, enterprise and now cloud hosts with stealthy resource-stealing malware have quietly been burrowing away in the dark.

This week, a new cryptojacking [campaign](https://www.cadosecurity.com/redis-miner-leverages-command-line-file-hosting-service/) targeting Redis database servers was brought to light. The campaign makes novel use of the popular file transfer service `transfer.sh`, a command line utility for sharing files over the internet. Many cloud-focused malware campaigns use shell scripts, and services like `transfer.sh` and pastebin are ideal for hosting and retrieving malicious payloads.

In this case, threat actors used the command line file transfer service to host scripts that dropped the XMRig cryptocurrency miner, terminated any competing miners, and installed the `pnscan` network scanner to discover other vulnerable Redis servers and spread the infection.

![redis cryptominer](https://www.sentinelone.com/wp-content/uploads/2023/03/Screenshot-2023-03-03-at-1.07.17-PM.jpg)

The campaign follows on the heels of renewed activity by [8220 Gang](https://www.sentinelone.com/blog/soc-team-essentials-how-to-investigate-and-track-the-8220-gang-cloud-threat/), who also propagate XMRig to surreptitiously mine cryptocurrency on compromised enterprise cloud workloads, and the recent discovery of [Honkbox](https://www.sentinelone.com/blog/hunting-for-honkbox-multistage-macos-cryptominer-may-still-be-hiding/), a novel XMRig cryptomining malware that uses I2P tunnels to hide its traffic, which has been quietly targeting macOS endpoints for over three years.

Aside from the increased costs due to the heavy use of electricity that cryptomining infections can cause, it’s also worth noting that in most cases, the miner is a separate stage payload from the dropper or infection vector. That means that while these campaigns may currently be focusing on stealing electricity to mine cryptocurrency, the threat actors could just as easily drop a different, more destructive or profitable payload should they wish. Securing those endpoints against any intrusion is the only safe way to operate.

## The Ugly

More hard knocks for password manager LastPass this week after [news](https://arstechnica.com/information-technology/2023/02/lastpass-hackers-infected-employees-home-computer-and-stole-corporate-vault/) broke of yet another hack in the wake of an earlier compromise. This time, in a highly-targeted attack, a decrypted LastPass vault was stolen from an employee, giving attackers access to a cloud-storage environment containing encryption keys for customer vault backups.

The attack, which took place between August and October last year, leveraged data stolen in the first attack even before LastPass had completed its initial mitigation.

In a [statement](https://support.lastpass.com/help/incident-2-additional-details-of-the-attack), the company revealed that the threat actor targeted one of only four DevOps engineers who had access to decryption keys needed to access a LastPass cloud storage service. The employee’s home computer was infected with a keylogger that then captured the employee’s master password as it was entered after [MFA authentication](https://www.sentinelone.com/blog/has-mfa-failed-us-how-authentication-is-only-one-part-of-the-solution/). The compromise was effected through exploiting a vulnerability in an unnamed “third-party media software package”. This afforded the attacker remote code execution capabilities and the opportunity to plant the keylogger.

[![](https://www.sentinelone.com/wp-content/uploads/2023/03/Screenshot-2023-03-03-at-1.17.06-PM.jpg)](https://support.lastpass.com/home)

The attack initially did not raise suspicions as the login behavior appeared indistinguishable from legitimate activity, but alerts from AWS flagged up anomalous behavior when the threat actor tried to use [IAM roles](https://www.sentinelone.com/blog/itdr-for-the-w...