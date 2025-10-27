---
title: 关键NAS风险：9.8 CVD的IO数据缺陷允许远程命令执行
url: https://www.anquanke.com/post/id/307447
source: 安全客-有思想的安全新媒体
date: 2025-05-17
fetch_date: 2025-10-06T22:26:27.431849
---

# 关键NAS风险：9.8 CVD的IO数据缺陷允许远程命令执行

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

# 关键NAS风险：9.8 CVD的IO数据缺陷允许远程命令执行

阅读量**89486**

发布时间 : 2025-05-16 15:39:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/critical-nas-risk-i-o-data-flaw-with-9-8-cvss-allows-remote-command-execution/>

译文仅供参考，具体内容表达以及含义原文为准。

![I-O DATA, NAS, 命令注入]()

网络附加存储(NAS)设备已成为家庭和业务网络的重要组成部分,提供集中存储和数据访问。revealedJPERT/CC最近的一项咨询揭示了I-O DATA DEVICE,INC中的多个关键漏洞。“HDL-T系列”NAS设备,对数据安全和网络完整性构成重大风险。

JPCERT/CC vulnerabilities咨询强调了影响 I-O DATA HDL-T 系列的以下关键漏洞:

* 操作系统命令注入(CVE-2025-32002,CVSS 9.8):这是启用“远程链接3函数”时存在的关键漏洞。它允许远程、未经身份验证的攻击者在 NAS 设备上执行任意操作系统命令。
* 关键功能的缺失身份验证(CVE-2025-32738,CVSS 5.3[vulnerability](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)):此漏洞允许远程、未经身份验证的攻击者更改产品设置。

漏洞影响以下具有固件 Ver.1.21 及更早版本的 I-O DATA HDL-T 系列产品:

* HDL-TC1
* HDL-TC500发动机
* HDL-T1NV
* HDL-T1WH
* HDL-T2NV
* HDL-T2WH
* HDL-T3NV
* HDL-T3WH

[vulnerabilities](https://securityonline.info/hostedscan-review-proactive-vulnerability-management-for-a-bulletproof-digital-presence/)利用这些漏洞可能带来严重后果:

* [完整的系统妥协:操作系统命令注入漏洞](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)(CVE-2025-320022)允许攻击者执行任意命令,可能导致完全控制NAS设备。这可能导致数据窃取、修改或删除,以及恶意软件的安装。
* 未经授权的配置更改:缺少身份验证漏洞(CVE-2025-32738)使攻击者能够未经授权修改 NAS 设备的设置。这可能涉及更改访问控制、网络设置或其他配置,导致进一步的安全漏洞或服务中断。

缓解这些漏洞的推荐解决方案是更新受影响的HDL-T系列NAS设备的固件。I-O DATA DEVICE, INC. 发布了 [HDL-T 系列固件 Ver.](https://www.iodata.jp/support/information/2025/05_hdl-t/index.htm)1.22 解决了这些问题。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-nas-risk-i-o-data-flaw-with-9-8-cvss-allows-remote-command-execution/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307447](/post/id/307447)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-nas-risk-i-o-data-flaw-with-9-8-cvss-allows-remote-command-execution/)

如若转载,请注明出处： <https://securityonline.info/critical-nas-risk-i-o-data-flaw-with-9-8-cvss-allows-remote-command-execution/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**5赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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