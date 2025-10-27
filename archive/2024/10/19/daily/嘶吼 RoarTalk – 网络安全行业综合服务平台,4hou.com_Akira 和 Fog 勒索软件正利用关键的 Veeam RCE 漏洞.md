---
title: Akira 和 Fog 勒索软件正利用关键的 Veeam RCE 漏洞
url: https://www.4hou.com/posts/nlzD
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-19
fetch_date: 2025-10-06T18:46:44.164253
---

# Akira 和 Fog 勒索软件正利用关键的 Veeam RCE 漏洞

Akira 和 Fog 勒索软件正利用关键的 Veeam RCE 漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Akira 和 Fog 勒索软件正利用关键的 Veeam RCE 漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-10-18 09:50:15

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)77558

收藏

导语：Veeam 表示，其产品被全球超过 550,000 家客户使用，其中包括全球 2,000 强公司中至少 74% 的客户。

据安全研究人员发现，勒索软件团伙现在正利用一个严重的安全漏洞，让攻击者能够在易受攻击的 Veeam Backup & Replication (VBR) 服务器上获得远程代码执行 (RCE)。

Code White 安全研究员 Florian Hauser 发现，该安全缺陷（现已追踪为 CVE-2024-40711）是由不可信数据漏洞的反序列化引起的，未经身份验证的威胁者可以在低复杂性攻击中利用该漏洞。

Veeam 于 9 月披露了该漏洞并发布了安全更新，而 watchTowr Labs 也发布了技术分析。不过，watchTowr Labs 将概念验证漏洞利用代码推迟发布，以便管理员有足够的时间来保护其服务器。

此次延迟是由于企业使用 Veeam 的 VBR 软件作为数据保护和灾难恢复解决方案来备份、恢复和复制虚拟、物理和云机器。

这使得它成为寻求快速访问公司备份数据的恶意分子非常受欢迎的目标。

正如 Sophos X-Ops 事件响应人员发现的那样，CVE-2024-40711 RCE 缺陷很快就被发现，并在 Akira 和 Fog 勒索软件攻击中与之前泄露的凭据一起被利用，以向本地管理员添加“点”本地帐户和远程桌面用户组。

Sophos X-Ops 表示：“在一个案例中，攻击者投放了 Fog 勒索软件。同一时间范围内的另一次攻击试图部署 Akira 勒索软件。所有 4 个案例中的指标都与之前的 Akira 和 Fog 勒索软件攻击重叠。”

在每种情况下，攻击者最初都使用受损的 VPN 网关访问目标，而没有启用多因素身份验证。其中一些 VPN 运行不受支持的软件版本。

在 Fog 勒索软件事件中，攻击者将其部署到未受保护的 Hyper-V 服务器上，然后使用实用程序 rclone 来窃取数据。

**这不是勒索软件攻击中的第一个 Veeam 漏洞**

去年，即 2023 年 3 月 7 日，Veeam 还修补了备份和复制软件 (CVE-2023-27532) 中的一个高严重性漏洞，该漏洞可被利用来破坏备份基础设施主机。

几周后，芬兰网络安全和隐私公司 WithSecure 发现 CVE-2023-27532 漏洞部署在与出于经济动机的 FIN7 威胁组织相关的攻击中，该组织因与 Conti、REvil、Maze、Egregor 和 BlackBasta 勒索软件操作的联系而闻名。

几个月后，同样的 Veeam VBR 漏洞被用于针对美国关键基础设施和拉丁美洲 IT 公司的古巴勒索软件攻击。

Veeam 表示，其产品被全球超过 550,000 家客户使用，其中包括全球 2,000 强公司中至少 74% 的客户。

文章翻译自：https://www.bleepingcomputer.com/news/security/akira-and-fog-ransomware-now-exploiting-critical-veeam-rce-flaw/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?1sFaOiKQ)

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