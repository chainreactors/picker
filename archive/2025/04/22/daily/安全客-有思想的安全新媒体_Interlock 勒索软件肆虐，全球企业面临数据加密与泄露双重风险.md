---
title: Interlock 勒索软件肆虐，全球企业面临数据加密与泄露双重风险
url: https://www.anquanke.com/post/id/306737
source: 安全客-有思想的安全新媒体
date: 2025-04-22
fetch_date: 2025-10-06T22:03:44.660927
---

# Interlock 勒索软件肆虐，全球企业面临数据加密与泄露双重风险

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

# Interlock 勒索软件肆虐，全球企业面临数据加密与泄露双重风险

阅读量**53048**

发布时间 : 2025-04-21 15:01:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/interlock-ransomware-uses-evolving-tactics-to-evade-detection/>

译文仅供参考，具体内容表达以及含义原文为准。

![Interlock Ransomware, ClickFix]()

Sekoia 威胁检测与研究团队（TDR）的一份新报告详细阐述了 Interlock 勒索软件的入侵活动。Interlock 首次被发现于 2024 年 9 月，以实施 Big Game Hunting 和双重勒索活动而闻名。尽管它不被归类为勒索软件即服务（RaaS）组织，但 Interlock 运营着一个名为 Worldwide Secrets Blog 的数据泄露网站，以此向受害者施压。

Interlock 的操控者利用托管在被攻陷网站上的虚假浏览器或安全软件更新程序来获取目标系统的访问权限。这些所谓的安装程序实际上是 PyInstaller 可执行文件，会启动基于 PowerShell 的后门程序。

报告解释道：“这个 PowerShell 脚本在一个无限循环中运行，持续执行 HTTP 请求。它收集系统信息，并提供执行任意命令和实现持久化的功能。”

这个脚本的后续版本（现已更新到第 11 版）添加了基于注册表的持久化功能，并使用 Cloudflare 的 trycloudflare.com 进行动态隧道传输，改进了命令与控制（C2）逻辑。该脚本会窃取加密的系统信息，并通过与 C2 服务器之间的 XOR 加密数据下载有效载荷。

2025 年 1 月，Sekoia 记录到 Interlock 在试验 ClickFix 技术，这是一种社会工程学手段，通过伪造的验证码或浏览器警报提示用户执行恶意的 PowerShell 命令。这些虚假提示会敦促用户将命令粘贴到终端中以 “修复” 某个问题，而这往往会导致恶意软件在用户毫无察觉的情况下被安装。这种策略通过诱骗受害者手动执行恶意命令，绕过了自动化防御系统。

尽管自 2025 年 2 月以来，支持 ClickFix 的基础设施似乎处于休眠状态，但它的使用表明 Interlock 在传播机制方面正在积极创新。

Interlock 的攻击活动持续使用一些知名的凭据窃取恶意软件，比如 LummaStealer 和 BerserkStealer，这些恶意软件通常与键盘记录器捆绑在一起，并由定制的加壳程序进行保护。该组织还部署了一种专有的远程访问木马（RAT），被打包成动态链接库（DLL）文件，支持原始 TCP 通信和高级命令功能。

每个样本都包含来自诸如 BitLaunch 等虚拟专用服务器（VPS）提供商的硬编码 IP 地址，选择这些提供商通常是因为它们支持匿名加密货币支付。

Interlock 的操控者通常使用远程桌面协议（RDP）和窃取来的凭据在被攻陷的网络中进行横向移动。他们常常将目标锁定为域控制器，以获取广泛的控制权。该组织还使用诸如 PuTTY、AnyDesk，可能还有 LogMeIn 等工具来维持远程访问。在数据窃取方面，据观察，他们使用了 Azure 存储资源管理器和 AZCopy 工具。

Interlock 勒索软件存在 Windows 和 Linux 两个版本。Windows 版本会加密文件并留下勒索便条，这些便条的内容会随着时间的推移而变化。

Sekoia 总结道：“Interlock不断改进他们的工具和方法，这表明他们既希望保持其影响力，又避免引起大规模的关注。”

本文翻译自securityonline [原文链接](https://securityonline.info/interlock-ransomware-uses-evolving-tactics-to-evade-detection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306737](/post/id/306737)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/interlock-ransomware-uses-evolving-tactics-to-evade-detection/)

如若转载,请注明出处： <https://securityonline.info/interlock-ransomware-uses-evolving-tactics-to-evade-detection/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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