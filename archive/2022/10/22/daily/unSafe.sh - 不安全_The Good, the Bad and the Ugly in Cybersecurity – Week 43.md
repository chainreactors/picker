---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 43
url: https://buaq.net/go-132044.html
source: unSafe.sh - 不安全
date: 2022-10-22
fetch_date: 2025-10-03T20:34:51.102796
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 43

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

![](https://8aqnet.cdn.bcebos.com/6ef2e55acc3659b7e37014749ebeff73.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 43

The GoodOfficials have busted two SIM hijackers for a six-month cyber crime spree which stripped a
*2022-10-21 21:0:45
Author: [www.sentinelone.com(查看原文)](/jump-132044.htm)
阅读量:28
收藏*

---

## The Good

Officials have busted two SIM hijackers for a six-month cyber crime spree which stripped a total of $550,000 from prominent cryptocurrency figures across the U.S. This week, Eric Meiggs (24) and Declan Harrington (22) were charged with wire fraud, conspiracy, computer fraud and abuse, and aggravated identity theft, earning them each two year sentences.

The [DoJ reports](https://www.justice.gov/opa/pr/two-men-sentenced-nationwide-scheme-steal-social-media-accounts-and-cryptocurrency) that Meiggs and Harrington used SIM swapping and hacking tactics to take over their targets’ email addresses, social media handles, and cell phone numbers linked to cryptocoin accounts. The scheme included sending hostile messages to the targets, sometimes threatening their family members if they did not comply with the demands. The pair focused their sights on cryptocurrency executives and blockchain-based business owners.

![SIM Swapping](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/GBUWk43_4_2.jpg?lossy=0&strip=1&webp=0)

SIM swapping exploits the process in which cell phone providers assign numbers to new devices. Threat actors pose as the victim to convince the provider to reassign the number from the victim’s original SIM card to one controlled by the actor. This method allows threat actors to divert password reset links and authentication codes to their own device so they can later break into crypto exchanges, online banking accounts, and email and social media accounts.

Threat actors are escalating their use of SIM swapping to target early adopters of cryptocurrency and heavy investors. The [FBI](https://www.fbi.gov/contact-us/field-offices/sanfrancisco/news/press-releases/fbi-san-francisco-warns-the-public-of-the-dangers-of-sim-swapping) have implored users to be on high alert and to avoid posting any personal data or information about their financial assets online. They also recommend users to remove sensitive documents from email accounts and to add PINs to [mobile phone](https://www.sentinelone.com/blog/mobile-threat-defense-bringing-ai-powered-endpoint-security-to-your-mobile-devices/) accounts. As the cryptocurrency space is still a relatively young one, the need for [digital identity](https://www.sentinelone.com/blog/rise-in-identity-based-attacks-drives-demand-for-a-new-security-approach/) protection continues to be significant in guarding against developing [crypto-related threats](https://www.sentinelone.com/blog/is-cryptojacking-going-out-of-fashion-or-making-a-comeback/).

## The Bad

URSNIF (*aka* [ISFB](https://www.sentinelone.com/labs/writing-malware-configuration-extractors-for-isfb-ursnif/)) malware has had a makeover, and it’s still not pretty. The [one-time banking trojan](https://www.sentinelone.com/blog/ursnif-polymorphic-delivery-mechanism-explained/) has shed its origins and has been revamped into a generic backdoor built to enable ransomware or data theft extortion operations. Researchers this week [published](https://www.mandiant.com/resources/blog/rm3-ldr4-ursnif-banking-fraud) an analysis on the malware’s milestone shift, hypothesizing that the change was to stay consistent with the [broader changes in the crimeware landscape](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/).

![Prestige ransomware](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/GBUWk43_4_1.jpg?lossy=0&strip=1&webp=0)

The new variant, dubbed LDR4, was first seen in a recent attack chain where fake invoices and job postings were emailed to unsuspecting users to lure them to visit a legitimate domain. Then, interaction with the CAPTCHA would prompt a download of a Microsoft Excel spreadsheet hiding the malware payload.

LDR4 leaves behind many features characteristic of previous URSNIF forms such as the `FJ.exe` [steganography](https://www.sentinelone.com/blog/hiding-code-inside-images-malware-steganography/) tool used to hide payloads in files. All banking features have been removed and its new set of commands are capable of loading DDL modules, starting and stopping `cmd.exe` reverse shells, running arbitrary commands, and terminating processes.

URSNIF has seen a fragmented timeline of [changes](https://research.checkpoint.com/2020/gozi-the-malware-with-a-thousand-faces/) prior to its latest transformation. The latest change trails the footsteps of other malware families that also had roots in banking fraud like [Trickbot](https://www.sentinelone.com/labs/anchor-project-for-trickbot-adds-icmp/), [Emotet](https://www.sentinelone.com/blog/emotet-story-of-disposable-c2-servers/), and Qakbot. More widely, threat actors are continuing to evolve their approach in extorting money from organizations, with many now shifting to pure [data extortion without ransomware](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/) or adopting techniques such as [partial encryption](https://www.sentinelone.com/labs/crimeware-trends-ransomware-developers-turn-to-intermittent-encryption-to-evade-detection/).

## The Ugly

Private Ukrainian and Polish transportation and logistics companies are finding themselves the target of a novel ransomware strain dubbed Prestige. Only seen in the wild as of last Tuesday, [researchers](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/) have already found that [Prestige](https://www.youtube.com/embed/J9n3KvGZZaM) shares victimology with recent Russian state-aligned activity. Perhaps not surprisingly, Prestige ransomware victims overlap with those of another malware, [HermeticWiper](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack/), which had been detected in hundreds of computers in Ukraine just hours before Russia launched a full-scale military invasion on the country.

The researchers state that the initial access vector in the recent string of attacks is still unknown, but in all instances the attack timeline began with the theft of highly privileged credentials such as [Active Directory](https://www.sentinelone.com/blog/microsoft-active-directory-as-a-prime-target-for-ransomware-operators/) admin accounts. Tracked by Microsoft as DEV-0960, the threat actors behind [Prestige ransomware](https://www.youtube.com/embed/J9n3KvGZZaM) have been observed using tools such as `winPEAS`, [comsvcs.dll](https://www.sentinelone.com/labs/log4j2-in-the-wild-iranian-aligned-threat-actor-tunnelvision-actively-exploiting-vmware-horizon/), and [ntdsutil.exe](https://www.sentinelone.com/blog/lapsus-data-breach/) to access the credentials needed to facilitate the deployment. Remote execution utilities were also noted in the campaign including `RemoteExec`, a tool often used for agentless software execution, and `impacket WMIexec`, an open-source and script-based solution used to manipulate network protocols.

While the new ransomware seems to be operating independently of known threat actor groups, concerns of the strain spreading to other countries are rising. Just earlier this year, President Biden released a [statement](https://www.whitehouse.gov/briefing-room/statements-releases/2022/03/21/statement-by-president-biden-on-our-nation...