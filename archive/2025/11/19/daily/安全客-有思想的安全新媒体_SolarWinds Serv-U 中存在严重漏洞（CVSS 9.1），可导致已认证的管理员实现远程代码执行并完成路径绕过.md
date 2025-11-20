---
title: SolarWinds Serv-U 中存在严重漏洞（CVSS 9.1），可导致已认证的管理员实现远程代码执行并完成路径绕过
url: https://www.anquanke.com/post/id/313245
source: 安全客-有思想的安全新媒体
date: 2025-11-19
fetch_date: 2025-11-20T03:08:29.582092
---

# SolarWinds Serv-U 中存在严重漏洞（CVSS 9.1），可导致已认证的管理员实现远程代码执行并完成路径绕过

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

# SolarWinds Serv-U 中存在严重漏洞（CVSS 9.1），可导致已认证的管理员实现远程代码执行并完成路径绕过

阅读量**15305**

发布时间 : 2025-11-19 17:37:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/critical-solarwinds-serv-u-flaws-cvss-9-1-allow-authenticated-admin-rce-and-path-bypass/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

SolarWinds 已发布安全更新，修复其文件传输管理和 FTP 服务器平台 **Serv-U** 中的三个严重漏洞。每个漏洞的 CVSS 评分均为 **9.1**，经认证的管理员滥用这些漏洞时可实现**远程代码执行（RCE）**。这三个漏洞均影响 **15.5.3 版本之前的 Serv-U**，SolarWinds 强烈敦促客户立即更新。

第一个漏洞 **CVE-2025-40547** 源于逻辑错误，攻击者在 Serv-U 中获得管理员权限后可触发该漏洞。

公告解释核心问题：“Serv-U 存在逻辑错误漏洞……可能使拥有管理员权限的恶意行为者获得代码执行能力。”

尽管该漏洞被评为严重（CVSS 9.1），但 SolarWinds 指出，由于典型的权限分离，Windows 环境中的风险较低：“在 Windows 部署中，风险被评为中等，因为服务默认情况下通常在权限较低的服务账户下运行。”

第二个漏洞 **CVE-2025-40548** 涉及 Serv-U 授权逻辑中缺失的验证。

SolarWinds 写道：“Serv-U 中存在缺失的验证流程，被滥用时可能使拥有管理员权限的恶意行为者获得代码执行能力。”

与前一个问题类似，攻击者必须已拥有管理员权限，但一旦获得权限，他们便可利用该漏洞在服务器上执行任意代码。

第三个漏洞 **CVE-2025-40549** 允许攻击者绕过目录路径限制，并在未授权目录中执行代码。

SolarWinds 警告：“Serv-U 存在路径限制绕过漏洞，被滥用时可能使拥有管理员权限的恶意行为者获得在目录上执行代码的能力。”

其严重性评分仍为严重（9.1），但由于操作系统级别的路径处理差异，Windows 系统的影响再次降低：“在 Windows 系统上，由于路径和主目录的处理方式不同，该漏洞的风险被评为中等。”

SolarWinds 感谢研究员 **Maurice Moss** 报告了此漏洞。

使用 Serv-U FTP Server 或 Serv-U Managed File Transfer Server 的组织如果尚未升级到 **15.5.3 版本**，则会受到影响。

SolarWinds 建议客户立即升级，并指出 Serv-U 15.5.3 已完全修复这三个漏洞。旧版本仍然存在漏洞，应尽快停用或更新。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-solarwinds-serv-u-flaws-cvss-9-1-allow-authenticated-admin-rce-and-path-bypass/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313245](/post/id/313245)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-solarwinds-serv-u-flaws-cvss-9-1-allow-authenticated-admin-rce-and-path-bypass/)

如若转载,请注明出处： <https://securityonline.info/critical-solarwinds-serv-u-flaws-cvss-9-1-allow-authenticated-admin-rce-and-path-bypass/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **706**

* 粉丝
* **6**

### TA的文章

* ##### [SnowSoul勒索软件样本分析：加密机制与解密研究](/post/id/313279)

  2025-11-19 21:35:35
* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10

### 相关文章

* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10
* ##### [macOS平台曝出“Nova”钱包窃取程序：通过替换Ledger/Trezor应用为钓鱼克隆版来窃取用户助记词](/post/id/313255)

  2025-11-19 17:39:45
* ##### [新型.NET加载器“隐匿窃密者”通过高级隐写术将LokiBot窃密木马植入BMP/PNG图片](/post/id/313252)

  2025-11-19 17:38:46
* ##### [npm供应链攻击预警：黑客利用Adspect伪装技术与虚假加密货币验证码同时欺骗用户与安全研究人员](/post/id/313249)

  2025-11-19 17:37:58

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