---
title: Fluent Bit 严重缺陷影响众多主要云提供商
url: https://www.4hou.com/posts/xzQ3
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-06-12
fetch_date: 2025-10-06T16:54:32.591822
---

# Fluent Bit 严重缺陷影响众多主要云提供商

Fluent Bit 严重缺陷影响众多主要云提供商 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Fluent Bit 严重缺陷影响众多主要云提供商

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-06-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)172603

收藏

导语：在拒绝服务和远程代码执行攻击中利用的关键 Fluent Bit 漏洞影响了许多主要云提供商和许多技术巨头。

Fluent Bit 是一种非常流行的日志记录和指标解决方案，适用于 Windows、Linux 和 macOS，嵌入在主要 Kubernetes 发行版中，包括来自 Amazon AWS、Google GCP 和 Microsoft Azure 的发行版。

截至 2024 年 3 月，Fluent Bit 的下载和部署次数超过 130 亿次，比 2022 年 10 月报道的 30 亿次下载量大幅增加。

Fluent Bit 也被 Crowdstrike 和 Trend Micro 等网络安全公司以及思科、VMware、英特尔、Adobe 和戴尔等许多科技公司使用。

可在拒绝服务和远程代码执行攻击中利用的关键 Fluent Bit 漏洞影响了许多主要云提供商和许多技术巨头。这个严重的内存损坏漏洞被跟踪为 CVE-2024-4323，并被发现该漏洞的安全研究人员称为 Linguistic Lumberjack，它是在版本 2.0.7 中引入的，是由 Fluent Bit 的嵌入式 HTTP 服务器解析跟踪请求中的堆缓冲区溢出漏洞引起。

尽管未经身份验证的攻击者可以轻松利用该安全漏洞来触发拒绝服务或远程捕获敏感信息，但如果有适当的条件和足够的时间来创建可靠的漏洞，他们也可以使用它来获得远程代码执行。

安全研究人员表示：“虽然已知此类堆缓冲区溢出是可利用的，但创建可靠的漏洞利用不仅困难，而且非常耗时。”

研究人员认为，最直接、最主要的风险是那些与 DoS 和信息泄露的简易程度有关的风险。

**Fluent Bit 3.0.4 附带的补丁**

Tenable 于 4 月 30 日向供应商报告了此安全漏洞，并于 5 月 15 日将修复程序提交到 Fluent Bit 的主分支。包含此补丁的官方版本预计将与 Fluent Bit 3.0.4 一起发布。

Tenable 还于 5 月 15 日通过其漏洞披露平台向 Microsoft、Amazon 和 Google 通报了此严重安全漏洞。

在所有受影响的平台都可以使用修复程序之前，在自己的基础设施上部署此日志记录实用程序的客户可以通过限制授权用户和服务对 Fluent Bit 监控 API 的访问来缓解该问题。

如果不使用此易受攻击的 API 端点，用户还可以禁用它，以确保阻止任何潜在的攻击并删除攻击面。

文章翻译自：https://www.bleepingcomputer.com/news/security/critical-fluent-bit-flaw-impacts-all-major-cloud-providers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?tcTG8M8D)

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