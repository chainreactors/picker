---
title: 伪造证书加载器隐藏 BlankGrabber 恶意软件链
url: https://mp.weixin.qq.com/s/aAJaL7vXkJtZjezp3vMnsQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:56.540831
---

# 伪造证书加载器隐藏 BlankGrabber 恶意软件链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7N4JbFnTUibHWXriaeGsEkKWd30tH4C1StDkic9ibT4k8NVX6icopicCam56nWdeBjVTpmcdUMB6vCggaibdyfYAULjaaNCVOCnWRu144/0?wx_fmt=jpeg)

# 伪造证书加载器隐藏 BlankGrabber 恶意软件链

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

BlankGrabber 的运营者现在滥用伪造的“证书”加载器来隐藏多阶段的 Rust 和 Python 感染链，使得这种商品窃取程序在 Windows 终端上更难被发现。

这项新技术依赖于内置工具（如 certutil.exe）、高度混淆的 PyInstaller 存根，以及通过 Telegram和公共网络服务进行的隐蔽数据泄露，以逃避静态和行为检测。

乍一看，该脚本解码数据并将其传递给 certutil.exe 以安装看似 Windows 证书的东西。

更深入的分析表明，编码后的 blob 根本不是证书，而是一个编译后的 Rust 可执行文件，它充当暂存器，负责解密和启动真正的有效载荷。

根据 Splunk 威胁研究团队 (STRT) 的说法，最近的 BlankGrabber 攻击活动始于托管在 Gofile.]io 文件共享服务上的批处理脚本。

Rust stager 通过伪装成证书数据并仅显示内存中的下一阶段，增加了一层混淆。

它还会执行反沙箱检查，查找诸如“Triage”、“Sandbox”、“Malware”或“Zenbox”之类的可疑驱动程序、用户名和计算机名称，以避免在自动化分析环境中引爆。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7OiblhInNXZ3icicNH5hEHVibxrQmg8zTEZuu8B7CtOTXsibTIHgR7CIz3elJnyyJhfUZ7qFlxOibrJWU7FMLmMLxmh57S9mEoo1xNcU/640?wx_fmt=png&from=appmsg)

一旦确认目标系统是真正的受害者系统，它就会解密并释放一个自解压 RAR (SFX) 存档到 %TEMP% 目录，使用的文件名通常是几个看起来很无害的文件名，例如 OneDriveUpdateHelper.exe、RuntimeBroker.exe 或 MicrosoftEdgeUpdate.exe。

## **XWorm + BlankGrabber 集成于单个音效中**

SFX 归档包含多个组件，特别是 XWorm 远程访问客户端 (host.exe) 和 PyInstaller 打包的 BlankGrabber 窃取程序 (Knock.exe)，从而可以在同一主机上进行远程控制和大规模数据窃取。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7PKrjiaAicqugRXUrtFs59gITnicUthTzpV5B2NdelAhAyVjfZvpR6NFPJt0KpA4fNowl51VJ2E3WKgIna9Cj5J02cybYsSP5zkso/640?wx_fmt=png&from=appmsg)

将这些工具打包在一起，可以帮助攻击者横向移动、持久化并一次性窃取数据。

BlankGrabber 本身最初是作为开源 Python 信息窃取工具发布的，它通过 GUI 构建器构建，该构建器将 Python 代码、第三方库和嵌入式工具封装到一个可执行文件中。

STRT 的分析表明，PyInstaller 包隐藏了一个名为“blank.aes”的加密数据块，该数据块在运行时使用自定义的 AES 例程进行解密，以重建下一阶段的 ZIP 存档。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7MicmI4cehkUicBcEGuVwFFkRakHMdPnzDp3Dx7zl0iciaVA5LibmTJT0ymFhIm2vE50jE6TiaJzOZibfHPJRA4xf9DLRAMS7XZichcq5s/640?wx_fmt=png&from=appmsg)

该存档包含另一个经过高度混淆的 Python 存根，它使用 zlib 压缩以及 Base64、ROT13 和字符串反转来分层加载逻辑，最终恢复可运行的 BlankGrabber 存根。

BlankGrabber 完全解压后，会执行广泛的环境检查，通过检查 UUID、适配器供应商以及连接到随机域来测试模拟的互联网响应，从而发现虚拟机、伪造的网络和安全工具。

然后，它使用 systeminfo、getmac、WMI 查询（例如 Win32\_ShortcutFile、AntivirusProduct、csproduct）和网络摄像头捕获等命令来分析受害者，并枚举已保存的 Wi-Fi 配置文件，以通过 netsh 提取明文 WLAN 密钥。

对于数据窃取，窃取者会解析 Chromium 和 Firefox 数据库以导出密码、cookie、历史记录和自动填充数据，抓取加密钱包扩展程序，并以 Telegram、Discord、Steam、Epic Games、Roblox 和 Minecraft 等平台为目标。

它还可以收集剪贴板文本，通过 PowerShell 截取基于 .NET 的屏幕截图，收集文档和凭据文件类型，并使用受密码“Blank123”保护的嵌入式 rar.exe 实用程序归档所有内容。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7MmXqyJ6qBlrVtKHNqEN58jYMicA4Fus6UfAwha9omlOEP00bk1QY1lKUKkeL6WZIBibM5T6ay65KJianAmum5YXPcFz9cz6YrRDo/640?wx_fmt=png&from=appmsg)

数据泄露依赖于Telegram 机器人和被滥用的网络服务的组合，包括 IP 查询 API（如 ip-api[.]com）和流行的文件共享或粘贴平台。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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