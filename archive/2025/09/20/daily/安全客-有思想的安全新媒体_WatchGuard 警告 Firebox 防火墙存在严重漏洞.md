---
title: WatchGuard 警告 Firebox 防火墙存在严重漏洞
url: https://www.anquanke.com/post/id/312257
source: 安全客-有思想的安全新媒体
date: 2025-09-20
fetch_date: 2025-10-02T20:24:30.548855
---

# WatchGuard 警告 Firebox 防火墙存在严重漏洞

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

# WatchGuard 警告 Firebox 防火墙存在严重漏洞

阅读量**69026**

发布时间 : 2025-09-19 18:41:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/watchguard-warns-of-critical-vulnerability-in-firebox-firewalls/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

WatchGuard 已发布安全更新，以修复影响该公司 Firebox 防火墙的远程代码执行漏洞。

该漏洞编号为 **CVE-2025-9242**，属于\*\*越界写入（Out-of-bounds Write）\*\*弱点，攻击者成功利用后，可在受影响的设备上远程执行恶意代码。

CVE-2025-9242 影响运行 **Fireware OS 11.x（已停止支持）、12.x 和 2025.1** 的防火墙，官方已在以下版本中修复：**12.3.1\_Update3 (B722811)、12.5.13、12.11.4 和 2025.1.1**。

虽然 Firebox 防火墙仅在配置了 **IKEv2 VPN** 时才容易受到攻击，但 WatchGuard 补充警告，即使已删除存在漏洞的配置，如果设备仍配置了到静态网关对等体（static gateway peer）的分支办公室 VPN（BOVPN），仍有被入侵的风险。

该公司在周三发布的公告中指出：

> “Fireware OS 中 iked 进程的越界写入漏洞，可能允许远程的未认证攻击者执行任意代码。该漏洞会影响使用 IKEv2 协议的移动用户 VPN，以及配置了动态网关对等体（dynamic gateway peer）的分支办公室 VPN。”
>
> “如果 Firebox 之前配置过基于 IKEv2 的移动用户 VPN，或基于动态网关对等体的分支办公室 VPN，即使后来删除了这些配置，只要设备仍配置了到静态网关对等体的分支办公室 VPN，仍可能存在漏洞风险。”

**受影响的防火墙产品分支：**

| 产品分支 | 受影响的防火墙型号 |
| --- | --- |
| Fireware OS 12.5.x | T15, T35 |
| Fireware OS 12.x | T20, T25, T40, T45, T55, T70, T80, T85, M270, M290, M370, M390, M470, M570, M590, M670, M690, M440, M4600, M4800, M5600, M5800, Firebox Cloud, Firebox NV5, FireboxV |
| Fireware OS 2025.1.x | T115-W, T125, T125-W, T145, T145-W, T185 |

对于暂时无法立即打补丁、且运行存在漏洞软件并配置了 **BOVPN 静态网关对等体** 的设备，WatchGuard 提供了临时缓解措施。

管理员需要：

* 禁用动态对等体 BOVPN，
* 添加新的防火墙策略，
* 禁用默认的 VPN 流量系统策略。

具体步骤已在官方支持文档中给出，指导管理员如何保护使用 IPSec 和 IKEv2 的 BOVPN。

目前尚无证据表明该严重漏洞已被利用，但 WatchGuard 建议管理员尽快为 Firebox 设备打补丁。防火墙一向是黑客的重点攻击目标。例如，**Akira 勒索软件团伙**正积极利用 **CVE-2024-40766**（一年前披露的高危漏洞）来入侵 SonicWall 防火墙。

早在 **2022 年 4 月**，美国网络安全和基础设施安全局（CISA）也曾要求联邦政府民用机构修补一个已被广泛利用的漏洞，该漏洞影响 WatchGuard Firebox 和 XTM 防火墙设备。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/watchguard-warns-of-critical-vulnerability-in-firebox-firewalls/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312257](/post/id/312257)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/watchguard-warns-of-critical-vulnerability-in-firebox-firewalls/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/watchguard-warns-of-critical-vulnerability-in-firebox-firewalls/>

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