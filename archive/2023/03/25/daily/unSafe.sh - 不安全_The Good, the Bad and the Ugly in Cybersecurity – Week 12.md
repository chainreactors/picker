---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 12
url: https://buaq.net/go-155136.html
source: unSafe.sh - 不安全
date: 2023-03-25
fetch_date: 2025-10-04T10:36:13.842270
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 12

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

![](https://8aqnet.cdn.bcebos.com/0edad6ca7d35d014bdb64b6956fe007d.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 12

The GoodDark forum site operator, ‘Pompompurin’, was arrested this week by U.S. law enforcement on
*2023-3-24 21:0:8
Author: [www.sentinelone.com(查看原文)](/jump-155136.htm)
阅读量:22
收藏*

---

## **The Good**

Dark forum site operator, ‘Pompompurin’, was arrested this week by U.S. law enforcement on the charge of conspiracy to commit access device fraud. One Conor Brian Fitzpatrick was arrested in his home where he admitted this alias and to owning and administrating the website, BreachForums, well-known across the cybercrime ecosystem for hosting stolen databases and selling personal data for fraudulent activities. Officials [reported](http://www.documentcloud.org/documents/23713130-pompourin-affidavit-govuscourts) that Fitzpatrick had been under close investigation for over a year before the arrest.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/pompompurin_breachforums_offline.jpg)

After the DoJ announced the successful seizure of the RaidForums website in April of 2022, it was widely speculated that Fitzpatrick created BreachForums as its successor. Since then, BreachForums has gained notoriety for being one of the most active hacker forums available to cybercriminals.

Under the Pompompurin alias, Fitpatrick quickly filled in the gap of selling and leaking sensitive information through social media, propelling the site to becoming one of the largest data leak forums of its kind. Fitzpatrick has also been connected to various high-profile cyberattacks, including those involving the [FBI](https://securityintelligence.com/news/fbi-database-breach-exposes-agents/), [Twitter](https://privacy.twitter.com/en/blog/2022/an-issue-affecting-some-anonymous-accounts), and popular online stock trading platform, [Robinhood](https://www.wsj.com/articles/robinhood-hack-exposes-millions-of-customer-names-email-addresses-11636408263). At the time of its takedown, BreachForums had more than 330000 members, 47000 threads, and almost one million posts.

Though the site is now defunct, these seizures remain critical in the uphill fight against increasingly sophisticated cybercrime syndicates. BreachForums was just one of many leak sites and dark marketplaces causing ongoing damage to [government](https://www.sentinelone.com/blog/why-governments-and-agencies-are-targeted-by-cyber-attacks-a-deep-dive-into-the-motives/) organizations and enterprises of all industries. Just as BreachForums rose from the ashes of RaidForums, it is vital for businesses to remain vigilant with protecting their data from opportunistic threat actors as new forums inevitably continue to propagate.

## **The Bad**

A new Go-based, [DDoS](https://www.sentinelone.com/cybersecurity-101/what-is-a-distributed-denial-of-service-ddos/)-focused malware dubbed ‘HinataBot’ hit the scene this week, taking its name from the popular anime series, *Naruto*. According to [researchers](https://www.akamai.com/blog/security-research/hinatabot-uncovering-new-golang-ddos-botnet), the threat actors behind the new malware were first observed in December of last year and have since started to develop their own malware approximately two months ago. Current indications point to the malware’s active evolution as it is updated by its authors and operators.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/naruto.jpg)

HinataBot is written in [Golang](https://www.sentinelone.com/labs/alphagolang-a-step-by-step-go-malware-reversing-methodology-for-ida-pro/) and is the latest in emerging [Go-based threats](https://www.sentinelone.com/labs/dragonspark-attacks-evade-detection-with-sparkrat-and-golang-source-code-interpretation/) that continue to proliferate in the cyber underground. Go is increasingly in use by attackers for its high performance and support for multiple architectures. Security researchers have [noted](https://www.sentinelone.com/labs/alphagolang-a-step-by-step-go-malware-reversing-methodology-for-ida-pro/) that Go-based malware presents extra challenges to analyze and reverse engineer.

So far, samples of the malware have been discovered in HTTP and SSH honeypots, where they have been observed abusing weak credentials and old remote code execution (RCE) vulnerabilities from as far back as nearly a decade ago. Analysis on the infection process for HinataBot has shown exploitation of the `miniigd` SOAP service on Realtek SDK devices ([CVE-2014-8361](https://nvd.nist.gov/vuln/detail/CVE-2014-8361)), Huawei HG532 routers ([CVE-2017-17215](https://nvd.nist.gov/vuln/detail/cve-2017-17215)), as well as exposed Hadoop YARN servers.

The discovery of HinataBot brings to light the responsibilities of organizations to deepen their visibility surrounding deployed services as well as weak spots in their overall infrastructure. In this case, nearly 10-year old vulnerabilities are still being exploited as threat actors continue to use [overlooked or low-hanging resources](https://www.sentinelone.com/blog/cybersecuritys-biggest-mistakes-of-2022/) to evade detection, build on new functionalities, and get a high return on through small investments.

## **The Ugly**

In a joint technical report released this week by SentinelLabs researchers and QGroup GmbH, telecom providers in the Middle East have become the latest target in a long-running cyberattack campaign dubbed [Operation Tainted Love](https://www.sentinelone.com/labs/operation-tainted-love-chinese-apts-target-telcos-in-new-attacks/). Based on the investigations, this campaign has been attributed to Chinese-based cyber espionage threat actors.

Initial attack vectors observed in the string of cyberattacks began with the infiltration of Internet-facing Microsoft Exchange servers to deploy web shells for command execution. After securing a foothold, the attacker conducted a variety of reconnaissance, [credential theft](https://www.sentinelone.com/cybersecurity-101/identity-security-what-it-is-why-its-so-important/), [lateral movement](https://www.sentinelone.com/cybersecurity-101/lateral-movement/), and [data exfiltration](https://www.sentinelone.com/cybersecurity-101/cyber-kill-chain/) activities.

In the latest attacks on Middle Eastern telecom providers, the actors have been seen deploying a custom variant of [Mimikatz](https://www.sentinelone.com/cybersecurity-101/mimikatz/) called mim221 to facilitate lateral movement techniques and privilege escalation as well as all-new anti-detection and credential theft capabilities. Special-purpose modules like these underscore the threat actor’s drive to advance their toolset with a marked focus on stealth. Techniques noted by SentinelLabs researchers included in-memory mapping of malicious images to evade EDR API hooks and file-based detections, the termination of Event Log threads instead of the host process to inhibit logging without raising suspicions, and staging a credential theft capability in the LSASS process itself by abusing native Windows capabilities.

![mim221 execution overview](https://www.sentinelone.com/wp-content/uploads/2023/03/tainted_love_17.jpg)

mim221 Execution Overview

Telecom providers find themselves frequently in the crosshairs of attack for the large amounts of [personal client data](https://www.sentinelone.com/blog/rise-in-identity-based-attacks-drives-demand-for-a-new-security-approach/) they hold and sensitive information transmitted. This campaign is expected to continue as the Chinese-linked threat actors upgrade their [malware](https://www.sentinelone.com/cybersecurity-101/what-is-malware-everythin...