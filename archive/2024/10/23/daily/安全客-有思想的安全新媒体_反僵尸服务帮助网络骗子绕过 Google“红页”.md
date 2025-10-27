---
title: 反僵尸服务帮助网络骗子绕过 Google“红页”
url: https://www.anquanke.com/post/id/301132
source: 安全客-有思想的安全新媒体
date: 2024-10-23
fetch_date: 2025-10-06T18:48:31.268357
---

# 反僵尸服务帮助网络骗子绕过 Google“红页”

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

# 反僵尸服务帮助网络骗子绕过 Google“红页”

阅读量**70257**

发布时间 : 2024-10-22 10:59:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Elizabeth Montalbano，文章来源：darkreading

原文地址：<https://www.darkreading.com/threat-intelligence/anti-bot-services-cybercrooks-bypass-google-red-page>

译文仅供参考，具体内容表达以及含义原文为准。

![Woman at desk holding a pen with left hand and right hand above a computer keyboard in front of a screen showing a mail icon and red warning circle]()

网络犯罪分子找到了一种新的方法来绕过对网络钓鱼攻击的有效威慑，即在暗网上销售的新型反机器人服务，这种服务允许他们绕过谷歌浏览器中提醒用户注意潜在欺诈行为的 “红页 ”保护性警告。

据SlashNext网站今天发表的最新研究报告称，反机器人服务旨在通过过滤网络安全机器人和伪装谷歌扫描仪无法识别的钓鱼网页，阻止安全爬虫识别钓鱼网页并将其列入黑名单。

红页是谷歌安全浏览（Google Safe Browsing）的一项功能，也是基于 Chromium 的浏览器和其他谷歌服务的一项功能，旨在通过警告用户潜在的危险（如网络钓鱼）来保护用户免受有害网站的侵害。该页面之所以被命名为 “安全浏览”，是因为它以红色显示，并警告用户正在浏览的网站可能具有欺骗性，建议用户避开。

帖子称，这样做可以 “严重 ”限制 “网络钓鱼攻击的潜在成功率”，为威胁活动提供 “巨大障碍”。这是因为这些活动依赖于高点击率，而当谷歌的检测标记一个网络钓鱼页面并将其添加到阻止列表时，点击率就会大大降低。

现在，在暗网上发现了各种反僵尸服务，如 Otus Anti-Bot、Remove Red 和 Limitless Anti-Bot 等，“有可能破坏这道防线，使更多用户面临复杂的网络钓鱼企图”。

**反僵尸服务的工作原理**

虽然每种服务都有自己独特的功能，但它们都基于几种技术的组合，使恶意内容能够绕过谷歌的红页功能。据 SlashNext 报道，大多数服务都依赖于僵尸检测机制，通过分析用户代理字符串和 IP 地址来过滤已知的安全僵尸流量，否则这些流量就会被阻止。

该帖子称：“网络安全爬虫的公开列表（如 Shodan）广泛存在，因此很容易过滤已知的安全僵尸流量。一旦某个 IP 地址或用户代理被标记为安全爬虫，就会被阻止，从而确保真实用户可以访问该网页，而网络安全实体则无法访问。”

这些服务还使用隐形技术，如上下文切换或 JavaScript 混淆，根据访问者的配置文件提供不同的内容。这些技术可以有效地将安全爬虫重定向到良性内容，同时将用户引导到钓鱼页面。

反僵尸服务的另一个共同特点是引入验证码或挑战页面，以过滤掉通常会分析网页恶意内容的自动扫描程序。“帖子称：”由于大多数机器人无法解决验证码问题，这种技术可以有效阻止它们，同时允许真实用户通过。

有些反机器人服务甚至会引入时间延迟，使安全机器人在扫描网页前 “超时”，从而进一步混淆用户，警告用户潜在的安全威胁。

据 SlashNext 报道，它们还可以通过提供特定地区的内容和阻止外国流量来绕过谷歌红页。研究人员指出，例如，如果网络钓鱼活动的目标是一家韩国银行，那么该服务可能只允许韩国流量访问该网站，同时阻止外国 IP 地址。此外，这些方法在地理位置方面可以变得非常具体，甚至可以将活动范围缩小到城市级别，这将阻止国际网络安全服务完全检测到该网页。

**并非完全万无一失**

研究人员指出，虽然这些反僵尸服务可以大大缩小谷歌红页的范围，但它们也有自己的局限性。研究人员指出，这些恶意服务在不太复杂的网络钓鱼活动中效果最好，因为它们可以识别并阻止用户代理字符串中的已知爬虫，而许多安全厂商都会在用户代理字符串中声明它们的机器人和爬虫。

帖子称：“这使得网络犯罪分子可以过滤掉僵尸流量，延长网络钓鱼活动的寿命。不过，在更复杂的网络钓鱼行动中，分析师的人工分析最终会检测到网页，从而将其列入拦截列表。”

尽管如此，任何能够限制终端用户发现网络钓鱼的行为都会对整体安全构成威胁，不仅是个人，还有企业。这是因为，尽管网络钓鱼是最古老的网络犯罪形式之一，但它仍然是攻击者初步进入企业网络实施其他类型恶意活动（如勒索软件攻击）的主要方式之一。

此外，网络钓鱼工具包的增加使攻击者很容易创建攻击活动，网络钓鱼策略的日益复杂，以及现在反僵尸服务的出现，都使个人和防御者的检测变得更加复杂。

据SlashNext网站报道，防止利用反僵尸服务绕过谷歌红页的最好办法是使用安全平台，这些平台可以在电子邮件、手机和信息应用程序中实时检测威胁，并尽可能准确。前面提到的对网络钓鱼网页的人工分析以及随后将恶意网站添加到阻止列表中，也可以阻止这些服务的有效使用。

本文翻译自darkreading [原文链接](https://www.darkreading.com/threat-intelligence/anti-bot-services-cybercrooks-bypass-google-red-page)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301132](/post/id/301132)

安全KER - 有思想的安全新媒体

本文转载自: [darkreading](https://www.darkreading.com/threat-intelligence/anti-bot-services-cybercrooks-bypass-google-red-page)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/anti-bot-services-cybercrooks-bypass-google-red-page>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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