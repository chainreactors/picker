---
title: 2月修复的 Windows 内核错误被用作零日漏洞
url: https://www.4hou.com/posts/PKB6
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-03-09
fetch_date: 2025-10-04T12:09:06.467024
---

# 2月修复的 Windows 内核错误被用作零日漏洞

2月修复的 Windows 内核错误被用作零日漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 2月修复的 Windows 内核错误被用作零日漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-03-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)246449

收藏

导语：建议Windows用户尽快安装2024年2月补丁星期二更新，以阻止Lazarus的CVE-2024-21338攻击。

微软在 2 月份修补了一个高严重性的 Windows 内核特权升级漏洞，并被告知该漏洞正被作为零日漏洞利用。

该安全漏洞的编号为CVE-2024-21338，由 Avast 高级恶意软件研究员在 appid.sys Windows AppLocker 驱动程序中发现。

该漏洞影响运行多个版本的 Windows 10 和 Windows 11（包括最新版本）以及 Windows Server 2019 和 2022 的系统。

微软解释说，成功利用该漏洞使本地攻击者能够在不需要用户交互的低复杂性攻击中获得系统权限。“要利用此漏洞，攻击者首先必须登录系统。然后攻击者可以运行特制的应用程序，该应用程序可以利用此漏洞并控制受影响的系统，”

该公司已于 2 月 13 日修补了该漏洞，并于 2 月 28 日更新了通报，以确认 CVE-2024-21338 已在野外被利用，但没有透露有关攻击的任何细节。

**该零日漏洞被利用**

有黑客至少从 2023 年 8 月起就一直在利用该漏洞作为零日攻击，以获得内核级访问权限并关闭安全工具，从而使他们能够避免使用更容易的检测 BYOVD（自带易受攻击的驱动程序）技术。“从攻击者的角度来看，从管理到内核的跨越开启了一个全新的可能性领域。通过内核级访问，攻击者可能会破坏安全软件、隐藏感染迹象（包括文件、网络活动、进程等）、禁用内核模式遥测、关闭缓解措施等等。”

此外，由于 PPL（受保护进程轻量级）的安全性依赖于管理到内核边界，攻击者获得了篡改受保护进程或为任意进程添加保护的能力。如果 lsass受到 RunAsPPL 的保护，绕过 PPL 可能使攻击者能够转储其他无法访问的凭据。

Lazarus 利用该缺陷建立了内核读/写原语，使更新的 FudModule rootkit 版本能够执行直接内核对象操作。

这个新的 FudModule 版本具有显著的隐蔽性和功能改进，包括用于逃避检测和关闭 AhnLab V3 Endpoint Security、Windows Defender、CrowdStrike Falcon 和 HitmanPro 安全保护以及更新的 Rootkit 技术。

在分析攻击时，还发现了 Lazarus 使用的一种以前未知的远程访问木马 (RAT) 恶意软件，该恶意软件将成为4 月份BlackHat Asia演示的焦点。

“由于管理到内核的零日漏洞现已被烧毁，Lazarus 面临着重大挑战。他们要么发现新的零日漏洞，要么恢复到旧的 BYOVD 技术，”相关人员说道。

建议Windows用户尽快安装2024年2月补丁星期二更新，以阻止Lazarus的CVE-2024-21338攻击。

文章翻译自：https://www.bleepingcomputer.com/news/security/windows-kernel-bug-fixed-last-month-exploited-as-zero-day-since-august/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0kNcgd8N)

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