---
title: Zenbleed攻击从AMD Zen2处理器窃取敏感数据
url: https://www.4hou.com/posts/xzLB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-30
fetch_date: 2025-10-04T11:52:26.086386
---

# Zenbleed攻击从AMD Zen2处理器窃取敏感数据

Zenbleed攻击从AMD Zen2处理器窃取敏感数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Zenbleed攻击从AMD Zen2处理器窃取敏感数据

ang010ela
[漏洞](https://www.4hou.com/category/vulnerable)
2023-07-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)107132

收藏

导语：​Zenbleed攻击从AMD Zen2处理器窃取敏感数据。

Zenbleed攻击从AMD Zen2处理器窃取敏感数据。

谷歌安全研究人员Tavis Ormandy发现了一个影响AMD Zen2 CPU处理器的安全漏洞——Zenbleed，漏洞CVE编号为CVE-2023-20593。攻击者利用该漏洞可以以30Kb/s的速度从CPU中窃取密码、加密密钥等敏感数据。

**漏洞概述**

推测执行是主流处理器使用的一种增强处理器性能的方法。Zenbleed漏洞产生的原因是推测执行过程中名为'vzeroupper'的指令处理不当导致的。

Ormandy使用和模糊和性能计数器发现了特定硬件事件，并使用Oracle序列化方法验证了结果。使用该方法可以检测到随机生成的程序和其序列化Oracle之间的不一致，最终成功发现了Zen2 CPU中的漏洞。

触发该漏洞后，研究人员成功从系统中窃取了敏感信息，包括虚拟机、隔离沙箱、容器等环境。30kb/s的信息窃取速度足以监控加密密钥和用户的登录密码等。

**漏洞影响**

虽然漏洞利用PoC是针对Linux系统的，但是该漏洞是操作系统无关，因此所有影响在Zen 2 CPU上的操作系统都受到该漏洞的影响。漏洞影响所有基于Zen 2架构的AMD CPU，包括Ryzen 3000、Ryzen 4000U/H ("Renoir")、Ryzen 5000U ("Lucienne")、Ryzen 7020、ThreadRipper 3000 和Epyc 服务器处理器。

但该漏洞对普通用户的实际影响并不大，因为漏洞利用需要对受影响的系统有物理访问权限，并且漏洞的利用需要很高程度的专业知识。

**漏洞补丁**

5月15日，研究人员将该漏洞提交给了AMD。7月24日，AMD针对受影响的系统发布了微代码。研究人员建议使用AMD Zen 2 CPU的用户尽快应用AMD的微代码更新。此外，研究人员称还可以通过将"chicken bit"设置为DE\_CFG来缓解该漏洞的影响，但这一操作会降低CPU的性能。

Ormandy称检测Zenbleed漏洞利用基本不可能，因为'vzeroupper'的不当使用并不需要很高的权限或特殊的系统调用，因此非常隐秘。

完整技术分析参见：https://lock.cmpxchg8b.com/zenbleed.html

本文翻译自：https://www.bleepingcomputer.com/news/security/zenbleed-attack-leaks-sensitive-data-from-amd-zen2-processors/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?RFCsLnV0)

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

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

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

[查看更多](https://www.4hou.com/member/e7OO)

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