---
title: Coyote恶意软件滥用Windows可访问性框架进行数据窃取
url: https://www.anquanke.com/post/id/310452
source: 安全客-有思想的安全新媒体
date: 2025-07-24
fetch_date: 2025-10-06T23:16:40.288967
---

# Coyote恶意软件滥用Windows可访问性框架进行数据窃取

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

# Coyote恶意软件滥用Windows可访问性框架进行数据窃取

阅读量**74815**

发布时间 : 2025-07-23 17:23:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/coyote-malware-abuses-windows-accessibility-framework-for-data-theft/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种新的银行木马变种“Coyote”开始利用Windows的可访问性功能——**微软的UI自动化框架（UIA）**，通过识别用户访问的银行和加密货币交易网站来窃取凭据。

微软的UIA是一个为残障人士设计的Windows可访问性框架，旨在帮助辅助技术与应用程序中的用户界面（UI）元素进行交互和控制。

Windows应用程序通过UI自动化树公开其UI元素，UIA API则提供了一种遍历该树、查询元素属性并与其交互的方式。

早在2024年12月，Akamai的研究人员就曾警告过，UIA可能会被恶意软件滥用来窃取凭据，指出该技术能够绕过端点检测与响应（EDR）防护。

现在，Akamai的研究团队报告称，自2025年2月起，他们已经在实际攻击中发现了滥用UIA的恶意软件，这标志着**首次有恶意软件在实际场景中使用微软UIA进行数据窃取**。

### **Coyote恶意软件的进化与UIA滥用**

Coyote是一种银行木马，主要**目标是窃取75个银行和加密货币交易平台的用户凭据**，特别是针对巴西用户。

该恶意软件最早在2024年2月被记录，最初采用键盘记录和钓鱼页面等技术，并自那时起得到了持续改进。

Akamai的报告称，尽管最新的Coyote变种仍然通过传统方式窃取硬编码应用的数据，但它在用户浏览网页银行或加密货币交易服务时，**增加了滥用UIA的新手段**。

如果Coyote无法通过窗口标题来识别目标，它会**利用UIA从浏览器的UI元素**（如标签或地址栏）中提取网页地址，并与目标服务的硬编码列表（75个网站）进行比对。

“如果找不到匹配项，Coyote会继续使用UIA解析窗口中的子元素，尝试识别浏览器标签或地址栏，”Akamai在报告中解释道。“然后，它会将这些UI元素的内容与之前的地址列表进行交叉验证。”

通过这种方法识别的银行和交易所包括：**Banco do Brasil、CaixaBank、Banco Bradesco、Santander、Original Bank、Sicredi、Banco do Nordeste、Expanse应用，以及加密货币交易所（如Binance、Electrum、Bitcoin、Foxbit等）**。

虽然目前滥用UIA的行为仅限于侦察阶段，Akamai也展示了一个概念验证，说明UIA可以被用来窃取用户输入的这些网站的凭据。

![]()

*演示微软用户界面自动化（UIA）如何被滥用于凭证窃取*
*来源：Akamai*

BleepingComputer已联系微软，询问是否会采取措施防止UIA被滥用，但目前未得到回复。

可访问性系统本是为了帮助残障人士更好地使用设备，功能非常强大，但这种强大也容易被恶意软件利用。在Android平台上，类似的问题已经非常严重，恶意软件大规模滥用可访问性服务。为此，谷歌也采取了多项措施来解决这个问题。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/coyote-malware-abuses-windows-accessibility-framework-for-data-theft/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310452](/post/id/310452)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/coyote-malware-abuses-windows-accessibility-framework-for-data-theft/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/coyote-malware-abuses-windows-accessibility-framework-for-data-theft/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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