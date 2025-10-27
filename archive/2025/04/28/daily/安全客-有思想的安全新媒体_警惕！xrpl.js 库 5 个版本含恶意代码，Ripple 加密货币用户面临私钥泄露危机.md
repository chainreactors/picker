---
title: 警惕！xrpl.js 库 5 个版本含恶意代码，Ripple 加密货币用户面临私钥泄露危机
url: https://www.anquanke.com/post/id/306923
source: 安全客-有思想的安全新媒体
date: 2025-04-28
fetch_date: 2025-10-06T22:04:15.846196
---

# 警惕！xrpl.js 库 5 个版本含恶意代码，Ripple 加密货币用户面临私钥泄露危机

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

# 警惕！xrpl.js 库 5 个版本含恶意代码，Ripple 加密货币用户面临私钥泄露危机

阅读量**64735**

发布时间 : 2025-04-27 14:25:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs 2

原文地址：<https://securityaffairs.com/176844/hacking/the-xrpl-js-ripple-cryptocurrency-library-was-compromised-in-a-supply-chain-attack.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Ripple 加密货币库在一场旨在窃取用户私钥的供应链攻击中遭到了入侵。

威胁行为者入侵了 Ripple 加密货币的 npm JavaScript 库 xrpl.js，以获取用户的私钥。

xrpl.js 是将 JavaScript/TypeScript 应用程序与 Ripple（XRP）集成的推荐库，每周下载量超过 14 万次。成千上万的应用程序和网站都使用这个软件包，到目前为止，该软件包的下载量已超过 290 万次。

4 月 21 日，Aikido Intel 检测到，作为供应链攻击的一部分，官方的 NPM 软件包被植入了后门程序。

Aikido Intel 发布的报告中写道：“格林尼治标准时间 + 0 4 月 21 日 20 点 53 分，我们 Aikido Intel 的系统开始发出警报，提示 xrpl 软件包出现了五个新的版本。它是 XRP Ledger 的官方软件开发工具包（SDK），每周下载量超过 14 万次。” “我们很快确认，官方的 Ripple（XPRL，即 Ripple）NPM 软件包已被老练的攻击者入侵，他们植入了一个后门程序，以窃取加密货币的私钥并获取对加密货币钱包的访问权限。”

研究人员对这次供应链攻击进行了调查，发现五个软件包版本（4.2.1、4.2.2、4.2.3、4.2.4 和 2.14.2）包含恶意代码。用户 “xrpl’mukulljangid” 从格林尼治标准时间 + 0 4 月 21 日 20 点 53 分开始发布了该库的所有五个含有恶意软件的版本。

研究人员注意到，代码中存在一个名为 checkValidityOfSeed 的函数，该函数被用于将窃取到的信息泄露到域名 “0x9c [.] xyz”。

![Ripple cryptocurrency npm JavaScript library xrpl.js ]()

目前尚不清楚这次攻击的幕后黑手是谁，不过专家指出，随着攻击者不断完善他们的攻击方法，出现了多次版本更新。4.2.1 版本删除了关键配置；4.2.2 版本引入了恶意 JavaScript 代码。后续版本（4.2.3、4.2.4）在 TypeScript 中添加了后门程序，这表明攻击者的策略在不断演变，他们试图避免被检测到，并且从手动插入代码转变为使用编译后的后门程序。

这个问题已在 4.2.5 版本和 2.14.3 版本中得到修复。

强烈敦促 xrpl.js 库的用户更新到 4.2.5 版本或 2.14.3 版本，以降低近期供应链攻击带来的风险。

该公司提供了受攻击的指标，以检查用户的系统是否可能受到了该库恶意版本的影响。

本文翻译自securityaffairs 2 [原文链接](https://securityaffairs.com/176844/hacking/the-xrpl-js-ripple-cryptocurrency-library-was-compromised-in-a-supply-chain-attack.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306923](/post/id/306923)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs 2](https://securityaffairs.com/176844/hacking/the-xrpl-js-ripple-cryptocurrency-library-was-compromised-in-a-supply-chain-attack.html)

如若转载,请注明出处： <https://securityaffairs.com/176844/hacking/the-xrpl-js-ripple-cryptocurrency-library-was-compromised-in-a-supply-chain-attack.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**10赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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