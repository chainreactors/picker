---
title: RomCom 黑客利用 Firefox 和 Windows 零日漏洞
url: https://www.4hou.com/posts/9jG8
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-29
fetch_date: 2025-10-06T19:14:18.774019
---

# RomCom 黑客利用 Firefox 和 Windows 零日漏洞

RomCom 黑客利用 Firefox 和 Windows 零日漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# RomCom 黑客利用 Firefox 和 Windows 零日漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-11-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)92466

收藏

导语：RomCom 现在还针对乌克兰、欧洲和北美的组织进行跨行业的间谍攻击，包括政府、国防、能源、制药和保险。

总部位于俄罗斯的 RomCom 网络犯罪组织在最近针对欧洲和北美 Firefox 和 Tor 浏览器用户的攻击中发现了两个零日漏洞。

第一个漏洞 (CVE-2024-9680) 是 Firefox 动画时间线功能中的释放后使用错误，该功能允许在 Web 浏览器的沙箱中执行代码。 Mozilla 于 2024 年 10 月 9 日（ESET 报告该漏洞一天后）修补了该漏洞。

利用的第二个零日漏洞是 Windows 任务计划程序服务中的权限升级漏洞 (CVE-2024-49039)，该漏洞允许攻击者在 Firefox 沙箱之外执行代码。 Microsoft 在本月初（即 11 月 12 日）修复了此安全漏洞。

RomCom 将这两个漏洞作为零日链漏洞利用，帮助他们无需用户交互即可获得远程代码执行。他们的目标只需访问一个由攻击者控制的恶意制作的网站，该网站会在其系统上下载并执行 RomCom 后门。

根据攻击中使用的 JavaScript 漏洞之一的名称 (main-tor.js)，威胁者还针对 Tor 浏览器用户（根据 ESET 的分析，版本 12 和 13）。

![romcom-attack-flow.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241127/1732690835694622.png "1732690783198751.png")

RomCom 攻击流程

ESET 研究员表示：“妥协链由一个虚假网站组成，该网站将潜在受害者重定向到托管漏洞的服务器，如果漏洞成功，就会执行 shellcode，下载并执行 RomCom 后门。”

虽然不知道假网站的链接是如何分发的，但是，如果使用易受攻击的浏览器访问该页面，则有效负载会被丢弃并在受害者的计算机上执行，无需用户交互。

一旦部署在受害者的设备上，该恶意软件使攻击者能够运行命令并部署额外的有效负载。将两个零日漏洞链接在一起，就会为 RomCom 提供了无需用户交互的漏洞。这种复杂程度也表明了威胁者获取或开发隐秘能力的决心和手段。

此外，这些攻击中成功利用攻击的次数最终导致 RomCom 后门部署在受害者的设备上，这使得人们有理由相信这是一次广泛的活动。根据 ESET 遥测数据，潜在目标的数量从每个国家一名受害者到多达 250 名受害者不等。

这并不是 RomCom 第一次利用零日漏洞进行攻击。 2023 年 7 月，其运营商利用多个 Windows 和 Office 产品中的零日漏洞 (CVE-2023-36884) 攻击参加立陶宛维尔纽斯北约峰会的组织。

RomCom（也被追踪为 Storm-0978、Tropical Scorpius 或 UNC2596）与出于经济动机的活动、精心策划的勒索软件和勒索攻击以及凭证盗窃（可能旨在支持情报行动）有关。该威胁组织还与 Industrial Spy 勒索软件行动有关，该组织后来转向地下勒索软件。

据 ESET 称，RomCom 现在还针对乌克兰、欧洲和北美的组织进行跨行业的间谍攻击，包括政府、国防、能源、制药和保险。

文章翻译自：https://www.bleepingcomputer.com/news/security/firefox-and-windows-zero-days-exploited-by-russian-romcom-hackers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2u7nKWmR)

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