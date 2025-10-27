---
title: CISA 将大华 IP 摄像头、Linux 内核和 Microsoft Exchange Server 漏洞添加到已知利用漏洞目录中
url: https://www.anquanke.com/post/id/299427
source: 安全客-有思想的安全新媒体
date: 2024-08-24
fetch_date: 2025-10-06T18:01:06.912520
---

# CISA 将大华 IP 摄像头、Linux 内核和 Microsoft Exchange Server 漏洞添加到已知利用漏洞目录中

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

# CISA 将大华 IP 摄像头、Linux 内核和 Microsoft Exchange Server 漏洞添加到已知利用漏洞目录中

阅读量**83483**

发布时间 : 2024-08-23 11:21:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167414/uncategorized/u-s-cisa-dahua-ip-camera-linux-kernel-microsoft-exchange-server-bugs-its-known-exploited-vulnerabilities-catalog.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 美国网络安全和基础设施安全局 （CISA） 将大华 IP 摄像头、Linux 内核和 Microsoft Exchange Server 漏洞添加到其已知利用漏洞目录中。

美国网络安全和基础设施安全局 （CISA） 在其已知利用漏洞 （KEV） 目录中添加了以下漏洞：

* CVE-2021-33044 漏洞大华网络摄像机认证绕过漏洞
* CVE-2021-33045 漏洞大华网络摄像机认证绕过漏洞
* CVE-2022-0185 漏洞Linux 内核堆为基础的缓冲区溢出
* CVE-2021-31196 漏洞Microsoft Exchange Server 信息泄漏漏洞

2021 年 10 月，专家**警告说**，大华摄像头中的几个身份验证绕过漏洞存在概念验证 （PoC） 漏洞利用代码，分别被追踪为 CVE-2021-33044 和 CVE-2021-33045。

远程攻击者可以通过向易受攻击的摄像头发送特别构建的数据包来利用这两个漏洞。

*“在登录过程中，在部分大华产品中发现了身份认证绕过漏洞。攻击者可以通过构建恶意数据包来绕过设备身份验证，“供应商在 9 月初发布的公告中写道。*

该漏洞的 CVSS v3 得分为 8.1，供应商建议其客户安装安全更新。

受影响的型号列表很长，包括IPC-X3XXX，HX5XXX，HUM7XX，VTO75X95X，VTO65XXX，VTH542XH，PTZ半球摄像机SD1A1，SD22，SD49，SD50，SD52C，SD6AL，散热TPC-BF1241，TPC-BF2221，TPC-SD2221，TPC-BF5XXX，TPC-SD8X21，TPC-PT8X21B，NVR1XXX，NVR2XXX，NVR4XXX，NVR5XXX，NVR6XX。

对于野外的威胁行为者来说，使用像 Shodan 这样的搜索引擎找到暴露的大华设备并尝试使用可用的 PoC 代码来入侵它们可能非常容易。为了保护大华设备，用户必须安装最新的固件版本。

CVE-2022-0185 漏洞是一个 Linux 内核问题，与中国相关的威胁行为者在野外攻击中利用了该漏洞。

该漏洞是一个基于堆的缓冲区溢出缺陷，存在于 Linux 内核的文件系统上下文功能中的 legacy\_parse\_param 函数验证所提供参数长度的方式中。能够打开不支持文件系统上下文 API（因此回退到传统处理）的文件系统的非特权（如果启用了非特权用户命名空间，否则需要命名空间CAP\_SYS\_ADMIN权限）本地用户可利用此缺陷提升其在系统上的权限。

CVE-2021-31196 是 Microsoft Exchange Server 中的远程代码执行 （RCE） 缺陷。该漏洞专门影响 Microsoft Exchange Server 处理内存中对象的方式。成功利用此漏洞的攻击者可以获得使用与受影响的 Exchange Server 服务帐户相同的权限执行代码的能力。Microsoft 于 2021 年 5 月在其安全更新中发布了用于解决此漏洞的补丁。

根据约束性操作指令 （BOD） 22-01：降低已知被利用漏洞的重大风险，FCEB 机构必须在截止日期之前解决已识别的漏洞，以保护其网络免受利用目录中缺陷的攻击。

专家还建议私营组织审查目录并解决其基础设施中的漏洞。

CISA 命令联邦机构在 2024 年 9 月 11 日之前修复此漏洞。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167414/uncategorized/u-s-cisa-dahua-ip-camera-linux-kernel-microsoft-exchange-server-bugs-its-known-exploited-vulnerabilities-catalog.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299427](/post/id/299427)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167414/uncategorized/u-s-cisa-dahua-ip-camera-linux-kernel-microsoft-exchange-server-bugs-its-known-exploited-vulnerabilities-catalog.html)

如若转载,请注明出处： <https://securityaffairs.com/167414/uncategorized/u-s-cisa-dahua-ip-camera-linux-kernel-microsoft-exchange-server-bugs-its-known-exploited-vulnerabilities-catalog.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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

* [美国网络安全和基础设施安全局 （CISA） 将大华 IP 摄像头、Linux 内核和 Microsoft Exchange Server 漏洞添加到其已知利用漏洞目录中。](#h2-0)

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