---
title: VED 测试镜像发布：Linux 数字军火漏洞利用方法和抵挡
url: https://buaq.net/go-172171.html
source: unSafe.sh - 不安全
date: 2023-07-17
fetch_date: 2025-10-04T11:50:56.818929
---

# VED 测试镜像发布：Linux 数字军火漏洞利用方法和抵挡

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

VED 测试镜像发布：Linux 数字军火漏洞利用方法和抵挡

Shawn the R0ck 写道：数字军火涉及利用计算机技术和网络渗透技术来制造和销售用于攻击和侵入计算机、网络和软件等信息系统的工具、程序和服务。这些工具和服务也包括漏洞利用工具、远控
*2023-7-16 23:50:33
Author: [www.solidot.org(查看原文)](/jump-172171.htm)
阅读量:16
收藏*

---

Shawn the R0ck 写道：数字军火涉及利用计算机技术和网络渗透技术来制造和销售用于攻击和侵入计算机、网络和软件等信息系统的工具、程序和服务。这些工具和服务也包括漏洞利用工具、远控软件、木马病毒、网络钓鱼和黑客攻击技术等，目标是窃取敏感信息、控制或破坏目标系统。数字军火的使用者可能包括政府军事和情报机构、犯罪团伙和黑客组织等。0-day漏洞利用是数字军火行业的重要部分，您可以参考Maor Shwartz的文章以获取更多关于0-day行业和数字军火行业的趋势的信息。像Drebin这样的团队，他们在全球各地的数字军火领域都有同行。HardenedVault在之前发布的VED技术白皮书后，收到了一些反馈。为了进一步沟通和解答，HardenedVault决定发布一份关于漏洞利用方法的测试镜像。HardenedVault使用CVE-2021-22555进行测试是因为其公开的PoC/exploit中同时涵盖了主流和非主流的攻击方法，具体来说，基于CVE-2021-22555编写了3种不同利用方法的漏洞利用，VED的防御目标并不是具体的某个漏洞，而是漏洞利用方法（攻击模式）。这个测试镜像中的针对CVE-2021-22555的三个漏洞利用使用以下漏洞利用方法实现提权和容器逃逸，比如绕过包含SMAP，SMEP，KASLR等防御机制和利用堆喷等漏洞利用方法，此测试镜像目的是通过理解三个漏洞利用所包含的攻击方法，进而对针对Linux系统的0-day/N-day作出更恰当的风险评估和威胁模型。

https://hardenedvault.net/zh-cn/blog/2023-07-16-vault-range-resilience-weaponized-exp-linux/

文章来源: https://www.solidot.org/story?sid=75528
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)