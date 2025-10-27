---
title: Google Project Zero 研究人员发现针对三星设备的零点击漏洞
url: https://www.anquanke.com/post/id/303453
source: 安全客-有思想的安全新媒体
date: 2025-01-14
fetch_date: 2025-10-06T20:04:35.698718
---

# Google Project Zero 研究人员发现针对三星设备的零点击漏洞

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

# Google Project Zero 研究人员发现针对三星设备的零点击漏洞

阅读量**60941**

发布时间 : 2025-01-13 14:13:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/01/google-project-zero-researcher-uncovers.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员详细介绍了一个现已打补丁的安全漏洞，该漏洞影响三星智能手机上的 Monkey’s Audio (APE) 解码器，可能导致代码执行。

该高严重性漏洞被追踪为 CVE-2024-49415（CVSS 得分：8.1），影响运行 Android 12、13 和 14 版本的三星设备。

“SMR Dec-2024 Release 1之前的libsaped.so中的越界写入允许远程攻击者执行任意代码，”三星在2024年12月针对该漏洞发布的公告中说，这是其每月安全更新的一部分。“补丁增加了适当的输入验证。”

发现并报告这一缺陷的谷歌 Project Zero 研究员娜塔莉-希尔瓦诺维奇（Natalie Silvanovich）将其描述为不需要用户交互即可触发（即零点击），在特定条件下是一个 “有趣的新攻击面”。

特别是，如果谷歌信息被配置为富通信服务（RCS）（Galaxy S23 和 S24 手机的默认配置），这种方法就会起作用，因为转录服务会在用户与信息交互之前对传入音频进行本地解码，以便转录。

Silvanovich 解释说：“libsaped.so 中的 saped\_rec 函数写入 C2 媒体服务分配的 dmabuf，其大小似乎总是 0x120000。”

“虽然 libsapedextractor 提取的每帧最大块值也限制在 0x120000，但如果输入的每个采样字节数为 24，saped\_rec 最多可以写出 3 \* 每帧块字节数。这就意味着，每帧块数较大的 APE 文件可能会大量溢出该缓冲区。”

在假设的攻击场景中，攻击者可以通过谷歌信息向任何启用了 RCS 的目标设备发送特制的音频信息，导致其媒体编解码器进程（“samsung.soft.media.c2”）崩溃。

三星的 2024 年 12 月补丁还解决了 SmartSwitch 中的另一个高严重性漏洞（CVE-2024-49413，CVSS 得分：7.1），该漏洞可能允许本地攻击者利用对加密签名的不当验证安装恶意应用程序。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/01/google-project-zero-researcher-uncovers.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303453](/post/id/303453)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/01/google-project-zero-researcher-uncovers.html)

如若转载,请注明出处： <https://thehackernews.com/2025/01/google-project-zero-researcher-uncovers.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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