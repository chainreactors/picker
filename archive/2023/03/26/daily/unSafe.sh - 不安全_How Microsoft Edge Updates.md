---
title: How Microsoft Edge Updates
url: https://buaq.net/go-155242.html
source: unSafe.sh - 不安全
date: 2023-03-26
fetch_date: 2025-10-04T10:42:20.388799
---

# How Microsoft Edge Updates

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

![](https://8aqnet.cdn.bcebos.com/0112080116985b6a26ffa0ebfd233753.jpg)

How Microsoft Edge Updates

When you see the update notifier in Edge (a green or red arrow on the … button)
*2023-3-25 20:41:49
Author: [textslashplain.com(查看原文)](/jump-155242.htm)
阅读量:23
收藏*

---

When you see the update notifier in Edge (a green or red arrow on the … button):

[![](https://textplain.files.wordpress.com/2023/03/image-49.png?w=632)](https://textplain.files.wordpress.com/2023/03/image-49.png)

… this means an update is ready for use and you simply need to restart the browser to have it applied.

While you’re in this state, if you open Edge’s application folder, you’ll see the new version sitting side-by-side with the currently-running version:

[![](https://textplain.files.wordpress.com/2023/03/image-50.png?w=986)](https://textplain.files.wordpress.com/2023/03/image-50.png)

When you choose to restart:

[![](https://textplain.files.wordpress.com/2023/03/image-51.png?w=895)](https://textplain.files.wordpress.com/2023/03/image-51.png)

…either via the prompt or manually, Edge will restart the new binaries and remove the old ones:

[![](https://textplain.files.wordpress.com/2023/03/image-52.png?w=854)](https://textplain.files.wordpress.com/2023/03/image-52.png)

The new instance restarts using Chromium’s [session restoration](https://textslashplain.com/2019/06/24/surprise-undead-session-cookies/) feature, so all of your tabs, windows, cookies, etc, are right where you left them before the update (akin to typing `edge://restart` in the omnibox).

This design means that the new version is ready to go immediately, without the need to wait for any downloads or other steps that could take a while or go wrong along the way. This is important, because users who don’t restart the browser will continue running the outdated version (even for new tabs or windows) until they restart, and this could expose them to security vulnerabilities.

A pair of [Group](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#relaunchnotification) [Policies](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#relaunchnotificationperiod) give administrators control of the relaunch process.

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-2022, working on Office, IE, and Edge. Now a SWE on Microsoft Defender Web Protection. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

文章来源: https://textslashplain.com/2023/03/25/how-microsoft-edge-updates/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)