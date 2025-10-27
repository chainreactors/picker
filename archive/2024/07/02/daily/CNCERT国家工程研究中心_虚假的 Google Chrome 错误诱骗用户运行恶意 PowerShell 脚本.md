---
title: 虚假的 Google Chrome 错误诱骗用户运行恶意 PowerShell 脚本
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545625&idx=2&sn=b08ed1dce1f542d7b53a3ac6a9988a4e&chksm=fa9385d8cde40cced0fccd76bc01c08e37a2756a6b94b80bbbe09d0d9831a70f45e027c40973&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-02
fetch_date: 2025-10-06T17:46:10.959153
---

# 虚假的 Google Chrome 错误诱骗用户运行恶意 PowerShell 脚本

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mlNmz3HQFvICQ5AQ1940wYAEJcxoS0hibw7Zy56wuMicCicwSnicaZd2ePiaP3mhJ5ib0iacibVIUricGe0Bw/0?wx_fmt=jpeg)

# 虚假的 Google Chrome 错误诱骗用户运行恶意 PowerShell 脚本

网络安全应急技术国家工程中心

一项新的恶意软件分发活动正使用虚假的 Google Chrome、Word 和 OneDrive 错误诱骗用户运行安装恶意软件的恶意 PowerShell“修复程序”。

据观察，这项新活动被多个恶意分子使用，包括 ClearFake 背后的恶意分子、一个名为 ClickFix 的新攻击集群，以及 TA571 威胁者，后者以垃圾邮件分发者的身份运作，发送大量电子邮件，导致恶意软件和勒索软件感染。

此前的 ClearFake 攻击利用网站覆盖层，提示访问者安装虚假的浏览器更新，进而安装恶意软件。

威胁者还在新的攻击中使用 HTML 附件和受感染网站中的 JavaScript。但是，现在覆盖层会显示虚假的Google Chrome、Microsoft Word 和 OneDrive 错误。这些错误会提示访问者单击按钮将 PowerShell“修复”复制到剪贴板，然后在“运行：”对话框或 PowerShell 提示符中粘贴并运行它。

ProofPoint 的一份新报告称：“尽管攻击链需要大量用户交互才能成功，但社会工程学可以同时向人们呈现看似真实的问题和解决方案，这可能会促使用户在不考虑风险的情况下采取行动。”

Proofpoint 发现的有效载荷包括DarkGate、Matanbuchus、NetSupport、Amadey Loader、XMRig、剪贴板劫持程序和 Lumma Stealer。

# **PowerShell“修复”导致恶意软件**

Proofpoint 分析师观察到三条攻击链，它们的区别主要在于初始阶段，只有第一条攻击链不能高度可信地归因于 TA571。

在第一个案例中，与 ClearFake 背后的恶意分子有关，用户访问一个受感染的网站，该网站通过币安的智能链合约加载托管在区块链上的恶意脚本。

该脚本执行一些检查并显示虚假的 Google Chrome 警告，指出显示网页时出现问题。然后，对话框提示访问者通过将 PowerShell 脚本复制到 Windows 剪贴板并在 Windows PowerShell（管理）控制台中运行该脚本来安装“根证书”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29k0QyM8MDJA52WZddU05HSLiaQK2ibzsmQo51FQ3X0ib2YhwMV5GDBIgib1QqIan75JMWXCZib2iaRiaAxw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

伪造的 Google Chrome 错误

当执行 PowerShell 脚本时，它将执行各种步骤来确认设备是有效目标，然后它将下载其他有效负载，如下所述：

·刷新 DNS 缓存；

·删除剪贴板内容；

·显示诱饵消息；

·下载另一个远程 PowerShell 脚本，该脚本在下载信息窃取程序之前执行反虚拟机检查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29k0QyM8MDJA52WZddU05HSyP1GiaItV6Wq6LleojibQ5KzjzldcQHQ9CB72L32nTNiaINaM29flqiahA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

“ClearFake”攻击链

第二条攻击链与“ClickFix”活动有关，它在受感染的网站上使用注入，创建一个 iframe 来覆盖另一个虚假的 Google Chrome 错误。用户被指示打开“Windows PowerShell（管理员）”并粘贴提供的代码，从而导致上述相同的感染。

最后，基于电子邮件的感染链使用类似于 Microsoft Word 文档的 HTML 附件，提示用户安装“Word Online”扩展程序才能正确查看文档。

错误消息提供“如何修复”和“自动修复”选项，其中“如何修复”将 base64 编码的 PowerShell 命令复制到剪贴板，指示用户将其粘贴到 PowerShell 中。

“自动修复”使用 search-ms 协议在远程攻击者控制的文件共享上显示 WebDAV 托管的“fix.msi”或“fix.vbs”文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29k0QyM8MDJA52WZddU05HSwH4npIa8DaZsCjFtj79SkYTSHgzvBhplpBu6IONWC7zWrgthbM6zjQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

伪造的 Microsoft Word 错误会导致恶意软件

在这种情况下，PowerShell 命令会下载并执行 MSI 文件或 VBS 脚本，从而分别导致 Matanbuchus 或 DarkGate 感染。

在所有情况下，恶意分子都利用了目标对在其系统上执行 PowerShell 命令的风险缺乏认识这一事实。他们还利用了 Windows 无法检测和阻止粘贴代码发起的恶意操作这一特点。

不同的攻击链都表明 TA571 正在积极尝试多种方法，以提高效率并寻找更多感染途径来入侵更多系统。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/fake-google-chrome-errors-trick-you-into-running-malicious-powershell-scripts/

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