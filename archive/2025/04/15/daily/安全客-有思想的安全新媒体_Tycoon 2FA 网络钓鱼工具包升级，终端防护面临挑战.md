---
title: Tycoon 2FA 网络钓鱼工具包升级，终端防护面临挑战
url: https://www.anquanke.com/post/id/306517
source: 安全客-有思想的安全新媒体
date: 2025-04-15
fetch_date: 2025-10-06T22:05:08.518224
---

# Tycoon 2FA 网络钓鱼工具包升级，终端防护面临挑战

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

# Tycoon 2FA 网络钓鱼工具包升级，终端防护面临挑战

阅读量**50141**

发布时间 : 2025-04-14 15:50:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/tycoon-2fa-phishing-kit-employs-new-evasion-techniques/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现，随着 Tycoon 2FA 网络钓鱼工具包采用了旨在绕过现代终端保护系统复杂的规避技术，网络钓鱼策略发生了重大演变。

据观察，这款先进的工具包部署了多层混淆和反分析方法，这在网络钓鱼威胁领域中是一个令人担忧的新发展。

Tycoon 2FA 工具包的运作方式是创建逼真的合法登录页面副本，不仅能获取初始凭据，还能获取双因素身份验证令牌。

该工具包与早期版本的不同之处在于，它采用了多层防御机制，这使得安全工具和研究人员对其进行检测和分析的难度大幅增加。

2025 年 4 月初，Trustwave 的研究人员识别出了这款更新后的工具包，并指出了几项技术创新，这些创新表明网络钓鱼活动正变得越来越复杂。

记录这一发现的 Trustwave SpiderLabs 团队表示：“这些规避技术清楚地表明，威胁行为者在设计工具时迈出了进化的一步，目的是让工具在更长时间内不被发现。”

这些创新的影响不仅仅局限于直接受害者，因为持续时间更长的网络钓鱼活动在被发现之前可能会攻陷更多账户。

金融机构、企业组织和云服务提供商是主要目标，这款工具包专门设计用于获取对时间敏感的身份验证码。

从核心来看，Tycoon 2FA 采用了三种主要的规避技术：通过 HTML5 画布实现自定义验证码（CAPTCHA）、使用不可见的 Unicode 字符对 JavaScript 进行混淆处理，以及采取激进的反调试措施来阻止安全分析。

#### ****深入探究不可见的 Unicode 字符混淆技术****

该工具包规避策略中最具创新性的方面在于，它使用不可见的 Unicode 字符对恶意 JavaScript 代码进行编码。

这种技术将特定的不可见字符 —— 代表二进制 0 的半角韩文字符填充符（UTF-16：0xFFA0）和代表二进制 1 的韩文字符填充符（UTF-16：0x3164）与 JavaScript 代理对象相结合，将代码执行推迟到运行时。

解码机制的工作原理是将这些不可见字符转换为二进制字符串，将其分割成 8 位的片段，然后将每个片段转换为相应的字符：

class ObfuscatedDecoder {

static decode(obfuscatedString) {

const binaryString = Array.from(obfuscatedString)

.map(char => +(‘)}>>’ char))

.join(”);

return binaryString.match(/.{8}/g)

.map(byte => String.fromCharCode(parseInt(byte, 2)))

.join(”);

}

}

这种方法使得有效载荷在人工检查时完全不可见，同时也能避开模式匹配检测方法。

当与该工具包的其他保护机制（包括自定义验证码验证和检测分析工具的反调试脚本）相结合时，这就对传统的安全措施构成了一道难以逾越的障碍。

建议安全团队实施基于行为的监控，增强浏览器沙盒功能，并部署更深入的 JavaScript 检查机制，以应对这些不断演变的威胁。

Trustwave 已经发布了一条 YARA 检测规则，专门针对与最新 Tycoon 2FA 变种相关的 Unicode 字符混淆模式。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/tycoon-2fa-phishing-kit-employs-new-evasion-techniques/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306517](/post/id/306517)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/tycoon-2fa-phishing-kit-employs-new-evasion-techniques/)

如若转载,请注明出处： <https://cybersecuritynews.com/tycoon-2fa-phishing-kit-employs-new-evasion-techniques/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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