---
title: 在 Baxter Life2000 通风系统中发现的关键漏洞
url: https://www.anquanke.com/post/id/301972
source: 安全客-有思想的安全新媒体
date: 2024-11-20
fetch_date: 2025-10-06T19:15:14.446134
---

# 在 Baxter Life2000 通风系统中发现的关键漏洞

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

# 在 Baxter Life2000 通风系统中发现的关键漏洞

阅读量**41933**

发布时间 : 2024-11-19 10:15:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/critical-vulnerabilities-found-in-baxter-life2000-ventilation-system/>

译文仅供参考，具体内容表达以及含义原文为准。

![Baxter Life2000 Ventilation System - CVE-2024-48966]()

关键基础设施领域使用的重要医疗保健设备百特 Life2000 通风系统被发现存在多个严重漏洞。这些问题在最近的安全公告（ICSMA-24-319-01）中有详细说明，带来的风险包括未经授权的访问、数据暴露和运行中断。

该公告概述了 Life2000 系统中的多个漏洞，包括

1. **CVE-2024-9834 (CVSSv4 9.3)： 敏感信息的明文传输**
   该漏洞允许攻击者利用设备的未加密串行接口获取未经授权的访问权限并操纵设备设置。Baxter 称这将导致未经授权的信息披露和/或对设备设置和性能造成意外影响。
2. **CVE-2024-9832 (CVSSv4 9.4)： 对过量验证尝试的不当限制**
   如果不限制登录尝试，攻击者就可以使用暴力技术访问呼吸机的设置，从而可能危及患者安全。
3. **CVE-2024-48971 (CVSSv4 9.4)： 使用硬编码凭证**
   硬编码临床医生密码允许攻击者绕过身份验证并控制呼吸机。
4. **CVE-2024-48973 (CVSSv4 9.4)： 物理访问控制不当**
   调试端口默认已启用，使设备容易受到物理篡改，从而导致数据泄露或未经授权的设置更改。
5. **CVE-2024-48974 (CVSSv4 9.4)： 下载未经完整性检查的代码**
   固件更新缺乏完整性检查为恶意代码注入打开了大门。
6. **CVE-2024-48966 (CVSSv4 10)： 关键功能验证缺失**
   用于测试和校准的服务工具缺乏身份验证，允许攻击者操纵设置或固件。

成功利用这些漏洞可导致

* **信息泄露**： 泄漏敏感的患者或操作数据。
* **设备中断**： 未经授权的设置更改可能导致设备无法运行。
* **患者安全风险**： 操纵关键功能会直接影响患者护理。

正如公告所述，这些漏洞 “可能导致信息泄露和/或设备功能中断而不被发现”。

虽然目前还没有利用这些漏洞的报告，但百特公司已经提供了临时指南：

* **物理安全**： 用户应避免将设备置于无人看管的不安全区域。
* **对更新保持警惕**： 巴克斯特计划在 2025 年第二季度之前发布解决这些问题的更新。
* **监控和报告**： 企业应实施日志记录和监控，以检测恶意活动并遵循适当的报告协议。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-vulnerabilities-found-in-baxter-life2000-ventilation-system/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301972](/post/id/301972)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-vulnerabilities-found-in-baxter-life2000-ventilation-system/)

如若转载,请注明出处： <https://securityonline.info/critical-vulnerabilities-found-in-baxter-life2000-ventilation-system/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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