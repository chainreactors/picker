---
title: 黑客自 8 月以来频繁利用公开漏洞攻击 WhatsUp Gold
url: https://www.4hou.com/posts/GAMy
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-16
fetch_date: 2025-10-06T18:22:01.603194
---

# 黑客自 8 月以来频繁利用公开漏洞攻击 WhatsUp Gold

黑客自 8 月以来频繁利用公开漏洞攻击 WhatsUp Gold - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客自 8 月以来频繁利用公开漏洞攻击 WhatsUp Gold

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-09-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)107956

收藏

导语：尽管相关工作人员在两周前就解决了安全问题，但许多客户仍然需要更新软件。

黑客一直在利用 Progress Software 的 WhatsUp Gold 网络可用性和性能监控解决方案中两个严重漏洞的公开漏洞代码。自 8 月 30 日以来，攻击中利用的两个漏洞是 SQL 注入漏洞，跟踪编号为 CVE-2024-6670 和 CVE-2024-6671，漏洞允许在未经身份验证的情况下检索加密密码。

尽管相关工作人员在两周前就解决了安全问题，但许多客户仍然需要更新软件，而威胁者正在利用这一漏洞发起攻击。

Progress Software 于 8 月 16 日发布了针对该问题的安全更新，并于 9 月 10 日在安全公告中添加了如何检测潜在危害的说明。

安全研究员 Sina Kheirkhah 发现了这些漏洞，并于 5 月 22 日将其报告给零日计划。8 月 30 日，该研究员发布了概念验证 (PoC) 漏洞。

该研究员在技术文章中解释了如何利用用户输入中不适当的清理问题将任意密码插入管理员帐户的密码字段，从而使其容易被接管。

![attack.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726216426171670.png "1726216273524130.png")

Kheirkhah 的漏洞概述

**野外开发**

网络安全公司最新的报告指出，黑客已经开始利用这些漏洞，根据观察，这些攻击似乎基于 Kheirkhah 的 PoC，用于绕过身份验证并进入远程代码执行和有效载荷部署阶段。在研究人员发布 PoC 漏洞代码五小时后，安全公司的遥测技术首次发现了主动攻击的迹象。

攻击者利用 WhatsUp Gold 的合法 Active Monitor PowerShell Script 功能，通过从远程 URL 检索的 NmPoller.exe 运行多个 PowerShell 脚本。

![powershell.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726216428135690.png "1726216358194593.png")

攻击者部署的恶意 PowerShell 脚本

接下来，攻击者使用合法的 Windows 实用程序“msiexec.exe”通过 MSI 包安装各种远程访问工具 (RAT)，包括 Atera Agent、Radmin、SimpleHelp Remote Access 和 Splashtop Remote。

植入这些 RAT 可让攻击者在受感染的系统上建立持久性。

在某些情况下，研究人员观察到部署了多个有效载荷。分析师无法将这些攻击归因于特定的威胁组织，但使用多个 RAT 表明它可能是勒索软件参与者。

![overview.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726216429912438.png "1726216392177385.png")

观察到的活动的攻击流程

据了解，这并不是 WhatsUp Gold 今年第一次受到公开漏洞的攻击。8 月初，威胁监测组织 Shadowserver Foundation 报告称，其蜜罐捕获了利用 CVE-2024-4885 的攻击，CVE-2024-4885 是一个于 2024 年 6 月 25 日披露的严重远程代码执行漏洞。这个缺陷也被 Kheirkhah 发现，两周后他在社交媒体上公布了完整的详细信息。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-targeting-whatsup-gold-with-public-exploit-since-august/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?yubl2bzT)

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