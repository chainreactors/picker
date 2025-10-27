---
title: JFrog研究人员发现，五分之一的 Docker Hub 存储库是恶意的
url: https://www.anquanke.com/post/id/296198
source: 安全客-有思想的安全新媒体
date: 2024-05-07
fetch_date: 2025-10-06T17:17:05.389737
---

# JFrog研究人员发现，五分之一的 Docker Hub 存储库是恶意的

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

# JFrog研究人员发现，五分之一的 Docker Hub 存储库是恶意的

阅读量**68546**

发布时间 : 2024-05-06 11:28:15

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybernews.com/security/fifth-of-docker-hub-repositories-malicious/>

译文仅供参考，具体内容表达以及含义原文为准。

***JFrog 的安全研究人员发现，Docker Hub（一个供 Web 开发人员协作编写 Web 应用程序代码的平台）上有近 300 万个存储库包含恶意内容。***

恶意行为者植入了数百万个没有任何图像的存储库，但这些存储库确实包含恶意元数据。其范围包括“从宣传盗版内容的简单垃圾邮件到由自动生成的帐户上传的恶意软件和网络钓鱼网站等极其恶意的实体”。

Docker Hub 是一个基于云的容器镜像存储库，提供公共和私有存储及协作解决方案。

存储库包含容器数据之上的文本描述和元数据。公共存储库还充当社区平台，它允许用户搜索和发现其项目的图像。

恶意行为者很快意识到他们可以利用文档功能来欺骗用户访问恶意网站。

JFrog 研究人员发现，460 万个公共存储库（占所有公共存储库的 30%）是无图像的。他们还透露，281 万个存储库可能与 Docker Hub 上运行的三个大规模恶意软件活动相关：

* “下载器”活动使用虚假 URL 缩短器将用户重定向到恶意软件下载。 9,309 位用户创建了 1,453,228 个此类存储库，占 Docker Hub 上所有存储库的 9.7%。
* “电子书网络钓鱼”活动承诺提供带有随机生成描述的免费电子书，但却窃取用户的信用卡信息并让用户进行昂贵的订阅。 1,042 位用户创建了 1,069,160 个此类存储库，占 Docker Hub 上所有存储库的 7.1%。
* “网站搜索引擎优化”活动没有明确的目标，因为存储库的内容大多是无害的。每个用户仅创建一个存储库。没有任何其他信息的随机短语可能被用来促进搜索引擎优化。 194,699 位用户创建了 215,451 个存储库 (1.4%)。

一些恶意存储库的活跃时间超过三年。

报告中写道：“Docker 安全团队迅速从 Docker Hub 中删除了所有恶意和不需要的存储库。”

建议用户优先选择标记为可信内容的 Docker 镜像，这些镜像是由信誉良好的来源策划和维护的。 “Docker 官方镜像”标签意味着存储库由知名软件开发基金会、组织和公司维护，例如 Python、Ubuntu 和 Node。

“Verified Publisher”标签标记属于 Docker Verified Publisher 计划一部分的存储库。 “赞助 OSS”标签分配给 Docker Hub 赞助的开源项目。

Cyber​​news 研究团队此前发现Docker Hub 上的数千个存储库还包含令牌、API 密钥和其他暴露敏感信息的秘密。

本文翻译自 [原文链接](https://cybernews.com/security/fifth-of-docker-hub-repositories-malicious/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296198](/post/id/296198)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybernews.com/security/fifth-of-docker-hub-repositories-malicious/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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