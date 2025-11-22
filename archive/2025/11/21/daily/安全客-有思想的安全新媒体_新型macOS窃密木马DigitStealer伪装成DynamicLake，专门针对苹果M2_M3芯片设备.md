---
title: 新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备
url: https://www.anquanke.com/post/id/313320
source: 安全客-有思想的安全新媒体
date: 2025-11-21
fetch_date: 2025-11-22T03:06:35.092281
---

# 新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备

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

# 新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备

阅读量**23085**

发布时间 : 2025-11-21 17:55:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2025/11/20/macos-digitstealer-malware-poses-as-dynamiclake-targets-apple-silicon-m2-m3-devices/>

译文仅供参考，具体内容表达以及含义原文为准。

一种新型信息窃取恶意软件正通过伪装成合法的 **DynamicLake UI增强工具** 和生产力实用程序，甚至可能伪装成 **Google Drive 桌面应用**，针对 macOS 用户。

### 多阶段投放机制

Jamf 研究人员将其命名为 **DigitStealer**，该威胁异常复杂：

在运行前，一个完全在内存中执行的 bash 脚本会检查系统的国家/地区设置，若发现设备位于特定区域则终止运行。
它还会检查设备是否为虚拟机，以及是否运行在 **Apple Silicon M2 或更新芯片** 上（通过检测特定硬件功能）。

研究人员发现：“恶意软件避免在虚拟机、基于 Intel 的 Mac 上运行，无论有意还是无意，也不支持 M1 芯片系统——尽管 M1 同样属于 Apple Silicon 家族。相反，它针对 M2 或更高版本芯片引入的新 ARM 特性设备。”

若“判定”条件满足，脚本会获取四个独立 payload 并开始投放和运行：

1. **第一个 payload**：简单的 AppleScript 信息窃取器，诱导用户输入密码。一旦用户输入，它会窃取凭证、小型用户文件（文档、笔记等），并重置 macOS TCC 数据库（记录哪些应用被允许访问敏感数据或系统功能）。
2. **第二个 payload**：压缩并窃取多个主流浏览器数据、Keychain 数据库、VPN 配置、Telegram 的 tdata 文件夹（可用于劫持 Telegram 账户），以及 Ledger、Electrum、Exodus、Coinomi 等加密货币钱包文件。
3. **第三个 payload**：用恶意版本替换 Ledger Wallet/Ledger Live 加密货币应用的 app.asar 文件，使其连接到攻击者控制的服务器，本质上劫持钱包，允许攻击者拦截或操纵受害者的加密货币钱包数据。
4. **第四个 payload**：在目标系统上投放并加载 Launch Agent 以实现持久化，每次运行时从攻击者服务器动态获取 payload。最初，该最终 payload 是一个后门——具有完整 AppleScript 权限的 JavaScript for Automation（JXA），但攻击者可随意更改 payload。

### 诱骗用户运行“应用”

研究人员表示：“已发现的样本以未签名磁盘镜像 **DynamicLake.dmg** 的形式存在。进一步调查后，我们识别出与该活动相关的其他几个磁盘镜像。”

DynamicLake.dmg 通过 **https[:]//dynamiclake[.]org** 域名和网站分发，该网站模仿同名合法 macOS 工具的官方站点。

被诱骗访问此伪造网站的用户会被指示将文件（实为初始脚本）拖入 Mac 的 **终端（Terminal）**，从而绕过 Gatekeeper 安全防护。

### 下载 Mac 应用时的注意事项

研究人员指出：“目前尚不清楚此特定变体的归属。但所用技术表明攻击者对 macOS 操作系统有深入了解，并持续专注于逃避检测。”

他们补充道，恶意软件作者不断滥用合法服务和分发方法，以绕过 macOS 安全控制并提高成功率。

过去几个月，攻击者创建了流行 Mac 应用的 **GitHub 仓库伪造副本**，并使用“拖入终端”技巧诱骗无防备用户运行恶意脚本（通常应用安装流程是拖入“应用程序”文件夹）。

最近，一名 Reddit 用户报告发现此伪造的 DynamicLake 应用以及伪造的 AirPosture，后者可能导致 DigitStealer 感染。

用户在搜索和安装新应用时应注意：

1. 仔细检查是否位于正确的网站/GitHub 仓库
2. 运行前使用 VirusTotal 扫描下载的安装程序
3. **切勿将应用拖入终端**
4. 可使用专业工具验证应用/安装程序的签名

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2025/11/20/macos-digitstealer-malware-poses-as-dynamiclake-targets-apple-silicon-m2-m3-devices/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313320](/post/id/313320)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2025/11/20/macos-digitstealer-malware-poses-as-dynamiclake-targets-apple-silicon-m2-m3-devices/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2025/11/20/macos-digitstealer-malware-poses-as-dynamiclake-targets-apple-silicon-m2-m3-devices/>

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
* **716**

* 粉丝
* **6**

### TA的文章

* ##### [N-able N-central 中存在严重漏洞，允许攻击者未授权交互遗留API并读取敏感文件](/post/id/313330)

  2025-11-21 17:56:21
* ##### [TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道](/post/id/313323)

  2025-11-21 17:55:57
* ##### [新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备](/post/id/313320)

  2025-11-21 17:55:18
* ##### [欧盟提出GDPR全面修订案，拟重新界定个人数据范畴与用户同意规则](/post/id/313317)

  2025-11-21 17:54:53
* ##### [Windows图形组件存在关键漏洞，可致攻击者通过单张图片夺取系统控制权](/post/id/313312)

  2025-11-21 17:54:23

### 相关文章

* ##### [N-able N-central 中存在严重漏洞，允许攻击者未授权交互遗留API并读取敏感文件](/post/id/313330)

  2025-11-21 17:56:21
* ##### [TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道](/post/id/313323)

  2025-11-21 17:55:57
* ##### [欧盟提出GDPR全面修订案，拟重新界定个人数据范畴与用户同意规则](/post/id/313317)

  2025-11-21 17:54:53
* ##### [Windows图形组件存在关键漏洞，可致攻击者通过单张图片夺取系统控制权](/post/id/313312)

  2025-11-21 17:54:23
* ##### [“Tsundere”僵尸网络利用游戏诱饵及基于以太坊的命令与控制服务器在Windows平台进行扩张](/post/id/313308)

  2025-11-21 17:53:47
* ##### [WSUS中存在关键远程代码执行漏洞（CVE-2025-59287），正被积极利用以部署ShadowPad后门](/post/id/313305)

  2025-11-21 17:52:53
* ##### [新型Sturnus木马可突破WhatsApp/Signal加密防护并完全控制Android设备](/post/id/313302)

  2025-11-21 17:51:00

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