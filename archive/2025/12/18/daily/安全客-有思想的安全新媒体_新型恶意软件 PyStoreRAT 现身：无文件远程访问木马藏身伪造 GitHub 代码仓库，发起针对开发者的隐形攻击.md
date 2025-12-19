---
title: 新型恶意软件 PyStoreRAT 现身：无文件远程访问木马藏身伪造 GitHub 代码仓库，发起针对开发者的隐形攻击
url: https://www.anquanke.com/post/id/313823
source: 安全客-有思想的安全新媒体
date: 2025-12-18
fetch_date: 2025-12-19T03:21:23.228830
---

# 新型恶意软件 PyStoreRAT 现身：无文件远程访问木马藏身伪造 GitHub 代码仓库，发起针对开发者的隐形攻击

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

# 新型恶意软件 PyStoreRAT 现身：无文件远程访问木马藏身伪造 GitHub 代码仓库，发起针对开发者的隐形攻击

阅读量**24981**

发布时间 : 2025-12-18 09:51:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/pystorerat-uncovered-fileless-rat-hides-in-fake-github-repos-to-launch-invisible-attacks-on-developers/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款技术复杂的新型威胁正潜伏在开源社区中，将开发者对 GitHub 代码仓库的信任变为攻击武器。莫菲赛克威胁实验室（Morphisec Threat Labs）发现了一款此前未被记录的远程访问木马（RAT）——**PyStoreRAT**，它藏身于看似无害的 Python 项目中，对受害设备发起隐形的无文件攻击。

该攻击活动自 2025 年年中起便处于活跃状态，攻击者通过打造精致却带有欺诈性质的软件工具，专门诱捕开发者与开源情报（OSINT）从业人员。

其攻击路径设计得阴险而简单。威胁攻击者在 GitHub 平台上大量投放伪装成实用工具的代码仓库，例如 “Spyder 开源情报工具”“HacxGPT”“漏洞监控程序” 等。这些仓库往往配有人工智能生成的图片与专业文档，以此伪装成合法项目。但实际上，这些项目的功能完全是虚假的表象。

研究人员指出：“这些伪装成开发工具或开源情报工具的代码仓库，仅包含寥寥数行代码，其作用是在后台静默下载远程 HTA 文件，并通过`mshta.exe`程序执行该文件。”

当用户运行仓库中附带的 Python 脚本（误以为自己在启动一款实用工具）时，一个隐藏的子进程会随即触发攻击感染链。“这些仓库的核心目的并非提供合法功能，而是诱导用户执行内置的 Python 或 JavaScript 加载器程序片段。”

此次攻击的恶意载荷**PyStoreRAT**，堪称现代恶意软件规避检测技术的典型范例。它作为一款无文件 JavaScript 植入程序，通过 Windows HTML 应用程序（HTA）子系统执行，几乎不会在磁盘上留下任何痕迹。尽管其传播载体十分轻量，但破坏力却不容小觑。

“PyStoreRAT 本质上是一款模块化的多阶段 JavaScript 植入程序，能够执行多种格式的恶意载荷，包括可执行文件（EXE）、动态链接库（DLL）、PowerShell 脚本、Windows 安装包（MSI）、Python 脚本、JavaScript 脚本以及 HTA 模块。”

这种模块化设计让攻击者能够动态调整攻击操作，既可以部署文件加密程序，也能植入高级间谍软件。在近期的攻击事件中，研究人员发现这款远程访问木马会投放臭名昭著的 “拉达曼迪斯”（Rhadamanthys）信息窃取器，用以窃取目标设备中的敏感数据。

PyStoreRAT 最令人警惕的特性之一，是它具备 \*\*“环境感知能力”\*\*。该恶意软件会主动扫描设备中安装的安全工具，并内置特定逻辑，专门规避主流安全检测产品的监控。

报告指出，这款恶意软件 “包含针对‘火眼猎鹰’（CrowdStrike Falcon）安全软件的明确规避逻辑”。一旦检测到火眼相关进程（如`csfalconservice`）或 “睿森实验室”（ReasonLabs）等其他杀毒软件，它会立刻改变自身执行方式 —— 通过命令行包装器启动，切断进程树关联，干扰安全工具的行为监控机制。

