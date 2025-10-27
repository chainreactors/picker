---
title: 研究人员发现 Kyber 后量子密钥封装机制 (KEM) 存在漏洞
url: https://www.anquanke.com/post/id/297064
source: 安全客-有思想的安全新媒体
date: 2024-06-06
fetch_date: 2025-10-06T16:55:33.678110
---

# 研究人员发现 Kyber 后量子密钥封装机制 (KEM) 存在漏洞

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

# 研究人员发现 Kyber 后量子密钥封装机制 (KEM) 存在漏洞

阅读量**100489**

发布时间 : 2024-06-05 10:26:55

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/kyber-post-quantum-key-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

一位安全研究人员在 Kyber 密钥封装机制 (KEM) 中发现了一个可利用的定时泄漏，该机制正在被 NIST 采用为后量子加密标准。

PQShield 的 Antoon Purnal 在一篇博客文章和社交媒体上详细介绍了他的发现，并指出该问题已在 Kyber 团队的帮助下得到解决。该问题出现在基于模块格子的密钥封装机制 (ML-KEM) 的参考实现中，该机制正在被采纳为NIST 后量子密钥封装标准。

**Clang 编译器引入侧通道漏洞**
Purnal 写道：“实施安全的一个关键部分是抵御侧信道攻击，侧信道攻击利用加密计算的物理副作用来推断敏感信息。”

为了防范旁道攻击，加密算法必须以某种方式实施，以便“攻击者可观察到的执行效果不会取决于它们处理的秘密”，他写道。在 ML-KEM 参考实施中，“我们关注的是几乎所有加密部署场景中都可观察到的特定旁道：时间。”

当编译器优化代码时，可能会出现此漏洞，在此过程中会悄悄撤销“熟练实施者采取的措施”。

在 Purnal 的分析中，发现 Clang 编译器在密钥封装和解封装所需的 ML-KEM 参考代码的poly\_frommsg函数中发出了一个易受攻击的秘密依赖分支，与 expand\_secure 实现相对应。

“在解封装过程中，poly\_frommsg 只使用一次。整个解封装过程需要超过 100K 个周期。这个分支产生的时间差异肯定太小而无足轻重吧？”Purnal 反问道。

“……经验丰富的本地攻击者可以执行高分辨率缓存攻击，以分支预测器为目标来了解哪些分支被采用，或者减慢库的速度来放大时间差异，”他回答道。“因此，谨慎的做法是修补。”

他说，测量完全解封装所需的时间“足以让攻击者拼凑出密钥”。

Purnal 在 GitHub 上发布了一个名为“clangover”的演示，展示了计时漏洞在恢复 ML-KEM 512 秘密加密密钥中的作用。他写道：“该演示在作者的笔记本电脑上不到 10 分钟就成功终止。”

**关键的后量子密钥漏洞**
Purnal 指出，虽然并非所有编译器、选项和平台都会受到影响，“但如果某个二进制文件受到影响，安全影响可能非常严重。因此，保守的做法是认真对待这个问题，并留意加密提供商提供的补丁。”

通过在单独的文件中将相关条件移动作为函数实现，对参考实现进行了修补。“这一变化使 Clang 无法识别条件标志的二进制性质，从而无法应用优化，”他说。

“值得注意的是，这并不排除其他基于参考实现但不逐字使用 poly\_frommsg 函数的库可能存在漏洞的可能性——无论是现在还是将来，”他总结道。

本文翻译自 [原文链接](https://thecyberexpress.com/kyber-post-quantum-key-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297064](/post/id/297064)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/kyber-post-quantum-key-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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