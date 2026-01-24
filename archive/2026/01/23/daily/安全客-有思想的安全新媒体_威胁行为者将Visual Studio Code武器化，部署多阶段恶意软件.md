---
title: 威胁行为者将Visual Studio Code武器化，部署多阶段恶意软件
url: https://www.anquanke.com/post/id/314458
source: 安全客-有思想的安全新媒体
date: 2026-01-23
fetch_date: 2026-01-24T03:29:44.760004
---

# 威胁行为者将Visual Studio Code武器化，部署多阶段恶意软件

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

# 威胁行为者将Visual Studio Code武器化，部署多阶段恶意软件

阅读量**28549**

发布时间 : 2026-01-23 10:23:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/threat-actors-weaponizing-visual-studio-code/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

威胁行为者正将 Visual Studio Code 变为攻击平台，借助其完善的扩展生态系统，向开发者工作站植入**多阶段恶意软件**。

此次最新攻击活动被命名为伊夫林窃取程序，该恶意程序隐匿于一款恶意扩展中，通过数个精心设计的攻击阶段，向目标端投放一款具备隐秘性的信息窃取工具。

攻击者的目标并非普通终端用户，而是**开发者群体**—— 这类人群往往掌握着源代码、云控制台及加密货币资产的核心访问权限。

攻击从受害者安装一款伪装成实用或无害的**植毒 Visual Studio Code 扩展**开始，该扩展会在后台释放伪造的 Lightshot.dll 组件，随后这一组件会被正版截图工具 Lightshot.exe 加载运行。

此后恶意软件攻击链逐步展开，不仅会远程获取新的攻击载荷、执行隐藏的 PowerShell 命令，还会为最终实现大规模数据窃取的伊夫林窃取程序可执行文件搭建运行环境。

![]()

趋势科技分析师指出，攻击者将用户对**Visual Studio Code 应用市场的信任**当作可利用的武器，以恶意扩展为载体构建完整攻击链，实现从初始加载器启动到最终数据窃取的全流程攻击。

![]()

攻击者通过滥用 Lightshot 这类开发者常用工具，并采用仿签名的导出方式，让攻击第一阶段融入开发者的正常操作流程，同时在后台悄然为后续的入侵环节做准备。

伊夫林窃取程序完全执行后，会从受感染设备中窃取**浏览器密码、Cookie、加密货币钱包、即时通讯会话记录、VPN 配置文件、Wi-Fi 密钥及各类敏感文件**。

同时该程序还会捕获设备截图和详细的系统信息，将所有数据压缩为单个压缩包后，上传至攻击者控制的 FTP 服务器。

对企业而言，仅一台开发者笔记本电脑被感染，就可能导致**源代码、云访问令牌及生产环境凭证**泄露，让一次工具链的使用疏漏，演变为波及范围广泛的安全入侵事件。

### 多阶段感染链的技术细节

攻击的第一阶段隐藏在恶意 Visual Studio Code 扩展内，伪装为 Lightshot.dll 文件，每当用户进行截图操作时，该文件就会被 Lightshot.exe 调用执行。

![]()

该下载器被触发后，会执行一条**隐藏的 PowerShell 命令**，从远程域名拉取名为 iknowyou.model 的第二阶段攻击文件，将其另存为 runtime.exe 并运行。

伊夫林窃取程序的攻击载荷会在设备中创建**AppData\Evelyn 文件夹**，向 Edge 和 Chrome 浏览器注入 abe\_decrypt.dll 文件，最终将窃取的数据打包为 ZIP 压缩包，通过 FTP 协议完成上传。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/threat-actors-weaponizing-visual-studio-code/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314458](/post/id/314458)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/threat-actors-weaponizing-visual-studio-code/)

如若转载,请注明出处： <https://cybersecuritynews.com/threat-actors-weaponizing-visual-studio-code/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [遭野外利用：思科关键RCE漏洞（CVE-2026-20045）已被攻击](/post/id/314457)

  2026-01-23 10:22:51
* ##### [CVE-2025-13878：高严重性BIND漏洞可致服务器远程崩溃](/post/id/314469)

  2026-01-23 10:22:16
* ##### [攻击者滥用Discord传播剪贴板劫持程序，窃取粘贴操作中的钱包地址](/post/id/314467)

  2026-01-23 10:21:16
* ##### [带宽盗贼：伪造的Notepad++安装包暗藏 “代理劫持”恶意软件](/post/id/314481)

  2026-01-23 10:20:42
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