为了在受害设备重启后仍能驻留，PyStoreRAT 采用了经典的伪装策略：创建一个看似常规驱动更新任务的 Windows 计划任务。

“该任务伪装成‘英伟达应用自动更新\_[全球唯一标识符]’（NVIDIA App SelfUpdate\_[GUID]），被设置为每 10 分钟运行一次，或在用户登录时触发”，以此确保恶意软件能长期潜伏在目标设备中。

尽管攻击者的溯源工作仍在进行，但莫菲赛克分析师已发现指向东方的线索。报告称：“软件中出现的俄语特征代码与编程模式，表明其幕后黑手很可能来自东欧地区。”

在开发者对开源生态系统依赖度日益提升的当下，PyStoreRAT 的出现为所有人敲响警钟：必须逐行核查代码的安全性。这款恶意软件 “标志着恶意软件正朝着模块化、脚本化植入程序的方向发展，这类恶意程序能够自适应安全防护措施，并加载多种格式的恶意载荷”，已然成为当下网络安全领域的一大强劲威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/pystorerat-uncovered-fileless-rat-hides-in-fake-github-repos-to-launch-invisible-attacks-on-developers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313823](/post/id/313823)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/pystorerat-uncovered-fileless-rat-hides-in-fake-github-repos-to-launch-invisible-attacks-on-developers/)

如若转载,请注明出处： <https://securityonline.info/pystorerat-uncovered-fileless-rat-hides-in-fake-github-repos-to-launch-invisible-attacks-on-developers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **820**

* 粉丝
* **6**

### TA的文章

* ##### [惠普预测：2026 年人工智能驱动型网络威胁与 Cookie 窃取攻击将激增](/post/id/313832)

  2025-12-18 09:52:40
* ##### [黑力钓鱼即服务平台（BlackForce PhaaS）滥用 React 框架与有状态会话，实现多因素认证绕过与凭证窃取](/post/id/313827)

  2025-12-18 09:51:49
* ##### [新型恶意软件 PyStoreRAT 现身：无文件远程访问木马藏身伪造 GitHub 代码仓库，发起针对开发者的隐形攻击](/post/id/313823)

  2025-12-18 09:51:11
* ##### [“幻影窃取者” 恶意软件借 ISO 钓鱼攻击瞄准金融领域，实施键盘记录与加密货币钱包窃取](/post/id/313818)

  2025-12-18 09:50:33
* ##### [青少年体育赛事及全美大学体育协会保险理赔数据或遭黑客窃取](/post/id/313816)

  2025-12-18 09:49:40

### 相关文章

* ##### [惠普预测：2026 年人工智能驱动型网络威胁与 Cookie 窃取攻击将激增](/post/id/313832)

  2025-12-18 09:52:40
* ##### [黑力钓鱼即服务平台（BlackForce PhaaS）滥用 React 框架与有状态会话，实现多因素认证绕过与凭证窃取](/post/id/313827)

  2025-12-18 09:51:49
* ##### [“幻影窃取者” 恶意软件借 ISO 钓鱼攻击瞄准金融领域，实施键盘记录与加密货币钱包窃取](/post/id/313818)

  2025-12-18 09:50:33
* ##### [青少年体育赛事及全美大学体育协会保险理赔数据或遭黑客窃取](/post/id/313816)

  2025-12-18 09:49:40
* ##### [飞塔防火墙单点登录高危漏洞遭在野利用：攻击者绕过认证并窃取配置文件](/post/id/313811)

  2025-12-18 09:48:51
* ##### [ScreenConnect 高危漏洞（CVE-2025-14265）存在配置泄露与恶意扩展安装风险](/post/id/313807)

  2025-12-18 09:48:07
* ##### [OpenShift GitOps 高危漏洞可致集群沦陷（CVE-2025-13888）—— 低权限用户可提权至 root 权限](/post/id/313803)

  2025-12-18 09:47:20

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