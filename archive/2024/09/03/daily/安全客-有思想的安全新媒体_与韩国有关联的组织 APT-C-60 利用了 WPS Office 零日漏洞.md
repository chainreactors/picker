---
title: 与韩国有关联的组织 APT-C-60 利用了 WPS Office 零日漏洞
url: https://www.anquanke.com/post/id/299696
source: 安全客-有思想的安全新媒体
date: 2024-09-03
fetch_date: 2025-10-06T18:23:59.385881
---

# 与韩国有关联的组织 APT-C-60 利用了 WPS Office 零日漏洞

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

# 与韩国有关联的组织 APT-C-60 利用了 WPS Office 零日漏洞

阅读量**78443**

发布时间 : 2024-09-02 16:55:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源： securityaffairs

原文地址：<https://securityaffairs.com/167825/hacking/apt-c-60-wps-office-zero-day.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 与韩国有关联的组织 APT-C-60 利用 Windows 版 WPS Office 中的零日漏洞来瞄准东亚国家。

与韩国有关联的组织 APT-C-60 利用 Windows 版 WPS Office 中的零日漏洞（跟踪为 CVE-2024-7262），在东亚目标的系统中部署 SpyGlace 后门。

WPS Office 是由中国软件公司金山软件开发的一款综合办公生产力套件，在亚洲得到广泛使用。它为用户提供了一系列用于创建、编辑和管理文档、电子表格、演示文稿和 PDF 的工具。

根据 WPS 网站，WPS Office 在全球拥有超过 5 亿活跃用户，

ESET 研究人员在 WPS Office for Windows 中发现了该漏洞以及利用该漏洞的另一种方法 CVE-2924-7263。

SpyGlace 后门被 ThreatBook 公开列为 TaskControler.dll。

该漏洞源于 WPS Office 中对 URL 的验证和清理不当，允许攻击者创建恶意超链接。

根本原因分析显示，安装 WPS Office for Windows 后，它会注册一个名为 的自定义协议处理程序。此处理程序允许在用户单击以 URI 方案开头的 URL 时执行外部应用程序。在 Windows 中，此注册在系统注册表中完成。具体而言，注册表项配置为执行特定的 WPS Office 可执行文件 （），其参数包含完整 URL。此机制使 WPS Spreadsheet 应用程序能够在用户使用该协议与超链接交互时启动外部应用程序。`ksoqing``ksoqing://``HKCR\ksoqing\shell\open\command``wps.exe``ksoqing`

APT-C-60 的攻击涉及处理包含 base64 编码命令的 URL 参数以执行特定插件，从而导致从攻击者的服务器加载用作自定义后门“SpyGlace”加载器的恶意 DLL。APT-C-60 已将 SpyGlace 用于以前针对人力资源和贸易相关组织的攻击。

![WPS Office]()

强烈建议用户更新到最新版本的 WPSOffice，至少为 12.2.0.17119，以缓解这些代码执行漏洞。ESET 强调了该漏洞利用的有效性，指出它能够使用看起来合法的电子表格欺骗用户，并使用 MHTML 文件格式将代码执行缺陷转化为远程漏洞利用。

本文翻译自 securityaffairs [原文链接](https://securityaffairs.com/167825/hacking/apt-c-60-wps-office-zero-day.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299696](/post/id/299696)

安全KER - 有思想的安全新媒体

本文转载自:  [securityaffairs](https://securityaffairs.com/167825/hacking/apt-c-60-wps-office-zero-day.html)

如若转载,请注明出处： <https://securityaffairs.com/167825/hacking/apt-c-60-wps-office-zero-day.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

### 热门推荐

文章目录

* [与韩国有关联的组织 APT-C-60 利用 Windows 版 WPS Office 中的零日漏洞来瞄准东亚国家。](#h2-0)

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