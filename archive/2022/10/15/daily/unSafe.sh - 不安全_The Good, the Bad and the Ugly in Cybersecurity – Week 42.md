---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 42
url: https://buaq.net/go-130916.html
source: unSafe.sh - 不安全
date: 2022-10-15
fetch_date: 2025-10-03T19:54:58.099888
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 42

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

![](https://8aqnet.cdn.bcebos.com/1ae0d47f1d58362cdd568e50931da0bb.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 42

The GoodAsk most security professionals about the weakest link in any organization and the answer
*2022-10-14 21:0:53
Author: [www.sentinelone.com(查看原文)](/jump-130916.htm)
阅读量:28
收藏*

---

## The Good

Ask most security professionals about the weakest link in any organization and the answer most commonly received is: *users*. A lack of awareness regarding threats as well as poor or absent cyber hygiene practices means that [phishing and social engineering](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) are a threat actors’ favorite play.

It may come as a welcome surprise, then, to learn that according to a [new survey](https://consumer-reports-ressh.cloudinary.com/image/upload/v1664551562/Consumer-Cyber-Readiness-Report-Final_edbv9f.pdf), there’s been a marked improvement in cyber security awareness among the general public over the last three years. Coming after the pandemic and the large-scale shift to [work from home](https://www.sentinelone.com/lp/wfh/), that can only be good news for enterprise security teams.

The survey found that in 2022, some 77% of respondents said they use MFA to log into online accounts compared to only 50% in 2019. An encouraging 88% said they now use [strong passwords](https://www.sentinelone.com/cybersecurity-101/password-security-business-tips/), up 12% from three years ago. In 2019, some 31% of people said they did not use any kind of security feature to unlock their smartphones. That number is down to 15% in 2022.

![Cybersecurity awareness data](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Screen-Shot-2022-10-14-at-10.22.34-AM.jpg?lossy=0&strip=1&webp=0)

What accounts for this rise in cybersecurity awareness? The report suggests that the [coverage of cybersecurity issues](https://www.sentinelone.com/blog/category/the-good-the-bad-and-the-ugly/) and emerging digital threats in the media, the increase in data breaches and the growing awareness of ‘cookies’ and third-party trackers on personal devices are all likely to have contributed to the general perception that cyber security is an issue that affects all of us, at home and at work.

## The Bad

If it’s good news we’re all becoming more cyber aware, on the other side of the fence is the unwelcome news that threat actors are making it easier to create and conduct phishing campaigns with a new PhaaS (Phishing-as-a-Service) platform called [Caffeine](https://www.mandiant.com/resources/blog/caffeine-phishing-service-platform). While PhaaS’s are not an entirely new phenomenon, what makes Caffeine particularly troubling is that anyone can sign up for it on the public internet.

Typically, threat actors wanting to use a PhaaS need a recommendation from a current customer or must go through some kind of vetting process. Caffeine is a site hosted on the public internet which accepts applications from anyone with just an email address, researchers say. For as little as $250/month, subscribers can use the platform to create customized [phishing](https://www.sentinelone.com/blog/phishing-revealing-vulnerable-targets/) kits, generate URLs to host malware payloads, and track their campaign’s success.

![Caffeine login page](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Caffeing-login-page.jpg?lossy=0&strip=1&webp=0)

Caffeine login page

Caffeine significantly lowers the barrier to entry to would-be threat actors, offering to take care of infrastructure, fake sign-in pages, website hosting, email templates and more. The service currently targets the theft of Microsoft 365 credentials via fake sign-in pages hosted on compromised WordPress sites. Researchers say they expect to see the service expand its targets as it develops.

With competing PhaaS offerings advertising services such as 2FA and [MFA bypasses](https://www.sentinelone.com/blog/category/the-good-the-bad-and-the-ugly/), it seems that threat actors have a wealth of easy options for getting new campaigns off the ground.

Whether Caffeine’s open registration and appearance on the public internet will survive scrutiny from security researchers and law enforcement remains to be seen, but even if the service eventually retreats underground, the onus is on users and security teams to bolster their defenses. The emergence of services like these is only likely to increase the already high volume of phishing attacks being seen by enterprise security teams.

## The Ugly

Last week, Fortinet issued a private [warning](https://twitter.com/Gi7w0rm/status/1578305143530848256) to its customers of a new authentication bypass flaw affecting its FortiOS, FortiProxy and FortiSwitchManager products. This week comes the unpleasant but not entirely unexpected [news](https://www.fortiguard.com/psirt/FG-IR-22-377) that the flaw, tracked as CVE-2022-40684, is being actively exploited in the wild.

The critical flaw allows an unauthenticated attacker to perform arbitrary operations on the products’ admin interface after sending maliciously-crafted HTTPS requests. These operations include modifying admin user’s SSH keys, adding new local users, updating network configurations to reroute traffic, and initiating packet captures.

> Exploit available for critical Fortinet auth bypass bug, patch now – [@serghei](https://twitter.com/serghei?ref_src=twsrc%5Etfw)<https://t.co/oqceLu6YeP>
>
> — BleepingComputer (@BleepinComputer) [October 13, 2022](https://twitter.com/BleepinComputer/status/1580622172066050048?ref_src=twsrc%5Etfw)

CISA has added the bug to its [database](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) of Known Exploited Vulnerabilities (KEV), and FortiNet has advised organizations to hunt for the following IoC in device logs:

```
user=”Local_Process_Access”
```

In addition, those using the [affected products](https://www.fortiguard.com/psirt/FG-IR-22-377) should apply the available patches without delay. For those that cannot patch, Fortinet is advising admins to disable HTTP/HTTPS administrative interface or limit the range of IPs allowed to reach it.

In other bug-related news, Microsoft’s monthly ‘Patch Tuesday’ failed to offer fixes for the recently reported Exchange Server vulnerabilities commonly-known as [ProxyNotShell](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-40-4/) but did fix 13 other critical flaws that could allow for privilege escalation, spoofing and remote code execution. Three critical RCEs affect Microsoft Office and Word. As always, Microsoft users are urged to patch at the earliest opportunity.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-42-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)