---
title: CISA紧急警告：Git代码执行漏洞正遭黑客利用
url: https://www.anquanke.com/post/id/311567
source: 安全客-有思想的安全新媒体
date: 2025-08-28
fetch_date: 2025-10-07T00:18:29.065377
---

# CISA紧急警告：Git代码执行漏洞正遭黑客利用

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

# CISA紧急警告：Git代码执行漏洞正遭黑客利用

阅读量**46774**

发布时间 : 2025-08-27 17:35:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-git-code-execution-flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全与基础设施安全局（CISA）近日警告称，黑客正在利用分布式版本控制系统 Git 中存在的任意代码执行漏洞发动攻击。

该漏洞已被纳入 CISA 的“已知被利用漏洞（KEV）”目录，并要求美国联邦机构最迟于 9 月 15 日前完成修补。

Git 是目前主流的软件版本控制工具，广泛应用于软件开发团队进行代码变更管理，也是 GitHub、GitLab、Bitbucket 等协作平台的核心基础。

此次被利用的漏洞编号为 **CVE-2025-48384**，风险等级为高危。漏洞源于 Git 在配置文件中对回车符（\r）处理不当。由于 Git 在读写回车符时存在差异，导致子模块路径解析错误。攻击者可通过发布带有以 \r 结尾的子模块和精心构造的恶意符号链接，并在其中设置恶意 Hook，从而在受害者克隆仓库时实现任意代码执行。

Git 已于 2025 年 7 月 8 日发现该漏洞，并发布修复版本，包括 2.43.7、2.44.4、2.45.4、2.46.4、2.47.3、2.48.2、2.49.1 和 2.50.1。
若无法立即更新，官方建议开发者避免从不受信任来源递归克隆子模块，可通过 `core.hooksPath` 全局禁用 Git Hooks，或仅允许使用经过审计的子模块。

除 Git 漏洞外，CISA 还将两项 Citrix 会话录制（Session Recording）漏洞纳入 KEV 目录。这两项漏洞（CVE-2024-8068 和 CVE-2024-8069）均已于 2024 年 11 月由厂商修复，风险等级为中危。

1. **CVE-2024-8068**：允许与会话录制服务器同属一个 Active Directory 域的已认证用户，将权限提升至 NetworkService 账户。
2. **CVE-2024-8069**：允许已认证的内网用户通过反序列化不受信任数据，以 NetworkService 权限实现有限的远程代码执行。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-git-code-execution-flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311567](/post/id/311567)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-git-code-execution-flaw/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-git-code-execution-flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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