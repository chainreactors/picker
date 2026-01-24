---
title: 带宽盗贼：伪造的Notepad++安装包暗藏 “代理劫持”恶意软件
url: https://www.anquanke.com/post/id/314481
source: 安全客-有思想的安全新媒体
date: 2026-01-23
fetch_date: 2026-01-24T03:29:53.516272
---

# 带宽盗贼：伪造的Notepad++安装包暗藏 “代理劫持”恶意软件

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

# 带宽盗贼：伪造的Notepad++安装包暗藏 “代理劫持”恶意软件

阅读量**27683**

发布时间 : 2026-01-23 10:20:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/bandwidth-bandits-fake-notepad-installers-hide-proxyjacking-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一波新的网络攻击正瞄准那些寻找免费软件的用户，把他们的电脑变成**不情愿的带宽共享参与者**。安恒实验室安全情报中心（ASEC）发布警告称，威胁组织 **Larva-25012** 正在通过分发伪装成热门文本编辑器 **Notepad++** 的恶意软件来实施攻击。

这是一种典型的 “**代理劫持（Proxyjacking）**” 攻击：攻击者在受害者电脑上悄悄安装软件，**盗用其网络带宽**来牟利。

该活动主要针对搜索**破解版或盗版软件**的用户。攻击者将受害者诱骗到 “伪装成提供破解 / 盗版软件下载的虚假网站”。这些网站通常声称自己 “界面友好、资源全面”，提供各种工具的恶意安装包，例如 AutoClicker、SteamCleaner，以及最引人注目的 **Notepad++**。

当用户下载并运行名为 **Setup.zip** 的文件时，他们得到的远不止一个文本编辑器。“通过 Setup.zip 分发的版本同时包含 \*\* 正版 Notepad++ 安装程序（Setup.exe）\*\* 和一个名为 **TextShaping.dll** 的恶意加载器 DLL。”

恶意软件使用 **DLL 侧加载（DLL side‑loading）** 技术来躲避检测。当受害者启动正版的 Notepad++ 安装程序时，它会无意中从同一文件夹加载恶意的 **TextShaping.dll**。

随后，该 DLL 会在内存中解密一个有效载荷，最终安装 **DPLoader**（一种下载器木马）。“一旦在 Windows 任务计划程序中注册，DPLoader 就会持久化执行，并从其 C&C 服务器获取指令。”

为了保持隐蔽，恶意软件还会主动篡改系统防御。“脚本会修改 Windows Defender 策略，包括添加排除路径、禁用安全通知，并阻止恶意软件样本提交。”

该活动的最终目的不是勒索或窃取数据，而是**牟利**。攻击者会安装 **代理软件（Proxyware）**，让受害者的网络连接被 “共享” 出去。

“代理劫持指的是在未经同意的情况下，在受害者机器上安装 Proxyware，从而让攻击者通过盗用受害者的网络带宽来赚钱。”

恶意软件会安装已知的代理软件，例如 **Infatica** 和 **DigitalPulse**。为了伪装得更逼真，Infatica 代理会被注册为名为 **“Microsoft Anti‑Malware Tool”** 的计划任务，让普通用户误以为它是一个合法的系统进程。

Larva-25012 还在不断升级攻击手段。ASEC 研究人员指出，攻击者 “正在积极更改技术以躲避检测 —— 例如将 Proxyware 注入 Windows 资源管理器进程，或使用基于 Python 的加载器”。

对用户来说，这是一个明确的提醒：

**从不明来源下载软件往往伴随着隐藏的代价 —— 这次，是你的网络带宽。**

本文翻译自securityonline [原文链接](https://securityonline.info/bandwidth-bandits-fake-notepad-installers-hide-proxyjacking-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314481](/post/id/314481)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/bandwidth-bandits-fake-notepad-installers-hide-proxyjacking-malware/)

如若转载,请注明出处： <https://securityonline.info/bandwidth-bandits-fake-notepad-installers-hide-proxyjacking-malware/>

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
* **950**

* 粉丝
* **6**

### TA的文章

* ##### [威胁行为者将Visual Studio Code武器化，部署多阶段恶意软件](/post/id/314458)

  2026-01-23 10:23:22
* ##### [遭野外利用：思科关键RCE漏洞（CVE-2026-20045）已被攻击](/post/id/314457)

  2026-01-23 10:22:51
* ##### [CVE-2025-13878：高严重性BIND漏洞可致服务器远程崩溃](/post/id/314469)

  2026-01-23 10:22:16
* ##### [攻击者滥用Discord传播剪贴板劫持程序，窃取粘贴操作中的钱包地址](/post/id/314467)

  2026-01-23 10:21:16
* ##### [带宽盗贼：伪造的Notepad++安装包暗藏 “代理劫持”恶意软件](/post/id/314481)

  2026-01-23 10:20:42

### 相关文章

* ##### [威胁行为者将Visual Studio Code武器化，部署多阶段恶意软件](/post/id/314458)

  2026-01-23 10:23:22
* ##### [遭野外利用：思科关键RCE漏洞（CVE-2026-20045）已被攻击](/post/id/314457)

  2026-01-23 10:22:51
* ##### [CVE-2025-13878：高严重性BIND漏洞可致服务器远程崩溃](/post/id/314469)

  2026-01-23 10:22:16
* ##### [攻击者滥用Discord传播剪贴板劫持程序，窃取粘贴操作中的钱包地址](/post/id/314467)

  2026-01-23 10:21:16
* ##### [蓝色起源推出太赫兹波卫星网络：6Tbps速率对标星链](/post/id/314480)

  2026-01-23 10:19:44
* ##### [勒索软件组织RansomHub攻击苹果供应商立讯精密，窃取1TB未发布产品数据](/post/id/314487)

  2026-01-23 10:19:09
* ##### [攻击者盯上飞塔刚修复的高危漏洞](/post/id/314490)

  2026-01-23 10:18:21

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