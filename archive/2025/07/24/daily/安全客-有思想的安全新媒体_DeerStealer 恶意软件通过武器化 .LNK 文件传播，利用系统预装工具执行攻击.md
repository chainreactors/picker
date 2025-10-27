---
title: DeerStealer 恶意软件通过武器化 .LNK 文件传播，利用系统预装工具执行攻击
url: https://www.anquanke.com/post/id/310427
source: 安全客-有思想的安全新媒体
date: 2025-07-24
fetch_date: 2025-10-06T23:16:50.817695
---

# DeerStealer 恶意软件通过武器化 .LNK 文件传播，利用系统预装工具执行攻击

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

# DeerStealer 恶意软件通过武器化 .LNK 文件传播，利用系统预装工具执行攻击

阅读量**63180**

发布时间 : 2025-07-23 17:18:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/deerstealer-malware-delivered/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一项新型高级网络钓鱼活动近期曝光，攻击者通过武器化的 .LNK 快捷方式文件传播 DeerStealer 恶意软件，利用 Windows 系统中的合法预装工具实施“借力攻击”（Living off the Land，LOLBin）技术。

此次攻击中，恶意软件伪装成名为“Report.lnk”的 PDF 文件，背后则隐藏着一个多阶段的复杂攻击链条，核心在于调用 Microsoft 的 HTML 应用程序宿主工具 **mshta.exe** 来执行恶意代码。

![]()

该攻击手法标志着恶意软件传播机制的显著升级，攻击者利用微软自身工具绕过传统安全防御机制。恶意 .LNK 文件会启动精心设计的执行序列，逐步调用多个系统组件，最终部署 DeerStealer 木马。

该策略利用了安全系统对操作系统合法组件的信任，从而显著提升检测难度。

## 恶意利用系统组件绕过防护

据 LinkedIn 的安全分析师和研究人员指出，该攻击活动采用了极为隐蔽的规避技术，滥用 MITRE ATT&CK 框架中的 **T1218.005 技术** —— 即对 mshta.exe 的恶意使用。

研究人员强调，攻击中使用的动态路径解析与混淆命令执行技术，体现出恶意软件技术水平的新高度。

## 执行链条与感染机制

DeerStealer 的感染流程由以下五个阶段组成：
`.lnk → mshta.exe → cmd.exe → PowerShell → DeerStealer`

初始的 .LNK 文件会秘密调用 **mshta.exe**，执行高度混淆的脚本，并采用通配路径绕过基于特征码的检测系统。恶意代码会动态解析 **System32** 目录下 mshta.exe 的完整路径，并以特定参数启动该工具，接着加载混淆的 Base64 编码字符串。

为了规避取证分析，该脚本会关闭日志记录与行为分析功能，极大降低了可见性。

脚本内部采用复杂的字符解码机制：以十六进制为单位解析字符对，转换为 ASCII 字符，再通过 PowerShell 的 `IEX（Invoke-Expression）` 命令动态拼接并执行真正的恶意逻辑。

## 最终载荷与持久化

最终载荷通过解码后的 URL 数组实现动态解析，同时下载一个诱饵 PDF 文件用于分散用户注意力，并将主恶意程序静默安装至 **AppData** 目录。

PDF 文件将通过 Adobe Acrobat 正常打开，作为烟雾弹吸引用户注意，实际则在后台悄然建立持久化机制。

## 已知威胁指标（IOCs）

* **恶意域名：** `tripplefury.com`
* **已知样本 SHA256：**

  + `fd5a2f9eed065c5767d5323b8dd928ef8724ea2edeba3e4c83e211edf9ff0160`
  + `8f49254064d534459b7ec60bf4e21f75284fbabfaea511268c478e15f1ed0db9`

建议加强对 `.lnk` 文件的监控，限制 mshta.exe、PowerShell 的使用权限，部署现代化 EDR 系统以检测多阶段攻击行为，以及结合已知 IOC 进行威胁狩猎。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/deerstealer-malware-delivered/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310427](/post/id/310427)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/deerstealer-malware-delivered/)

如若转载,请注明出处： <https://cybersecuritynews.com/deerstealer-malware-delivered/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [恶意利用系统组件绕过防护](#h2-0)
* [执行链条与感染机制](#h2-1)
* [最终载荷与持久化](#h2-2)
* [已知威胁指标（IOCs）](#h2-3)

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