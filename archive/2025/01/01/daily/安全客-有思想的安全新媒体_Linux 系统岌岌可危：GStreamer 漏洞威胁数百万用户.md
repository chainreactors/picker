---
title: Linux 系统岌岌可危：GStreamer 漏洞威胁数百万用户
url: https://www.anquanke.com/post/id/303158
source: 安全客-有思想的安全新媒体
date: 2025-01-01
fetch_date: 2025-10-06T20:04:34.629117
---

# Linux 系统岌岌可危：GStreamer 漏洞威胁数百万用户

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

# Linux 系统岌岌可危：GStreamer 漏洞威胁数百万用户

阅读量**78653**

发布时间 : 2024-12-31 09:00:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/linux-systems-at-risk-gstreamer-vulnerabilities-threaten-millions/>

译文仅供参考，具体内容表达以及含义原文为准。

GitHub 安全实验室的安东尼奥-莫拉莱斯（Antonio Morales）最近发布了一份报告，公布了 GStreamer 中的 29 个漏洞，GStreamer 是一个开源多媒体框架，广泛应用于 Ubuntu、Fedora 和 openSUSE 等 Linux 发行版。GStreamer 支持广泛的多媒体功能，包括音频和视频解码、字幕解析和媒体流。它与 Nautilus、GNOME Videos 和 Rhythmbox 等关键应用程序的集成使其成为许多系统的重要组件，也成为网络攻击者的诱人目标。

莫拉莱斯在报告中解释说：“GStreamer 是一个大型库，包括 300 多个不同的子模块。在这项研究中，我决定只关注 Ubuntu 发行版默认包含的’Base’和’Good’插件。”这些插件支持 MP4、MKV、OGG 和 AVI 等流行编解码器，因此特别容易被利用。

在已发现的 29 个漏洞中，大多数是在 MP4 和 MKV 格式中发现的。以下是一些最值得注意的漏洞：

* **CVE-2024-47537**：isomp4/qtdemux.c.中的越界（OOB）写入。
* **CVE-2024-47538**: vorbis\_handle\_identification\_packet 中的堆栈缓冲区溢出。
* **CVE-2024-47607**： gst\_opus\_dec\_parse\_header 中的堆栈缓冲区溢出。
* **CVE-2024-47615**: gst\_parse\_vorbis\_setup\_packet 中的 OOB 写入。
* **CVE-2024-47539**：convert\_to\_s334\_1a 中的 OOB 写入。

这些漏洞包括 OOB 写入、堆栈缓冲区溢出和空指针取消引用，所有这些漏洞都可能允许攻击者执行任意代码、导致系统崩溃或外泄敏感信息。

GStreamer 在桌面环境和多媒体应用程序中的广泛使用凸显了这些漏洞的严重性。莫拉莱斯称：“该库中的关键漏洞可以打开许多攻击载体。例如，恶意制作的媒体文件可以利用这些漏洞入侵用户系统。”

为了发现这些漏洞，莫拉莱斯采用了一种新颖的模糊方法。由于大型媒体文件的大小和复杂性，传统的覆盖引导模糊器在处理大型媒体文件时往往会遇到困难。莫拉莱斯选择了一种定制方法： 他说：“我从头开始创建了一个输入语料生成器，”他介绍说，该技术生成了 400 多万个测试文件，专门用于发现 MP4 和 MKV 解析器中的罕见执行路径。

我们敦促开发人员和用户尽快更新到最新的 GStreamer 补丁版本。

本文翻译自securityonline [原文链接](https://securityonline.info/linux-systems-at-risk-gstreamer-vulnerabilities-threaten-millions/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303158](/post/id/303158)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/linux-systems-at-risk-gstreamer-vulnerabilities-threaten-millions/)

如若转载,请注明出处： <https://securityonline.info/linux-systems-at-risk-gstreamer-vulnerabilities-threaten-millions/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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