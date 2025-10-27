---
title: Windows 修复漏洞遭利用，推送恶意脚本
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247544704&idx=3&sn=a6156d6b4aefa04de16dcdaed046d91b&chksm=c1e9a3d1f69e2ac75a6c20168062423c9fb229c9130cc03d103ee9da4752ca51c54d63eb7f1d&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-03
fetch_date: 2025-10-06T17:43:34.584090
---

# Windows 修复漏洞遭利用，推送恶意脚本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogt6dnKwtVIc9Fw9fGEAnkrQ9g3gRjm4UTEa0WlJKR6rZPIraLp2cPXRxZVH3M7Gobudw6LJHtn4OA/0?wx_fmt=jpeg)

# Windows 修复漏洞遭利用，推送恶意脚本

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogt6dnKwtVIc9Fw9fGEAnkrQ3385u9Jt7icAYQ9yrCMASrO6S9diaTX9lNVB4aL1n9cvjdfRzSZIwjyw/640?wx_fmt=png&from=appmsg)

虚假的 IT 支持网站宣传针对常见 Windows 错误（如 0x80070643 错误）的恶意 PowerShell“修复”，以使用窃取信息的恶意软件感染设备。

这些虚假支持网站首先由 eSentire 的威胁响应部门 (TRU) 发现，它们通过已被入侵和劫持的 YouTube 频道进行推广，以增加内容创建者的合法性。

具体来说，威胁行为者正在制作虚假视频，宣传修复自一月份以来数百万 Windows 用户一直在处理的 0x80070643 错误。

在 2024 年 1 月补丁星期二期间，微软发布了安全更新以修复 BitLocker 加密绕过漏洞，该漏洞被追踪为 CVE-2024-20666。

安装更新后，全球的 Windows 用户报告称，在尝试安装更新时收到“0x80070643 - ERROR\_INSTALL\_FAILURE”，无论他们如何努力，该错误都不会消失。

“安装更新时出现一些问题，但我们稍后会再试。如果您继续看到此信息并想在网上搜索或联系支持人员获取信息，这可能会有所帮助：（0x80070643）”，Windows 更新错误显示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6x7ziaricJ0oftwzMpjsLkLFK5xHMOMXjvGP7rPNGsAQcZjycIYQU3JYgCJ0oiafjYBpjQbaOtQkA7Zw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Windows 更新中的 0x80070643

事实证明，Windows Update 显示了不正确的错误消息，因为它应该在 Windows 恢复环境 (WinRE) 分区太小而无法安装更新的系统上显示 CBS\_E\_INSUFFICIENT\_DISK\_SPACE 错误。

微软解释称，新的安全更新要求 WinRE 分区有 250MB 的可用空间，如果没有，则必须自行手动扩展该分区。

但是，对于那些 WinRE 不是驱动器上的最后一个分区的人来说，扩展 WinRE 分区很复杂，甚至是不可能的。

因此，许多人无法安装安全更新，并且每次使用 Windows 更新时都会出现 0x80070643 错误消息。

这些错误导致许多沮丧的 Windows 用户在线寻求解决方案，从而让威胁行为者得以利用他们寻找解决方案的机会。

**虚假 IT 网站宣传 PowerShell 修复程序**

据 eSentire 称，威胁行为者正在创建许多虚假的 IT 支持网站，这些网站专门用于帮助用户解决常见的 Windows 错误，重点关注 0x80070643 错误。

eSentire 报告解释道：“2024 年 6 月，eSentire 的 威胁响应部门 (TRU)观察到一个有趣的案例，涉及通过虚假 IT 支持网站发起的 Vidar Stealer 感染（图 1）。”

“当受害者在网上搜索 Windows 更新错误代码的解决方案时，感染就开始了。”

研究人员在 YouTube 上发现了两个虚假的 IT 支持网站，名为 pchelprwizzards[.]com 和 pchelprwizardsguide[.]com、pchelprwizardpro[.]com、pchelperwizard[.]com 和 fixedguides[.]com 等网站。

