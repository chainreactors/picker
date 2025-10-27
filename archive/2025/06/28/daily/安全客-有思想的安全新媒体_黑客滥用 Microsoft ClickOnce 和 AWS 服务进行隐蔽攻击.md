---
title: 黑客滥用 Microsoft ClickOnce 和 AWS 服务进行隐蔽攻击
url: https://www.anquanke.com/post/id/309056
source: 安全客-有思想的安全新媒体
date: 2025-06-28
fetch_date: 2025-10-06T22:52:00.136120
---

# 黑客滥用 Microsoft ClickOnce 和 AWS 服务进行隐蔽攻击

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

# 黑客滥用 Microsoft ClickOnce 和 AWS 服务进行隐蔽攻击

阅读量**90617**

发布时间 : 2025-06-27 14:24:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ionut Ilascu，文章来源： bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/oneclik-attacks-use-microsoft-clickonce-and-aws-to-target-energy-sector/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一个被研究人员称为 OneClik 的复杂恶意活动一直在利用微软的 ClickOnce 软件部署工具和定制的 Golang 后门入侵能源、石油和天然气行业的组织。

黑客依靠合法的 AWS 云服务（AWS、Cloudfront、API Gateway、Lambda）来隐藏指挥和控制（C2）基础设施。

ClickOnce 是微软的一种部署技术，允许开发人员创建基于 Windows 的自更新应用程序，将用户交互降至最低。

网络安全公司 Trellix 的安全研究人员分析了该活动的三种变体（v1a、BPI-MDM 和 v1d），它们都通过 .基于 NET 的加载程序跟踪为 OneClikNet。

据他们介绍，OneClik 活动的每个版本都随着先进的策略和 C2 混淆、强大的反分析和沙盒规避技术而发展。

虽然运营指标指向与中国有关联的威胁行为者，但研究人员在进行归因时持谨慎态度。

**滥用 Microsoft 的 ClickOnce 部署工具**

OneClik 攻击将合法工具与自定义恶意软件以及云和企业工具相结合，使威胁行为者能够逃避对作的检测。

它从一封网络钓鱼电子邮件开始，其中包含指向 Azure 生态系统中托管的虚假硬件分析站点的链接，该站点提供伪装成合法工具的 .APPLICATION 文件（ClickOnce 清单）。

Trellix 研究人员表示，攻击者使用 ClickOnce 应用程序作为恶意负载的交付机制，而没有触发用户帐户控制机制。

“ClickOnce 应用程序在部署服务 （dfsvc.exe） 下启动，使攻击者能够通过此受信任的主机代理执行恶意负载。

由于 ClickOnce 应用程序以用户级权限运行（无需用户帐户控制），因此它们为旨在避免权限提升的威胁行为者提供了一种有吸引力的交付机制，“研究人员解释说。

![]()

```
OneClik 攻击中的感染链 来源：Trellix
```

在 OneClik 的情况下，这允许威胁行为者使用合法的 .NET 可执行文件（例如 *ZSATray.exe*、*umt.exe* 或 *ied.exe*）来加载正常依赖项以外的其他内容。

“加载程序就位后，有效负载执行在 *dfsvc.exe* 下进行，与良性的 ClickOnce 活动混合在一起，”Trellix 研究人员说。

为了将作隐藏更长时间，威胁行为者利用了合法的 AWS 服务，这使得 C2 通信与无害的 CDN 流量混合在一起，看起来就像正常的云使用一样。

在 OneClik v1a 变体中，信标联系了 Cloudfront 分发域和 API Gateway 终端节点。在 v1d 中，它使用 AWS Lambda 函数 URL 作为 HTTP 回调地址。

Trellix 研究人员澄清说：“通过’隐藏在云中’，攻击者利用了 AWS 的高信任和可用性：防御者必须解密 SSL 或将整个 AWS 域列入黑名单才能注意到此流量，这通常是不切实际的。

**基于 Go 的 RunnerBeacon 后门**

对基于 Golang 的 RunnerBeacon 后门的分析表明，其 C2 协议使用 RC4 流密码算法加密所有流量，并使用 MessagePack 序列化数据。

它具有具有多种消息类型的模块化消息协议，其中包括 BeaconData、FileRequest、CommandRequest、SOCKSRequest 和 FileUpload。

研究人员在后门用来阻碍分析的一些方法中发现了 “obfuscate\_and\_sleep” 例程和信标间隔中的随机 “抖动”。

研究人员还观察到允许威胁行为者执行以下作的高级命令：

* 执行 shell 命令 （CreateProcessW）
* Numerate 进程
* 运行文件作（目录列表、上传、下载）
* 执行与网络相关的任务 （端口扫描）
* 建立 SOCKS5 隧道以代理数据流量

其他 RunnerBeacon 功能包括高级作，如进程注入和为权限提升设置阶段。

Trellix 表示，RunnerBeacon 的设计类似于已知的基于 Go 的 Cobalt Strike 信标，例如 Geacon 系列中的信标。

由于命令集的相似性和跨协议 C2 的使用，他们表示“RunnerBeacon 可能是 Geacon 的进化分支或私人修改变体，专为更隐蔽和云友好的作量身定制”

**谨慎归因**

尽管最近发现了 OneClik 活动，但在 3 月初，2023 年 9 月在中东的一家石油和天然气行业的公司发现了 RunnerBeacon 装载机的变体。

无法确定交付方法，但变体的代码与 OneClik作中分析的模块几乎相同。

指向与中国有关联的国家行为者相关活动的线索包括在其他活动中发现的归因于中国威胁行为者的策略、技术和程序。

Trellix 强调，.NET AppDomainManager 注入技术已被用于归因于中国威胁行为者的多次网络攻击。用于部署加密负载的方法也是如此。

此外，之前与中国相关的活动表明，他们更喜欢使用阿里巴巴和亚马逊的服务进行基于云的暂存。

但是，这些重叠不足以将 OneClik 攻击归因于特定的威胁行为者。

Trellix 的报告包括 OneClik 活动中所有组件的入侵指标的完整列表，从网络钓鱼诱饵和恶意软件加载程序到配置文件、后门二进制文件、合法可执行文件、域和配置参数。

本文翻译自 bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/oneclik-attacks-use-microsoft-clickonce-and-aws-to-target-energy-sector/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309056](/post/id/309056)

安全KER - 有思想的安全新媒体

本文转载自:  [bleepingcomputer](https://www.bleepingcomputer.com/news/security/oneclik-attacks-use-microsoft-clickonce-and-aws-to-target-energy-sector/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/oneclik-attacks-use-microsoft-clickonce-and-aws-to-target-energy-sector/>

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

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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