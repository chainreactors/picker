---
title: 揭秘一种针对 WooCommerce 商店的新型复杂信用卡窃取技术
url: https://www.anquanke.com/post/id/300169
source: 安全客-有思想的安全新媒体
date: 2024-09-19
fetch_date: 2025-10-06T18:24:15.156491
---

# 揭秘一种针对 WooCommerce 商店的新型复杂信用卡窃取技术

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

# 揭秘一种针对 WooCommerce 商店的新型复杂信用卡窃取技术

阅读量**80534**

发布时间 : 2024-09-18 14:59:53

**x**

##### 译文声明

本文是翻译文章，文章来源：securityonline

原文地址：<https://securityonline.info/woocommerce-skimmer-employs-stealthy-tactics-to-pilfer-card-data/>

译文仅供参考，具体内容表达以及含义原文为准。

在 Sucuri 安全分析师 Ben Martin 的详细报告中，发现了一种针对 WooCommerce 商店的新的复杂信用卡盗刷技术。这种新颖的方法使用样式标签并将恶意代码伪装成图像文件，以便在结账时秘密窃取客户的信用卡详细信息。

撇渣器的操作从直接恶意注入结帐页面的源代码开始，通常是通过被盗用的管理员帐户实现的。一旦就位，恶意软件就会使用自定义的加扰机制来混淆其代码，使其在未经训练的人看来是胡言乱语。

这种攻击最非正统的元素之一是使用 <style> 标签而不是传统的 <script> 标签来执行 JavaScript。通常用于嵌入 CSS，<style> 标签还可以触发 onload 等事件，该事件在页面完全加载时运行脚本。在这种情况下，攻击者利用此属性隐藏恶意 JavaScript，这些 JavaScript 只会在用户输入敏感付款详细信息的结帐页面上激活。

这种策略使恶意软件能够逃避检测，因为网站所有者在扫描恶意代码时经常忽略<式>标签。大多数传统的刷卡恶意软件都可以通过 <script> 标签轻松识别，但此处使用 <style> 标签可实现更隐蔽的方法。

![WooCommerce 撇渣器]()

图片来源： Sucuri

攻击者通过将部分有效载荷嵌入到 .webp 图像文件中，进一步展示了他们的聪明才智。此文件伪装成网站的网站图标，即浏览器选项卡中出现的小图标。通过在图像中伪装他们的略读代码，攻击者可以避免在站点管理员查看其媒体库时引起怀疑。

经过仔细检查，Sucuri 分析师发现此“图像”的顶部包含混淆代码。图像文件不仅仅是一个无害的徽标，而且还包含与支付卡信息直接相关的字符串，例如“credit”、“expiry”、“CVV”以及“HolderFirst”和“HolderLast”名称。这种巧妙地伪装的支付表格窃取了用户的卡详细信息并将其发送到远程服务器。

![]()

“image” 文件 |图片来源： Sucuri

敦促网站所有者实施强大的安全实践，包括双因素身份验证、强密码、定期更新和使用网站防火墙。通过保持警惕并采用深度防御方法，企业可以更好地保护自己和客户免受 Magecart 攻击的无处不在的威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/woocommerce-skimmer-employs-stealthy-tactics-to-pilfer-card-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300169](/post/id/300169)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/woocommerce-skimmer-employs-stealthy-tactics-to-pilfer-card-data/)

如若转载,请注明出处： <https://securityonline.info/woocommerce-skimmer-employs-stealthy-tactics-to-pilfer-card-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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