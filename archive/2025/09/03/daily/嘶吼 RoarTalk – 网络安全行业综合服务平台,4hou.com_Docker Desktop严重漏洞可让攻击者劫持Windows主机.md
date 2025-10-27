---
title: Docker Desktop严重漏洞可让攻击者劫持Windows主机
url: https://www.4hou.com/posts/omzK
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-03
fetch_date: 2025-10-02T19:32:25.176012
---

# Docker Desktop严重漏洞可让攻击者劫持Windows主机

Docker Desktop严重漏洞可让攻击者劫持Windows主机 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Docker Desktop严重漏洞可让攻击者劫持Windows主机

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-09-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)47829

收藏

导语：该安全问题属于服务器端请求伪造（SSRF）漏洞，目前已被编号为CVE-2025-9074，其严重等级被评定为9.3分。

Docker Desktop针对Windows和macOS系统的版本存在一个严重漏洞，即便“增强容器隔离（ECI）”保护功能处于开启状态，攻击者仍可通过运行恶意容器入侵主机。

该安全问题属于服务器端请求伪造（SSRF）漏洞，目前已被编号为CVE-2025-9074，其严重等级被评定为9.3分（极高）。

在Docker Desktop上运行的恶意容器，无需挂载Docker套接字，就能访问Docker引擎并启动更多容器。这可能导致主机系统上的用户文件被未授权访问，且增强容器隔离（ECI）无法缓解该漏洞带来的风险。

安全研究员兼漏洞赏金猎人Felix Boulet发现，任何运行中的容器都能未经认证访问“http://192.168.65.7:2375/”地址下的Docker Engine API。他通过演示证明，只需两个wget HTTP POST请求，就能创建并启动一个新容器，将Windows主机的C盘挂载到该容器的文件系统中。

Boulet的概念验证（PoC）漏洞利用代码无需在容器内获取代码执行权限。Pvotal Technologies公司的DevSecOps工程师、NorthSec网络安全会议的挑战设计员Philippe Dugre证实，该漏洞影响Docker Desktop的Windows和macOS版本，但不涉及Linux版本。

由于操作系统本身的安全防护机制，该漏洞在macOS系统上的危险性相对较低。他能在Windows系统的用户主目录中创建文件，但在macOS系统上，若未获得用户许可，则无法完成同样的操作。

在Windows系统中，Docker Engine通过WSL2运行，攻击者可作为管理员挂载整个文件系统，读取任何敏感文件，最终甚至能通过覆盖系统DLL文件，将权限提升至主机系统管理员级别。

然而在macOS系统中，Docker Desktop应用仍存在一层隔离机制，尝试挂载用户目录时会向用户请求许可。默认情况下，Docker应用无法访问文件系统的其他部分，也不会以管理员权限运行，因此相比Windows系统，macOS主机要安全得多。

不过，Philippe Dugre也提醒，即便在macOS系统上，仍存在恶意活动的操作空间——攻击者可完全控制应用程序和容器，这意味着他们可能在无需许可的情况下植入后门或修改配置。他还指出，该漏洞极易被利用，其漏洞利用代码仅由三行Python代码构成，这一点也印证了这一说法。

目前，该漏洞已被报告给Docker公司，Docker上周发布的Docker Desktop 4.44.3版本中修复了该问题。

文章翻译自：https://www.bleepingcomputer.com/news/security/critical-docker-desktop-flaw-lets-attackers-hijack-windows-hosts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?j9leh1zV)

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