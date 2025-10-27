---
title: “Water Makara”使用Astaroth恶意软件对巴西组织进行有针对性的攻击
url: https://www.anquanke.com/post/id/300950
source: 安全客-有思想的安全新媒体
date: 2024-10-17
fetch_date: 2025-10-06T18:46:05.957904
---

# “Water Makara”使用Astaroth恶意软件对巴西组织进行有针对性的攻击

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

# “Water Makara”使用Astaroth恶意软件对巴西组织进行有针对性的攻击

阅读量**101767**

发布时间 : 2024-10-16 11:29:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/water-makara-employs-astaroth-malware-in-targeted-attacks-on-brazilian-organizations/>

译文仅供参考，具体内容表达以及含义原文为准。

![Water Makara - Astaroth Malware]()

趋势科技研究公司的一份最新报告指出，巴西出现了一种鱼叉式网络钓鱼活动，该活动结合使用了混淆 JavaScript 和 Astaroth 恶意软件，以各行各业的公司为目标。该活动背后的威胁行动者被追踪为 “Water Makara”，他们采用了复杂的技术来逃避检测，对该地区的制造企业、零售企业和政府机构构成了严重威胁。

该活动以伪装成官方税务通知或合规文件的网络钓鱼电子邮件开始，这种策略旨在引诱毫无戒心的用户。报告称，“这些电子邮件的附件通常伪装成个人所得税文件”，而这些附件中包含有害的 ZIP 文件。钓鱼邮件的主题行是 “Aviso de Irregularidade”（违规通知），诱骗收件人打开包含恶意 LNK 文件的 ZIP 文件。这些 LNK 文件被执行后，会通过 mshta.exe 工具运行嵌入的 JavaScript 命令，而 mshta.exe 工具是一个通常用于执行 HTML 应用程序的合法程序。

![]()

最终有效载荷为 Astaroth 恶意软件的鱼叉式网络钓鱼电子邮件示例 | 图片： 趋势科技研究

趋势科技研究人员解释说：“除了 LNK 文件外，ZIP 文件还包含另一个文件，其中有类似的混淆 JavaScript 命令，”这些命令在执行过程中会被解码，并连接到命令与控制（C&C）服务器以获取进一步的指令。

该活动的核心是 Astaroth，这是一种臭名昭著的银行木马，可窃取包括凭证和财务数据在内的敏感信息。一旦恶意软件站稳脚跟，它就会造成长期破坏，不仅包括数据盗窃，还包括监管罚款、业务中断和失去消费者信任。“报告警告说：”虽然 Astaroth 看起来像是一个古老的银行木马，但它的再次出现和持续演化使其成为一个持久的威胁。

Water Makara 采用了先进的混淆技术，使检测变得困难。研究人员发现，编码后的 JavaScript 命令会指向恶意 URL，如 patrimoniosoberano[.]world。这些 URL 采用了域名生成算法 (DGA)，这是网络犯罪分子用来创建大量域名从而逃避检测的一种策略。

巴西的制造业、零售业和政府部门是这一活动的主要目标。报告指出：“鱼叉式网络钓鱼活动主要针对巴西的公司，”“其中受影响最大的是制造公司、零售公司和政府机构”。

“报告总结道：”Water Makara 的鱼叉式网络钓鱼活动依赖于不知情的用户点击恶意文件，这凸显了人类意识的关键作用。

随着巴西继续面临来自复杂网络行为者的日益严重的威胁，防御这些极具针对性的鱼叉式网络钓鱼活动需要采取多层次的方法，将技术防御与强大的用户教育相结合。

本文翻译自securityonline [原文链接](https://securityonline.info/water-makara-employs-astaroth-malware-in-targeted-attacks-on-brazilian-organizations/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300950](/post/id/300950)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/water-makara-employs-astaroth-malware-in-targeted-attacks-on-brazilian-organizations/)

如若转载,请注明出处： <https://securityonline.info/water-makara-employs-astaroth-malware-in-targeted-attacks-on-brazilian-organizations/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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