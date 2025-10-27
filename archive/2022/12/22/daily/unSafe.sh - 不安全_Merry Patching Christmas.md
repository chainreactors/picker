---
title: Merry Patching Christmas
url: https://buaq.net/go-140900.html
source: unSafe.sh - 不安全
date: 2022-12-22
fetch_date: 2025-10-04T02:11:36.290949
---

# Merry Patching Christmas

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

Merry Patching Christmas

Here’s an important update to make before you log off for the holidays.For those of you that are on
*2022-12-21 17:7:40
Author: [blog.avast.com(查看原文)](/jump-140900.htm)
阅读量:20
收藏*

---

Here’s an important update to make before you log off for the holidays.

For those of you that are on your way to take a break next week, we’ve got a bit of advice to avoid encountering some unnecessary scares during this time that you’ll be spending with your loved ones.

Put simply: If you’re running any version of Windows, please update it as soon as possible! There’s a [new Windows remote code execution vulnerability](https://arstechnica.com/information-technology/2022/12/critical-windows-code-execution-vulnerability-went-undetected-until-now/) affecting all Windows machines. Even though it’s not *yet* being exploited in the wild, it’s better to be safe than sorry.

## **Looking back at WannaCry**

Some of you probably remember the worst ransomware outbreak in history, [WannaCry](https://blog.avast.com/wannacry-update-the-worst-ransomware-outbreak-in-history?_ga=2.9361587.721450066.1671613521-83091737.1671613521). In that case, the attack was also taking advantage of a remote code execution vulnerability. WannaCry affected the SMB protocol, while this new one (CVE-2022-37958) works in a broader range of network protocols, including SMTP and HTTP when SPNEGO web authentication is enabled.

Microsoft has [a list](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37958) with the different security updates covering from Windows 7 up to Windows 11. The update first appeared in September’s Patch Tuesday security updates and was deemed as “important”; however, after new information was discovered showing the attack potential of the vulnerability, it has been updated to “critical” by Microsoft with a severity rating of 8.1 (note that this is the same as EternalBlue, the exploit used by WannaCry).

While consumers usually have security updates on and applied by default, this isn’t the case for SMBs and bigger enterprises. This is due to the fact that a number of steps have to be taken in advance, such as ensuring compatibility with used applications.

For SMBs and enterprises, the priority of [patching this vulnerability](https://blog.avast.com/patching-systems-business?_ga=2.9361587.721450066.1671613521-83091737.1671613521) must be increased, as all unpatched computers will be at risk if (when!) a new [worm](https://www.avast.com/c-computer-worm?_ga=2.9361587.721450066.1671613521-83091737.1671613521) using this vulnerability is released.

文章来源: https://blog.avast.com/merry-patching-christmas
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)