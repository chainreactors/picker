---
title: Shopware 安全插件现漏洞，SQL 注入风险骤增
url: https://www.anquanke.com/post/id/306354
source: 安全客-有思想的安全新媒体
date: 2025-04-11
fetch_date: 2025-10-06T22:03:01.194473
---

# Shopware 安全插件现漏洞，SQL 注入风险骤增

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

# Shopware 安全插件现漏洞，SQL 注入风险骤增

阅读量**62200**

发布时间 : 2025-04-10 14:25:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/shopware-security-plugin-exposes-systems/>

译文仅供参考，具体内容表达以及含义原文为准。

一款旨在修复 Shopware 旧版本中安全漏洞的插件，其自身被发现容易受到 SQL 注入攻击。

这一漏洞是在 Shopware Security Plugin 6 的 2.0.10 版本中被发现的，受影响的是版本低于 6.5.8.13 和 6.6.5.1 的 Shopware 安装系统，攻击者有可能借此获取数据库系统的读写权限，进而对其造成破坏。

该漏洞源于对先前已知的 SQL 注入问题（CVE-2024-22406 和 CVE-2024-42357）的修复不彻底。

虽然这款安全插件本应追溯修复 Shopware 旧版本中的这些漏洞，但在实际实施过程中，由于嵌套的 API 请求，导致系统仍处于暴露状态。

这种疏忽为依赖插件进行保护的电子商务平台造成了重大的安全漏洞，同时延迟了完整版本的升级。

SQL 注入攻击使得恶意行为者能够操纵数据库查询，这有可能导致未经授权访问敏感的客户数据、交易记录，甚至使整个系统遭到破坏。

其严重程度取决于哪些用户可以访问 Shopware 的 API，如果 Store  API 中与搜索相关的端点被公开暴露，那么风险就会特别高。

Red Team Pentesting 的研究人员在 2025 年 2 月 12 日发现了这一漏洞，并指出虽然该安全插件正确修复了聚合对象name字段中的漏洞，但它未能对可以递归使用的嵌套聚合对象进行处理。

****可被利用的途径****

这一疏忽为能够访问 Shopware Store API 或Admin API 的攻击者提供了一条可利用的途径。

该技术漏洞存在于插件处理诸如 “/api/search/order” 等 API 端点中所使用的聚合字段的方式上。以下代码片段展示了安全插件中不完整的修复情况：

class PatchedAggregationParser extends AggregationParser

{

public function buildAggregations(EntityDefinition $definition, array $payload, Criteria $criteria, SearchRequestException $searchRequestException): void

{

parent::buildAggregations($definition, $payload, $criteria, $searchRequestException);

foreach ($criteria->getAggregations() as $i => $aggregation) {

if (str\_contains($aggregation->getName(), ‘?’) || str\_contains($aggregation->getName(), ‘:’)) {

$searchRequestException->add(new InvalidAggregationQueryException(‘Invalid character in aggregation name’));

}

}

}

}

这个 foreach 循环只检查了聚合对象最顶层的name字段，这就使得攻击者能够在嵌套的聚合对象中注入诸如 “?” 或 “:” 这样的符号。

攻击者可以通过精心构造特殊设计的查询语句，利用预编译语句机制来操纵数据库，从而利用这一漏洞。

Shopware 已经发布了安全插件 6 的 2.0.11 版本来修复这一漏洞。

或者，用户也可以升级到 Shopware 6.5.8.13 或 6.6.5.1 版本，这些版本独立于该安全插件修复了这一问题。鉴于存在权限提升和数据泄露的潜在风险，强烈建议立即进行补丁修复。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/shopware-security-plugin-exposes-systems/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306354](/post/id/306354)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/shopware-security-plugin-exposes-systems/)

如若转载,请注明出处： <https://cybersecuritynews.com/shopware-security-plugin-exposes-systems/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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