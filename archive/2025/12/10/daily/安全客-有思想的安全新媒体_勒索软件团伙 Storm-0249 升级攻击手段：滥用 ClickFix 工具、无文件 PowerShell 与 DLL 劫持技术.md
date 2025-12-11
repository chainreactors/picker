---
title: 勒索软件团伙 Storm-0249 升级攻击手段：滥用 ClickFix 工具、无文件 PowerShell 与 DLL 劫持技术
url: https://www.anquanke.com/post/id/313647
source: 安全客-有思想的安全新媒体
date: 2025-12-10
fetch_date: 2025-12-11T03:22:48.966771
---

# 勒索软件团伙 Storm-0249 升级攻击手段：滥用 ClickFix 工具、无文件 PowerShell 与 DLL 劫持技术

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

# 勒索软件团伙 Storm-0249 升级攻击手段：滥用 ClickFix 工具、无文件 PowerShell 与 DLL 劫持技术

阅读量**18108**

发布时间 : 2025-12-10 17:36:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/12/storm-0249-escalates-ransomware-attacks.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

知名威胁行为体 **Storm-0249** 正从 “初始访问中介” 角色转型，开始整合**域名欺骗、DLL 劫持、无文件 PowerShell 执行**等更高级攻击战术，以协助实施勒索软件攻击。

“这些手段使其能够绕过防御系统、渗透网络、维持持久控制并隐蔽运作，给安全团队带来严重隐患，”ReliaQuest 在分享给《黑客新闻》（The Hacker News）的报告中表示。

Storm-0249 是微软为某初始访问中介分配的代号，该组织曾向勒索软件团伙、勒索攻击者（如 Storm-0501）等其他网络犯罪集团出售企业网络访问权限。微软于 **2024 年 9 月** 首次公开披露该组织的相关活动。

今年早些时候，微软还曝光了该威胁行为体发起的一场钓鱼攻击活动：攻击者以税务相关主题为诱饵，在美国报税季前夕针对美国用户实施攻击，植入 **Latrodectus 恶意软件**与 **BruteRatel C4（BRc4）后渗透框架**。

此类攻击的最终目标是获取多个企业网络的**持久访问权限**，并通过将这些权限出售给勒索软件团伙实现变现 —— 这为勒索软件集团提供了稳定的攻击目标来源，同时加速了勒索攻击的实施节奏。

ReliaQuest 的最新研究发现，Storm-0249 出现**战术转型**：该组织开始滥用臭名昭著的 **ClickFix 社会工程战术**，以 “解决技术问题” 为借口，诱骗目标用户通过 Windows 运行对话框（Run dialog）执行恶意命令。

在该攻击场景中，攻击者通过命令复制执行合法工具 **curl.exe**，从一个仿冒微软域名的链接（`sgcipl[.]com/us.microsoft.com/bdo/`）下载 PowerShell 脚本（虚假域名旨在获取受害者信任），并通过 PowerShell 以**无文件方式**执行该脚本。

这一操作会进一步触发恶意 MSI 安装包以 **SYSTEM 权限**运行，随后在用户的 AppData 文件夹中释放一个伪造的 SentinelOne 终端安全解决方案相关 DLL 文件（`SentinelAgentCore.dll`），同时植入合法的 `SentinelAgentWorker.exe` 可执行文件。

攻击者的核心意图是：当 `SentinelAgentWorker.exe` 进程启动时，通过**DLL 劫持**加载恶意 DLL，从而实现隐蔽运作。该恶意 DLL 随后会与**命令与控制（C2）服务器**建立加密通信。

研究还发现，Storm-0249 会利用 `reg.exe`、`findstr.exe` 等**合法 Windows 管理工具**，提取 MachineGuid 等唯一系统标识符，为后续勒索软件攻击奠定基础。这种**驻留内存（LotL）战术**，加之所有命令均通过受信任的 `SentinelAgentWorker.exe` 进程执行，使得攻击行为难以触发安全告警。

研究结果表明，Storm-0249 已从 “大规模钓鱼攻击” 转向 “精准攻击”—— 通过滥用已签名进程的信任度，进一步提升攻击的隐蔽性。

“这并非普通的侦察行为，而是在为勒索软件附属团伙做准备，”ReliaQuest 指出，“LockBit、ALPHV 等勒索软件集团会利用 MachineGuid 将加密密钥与受害者的单个系统绑定。”

“通过将加密密钥与 MachineGuid 关联，攻击者可确保：即便防御者获取了勒索软件样本或尝试逆向破解加密算法，若没有攻击者控制的密钥，也无法解密文件。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/12/storm-0249-escalates-ransomware-attacks.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313647](/post/id/313647)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/12/storm-0249-escalates-ransomware-attacks.html)

如若转载,请注明出处： <https://thehackernews.com/2025/12/storm-0249-escalates-ransomware-attacks.html>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **790**

* 粉丝
* **6**

### TA的文章

* ##### [LOLPROX 曝光隐蔽攻击路径，可助力实施隐秘的虚拟化管理程序（Hypervisor）攻击](/post/id/313652)

  2025-12-10 18:32:53
* ##### [KimJongRAT 利用武器化 .hta 文件攻击 Windows 用户，窃取登录凭据](/post/id/313655)

  2025-12-10 18:32:25
* ##### [新型多阶段 JS#SMUGGLER 恶意软件攻击通过投递 NetSupport RAT 实现系统完全控制](/post/id/313649)

  2025-12-10 18:31:50
* ##### [勒索软件团伙 Storm-0249 升级攻击手段：滥用 ClickFix 工具、无文件 PowerShell 与 DLL 劫持技术](/post/id/313647)

  2025-12-10 17:36:18
* ##### [Checkmarx 收购 Tromzo，强化 AI 安全自动化能力](/post/id/313645)

  2025-12-10 17:35:33

### 相关文章

* ##### [LOLPROX 曝光隐蔽攻击路径，可助力实施隐秘的虚拟化管理程序（Hypervisor）攻击](/post/id/313652)

  2025-12-10 18:32:53
* ##### [KimJongRAT 利用武器化 .hta 文件攻击 Windows 用户，窃取登录凭据](/post/id/313655)

  2025-12-10 18:32:25
* ##### [新型多阶段 JS#SMUGGLER 恶意软件攻击通过投递 NetSupport RAT 实现系统完全控制](/post/id/313649)

  2025-12-10 18:31:50
* ##### [Checkmarx 收购 Tromzo，强化 AI 安全自动化能力](/post/id/313645)

  2025-12-10 17:35:33
* ##### [高危 n8n 远程代码执行漏洞（CVE-2025-65964）可通过操纵 Git 节点配置实现远程代码执行](/post/id/313634)

  2025-12-10 17:35:08
* ##### [FortiOS、FortiWeb 及 FortiProxy 漏洞可导致攻击者绕过 FortiCloud 单点登录（SSO）认证](/post/id/313637)

  2025-12-10 17:33:59
* ##### [Stripe 推出 Tempo 支付区块链并开放公测，万事达卡、瑞银集团已正式接入](/post/id/313639)

  2025-12-10 17:32:42

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