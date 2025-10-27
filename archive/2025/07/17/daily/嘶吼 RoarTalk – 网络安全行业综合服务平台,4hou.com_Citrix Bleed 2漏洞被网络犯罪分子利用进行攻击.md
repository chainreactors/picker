---
title: Citrix Bleed 2漏洞被网络犯罪分子利用进行攻击
url: https://www.4hou.com/posts/l0yr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-17
fetch_date: 2025-10-06T23:27:28.067626
---

# Citrix Bleed 2漏洞被网络犯罪分子利用进行攻击

Citrix Bleed 2漏洞被网络犯罪分子利用进行攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Citrix Bleed 2漏洞被网络犯罪分子利用进行攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-07-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)55647

收藏

导语：研究人员的担忧似乎是有根据的，因为ReliaQuest表示，CVE-2025-5777已经被用于有针对性的攻击。

据网络安全公司ReliaQuest称，NetScaler ADC和网关的一个关键漏洞“Citrix Bleed 2”（CVE-2025-5777）现在很可能被利用在攻击中，Citrix设备上的可疑会话有所增加。

Citrix Bleed 2，由网络安全研究员Kevin Beaumont命名，因为它与最初的Citrix Bleed （CVE-2023-4966）相似，是一个内存读取漏洞，允许未经身份验证的攻击者访问通常不可访问的内存部分。

这可能允许攻击者从面向公众的网关和虚拟服务器窃取会话令牌、凭据和其他敏感数据，使他们能够劫持用户会话并绕过多因素身份验证（MFA）。

Citrix的顾问也确认了这一风险，提醒用户安装安全更新以阻止访问任何被劫持的会话后，结束所有ICA和PCoIP会话。

该漏洞被追踪为CVE-2025-5777，Citrix于2025年6月17日解决了该漏洞，没有任何活跃利用的报告。然而，Beaumont警告说上周存在被利用的可能性较高。

研究人员的担忧似乎是有根据的，因为ReliaQuest表示，CVE-2025-5777已经被用于有针对性的攻击。

虽然没有公开利用CVE-2025-5777（被称为“Citrix Bleed 2”）的报道，但ReliaQuest认为，攻击者正在积极利用这一漏洞，获得对目标环境的初始访问权限。

这一结论是基于对最近实际攻击的以下观察得出的：

**·**被劫持的Citrix web会话在没有用户交互的情况下被授予身份验证，这表明攻击者使用被盗的会话令牌绕过了MFA。

**·**攻击者在合法和可疑的IP地址上重复使用相同的Citrix会话，这表明会话劫持和从未经授权的来源重播。

**·**LDAP查询是在访问后发起的，这表明攻击者执行了Active Directory侦察来映射用户、组和权限。

**·**adeexplorer64 .exe的多个实例跨系统运行，表明协调的域侦察和对各种域控制器的连接尝试。

**·**Citrix会话起源于与消费者VPN提供商（如DataCamp）相关的数据中心ip，这表明攻击者通过匿名基础设施进行混淆。

上述情况与未经授权访问Citrix后的开发活动一致，强化了CVE-2025-5777正在被利用的评估。

为了防止这种活动，可能受到影响的用户应该升级到14.1-43.56+、13.1-58.32+或13.1-FIPS/NDcPP 13.1-37.235+版本来修复漏洞。

在安装最新固件后，管理员应该终止所有活动的ICA和PCoIP会话，因为它们可能已经被劫持了。

在终止活动会话之前，管理员应该首先使用show icconnection命令和NetScaler Gateway > PCoIP > Connections检查它们是否存在可疑活动。在检查活动会话后，管理员可以使用以下命令终止它们：终止所有连接、终止pcoipconnection -all。如果无法立即安装安全更新，建议通过网络acl或防火墙规则限制外部对NetScaler的访问。

在被问到关于CVE-2025-5777是否被积极利用的问题时，Citrix表示没有发现任何利用的迹象。然而，另一个Citrix漏洞，跟踪为CVE-2025-6543，正在攻击中被利用，导致NetScaler设备上的拒绝服务条件。Citrix表示，这个漏洞和CVE-2025-5777漏洞在同一个模块中，但是不同的漏洞。

文章翻译自：https://www.bleepingcomputer.com/news/security/citrix-bleed-2-flaw-now-believed-to-be-exploited-in-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?QtPMH6CI)

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