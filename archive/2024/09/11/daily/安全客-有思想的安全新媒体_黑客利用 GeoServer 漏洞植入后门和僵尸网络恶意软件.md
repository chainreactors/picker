---
title: 黑客利用 GeoServer 漏洞植入后门和僵尸网络恶意软件
url: https://www.anquanke.com/post/id/299929
source: 安全客-有思想的安全新媒体
date: 2024-09-11
fetch_date: 2025-10-06T18:20:56.225324
---

# 黑客利用 GeoServer 漏洞植入后门和僵尸网络恶意软件

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

# 黑客利用 GeoServer 漏洞植入后门和僵尸网络恶意软件

阅读量**110648**

发布时间 : 2024-09-10 14:21:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/geoserver-vulnerability-targeted-by.html>

译文仅供参考，具体内容表达以及含义原文为准。

OSGeo GeoServer GeoTools 中最近披露的安全漏洞已被利用为多个活动的一部分，以提供加密货币矿工、Condi 和 JenX 等僵尸网络恶意软件，以及一个名为 SideWalk 的已知后门。

该安全漏洞是一个严重的远程代码执行错误（CVE-2024-36401，CVSS 评分：9.8），可能允许恶意行为者接管易受攻击的实例。

7 月中旬，美国网络安全和基础设施安全局 （CISA） 根据主动利用的证据，将其添加到已知利用漏洞 （KEV） 目录中。Shadowserver Foundation 表示，从 2024 年 7 月 9 日开始，它检测到针对其蜜罐传感器的漏洞利用企图。

据 Fortinet FortiGuard Labs 称，已观察到该漏洞被用于交付 GOREVERSE，这是一种反向代理服务器，旨在与命令和控制 （C2） 服务器建立连接，以进行利用后活动。

据说这些攻击的目标是印度的 IT 服务提供商、美国的科技公司、比利时的政府实体以及泰国和巴西的电信公司。

GeoServer 服务器还充当了 Condi 和名为 JenX 的 Mirai 僵尸网络变体以及至少四种类型的加密货币矿工的渠道，其中一种是从冒充印度特许会计师协会 （ICAI） 的虚假网站中检索到的。

也许利用该漏洞的攻击链中最引人注目的是传播名为 SideWalk 的高级 Linux 后门的攻击链，该后门归因于被跟踪为 APT41 的中国威胁行为者。

起点是一个 shell 脚本，该脚本负责下载 ARM、MIPS 和 X86 架构的 ELF 二进制文件，该脚本反过来又从加密配置中提取 C2 服务器，连接到该服务器，并接收进一步的命令，以便在受感染的设备上执行。

这包括运行称为快速反向代理 （FRP） 的合法工具，通过创建从主机到攻击者控制的服务器的加密隧道来逃避检测，从而允许持续的远程访问、数据泄露和有效负载部署。

“主要目标似乎分布在三个主要地区：南美、欧洲和亚洲，”安全研究人员 Cara Lin 和 Vincent Li 说。

“这种地理分布表明存在复杂而影响深远的攻击活动，可能会利用这些不同市场的常见漏洞，或针对这些地区普遍存在的特定行业。”

在此之前，CISA 本周在其 KEV 目录中添加了 2021 年在 DrayTek VigorConnect 中发现的两个缺陷（CVE-2021-20123 和 CVE-2021-20124，CVSS 评分：7.5），这些漏洞可能被利用以 root 权限从底层操作系统下载任意文件。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/geoserver-vulnerability-targeted-by.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299929](/post/id/299929)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/geoserver-vulnerability-targeted-by.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/geoserver-vulnerability-targeted-by.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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