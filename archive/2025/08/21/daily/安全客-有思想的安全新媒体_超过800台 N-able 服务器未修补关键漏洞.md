---
title: 超过800台 N-able 服务器未修补关键漏洞
url: https://www.anquanke.com/post/id/311378
source: 安全客-有思想的安全新媒体
date: 2025-08-21
fetch_date: 2025-10-07T00:47:42.696607
---

# 超过800台 N-able 服务器未修补关键漏洞

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

# 超过800台 N-able 服务器未修补关键漏洞

阅读量**56896**

发布时间 : 2025-08-20 17:51:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/over-800-n-able-servers-left-unpatched-against-critical-flaws/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

超过800台 N-able N-central 服务器仍未修补两项关键安全漏洞，这些漏洞在上周已被证实遭到积极利用。

N-central 是一款广泛使用的平台，被众多托管服务提供商（MSPs）和 IT 部门用于通过集中式 Web 控制台监控和管理网络及设备。

这两个漏洞编号为 **CVE-2025-8875** 和 **CVE-2025-8876**。前者由于未正确清理用户输入，可能允许已认证的攻击者注入命令；后者则涉及不安全的反序列化弱点，攻击者可借此在未修补的设备上执行命令。

N-able 已在 **N-central 2025.3.1** 版本中修复了相关漏洞，并在周四告知 BleepingComputer，这些安全缺陷已遭到活跃利用，敦促管理员尽快加固服务器，以防止在漏洞细节披露前遭到进一步攻击。

N-able 在声明中表示：“我们的安全调查显示，在少量本地部署环境中发现了此类利用的证据，但在 N-able 托管的云环境中尚未发现相关迹象。您必须将本地部署的 N-central 升级至 2025.3.1。（根据我们的安全实践，漏洞详情将在修复版本发布后三周公布。）”

根据网络安全公益组织 **Shadowserver Foundation** 周五的监测结果，目前仍有 **880 台 N-central 服务器**暴露在可被利用的状态下，其中大多数位于美国、加拿大和荷兰。

![]()

“这些结果是通过对唯一 IP 地址进行计数后相加得出的，这意味着某些‘唯一’ IP 可能被重复统计。因此相关数据仅能作为参考，而非精确数值。”Shadowserver 表示。

根据 Shodan 的搜索结果，目前大约有 **2000 个 N-central 实例** 暴露在互联网上。

### 联邦机构被要求一周内完成修复

美国网络安全和基础设施安全局（CISA）已将这些漏洞加入其 **已知被利用漏洞目录（Known Exploited Vulnerabilities Catalog）**，并在 N-able 确认漏洞已遭滥用的前一天，就标记其已被用于零日攻击。

CISA 已命令所有联邦平民行政部门（FCEB）机构（包括国土安全部、财政部和能源部）必须在 **8 月 20 日之前**完成系统修补，此要求依据 2021 年 11 月发布的 **绑定性操作指令（BOD）22-01**。

虽然非政府组织并不在 BOD 22-01 的强制要求范围内，但 CISA 仍敦促所有网络防御人员尽快保护其系统，抵御正在进行的攻击。

CISA 表示：“请根据供应商的说明应用缓解措施，遵循 BOD 22-01 针对云服务的相关指导，若无可用缓解措施，应停止使用相关产品。此类漏洞是恶意网络行为者的常见攻击入口，对联邦企业构成重大风险。”

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/over-800-n-able-servers-left-unpatched-against-critical-flaws/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311378](/post/id/311378)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/over-800-n-able-servers-left-unpatched-against-critical-flaws/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/over-800-n-able-servers-left-unpatched-against-critical-flaws/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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