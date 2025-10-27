---
title: Malformed signature trick can bypass Mark of the Web
url: https://buaq.net/go-132809.html
source: unSafe.sh - 不安全
date: 2022-10-27
fetch_date: 2025-10-03T20:58:24.671135
---

# Malformed signature trick can bypass Mark of the Web

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

Malformed signature trick can bypass Mark of the Web

Mark of the Web (MOTW)—the technology that ensures Windows pops a warni
*2022-10-26 22:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-132809.htm)
阅读量:18
收藏*

---

Mark of the Web (MOTW)—the technology that ensures Windows pops a warning message when trying to open a file downloaded from the Internet—is back in the news, but unfortunately not in a good way.

Bleeping Computer [reports](https://www.bleepingcomputer.com/news/security/exploited-windows-zero-day-lets-javascript-files-bypass-security-warnings/) that a recently uncovered (but somewhat old) bug has been unearthed which helps people with bad intentions to leapfrog MOTW alerts. This has, apparently, already been observed in ransomware attacks.

MOTW was originally an [Internet Explorer security feature](https://outflank.nl/blog/2020/03/30/mark-of-the-web-from-a-red-teams-perspective/). It broadened out into a way for your Windows devices to raise a warning when interacting with files downloaded from who-knows-where. Over time, it even contributed to [preventing certain types of files from running](https://nolongerset.com/motw-blocks-all-vba/). It’s a versatile, helpful thing. We most recently talked about it when [7-Zip decided to support MOTW](https://www.malwarebytes.com/blog/news/2022/06/7-zip-gets-mark-of-the-web-feature-increases-protection-for-users).

If you open a file flagged with MOTW, at the bare minimum you should see one of several messages, depending on if you're looking at file properties, or attempting to open a file which you've downloaded. It might be this:

> This file came from another computer and might be blocked to help protect this computer.

Alternatively, you might see this one instead:

> While files from the internet can be useful, this file type can potentially harm your computer. If you do not trust the source, do not open this software.

Microsoft Office will also use MOTW as a way of deciding if [Protected View](https://support.microsoft.com/en-us/topic/what-is-protected-view-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653) activates.

## Bypassing MOTW

It seems that signed files are the key to this conundrum. Files can be cryptographically signed in order to [confirm who created them](https://learn.microsoft.com/en-us/previous-versions/tn-archive/ee176795%28v%3Dtechnet.10%29?redirectedfrom=MSDN), and to confirm that they have not been changed since they were signed. (As Microsoft points out, this doesn’t assert that a file is *safe*, only that it has not been tampered with.)

So far, so good. How does this result in MOTW bypasses, though? Well, first of all it seems this has been an issue for several years. To be more specific, this probably became a bug around the release of Windows 10.

> Windows 8.0 RTM gets it right.
>
> — Will Dormann (@wdormann) [October 20, 2022](https://twitter.com/wdormann/status/1582925407107821568?ref_src=twsrc%5Etfw)

The problem is that a malformed signature results in the various possible warnings to notify of bad times ahead going AWOL. You will simply never see them:

> OK this is bad. You're on the right track that it's signature-related. But the problem is:
> If the file has this malformed Authenticode signature, the SmartScreen and/or file-open warning dialog will be skipped. Regardless of script contents
> As if there is no MotW on the file. [pic.twitter.com/pdDWDU98UU](https://t.co/pdDWDU98UU)
>
> — Will Dormann (@wdormann) [October 18, 2022](https://twitter.com/wdormann/status/1582458287915573249?ref_src=twsrc%5Etfw)

According to an interview with Will Dormann on Bleeping Computer, the problem appears to be related to SmartScreen, introduced in Windows 10.

> Why does Windows 8.1 not have the behavior where a corrupt signature skips the MotW prompting?
> Windows 10 and newer MotW prompting is sort of intermingled with SmartScreen by default.
> If you turn off "Check apps and files", you'll get behavior more like earlier Windows versions. [pic.twitter.com/T6k3xNKOFY](https://t.co/T6k3xNKOFY)
>
> — Will Dormann (@wdormann) [October 20, 2022](https://twitter.com/wdormann/status/1583179494189592576?ref_src=twsrc%5Etfw)

It's never a good thing when malware authors are able to turn security features on their head and use them against the people sitting in front of their device. Making yourself less safe by disabling a setting like SmartScreen just to ensure you see a warning that you should see anyway, and is also supposed to keep you safe, isn't a trade off that anyone should need to make. Fingers crossed that this one is resolved as soon as possible.

文章来源: https://www.malwarebytes.com/blog/news/2022/10/malware-authors-use-malformed-signature-trick-to-bypass-mark-of-the-web
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)