---
title: 守护者的零之曙光：Hardened SIEM/XDR
url: https://www.solidot.org/story?sid=75901
source: 奇客Solidot–传递最新科技情报
date: 2023-08-27
fetch_date: 2025-10-04T11:59:35.890415
---

# 守护者的零之曙光：Hardened SIEM/XDR

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

**本文已被查看 5954 次**

## 守护者的零之曙光：Hardened SIEM/XDR

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年08月26日 11时45分 星期六 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75901&appkey=1370085986&title=%E5%AE%88%E6%8A%A4%E8%80%85%E7%9A%84%E9%9B%B6%E4%B9%8B%E6%9B%99%E5%85%89%EF%BC%9AHardened%20SIEM%2FXDR "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自超能第七感·碰撞**

Shawn the R0ck 写道：现代网络安全运营中心主要依赖于两个关键要素：基于agent的安全解决方案，在台式机、笔记本和服务器操作系统上运行；以及威胁分析系统，通常称为安全信息与事件管理（SIEM）系统或扩展检测与响应（XDR）系统充当安全大脑的角色。然而，网络安全行业面临两个主要挑战。首先，大多数安全解决方案未能在操作系统（OS）及OS以下层面提供全面的威胁检测，导致这一关键领域容易受到攻击。安全大脑本身或者周边的安全产品被攻陷并不是一件有趣的事情，安全领域最尴尬之处莫过于次。其次，威胁分析系统通常缺乏与最佳安全实践相一致的强大保护措施，这可能无意中导致安全漏洞。针对这些挑战，HardenedVault开发了一种基于开源SIEM/XDR工具Wazuh的解决方案，以展示HardenedVault可以如何解决这些问题。该工具与VED无缝集成，扩展了对Linux内核运行时的监控维度，实时监控漏洞提权、容器逃逸和rootkit，同时提供了其他安全措施，如CIS合规性，为已识别的威胁提供了强大的解决方案。VED能够将SIEM/XDR的监控维度扩展到Linux内核运行时，以应对特权升级、容器逃逸和Rootkits等安全威胁，这是一个强大的增强功能。通过整合这一功能，VED可以为内核中潜在的安全威胁提供全面的可见性和检测能力。这确保了主动防御，并增强了系统的整体安全状态，从而保护系统免受复杂的攻击和未经授权的访问尝试。目前，HardenedVault在AWS上提供了Hardened SIEM/XDR，方便集成和部署。对于那些有兴趣在自建机房环境中实施类似解决方案的用户，HardenedVault将乐意提供帮助。
https://hardenedvault.net/blog/2023-08-25-hardened-siem-xdr-ved/

https://github.com/hardenedvault/vault-docs/blob/f75770e34dd3d4c619992731c83d652355aeda51/whitepaper/hardenedvault-whitepaper-en.pdf

﻿

与魔鬼战斗的人，应当小心自己不要成为魔鬼。当你远远凝视深渊时，深渊也在凝视你。——尼采

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