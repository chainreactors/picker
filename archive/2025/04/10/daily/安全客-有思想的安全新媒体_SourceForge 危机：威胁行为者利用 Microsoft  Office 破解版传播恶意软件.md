---
title: SourceForge 危机：威胁行为者利用 Microsoft  Office 破解版传播恶意软件
url: https://www.anquanke.com/post/id/306309
source: 安全客-有思想的安全新媒体
date: 2025-04-10
fetch_date: 2025-10-06T22:04:01.974164
---

# SourceForge 危机：威胁行为者利用 Microsoft  Office 破解版传播恶意软件

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

# SourceForge 危机：威胁行为者利用 Microsoft Office 破解版传播恶意软件

阅读量**56765**

发布时间 : 2025-04-09 11:05:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/04/cryptocurrency-miner-and-clipper.html>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员观察到，威胁行为者通过热门软件托管服务 SourceForge，以Microsoft Office等正版应用程序破解版的名义，分发诸如加密货币挖矿程序和剪切板劫持恶意软件等恶意有效载荷。

卡巴斯基在今日发布的一份报告中称：“在 sourceforge.net 主网站上，有一个名为 officepackage 的项目，乍一看似乎并无危害，它包含从一个合法的 GitHub 项目复制来的 Microsoft Office 插件。”

虽然在 sourceforge.net 上创建的每个项目都会被分配一个 “<项目名>.sourceforge.io” 的域名，但这家俄罗斯网络安全公司发现，officepackage 项目的域名 “officepackage.sourceforge [.] io” 会显示一长串 Microsoft Office 应用程序，以及相应的俄语下载链接。

除此之外，将鼠标悬停在下载按钮上时，浏览器状态栏中会显示一个看似合法的网址：“loading.sourceforge [.] io/download”，这给人一种该下载链接与 SourceForge 相关联的假象。然而，点击该链接会将用户重定向到一个完全不同的页面，该页面托管在 “taplink [.] cc” 上，并且突出显示另一个下载按钮。

如果受害者点击这个下载按钮，就会下载到一个 7 兆字节的 ZIP 压缩文件（“vinstaller.zip”）。打开这个文件后，里面有一个受密码保护的压缩文件（“installer.zip”），以及一个包含打开该文件的密码的文本文件。

在新的 ZIP 文件中，有一个 MSI 安装程序，它负责创建几个文件、一个名为 “UnRAR.exe” 的控制台压缩实用程序、一个 RAR 压缩文件以及一个 Visual Basic（VB）脚本。

卡巴斯基表示：“这个 VB 脚本会运行一个 PowerShell 解释器，从 GitHub 上下载并执行一个名为 confvk 的批处理文件，这个文件包含 RAR 压缩文件的密码。它还会解压恶意文件并运行下一阶段的脚本。”

这个批处理文件还被设计为运行两个 PowerShell 脚本，其中一个会使用 Telegram API 发送系统元数据。另一个文件会下载另一个批处理脚本，该脚本随后会对 RAR 压缩文件的内容进行操作，最终启动挖矿程序和剪切板劫持恶意软件（又名 ClipBanker）有效载荷。

同时被释放的还有 netcat 可执行文件（“ShellExperienceHost.exe”），它会与远程服务器建立加密连接。这还不是全部，研究发现，confvk 批处理文件会创建另一个名为 “ErrorHandler.cmd” 的文件，其中包含一个 PowerShell 脚本，该脚本被编程为通过 Telegram API 检索并执行一个文本字符串。

该网站具有俄语界面这一事实表明，其目标主要是俄语用户。遥测数据显示，90% 的潜在受害者位于俄罗斯，在 1 月初至 3 月底期间，有 4604 名用户遭遇了这一攻击计划。

由于 sourceforge [.] io 页面被搜索引擎索引并出现在搜索结果中，因此据信，在 Yandex 上搜索 Microsoft Office 的俄罗斯用户很可能是这次攻击活动的目标。

卡巴斯基称：“当用户在官方渠道之外寻找下载应用程序的方法时，攻击者就会提供他们自己的版本。虽然这次攻击主要通过部署挖矿程序和 ClipBanker 来针对加密货币，但攻击者可能会将系统访问权限出售给更危险的行为者。”

与此同时，该公司还披露了一起攻击活动的详细信息，攻击者通过模仿 DeepSeek 人工智能（AI）聊天机器人以及远程桌面和 3D 建模软件的欺诈性网站，分发一种名为 TookPS 的恶意软件下载器。

这些欺诈性网站包括 deepseek-ai-soft [.] com 等，毫无防备的用户会通过Google 搜索结果被重定向到这些网站。

TookPS 旨在下载并执行 PowerShell 脚本，通过 SSH 实现对受感染主机的远程访问，并释放一个名为 TeviRat 的木马修改版本。这凸显了威胁行为者试图通过各种方式完全控制受害者计算机的企图。

卡巴斯基表示：“该样本使用 DLL 侧加载技术，将 TeamViewer 远程访问软件修改并部署到受感染设备上。” “简单来说，攻击者将一个恶意库放置在与 TeamViewer 相同的文件夹中，这会改变该软件的默认行为和设置，使其对用户隐藏，并为攻击者提供隐蔽的远程访问权限。”

在此之前，还发现了针对热门的 VMware 实用工具 RVTools 的恶意Google 广告，这些广告会提供一个被篡改的版本，其中植入了 ThunderShell（又名 SMOKEDHAM），这是一种基于 PowerShell 的远程访问工具（RAT），这进一步凸显了恶意广告仍然是一种持续存在且不断演变的威胁。

Field Effect 表示：“ThunderShell，有时也被称为 SmokedHam，是一个公开可用的攻击后利用框架，用于红队演练和渗透测试。它提供了一个命令与控制（C2）环境，允许操作者通过基于 PowerShell 的代理在被攻陷的机器上执行命令。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/04/cryptocurrency-miner-and-clipper.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306309](/post/id/306309)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/04/cryptocurrency-miner-and-clipper.html)

如若转载,请注明出处： <https://thehackernews.com/2025/04/cryptocurrency-miner-and-clipper.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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