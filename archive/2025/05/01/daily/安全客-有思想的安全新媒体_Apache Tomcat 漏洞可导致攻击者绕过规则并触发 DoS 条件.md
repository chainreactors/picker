---
title: Apache Tomcat 漏洞可导致攻击者绕过规则并触发 DoS 条件
url: https://www.anquanke.com/post/id/307057
source: 安全客-有思想的安全新媒体
date: 2025-05-01
fetch_date: 2025-10-06T22:23:25.296048
---

# Apache Tomcat 漏洞可导致攻击者绕过规则并触发 DoS 条件

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

# Apache Tomcat 漏洞可导致攻击者绕过规则并触发 DoS 条件

阅读量**146206**

发布时间 : 2025-04-30 14:16:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/apache-tomcat-vulnerability-let-bypass-rules/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Apache 软件基金会披露了 Apache Tomcat 中的一个重大安全漏洞，该漏洞可能允许攻击者绕过安全规则并通过操纵 HTTP 优先级标头 触发拒绝服务条件。

该高危漏洞编号为 CVE-2025-31650，影响多个 Tomcat 版本，对依赖此流行 Java 应用服务器的组织构成重大安全风险。

## Apache Tomcat 拒绝服务漏洞

该漏洞源于 Apache Tomcat 在处理 HTTP 优先级标头时输入验证不当。

根据安全公告，“对某些无效 HTTP 优先级标头的错误处理不正确，导致失败的请求清理不完整，从而造成内存泄漏”。

当攻击者发送大量包含无效 HTTP 优先级标头的格式错误的请求时，他们可能会触发 OutOfMemoryException，从而导致拒绝服务，使应用程序不可用。

HTTP 优先级标头是 Web 通信的合法组件，它指示客户端对响应传递优先级顺序的偏好。

然而，这个新的漏洞表明 Tomcat 对这些标头的处理存在一个缺陷，无法正确验证和清理输入。

|  |  |
| --- | --- |
| **风险因素** | **细节** |
| 受影响的产品 | Apache Tomcat 9.0.76–9.0.102Apache Tomcat 10.1.10–10.1.39Apache Tomcat 11.0.0-M2–11.0.5 |
| 影响 | 拒绝服务（DoS） |
| 漏洞利用前提条件 | 攻击者必须发送大量带有无效 HTTP 优先级标头的 HTTP 请求；无需身份验证 |
| CVSS 3.1 评分 | 高的 |

## 受影响的版本

该漏洞影响以下 Apache Tomcat 版本：

* Apache Tomcat 11.0.0-M2 至 11.0.5
* Apache Tomcat 10.1.10 至 10.1.39
* Apache Tomcat 9.0.76 至 9.0.102

这些版本的用户应立即考虑升级到修补版本。

该漏洞利用了 Tomcat 处理内存资源的方式。当服务器收到无效的 HTTP Priority 标头时，它无法正确清理资源，从而造成内存泄漏。

正如报告中所指出的，“大量此类请求可能会触发 OutOfMemoryException，从而导致拒绝服务”。

这让人想起了之前的 Java 应用程序内存问题。正如一位系统管理员在之前的事件中指出的那样，“Tomcat 无法释放未使用的内存。它只会不断添加内存，最终达到其最大分配内存量”。

## 减轻

Apache 软件基金会建议采取以下缓解措施：

* 升级到 Apache Tomcat 11.0.6 或更高版本
* 升级到 Apache Tomcat 10.1.40 或更高版本
* 升级到 Apache Tomcat 9.0.104 或更高版本

尽管 9.0.103 版本已修复此问题，但“9.0.103 候选版本的发布投票未通过”，因此尽管包含修复程序，但此版本并不包含在受影响的版本中。

这是近几个月来第二个重大Apache Tomcat 漏洞。2025 年 3 月，CVE-2025-24813 被披露，这是一个 CVSS 评分为 9.8 的严重远程代码执行漏洞，攻击者可以利用该漏洞控制易受攻击的服务器。

鉴于此漏洞的严重性及其完全禁用 Web 应用程序的可能性，强烈建议立即采取行动。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/apache-tomcat-vulnerability-let-bypass-rules/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307057](/post/id/307057)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/apache-tomcat-vulnerability-let-bypass-rules/)

如若转载,请注明出处： <https://cybersecuritynews.com/apache-tomcat-vulnerability-let-bypass-rules/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**6赞

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

* [Apache Tomcat 拒绝服务漏洞](#h2-0)
* [受影响的版本](#h2-1)
* [减轻](#h2-2)

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