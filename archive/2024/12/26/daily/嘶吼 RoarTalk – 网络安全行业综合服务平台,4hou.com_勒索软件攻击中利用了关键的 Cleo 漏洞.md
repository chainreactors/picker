---
title: 勒索软件攻击中利用了关键的 Cleo 漏洞
url: https://www.4hou.com/posts/33V9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-26
fetch_date: 2025-10-06T19:34:25.504247
---

# 勒索软件攻击中利用了关键的 Cleo 漏洞

勒索软件攻击中利用了关键的 Cleo 漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索软件攻击中利用了关键的 Cleo 漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-12-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)93434

收藏

导语：此漏洞编号为 CVE-2024-50623，影响 5.8.0.21 之前的所有版本，使未经身份验证的攻击者，能够在在线暴露的易受攻击的服务器上远程执行代码。

CISA 已确认，Cleo Harmony、VLTrader 和 LexiCom 文件传输软件中的一个关键安全漏洞正在被勒索软件攻击所利用。

此漏洞编号为 CVE-2024-50623，影响 5.8.0.21 之前的所有版本，使未经身份验证的攻击者，能够在在线暴露的易受攻击的服务器上远程执行代码。

Cleo 于 10 月份发布了安全更新来修复该问题，并警告所有客户“立即升级实例”以应对其他潜在的攻击媒介。目前尚未透露 CVE-2024-50623 是在野外的攻击目标。然而，CISA 将该安全漏洞添加到其已知被利用漏洞的目录中，并将其标记为用于勒索软件活动。

在添加到 KEV 目录后，美国联邦机构必须按照 2021 年 11 月发布的具有约束力的操作指令 (BOD 22-01) 的要求，在 1 月 3 日之前提出申请，确保其网络免受攻击。

虽然网络安全机构没有提供有关针对易受 CVE-2024-50623 漏洞，利用的 Cleo 服务器的勒索软件活动的任何其他信息，但这些攻击与之前利用 MOVEit Transfer、GoAnywhere MFT 中的零日漏洞的 Clop 数据盗窃攻击惊人地相似，以及近年来的Accellion FTA。

一些人还认为该漏洞被 Termite 勒索软件操作所利用。然而，这个链接只是因为 Blue Yonder 拥有暴露的 Cleo 软件服务器，并且在勒索软件团伙声称的网络攻击中遭到破坏。

**Cleo 零日漏洞也被积极利用**

正如 Huntress 安全研究人员首次发现的那样，经过全面修补的 Cleo 服务器仍然受到威胁，很可能使用 CVE-2024-50623 绕过（尚未收到 CVE ID），使攻击者能够导入和执行任意 PowerShell 或 bash 命令通过利用默认的自动运行文件夹设置。

Cleo 现已发布补丁来修复这个被积极利用的零日漏洞，并敦促客户尽快升级到版本 5.8.0.24，以保护暴露在互联网上的服务器免受破坏尝试。应用补丁后，系统会记录启动时发现的与此漏洞相关的任何文件的错误，并删除这些文件。

建议无法立即升级的管理员通过从系统选项中清除 Autorun 目录来禁用自动运行功能，以减少攻击面。正如 Rapid7 在调查零日攻击时发现的那样，威胁者利用零日攻击来删除 Java Archive (JAR) 有效负载 [VirusTotal]，该负载是更大的基于 Java 的后利用框架的一部分。

![Cleo_attack_flow.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241216/1734334182976794.png "1734319363148049.png")

Cleo 攻击流程

Huntress 也分析了该恶意软件并将其命名为 Malichus，目前只发现它部署在 Windows 设备上。

根据另一家调查正在进行攻击的网络安全公司 Binary Defense ARC Labs 的说法，恶意软件操作者可以使用 Malichus 进行文件传输、命令执行和网络通信。

到目前为止，Huntress 已发现多家公司的 Cleo 服务器遭到入侵，并表示可能还有其他潜在受害者。Sophos 的 MDR 和实验室团队还在 50 多个 Cleo 主机上发现了妥协迹象。截止到目前，Cleo 发言人确认 CVE-2024-50623 漏洞已被作为零日攻击利用。

文章翻译自：https://www.bleepingcomputer.com/news/security/cisa-confirms-critical-cleo-bug-exploitation-in-ransomware-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6sIrJ8cz)

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