---
title: pac4j-jwt 曝出10.0分高危漏洞 攻击者可伪造管理员令牌
url: https://www.anquanke.com/post/id/315020
source: 安全客-有思想的安全新媒体
date: 2026-03-06
fetch_date: 2026-03-07T03:54:53.820965
---

# pac4j-jwt 曝出10.0分高危漏洞 攻击者可伪造管理员令牌

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

# pac4j-jwt 曝出10.0分高危漏洞 攻击者可伪造管理员令牌

阅读量**21567**

发布时间 : 2026-03-06 10:50:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/critical-10-0-cvss-flaw-in-pac4j-jwt-lets-hackers-forge-admin-tokens/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员在一款主流 Java 安全库 **pac4j-jwt** 中发现一处**高危漏洞**。该库基于 JSON Web Token（JWT）为成千上万的应用提供身份认证与安全保护。

该漏洞编号为 **CVE-2026-29000**，CVSS 评分达到**满分 10.0**，属于**Critical 高危漏洞**。只要攻击者获取到服务器的 RSA 公钥，即可**远程伪造管理员身份凭证**。

---

该漏洞由 **CodeAnt AI 安全研究团队**发现，存在于库中 **JwtAuthenticator** 组件对加密令牌（JWE）的处理逻辑中。

标准 JWT 安全机制依赖签名（JWS）验证令牌完整性，而许多企业系统同时会使用加密（JWE）隐藏令牌内容。**pac4j-jwt 的漏洞正是出在这两种机制的结合处**。

### JWE 封装明文 JWT 攻击手法

攻击者可构造一个**无签名的 PlainJWT**，并用服务器公钥将其封装进 JWE 加密容器中。

### 核心逻辑缺陷

服务器解密令牌后，库内的 `toSignedJWT()` 函数会因内部令牌未签名而正确返回 `null`。但后续的签名校验模块仅通过简单的 `null` 判断就被**直接跳过**。

### 静默认证绕过

库会直接使用令牌中**未经验证**的声明信息创建用户档案，相当于将伪造的 PlainJWT 视为可信身份。

攻击者只需在令牌中随意指定 `subject`（用户）和 `role`（角色）字段，**无需知晓服务器私钥**，就能冒充任意用户包括系统管理员，进而导致：

* **系统完全沦陷**：获取管理员后台与敏感数据的全部权限
* **横向渗透**：利用劫持凭证深入企业内网

---

pac4j 维护者 **Jérôme Leleu** 已确认漏洞，并在所有活跃版本分支中发布修复补丁。使用 pac4j-jwt 的机构应**立即优先升级**：

| 受影响分支 | 建议升级版本 |
| --- | --- |
| 4.x 系列 | 升级至 4.5.9 及以上 |
| 5.x 系列 | 升级至 5.7.9 及以上 |
| 6.x 系列 | 升级至 6.3.3 及以上 |

CodeAnt AI 安全研究团队已在官方博客发布完整技术分析与**可利用 PoC**，帮助安全团队理解并排查该漏洞。

安全专家建议：即便完成补丁修复，企业仍应检查 JWT 配置，**强制要求令牌必须携带签名**，避免出现本次漏洞中 “静默跳过校验” 的逻辑。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-10-0-cvss-flaw-in-pac4j-jwt-lets-hackers-forge-admin-tokens/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315020](/post/id/315020)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-10-0-cvss-flaw-in-pac4j-jwt-lets-hackers-forge-admin-tokens/)

如若转载,请注明出处： <https://securityonline.info/critical-10-0-cvss-flaw-in-pac4j-jwt-lets-hackers-forge-admin-tokens/>

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
* **1060**

* 粉丝
* **6**

### TA的文章

* ##### [Django发布安全补丁 修复拒绝服务与权限类漏洞](/post/id/315047)

  2026-03-06 10:56:33
* ##### [攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据](/post/id/315044)

  2026-03-06 10:54:37
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13

### 相关文章

* ##### [Django发布安全补丁 修复拒绝服务与权限类漏洞](/post/id/315047)

  2026-03-06 10:56:33
* ##### [攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据](/post/id/315044)

  2026-03-06 10:54:37
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13
* ##### [Coruna席卷全球威胁格局的高性能iOS漏洞利用工具包](/post/id/315032)

  2026-03-06 10:52:45
* ##### [Grammarly 从文字纠错转向文学模仿](/post/id/315029)

  2026-03-06 10:52:13

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