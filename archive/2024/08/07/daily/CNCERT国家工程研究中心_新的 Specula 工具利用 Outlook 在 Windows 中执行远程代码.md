---
title: 新的 Specula 工具利用 Outlook 在 Windows 中执行远程代码
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546220&idx=1&sn=631a681f19ec633cff4f667a3dd377a8&chksm=fa9383adcde40abba1edee4a843e61b2fb34362595ce8a089c3c26cfcb3e3f1c0fac41150409&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-07
fetch_date: 2025-10-06T18:04:48.538287
---

# 新的 Specula 工具利用 Outlook 在 Windows 中执行远程代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lsPeECN1yxChvqJWdrXMNPThvh2qa2lGCeMd713pIUib7HmIQvjfcHbNW9VTuWcALgzKYfkkLgseg/0?wx_fmt=jpeg)

# 新的 Specula 工具利用 Outlook 在 Windows 中执行远程代码

网络安全应急技术国家工程中心

Microsoft Outlook 可变成 C2 信标来远程执行代码，网络安全公司 TrustedSec 本周发布的全新红队后利用框架“Specula”就证明了这一点。

该 C2 框架通过利用 CVE-2017-11774（2017 年 10 月修补的 Outlook 安全功能绕过漏洞）使用 WebView 创建自定义 Outlook 主页。

微软表示：“在文件共享攻击场景中，攻击者可以提供专门为利用该漏洞而设计的文档文件，然后诱使用户打开该文档文件并与文档进行交互。”

然而，即使微软修补了该漏洞并删除了显示 Outlook 主页的用户界面，攻击者仍然可以使用 Windows 注册表值创建恶意主页，即使在安装了最新 Office 365 版本的系统上也是如此。

正如 Trusted 所解释的那样，Specula 纯粹在 Outlook 环境中运行，其工作原理是通过调用交互式 Python Web 服务器的注册表项设置自定义 Outlook 主页。

为此，非特权威胁者可以在 HKEY\_CURRENT\_USER\Software\Microsoft\Office\16.0\Outlook\WebView\ 下的 Outlook WebView 注册表项中将 URL 目标设置为他们控制的外部网站。

# **Outlook Specula 注册表值**

攻击者控制的 Outlook 主页旨在提供自定义 VBscript 文件，攻击者可使用该文件在受感染的 Windows 系统上执行任意命令。

TrustedSec 表示：“尽管目前已有相关知识和预防措施，但 TrustedSec 仍能够利用这一特定渠道对数百个客户端进行初始访问。当通过 Microsoft 在其解决方法中列出的任何注册表项设置自定义主页时，Outlook 将在选择相关选项卡时下载并显示该 HTML 页面，而不是显示正常的邮箱元素（收件箱、日历、已发送等）。

从下载的 HTML 页面，可以在特权上下文中运行 vbscript 或 jscript，或多或少可以完全访问本地系统，就像运行 cscript / wscript.exe 一样。

虽然首先需要入侵设备才能配置 Outlook 注册表项，但一旦配置完成，攻击者就可以使用此技术实现持久性并横向传播到其他系统。

由于 outlook.exe 是一个受信任的进程，因此攻击者在执行命令时可以更轻松地逃避现有软件。

正如美国网络司令部（US CyberCom）五年前警告的那样，CVE-2017-11774 Outlook 漏洞也被用来攻击美国政府机构。

Chronicle、FireEye 和 Palo Alto Networks 的安全研究人员后来将这些攻击与伊朗支持的 APT33 网络间谍组织联系起来。

FireEye 网络安全研究人员表示，FireEye 于 2018 年 6 月首次观察到 APT34 使用 CVE-2017-11774，随后 APT33 从 2018 年 7 月开始采用该漏洞进行范围更广的攻击活动，并持续了至少一年。

**参考及来源：**
https://www.bleepingcomputer.com/news/security/new-specula-tool-uses-outlook-for-remote-code-execution-in-windows/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过