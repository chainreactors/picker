---
title: 非盈利数字图书馆互联网档案馆（The Internet Archive）披露遭遇重大数据泄露，影响超过 3100 万用户
url: https://www.anquanke.com/post/id/300798
source: 安全客-有思想的安全新媒体
date: 2024-10-13
fetch_date: 2025-10-06T18:46:57.144378
---

# 非盈利数字图书馆互联网档案馆（The Internet Archive）披露遭遇重大数据泄露，影响超过 3100 万用户

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

# 非盈利数字图书馆互联网档案馆（The Internet Archive）披露遭遇重大数据泄露，影响超过 3100 万用户

阅读量**76286**

发布时间 : 2024-10-12 11:03:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Fiona Jackson，文章来源：techrepublic

原文地址：<https://www.techrepublic.com/article/internet-archive-accounts-exposed/>

译文仅供参考，具体内容表达以及含义原文为准。

攻击者获得了一个 6.4 GB 的文件，其中包含在互联网档案馆注册的用户的电子邮件地址和散列密码。
互联网档案馆（The Internet Archive）是一家非营利性数字图书馆，因其 Wayback Machine 而闻名。

10 月 9 日下午，互联网档案馆的访问者开始看到弹出消息，内容如下： “你是否曾感觉互联网档案馆就像在木棍上运行一样，时刻处于遭受灾难性安全漏洞的边缘？这一切刚刚发生。我们在 HIBP 上见过 3100 万个你们！”

HIPB是 “我被破解了吗？”（Have I Been Pwned? – 是一个免费网站，用户可以通过它检查自己的个人信息是否在数据泄露事件中被泄露。

据 Bleeping Computer 报道，攻击者成功入侵了一个 6.4 GB 的 SQL 数据库，其中包含 Archive 注册会员的身份验证信息，包括电子邮件地址、网名、密码更改时间戳和 bcrypt 加密密码。

不过，HIBP 表示，54% 的外泄数据已经在其服务中被标记为在之前的外泄事件中暴露。目前尚不清楚攻击者是如何入侵互联网档案馆的，也不知道他们是否窃取了其他数据。

参见：全国公共数据泄露： 仅有 1.34 亿封电子邮件被泄露，公司承认事件发生

互联网安全公司 ESET 的全球网络安全顾问杰克-摩尔（Jake Moore）在一封电子邮件中告诉 TechRepublic： “黑客攻击过去通常在技术上是不可能的，但这次数据泄露事件可能是我们最接近的一次。被盗数据集包括个人信息，但至少被盗密码是加密的。

“不过，这也是一个很好的提醒，要确保你的所有密码都是唯一的，因为即使是加密密码也可以与以前使用过的密码进行交叉比对。

“Have I Been Pwned 是一项非常棒的免费服务，可以在发生漏洞后使用。它安全地包含了数百万个被破解的用户名和密码，人们可以安全地对照数据库检查自己的凭据，看看自己是否曾经被破解过。

“如果你发现自己的数据被泄露，最好更改密码并实施多因素身份验证”。

互联网档案馆的注册会员可以在网站重新上线后更改密码。

本周互联网档案馆遭受攻击的时间轴
数据集中最新的密码更改时间戳被发现是 9 月 28 日，这很可能就是密码被盗的时间。事实上，HIBP 操作员特洛伊-亨特（Troy Hunt）说，他是在 9 月 30 日收到该文件的，并通过将其数据与用户的账户详细信息进行匹配来验证该文件。

亨特在 X 上发表的一篇文章中说，他于 10 月 6 日首次向互联网档案馆通报了这一漏洞，并表示他将在 72 小时内把被盗数据加载到 HIBP 上。两天后，互联网档案馆遭到了一次明显无关的 DDoS 攻击，但在一小时内就得到了控制。

10 月 9 日，Hunt 开始将数据加载到 HIPB 上，巧合的是，弹出窗口开始出现。到美国东部时间下午 5:30，弹出窗口和网站本身都已失效，一些访问者看到了一条消息，称 “服务暂时离线”，请访问档案馆的 X 账户以获取更新。

据档案管理员杰森-斯科特（Jason Scott）称，该网站还遭遇了另一次 DDoS 攻击。Kahle 在美国东部时间晚上 9 点后通过 X 确认了这次入侵和 DDoS 攻击。他说，弹出窗口是通过 JavaScript 库添加的，后来被禁用了，第二次 DDoS “暂时被抵御住了”。

查看 富达数据泄露暴露了 77099 名客户的数据

然而，第二天早上，Kahle 又在 X 上发帖称，DDoS 攻击再次爆发，导致 archive.org 和 openlibrary.org 离线。在撰写本文时，这两个网站仍处于关闭状态，同时正在进行系统升级。

本文翻译自techrepublic [原文链接](https://www.techrepublic.com/article/internet-archive-accounts-exposed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300798](/post/id/300798)

安全KER - 有思想的安全新媒体

本文转载自: [techrepublic](https://www.techrepublic.com/article/internet-archive-accounts-exposed/)

如若转载,请注明出处： <https://www.techrepublic.com/article/internet-archive-accounts-exposed/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

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