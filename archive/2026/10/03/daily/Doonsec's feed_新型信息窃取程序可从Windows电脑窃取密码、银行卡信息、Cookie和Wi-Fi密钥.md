---
title: 新型信息窃取程序可从Windows电脑窃取密码、银行卡信息、Cookie和Wi-Fi密钥
url: https://mp.weixin.qq.com/s/2pCd5JLI6ulokOZ0jo5_Cw
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:37:09.120413
---

# 新型信息窃取程序可从Windows电脑窃取密码、银行卡信息、Cookie和Wi-Fi密钥

# 新型信息窃取程序可从Windows电脑窃取密码、银行卡信息、Cookie和Wi-Fi密钥

原创

ZM
ZM

暗镜

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一个基于 Python 的信息窃取器构建器，使威胁行为者能够生成自定义的 Windows 有效载荷，从而窃取浏览器凭据、支付卡数据、会话 cookie、Discord 令牌、Wi-Fi 密码和大量系统信息。

该软件包并非一次性窃取程序，而是包含一个构建器接口和一个嵌入式有效载荷，提供了一种与恶意软件即服务操作一致的模型。

操作人员可以配置攻击者控制的 webhook，选择编译方法，并生成单独的 Windows 二进制文件进行分发。

这种设计可以帮助关联方部署具有不同哈希值的样本和外泄基础设施，从而使关联和基于签名的检测变得复杂。

构建器启动时会自动安装所需的 Python 依赖项，从而降低了在干净的 Python 环境中运行的犯罪分子的设置要求。

这种行为使得`pip.exe`来自非开发应用程序的意外活动成为一种潜在的有用检测信号。有效载荷在运行时逆转此过程，防止 webhook 在编译后的可执行文件中以明文形式出现。操作人员可以使用 Nuitka、PyInstaller 构建有效载荷，或者将恶意软件保存为原始 Python 脚本。

Nuitka 特别值得注意，因为它通过 C 将 Python 代码编译成本地可执行文件，从而限制了 Python 字节码恢复工具的用途。

据报道，该构建器宣称此方法可提供更强的防病毒规避能力，而 PyInstaller 生成的软件包通常可以解包以恢复`.pyc`字节码。该构建器还排除了非必要的 Python 库，例如`tkinter`、和`matplotlib`，以减少文件大小并可能最大限度地减少其检测占用空间。`numpy``pandasK7 安全实验室在一份与 GBhackers 分享的报告中表示`，该恶意软件是在一个可疑的嵌套存档链中发现的，该存档链包含*“* my new program called 2.rar”及“TokenGrabberBuilder.zip”

相关IOC

|  |  |
| --- | --- |
| c65a3f8e88559f89ed90ea9ee5c | Password-Stealer ( 006dba241 ) |
| 429ed63ab3fbda8d22d0ac750ecfe8cc | Password-Stealer ( 006dba241 ) |
| 9ffe0e45c7a3f20e4481206c1c3b0854 | Trojan ( 006e632e1 ) |

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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