---
title: Exchange Server security updates updated
url: https://buaq.net/go-174813.html
source: unSafe.sh - 不安全
date: 2023-08-19
fetch_date: 2025-10-04T11:59:23.276785
---

# Exchange Server security updates updated

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

Exchange Server security updates updated

Microsoft has re-released the August 2023 Security Updates (SUs) for Ex
*2023-8-18 19:45:0
Author: [www.malwarebytes.com(查看原文)](/jump-174813.htm)
阅读量:20
收藏*

---

Microsoft has re-released the [August 2023 Security Updates (SUs) for Exchange Server](https://techcommunity.microsoft.com/t5/exchange-team-blog/released-august-2023-exchange-server-security-updates/ba-p/3892811). The original release of the SUs, from August 8 2023, had a localization issue with Exchange Server running on a non-English Operating Systems (OSes) that caused Setup to stop unexpectedly, leaving Exchange services in a disabled state.

Exchange Online users are already protected from the vulnerabilities addressed by these Security Updates and do not need to take any action other than updating any Exchange servers or Exchange Management tools workstations in their environment.

This patch comes with a [complicated table](https://techcommunity.microsoft.com/t5/exchange-team-blog/re-release-of-august-2023-exchange-server-security-update/ba-p/3900025) of recommended actions, in which version 1 is the original August 2023 SU and version 2 is the re-released August 2023 SU. Microsoft says:

* If you successfully installed version 1 without problems, no further action is needed.
* If you installed version 1 automatically without any problems or issues, version 2 will be downloaded automatically.
* If the installation of version 1 failed, leaving Exchange services disabled, and you restarted the Exchange services without installing version 1 again, you should install version 2.
* If the installation of version 1 failed, leaving Exchange services disabled, you restarted the Exchange services, and you used the workaround to manually create a “Network Service” account and then installed version 1, you should:
  + Uninstall version 1 and reboot.
  + Remove the manually created “Network Service” account (if it still exists).
  + Install version 2.

If version 1 was never installed, you can skip straight to version 2. Although there is no reason to suspect there are active exploits in the wild, we still recommend to do this as soon as possible to protect your environment. Exchange Servers are attractive targets for cybercriminals.

The vulnerability fixed by the security update, listed as [CVE-2023-21709](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21709), required users to run a script in addition to installing the update. If you took the extra steps needed to address CVE-2023-21709 none of the actions above will undo them, so you do not have to repeat or undo them at any point. But again, if you haven’t done it yet, you should do so as soon as possible.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/08/exchange-server-security-updates-re-released
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)