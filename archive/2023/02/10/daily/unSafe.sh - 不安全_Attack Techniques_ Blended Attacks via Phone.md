---
title: Attack Techniques: Blended Attacks via Phone
url: https://buaq.net/go-148731.html
source: unSafe.sh - 不安全
date: 2023-02-10
fetch_date: 2025-10-04T06:12:30.148084
---

# Attack Techniques: Blended Attacks via Phone

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

![](https://8aqnet.cdn.bcebos.com/82a95922c7374fa901d16c9d803bbbf3.jpg)

Attack Techniques: Blended Attacks via Phone

Last month, we looked at a technique where a phisher serves his attack from the
*2023-2-9 22:25:0
Author: [textslashplain.com(查看原文)](/jump-148731.htm)
阅读量:32
收藏*

---

Last month, we looked at [a technique](https://textslashplain.com/2023/01/11/attack-techniques-phishing-via-local-files/) where a phisher serves his attack from the user’s own computer so that anti-phishing code like SmartScreen and SafeBrowsing do not have a meaningful URL to block.

Another approach for conducting an attack like this is to send a lure which demands that the victim complete the attack out-of-band using a telephone. Because the data theft is not conducted over the web, URL reputation systems don’t have anything to block.

Here’s an example of such a scam, which falsely claims that the user was charged $400 for one of the free programs already on their PC:

[![](https://textplain.files.wordpress.com/2023/02/image-2.png?w=793)](https://textplain.files.wordpress.com/2023/02/image-2.png)

The attacker hopes that the user, upon seeing this charge, will call the phone number within the email and get tricked into supplying sensitive information. This particular scam’s phone number is routed to a call center purporting to be “Microsoft Support.”

Evidence suggests that some email services have gotten wise to this scam: because the phone number needs only be read by a human, attackers may try to evade detection and blocking by encoding their phone numbers using non-digit characters or irregular formatting, as in this lure:

[![](https://textplain.files.wordpress.com/2023/02/image-3.png?w=883)](https://textplain.files.wordpress.com/2023/02/image-3.png)

Unfortunately, relatively few phones offer any mechanism for warning the user when they’re calling a known-scam number — Google’s “Scam Likely” warnings only seem to show on the Pixel for *inbound calls*. As with traditional phishing attacks, bad actors can usually switch their infrastructure easily after they are blocked.

Stay safe out there!

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-2022, working on Office, IE, and Edge. Now a SWE on Microsoft Defender Web Protection. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

文章来源: https://textslashplain.com/2023/02/09/attack-techniques-blended-attacks-via-phone/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)