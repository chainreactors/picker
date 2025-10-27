---
title: AMD 多款嵌入式处理器现安全隐患，官方建议升级固件防范
url: https://www.anquanke.com/post/id/304437
source: 安全客-有思想的安全新媒体
date: 2025-02-19
fetch_date: 2025-10-06T20:36:04.499767
---

# AMD 多款嵌入式处理器现安全隐患，官方建议升级固件防范

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

# AMD 多款嵌入式处理器现安全隐患，官方建议升级固件防范

阅读量**67123**

发布时间 : 2025-02-18 14:37:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/amd-patches-multi-vulnerabilities-in-embedded-processors/>

译文仅供参考，具体内容表达以及含义原文为准。

![AMD Embedded Processors Vulnerabilities]()

美国超微半导体公司（AMD）已发布安全更新，以修复其霄龙（EPYC）和锐龙（Ryzen）嵌入式处理器中的多个漏洞，其中一些漏洞可能导致任意代码执行、内存损坏或权限提升。最严重的漏洞的通用漏洞评分系统（CVSS）评分为 7.5 分（高危），并影响到各种系统管理模式（SMM）、安全加密虚拟化（SEV）以及固件组件。

安全公告列出了影响 AMD 嵌入式处理器系列的十个漏洞。其中，最严重的问题 ——CVE-2023-31342、CVE-2023-31343 和 CVE-2023-31345—— 每个漏洞的 CVSS 评分均为 7.5 分（高危），这些漏洞源于系统管理模式（SMM）处理程序中不当的输入验证。据 AMD 称，这些漏洞 “可能使具有特权的攻击者覆盖系统管理随机存取存储器（SMRAM），从而有可能导致任意代码执行”。

另一个高风险漏洞 CVE-2023-31352（CVSS 评分为 6.0 分，中危）影响到安全加密虚拟化（SEV）固件，AMD 警告称，“该漏洞可能使具有特权的攻击者读取未加密的内存，从而有可能导致虚拟机客户机私有数据丢失”。

其他值得注意的漏洞包括：

1.CVE-2023-20515（CVSS 评分为 5.7 分，中危）：固件可信平台模块（fTPM）驱动程序中不当的访问控制可能会让具有特权的攻击者损坏系统内存，损害数据完整性。

2.CVE-2023-20582（CVSS 评分为 5.3 分，中危）：输入输出内存管理单元（IOMMU）中的缺陷可能使攻击者绕过安全加密虚拟化 – 安全嵌套分页（SEV-SNP）中的受保护内存区域（RMP）检查，影响虚拟机客户机内存的安全性。

3.CVE-2023-31356（CVSS 评分为 4.4 分，中危）：安全加密虚拟化（SEV）固件中不完整的系统内存清理可能会损坏虚拟机客户机的私有内存，影响数据完整性。

AMD 已确认这些漏洞会影响霄龙嵌入式 3000 系列、7002 系列、7003 系列、9004 系列，以及锐龙嵌入式 R1000 系列、R2000 系列、5000 系列、7000 系列、V1000 系列、V2000 系列和 V3000 系列。

为应对这些安全风险，AMD 建议更新平台初始化（PI）固件。一些关键的固件更新包括：

1.适用于霄龙嵌入式 7003 系列的 EmbMilanPI-SP3 1.0.0.8 版本（2024 年 1 月 15 日发布）

2.适用于霄龙嵌入式 9004 系列的 EmbGenoaPI-SP5 1.0.0.7 版本（2024 年 7 月 15 日发布）

3.适用于锐龙嵌入式 R1000 系列的 EmbeddedPI-FP5 1.2.0.C 版本（2024 年 6 月 14 日发布）

4.适用于锐龙嵌入式 7000 系列的 EmbeddedAM5PI 1.0.0.1 版本（2024 年 7 月 31 日发布）

AMD 建议所有使用受影响嵌入式处理器的客户和供应商：

1.尽快应用最新的固件更新，以降低潜在的被利用风险。

2.与原始设备制造商（OEM）供应商合作，确保基本输入输出系统（BIOS）和固件补丁得到妥善部署。

3.实施严格的访问控制策略，防止未经授权的固件修改。

本文翻译自securityonline [原文链接](https://securityonline.info/amd-patches-multi-vulnerabilities-in-embedded-processors/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304437](/post/id/304437)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/amd-patches-multi-vulnerabilities-in-embedded-processors/)

如若转载,请注明出处： <https://securityonline.info/amd-patches-multi-vulnerabilities-in-embedded-processors/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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