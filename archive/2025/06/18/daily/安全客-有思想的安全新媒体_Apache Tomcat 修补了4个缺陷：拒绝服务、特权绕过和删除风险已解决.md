---
title: Apache Tomcat 修补了4个缺陷：拒绝服务、特权绕过和删除风险已解决
url: https://www.anquanke.com/post/id/308516
source: 安全客-有思想的安全新媒体
date: 2025-06-18
fetch_date: 2025-10-06T22:52:02.648335
---

# Apache Tomcat 修补了4个缺陷：拒绝服务、特权绕过和删除风险已解决

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

# Apache Tomcat 修补了4个缺陷：拒绝服务、特权绕过和删除风险已解决

阅读量**110436**

发布时间 : 2025-06-17 14:53:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/apache-tomcat-patches-4-flaws-dos-privilege-bypass-installer-risks-addressed/>

译文仅供参考，具体内容表达以及含义原文为准。

![Apache Tomcat 漏洞]()

Apache Software Foundation 披露了四个安全漏洞，这些漏洞影响了 Apache Tomcat（广泛使用的开源 Java servlet 容器）的多个版本。这些缺陷（从拒绝服务 （DoS） 情况到权限绕过和安装程序滥用）会影响 Tomcat 版本 9.0、10.1 和 11.0。

**CVE-2025-48976 – 通过多部分标头重载的 DoS**

Apache Commons FileUpload 之前对多部分标头大小强制实施了硬编码的 10kB 限制。包含大量分段标头的恶意请求可能会消耗过多内存，从而导致拒绝服务。

“*使用大量具有大标头的部件的特制请求可能会触发过多的内存使用，从而导致 DoS，*”该公告解释说。

通过 maxPartHeaderSize 连接器属性配置限制（现在默认仅为 512 字节）可以缓解此问题。

**CVE-2025-48988 – 分段上传滥用启用 DoS**

此漏洞还涉及分段上传，但侧重于段的总数，而不仅仅是标头大小。由于 Tomcat 以前在请求参数和部分之间共享内存限制，因此攻击者可能会用部分密集型上传淹没服务器，以耗尽内存并导致服务崩溃。

“*处理分段请求可能会导致内存使用量明显增加…使用大量部分的特制请求可能会触发过多的内存使用，从而导致 DoS，*“公告写道。

缓解措施现在包括一个新设置：maxPartCount，默认值为 10 个部分。

**CVE-2025-49124 – Windows 安装程序旁加载风险**

在 Windows 系统上，Tomcat 安装程序使用icacls.exe而不指定完整路径，如果系统路径中存在同名的恶意可执行文件，则可能允许旁加载攻击。

“*适用于 Windows 的 Tomcat 安装程序使用icacls.exe，但未指定完整路径。这启用了一个侧载漏洞，*“公告中写道。

虽然严重性评级为低，但安装程序可能被篡改的企业环境应采取措施。

**CVE-2025-49125 – Pre/PostResources 中的安全限制绕过**

当 Web 应用程序使用挂载在根目录外部的 PreResources 或 PostResources 时，Apache Tomcat 可能会允许通过备用路径进行意外访问。这些路径可能不受相同安全约束的保护，从而导致授权绕过。

“*可以通过一条意想不到的路径访问这些资源……允许绕过这些安全约束，*“该公告指出。

此缺陷的等级为中等，可能会影响任何依赖资源挂载进行访问控制的 Tomcat 部署。

**立即修补**

所有四个漏洞均已在以下修补版本中得到解决：

* Apache Tomcat 11.0.8 版本
* Apache Tomcat 10.1.42 版
* Apache Tomcat 9.0.106 版本

本文翻译自securityonline [原文链接](https://securityonline.info/apache-tomcat-patches-4-flaws-dos-privilege-bypass-installer-risks-addressed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308516](/post/id/308516)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/apache-tomcat-patches-4-flaws-dos-privilege-bypass-installer-risks-addressed/)

如若转载,请注明出处： <https://securityonline.info/apache-tomcat-patches-4-flaws-dos-privilege-bypass-installer-risks-addressed/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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