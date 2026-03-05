---
title: Windows错误报告服务ALPC权限提升漏洞PoC已公开
url: https://www.anquanke.com/post/id/314970
source: 安全客-有思想的安全新媒体
date: 2026-03-04
fetch_date: 2026-03-05T04:05:30.647914
---

# Windows错误报告服务ALPC权限提升漏洞PoC已公开

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

# Windows错误报告服务ALPC权限提升漏洞PoC已公开

阅读量**27427**

发布时间 : 2026-03-04 10:36:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Abinaya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/poc-windows-alpc-privilege-escalation/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

随着概念验证（PoC）利用代码公开，微软 Windows 系统中一处**关键本地权限提升（LPE）漏洞**随之曝光。

该漏洞编号为 **CVE-2026-20817**，存在于 **Windows 错误报告服务（WER）** 内部。

此漏洞可让**低权限已认证用户**执行任意恶意代码，并**获取完整 SYSTEM 系统权限**。

安全研究员 @oxfemale（X/Twitter 账号 @bytecodevm）已在 GitHub 上发布了详细研究内容及配套 **C++ PoC 利用代码**。

此次公开暴露出 Windows 面向进程间通信的错误报告机制中存在**重大安全隐患**。

漏洞核心涉及**高级本地过程调用（ALPC）协议**。

WER 服务对外开放了一个名为 **\WindowsErrorReportingService** 的 ALPC 端口，用于与其他进程通信。

根据研究员分析，漏洞具体存在于 **SvcElevatedLaunch 方法**，对应方法号为 **0x0D**。

该服务**未对调用用户的权限进行任何有效校验**。

![]()

因此，攻击者可通过共享内存传入自定义命令行参数，强制服务启动 `WerFault.exe`。

## 漏洞利用执行步骤

攻击者只需执行以下简单步骤即可成功触发漏洞：

| 操作 | 说明 |
| --- | --- |
| Create Shared Memory | 创建共享内存块，并在其中写入构造好的恶意命令行 |
| Connect to WER ALPC Port | 本地连接至 Windows 错误报告服务（WER）的 ALPC 端口 |
| Send ALPC Message (Method 0x0D) | 使用**方法 0x0D**发送 ALPC 消息，携带客户端进程 ID、共享内存句柄及命令行长度 |
| Trigger Command Execution | WER 服务复制句柄，并使用传入的命令行启动 `WerFault.exe` |

由于 WER 服务以**高权限**运行，新建进程会**继承 SYSTEM 令牌**。

该令牌包含多项高危权限，例如：

**SeDebugPrivilege**（可调试任意进程）和 **SeImpersonatePrivilege**（可模拟任意用户）。

尽管该令牌不包含操作系统核心级别的 SeTcbPrivilege，但获取到的权限已足以**实现对系统的完全控制**。

该漏洞影响范围极广，包括：

2026 年 1 月之前的所有 **Windows 10、Windows 11** 版本，

以及运行 **Windows Server 2019、Windows Server 2022** 的企业服务器环境。

微软已在**2026 年 1 月安全更新**中正式修复此漏洞。

鉴于 GitHub 已公开 PoC，强烈建议企业与系统管理员**立即安装最新安全补丁**，保障网络安全。

安全团队还应监控环境中是否出现**异常的 WerFault.exe 子进程**与**不规范的 SYSTEM 令牌行为**，以发现潜在的漏洞利用行为。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/poc-windows-alpc-privilege-escalation/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314970](/post/id/314970)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/poc-windows-alpc-privilege-escalation/)

如若转载,请注明出处： <https://cybersecuritynews.com/poc-windows-alpc-privilege-escalation/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [AuraStealer信息窃密木马活跃传播，攻击者依托48个C2域名持续攻击用户](/post/id/314998)

  2026-03-04 10:33:55

### 热门推荐

文章目录

* [漏洞利用执行步骤](#h2-0)

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