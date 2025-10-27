---
title: 紧急预警：Morphing Meerkat 利用 DNS 技术，精准定制钓鱼页面威胁企业安全
url: https://www.anquanke.com/post/id/306319
source: 安全客-有思想的安全新媒体
date: 2025-04-10
fetch_date: 2025-10-06T22:03:59.284630
---

# 紧急预警：Morphing Meerkat 利用 DNS 技术，精准定制钓鱼页面威胁企业安全

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

# 紧急预警：Morphing Meerkat 利用 DNS 技术，精准定制钓鱼页面威胁企业安全

阅读量**53838**

发布时间 : 2025-04-09 14:34:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/morphing-meerkat-phaas-using-dns-reconnaissance/>

译文仅供参考，具体内容表达以及含义原文为准。

Morphing Meerkat 是一个复杂的网络钓鱼即服务（PhaaS）平台，于 2020 年首次被发现。它已从一个只能模仿五种电子邮件服务的简单工具，发展成为一个全面的网络犯罪资源平台，提供超过 100 种不同的诈骗模板。

这个平台代表了网络钓鱼方法上的重大进步，它利用先进的域名系统（DNS）侦察技术，根据受害者的电子邮件服务提供商来定制攻击方式。

该恶意软件的核心功能在于它能够动态生成极具说服力的网络钓鱼页面，这些页面与合法的电子邮件服务界面极为相似，极大地提高了窃取凭据操作的成功率。

当毫无防备的用户点击嵌入在 Morphing Meerkat 生成内容中的恶意链接时，该平台会立即开始侦察工作，分析域名信息以精心策划一场量身定制的攻击。

Check Point 的研究人员指出，这个平台特别危险的地方在于它在利用 DNS 方面的技术复杂性。

在分析该平台的运作方式时，他们发现它能够查询电子邮件域名的 DNS 邮件交换（MX）记录，使其能够精确识别目标所使用的特定电子邮件服务提供商。

Morphing Meerkat 的多语言功能和广泛的品牌仿冒特性，给全球各地的组织机构带来了严重的隐患。

随着该平台的不断发展，其网络钓鱼模板库也在不断扩充，这使得用户越来越难以区分合法的登录页面和欺诈性页面。

一旦凭据被窃取，利用这个平台的网络犯罪分子就能够未经授权访问企业网络和敏感信息，这可能会导致数据泄露、经济损失以及声誉受损。

### ****DNS 侦察的技术实现****

Morphing Meerkat 之所以有效，其技术基础在于它的 DNS 侦察机制。

当受害者点击恶意链接时，该平台会使用一个简单而有效的 DNS 查找函数，针对域名的 MX 记录执行查询操作：

async function identifyEmailProvider(domain) {

const mxRecords = await dns.resolveMx(domain);

const provider = analyzeMxRecords(mxRecords);

return generatePhishingPage(provider);}

这个函数使该平台能够确定目标用户是否使用 Microsoft 365、Google Workspace 或其他电子邮件服务提供商的服务。

在识别出目标用户所使用的电子邮件服务提供商后，Morphing Meerkat 会采用各种逃避检测的技术，包括开放重定向和代码混淆，以避免被安全工具检测到。

该平台甚至可能会在用户 “认证失败” 后，将其重定向到合法的登录页面，以减少用户的怀疑，营造出一种无缝的欺骗体验，以至于受害者往往在其凭据被盗取之后才会察觉到异常。

建议各组织机构实施强大的 DNS 安全措施、持续的监控系统、全面的员工培训计划以及多层级的网络安全解决方案，以防范这种不断演变的威胁。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/morphing-meerkat-phaas-using-dns-reconnaissance/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306319](/post/id/306319)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/morphing-meerkat-phaas-using-dns-reconnaissance/)

如若转载,请注明出处： <https://cybersecuritynews.com/morphing-meerkat-phaas-using-dns-reconnaissance/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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