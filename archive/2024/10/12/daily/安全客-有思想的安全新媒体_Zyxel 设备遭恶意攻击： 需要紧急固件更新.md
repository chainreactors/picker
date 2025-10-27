---
title: Zyxel 设备遭恶意攻击： 需要紧急固件更新
url: https://www.anquanke.com/post/id/300733
source: 安全客-有思想的安全新媒体
date: 2024-10-12
fetch_date: 2025-10-06T18:51:46.708055
---

# Zyxel 设备遭恶意攻击： 需要紧急固件更新

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

# Zyxel 设备遭恶意攻击： 需要紧急固件更新

阅读量**61415**

发布时间 : 2024-10-11 10:23:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/zyxel-devices-targeted-by-malicious-actors-urgent-firmware-update-required/>

译文仅供参考，具体内容表达以及含义原文为准。

Zyxel EMEA 团队的安全研究员 Serhii Boiarynov 最近发布了一份安全公告，揭露了针对 Zyxel 安全设备的恶意活动。攻击者正在利用 ATP 和 USG FLEX 系列中先前已知的漏洞，通过 SSL VPN 通道窃取凭证和未经授权的访问。这种活动被追踪到运行过时固件版本的设备，特别是 ZLD V4.32 和 ZLD V5.38 之间的设备。

![Zyxel security]()

据报告称，攻击者使用的是之前窃取的尚未更新的凭证。这些凭证允许他们创建临时用户，如 “SUPPOR87 ”或 “SUPPOR817”，并修改安全策略以允许自己访问网络。“Boiarynov 指出：”根据我们的调查，威胁分子能够从以前的漏洞中窃取有效凭证……使他们现在能够创建具有临时用户的 SSL VPN 通道。

我们建议管理员注意设备可能受到攻击的几个迹象。这些迹象包括

来自可疑用户名的 SSL VPN 连接，如 “SUPPOR87 ”或 “SUPPOR817”。
来自未知 IP 地址的管理员登录，特别是那些来自非认可国家的 IP 地址。
未经授权更改安全策略，如开放从广域网到局域网的访问，或更改 NAT 规则以允许不受限制的流量
在更严重的情况下，攻击者甚至可能通过被破坏的 VPN 连接访问活动目录 (AD) 服务器，对关键文件进行加密。“报告警告说：”黑客利用 SSL VPN 连接访问 AD 服务器并加密文件。

Ezoic
为防范这些攻击，Zyxel 强烈建议将设备升级到最新的固件 5.39 版，并更改与管理员账户、用户账户和 VPN 设置相关的所有密码。“报告建议：”如果设备仍未升级，请将其升级到最新的固件 5.39。

此外，管理员应删除任何未知用户，强制注销可疑会话，并删除允许从广域网或 SSL VPN 区域进行广泛访问的防火墙规则。此外，还强烈建议实施双因素身份验证（2FA）和更改 SSL VPN 访问的默认端口。

Zyxel 团队强调遵循安全最佳实践的重要性。管理员应定期检查防火墙配置，确保默认情况下拒绝所有非信任连接。报告还强调了使用 GEO IP Country 功能限制特定区域访问以及在配置文件中添加私人加密密钥的重要性。

由于恶意行为者不断利用未打补丁的漏洞，管理员在更新系统和实施这些建议时必须保持警惕。如果不解决这些问题，可能会导致未经授权的访问、数据加密和大范围的网络运行中断。

本文翻译自securityonline [原文链接](https://securityonline.info/zyxel-devices-targeted-by-malicious-actors-urgent-firmware-update-required/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300733](/post/id/300733)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/zyxel-devices-targeted-by-malicious-actors-urgent-firmware-update-required/)

如若转载,请注明出处： <https://securityonline.info/zyxel-devices-targeted-by-malicious-actors-urgent-firmware-update-required/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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