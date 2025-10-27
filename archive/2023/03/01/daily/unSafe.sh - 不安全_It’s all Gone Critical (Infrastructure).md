---
title: It’s all Gone Critical (Infrastructure)
url: https://buaq.net/go-151399.html
source: unSafe.sh - 不安全
date: 2023-03-01
fetch_date: 2025-10-04T08:19:05.763079
---

# It’s all Gone Critical (Infrastructure)

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

It’s all Gone Critical (Infrastructure)

We have long recognised that large parts of our civilian infrastructure are critical to our liv
*2023-2-28 20:26:4
Author: [www.forcepoint.com(查看原文)](/jump-151399.htm)
阅读量:24
收藏*

---

We have long recognised that large parts of our civilian infrastructure are critical to our lives and well-being and need special protection—things like our personal finances and energy consumption and distribution. They keep the country going, and without them we quickly return to the Stone Age. But these emerging reports highlight more and more areas that are critical. And stakes increase for infrastructure attacks, like the Iranian nation state ones [Albania recently suffered](https://www.cisa.gov/uscert/ncas/alerts/aa22-264a) (on a related note, this [recent WEF panel discussion](https://www.weforum.org/videos/davos-am23-securing-critical-infrastructure-english) with Prime Minister Rama and other experts is well worth a watch). Or when hundreds of patients [were denied healthcare](https://www.nbcnews.com/tech/security/ransomware-attack-delays-patient-care-hospitals-us-rcna50919) across hospitals after a massive ransomware attack.

**Dependency makes more things critical**

Sometimes technology creates new potential vulnerabilities that we didn’t have to worry about before. As we switch from oil powered to electric cars, for example, we become dependent on the highly interconnected and highly vulnerable EV charging points. And these days, as we grow more dependent on using smartphones to communicate multiple times a day, being able to rely on their connectivity is more important than ever, especially during emergencies. In this context, what’s defined as critical infrastructure seems to expand continuously. Perhaps now, we’re better served asking what infrastructure isn’t critical, rather than what is.

Besides the expanding nature of what can be called critical infrastructure, the other challenge remains protecting it effectively. If we look at modern operating systems, and the applications we use with them, they are packed with security controls - breaking into them should be astonishingly difficult, and yet it doesn’t seem to be.

Technology lag is part of the reason. It’s clear that lots of organizations don’t use the latest equipment both in terms of hardware and software. Many hospitals for example, use outdated machines simply because they can’t afford to upgrade. It’s a similar story for industrial plants—not because of affordability, but because there’s simply few actual opportunities to upgrade.

**Analysts tend to skip the origin**

When we read reports of a hack in the technical press, we often get some detailed diagnosis of what happened by some researcher who has spent considerable time working out what the attackers did. But rarely does this work tell us how the attack started. Almost always the report is about what the attack did once it got going, and that’s because the evidence is there to analyse, whereas the point of entry is something small and obscure and the evidence is lost or destroyed. Mostly we just hear that somehow the attacker got a victim to run some code that was the initial stage of the attack.

Looking at these reports, it’s obvious that most of them start by the initial victim running the attacker’s code. And as soon as even a little bit of code is run, whether it is a macro or some fileless malware, the attacker then cleverly uses this to run increasingly more complicated code, bootstrapping themselves into a position of total control over your system. A bit like the crack in a dam, that starts with a little trickle but gradually erodes into a stream, then a torrent and finally ends up with a catastrophic failure.

**Clear benefits of keeping the attackers out**

Yes, there are exceptions, certain people in organizations do need to receive code and distribute it, but they are in a distinct minority - people like the software engineers who built the system - and they need to be tackled separately from the main bulk of users in any organisation who just don’t need to pass code around.

Stopping code is a very effective measure. Looking at a collection of [30 million pieces of malware](https://www.forcepoint.com/resources/reports/30-million-viruses-no-problem-zero-trust-cdr), just over 95% of those samples are code – the rest are malformed data of some kind. Typical anti-virus scanning is at best 90% effective so CDR beats it hands down.

But CDR only works if it can get into the data flows. Unlike anti-virus, it can’t sit on every desktop and check files before they are used – the attack might start before the CDR has a chance to intervene, and the time it takes to clean a whole file would ruin the user’s experience with a noticeable delay. We need to put CDR at the boundary of our systems, between us and the attackers, and also along internal boundaries to stop the spread of an attack that manages to hit its first victim.

Fortunately, the world is moving in a direction that makes this easy: The cloud. As we use central cloud services as the means of sharing information, the cloud service becomes the natural place to tackle malware. CDR can be injected into these services, either directly or by security addons such as Cloud Access Security Brokers (CASBs). The old vulnerable equipment used in so many of the systems we rely on doesn’t get touched. The flaws in it remain, but they become inaccessible – the attacker cannot get to them to exploit them. This buys time to get everything updated to the latest and greatest.

文章来源: https://www.forcepoint.com/blog/x-labs/all-gone-critical-infrastructure
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)