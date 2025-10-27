---
title: GHOSTPULSE 不断进化： 恶意软件现在隐藏在图像像素中，逃避检测
url: https://www.anquanke.com/post/id/301072
source: 安全客-有思想的安全新媒体
date: 2024-10-22
fetch_date: 2025-10-06T18:48:10.770987
---

# GHOSTPULSE 不断进化： 恶意软件现在隐藏在图像像素中，逃避检测

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

# GHOSTPULSE 不断进化： 恶意软件现在隐藏在图像像素中，逃避检测

阅读量**52429**

发布时间 : 2024-10-21 10:33:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/ghostpulse-evolves-malware-now-hides-in-image-pixels-evading-detection/>

译文仅供参考，具体内容表达以及含义原文为准。

![IMAPLoader malware]()

Elastic Security Labs 最近发现 GHOSTPULSE 恶意软件家族（又称 HIJACKLOADER 或 IDATLOADER）的战术发生了重大演变。Elastic Security Labs 在其最新报告中揭示了该恶意软件是如何从使用 PNG 文件的 IDAT 块转向将其有效载荷隐藏在像素结构本身中的。这种基于像素的算法代表了一种新的欺骗水平，使网络安全专业人员的检测和提取工作更具挑战性。

自 2023 年被发现以来，GHOSTPULSE 不断进化以躲避检测。在早期版本中，该恶意软件将其加密配置隐藏在 PNG 文件的 IDAT 块中，并通过解析这些文件来检索恶意有效载荷。然而，最新版本的恶意软件引入了像素级欺骗技术。正如 Elastic Security Labs 解释的那样，“恶意软件通过使用 GdiPlus(GDI+) 库中的标准 Windows API 依次提取每个像素的红、绿、蓝（RGB）值来构建字节数组”。

![GHOSTPULSE malware]()
新旧算法的伪代码对比 | 图片： 弹性安全实验室

通过直接在像素值中嵌入恶意数据，GHOSTPULSE 避开了依赖分析文件结构或文件头的检测机制。然后，恶意软件使用嵌入像素数据中的 CRC32 哈希值和 XOR 密钥解密配置。这种方法使 GHOSTPULSE 能够将其有效载荷隐藏在看似无害的图像中，使其更难被发现。

新版 GHOSTPULSE 不仅采用了先进的隐藏技术，还采用了更精简的发送方法。与依赖多文件包的早期版本不同，该恶意软件的最新迭代版本现在使用的是单个受损可执行文件，其资源部分包含一个大型 PNG 文件。该 PNG 文件包含加密配置和有效载荷，无需单独文件。

GHOSTPULSE 活动通常采用创造性的社交工程策略来诱骗用户执行恶意软件。在某些情况下，受害者会被诱骗完成一个虚假的验证码，验证码不是验证他们的身份，而是指示他们运行特定的 Windows 键盘快捷方式。这些快捷方式会触发恶意 PowerShell 脚本，启动 GHOSTPULSE 感染。

为了应对这种不断演变的威胁，Elastic Security Labs 更新了其检测机制。Elastic Defend 内置的原始 GHOSTPULSE YARA 规则仍能有效防止最后阶段的感染。不过，新开发的规则可以检测到这种基于像素的隐藏技术。“Elastic Security Labs 指出：”更新后的样本可以使用以下 YARA 规则进行检测，并将在未来的版本中与 Elastic Defend 一起发布。

本文翻译自securityonline [原文链接](https://securityonline.info/ghostpulse-evolves-malware-now-hides-in-image-pixels-evading-detection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301072](/post/id/301072)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/ghostpulse-evolves-malware-now-hides-in-image-pixels-evading-detection/)

如若转载,请注明出处： <https://securityonline.info/ghostpulse-evolves-malware-now-hides-in-image-pixels-evading-detection/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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