就像 eSentire 为 PCHelperWizard 拼写错误网站找到的其他视频一样，研究人员还在 FixedGuides 网站上找到了 YouTube 视频，同样宣传了针对 0x80070643 错误的修复。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6x7ziaricJ0oftwzMpjsLkLFKaqP5kIGAwFrGVN2DInDdwTSSkicnll83IPSBLGjHvzALQxswoMic809A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

YouTube 上宣传的虚假 IT 支持网站

这些网站都提供了修复方法，要么要求您复制并运行 PowerShell 脚本，要么导入 Windows 注册表文件的内容。

无论使用哪种“解决方案”，都会执行一个 PowerShell 脚本，在设备上下载恶意软件。

eSentire 的报告概述了 PCHelperWizard 网站（不要与合法课程网站混淆）如何引导用户将 PowerShell 脚本复制到 Windows 剪贴板并在 PowerShell 提示符中执行它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6x7ziaricJ0oftwzMpjsLkLFKx35mtKPaK8ic0fwCQAiaY7RMOnFT5fgcictxm1OIUgjYeLpib9X1oRYDPg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

伪装成 Windows 错误修复程序的恶意 PowerShell 脚本

该 PowerShell 脚本包含一个 Base64 编码的脚本，它将连接到远程服务器以下载另一个 PowerShell 脚本，该脚本会在设备上安装 Vidar 信息窃取恶意软件。

脚本完成后，它会显示修复成功的消息并重新启动计算机，同时还会启动恶意软件。

FixedGuides 网站的做法略有不同，它使用混淆的 Windows 注册表文件来隐藏启动恶意 PowerShell 脚本的自动启动程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6x7ziaricJ0oftwzMpjsLkLFKjufy65slmYySTIRpuOY9fhq0uJa15SjG5EO8iawuicEGPajYbhSC33Ig/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

混淆的 Windows 注册表文件

但是，当从上述文件中提取字符串时，您可以看到它包含一个有效的注册表文件，该文件添加了运行 PowerShell 脚本的 Windows 自动启动 (RunOnce) 条目。该脚本最终会在计算机上下载并安装窃取信息的恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6x7ziaricJ0oftwzMpjsLkLFKXAdzNRhoMjd5FxVnrPGVdVTB6nQibebUXqZ3Y4PoJOBibT2qoacAGUvQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

未混淆的 Windows 注册表文件

使用任何虚假修复都会导致在 Windows 重新启动后启动窃取信息的恶意软件。一旦启动，恶意软件将从您的浏览器中提取已保存的凭据、信用卡、cookie 和浏览历史记录。

Vidar 还可以窃取加密货币钱包、文本文件和 Authy 2FA 身份验证器数据库，以及截取您的桌面屏幕截图。

这些数据被汇编成一个名为“日志”的档案，然后上传到攻击者的服务器。被盗数据随后被用来发动其他攻击，例如勒索软件攻击，或在暗网市场上出售给其他威胁行为者。

然而，受感染的用户现在面临一场噩梦，他们的所有帐户均被盗用，并可能遭受金融欺诈。

虽然 Windows 错误可能令人烦恼，但至关重要的是只从可信赖的网站下载软件和修复程序，而不是从随机视频和信誉不佳或没有信誉的网站下载。

您的凭证已经成为一种宝贵的商品，而威胁行为者正在想出各种狡猾且有创意的方法来窃取它们，因此不幸的是，每个人都需要对不寻常的攻击方法保持警惕。

至于 0x80070643 错误，如果您无法调整 WinRE 分区的大小，最好的办法是使用Microsoft 的显示或隐藏工具来隐藏 KB5034441 更新，以便 Windows Update 不再在您的系统上提供它，并且不会在 Internet 上搜索神奇的修复方法。

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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