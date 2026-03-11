---
title: 海康威视与罗克韦尔自动化高危漏洞纳入CISA已知被利用漏洞清单
url: https://www.anquanke.com/post/id/315077
source: 安全客-有思想的安全新媒体
date: 2026-03-10
fetch_date: 2026-03-11T04:03:27.412994
---

# 海康威视与罗克韦尔自动化高危漏洞纳入CISA已知被利用漏洞清单

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

# 海康威视与罗克韦尔自动化高危漏洞纳入CISA已知被利用漏洞清单

阅读量**22747**

发布时间 : 2026-03-10 14:00:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全和基础设施安全局（CISA）于周四将**影响海康威视与罗克韦尔自动化产品的两处安全漏洞**纳入**已知被利用漏洞（KEV）清单**，并证实存在**在野主动利用行为**。

这两处**Critical 高危漏洞**分别如下：

**CVE-2017-7921（CVSS 评分：9.8）**

影响海康威视多款产品的**身份认证不当漏洞**，可使恶意攻击者实现**系统权限提升**并访问敏感信息。

**CVE-2021-22681（CVSS 评分：9.8）**

存在于罗克韦尔自动化多款产品（Studio 5000 Logix Designer、RSLogix 5000、Logix 控制器）中的**凭证保护不足漏洞**。拥有控制器网络访问权限的未授权攻击者可**绕过校验机制完成认证**，并篡改设备配置与应用代码。

在 **CVE-2017-7921** 被纳入 KEV 清单四个多月前，SANS 互联网风暴中心就已披露，监测到针对存在该漏洞的海康威视摄像头的**在野攻击尝试**。

但目前暂无公开报告显示 **CVE-2021-22681** 已被用于实际攻击。

依据**约束性运营指令（BOD 22-01）要求，鉴于漏洞已被主动利用，建议联邦行政部门机构在2026 年 3 月 26 日前**将相关软件升级至受支持的最新版本。

CISA 表示：**“此类漏洞是网络攻击者常用的攻击入口，对联邦机构构成重大安全风险。”**

“尽管 BOD 22-01 仅适用于联邦行政部门机构，但 CISA**强烈敦促所有组织**将 KEV 清单内漏洞的**及时修复**纳入漏洞管理流程，以降低遭受网络攻击的风险。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315077](/post/id/315077)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html)

如若转载,请注明出处： <https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1070**

* 粉丝
* **6**

### TA的文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [恶意浏览器插件针对imToken用户窃取私钥](/post/id/315065)

  2026-03-10 14:02:18

### 相关文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [恶意浏览器插件针对imToken用户窃取私钥](/post/id/315065)

  2026-03-10 14:02:18
* ##### [Viber即时通讯软件存在TLS漏洞，Cloak代理模式失效并导致用户暴露](/post/id/315068)

  2026-03-10 14:01:44
* ##### [黑客可利用间接提示注入攻击 借助外部内容操控AI智能体](/post/id/315071)

  2026-03-10 14:01:03

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