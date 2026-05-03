---
title: EtherRAT 攻击活动利用 SEO 投毒和 GitHub 伪装账户攻击企业管理员
url: https://mp.weixin.qq.com/s/0hNj1tNym2jULVVyEDnyXg
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:27:46.700853
---

# EtherRAT 攻击活动利用 SEO 投毒和 GitHub 伪装账户攻击企业管理员

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PaFY6wibdwyKWyx60D6qAltJfcZdkGJmKqErQkIm9p5Bh0ebvMj458B46Lru5FhFQXVVibzyhQpYeib5LX5XlECJONx9rxzfXFXOFAkEZZ0pUs/0?wx_fmt=jpeg)

# EtherRAT 攻击活动利用 SEO 投毒和 GitHub 伪装账户攻击企业管理员

会杀毒的单反狗
会杀毒的单反狗

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导****读**

一场精心策划的新型恶意软件攻击活动正通过劫持企业管理员、DevOps工程师和安全分析师的日常搜索习惯，积极地针对他们进行攻击。

这次行动背后的威胁组织没有使用大规模网络钓鱼或垃圾邮件攻击，而是精心设计了一条传播链，将危险软件直接推送给那些在网上搜索常规管理工具的高权限 IT 专业人员。

![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyIO4rVevNNz4cYyb4ul8fqHZwmsgLpLeH4Hmx2X15QrjYibKjXdgyibZFFFDD5gVBss0NJQBZY58ppQFD7bUubKULUnsnuyTKBLo/640?wx_fmt=png&from=appmsg)

该活动通过污染多个主要平台（包括 Bing、Yahoo、DuckDuckGo 和 Yandex）的搜索引擎结果来实现。

当 IT 人员搜索 PsExec、AzCopy、Sysmon、LAPS 或 KustoExplorer 等工具时，搜索结果页面顶部会显示虚假的、看起来很专业的GitHub 存储库。

这些代码库看起来干净合法，表面上不包含任何恶意代码。

它们纯粹充当网关，悄悄地将毫无戒心的用户重定向到一个隐藏的辅助 GitHub 帐户，真正的恶意软件就托管在这个帐户中并进行分发。

Atos 分析师在 3 月份发现了这一复杂且具有高韧性的恶意攻击活动。

研究人员证实，该活动仍然非常活跃，并且自其开始以来已经取得了显著的技术成熟，随着时间的推移，已经发现了几个不同的变体和额外的指挥控制 (C2) 基础设施。

此次攻击活动的核心恶意软件是一个用 JavaScript 编写的多阶段、无文件式远程访问木马 (RAT)。

Atos 的研究人员证实，这是 EtherRAT，一种最近出现的威胁，它利用以太坊区块链存储其实时 C2 服务器地址，从而有效阻止传统的域名删除或 IP 封锁措施。

该恶意软件通过伪装成 PsExec、AzCopy、Sysmon、LAPS 和 KustoExplorer 等工具的恶意 MSI 安装程序进行传播，这些工具几乎完全由具有较高网络和系统权限的人员使用。

成功感染管理员工作站，就能让攻击者掌握整个企业环境的控制权。

此次攻击活动的心理层面尤其具有攻击性。许多被冒充的工具与安全专业人员用于调查和应对恶意活动的工具完全相同。

这就造成了一种讽刺的局面：防御者试图使用 Process Explorer 或 TCPView 等工具来诊断感知到的问题，却无意中引入了他们试图发现的威胁。

双阶段 GitHub 交付链

该活动采用精心设计的两阶段分发架构，即使部分内容被移除，也能继续进行。

第一个 GitHub 代码库仅作为外观简洁的展示平台。它经过 SEO 优化，包含专业的 README 文件，不包含任何恶意代码，从而在用户和安全工具中建立初步信任。

该README文件中嵌入了一个指向第二个隐藏GitHub帐户的链接。这个辅助仓库托管着实际的恶意MSI有效载荷。

通过将 SEO 可见的店面与有效载荷交付帐户分开，威胁组织可以在被标记后迅速轮换其分发存储库，而主要的搜索引擎索引外观仍然保持活跃且不受影响。

从 2024 年 12 月初到 2026 年 4 月，威胁组织部署了 17 个独立的 GitHub 外观，每个外观都模仿不同的管理或开发工具，这表明他们持续努力，以最大限度地提高搜索引擎可见性并捕获各种高权限受害者。

当受害者下载并运行 MSI 时，会提取四个文件，并在文件提取后立即通过具有 SYSTEM 权限的自定义操作启动 CMD 批处理脚本。

入口点是一个经过高度混淆的 Windows 批处理脚本，由 MSI 自定义操作在文件提取后立即以 SYSTEM 权限启动。

它的主要混淆机制是将所有敏感命令名称（包括 curl、tar、copy、start 和 cmd）拆分到多个 SET 变量赋值中，这些赋值会在运行时静默地连接起来，从而确保原始文件中不会出现任何可识别的关键字，并阻止简单的基于字符串的静态分析。

第二阶段是一个最小的 Node.js 脚本，未混淆且完全可读，但永远不会保存到磁盘。

它的主要目标是读取包含第二阶段加密有效载荷的文件，使用硬编码的密钥和初始化向量（IV）对其进行解密，并在内存中执行。它还会通过注册表中的 Run 键创建持久化存储。

第三阶段是恶意软件的主要有效载荷，它是一个 JavaScript 文件，在每次系统启动时都会在 conhost.exe（一个合法的Windows 进程）内部静默运行，因此不会在任务管理器中显眼。

技术报告：

https://atos.net/en/lp/cybershield/etherrat-distribution-spoofing-administrative-tools-via-github-facades

新闻链接：

https://cybersecuritynews.com/etherrat-campaign-uses-seo-poisoning/

