---
title: Android 安全告急：黑客伪造 Google Chrome 安装页，植入 SpyNote 恶意软件
url: https://www.anquanke.com/post/id/306509
source: 安全客-有思想的安全新媒体
date: 2025-04-15
fetch_date: 2025-10-06T22:05:09.630954
---

# Android 安全告急：黑客伪造 Google Chrome 安装页，植入 SpyNote 恶意软件

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

# Android 安全告急：黑客伪造 Google Chrome 安装页，植入 SpyNote 恶意软件

阅读量**52037**

发布时间 : 2025-04-14 15:26:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-mimic-google-chrome-install-page/>

译文仅供参考，具体内容表达以及含义原文为准。

安全研究人员发现了一场精心策划的恶意软件攻击活动，该活动通过虚假的 Google Chrome 安装页面来针对 Android 用户。

网络犯罪分子在新注册的域名上创建了具有欺骗性的网站，这些网站与 Google Play Store 上的 Google Chrome 安装页面极为相似。

这些欺诈性网站是传播 SpyNote 的载体，SpyNote 是一种功能强大的 Android 远程控制木马（RAT），具备全面监控、数据窃取以及对受感染设备进行完全远程控制的能力。

这些网站在视觉上与合法的 Google Play Store 页面高度相似，营造出一种极具说服力的假象，诱使毫无防备的用户安装恶意应用程序，让他们误以为自己是从Google 官方应用商店下载的正版软件。

上述被称为 SpyNote 的恶意软件，因其强大的功能，对移动设备的安全构成了重大威胁。一旦安装，SpyNote 就能获取包括短信、联系人、通话记录、位置数据和存储文件等在内的敏感信息。

更令人担忧的是，该恶意软件能够激活设备的摄像头和麦克风、操控通话、执行任意命令，还能针对应用程序的凭据实施强大的键盘记录功能。

SpyNote 与包括 OilRig（APT34）、APT-C-37（Pat-Bear）和 OilAlpha 等在内的高级持续性威胁（APT）组织有关联，这表明它既能用于有针对性的间谍活动，也适用于更广泛的网络犯罪活动。

DomainTools 的研究人员发现了攻击基础设施中的常见模式，指出许多恶意域名是通过 NameSilo, LLC 或 XinNet Technology Corporation 注册的。

他们的分析显示，这些恶意网站的托管模式具有一致性，其 IP 地址主要与 Lightnode Limite）和 Vultr Holdings LLC 相关。

这些网站本身的结构极为相似，恶意软件的配置以及命令与控制基础设施方面的差异微乎其微。

对于那些实行自带设备（BYOD）政策的组织，或者员工可能会在个人设备上不小心安装该恶意软件，随后这些设备又会连接到公司网络的组织而言，这场攻击活动构成了特别的威胁。

鉴于 SpyNote 的持续存在机制（通常需要恢复出厂设置才能彻底清除），受感染的设备存在重大的安全隐患。

该恶意软件能够通过辅助功能服务获取身份验证凭据并拦截双因素身份验证码，这使其成为夺取账户控制权和进一步渗透网络的有效工具。

#### ****感染机制解析****

这些具有欺骗性的网站运用了多种复杂手段来营造出令人信服的假象。

它们包括图片轮播功能，展示模仿 Google Play Store 应用页面的截图，这些截图来自诸如 “bafanglaicai888 [.] top” 等可疑域名，而这些域名很可能由同一批威胁行为者操控。

这些视觉元素旨在增强网站的可信度，减少受害者的怀疑。

当用户与虚假的 Google Play Store 界面进行交互时，他们会在无意识中触发一个名为 “download ()” 的 JavaScript 函数，该函数会从硬编码的 URL 中获取一个恶意的 .apk  文件。

这段 JavaScript 代码虽然简单，但通过一个不可见的 iframe 有效地实现了下载操作：

function download(url){

var src = url;

var iframe = document.createElement(‘iframe’);

iframe.style.display = ‘none’;

iframe.src = “javascript: ‘location.href=\”” + src + “\”‘”;

document.getElementsByTagName(‘body’)[0].appendChild(iframe);

}

下载的文件会启动一个两阶段的安装过程。最初的 .apk 文件充当释放器，安装第二个嵌入的 .apk 文件，该文件包含 SpyNote 恶意软件的核心功能。

该恶意软件通过 assets 文件夹中的 base.dex 文件来实现其命令与控制基础设施，该文件包含远程通信的连接参数。

命令与控制（C2）域名始终使用 8282 端口进行通信，一些变体直接在代码中硬编码了 IP 地址 “66.42.63.74”。

感染链的最后一步是该恶意软件大量请求众多具有侵入性的权限，从而获得对受感染设备的广泛控制权，并与攻击者控制的服务器建立持续通信。

这场攻击活动的复杂性凸显了移动设备面临的不断演变的威胁态势，也强调了即使网站看似来自合法来源，在下载应用程序时也务必保持谨慎的必要性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-mimic-google-chrome-install-page/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306509](/post/id/306509)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-mimic-google-chrome-install-page/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-mimic-google-chrome-install-page/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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