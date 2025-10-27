---
title: 黑客借力X平台Grok人工智能 通过推广帖子恶意链接传播量激增
url: https://www.anquanke.com/post/id/311942
source: 安全客-有思想的安全新媒体
date: 2025-09-06
fetch_date: 2025-10-02T19:43:04.705805
---

# 黑客借力X平台Grok人工智能 通过推广帖子恶意链接传播量激增

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

# 黑客借力X平台Grok人工智能 通过推广帖子恶意链接传播量激增

阅读量**398415**

发布时间 : 2025-09-05 18:17:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-exploit-xs-grok-ai/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为 **“Grokking”** 的新型网络攻击正在大规模滥用社交平台 X 的功能，用于传播恶意链接。

攻击者通过操纵平台的广告系统以及其生成式 AI —— **Grok**，绕过了安全检测，将 X 自身的工具变成了大规模恶意广告活动中的“帮凶”。

据 GuardioSecurity 研究员 **Nati Tal** 介绍，攻击的第一步是利用恶意软件推广所谓的“显卡”视频帖子。这类帖子往往包含露骨或猎奇的“成人”内容，以吸引用户点击。

虽然 X 的政策明令禁止在推广内容中直接加入外链，以打击恶意广告，但攻击者却发现了一个关键漏洞。

![]()

## 恶意链接的“隐藏点”

黑客并不会将恶意链接放在帖子正文里，而是埋在视频播放器下方的一个小小的 **“From:” 字段**中。

由于 X 的自动化安全扫描似乎忽略了这个区域，这些帖子得以顺利传播开来，每条推广帖甚至能获得 **10 万到 500 万次付费曝光**。

## 借助 Grok 放大攻击

攻击的第二阶段利用了平台的 AI 助手 **Grok**。很多用户因好奇而向 Grok 询问视频来源。

在尝试提供答案时，Grok 会扫描帖子信息，并从“From:”字段中提取域名。结果就是，**Grok 直接把恶意链接回复给用户**。

Tal 指出，研究人员观察到，当用户询问某个视频的出处时，Grok 会返回可疑域名的链接。

换句话说，Grok 不仅替攻击者“传话”，还在无意中提升了恶意链接的可见度和可信度。

![]()

## 平台信誉被滥用

由于这些恶意域名是由 X 的官方 AI 工具“引用”的，攻击者可能因此获得额外的搜索引擎优化（SEO）效果，甚至提升了这些恶意站点的信誉。对于毫无戒心的用户来说，这些链接看起来更值得信赖，从而进一步放大了风险。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-exploit-xs-grok-ai/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311942](/post/id/311942)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-exploit-xs-grok-ai/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-exploit-xs-grok-ai/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* [恶意链接的“隐藏点”](#h2-0)
* [借助 Grok 放大攻击](#h2-1)
* [平台信誉被滥用](#h2-2)

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