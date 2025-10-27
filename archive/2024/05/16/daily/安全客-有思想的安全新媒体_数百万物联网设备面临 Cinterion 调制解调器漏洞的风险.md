---
title: 数百万物联网设备面临 Cinterion 调制解调器漏洞的风险
url: https://www.anquanke.com/post/id/296504
source: 安全客-有思想的安全新媒体
date: 2024-05-16
fetch_date: 2025-10-06T17:13:54.227223
---

# 数百万物联网设备面临 Cinterion 调制解调器漏洞的风险

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

# 数百万物联网设备面临 Cinterion 调制解调器漏洞的风险

阅读量**68536**

发布时间 : 2024-05-15 11:43:54

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/millions-iot-cinterion-modem-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

由于广泛使用的蜂窝调制解调器技术存在多个漏洞，工业、医疗保健、汽车、金融和电信领域的数百万物联网 (IoT) 设备面临巨大风险。 Telit Cinterion 制造的调制解调器中发现的这些 Cinterion 调制解调器漏洞对设备完整性和网络安全构成严重威胁。

Telit Cinterion 是一家物联网 (IoT) 技术提供商公司，总部位于美国加利福尼亚州欧文市。它提供各种从边缘到云端的物联网服务，例如连接计划、物联网 SIM、物联网嵌入式软件和 PaaS 物联网部署托管服务。

新发现的漏洞对通信网络和物联网设备构成重大风险，可能导致广泛的全球破坏。

**发现多个 Cinterion 调制解调器漏洞**
卡巴斯基研究人员的研究结果首次在最近于柏林举行的 OffectiveCon 国际安全会议上公布。调查结果揭示了集成到各种物联网设备中的 Cinterion 调制解调器中的几个关键漏洞。

这些漏洞包括用户应用程序 (MIDlet) 以及与调制解调器集成的 OEM 捆绑固件中存在的远程代码执行 (RCE) 和未经授权的权限升级缺陷。

最严重的漏洞CVE-2023-47610 是内存堆溢出，攻击者可以通过该漏洞在受影响的设备上通过特制的短信远程执行任意命令，而无需进一步身份验证或任何物理访问。此漏洞还可以解锁对特殊 AT 命令的访问，使攻击者能够读取和写入调制解调器的 RAM 和闪存。

研究人员通过开发自己的基于 SMS 的文件系统来证明其存在，并利用已识别的漏洞将其安装在调制解调器上。这使得研究人员能够远程激活 OTA（无线配置）来安装任意 MIDlet，这些 MIDlet 受到标准机制的保护以防止删除，并且需要完全刷新固件才能删除。

除了 RCE 漏洞之外，研究人员还发现了名为 MIDlet 的用户应用程序和调制解调器的 OEM 捆绑固件中的几个安全问题。这些漏洞（编号为 CVE-2023-47611 至 CVE-2023-47616）可能允许具有调制解调器物理访问权限的攻击者破坏用户 MIDlet 的机密性和完整性、执行未经授权的代码、提取和替换数字签名以及提升执行权限将用户 MIDlet 提升到制造商级别。

研究人员去年 11 月向 Telit Cinterion 报告了这些漏洞，尽管该公司已针对部分漏洞发布了补丁，但并非所有漏洞都已得到解决，导致数百万台设备仍面临风险。

这些调制解调器嵌入到各种物联网产品中，包括工业设备、智能电表、远程信息处理系统和医疗设备，因此编制受影响产品的完整列表具有挑战性。

为了减轻潜在威胁，建议组织禁用非必要的短信功能、使用私有接入点名称 (APN)、控制对设备的物理访问，并定期进行安全审核和更新。

**人们对物联网安全的担忧日益加剧**
这些漏洞的发现凸显了人们对物联网环境安全性的日益关注，特别是在工业控制和操作技术环境中。 Nozomi Networks 对 2023 年威胁数据的分析指出，由于物联网漏洞的增加，针对物联网和 OT 网络的攻击显着增加。

之前的事件（例如 Robustel R1510 在工业路由器中发现的 9 个漏洞）表明，路由器仍然是网络中的一个常见弱点，存在远程代码执行或 DDoS 缺陷等漏洞，这些漏洞可能会被用来在连接的设备上传播攻击。

总之，Cinterion 调制解调器中的这些漏洞要求设备制造商和电信运营商采取紧急行动，以降低风险并保护重要基础设施。根据这项研究的结果，研究人员计划在 2024 年 5 月内发布有关调制解调器安全内部结构的白皮书。

本文翻译自 [原文链接](https://thecyberexpress.com/millions-iot-cinterion-modem-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296504](/post/id/296504)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/millions-iot-cinterion-modem-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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