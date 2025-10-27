---
title: PTZOptics相机的零日漏洞正在被广泛利用
url: https://www.anquanke.com/post/id/301571
source: 安全客-有思想的安全新媒体
date: 2024-11-06
fetch_date: 2025-10-06T19:16:50.931386
---

# PTZOptics相机的零日漏洞正在被广泛利用

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

# PTZOptics相机的零日漏洞正在被广泛利用

阅读量**70815**

发布时间 : 2024-11-05 11:24:58

**x**

##### 译文声明

本文是翻译文章，文章来源：CN-SEC

原文地址：<https://cn-sec.com/archives/3353182.html>

译文仅供参考，具体内容表达以及含义原文为准。

![PTZOptics相机的零日漏洞正在被广泛利用]()

GreyNoise研究人员警告称，攻击者正在试图利用PTZOptics平移变焦（PTZ）直播[摄像机](https://cn-sec.com/archives/tag/%E6%91%84%E5%83%8F%E6%9C%BA)中的两个零日漏洞（CVE-2024-8956和CVE-2024-8957）。GreyNoise在其基于大型语言模型的威胁狩猎工具Sift检测到一个漏洞利用程序后，在调查过程中发现了这两个漏洞。这些零日漏洞存在于用于工业运营、医疗保健和其他敏感环境的物联网直播[摄像机](https://cn-sec.com/archives/tag/%E6%91%84%E5%83%8F%E6%9C%BA)中。

攻击者使用自动化的大规模侦察来部署漏洞利用程序。GreyNoise与VulnCheck合作，负责任地披露了这两个漏洞。“这些漏洞影响了多个厂商的启用NDI的平移变焦（PTZ）摄像机。

受影响的设备使用VHD PTZ摄像机固件<6.3.40，这些固件用于基于海思Hi3516A V600 SoC V60、V61和V63的PTZOptics、Multicam Systems SAS和SMTA Corporation设备。”GreyNoise发布的分析报告中写道。“据报道，这些摄像机具有嵌入式Web服务器，允许通过Web浏览器直接访问，它们被部署在可靠性和隐私至关重要的环境中。”

CVE-2024-8956（CVSS评分为9.1）是身份验证机制不足，可能允许攻击者访问敏感信息，例如用户名、MD5密码哈希和配置数据。

CVE-2024-8957（CVSS评分为7.2）是操作系统命令注入漏洞。攻击者可以使用CVE-2024-8956触发此漏洞，在受影响的摄像机上执行任意操作系统命令，这可能允许攻击者完全控制系统。攻击者可以利用此漏洞完全接管设备，查看或更改视频馈送，并危及敏感会话，例如商务会议或远程医疗。受损的摄像机可以添加到僵尸网络中，并用于执行拒绝服务攻击。攻击者还可以利用漏洞提取网络详细信息以渗透连接的系统，从而增加数据泄露和勒索软件攻击的风险。此外，攻击者可以完全错误配置或禁用摄像机，从而扰乱工业和其他敏感环境中的运营。

GreyNoise还观察到一起使用wget下载反向shell访问shell脚本的攻击实例。“使用VHD PTZ摄像机固件<6.3.40（用于基于海思Hi3516A V600 SoC V60、V61和V63的PTZOptics、Multicam Systems SAS和SMTA Corporation设备）的组织应立即采取措施修补已发现的漏洞并保护其系统。VulnCheck已将这些漏洞告知受影响的制造商，但仅收到了PTZOptics的回应。该制造商已发布了用于解决这些漏洞的固件更新。”报告总结道。

本文翻译自CN-SEC [原文链接](https://cn-sec.com/archives/3353182.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301571](/post/id/301571)

安全KER - 有思想的安全新媒体

本文转载自: [CN-SEC](https://cn-sec.com/archives/3353182.html)

如若转载,请注明出处： <https://cn-sec.com/archives/3353182.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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