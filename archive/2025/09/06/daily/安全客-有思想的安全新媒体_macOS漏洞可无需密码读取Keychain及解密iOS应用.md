---
title: macOS漏洞可无需密码读取Keychain及解密iOS应用
url: https://www.anquanke.com/post/id/311929
source: 安全客-有思想的安全新媒体
date: 2025-09-06
fetch_date: 2025-10-02T19:43:04.363259
---

# macOS漏洞可无需密码读取Keychain及解密iOS应用

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

# macOS漏洞可无需密码读取Keychain及解密iOS应用

阅读量**397353**

发布时间 : 2025-09-05 18:18:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mirko Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2025/09/04/macos-gcore-vulnerability-cve-2025-24204/>

译文仅供参考，具体内容表达以及含义原文为准。

在今天的 Nullcon Berlin 大会上，一名研究员披露了一个严重的 macOS 漏洞（CVE-2025-24204），该漏洞允许攻击者在 **系统完整性保护（SIP）** 启用的情况下，读取任意进程的内存，进而实现无需密码即可解密 **Keychain** 和 **iOS 应用**。

问题源自 Apple 在 macOS 15.0（Sequoia）中误将 **/usr/bin/gcore** 工具赋予了 **com.apple.system-task-ports.read** 权限。这一权限让 gcore 获得了读取系统中任意进程内存的能力，而 Apple 已在 macOS 15.3 中移除了该权限。

![]()

本次漏洞由 FFRI Security 的研究员 **Koh M. Nakagawa** 发现。他指出，这一配置错误打破了关键的安全边界，使得敏感用户数据暴露在风险之中，包括 **钥匙串内容**、受 **透明度、同意与控制（TCC）** 机制保护的数据，甚至是 **加密的 iOS 应用程序二进制文件**。

Nakagawa 在接受 Help Net Security 采访时透露，自己是在一个意料之外的场景中发现该漏洞的：“当微软发布 Mac 版 ProcDump 工具时，我最初觉得它没什么用，因为在 SIP 启用的情况下，它本不可能转储大多数进程的内存。我认为这工具只在关闭 SIP 时才有效。但当我下载并尝试后，意外发现它竟然能转储进程内存，包括系统进程，即便 SIP 仍然开启。这让我非常震惊。深入分析后，我发现 ProcDump-for-Mac 内部调用了 gcore，而 gcore 被赋予了特殊权限。很可能微软也注意到了 gcore 新增的这一权限，所以才会开发并发布该工具，但他们似乎并未意识到这是一个漏洞。”

**gcore 本是 macOS 提供的合法调试工具**，用于生成正在运行的进程核心转储。按理说，它不应在没有特定条件的情况下读取受保护的内存区域。然而，随着新增权限的引入，gcore 能够转储包括加密与凭证管理进程在内的任意内存。Nakagawa 演示了其影响：

**1.**他可以转储 **securityd** 进程（负责管理登录钥匙串），并在转储文件中搜索到用于加密钥匙串文件的主密钥（Master Key）。一旦获得该密钥，攻击者便能在无需用户密码的情况下解密登录钥匙串。

**2.**他展示了绕过 **TCC 机制** 的方法。受沙箱保护的应用（如 Preview 打开的 PDF、通讯录中的联系人数据）虽然受限于文件访问权限，但其加载的内容仍会驻留在内存中。通过转储这些应用的内存并借助 vmmap 工具进行分析，即可还原受保护文件的内容。

**3.**他还发现了漏洞对 **FairPlay 加密 iOS 应用** 的影响。Apple Silicon Mac 能直接运行 iOS 应用，但其二进制文件在磁盘上依旧保持加密。利用 gcore 在应用运行时转储内存，Nakagawa 能够提取出已解密的应用程序二进制文件，而无需越狱设备。

Apple 已在 macOS 15.3 中移除了 gcore 的相关权限。针对检测方面，可以借助 Apple 的 **终端安全框架（ESF）**，通过监控 `get_task_read` 事件来发现 gcore 对敏感进程调用 `task_read_for_pid` 的行为，从而标记潜在的利用企图。但对于企业防御者而言，Nakagawa 并不认为有必要大规模监控系统二进制权限的变动：“即便发现问题，除了等待 Apple 的系统更新，几乎没有什么可以做。”

这一事件再次凸显了 **错误配置权限的严重风险**。一个合法的调试工具，如果被赋予了过高的权限，也可能演变成严重的安全隐患。Nakagawa 强调，这并非个例：“我认为类似的漏洞极有可能存在。我的研究表明，Apple 在为系统二进制文件授予强权限时，并未进行充分的安全审查。事实上，在另一个系统组件中，Apple 也曾在随后的更新中移除了同样的 com.apple.system-task-ports.read 权限。这或许意味着与 gcore 类似的漏洞此前也存在，只是后来被静默修复了。”

他补充道，识别这类问题更多依赖于安全研究者的努力：“我在分享的演讲中展示了一个方法，可以在每次系统更新后运行 `ipsw diff` 命令，来对比权限变化。”

Nakagawa 的研究也提醒我们，**部分权限提升**（如只读内存访问）同样具有极大破坏力。攻击者不需要写权限或完全控制，就能窃取关键数据。更重要的是，本次事件证明了 **SIP、TCC 等安全边界的有效性取决于其严格执行**，一旦出现纰漏，整个系统的攻击面便会急剧扩大。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2025/09/04/macos-gcore-vulnerability-cve-2025-24204/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311929](/post/id/311929)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2025/09/04/macos-gcore-vulnerability-cve-2025-24204/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2025/09/04/macos-gcore-vulnerability-cve-2025-24204/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

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