---
title: Sophos揭露基于SVG的网络钓鱼攻击日益严重的威胁
url: https://www.anquanke.com/post/id/304002
source: 安全客-有思想的安全新媒体
date: 2025-02-11
fetch_date: 2025-10-06T20:35:00.220350
---

# Sophos揭露基于SVG的网络钓鱼攻击日益严重的威胁

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

# Sophos揭露基于SVG的网络钓鱼攻击日益严重的威胁

阅读量**252064**

发布时间 : 2025-02-10 09:58:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/sophos-uncovers-rising-threat-of-svg-based-phishing-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![SVG Phishing Attacks]()

来源：Sophos 公司

Sophos 公司发现了一种新型网络钓鱼技术，该技术利用可缩放矢量图形（SVG）文件绕过反垃圾邮件和反网络钓鱼防护机制，使攻击者能够传播恶意链接，进而窃取用户凭证。

据 Sophos 称，“通过电子邮件实施网络钓鱼攻击的犯罪分子，越发频繁地滥用一种旨在绕过现有反垃圾邮件和反网络钓鱼防护的新威胁载体：使用一种名为 SVG 的图形文件格式。”

SVG 文件通常用于基于矢量的图像，可在任何现代网页浏览器中读取。与 JPEG 或 PNG 等传统图像格式不同，SVG 文件包含基于文本的 XML 指令，其中可包括超链接、脚本和其他活动网页元素。

Sophos 的研究人员发现，网络钓鱼电子邮件中的恶意 SVG 附件不仅包含简单图形，还含有指向外部网络钓鱼页面的锚标签。

Sophos 解释称：“攻击中使用的 SVG 文件包含一些绘制非常简单形状（如矩形）的指令，但同时也包含一个指向其他地方托管网页的锚标签。”

当毫无防备的用户双击 SVG 电子邮件附件时，该文件会在其默认网页浏览器中自动打开，同时加载矢量图像和恶意链接。如果受害者点击嵌入的链接，就会被重定向到一个伪装成合法登录门户的凭证收集网站。

攻击者在网络钓鱼电子邮件中使用精心设计的社会工程诱饵，诱使收件人打开恶意 SVG 附件。这些邮件冒充知名品牌，如 DocuSign、微软 SharePoint、Dropbox 和谷歌语音，以提高其可信度。

Sophos 指出：“许多知名品牌和在线服务都遭到这些攻击的滥用，包括 DocuSign、微软 SharePoint、Dropbox、谷歌语音和 RingCentral。”

Sophos 的研究人员观察到越来越复杂的 SVG 网络钓鱼攻击，包括：

1.Cloudflare 验证码关卡 —— 受害者在被重定向到实际的网络钓鱼页面之前，需要 “证明自己是人”，这使得自动化安全扫描无效。

2.凭证预填充 —— 网络钓鱼页面会自动填充受害者的电子邮件地址，使其看起来合法。

3.实时网络钓鱼模板 —— 攻击者在 SVG 文件中嵌入实时链接，指向动态生成的虚假登录页面，常冒充微软 365 或 Dropbox。

4.JavaScript 自动重定向 —— 在某些情况下，SVG 文件无需点击即可自动加载网络钓鱼页面。

Sophos 警告称：“这些网络钓鱼页面均托管在攻击者控制的域名上，…… 几乎所有页面都设有 Cloudflare 验证码关卡，以防止自动访问。”

随着时间推移，这些攻击的复杂程度不断提高，攻击者不断完善其方法，使其看起来更具说服力。研究人员还发现了针对特定目标用户语言设计的本地化网络钓鱼页面。

Sophos 指出：“我们最终发现了针对不同语言的版本，这取决于收件人的顶级域名。例如，发送给日本学术机构目标对象的电子邮件及其嵌入的 SVG 均为日语制作。”

本文翻译自securityonline [原文链接](https://securityonline.info/sophos-uncovers-rising-threat-of-svg-based-phishing-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304002](/post/id/304002)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/sophos-uncovers-rising-threat-of-svg-based-phishing-attacks/)

如若转载,请注明出处： <https://securityonline.info/sophos-uncovers-rising-threat-of-svg-based-phishing-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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