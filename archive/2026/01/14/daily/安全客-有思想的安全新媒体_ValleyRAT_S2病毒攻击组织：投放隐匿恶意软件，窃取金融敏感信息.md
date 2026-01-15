---
title: ValleyRAT_S2病毒攻击组织：投放隐匿恶意软件，窃取金融敏感信息
url: https://www.anquanke.com/post/id/314334
source: 安全客-有思想的安全新媒体
date: 2026-01-14
fetch_date: 2026-01-15T03:28:07.624733
---

# ValleyRAT_S2病毒攻击组织：投放隐匿恶意软件，窃取金融敏感信息

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

# ValleyRAT\_S2病毒攻击组织：投放隐匿恶意软件，窃取金融敏感信息

阅读量**16473**

发布时间 : 2026-01-14 12:59:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/valleyrat_s2-attacking-organizations/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

新一轮网络攻击正借助**ValleyRAT\_S2 恶意软件**悄然入侵各类组织机构，该病毒可实现长期潜伏，并窃取目标机构的敏感金融数据。

ValleyRAT\_S2 是 ValleyRAT 恶意软件家族的**第二阶段载荷**，基于 C++ 语言开发。一旦侵入目标网络，它就会以完整远程访问木马（RAT）的形态运行，让攻击者获得对受感染系统的高度控制权，同时搭建起稳定的数据外传通道。

当前，该攻击活动的主要传播途径为**伪造的中文办公软件、破解版程序**，以及伪装成人工智能表格生成工具的植马安装包。

在诸多攻击案例中，恶意软件会通过**DLL 侧载技术**实现植入：攻击者诱导一个带有合法数字签名的应用程序，加载看似正常的恶意动态链接库文件，例如命名为`steam_api64.dll`的恶意模块。

网络安全团队 APOPHiS 通过追踪多起相关攻击事件，确认**ValleyRAT\_S2 是此类入侵活动的核心第二阶段后门程序**。

除此之外，该恶意软件还会通过鱼叉式钓鱼邮件附件，以及被劫持的软件更新渠道进行传播。

恶意文档或压缩包会将载荷文件释放至系统临时文件夹等路径，例如：

`C:\Users\Admin\AppData\Local\Temp\AI自动化办公表格制作生成工具安装包\steam_api64.dll`

攻击的第一阶段以躲避安全检测为核心目标，而 ValleyRAT\_S2 则会接管后续操作，负责**长期驻留控制、系统信息探查、凭证窃取及金融数据收集**等关键任务。

**![]()**

ValleyRAT\_S2 激活后，会对系统进程、文件系统及注册表项展开扫描，随后通过自定义 TCP 协议，连接预先写入代码的命令与控制（C&C）服务器，例如`27.124.3.175:14852`。该病毒具备文件上传下载、执行 Shell 命令、注入恶意载荷、记录键盘输入等多种功能，

这些特性使其能够精准窃取网银账户凭证、支付交易数据及内部财务文档。

### **持久化机制与监控守护功能**

ValleyRAT\_S2 的一大高危特性，是其**多层级持久化设计与监控守护机制**，这让它能够在系统重启或手动清理后依然存活。

恶意软件会先将相关文件释放到用户的临时文件夹（Temp）和应用数据文件夹（AppData）中，创建`%TEMP%\target.pid`这类进程标识文件，同时在`%APPDATA%\Promotions\Temp.aps`路径下生成配置文件。

它还会利用 COM 接口调用 Windows 任务计划程序，实现开机自启动；同时会在注册表启动项中写入备份路径，作为双重保障。

**![]()**

该病毒的一个关键特征是会生成一个名为`monitor.bat`的批处理脚本，以此构建监控守护循环。

这个脚本会从`target.pid`文件中读取恶意主程序的进程 ID，持续检查主程序是否处于运行状态，一旦发现主程序被终止，就会自动静默重启。

以下是该脚本的简化版本：

```
@echo off
set "PIDFile=%TEMP%\target.pid"
set /p pid=<"%PIDFile%"
del "%PIDFile%"
:check
tasklist /fi "PID eq %pid%" | findstr >nul
if errorlevel 1 (
  cscript //nologo "%TEMP%\watch.vbs"
  exit
)
timeout /t 15 >nul
goto check
```

这一守护循环，能让 ValleyRAT\_S2 在主进程被安全工具或管理员终止后快速恢复。此外，该恶意软件还结合了**结构化异常处理、沙箱环境检测**，以及进程注入技术 —— 将自身注入`Telegra.exe`、`WhatsApp.exe`等具有可信名称的进程中，以此实现隐蔽且稳固的持久化驻留。

对于防御方而言，这意味着**单纯终止恶意进程无法实现彻底清除**；想要根除该病毒，必须同时针对计划任务、批处理与 VBS 监控脚本、释放的恶意文件及后门进程等所有相关组件，开展一体化清除操作。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/valleyrat_s2-attacking-organizations/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314334](/post/id/314334)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/valleyrat_s2-attacking-organizations/)

如若转载,请注明出处： <https://cybersecuritynews.com/valleyrat_s2-attacking-organizations/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **920**

* 粉丝
* **6**

### TA的文章

* ##### [双重严重：Ruckus IoT控制器因硬编码密钥泄露面临root权限远程代码执行](/post/id/314315)

  2026-01-14 13:01:25
* ##### [攻击者借助伪造PDF将合法远程监控管理工具武器化](/post/id/314309)

  2026-01-14 13:01:19
* ##### [蜜罐陷阱(HoneyTrap)——抵御越狱攻击的全新大语言模型防御框架](/post/id/314328)

  2026-01-14 13:00:52
* ##### [高危漏洞CVE-2025-52694：研华设备存在 SQL 注入，可导致 IoT设备被完全攻陷](/post/id/314324)

  2026-01-14 13:00:38
* ##### [n8n供应链攻击：滥用社区节点窃取OAuth令牌](/post/id/314316)

  2026-01-14 13:00:22

### 相关文章

* ##### [双重严重：Ruckus IoT控制器因硬编码密钥泄露面临root权限远程代码执行](/post/id/314315)

  2026-01-14 13:01:25
* ##### [攻击者借助伪造PDF将合法远程监控管理工具武器化](/post/id/314309)

  2026-01-14 13:01:19
* ##### [蜜罐陷阱(HoneyTrap)——抵御越狱攻击的全新大语言模型防御框架](/post/id/314328)

  2026-01-14 13:00:52
* ##### [高危漏洞CVE-2025-52694：研华设备存在 SQL 注入，可导致 IoT设备被完全攻陷](/post/id/314324)

  2026-01-14 13:00:38
* ##### [n8n供应链攻击：滥用社区节点窃取OAuth令牌](/post/id/314316)

  2026-01-14 13:00:22
* ##### [高危警报：Moxa交换机存在OpenSSH远程代码执行漏洞（CVSS 9.8）](/post/id/314327)

  2026-01-14 12:59:46
* ##### [苹果确认谷歌 Gemini 将为 Siri 提供技术支持，强调隐私仍是核心优先级](/post/id/314310)

  2026-01-14 12:58:29

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