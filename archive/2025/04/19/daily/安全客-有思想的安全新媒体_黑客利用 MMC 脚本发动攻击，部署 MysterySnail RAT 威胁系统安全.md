---
title: 黑客利用 MMC 脚本发动攻击，部署 MysterySnail RAT 威胁系统安全
url: https://www.anquanke.com/post/id/306679
source: 安全客-有思想的安全新媒体
date: 2025-04-19
fetch_date: 2025-10-06T22:05:16.482445
---

# 黑客利用 MMC 脚本发动攻击，部署 MysterySnail RAT 威胁系统安全

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

# 黑客利用 MMC 脚本发动攻击，部署 MysterySnail RAT 威胁系统安全

阅读量**65769**

发布时间 : 2025-04-18 14:22:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/mmc-script-weaponized/>

译文仅供参考，具体内容表达以及含义原文为准。

一场复杂的网络间谍活动利用了恶意的微软管理控制台（MMC）脚本来部署隐秘的 MysterySnail 远程访问木马（RAT）。

MysterySnail 远程访问木马最早于 2021 年在对 CVE-2021-40449 零日漏洞的调查中被发现，此后它似乎从网络威胁领域中消失了。

该恶意软件被认为出自一个名为 IronHusky的威胁行为者之手，至少从 2017 年起这个组织就开始活跃了。显然，多年来这种恶意软件一直处于活跃状态，只是未被发现。

卡巴斯基表示：“事实证明，尽管此前没有相关报告，但这些年来这种植入程序一直在网络攻击中被频繁使用。”

****复杂的感染链条****

攻击始于一个伪装成 ALAMGAC 文件的恶意 MMC 脚本。这种社会工程策略增加了政府目标打开这个伪装文件的可能性。

一旦脚本被执行，就会启动一个多阶段的感染过程。首先，它会从 file [.] io 存储中获取一个 ZIP 压缩包，其中包含第二阶段的有效载荷和一个合法的 DOCX 文件。

该压缩包会被解压到特定目录：% AppData%\Cisco\Plugins\X86\bin\etc\Update

一个合法的可执行文件（CiscoCollabHost.exe）会被启动，它通过 DLL 侧加载技术加载一个恶意库（CiscoSparkLauncher.dll）。

此外，攻击者会通过修改注册表来实现持久驻留，同时诱饵文件会打开以避免引起怀疑。

研究人员发现了一种创新的中间后门程序，它通过滥用开源的管道服务器项目与命令和控制（C2）服务器进行通信。

作为一种不同寻常的反分析技术，这个后门程序将 Windows API 函数信息存储在一个外部文件（log\MYFC.log）中，该文件使用单字节异或（XOR）加密，并在运行时加载。

这个后门程序会与 https://ppng.io 通信以接收以下命令：

1.RCOMM：运行命令shell。

2.FSEND：从 C2 服务器下载文件。

3.FRECV：将文件上传到 C2 服务器。

4.FEXEC：创建新进程。

5.FDELE：删除文件。

****进化后的**** ****MysterySnail********远程访问木马****

最新版本的 MysterySnail 作为一项服务保持持久驻留，并使用了复杂的加密技术。其恶意 DLL 会从一个名为 attach.dat 的文件中加载用 RC4 和异或（XOR）加密的有效载荷，并通过使用 run\_pe 库的 DLL 空洞化技术来实现反射式加载。

研究人员观察到，它会与多个由攻击者控制的域名进行通信，包括 watch-smcsvc [.] com 和 leotolstoys [.] com。

与 2021 年的版本不同，当时的版本在单个组件中实现了大约 40 个命令，而新的 MysterySnail 采用了模块化架构，在运行时会下载五个专门的 DLL：

1.BasicMod.dll：处理磁盘驱动器列表、文件删除和系统指纹识别。

2.ExplorerMoudleDll.dll：管理文件读取、服务管理和进程创建。

3.process.dll：列出并终止正在运行的进程。

4.cmd.dll：创建进程和命令shell。

5.tcptran.dll：管理网络连接。

研究人员还发现了一个名为 MysteryMonoSnail的轻量级变种，它通过 WebSocket 协议而非 HTTP 进行通信，功能较少，仅提供 13 个基本命令。

MysterySnail 的再次出现凸显了对潜在威胁保持警惕的重要性。

研究人员警告称：“在进行威胁搜寻活动时，至关重要的是要考虑到那些多年来未被报道的旧恶意软件家族，它们可能仍在暗中继续活动。”

MysterySnail 的案例表明，威胁行为者如何通过对现有恶意软件进行最小限度的修改来保持其操作的持续性，从而使其在很长一段时间内不被发现。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/mmc-script-weaponized/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306679](/post/id/306679)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/mmc-script-weaponized/)

如若转载,请注明出处： <https://cybersecuritynews.com/mmc-script-weaponized/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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