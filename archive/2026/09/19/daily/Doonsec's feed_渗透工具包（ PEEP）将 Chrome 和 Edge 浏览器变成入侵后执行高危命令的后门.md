---
title: 渗透工具包（ PEEP）将 Chrome 和 Edge 浏览器变成入侵后执行高危命令的后门
url: https://mp.weixin.qq.com/s/-NIB_ogIamwt-z1nBUpFSA
source: Doonsec's feed
date: 2026-09-19
fetch_date: 2026-09-20T07:14:44.206741
---

# 渗透工具包（ PEEP）将 Chrome 和 Edge 浏览器变成入侵后执行高危命令的后门

# 渗透工具包（ PEEP）将 Chrome 和 Edge 浏览器变成入侵后执行高危命令的后门

Rhinoer
Rhinoer

犀牛安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/vO1zY1O9p8JjsA5xG2F4TTMXmKMzRZiaDFicwUOEMbYTHwUqhVqV0PnyDKRnnsDyBX4y4ev9Bt4h10IXvOh4bzcAanjHvmMDUDu8BLVrEUe00/640?wx_fmt=png&from=appmsg)

**网络安全研究人员披露了一款名为PEEP**的基于 Chromium 的后渗透工具包的详细信息，该工具包伪装成网络浏览器的书签扩展程序。

SOCRadar指出： “该扩展程序需要事先获得管理员权限或代码执行权限，其安装程序会将扩展程序直接注入 Chrome/Edge 用户配置文件，通过伪造 Chromium 自身的安全首选项完整性值来绕过网上应用商店的检查和用户提示。然后，一个原生消息传递工具会将功能从浏览器遥测扩展到主机级命令执行和文件管理。”

安装完成后，PEEP“扩展”代理程序会每30秒通过明文HTTP协议轮询其命令与控制（C2）服务器（“206.237.30[.]232”或“ xfjcc[.]fun ”）以获取新命令，同时窃取浏览历史记录、活动标签页元数据和会话cookie。它还可用作远程访问和浏览器监控工具包，执行主机命令、窃取凭据、劫持会话并篡改网页。

PEEP 基于RedExt构建，RedExt 是一个开源的浏览器数据分析和红队演练框架，此前也曾用于 GlassWorm 攻击。然而，PEEP 在 RedExt 的基础上进行了扩展，提供了专用的安装程序、原生主机桥接、心跳遥测、更新通道以及更丰富的命令集。因此，PEEP 可以说是 RedExt 的一个衍生版本。

PEEP 被描述为一种入侵后攻击框架，因为它本身缺乏初始访问途径，这意味着攻击者需要通过其他方式入侵目标机器并部署恶意软件。尽管源代码中存在中文痕迹，表明攻击者可能讲中文，但此次攻击活动的具体来源仍未确定。

该扩展程序伪装成“智能书签”（ID：ejkndncpkdcjcikfhiamcdehdoegilbj）。它是负责执行信标循环的主要代理，其方式是轮询“/api/commands”、收集浏览器数据、接收额外任务并将结果发送回服务器。

当需要访问操作系统时，该浏览器插件还会调用一个辅助可执行文件（“nm\_host.exe”），而基于浏览器的命令（例如，屏幕截图、剪贴板操作或 JavaScript 注入）则在本地运行。使用Native Messaging Host 二进制文件使得该恶意软件从基本的凭据窃取程序转变为远程访问工具。

SOCRadar 表示：“该扩展程序在用户上下文中运行，提取浏览器相关数据，并使用 com.peep.lab/nm\_host.exe 来运行 shell 命令、管理文件以及发现进程和服务。PEEP 通过绕过 Web 应用商店的检查，利用侧载、企业强制安装策略、首选项完整性操作以及脚本缓存回退机制来保持持久性。”

![](https://mmbiz.qpic.cn/mmbiz_png/vO1zY1O9p8IiazbspIgcSoTOOvqavgMGV1YEOf8rk9HZyhicusCQxVoXXxPh5pfMXHqpiamrcl4FuIDqoQq2HaePbwmqSiau9ibvc0T5ogp3m54A/640?wx_fmt=png&from=appmsg)

该扩展程序还使用了其他几个端点 -

* 使用“/api/register”注册感染
* 使用“/api/agents/<id>/heartbeat”发送有关浏览器用户代理字符串、操作系统和时区的详细信息
* “/api/extension\_update/” 和 “/api/extension\_crx/” 用于更新扩展程序本身
* 使用“/api/agents/<id>/task\_result”发布命令执行结果
* 使用“/api/exfil”发布自动收集的数据，例如 cookie、最近历史记录、打开的标签页、活动 URL、公共 IP 地址、语言环境和时区。
* “/health”用于提供内部系统状态信息，无需登录凭据
* "/login" 用于在端口 5001 上为 C2 面板提供登录界面。

PEEP 的另一个显著特点是能够修改安全首选项文件，确保浏览器启动时自动启用扩展程序。由于该扩展程序未在 Chrome 网上应用店和其他官方扩展程序市场上架，它还利用 ExtensionInstallForcelist 或 ExtensionSettings 策略以及侧载技巧进行部署。

为了协助进行这种篡改，该恶意软件使用了两个 PowerShell 脚本，而第三个脚本则充当扩展程序的重新注册助手，而不会触及安全首选项 -

* install\_silent.ps1，它启用开发者模式以侧载任意扩展。
* patch\_secure\_prefs.ps1，用于修补安全首选项文件。
* force\_enable.ps1 脚本会从“首选项”的 external\_uninstalls 列表中移除扩展程序，将 CRX 文件放置在 %LOCALAPPDATA%PEEPcrx 目录下，通过 HKCU Extensions 注册表项和 External Extensions JSON 清单文件重新注册该扩展程序，然后重启浏览器。

还有一个名为“patch\_secure\_prefs\_linux.py”的Python脚本，其功能与PowerShell版本相同，这表明该行动背后的威胁行为者正在复制这种行为，以攻击Linux环境。

初始化后，该扩展程序会解析配置文件以提取 C2 信息并激活自动数据采集，同时，配套的内容脚本（“content.js”）会嵌入到所有活动的网页中。

SOCRadar表示，他们发现了一些提及“授权CTF”使用情况的信息，这提示攻击者可能利用这种说法来降低AI工具的安全防护级别，并协助其开发恶意软件。目前尚不清楚攻击者的目标是谁，但“/health”端点显示有34个代理条目、10个活跃会话和507条数据记录。不过，目前无法区分实际感染的主机、测试条目或已验证的部署。

SOCRadar指出：“PEEP利用现有的主机入侵手段，通过原生消息桥将Chrome/Edge浏览器转换为持久性后门，从而突破浏览器沙箱，直达操作系统。由于其逻辑运行在已签名的浏览器进程内，因此可以绕过对新二进制文件或未签名二进制文件的密钥检测。因此，浏览器可以作为凭据窃取、会话滥用和命令执行的入口点。”

信息来源：The Hacker News

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlHBkILqQuaxKrXKhgz0ZMBz6S8ME08fAF1vUqLQlYxwYIVWh5bsgnAictt45YVfMuqzAic2QZd6Siag/0?wx_fmt=png)

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