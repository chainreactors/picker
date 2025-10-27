---
title: Interlock——针对 FreeBSD 服务器的新型勒索软件
url: https://www.4hou.com/posts/nlGD
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-28
fetch_date: 2025-10-06T19:13:32.675718
---

# Interlock——针对 FreeBSD 服务器的新型勒索软件

Interlock——针对 FreeBSD 服务器的新型勒索软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Interlock——针对 FreeBSD 服务器的新型勒索软件

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-11-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)92898

收藏

导语：每个受害者都有一个唯一的“公司 ID”，与电子邮件地址一起用于在威胁者的 Tor 协商站点上注册。

一种名为 Interlock 的相对较新的勒索软件正采用不寻常的方法创建加密器来针对 FreeBSD 服务器，以攻击世界各地的组织。

Interlock 于 2024 年 9 月底出现，此后声称对六个组织发起攻击，在未支付赎金后在其数据泄露网站上发布了被盗数据。美国密歇根州就是受害者之一，于 10 月初遭受了网络攻击。

关于勒索软件的操作，人们知之甚少，其中一些信息来自 10 月初的事件响应者 Simo，他在 Interlock 勒索软件事件中发现了一个新的后门 [VirusTotal]。

不久之后，网络安全研究人员 MalwareHuntTeam 发现了用于 Interlock 操作的 Linux ELF 加密器 [VirusTotal]。安全研究人员尝试在虚拟机上测试它，但它立即崩溃了。

检查可执行文件中的字符串表明它是专门为 FreeBSD 编译的，Linux“File”命令进一步确认它是在 FreeBSD 10.4 上编译的。然而，即使在 FreeBSD 虚拟机上测试示例，也无法让示例正确执行。

虽然针对 VMware ESXi 服务器和虚拟机创建的 Linux 加密器很常见，但为 FreeBSD 创建的加密器却很少见。已知的唯一创建 FreeBSD 加密器的勒索软件操作是现已解散的 Hive 勒索软件操作，该操作于 2023 年被 FBI 破坏。

本周，有安全研究人员分享说，他们发现了 FreeBSD 的额外样本ELF 加密器 [VirusTotal] 和操作的 Windows 加密器 [VirusTotal] 示例。

并表示威胁者可能创建了 FreeBSD 加密器，因为该操作系统通常用于关键基础设施，攻击可能会造成广泛的破坏。

Interlock 针对 FreeBSD，因为它广泛用于服务器和关键基础设施。攻击者可以破坏重要服务，索要巨额赎金，并强迫受害者付款。

**Interlock 勒索软件**

虽然无法让 FreeBSD 加密器正常工作，但 Windows 版本在虚拟机上运行没有问题。Windows 加密器将清除 Windows 事件日志，如果启用了自删除，将使用 DLL 通过 rundll32.exe 删除主要二进制文件。

加密文件时，勒索软件会将 .interlock 扩展名附加到所有加密文件名中，并在每个文件夹中创建勒索信息。

![encrypted-files.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241104/1730713492792906.png "1730713128157437.png")

Interlock 加密的文件

这份勒索字条名为 !\_\_README\_\_!.txt，简要描述了受害者文件发生的情况、发出的威胁以及 Tor 协商和数据泄露站点的链接。

![ransom-note.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241104/1730713494828936.png "1730713184907152.png")

联锁勒索信

每个受害者都有一个唯一的“公司 ID”，与电子邮件地址一起用于在威胁者的 Tor 协商站点上注册。与最近的许多其他勒索软件操作一样，面向受害者的谈判站点仅包含一个可用于与威胁者进行通信的聊天系统。

![interlock-negoration-site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241104/1730713495204777.png "1730713222178027.png")

Interlock 暗网谈判网站

在进行攻击时，Interlock 将破坏公司网络并从服务器窃取数据，同时横向传播到其他设备。完成后，威胁者会部署勒索软件来加密网络上的所有文件。

被盗数据被用作双重勒索攻击的一部分，威胁者威胁称，如果不支付赎金，就会公开泄露这些数据。

![data-leak-site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241104/1730713497107393.png "1730713275102295.png")

Interlock数据泄露现场

有媒体了解到，勒索软件操作要求的赎金从数十万美元到数百万美元不等，具体金额取决于其规模。

文章翻译自：https://www.bleepingcomputer.com/news/security/meet-interlock-the-new-ransomware-targeting-freebsd-servers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?4z2DmSIX)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)