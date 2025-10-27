---
title: Prometei 僵尸网络不断演变： Linux变种卷土重来，有效载荷更加隐蔽，专注于开采门罗币
url: https://www.anquanke.com/post/id/308768
source: 安全客-有思想的安全新媒体
date: 2025-06-24
fetch_date: 2025-10-06T22:52:20.916658
---

# Prometei 僵尸网络不断演变： Linux变种卷土重来，有效载荷更加隐蔽，专注于开采门罗币

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

# Prometei 僵尸网络不断演变： Linux变种卷土重来，有效载荷更加隐蔽，专注于开采门罗币

阅读量**44088**

发布时间 : 2025-06-23 15:54:07

**x**

##### 译文声明

本文是翻译文章，文章来源：https://securityonline.info/prometei-botnet-evolves-linux-variant-returns-with-stealthier-payloads-and-monero-mining-focus/#google\_vignette

译文仅供参考，具体内容表达以及含义原文为准。

![]()

2025 年 3 月，Palo Alto Networks Unit 42 的研究人员发现了 Prometei 僵尸网络的卷土重来，这是一种复杂的模块化恶意软件系统，于 2020 年首次被发现。虽然历史上在 Windows 系统上很活跃，但最新一波重新引入了一种更隐蔽、功能更强大的 Linux 变体——专为门罗币加密货币挖掘、凭证盗窃和无声横向移动而设计。

Prometei 是指僵尸网络及其相关的恶意软件家族。自 2020 年 7 月以来，该僵尸网络一直活跃，已从简单的门罗币挖矿程序演变为具有高级持久性、利用和侦察功能的多阶段、跨平台威胁。

根据 [Unit 42](https://unit42.paloaltonetworks.com/prometei-botnet-2025-activity/)：

> “*这个恶意软件家族……允许攻击者远程控制受感染的系统进行加密货币挖掘（尤其是门罗币）和凭据盗窃*。

Prometei 的架构是模块化的，具有不同的组件负责特定任务，例如：

* 暴力破解管理员凭据
* 利用漏洞（例如 SMB 协议缺陷、EternalBlue）
* 挖掘 门罗币
* 窃取系统和用户凭据
* 通过域生成算法 （DGA） 与其 C2 基础设施通信

它的自我更新功能确保它可以逃避检测并快速适应防御变化：

> “*Prometei 使用 DGA 和自我更新功能来创建有弹性和自适应的恶意软件。”*

最新的示例（版本 3 和 4）与版本 2 （最后一次出现于 2021 年）有很大不同：

* 作为伪装成 k.php 的 UPX 打包的 ELF 可执行文件分发
* 使用附加到二进制文件的自定义 JSON 尾部进行配置
* 通过 ParentID、ParentHostname 和 ParentIp 值使用动态 C2 分配

有趣的是，由于故意混淆，恶意软件无法使用标准 UPX 工具解压缩：

> “恶意软件附加的*自定义配置 JSON 尾部会中断此过程……导致 UPX 工具错误地确定该文件不是有效的 UPX 存档*。

僵尸网络使用以下命令从受感染的 Linux 计算机中收集详细的系统信息：

* /proc/cpuinfo （CPU）
* dmidecode –type 底板（主板）
* uname -a （内核）
* 正常运行时间（系统寿命）

所有这些都通过 HTTP GET 泄露到 C2 服务器，网址为：

```
hxxp://152.36.128[.]18/cgi-bin/p.cgi
```

Prometei 样品通过以下方式分发：

```
hxxp[://]103.41.204[.]104/k.php?a=x86_64.
```

基础设施由位于印度尼西亚雅加达的 Infinys Network （ASN 58397） 托管。

尽管文件扩展名k.php，但有效负载不是 PHP 脚本，而是另一层欺骗。

> “*尽管该文件被命名为 k.php，但它并不是 PHP 脚本，可能是一种进一步掩盖其真实性质的策略*。”

Unit 42 的研究人员强调了分析最近 Prometei 样本的复杂性。在分析之前，恶意软件必须：

* 剥离 JSON 尾部
* 使用自定义方法解包
* 重新连接其原始拖车以进行执行测试

这个过程凸显了恶意软件日益复杂，将传统压缩与定制的反分析技术相结合。

虽然 Prometei 展示了类似 APT 的复杂性，但 Unit 42 没有发现与民族国家运作的联系。该僵尸网络仍然以经济动机为动机，主要专注于门罗币挖矿和可能出售收获的凭证。

> “*我们评估认为，Prometei 的运营似乎是由经济利益驱动的，没有证据表明与民族国家行为者有联系*。”

本文翻译自https://securityonline.info/prometei-botnet-evolves-linux-variant-returns-with-stealthier-payloads-and-monero-mining-focus/#google\_vignette 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308768](/post/id/308768)

安全KER - 有思想的安全新媒体

本文转载自: https://securityonline.info/prometei-botnet-evolves-linux-variant-returns-with-stealthier-payloads-and-monero-mining-focus/#google\_vignette

如若转载,请注明出处：

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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