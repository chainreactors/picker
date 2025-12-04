---
title: 恶意Rust软件包“evm-units”使加密货币开发者面临隐秘攻击风险
url: https://www.anquanke.com/post/id/313542
source: 安全客-有思想的安全新媒体
date: 2025-12-03
fetch_date: 2025-12-04T03:17:35.785303
---

# 恶意Rust软件包“evm-units”使加密货币开发者面临隐秘攻击风险

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

# 恶意Rust软件包“evm-units”使加密货币开发者面临隐秘攻击风险

阅读量**13472**

发布时间 : 2025-12-03 17:19:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/malicious-rust-package-evm-units-exposes-crypto-developers-to-stealth-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款看似无害的以太坊开发者工具被揭露为 **复杂的隐身加载器**。Socket 威胁研究团队近期发现一个名为 `evm-units` 的恶意 Rust 包（用户 `ablerust` 开发），在被移除前累计下载量超 7,000 次。该包在 Crates.io 仓库存在八个月，伪装成处理以太坊虚拟机（EVM）单位的工具，实则隐藏着旨在 **静默执行的危险 payload**。

恶意软件的核心欺骗性在于 **“明处隐藏”**。对普通观察者或运行测试的开发者而言，包表现正常：“它会返回以太坊版本号，让受害者完全无察觉。”

但 `get_evm_version()` 函数远不止返回简单整数。研究人员警告：“调用该函数检查版本号时，会启动一系列最终导致入侵的步骤。”

触发后，函数会解码隐藏的 Base64 URL，并下载针对受害者操作系统（Linux/macOS/Windows）的恶意 payload。执行过程设计为 **极致隐身**：

1. **Linux/macOS**：通过 `nohup` 在后台运行 payload，抑制所有终端输出
2. **Windows**：利用 VBScript 包装器执行隐藏的 PowerShell 窗口，确保用户屏幕无任何显示

`evm-units` 最显著的特征是其在 Windows 系统上的特定行为，强烈暗示威胁者 **重点关注亚洲市场受害者**。

执行 payload 前，恶意软件会检查系统是否存在 `qhsafetray.exe`

报告指出若检测到杀毒软件，恶意软件会 **切换执行方式**：放弃 VBScript 包装器，直接使用 PowerShell 命令以绕过检测。

攻击不仅限于直接安装 `evm-units` 的用户。威胁者还通过创建第二个包 `uniswap-utils` 污染供应链——该包声称是热门去中心化交易所 Uniswap 的辅助库。

研究人员解释：“同一作者开发的 `uniswap-utils` 看似完全无害，但它依赖 `evm-units` 并在文件中调用其函数。”

这种依赖通过 Rust 的 **自动执行特性** 被武器化：“恶意代码因 `#[ctor::ctor]` 注解在初始化时自动运行，构成典型的供应链攻击。”

尽管该包已从 Crates.io 移除，但其八个月的生命周期和定向攻击模式仍发出严厉警告。“包名称和代码行为（EVM 工具、仿 Uniswap 库），表明 payload 很可能用于 **窃取加密货币**。”

本文翻译自securityonline [原文链接](https://securityonline.info/malicious-rust-package-evm-units-exposes-crypto-developers-to-stealth-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313542](/post/id/313542)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/malicious-rust-package-evm-units-exposes-crypto-developers-to-stealth-attacks/)

如若转载,请注明出处： <https://securityonline.info/malicious-rust-package-evm-units-exposes-crypto-developers-to-stealth-attacks/>

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
* **770**

* 粉丝
* **6**

### TA的文章

* ##### [Django框架中存在漏洞（CVE-2025-13372），可导致PostgreSQL FilteredRelation功能出现SQL注入风险](/post/id/313545)

  2025-12-03 17:24:38
* ##### [美国CISA发布警告：Iskra iHUB智能计量枢纽存在严重漏洞（CVE-2025-13510），可致攻击者未授权接管智能计量系统](/post/id/313548)

  2025-12-03 17:24:17
* ##### [Elementor插件中存在严重漏洞（CVE-2025-8489，CVSS 9.8），正被积极利用以获取未授权的网站管理员权限](/post/id/313551)

  2025-12-03 17:23:53
* ##### [亚马逊推出基于NVIDIA架构的本地化“AI工厂”解决方案，向竞争对手发起挑战](/post/id/313554)

  2025-12-03 17:23:14
* ##### [AWS与NVIDIA联合发布“AI工厂”解决方案，整合Blackwell GPU与Trainium芯片](/post/id/313557)

  2025-12-03 17:22:56

### 相关文章

* ##### [Django框架中存在漏洞（CVE-2025-13372），可导致PostgreSQL FilteredRelation功能出现SQL注入风险](/post/id/313545)

  2025-12-03 17:24:38
* ##### [美国CISA发布警告：Iskra iHUB智能计量枢纽存在严重漏洞（CVE-2025-13510），可致攻击者未授权接管智能计量系统](/post/id/313548)

  2025-12-03 17:24:17
* ##### [Elementor插件中存在严重漏洞（CVE-2025-8489，CVSS 9.8），正被积极利用以获取未授权的网站管理员权限](/post/id/313551)

  2025-12-03 17:23:53
* ##### [亚马逊推出基于NVIDIA架构的本地化“AI工厂”解决方案，向竞争对手发起挑战](/post/id/313554)

  2025-12-03 17:23:14
* ##### [AWS与NVIDIA联合发布“AI工厂”解决方案，整合Blackwell GPU与Trainium芯片](/post/id/313557)

  2025-12-03 17:22:56
* ##### [Google运用Gmail数据驱动AI个性化服务，此举引发用户隐私担忧](/post/id/313560)

  2025-12-03 17:22:31
* ##### [攻击者利用Evilginx工具，通过仿冒合法单点登录网站从根本上攻破多因素认证安全](/post/id/313563)

  2025-12-03 17:22:07

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