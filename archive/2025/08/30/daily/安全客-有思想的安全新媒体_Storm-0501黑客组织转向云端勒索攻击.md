---
title: Storm-0501黑客组织转向云端勒索攻击
url: https://www.anquanke.com/post/id/311721
source: 安全客-有思想的安全新媒体
date: 2025-08-30
fetch_date: 2025-10-07T00:17:56.260594
---

# Storm-0501黑客组织转向云端勒索攻击

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

# Storm-0501黑客组织转向云端勒索攻击

阅读量**69345**

发布时间 : 2025-08-29 16:04:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/storm-0501-hackers-shift-to-ransomware-attacks-in-the-cloud/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软近日警告称，一个名为 **Storm-0501** 的威胁组织正在改变其作案手法，从以往对本地设备的勒索加密，转向 **云端加密、数据窃取与勒索**。

不同于传统勒索软件依赖恶意加密程序，Storm-0501 现在直接 **利用云原生功能** 实现数据窃取、删除备份、销毁存储账户等目的，从而向受害者施压并进行敲诈，而无需部署任何传统勒索工具。

## 背景回顾

Storm-0501 至少自 2021 年起活跃，最初通过 **Sabbath 勒索软件**攻击全球组织。此后，该组织逐渐加入多个 **勒索即服务（RaaS）平台**，先后使用 Hive、BlackCat（ALPHV）、Hunters International、LockBit 以及近期的 Embargo 勒索软件。

2024 年 9 月，微软曾披露该组织将攻击范围延伸至 **混合云环境**，从入侵本地 Active Directory 转向针对 Entra ID 租户。在此类攻击中，他们或通过恶意联合域创建持久后门，或使用 Embargo 等勒索软件加密本地设备。

## 全新战术：云端勒索

在微软今日发布的最新报告中，Storm-0501 被发现已不再依赖本地设备加密，而是完全在云环境中展开攻击。

微软威胁情报团队指出：

> “与传统本地勒索不同，云端勒索意味着攻击者无需在终端部署恶意加密器，而是直接利用云原生功能来窃取数据、销毁备份并勒索受害者。这是一种根本性的战术转变。”

## 攻击链条

微软的调查揭示了 Storm-0501 的攻击步骤：

1. **初始突破**
   * 攻击者利用 **Microsoft Defender 部署中的缺口**，入侵多个 Active Directory 域与 Entra 租户。
   * 使用窃取的 **目录同步账户（DSA）** 配合 **AzureHound** 工具，枚举用户、角色和 Azure 资源。
2. **权限提升**
   * 攻击者发现一个 **未启用多因素认证（MFA）的全局管理员账户**，通过重置密码获得完全控制权。
   * 随后新增恶意联合域，以此冒充任意用户，绕过域内的 MFA 保护。
   * 进一步滥用 **Microsoft.Authorization/elevateAccess/action**，将自己加入 **Owner 角色**，完全接管受害组织的 Azure 环境。
3. **破坏与加密**
   * 禁用安全防护，窃取 Azure Storage 中的敏感数据。
   * 尝试删除存储快照、恢复点、恢复服务保管库以及存储账户，阻止受害者免费恢复数据。
   * 在无法直接删除数据时，创建新的 **Key Vault 与自定义密钥**，对数据进行再次加密，受害者必须支付赎金才能重新访问。
4. **勒索阶段**
   * 在数据窃取与破坏完成后，攻击者通过 **被攻陷的 Microsoft Teams 账户**联系受害者，直接递送勒索信息。

## 趋势与启示

微软提醒，随着传统勒索加密器在终端层面越来越容易被拦截，其他威胁组织可能会仿效 Storm-0501，转向 **更隐蔽、更难检测的云端勒索与数据窃取手法**。

微软报告中还提供了防护建议、Microsoft Defender XDR 检测规则以及狩猎查询，以帮助组织识别与拦截相关攻击战术。

这种 **“无恶意软件化” 的云端勒索模式** 标志着勒索攻击的又一次进化：它跳过了传统加密工具，直接利用云自身的功能实现控制与勒索。对于企业而言，如何加强云环境的身份安全与备份防护，将是未来防御的关键。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/storm-0501-hackers-shift-to-ransomware-attacks-in-the-cloud/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311721](/post/id/311721)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/storm-0501-hackers-shift-to-ransomware-attacks-in-the-cloud/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/storm-0501-hackers-shift-to-ransomware-attacks-in-the-cloud/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* [背景回顾](#h2-0)
* [全新战术：云端勒索](#h2-1)
* [攻击链条](#h2-2)
* [趋势与启示](#h2-3)

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