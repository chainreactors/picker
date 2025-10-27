---
title: 警报拉响！新型 SVG 文件钓鱼攻击激增，传统防护体系濒临崩溃
url: https://www.anquanke.com/post/id/306893
source: 安全客-有思想的安全新媒体
date: 2025-04-26
fetch_date: 2025-10-06T22:03:57.654603
---

# 警报拉响！新型 SVG 文件钓鱼攻击激增，传统防护体系濒临崩溃

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

# 警报拉响！新型 SVG 文件钓鱼攻击激增，传统防护体系濒临崩溃

阅读量**108731**

发布时间 : 2025-04-25 14:45:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/threat-actors-using-weaponized-svg-files/>

译文仅供参考，具体内容表达以及含义原文为准。

2025 年，网络钓鱼活动发生了重大演变，威胁行为者越来越多地利用非常规文件格式来绕过安全防护解决方案。

一个尤为值得关注的趋势是，可缩放矢量图形（SVG）文件被恶意利用。这些文件中嵌入了恶意的 JavaScript 代码，其目的是将毫无防备的用户重定向到窃取凭据的网站。

这些攻击既利用了 SVG 文件本身固有的灵活性，又成功避开了传统的检测机制，使得威胁行为者能够顺利地将网络钓鱼的有效载荷发送到用户的收件箱中。

SVG 文件通常用于合法的网络图形设计，是一种基于 XML 的格式，能够呈现二维图形。

与传统的图像格式不同，SVG 文件支持嵌入脚本、超链接以及交互元素，这使得它们在合法用途和恶意利用方面都具有很强的通用性。

随着 SVG 文件在网页设计和营销材料中越来越受欢迎，攻击者有了可乘之机，在复杂的网络钓鱼活动中滥用这种文件格式。

Intezer 的研究人员注意到，在 2025 年年初，基于 SVG 文件的攻击显著增多，并记录了多个案例，在这些案例中，这些被恶意利用的文件成功绕过了电子邮件的防护系统。

根据他们的分析，这些恶意的 SVG 文件常常以看似无害的电子邮件附件形式出现，而且不会触发传统安全防护解决方案的警报。

研究团队报告称：“SVG 文件的灵活性使其成为绕过安全过滤器的理想选择，因为许多安全防护解决方案不会对 SVG 文件中嵌入的 JavaScript 代码进行深入检查。”

攻击方法是将经过 Base64 编码的 JavaScript 代码嵌入到 SVG 文件中，通常是在<iframe>或<embed>标签内。

当受害者打开 SVG 文件时，编码后的脚本就会执行，自行解码，并在用户毫无察觉的情况下将其重定向到一个专门用于窃取凭据的网络钓鱼网站。

这种攻击技术特别有效的原因在于，它采用了多层混淆手段，能够使恶意有效载荷躲过静态分析引擎的检测。

最令人担忧的是这些攻击在逃避检测方面的成功率。在多个有记录的案例中，恶意的 SVG 文件在 VirusTotal 上未被检测到任何威胁，这使得它们能够在不触发安全警报的情况下到达目标受害者手中。这种检测漏洞是当前电子邮件和终端安全防护解决方案中的一个重大盲点。

****感染机制与混淆技术****

基于 SVG 文件的攻击的复杂性体现在其编码和混淆技术上。

在分析样本文件 b5a7406d5b4ef47a62b8dd1e4bec7f1812162433955e3a5b750cc471cbfad93e 时，Intezer 的研究人员发现了一种复杂的多步骤混淆模式，这种模式旨在逃避检测。

恶意有效载荷最初是以<iframe>标签内的 Base64 编码数据形式存在的。

而经过混淆处理的 JavaScript 有效载荷遵循一种复杂的逃避检测模式：

var x3=”w+z-w+z-w+z-aqxm-6zfqx-09z-73xq-7bzqx-31-0qz-dq6-axq-0z3-exqzxq-7ez-3z9-6cx-b8zxq-ac-f3zx”;

x3=x3.replace(/[xqz]/g,””);

var y6=””;

var xp=x3.split(“-“);

for(i=0;i<xp.length;i++){

y6+=String.fromCharCode(parseInt(xp[i],16));

}

window.location=y6;

该脚本采用了多层防护措施：字符串反转、有策略地插入会被程序删除的垃圾字符、通过数学公式将十六进制转换为 ASCII 码，最后是重建 URL，将受害者重定向到一个窃取凭据的页面。

这种复杂的手段确保了传统的静态分析工具无法轻易识别出恶意行为。

为了应对这些威胁，Intezer 开发了专门的分析工具，能够解构这些混淆层。

他们的研究表明，有必要对非常规文件格式进行更深入的检查，并强调了在 2025 年的网络安全环境中，SVG 文件已日益成为一种常见的攻击载体。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/threat-actors-using-weaponized-svg-files/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306893](/post/id/306893)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/threat-actors-using-weaponized-svg-files/)

如若转载,请注明出处： <https://cybersecuritynews.com/threat-actors-using-weaponized-svg-files/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

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