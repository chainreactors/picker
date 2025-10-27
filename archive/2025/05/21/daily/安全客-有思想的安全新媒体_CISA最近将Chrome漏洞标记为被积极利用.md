---
title: CISA最近将Chrome漏洞标记为被积极利用
url: https://www.anquanke.com/post/id/307583
source: 安全客-有思想的安全新媒体
date: 2025-05-21
fetch_date: 2025-10-06T22:25:27.476366
---

# CISA最近将Chrome漏洞标记为被积极利用

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

# CISA最近将Chrome漏洞标记为被积极利用

阅读量**53850**

发布时间 : 2025-05-20 15:15:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 塞尔吉乌·加特兰，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cisa-tags-recently-patched-chrome-bug-as-actively-exploited-zero-day/>

译文仅供参考，具体内容表达以及含义原文为准。

![Google Chrome]()

周四,CISA警告美国联邦机构保护其系统免受利用Chrome网络浏览器中高严重性漏洞的持续攻击。

Solidlab安全研究员Vsevolod Kokorin发现了这个漏洞(CVE-2025-4664),并于5月5日在线分享了技术细节。released security updates谷歌周三发布了安全更新以修补它。

正如Kokorin解释的那样,due该漏洞是由于Google Chrome的Loader组件中策略执行不力,并且成功的利用可以允许远程攻击者通过恶意制作的HTML页面泄漏跨源数据。

你可能知道,与其他浏览器不同,Chrome 会解析子资源请求上的 Link 标头。但问题是什么?问题在于 Link 标头可以设置引用策略。我们可以指定不安全的URL并捕获完整的查询参数,“Kokorin指出。

查询参数可以包含敏感数据,例如,在 OAuth 流中,这可能会导致 Account 接管。开发人员很少考虑通过第三方资源的图像窃取查询参数的可能性。

虽然谷歌没有透露该漏洞以前是否在攻击中被滥用,或者它是否仍在被利用,但它在安全咨询中警告说,它有一个公开的漏洞,这通常是它暗示主动利用的方式。

###

### 被标记为被积极利用

一天后[,](https://www.cisa.gov/news-events/alerts/2025/05/15/cisa-adds-three-known-exploited-vulnerabilities-catalog)CISA证实CVE-2025-4664在野外被滥用,并将其添加到已知的受剥削脆弱性目录中,该目录列出了在攻击中积极利用的安全漏洞。

根据2021年11月具有约束力的操作指令(BOD)22-01,美国联邦文职行政部门(FCEB)机构必须在6月5日之前在三周内修补其Chrome安装,以保护其系统免受潜在违规行为的影响。

虽然此指令仅适用于联邦机构,但建议所有网络维护者尽快优先修补此漏洞。

“这些类型的漏洞是恶意网络行为者的频繁攻击媒介,对联邦企业构成重大风险,”网络安全机构警告说。

这是谷歌今年第二个被谷歌积极利用的Chrome零日修补, 此前又出现了另一个高严重度的Chrome零日漏洞(CVE-2025-2783),该漏洞被滥用于针对俄罗斯政府组织、媒体机构和教育机构的网络间谍攻击。

发现零日攻击的卡巴斯基研究人员表示,威胁行为者使用CVE-2025-2783漏洞绕过Google Chrome的沙箱保护,并用恶意软件感染目标。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cisa-tags-recently-patched-chrome-bug-as-actively-exploited-zero-day/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307583](/post/id/307583)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cisa-tags-recently-patched-chrome-bug-as-actively-exploited-zero-day/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cisa-tags-recently-patched-chrome-bug-as-actively-exploited-zero-day/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [Cyera融资5.4亿美元，估值翻番，致力于人工智能数据保护](/post/id/308391)

  2025-06-12 14:36:27
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [Jenkins Gatling 插件中未修补的 XSS 漏洞会给用户带来风险 (CVE-2025-5806)](/post/id/308251)

  2025-06-09 17:13:32
* ##### [新的 Mirai 僵尸网络变种通过 CVE-2024-3721 瞄准 DVR 系统](/post/id/308245)

  2025-06-09 17:08:32
* ##### [HPE 发布针对 StoreOnce 漏洞的重要补丁程序](/post/id/308181)

  2025-06-06 15:04:41

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