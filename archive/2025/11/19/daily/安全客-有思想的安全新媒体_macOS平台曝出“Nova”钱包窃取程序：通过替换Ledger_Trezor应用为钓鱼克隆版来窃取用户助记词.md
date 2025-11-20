---
title: macOS平台曝出“Nova”钱包窃取程序：通过替换Ledger/Trezor应用为钓鱼克隆版来窃取用户助记词
url: https://www.anquanke.com/post/id/313255
source: 安全客-有思想的安全新媒体
date: 2025-11-19
fetch_date: 2025-11-20T03:08:24.385506
---

# macOS平台曝出“Nova”钱包窃取程序：通过替换Ledger/Trezor应用为钓鱼克隆版来窃取用户助记词

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

# macOS平台曝出“Nova”钱包窃取程序：通过替换Ledger/Trezor应用为钓鱼克隆版来窃取用户助记词

阅读量**15834**

发布时间 : 2025-11-19 17:39:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/macos-wallet-stealer-uncovered-nova-malware-replaces-ledger-trezor-apps-with-phishing-clones-for-seed-theft/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究员布鲁斯（Bruce）发现了一场新的 macOS 窃取者活动——研究人员内部将其命名为“Nova”。该活动揭示了一个模块化恶意软件生态系统，旨在窃取加密货币钱包、收集系统遥测数据，并**用钓鱼克隆体静默替换 Ledger 和 Trezor 应用**。

分析显示，攻击始于一个未知投放器（dropper），它会静默执行名为 **mdriversinstall.sh** 的恶意安装脚本。正如布鲁斯所述：“一个未知投放器获取并运行 mdriversinstall.sh ，该脚本会在 ~/.mdrivers 目录下安装一个小型脚本协调器，并注册一个标签为 application.com.artificialintelligence 的 LaunchAgent。”

此后，恶意软件会建立持久化机制，部署模块化协调器，从其命令与控制（C2）服务器获取额外的 **Base64 编码脚本**，并在**分离的 screen 会话**中运行这些脚本——这种行为在 macOS 恶意软件中极为罕见。

安装完成后，协调器会反复与攻击者的后端通信以检索恶意模块。布鲁斯指出：“该协调器从 C2 拉取经过 b64 编码的额外脚本，将其保存到 ~/.mdrivers/scripts 目录下，并在后台的分离 screen 会话中运行。”

这种架构允许攻击者**无需重新感染系统即可添加、更新或删除功能**。正如报告所解释：“这种模块化方法使攻击者能够即时轻松添加、删除或更新恶意功能。”

恶意软件甚至会在应用更新前检查现有 screen 会话——根据需要干净地终止并重启模块。

### C2 服务器当前提供的四个模块

#### 1. mdriversfiles.sh —— 加密货币钱包窃取

此模块专门用于窃取加密货币数据。报告显示，它会窃取：

1. Trezor Suite IndexedDB 日志
2. Exodus 的 passphrase.json 和 seed.seco 等文件
3. Ledger Live 的 app.json

布鲁斯表示：“对于每个找到的文件，它都会以二进制形式将原始文件 POST 到 C2……并添加 User\_ID 作为头部。”

#### 2. mdriversmetrics.sh —— 系统和应用程序分析

恶意软件会收集大量遥测数据，包括：

1. 已安装的应用程序
2. 正在运行的进程
3. 与钱包相关的检查
4. 自身组件的修改时间

报告指出，此模块“收集并通过 curl 发送大量关于系统及其使用情况的数据”。

#### 3. mdriversswaps.sh —— 钱包应用替换（钓鱼替换攻击）

最令人担忧的功能是**用攻击者控制的伪造应用替换真实的 Ledger Live.app 和 Trezor Suite.app** 。

布鲁斯强调了这一日益增长的趋势：“显然，替换加密货币钱包应用以获取助记词正成为 macOS 窃取者开发者的新趋势。”

该模块会：

1. 删除合法应用
2. 编辑 Dock 和 Launchpad 条目
3. 从攻击者服务器下载恶意替换应用
4. 将其持久化到用户可写目录

这确保受害者会在不知情的情况下启动钓鱼应用。

#### 4. mdriversusers.sh —— 未来的用户特定滥用

目前功能较少，此模块“加载 USER\_ID 并定期休眠……可能计划在未来用于特定用户”。

### 钓鱼应用与实时监控

这些替换应用是**未签名的 Swift 应用**，使用 WebKit，几乎与正版应用完全一致，每个应用都嵌入了一个加载钓鱼页面的 WebView。

钓鱼页面使用：

1. BIP-39 和 SLIP-39 词表进行自动验证
2. 自动前进的用户体验，模拟合法钱包恢复流程
3. 自动提交遥测数据，在用户输入时发送部分助记词
4. 通过 /track 端点进行持续活动跟踪

报告解释：“任何按键都会发送到目前为止已输入的内容；这使服务器能够在用户输入时重建助记词，无需最终‘提交’。”

即使是细微的交互——悬停事件、鼠标移动——也会被记录：“点击会被 POST 到 /track……每 10 秒记录一次在线活动。”

这种级别的遥测使攻击者能够重建助记词、密码短语和用户行为。

尽管具有模块化设计和持久化能力，布鲁斯指出该恶意软件并非特别隐蔽：“它不是一个复杂的威胁……它在磁盘上留下痕迹，使其易于检测，但其某些设计选择仍然值得关注。”

然而，其替换可信钱包应用的能力，再加上远程控制的实时钓鱼页面，对加密货币持有者构成了严重威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/macos-wallet-stealer-uncovered-nova-malware-replaces-ledger-trezor-apps-with-phishing-clones-for-seed-theft/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313255](/post/id/313255)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/macos-wallet-stealer-uncovered-nova-malware-replaces-ledger-trezor-apps-with-phishing-clones-for-seed-theft/)

如若转载,请注明出处： <https://securityonline.info/macos-wallet-stealer-uncovered-nova-malware-replaces-ledger-trezor-apps-with-phishing-clones-for-seed-theft/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **706**

* 粉丝
* **6**

### TA的文章

* ##### [SnowSoul勒索软件样本分析：加密机制与解密研究](/post/id/313279)

  2025-11-19 21:35:35
* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10

### 相关文章

* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10
* ##### [新型.NET加载器“隐匿窃密者”通过高级隐写术将LokiBot窃密木马植入BMP/PNG图片](/post/id/313252)

  2025-11-19 17:38:46
* ##### [npm供应链攻击预警：黑客利用Adspect伪装技术与虚假加密货币验证码同时欺骗用户与安全研究人员](/post/id/313249)

  2025-11-19 17:37:58
* ##### [SolarWinds Serv-U 中存在严重漏洞（CVSS 9.1），可导致已认证的管理员实现远程代码执行并完成路径绕过](/post/id/313245)

  2025-11-19 17:37:15

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