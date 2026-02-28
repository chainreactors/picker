---
title: Python库ormar曝出高危SQL注入漏洞
url: https://www.anquanke.com/post/id/314890
source: 安全客-有思想的安全新媒体
date: 2026-02-27
fetch_date: 2026-02-28T03:49:59.922765
---

# Python库ormar曝出高危SQL注入漏洞

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Python库ormar曝出高危SQL注入漏洞

阅读量**24807**

发布时间 : 2026-02-27 10:29:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/critical-sql-injection-vulnerability-found-in-ormar-python-library/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

热门 Python 异步轻量级对象关系映射（ORM）库**ormar**被发现存在重大安全漏洞。该库主要用于衔接 Postgres、MySQL 和 SQLite 数据库，是众多开发者的核心工具。此次曝出的漏洞编号为**CVE-2026-26198**，**CVSS 评分高达 9.8 分**，可能导致未授权攻击者窃取整个数据库的全部数据。

ormar 的下载量已超**441 万次**，是 FastAPI 及各类异步 Python 应用的常用组件，因此该漏洞的潜在影响范围极大。

漏洞根源在于库中**聚合函数调用逻辑**，具体为`min()`和`max()`方法。技术报告指出，问题核心是该 ORM 框架 “将用户传入的列名直接传入`sqlalchemy.text()`构造 SQL 表达式，完全未做任何验证或净化处理”。

尽管`sum()`、`avg()`等其他函数通过类型检查实现了部分防护，但`min()`和`max()`函数完全跳过了这些安全校验。这一疏漏使得攻击者可向原生 SQL 查询中注入任意字符串。报告警示：“未授权用户可通过向列参数中注入子查询，利用该漏洞读取数据库全部内容，包括与查询模型无关的表数据。”

安全分析显示，该漏洞最早可追溯至**2021 年 3 月 12 日**—— 有问题的代码在 0.9.9 版本中被引入，且近四年间未做任何修改。

研究人员指出：“存在漏洞的`SelectAction.get_text_clause()`方法与`min()`/`max()`聚合函数是同期引入的…… 且相关漏洞代码自始至终未被修改。” 这意味着所有运行**0.9.9 至 0.22.0 版本 ormar**的应用当前均面临风险。

由于许多开发者严格遵循该库的官方文档进行开发，这一漏洞常被植入标准 API 设计中。报告特别强调，“支持用户自选聚合字段的 REST API” 或 “接收字段名作为参数的 GraphQL 解析器” 是最易受攻击的场景。

研究人员通过标准 FastAPI 应用验证了攻击可行性：**任何将用户可控输入传入`Model.objects.min()`或`Model.objects.max()`的 API 端点，都会成为完整的 SQL 注入入口**。该攻击方式已被证实可在所有主流支持的数据库后端（SQLite、PostgreSQL、MySQL）上成功实施。

ormar 维护团队已迅速修复该高危漏洞，**0.23.0 版本已完全解决此问题**。

研究人员强烈建议开发者和系统管理员立即审计 Python 运行环境，并**尽快将 ormar 依赖升级至最新版本**。

### 总结

1. ormar 库的`min()`/`max()`聚合函数因未校验用户输入，存在高危 SQL 注入漏洞（CVE-2026-26198，CVSS 9.8），可导致数据库全量数据泄露；
2. 0.9.9 至 0.22.0 版本均受影响，0.23.0 版本已完成修复，需立即升级；
3. 接收用户输入作为聚合字段的 FastAPI/GraphQL 接口是攻击重灾区，需重点审计。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-sql-injection-vulnerability-found-in-ormar-python-library/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314890](/post/id/314890)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-sql-injection-vulnerability-found-in-ormar-python-library/)

如若转载,请注明出处： <https://securityonline.info/critical-sql-injection-vulnerability-found-in-ormar-python-library/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1030**

* 粉丝
* **6**

### TA的文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [网络犯罪分子利用假冒Avast网站窃取用户信用卡信息](/post/id/314875)

  2026-02-27 10:30:44
* ##### [GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管](/post/id/314882)

  2026-02-27 10:30:24
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [Python库ormar曝出高危SQL注入漏洞](/post/id/314890)

  2026-02-27 10:29:42

### 相关文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [网络犯罪分子利用假冒Avast网站窃取用户信用卡信息](/post/id/314875)

  2026-02-27 10:30:44
* ##### [GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管](/post/id/314882)

  2026-02-27 10:30:24
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [未修补的ActiveMQ漏洞引发二次入侵与LockBit勒索攻击](/post/id/314906)

  2026-02-27 10:29:22
* ##### [Claude Code推出远程控制功能 实现移动端全自主开发](/post/id/314902)

  2026-02-27 10:28:57
* ##### [思科SD-WAN曝出CVSS 10级零日漏洞 已遭UAT-8616组织利用](/post/id/314880)

  2026-02-27 10:28:35

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)