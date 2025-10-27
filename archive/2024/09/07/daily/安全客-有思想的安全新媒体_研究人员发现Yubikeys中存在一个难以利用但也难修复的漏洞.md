---
title: 研究人员发现Yubikeys中存在一个难以利用但也难修复的漏洞
url: https://www.anquanke.com/post/id/299856
source: 安全客-有思想的安全新媒体
date: 2024-09-07
fetch_date: 2025-10-06T18:22:23.956327
---

# 研究人员发现Yubikeys中存在一个难以利用但也难修复的漏洞

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

# 研究人员发现Yubikeys中存在一个难以利用但也难修复的漏洞

阅读量**144016**

发布时间 : 2024-09-06 11:16:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kevin Poireault，文章来源：infosecurity magazine

原文地址：<https://www.infosecurity-magazine.com/news/researcher-vulnerability-yubikeys/>

译文仅供参考，具体内容表达以及含义原文为准。

Yubikeys 是使用最广泛的双因素身份验证 （2FA） 硬件工具之一，某些版本容易受到侧信道攻击。

NinjaLab 的安全专家兼联合创始人 Thomas Roche 发现 YubiKey 5 系列设备包含一个加密漏洞，当攻击者获得对它们的临时物理访问权限时，它们很容易被克隆。

虽然漏洞无法修复，但也很难被利用。

## 了解如何使用 Yubikey

Yubikeys 是由 Yubico 开发的基于 USB 的物理安全设备，在登录在线帐户时增加了一层额外的保护。它们通常用于 2FA，除了密码外，还需要物理设备才能访问您的帐户。

Yubikeys 被许多安全专家认为是多因素身份验证 （MFA） 最安全的硬件选项之一，特别是因为它们通常支持 Fast Identity Online 2 （FIDO2） 标准。

FIDO2 身份验证由 FIDO 联盟和万维网联盟 （W3C） 联合开发，基于公钥加密，比基于密码的身份验证更安全，并且更能抵抗网络钓鱼和其他攻击。

## 14 年未被注意到的侧信道漏洞

在执行他称为 EUCLEAK 的侧信道攻击时，Roche 在许多 YubiKey 产品使用的加密库中发现了一个漏洞，该漏洞允许他克隆这些设备。

侧信道攻击是一种入侵尝试，旨在利用设备或系统的物理特性来提取敏感信息。

研究人员指出，侧信道漏洞是最大的安全元件制造商之一英飞凌科技公司提供的库中的加密漏洞，14 年来一直没有引起注意，并进行了大约 80 次最高级别的通用标准认证评估。

研究人员在公布他的经历结果之前联系了 Yubiso。

## 受影响的 Yubikey 设备

在公开公告中，Yubico 承认了该漏洞，并指定受影响的设备是：

* YubiKey 5 系列5.7 之前的版本
* YubiKey 5 FIPS 系列 5.7 之前的版本
* YubiKey 5 CSPN 系列 5.7 之前的版本
* YubiKey Bio 系列 5.7.2 之前的版本
* 5.7 之前的 Security Keys 系列
* YubiHSM 2 2.4.0 之前的版本
* YubiHSM 2 FIPS 2.4.0 之前的版本

较新的版本不受影响。

## 复杂的 Yubikey 漏洞利用场景

主要制造商表示，该漏洞的严重性为“中等”。

这部分是因为它相对难以利用。罗氏使用价值 11,000 欧元的材料来执行 EUCLEAK 攻击，并可以物理访问该设备——这两个标准可能令人望而却步。

Roche 提供了一个典型的攻击场景，可以成功利用 Yubikey 漏洞：

1. 攻击者窃取了受 FIDO 保护的受害者应用程序帐户的登录名和密码（例如，通过网络钓鱼攻击）
2. 攻击者在有限的时间内对受害者的设备进行物理访问，而受害者没有注意到
3. 由于被盗受害者的登录名和密码（对于给定的应用程序帐户），攻击者在执行侧信道测量时，根据需要多次向设备发送身份验证请求
4. 攻击者悄悄地将 FIDO 设备归还给受害者
5. 攻击者对测量结果执行侧信道攻击，并成功提取链接到受害者应用程序账户的椭圆曲线数字签名算法 （ECDSA） 私钥
6. 攻击者可以在 FIDO 设备或受害者没有注意到的情况下登录受害者的应用程序帐户。换句话说，攻击者为受害者的应用程序账户创建了 FIDO 设备的克隆。只要合法用户不撤销其身份验证凭证，此克隆就会授予对应用程序账户的访问权限。

本文翻译自infosecurity magazine [原文链接](https://www.infosecurity-magazine.com/news/researcher-vulnerability-yubikeys/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299856](/post/id/299856)

安全KER - 有思想的安全新媒体

本文转载自: [infosecurity magazine](https://www.infosecurity-magazine.com/news/researcher-vulnerability-yubikeys/)

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/researcher-vulnerability-yubikeys/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

### 热门推荐

文章目录

* [了解如何使用 Yubikey](#h2-0)
* [14 年未被注意到的侧信道漏洞](#h2-1)
* [受影响的 Yubikey 设备](#h2-2)
* [复杂的 Yubikey 漏洞利用场景](#h2-3)

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