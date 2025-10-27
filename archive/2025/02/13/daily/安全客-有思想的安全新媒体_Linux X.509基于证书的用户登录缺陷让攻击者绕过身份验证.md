---
title: Linux X.509基于证书的用户登录缺陷让攻击者绕过身份验证
url: https://www.anquanke.com/post/id/304207
source: 安全客-有思想的安全新媒体
date: 2025-02-13
fetch_date: 2025-10-06T20:34:11.354908
---

# Linux X.509基于证书的用户登录缺陷让攻击者绕过身份验证

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

# Linux X.509基于证书的用户登录缺陷让攻击者绕过身份验证

阅读量**66974**

发布时间 : 2025-02-12 14:58:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/linux-x-509-certificate-based-user-login-flaws/>

译文仅供参考，具体内容表达以及含义原文为准。

在 PAM-PKCS#11 模块中发现了三个严重漏洞，该模块是一款广泛使用的 Linux-PAM 登录模块，用于实现基于 X.509 证书的用户身份认证。

这些漏洞的编号分别为 CVE-2025-24032、CVE-2025-24531 和 CVE-2025-24031。它们带来了极大的风险，因为攻击者可借此绕过身份认证机制，进而可能导致未经授权的访问以及系统中断。

CVE-2025-24032—— 通过令牌劫持绕过身份认证 第一个漏洞 CVE-2025-24032 影响 0.6.13 版本之前的 PAM-PKCS#11。在这种情况下，如果证书策略（cert\_policy）设置为 “无”（none，这是默认设置），该模块只会验证用户能否登录令牌，而不会检查私钥的签名。

这一缺陷使得攻击者能够利用用户的公钥证书和已知的个人识别码（PIN）创建一个令牌，从而无需私钥即可以该用户身份登录。

由于存在导致未经授权访问的潜在风险，该漏洞被归类为高严重级别。修复方法是升级到 0.6.13 或更高版本，在这些版本中，默认行为已更改为需要进行签名检查。

CVE-2025-24531—— 在错误情况下绕过身份认证 第二个问题 CVE-2025-24531 是在 PAM-PKCS#11 的 0.6.12 版本中引入的，并在 0.6.13 版本中得到修复。该漏洞使得在错误情况下能够绕过身份认证，尤其是在内存分配失败或权限更改不正确时。

该模块会返回 “PAM\_IGNORE”（忽略），如果启用了 “nouserok” 选项，这可能会导致身份认证被绕过，使攻击者无需经过适当验证即可登录。

CVE-2025-24031—— 输入 PIN 时发生段错误 最后，CVE-2025-24031 影响 0.6.12 及更早版本，在这些版本中，如果用户取消 PIN 输入过程（通过按下 ctrl-c 或 ctrl-d），该模块就会发生段错误。这会导致系统崩溃，进而造成拒绝服务，影响系统的可用性。建议的缓解措施是更新到 0.6.13 或更高版本，该版本包含针对此问题的补丁。

缓解措施与建议 为了缓解这些漏洞带来的影响，强烈建议用户采取以下措施：

1.升级到 PAM-PKCS#11 的 6.13 或更高版本，以修复所有这三个漏洞。

2.在conf 中配置 “cert\_policy = signature;”，作为针对 CVE-2025-24032 的临时解决办法。

3.如果受影响的服务因 CVE-2025-24031 而崩溃，需对其进行监控并重新启动。

4.实施额外的访问控制措施，并对用户进行教育，使其了解取消 PIN 输入的风险。

这些漏洞凸显了在 Linux 环境中定期更新和仔细配置身份认证模块的重要性，这样做可以防止未经授权的访问，并确保系统的完整性。

用户和系统管理员应立即采取行动，保护他们的系统免受这些潜在威胁的侵害。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/linux-x-509-certificate-based-user-login-flaws/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304207](/post/id/304207)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/linux-x-509-certificate-based-user-login-flaws/)

如若转载,请注明出处： <https://cybersecuritynews.com/linux-x-509-certificate-based-user-login-flaws/>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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