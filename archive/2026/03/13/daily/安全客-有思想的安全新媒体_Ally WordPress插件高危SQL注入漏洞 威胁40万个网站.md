---
title: Ally WordPress插件高危SQL注入漏洞 威胁40万个网站
url: https://www.anquanke.com/post/id/315140
source: 安全客-有思想的安全新媒体
date: 2026-03-13
fetch_date: 2026-03-14T04:02:59.625908
---

# Ally WordPress插件高危SQL注入漏洞 威胁40万个网站

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

# Ally WordPress插件高危SQL注入漏洞 威胁40万个网站

阅读量**32493**

发布时间 : 2026-03-13 10:34:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/high-severity-sql-injection-in-ally-wordpress-plugin-threatens-400k-sites/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

知名 WordPress 网页无障碍易用性插件**Ally**被曝出**高危 SQL 注入漏洞**。该插件活跃安装量超**40 万**，巨大的覆盖范围使其成为未授权攻击者窃取敏感数据库的重点目标。

该漏洞编号为**CVE-2026-2413**，**CVSS 评分为 7.5 分**。安全研究员 Drew Webber 通过 Wordfence 漏洞悬赏计划发现此漏洞，并在漏洞被引入插件代码仅 5 天后就提交报告，获得**800 美元**奖励。

漏洞存在于插件的`get_global_remediations()`方法中：该方法在将 URL 参数拼入数据库查询前，**未对其做充分的安全过滤**。尽管插件采取了部分防护措施，但仍不足以抵御针对性攻击。

Wordfence 报告指出：**即便使用了`esc_url_raw()`对 URL 做处理，也无法阻止单引号、括号等 SQL 元字符被注入**。

由于用户传入的 URL 参数**被直接拼接到 SQL JOIN 语句中，缺乏合规净化处理**，未授权攻击者可在原有查询语句后追加恶意 SQL 指令，进而从 WordPress 数据库中窃取密码哈希等高敏感数据。

此次漏洞利用方式为**时间型盲注（Time-Based blind SQL injection）**。该技术**复杂但成功率极高**，攻击者通过 SQL CASE 语句与`SLEEP()`函数，根据服务器响应时间逐字节窃取数据。

只有启用 Ally 插件中修复模块（Remediation）的网站才会受影响，该模块要求插件绑定 Elementor 账号。尽管受影响范围有所收窄，但插件庞大的安装基数仍使数千网站处于风险之中。

厂商已快速修复漏洞并采用更安全的编码规范：**开发者在 JOIN 语句中使用`wpdb->prepare()`函数**，确保用户输入被安全参数化绑定，而非简单拼接。

我们强烈建议用户尽快将**Ally 插件升级至已修复的最新版本（本文发布时为 4.1.0 版）**。

本文翻译自securityonline [原文链接](https://securityonline.info/high-severity-sql-injection-in-ally-wordpress-plugin-threatens-400k-sites/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315140](/post/id/315140)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/high-severity-sql-injection-in-ally-wordpress-plugin-threatens-400k-sites/)

如若转载,请注明出处： <https://securityonline.info/high-severity-sql-injection-in-ally-wordpress-plugin-threatens-400k-sites/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1090**

* 粉丝
* **6**

### TA的文章

* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13

### 相关文章

* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13
* ##### [Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据](/post/id/315158)

  2026-03-13 10:32:51
* ##### [Armadin获1.9亿美元融资 用AI实现自动化红队攻防](/post/id/315161)

  2026-03-13 10:32:28
* ##### [Splunk修复文件预览功能中的高危RCE漏洞](/post/id/315164)

  2026-03-13 10:32:03

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