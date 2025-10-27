---
title: 攻击者入侵ConnectWise，危及客户ScreenConnect实例
url: https://www.anquanke.com/post/id/308057
source: 安全客-有思想的安全新媒体
date: 2025-06-04
fetch_date: 2025-10-06T22:50:39.450691
---

# 攻击者入侵ConnectWise，危及客户ScreenConnect实例

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

# 攻击者入侵ConnectWise，危及客户ScreenConnect实例

阅读量**57046**

发布时间 : 2025-06-03 14:59:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2025/06/02/attackers-breached-connectwise-compromised-customer-screenconnect-instances/>

译文仅供参考，具体内容表达以及含义原文为准。

该公司周三透露，一个疑似“老练的民族国家行为者”已经入侵了“极少数”ConnectWise 客户的 ScreenConnect 云实例。

![受损的 ConnectWise ScreenConnect]( "ConnectWise")

“自 4 月 24 日发布补丁以来，我们没有在 ScreenConnect 云实例中观察到任何其他可疑活动，”他们在周五补充道。

该补丁修复了 CVE-2025-3935，这是一个影响 ScreenConnect 版本 25.2.3 及更早版本的 ViewState 反序列化漏洞，该漏洞可能允许攻击者注入恶意代码并在底层服务器上实现未经身份验证的远程代码执行。

### 发生了什么事？

ConnectWise 是一家总部位于佛罗里达州的公司，致力于为托管服务提供商 （MSP）、IT 部门和技术解决方案提供商 （TSP） 开发量身定制的软件解决方案。

ScreenConnect 是该公司流行的远程支持/访问产品，可以由 ConnectWise 托管在其云基础设施上，也可以由组织在其自己的专用物理或虚拟基础设施或私有云中自行托管。

ConnectWise 提到了其环境中的可疑活动，这表明 ConnectWise 托管的客户实例已经被盗用——显然是在部署 4 月 24 日补丁（针对 CVE-2025-3935）之前。

该公司最初的安全事件公告很简短，周五添加的常见问题 （FAQ） 部分未能更清楚地说明泄露是如何发生的。

ConnectWise 证实，Mandiant 的法医专家正在帮助他们调查入侵事件。我们已经联系了 ConnectWise 以获取更多信息，但他们只是向我们指出了稀疏的公告。

“我们的调查正在进行中，我们将尽可能分享更多信息，”该公司表示。

### 关于 CVE-2025-3935

ScreenConnect 是使用 ASP.NET 构建的， 是 Microsoft 开发的 Web 框架，用于构建 Web 应用程序和服务。

ASP.NET Web Forms 使用 ViewState 来记住两次访问之间的网页状态，方法是将相关数据转换为字符串，使用 Base64 进行编码，然后将其放入网页的\_\_VIEWSTATE隐藏字段中。为了防止此数据被篡改，ASP.NET 使用计算机密钥。

但是，如果攻击者获得了这些密钥，他们就可以构建一个恶意的 ViewState，并通过 POST 请求将其发送到网站。该网站会认为数据是安全的并会运行它，从而允许攻击者在网站的服务器上远程执行潜在的恶意代码。

因此，攻击的成功取决于攻击者获得提取机器密钥的特权访问权限，当然，也取决于他们知道如何利用反序列化漏洞。

ConnectWise 的开发人员通过推出 ScreenConnect 2025.4 补丁来降低这种风险，该补丁禁用了 ViewState 并消除了对它的任何依赖。

不幸的是，攻击者似乎在补丁实施之前就设法利用了这个漏洞：根据 Reddit 上一位（自称）受影响的客户的投诉，他们的实例遭到入侵发生在 2024 年 11 月。

ConnectWise 指出，该漏洞会影响 ScreenConnect，因此被标记为 CVE-2025-3935，尽管该问题有效地影响了使用 ASP.NET 框架/ViewState 的任何产品。

攻击者也利用类似的漏洞来破坏 Gladinet 的 CentreStack 和 Triofox 文件共享和远程访问平台：CVE-2025-30406 源于允许攻击者成功伪造 ViewState 数据的硬编码机器密钥。

去年，出于经济动机的威胁行为者和政府支持的攻击者臭名昭著地利用了 ScreenConnect 漏洞，但 ConnectWise 表示，这次最新的攻击与此无关。

“[最近发现的] 可疑活动与一个以情报收集而闻名的民族国家威胁行为者有关，”该公司分享道。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2025/06/02/attackers-breached-connectwise-compromised-customer-screenconnect-instances/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308057](/post/id/308057)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2025/06/02/attackers-breached-connectwise-compromised-customer-screenconnect-instances/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2025/06/02/attackers-breached-connectwise-compromised-customer-screenconnect-instances/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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