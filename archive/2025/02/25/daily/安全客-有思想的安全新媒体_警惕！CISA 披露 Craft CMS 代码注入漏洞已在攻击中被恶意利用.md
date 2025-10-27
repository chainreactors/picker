---
title: 警惕！CISA 披露 Craft CMS 代码注入漏洞已在攻击中被恶意利用
url: https://www.anquanke.com/post/id/304684
source: 安全客-有思想的安全新媒体
date: 2025-02-25
fetch_date: 2025-10-06T20:34:18.501684
---

# 警惕！CISA 披露 Craft CMS 代码注入漏洞已在攻击中被恶意利用

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

# 警惕！CISA 披露 Craft CMS 代码注入漏洞已在攻击中被恶意利用

阅读量**83935**

发布时间 : 2025-02-24 10:40:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cisa-flags-craft-cms-code-injection-flaw-as-exploited-in-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![Craft CMS]()

美国网络安全与基础设施安全局（CISA）警告称，Craft CMS 存在的一个远程代码执行漏洞正被用于攻击。

该漏洞编号为 CVE – 2025 – 23209，严重程度为高危（CVSS v3 评分：8.0），是一个代码注入（RCE）漏洞，影响 Craft CMS 4 和 5 版本。

Craft CMS 是一种用于构建网站和定制数字化体验的内容管理系统（CMS）。

目前关于 CVE – 2025 – 23209 的技术细节披露不多，但利用该漏洞进行攻击并不容易，因为这需要先获取已安装系统的安全密钥。

在 Craft CMS 中，安全密钥是一种加密密钥，用于保护用户身份验证令牌、会话 cookie、数据库值以及敏感的应用程序数据。

只有在攻击者已经获取了这个安全密钥的情况下，CVE – 2025 – 23209 漏洞才会引发问题，这会为攻击者解密敏感数据、生成伪造的身份验证令牌，或远程注入和执行恶意代码打开方便之门。

CISA 已将该漏洞列入已知被利用漏洞（KEV）清单，但并未透露有关攻击范围、来源以及攻击目标的任何信息。

联邦机构需在 2025 年 3 月 13 日前修复 Craft CMS 的这个漏洞。

该漏洞已在 Craft 5.5.8 和 4.13.8 版本中得到修复，因此建议用户尽快升级到这些版本或更新的版本。

如果怀疑系统已被入侵，建议删除 “.env” 文件中包含的旧密钥，并使用命令生成新密钥。请注意，更改密钥会使任何用先前密钥加密的数据无法访问。

除了 CVE – 2025 – 23209，CISA 还将Palo Alto Networks防火墙中的一个漏洞（CVE – 2025 – 0111）列入了已知被利用漏洞目录，并设定了同样的截止日期 ——3 月 13 日。

这是一个影响 PAN – OS 防火墙的文件读取漏洞，据供应商披露，黑客将其作为利用 CVE – 2025 – 0108 和 CVE – 2024 – 9474 的攻击链的一部分加以利用。

对于修复了该漏洞的 PAN – OS 版本，受影响的用户可以查看Palo Alto Networks的安全公告。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cisa-flags-craft-cms-code-injection-flaw-as-exploited-in-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304684](/post/id/304684)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cisa-flags-craft-cms-code-injection-flaw-as-exploited-in-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cisa-flags-craft-cms-code-injection-flaw-as-exploited-in-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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