---
title: Metasploit针对Linux RC4漏洞、BeyondTrust及注册表持久化攻击新增模块
url: https://www.anquanke.com/post/id/314945
source: 安全客-有思想的安全新媒体
date: 2026-03-03
fetch_date: 2026-03-04T04:02:09.790404
---

# Metasploit针对Linux RC4漏洞、BeyondTrust及注册表持久化攻击新增模块

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

# Metasploit针对Linux RC4漏洞、BeyondTrust及注册表持久化攻击新增模块

阅读量**16277**

发布时间 : 2026-03-03 09:59:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Dhivya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/metasploit-adds-new-modules-targeting-linux-rc4/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Metasploit 于 2026 年 2 月 27 日发布的最新版本，为安全从业者与渗透测试人员带来了**强大的新功能支持**。

本次更新新增 7 个模块、9 项功能增强，并修复了多项高危漏洞。

其中亮点模块包括：针对 Ollama、BeyondTrust 及潮流网络（Grandstream）VoIP 设备的**未授权远程代码执行（RCE）漏洞利用工具**，以及面向 Linux 环境的高级规避技术模块。

### 高危远程代码执行漏洞利用工具

本次更新提供了针对企业级及人工智能基础设施中**高危漏洞的完整攻击链利用工具**。

1. **Ollama 模型注册表路径遍历漏洞（CVE-2024-37032）**：

   该漏洞 CVSS 评分 8.8，攻击者可利用路径遍历序列劫持 Ollama 的拉取（pull）机制。

   该模块通过加载恶意 OCI 注册表，将恶意共享对象文件写入目标设备；强制 Ollama 生成新进程后，恶意库会被加载，最终实现**未授权的 root 级远程代码执行**。
2. **BeyondTrust PRA 与 RS 命令注入漏洞（CVE-2026-1731）**：

   该高危漏洞 CVSS 评分 9.9，可在 BeyondTrust 特权远程访问（PRA）与远程支持（RS）设备中实现**未授权命令注入**。

   本次更新还新增了 BeyondTrust 辅助库，以简化后续模块的开发流程。
3. **潮流网络 GXP1600 栈溢出漏洞（CVE-2026-2329）**：

   该漏洞针对 VoIP 设备，CVSS 评分 9.3，攻击者可通过该漏洞获取**root 权限会话**。

   Rapid7 本次发布包含 1 个漏洞利用模块和 2 个后渗透模块，可利用该权限窃取凭证，并代理 SIP 流量以实现数据包捕获。

本次更新的另一大亮点是**首个面向 ARM64 架构的 Linux 规避模块**。

该 Linux RC4 打包器（Linux RC4 Packer）采用 RC4 加密算法，可在内存中直接执行 ELF 二进制文件，并通过休眠规避技术（sleep evasion）**绕过检测机制**。

此外，更新还新增了面向 Windows 及 Windows 子系统 Linux（WSL）的持久化模块：

* WSL 模块会将载荷写入用户启动文件夹；
* Windows 注册表 Active Setup 模块则通过系统原生功能启动载荷，但会将权限降级至用户级别，且**每个用户配置文件仅执行一次**。

### 核心功能增强与漏洞修复

经典漏洞模块迎来了大幅体验优化：

* Unreal IRCd 与 vsftpd 后门模块新增了更完善的检测方法、原生 Meterpreter 载荷，并支持详细的故障排查输出；
* SolarWinds 漏洞利用工具优化为可自动选择正确的 SRVHOST 值；
* MS17-010 扫描器新增检测方法，提升了自动化元数据处理能力。

此外，执行文件被拆分重构，可更精细化地适配不同平台与架构。

最后，本次更新修复了 LDAP ESC 扫描器与 GraphQL 自省（Introspection）扫描器的崩溃问题与误报问题。

### 补充说明

* **CVSS**：通用漏洞评分系统（行业标准，分数越高漏洞风险越高）
* **Meterpreter**：Metasploit 核心渗透载荷，支持交互式控制目标设备
* **ELF**：Linux 系统标准可执行文件格式
* **Active Setup**：Windows 注册表项，用于实现程序开机自启

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/metasploit-adds-new-modules-targeting-linux-rc4/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314945](/post/id/314945)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/metasploit-adds-new-modules-targeting-linux-rc4/)

如若转载,请注明出处： <https://cybersecuritynews.com/metasploit-adds-new-modules-targeting-linux-rc4/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1050**

* 粉丝
* **6**

### TA的文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26

### 相关文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26
* ##### [Anthropic推出记忆导入功能，助力QuitGPT浪潮下用户迁移对话数据](/post/id/314990)

  2026-03-04 10:34:57
* ##### [Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风](/post/id/314994)

  2026-03-04 10:34:28

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