![](https://mmbiz.qpic.cn/mmbiz_svg/McYMgia19V0WHlibFPFtGclHY120OMhgwDUwJeU5D8KY3nARGC1mBpGMlExuV3bibicibJqMzAHnDDlNa5SZaUeib46xSzdeKIzoJA/640?wx_fmt=svg)

**今日安全资讯速递**

**APT事件**

Advanced Persistent Threat

1. 复杂 Deep#Door 后门实现间谍活动和破坏

这种隐蔽的基于Python的后门框架部署了一个持久化的Windows植入物，可能旨在进行间谍活动。

🔗https://www.securityweek.com/sophisticated-deepdoor-backdoor-enables-espionage-disruption/

2. 新型间谍软件平台允许买家进行品牌重塑和重新销售安卓监控恶意软件

一种新的安卓间谍软件工具KidsProtect正在互联网上公开出售，它所具备的危险性远不止其监控功能。付费后，任何人都可以购买该工具，加上自己的名称和标志，然后将其作为自己的产品进行销售。

🔗https://cybersecuritynews.com/new-spyware-platform-lets-buyers-rebrand/

3. 威胁组织针对亚洲政府、北约、记者和活动人士

网络安全研究人员披露一项新的间谍活动细节，该活动针对南亚、东亚和东南亚地区敏感部门，以及一个属于北约的组织。Trend Micro 将此活动归因于命名为 SHADOW-EARTH-053 的威胁组织。

🔗https://thehackernews.com/2026/05/china-linked-hackers-target-asian.html

**一般威胁事件**

General Threat Incidents

1. 网络犯罪活动涉及4.5万次攻击和5300多个后门

SOCRadar威胁研究团队发现一个庞大自动化网络犯罪网络。该网络犯罪活动使用名为Paperclip的中央后端和名为OpenClaw的基于代理的工作流系统。

🔗https://hackread.com/45k-attacks-53k-backdoor-china-cybercrime-operation/

2. EtherRAT 攻击活动利用 SEO 投毒和 GitHub 伪装账户攻击企业管理员

一场精心策划的新型恶意软件攻击活动正通过劫持企业管理员、DevOps工程师和安全分析师的日常搜索习惯，积极地针对他们进行攻击。

🔗https://cybersecuritynews.com/etherrat-campaign-uses-seo-poisoning/

3. 污染的 Ruby 安装包和 Go 模块利用 CI 流水线进行凭据窃取

最近发现了一种新的软件供应链攻击活动，该活动使用休眠包作为渠道，随后推送恶意负载，实现了凭证窃取、GitHub Actions篡改和SSH持久化。该活动被归因于GitHub账户“BufferZoneCorp”，该账户发布了一系列与恶意Ruby gem和Go模块相关的仓库。

🔗https://thehackernews.com/2026/05/poisoned-ruby-gems-and-go-modules.html

4. 不断升级的供应链攻击渗透到 SAP npm 包及其他开发工具

Mini Shai-Hulud 被发现传播窃取凭据的恶意软件针对安全和开发工具的供应链攻击浪潮已导致更多受害者，即 SAP 和 Intercom 的 npm 包，以及闪电般的 PyPI 包。

🔗https://go.theregister.com/feed/www.theregister.com/2026/04/30/supply\_chain\_attacks\_sap\_npm\_packages/

5. 攻击者滥用 CAPTCHA 和 ClickFix 策略以提升凭证窃取活动

网络犯罪分子不再仅仅依赖简单的电子邮件欺骗手段。在2026年第一季度，攻击者通过使用CAPTCHA页面和ClickFix技术，以惊人的规模加强了凭证窃取行动。

🔗https://cybersecuritynews.com/attackers-abuse-captcha-and-clickfix-tactics/

6. Canonical 遭受持续 DDoS 攻击，全球 Ubuntu 服务中断

Canonical 遭受 DDoS 攻击，导致关键的 Ubuntu 服务和补丁工作流程中断。

🔗https://www.esecurityplanet.com/threats/canonical-hit-by-sustained-ddos-attack-disrupting-ubuntu-services-worldwide/

7. 黑客利用 Jenkins 访问权限在游戏服务器上部署 DDoS 僵尸网络

一个新攻击活动显示，被配置错误的 Jenkins 服务器被滥用于部署针对游戏系统的 DDoS 僵尸网络，Valve 公司的基础设施成为重点目标。

🔗https://hackread.com/hackers-jenkins-ddos-botnet-gaming-servers/

**漏洞事件**

Vulnerability Incidents

1. 正在被利用的 cPanel 漏洞使数百万网站面临被接管的风险

cPanel/WHM 管理界面中的一个漏洞使攻击者可以在无需用户名和密码的情况下访问网站。

🔗https://www.malwarebytes.com/blog/news/2026/05/actively-exploited-cpanel-bug-exposes-millions-of-websites-to-takeover

2. 危险的新 Linux 漏洞CopyFail使攻击者获得无数计算机的 root 访问权限

该漏洞被称为CopyFail，追踪编号为CVE-2026-31431，允许黑客接管个人电脑和数据中心服务器。

🔗https://www.wired.com/story/dangerous-new-linux-exploit-gives-attackers-root-access-to-countless-computers/

3. 多个 Wireshark 漏洞通过恶意数据包允许任意代码执行

Wireshark基金会已发布其广泛使用的网络协议分析器的4.6.5版本，修复了大量安全漏洞。此次紧急更新修补了40多个不同的安全漏洞，这是由于近期AI辅助漏洞报告的激增所驱动。

🔗https://gbhackers.com/multiple-wireshark-vulnerabilities/

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

军哥网络安全读报

**讲述普通人能听懂的安全故事**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

爱拍照的老李

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过