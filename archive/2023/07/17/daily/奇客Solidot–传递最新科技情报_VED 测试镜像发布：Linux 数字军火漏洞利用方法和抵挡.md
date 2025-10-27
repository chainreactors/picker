---
title: VED 测试镜像发布：Linux 数字军火漏洞利用方法和抵挡
url: https://www.solidot.org/story?sid=75528
source: 奇客Solidot–传递最新科技情报
date: 2023-07-17
fetch_date: 2025-10-04T11:53:13.651303
---

# VED 测试镜像发布：Linux 数字军火漏洞利用方法和抵挡

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251003)
  [往日投票](/polllist)
* 皮肤

  [蓝色](/?theme=blue)
  [橙色](/?theme=yellow)
  [绿色](/?theme=green)
  [浅绿色](/?theme=clightgreen)

* 分类:
* [首页](//www.solidot.org/)
* [Linux](//linux.solidot.org/)
* [科学](//science.solidot.org/)
* [科技](//technology.solidot.org/)
* [移动](//mobile.solidot.org/)
* [苹果](//apple.solidot.org/)
* [硬件](//hardware.solidot.org/)
* [软件](//software.solidot.org/)
* [安全](//security.solidot.org/)
* [游戏](//games.solidot.org/)
* [书籍](//books.solidot.org/)
* [idle](//idle.solidot.org/)
* [云计算](//cloud.solidot.org/)
* [高飞的电子替身](//story.solidot.org/)

## 关注我们：

solidot新版网站常见问题，请点击[这里](/QA)查看。

## 消息

**本文已被查看 5791 次**

## VED 测试镜像发布：Linux 数字军火漏洞利用方法和抵挡

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年07月16日 23时50分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75528&appkey=1370085986&title=VED%20%E6%B5%8B%E8%AF%95%E9%95%9C%E5%83%8F%E5%8F%91%E5%B8%83%EF%BC%9ALinux%20%E6%95%B0%E5%AD%97%E5%86%9B%E7%81%AB%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%E6%96%B9%E6%B3%95%E5%92%8C%E6%8A%B5%E6%8C%A1 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自3001太空漫游**

Shawn the R0ck 写道：数字军火涉及利用计算机技术和网络渗透技术来制造和销售用于攻击和侵入计算机、网络和软件等信息系统的工具、程序和服务。这些工具和服务也包括漏洞利用工具、远控软件、木马病毒、网络钓鱼和黑客攻击技术等，目标是窃取敏感信息、控制或破坏目标系统。数字军火的使用者可能包括政府军事和情报机构、犯罪团伙和黑客组织等。0-day漏洞利用是数字军火行业的重要部分，您可以参考Maor Shwartz的文章以获取更多关于0-day行业和数字军火行业的趋势的信息。像Drebin这样的团队，他们在全球各地的数字军火领域都有同行。HardenedVault在之前发布的VED技术白皮书后，收到了一些反馈。为了进一步沟通和解答，HardenedVault决定发布一份关于漏洞利用方法的测试镜像。HardenedVault使用CVE-2021-22555进行测试是因为其公开的PoC/exploit中同时涵盖了主流和非主流的攻击方法，具体来说，基于CVE-2021-22555编写了3种不同利用方法的漏洞利用，VED的防御目标并不是具体的某个漏洞，而是漏洞利用方法（攻击模式）。这个测试镜像中的针对CVE-2021-22555的三个漏洞利用使用以下漏洞利用方法实现提权和容器逃逸，比如绕过包含SMAP，SMEP，KASLR等防御机制和利用堆喷等漏洞利用方法，此测试镜像目的是通过理解三个漏洞利用所包含的攻击方法，进而对针对Linux系统的0-day/N-day作出更恰当的风险评估和威胁模型。
https://hardenedvault.net/zh-cn/blog/2023-07-16-vault-range-resilience-weaponized-exp-linux/

﻿

活了一百年却只能记住30M字节是荒谬的。你知道，这比一张压缩盘还要少。人类境况正在变得日趋退。--Marvin Minsky

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251003)
* [过去的投票](/polllist)
* [编辑介绍](/authors)
* [隐私政策](/privacy)
* [使用条款](/terms)
* [网站介绍](/introd)
* [RSS](/index.rss)

本站提到的所有注册商标属于他们各自的所有人所有，评论属于其发表者所有，其余内容版权属于 solidot.org(2009-) 所有 。

[![php](https://icon.solidot.org/images/btn/php.gif)](//php.net/ "PHP 服务器")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](//apache.org/ "Apache 服务器")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](//www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](//www.solidot.org "solidot.org")

京ICP证161336号    [京ICP备15039648号-15](http://beian.miit.gov.cn) 北京市公安局海淀分局备案号：11010802021500 [![](//icon.zhiding.cn/beian/icon.png)](//icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

举报电话：010-62641205　涉未成年人举报专线：010-62641208 举报邮箱：jubao@zhiding.cn　网上有害信息举报专区：<https://www.12377.cn>