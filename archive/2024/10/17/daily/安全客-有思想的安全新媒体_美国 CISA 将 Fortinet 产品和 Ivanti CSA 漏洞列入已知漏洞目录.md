---
title: 美国 CISA 将 Fortinet 产品和 Ivanti CSA 漏洞列入已知漏洞目录
url: https://www.anquanke.com/post/id/300963
source: 安全客-有思想的安全新媒体
date: 2024-10-17
fetch_date: 2025-10-06T18:46:01.237701
---

# 美国 CISA 将 Fortinet 产品和 Ivanti CSA 漏洞列入已知漏洞目录

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

# 美国 CISA 将 Fortinet 产品和 Ivanti CSA 漏洞列入已知漏洞目录

阅读量**73437**

发布时间 : 2024-10-16 14:30:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/169804/security/u-s-cisa-adds-fortinet-products-and-ivanti-csa-bugs-known-exploited-vulnerabilities-catalog.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**美国网络安全和基础设施安全局（CISA）在其已知漏洞目录中增加了 Fortinet 产品和 Ivanti CSA 漏洞。**
美国网络安全和基础设施安全局 (CISA) 在其已知漏洞 (KEV) 目录中增加了以下漏洞：

* CVE-2024-23113 (CVSS 得分 9.8) Fortinet 多种产品格式字符串漏洞。Fortinet FortiOS 中使用外部控制的格式字符串，允许攻击者通过特制数据包执行未经授权的代码或命令。
* CVE-2024-9379（CVSS 得分 6.5）在 5.0.2 版之前的 Ivanti CSA 的管理 web 控制台中存在 SQL 注入。具有管理员权限的远程验证攻击者可利用此漏洞运行任意 SQL 语句。
* CVE-2024-9380 (CVSS 得分 7.2) – 版本 5.0.2 之前的 Ivanti CSA 管理員網頁主控台中的作業系統指令注入漏洞。拥有管理员权限的远程验证攻击者可利用该漏洞实现远程代码执行。

上周，Ivanti 警告说，其云服务设备 (CSA) 中存在三个新的安全漏洞（CVE-2024-9379、CVE-2024-9380 和 CVE-2024-9381），这些漏洞在野外攻击中被积极利用。

威胁者正在将这三个漏洞与该软件公司 9 月份解决的 CSA 零日漏洞 CVE-2024-8963（CVSS 得分为 9.4）进行连锁。

威胁者可以利用这些漏洞实施 SQL 注入攻击，通过命令注入执行任意代码，以及通过滥用易受攻击的 CSA 网关上的路径遍历弱点绕过安全限制。

“Ivanti 发布的公告中写道：”据我们所知，当 CVE-2024-9379、CVE-2024-9380 或 CVE-2024-9381 与 CVE-2024-8963 相连时，运行 CSA 4.6 补丁 518 及以前版本的少数客户已被利用。“我们没有证据表明任何其他漏洞在野外被利用。这些漏洞不会影响任何其他 Ivanti 产品或解决方案”。

根据约束性操作指令（BOD）22-01： 减少已知漏洞被利用的重大风险》，FCEB 各机构必须在规定日期前解决已发现的漏洞，以保护其网络免受利用目录中漏洞的攻击。

专家还建议私营机构审查目录并解决其基础设施中的漏洞。

CISA 命令联邦机构在 2024 年 10 月 30 日前修复该漏洞。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/169804/security/u-s-cisa-adds-fortinet-products-and-ivanti-csa-bugs-known-exploited-vulnerabilities-catalog.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300963](/post/id/300963)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/169804/security/u-s-cisa-adds-fortinet-products-and-ivanti-csa-bugs-known-exploited-vulnerabilities-catalog.html)

如若转载,请注明出处： <https://securityaffairs.com/169804/security/u-s-cisa-adds-fortinet-products-and-ivanti-csa-bugs-known-exploited-vulnerabilities-catalog.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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