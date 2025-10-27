---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 33
url: https://buaq.net/go-174791.html
source: unSafe.sh - 不安全
date: 2023-08-19
fetch_date: 2025-10-04T11:59:20.265866
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 33

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

![]()

The Good, the Bad and the Ugly in Cybersecurity – Week 33

The Good | DigiHeals Aims to Boost Resilience of Healthcare Sector to Fight Off Cyber AttacksThe h
*2023-8-18 21:0:27
Author: [www.sentinelone.com(查看原文)](/jump-174791.htm)
阅读量:15
收藏*

---

## The Good | DigiHeals Aims to Boost Resilience of Healthcare Sector to Fight Off Cyber Attacks

The healthcare sector has borne a particularly tough brunt of attacks over the last few years as ransomware-wielding cybercriminals have sought easy-pickings from often-under-resourced public services. Good news this week, then, as the Biden-Harris administration’s ARPA-H project has launched a digital health security initiative to help ensure patients continue to receive care in the wake of a medical facility cyberattack.

The initiative, dubbed DigiHeals, aims to encourage proposals for proven technologies developed for national security and apply them to civilian health systems, clinical care facilities, and personal health devices.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/health-team-scaled.jpg)

The aim is to focus on [cutting-edge security](https://www.sentinelone.com/platform) protocols, [vulnerability detection](https://www.sentinelone.com/press/sentinelone-streamlines-vulnerability-management-with-singularity-ranger-insights/), and automatic [patching](https://www.sentinelone.com/blog/enterprise-security-essentials-top-12-most-routinely-exploited-vulnerabilities/) in order to limit the ability for threat actors to attack digital health software, with the ultimate objective being to ensure continuity of care for patients in the wake of a cyberattack on a medical facility.

Aside from a lack of cybersecurity resources, [healthcare services](https://www.sentinelone.com/lp/healthcare-under-attack-actionable-advice-and-lessons-learned/) present unique [problems for digital defense](https://www.sentinelone.com/blog/healthcare-cybersecurity-how-to-strengthen-defenses-against-cyber-attacks/), as medical facility networks are typically made up of a vast patchwork of disparate devices, systems, and services. The DigiHeals project hopes to encourage submissions from researchers, both amateur and professional, from a wide range of fields and expertise. Accepted proposals related to vulnerability detection, software hardening, and system patching, as well as the expansion or development of security protocols, will receive funding and further support from the project.

## The Bad | Actively Exploited Citrix Vulnerabilities May Pose Threat Evan After Patching

Bad news for Citrix users this week as CISA are warning that cyber adversaries are making widespread use of two n-day vulnerabilities, CVE-2023-24489 and CVE-2023-3519. Neither are new, but in-the-wild exploitations are on the rise, with some admins having patched their systems but failing to check whether they had already been breached.

[CVE-2023-3519](https://nvd.nist.gov/vuln/detail/CVE-2023-3519) is a vulnerability in Citrix’s networking product NetScalers, first disclosed last month. Researchers [say](https://blog.fox-it.com/2023/08/15/approximately-2000-citrix-netscalers-backdoored-in-mass-exploitation-campaign/) that almost 70% of patched NetScalers still contain a backdoor, indicating that admins applied the patch after the bug had been successfully exploited and did not check or discover the compromise.

> Over 1,900+ Citrix NetScaler instances breached in a massive attack exploiting critical [#vulnerability](https://twitter.com/hashtag/vulnerability?src=hash&ref_src=twsrc%5Etfw).
>
> Hackers used automated methods to install web shells, gaining unauthorized access even after patches.
>
> Details: <https://t.co/DowI4QRzhR>[#cybersecurity](https://twitter.com/hashtag/cybersecurity?src=hash&ref_src=twsrc%5Etfw) [#infosec](https://twitter.com/hashtag/infosec?src=hash&ref_src=twsrc%5Etfw) [#hacking](https://twitter.com/hashtag/hacking?src=hash&ref_src=twsrc%5Etfw)
>
> — The Hacker News (@TheHackersNews) [August 16, 2023](https://twitter.com/TheHackersNews/status/1691666772078833864?ref_src=twsrc%5Etfw)

According to the researchers, it appears an [adversary](https://www.sentinelone.com/blog/how-to-stay-ahead-of-the-adversary-in-2022-a-cybersecurity-checklist/) exploited the bug in an automated fashion in mid-July, dropping webshells on vulnerable systems. The webshells allow for the execution of arbitrary commands, even if the NetScaler is subsequently patched or rebooted.

Equally concerning, [CVE-2023-24489](https://nvd.nist.gov/vuln/detail/CVE-2023-24489) is a bug with a CVSS score of 9.1 out of 10 affecting the Citrix Content Collaboration tool ShareFile. Exploitation allows an unauthenticated attacker to remotely compromise customer-managed ShareFile storage zones controllers.

CISA [advised](https://www.cisa.gov/news-events/alerts/2023/08/16/cisa-adds-one-known-exploited-vulnerability-catalog) on Wednesday that the bug was being actively exploited. Researchers at GreyNoise [reported](https://www.greynoise.io/blog/introducing-cve-2023-24489-a-critical-citrix-sharefile-rce-vulnerability) a steep spike in attacker activity around CVE-2023-24489 after the advisory went public, indicating that attackers are racing against time to exploit vulnerable instances before security teams plug the gap.

Researchers believe there are anywhere between 1000-6000 vulnerable instances that are accessible from the public internet.

In both cases, admins are urged both to patch without delay and to investigate whether a compromise may have already occurred.

## The Ugly | Free Cloud Storage Services Abused By Threat Actors Phishing for Microsoft Credentials

[Cloud security](https://www.sentinelone.com/cybersecurity-101/cloud-security/) is in the spotlight again this week as cloud storage service Cloudflare R2 has [reportedly](https://thehackernews.com/2023/08/cybercriminals-abusing-cloudflare-r2.html) seen a 61-fold increase in hosted phishing pages in the last six months. R2, which offers a similar service to Azure blob and AWS S3, is being used for campaigns that primarily phish for Microsoft login credentials, although Adobe, Dropbox and other cloud apps’ login pages have also been targeted.

The massive increase may relate to the fact that R2, a relatively new entrant in the field of cloud storage, offers some free services to attract customers that [threat actors](https://www.sentinelone.com/resources/threat-actor-basics-understanding-the-5-main-threat-types/) have found useful to abuse. First, [fake login pages](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) are hosted on a free subdomain that can be reused without limit. The domains all have the pattern:

```
https://pub-<32_alphanumeric_string>.r2.dev
```

Second, Cloudflare offers a free CAPTCHA service called Turnstile to help legitimate websites reduce spam. The threat actors have deployed Turnstile to prevent URL scanners and internet analyzers from examining the [phishing](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) pages’ content and marking them as dangerous. The use of the CAPTCHA has the added bonus of making the site seem more legitimate to unsuspecting users.

In addition, victims are redirected to the phishing pages from other malicious websites, and the former only serve up the fake login pages if the referring sites are recognized as the source. Researchers [say](https://www.netskope.com/blog/evasive-phishing-campaign-steals-cloud-credentials-using-cloudflare-r2-and-turnstile) that referring web pages include a timestamp after a hash (`#`) symbol in the URL. If the URL parameter is missing,...