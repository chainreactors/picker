---
title: SonicWall警告被木马入侵的NetExtender窃取VPN登录信息
url: https://www.anquanke.com/post/id/309026
source: 安全客-有思想的安全新媒体
date: 2025-06-27
fetch_date: 2025-10-06T22:50:05.639020
---

# SonicWall警告被木马入侵的NetExtender窃取VPN登录信息

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

# SonicWall警告被木马入侵的NetExtender窃取VPN登录信息

阅读量**66104**

发布时间 : 2025-06-26 14:04:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源： bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-trojanized-netextender-stealing-vpn-logins/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

SonicWall 警告客户，威胁行为者正在分发其 NetExtender SSL VPN 客户端的木马版本，用于窃取 VPN 凭据。

SonicWall 和 Microsoft 威胁情报 （MSTIC） 研究人员发现的假冒软件模仿了合法的 NetExtender v10.3.2.27，这是最新的可用版本。

恶意安装程序文件托管在一个欺骗性网站上，该网站看起来是真实的，诱使访问者认为他们正在从 SonicWall 下载软件。

虽然安装程序文件没有由 SonicWall 进行数字签名，但它由“CITYLIGHT MEDIA PRIVATE LIMITED”签名，使其能够绕过基本防御。

![]()

```
修改后文件上的数字 签名来源：SonicWall
```

木马应用程序的目标是窃取 VPN 配置和帐户凭据，并将其泄露给攻击者。

SonicWall NetExtender 是一个远程访问 VPN 客户端，允许用户从远程位置安全地连接到其组织的内部网络。

它专为与 SonicWall SSL VPN 设备和防火墙配合使用而设计，通常由中小型企业的远程员工、IT 管理员和各行各业的承包商使用。

SonicWall 和 Microsoft 发现了恶意欺骗网站分发的其产品的两个修改后的二进制文件。

修改后的 **NeService.exe** 的验证逻辑已修补以绕过数字证书检查，**NetExtender.exe**文件已被修改以窃取数据。

“添加了额外的代码，以通过端口 8080 将 VPN 配置信息发送到 IP 地址为 132.196.198.163 的远程服务器，”SonicWall 公告解释说。

“输入 VPN 配置详细信息并单击”连接“按钮后，恶意代码会在将数据发送到远程服务器之前执行自己的验证。被盗的配置信息包括用户名、密码、域等。

![]()

```
“NetExtender.exe”文件上的恶意代码 来源：SonicWall
```

该公司的安全工具和 Microsoft Defender 现在可以检测并阻止恶意安装程序，但其他安全工具可能无法。

通常，人们会被重定向到欺骗性网站，这些网站通过恶意广告、SEO 中毒、私信、论坛帖子以及 YouTube 或 TikTok 视频提供木马安装程序。

下载软件时，请使用供应商的官方网站并跳过所有推广的结果。此外，在设备上执行下载的文件之前，请始终在最新的 AV 上扫描它们。

本文翻译自 bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-trojanized-netextender-stealing-vpn-logins/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309026](/post/id/309026)

安全KER - 有思想的安全新媒体

本文转载自:  [bleepingcomputer](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-trojanized-netextender-stealing-vpn-logins/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-trojanized-netextender-stealing-vpn-logins/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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