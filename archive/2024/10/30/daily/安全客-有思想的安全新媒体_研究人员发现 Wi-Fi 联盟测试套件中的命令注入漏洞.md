---
title: 研究人员发现 Wi-Fi 联盟测试套件中的命令注入漏洞
url: https://www.anquanke.com/post/id/301369
source: 安全客-有思想的安全新媒体
date: 2024-10-30
fetch_date: 2025-10-06T18:46:42.885209
---

# 研究人员发现 Wi-Fi 联盟测试套件中的命令注入漏洞

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

# 研究人员发现 Wi-Fi 联盟测试套件中的命令注入漏洞

阅读量**57691**

发布时间 : 2024-10-29 14:24:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/researchers-discover-command-injection.html>

译文仅供参考，具体内容表达以及含义原文为准。

一个影响 Wi-Fi 测试套件的安全漏洞可使未经认证的本地攻击者以较高权限执行任意代码。

CERT 协调中心（CERT/CC）称，在 Arcadyan FMIMG51AX000J 路由器上发现了来自 Wi-Fi 联盟的受影响代码。该漏洞被追踪为 CVE-2024-41992。

CERT/CC 在周三发布的一份公告中说：“这个漏洞允许未经认证的本地攻击者通过发送特制数据包来利用 Wi-Fi 测试套件，从而在受影响的路由器上以 root 权限执行任意命令。”

Wi-Fi Test Suite 是 Wi-Fi 联盟开发的一个集成平台，可自动测试 Wi-Fi 组件或设备。虽然该工具包的开源组件是公开的，但完整的软件包只对其成员开放。

SSD Secure Disclosure 早在 2024 年 8 月就发布了该漏洞的详细信息，并将其描述为一个命令注入案例，可使威胁行为者以 root 权限执行命令。该漏洞最初是在 2024 年 4 月报告给 Wi-Fi 联盟的。

一位化名为 “fj016 ”的独立研究人员发现并报告了这一安全漏洞。该研究人员还提供了针对该漏洞的概念验证 (PoC) 漏洞。

CERT/CC 指出，Wi-Fi 测试套件并不打算用于生产环境，但在商用路由器部署中却发现了这一漏洞。

“成功利用该漏洞的攻击者可以获得对受影响设备的完全管理控制权，”它说。

“利用这种访问权限，攻击者可以修改系统设置、中断关键网络服务或完全重置设备。这些行为可能导致服务中断、网络数据泄露，并可能导致依赖受影响网络的所有用户失去服务。”

在台湾路由器制造商没有提供补丁的情况下，建议其他包含 Wi-Fi 测试套件的供应商要么从生产设备中完全删除该套件，要么将其更新到 9.0 或更高版本，以降低被利用的风险。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/researchers-discover-command-injection.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301369](/post/id/301369)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/researchers-discover-command-injection.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/researchers-discover-command-injection.html>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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