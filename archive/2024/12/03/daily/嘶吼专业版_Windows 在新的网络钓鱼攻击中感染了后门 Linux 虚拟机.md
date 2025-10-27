---
title: Windows 在新的网络钓鱼攻击中感染了后门 Linux 虚拟机
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247579944&idx=1&sn=937ff8a0f0fd609a57acccbdd578fda7&chksm=e9146912de63e004ecb5626f2db5e96318c1d74af21bd6d69a51ece9f3736a3326df2c7b3a18&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-12-03
fetch_date: 2025-10-06T19:40:22.949778
---

# Windows 在新的网络钓鱼攻击中感染了后门 Linux 虚拟机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibiadpQRoNZN8AiciaqRYeJSGwmxf1Q1PjByiapJarDico3lln8RicdGgbUW57DBqcmliaTNj40ffBwqxv1Q/0?wx_fmt=jpeg)

# Windows 在新的网络钓鱼攻击中感染了后门 Linux 虚拟机

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一种名为“CRON#TRAP”的新网络钓鱼活动通过 Linux 虚拟机感染 Windows，该虚拟机包含内置后门，可以秘密访问公司网络。

使用虚拟机进行攻击并不是什么新鲜事，勒索软件团伙和加密货币挖矿者利用虚拟机来秘密执行恶意活动。然而，威胁者通常在破坏网络后手动安装这些软件。

Securonix 研究人员发现的一项新活动是使用网络钓鱼电子邮件执行无人值守的 Linux 虚拟机安装，以破坏企业网络并获得持久性。

网络钓鱼电子邮件伪装成“OneAmerica 调查”，其中包含一个 285MB 的大型 ZIP 存档，用于安装预装后门的 Linux 虚拟机。

该 ZIP 文件包含一个名为“OneAmerica Survey.lnk”的 Windows 快捷方式和一个包含 QEMU 虚拟机应用程序的“data”文件夹，其中主要可执行文件伪装为 fontdiag.exe。

启动快捷方式时，它会执行 PowerShell 命令将下载的存档解压到“%UserProfile%\datax”文件夹，然后启动“start.bat”以在设备上设置并启动自定义 QEMU Linux 虚拟机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibiadpQRoNZN8AiciaqRYeJSGw4q87avKX03klJORbRrkzyTJ6wtV49KKpAmEkMCdf2vgt1dCdgiae3Kg/640?wx_fmt=png&from=appmsg)

Start.bat批处理文件安装QEMU Linux虚拟机

安装虚拟机时，同一个批处理文件将显示从远程站点下载的 PNG 文件，该文件显示虚假服务器错误作为诱饵，这意味着调查链接已损坏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibiadpQRoNZN8AiciaqRYeJSGwYG8gw5icwTN0lhfpicibHcHJaPhwTDcVeiaMlWNumVYL1jZRRTkEE8RqvA/640?wx_fmt=png&from=appmsg)

显示假错误的图像

名为“PivotBox”的定制 TinyCore Linux VM 预装了一个后门，可保护持久的 C2 通信，允许攻击者在后台进行操作。

由于 QEMU 是一个经过数字签名的合法工具，因此 Windows 不会对其运行发出任何警报，并且安全工具无法检查虚拟机内运行的恶意程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibiadpQRoNZN8AiciaqRYeJSGwGxpxDL50v3OkMbMxoDWElWXtnib5o9xwcvrBYpBhLPM6qYQ9Cx0gazQ/640?wx_fmt=png&from=appmsg)

LNK 文件内容

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibiadpQRoNZN8AiciaqRYeJSGwKVvoxOWWuuZJsGhxTYabUpTiarK5Vc8QH0XurtUpic5pxv5ic8yLs0kHA/640?wx_fmt=png&from=appmsg)后门操作

后门的核心是一个名为 Chisel 的工具，这是一个网络隧道程序，经过预先配置，可通过 WebSockets 与特定命令和控制 (C2) 服务器创建安全通信通道。

Chisel 通过 HTTP 和 SSH 传输数据，允许攻击者与受感染主机上的后门进行通信，即使防火墙保护网络也是如此。

为了持久性，QEMU 环境设置为在主机通过“bootlocal.sh”修改重新引导后自动启动。同时，会生成并上传 SSH 密钥，以避免重新进行身份验证。

Securonix 突出显示了两个命令，即“get-host-shell”和“get-host-user”。第一个在主机上生成一个交互式 shell，允许执行命令，而第二个用于确定权限。

然后可以执行的命令包括监视、网络和有效负载管理操作、文件管理和数据泄露操作，因此攻击者拥有一组多功能的命令，使他们能够适应目标并执行破坏性操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibiadpQRoNZN8AiciaqRYeJSGwXx3o7rSncnbUoTRicDa3HEycqSSrAmWZ20do1WSo4VTJ3z3uTaQbBTQ/640?wx_fmt=png&from=appmsg)

恶意分子的命令历史记录

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibiadpQRoNZN8AiciaqRYeJSGwKVvoxOWWuuZJsGhxTYabUpTiarK5Vc8QH0XurtUpic5pxv5ic8yLs0kHA/640?wx_fmt=png&from=appmsg)防御 QEMU 滥用

CRON#TRAP 活动并不是黑客第一次滥用 QEMU 与其 C2 服务器建立秘密通信。

2024 年 3 月，卡巴斯基报告了另一场活动，威胁者使用 QEMU 创建虚拟网络接口和套接字类型网络设备来连接到远程服务器。

在这种情况下，隐藏在仅运行 1MB RAM 的 Kali Linux 虚拟机内的一个非常轻的后门被用来建立一个隐蔽的通信隧道。

要检测和阻止这些攻击，请考虑为从用户可访问的文件夹执行的“qemu.exe”等进程放置监视器，将 QEMU 和其他虚拟化套件放入阻止列表中，并从系统 BIOS 禁用或阻止关键设备上的虚拟化。

参考及来源：https://www.bleepingcomputer.com/news/security/windows-infected-with-backdoored-linux-vms-in-new-phishing-attacks/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibiadpQRoNZN8AiciaqRYeJSGw5cYsWXwc6wzhNl77DXd6cK4v92Lgq5dOwXKFceuvNdFyJDPa3DmV3A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibiadpQRoNZN8AiciaqRYeJSGwRtptib8iaqUbpCPCt384rMu1peIdZ4of5evbcBtuib36T5KJrXCN7icHFA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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