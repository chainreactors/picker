---
title: SonicWall SMA设备遭“OVERSTEP” rootkit入侵，疑与勒索软件攻击相关
url: https://www.anquanke.com/post/id/310256
source: 安全客-有思想的安全新媒体
date: 2025-07-19
fetch_date: 2025-10-06T23:39:08.162460
---

# SonicWall SMA设备遭“OVERSTEP” rootkit入侵，疑与勒索软件攻击相关

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

# SonicWall SMA设备遭“OVERSTEP” rootkit入侵，疑与勒索软件攻击相关

阅读量**76566**

发布时间 : 2025-07-18 17:30:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ionut Ilascu，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/sonicwall-sma-devices-hacked-with-overstep-rootkit-tied-to-ransomware/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一名威胁行为者部署了一种此前未见的恶意软件“OVERSTEP”，该恶意软件能够修改已完全打好补丁但已停止支持的 SonicWall Secure Mobile Access（SMA）设备的启动流程。

该后门为用户态 rootkit，允许黑客隐藏恶意组件，保持设备的持久访问权限，并窃取敏感凭证。

谷歌威胁情报组（GTIG）研究人员在攻击中发现了该 rootkit，怀疑攻击可能利用了“一种未知的零日远程代码执行漏洞”。

该威胁行为者被追踪编号为 UNC6148，至少自去年十月起开始活动，最近一次攻击目标是在今年五月。

由于从受害者处窃取的文件随后被发布在 World Leaks（Hunters International 改名后的网站）数据泄露平台上，谷歌威胁情报组（GTIG）研究人员认为，UNC6148 从事数据窃取和勒索攻击，并可能部署名为 **Abyss** 勒索软件（GTIG 追踪代号为 VSOCIETY）。

### 黑客有备而来

黑客针对的是已停止支持（EoL）的 SonicWall SMA 100 系列设备，该设备用于为本地网络、云端或混合数据中心中的企业资源提供安全远程访问。

目前尚不清楚攻击者是如何获得初始访问权限的，但在调查 UNC6148 的攻击过程中，研究人员发现该威胁行为者已经掌握了目标设备的本地管理员凭据。

“谷歌威胁情报组（GTIG）高度确定，UNC6148 在目标 SMA 设备更新至最新固件版本（10.2.1.15-81sv）之前，利用了一个已知漏洞窃取了管理员凭据。”

通过分析网络流量元数据，研究人员发现证据表明，UNC6148 可能在今年一月就已窃取了目标设备的凭据。

攻击者可能利用了多个“n-day”漏洞**（CVE-2021-20038、CVE-2024-38475、CVE-2021-20035、CVE-2021-20039、CVE-2025-32819）**实施攻击，这些漏洞中最早的于 2021 年披露，最新的则是在 2025 年 5 月。

其中，攻击者可能利用了 **CVE-2024-38475** 漏洞，因为该漏洞可泄露“本地管理员凭据和可被 UNC6148 重用的有效会话令牌”。

不过，来自谷歌旗下的事件响应团队 Mandiant 表示，尚无法确认攻击者是否确实利用了该漏洞。

### 反向 Shell 之谜

在今年 6 月的一次攻击中，UNC6148 利用本地管理员凭据通过 SSL-VPN 会话连接至目标 SMA 100 系列设备。

尽管从设计上来说该类设备不应允许 Shell 访问，但攻击者仍成功发起了一个反向 Shell 会话。

SonicWall 产品安全事件响应团队（PSIRT）试图调查攻击者是如何实现这一行为的，但未能得出明确结论，其中一个可能的原因是攻击者利用了尚未公开的安全漏洞。

通过获得对设备的 Shell 访问权限，威胁行为者随后执行了侦察、文件操作，并导入了一组设置，其中包含新的网络访问控制策略规则，用以允许来自攻击者 IP 地址的连接请求。

### OVERSTEP Rootkit 不留痕迹

在获取设备控制权限后，**UNC6148** 通过一系列命令部署了名为 **OVERSTEP** 的 **Rootkit**，该恶意程序通过 **base64** 解码得到二进制文件，并作为 .ELF 文件植入设备系统。

“安装完成后，攻击者手动清除了系统日志并重启了设备，从而激活了 OVERSTEP 后门。”——谷歌威胁情报组

OVERSTEP 是一种后门程序，可建立反向 Shell 连接并从主机中窃取密码信息。同时，它还具备用户态 Rootkit 功能，能够隐藏自身组件，在受害设备中长期潜伏而不被发现。

Rootkit 组件赋予攻击者长期持久化能力，可在每次启动动态可执行文件时加载并执行恶意代码。

OVERSTEP 具备反取证功能，允许攻击者有选择性地删除日志条目，从而掩盖其入侵轨迹。正因如此，加之磁盘中缺乏命令执行记录，研究人员无法追踪攻击者在入侵成功后的具体行为。

不过，谷歌威胁情报组（GTIG）警告称，OVERSTEP 能窃取诸如 `persist.db` 数据库和证书文件等敏感信息，这些文件包含凭据、一次性密码（OTP）种子以及可用于维持持久访问的证书内容。

尽管研究人员目前尚无法明确 UNC6148 的攻击目的，但他们指出该组织的活动与多起部署 Abyss 勒索软件的安全事件存在“明显重合”。

2023 年底，Truesec 安全研究团队曾调查一起涉及 Abyss 勒索软件的事件。攻击者在一台 SMA 设备中部署 Web Shell，实施隐藏操作，并成功实现固件更新后仍保持访问权限的持久化。

几个月后的 2024 年 3 月，InfoGuard AG 事件响应专家 Stephan Berger 发表文章，描述了一起类似的 SMA 设备入侵事件，最终同样导致 Abyss 恶意软件被植入系统。

建议部署了 SMA 设备的组织立即检查其设备是否存在被入侵的风险，方法是获取设备的磁盘镜像，以避免受到 rootkit 的干扰。

谷歌威胁情报组（GTIG）已发布一系列入侵指标（Indicators of Compromise, IOCs），并提供了供安全分析人员参考的可疑行为特征，以帮助判断设备是否已遭黑客攻击。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/sonicwall-sma-devices-hacked-with-overstep-rootkit-tied-to-ransomware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310256](/post/id/310256)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/sonicwall-sma-devices-hacked-with-overstep-rootkit-tied-to-ransomware/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/sonicwall-sma-devices-hacked-with-overstep-rootkit-tied-to-ransomware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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