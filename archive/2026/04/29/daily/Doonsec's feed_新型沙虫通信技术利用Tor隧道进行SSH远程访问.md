---
title: 新型沙虫通信技术利用Tor隧道进行SSH远程访问
url: https://mp.weixin.qq.com/s/XcU7KHJfuzugFibEBOtE-w
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:26:37.876498
---

# 新型沙虫通信技术利用Tor隧道进行SSH远程访问

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J7CSmJcRR8l8xAATDOTJADbszz5NxAnI20OXtibxpHa38vJ5e1PpBO28mbzVET6ZoVrXAseRavSJ6PPDkpjyMl0TMyLYowRP9AhjURNFXtd0/0?wx_fmt=jpeg)

# 新型沙虫通信技术利用Tor隧道进行SSH远程访问

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8mVstOqAPmm8EU6ibJerTnotNGngvEE9hCbianuibsHAYvJOibuBJnfia9Zd7hn5Hiah0c8eQlxs1ku5cDHYO67MrNwRC631KxuWKicBw/640?wx_fmt=png&from=appmsg)

一个名为 Sandworm（也被称为 APT-C-13 和 FROZENBARENTS）的国家支持的威胁组织发起了一场有针对性的网络攻击活动，该活动结合了 SSH 和 Tor 隧道技术，以在受害者网络中保持长期的隐藏访问权限。

此次攻击活动标志着该组织入侵策略的明显升级，从简单的恶意软件回调转向了完全匿名、加密的远程控制系统，该系统能够在企业防火墙后悄无声息地运行。

该组织至少从 2014 年起就十分活跃，主要目标是政府机构、外交部门、能源公司和研究机构，以窃取政治、军事和技术情报。

在最近的这次攻击活动中，攻击者改进了他们的攻击方法，部署了双层匿名隧道，旨在融入正常的网络流量中。

感染始于一封带有 ZIP 压缩文件的鱼叉式网络钓鱼电子邮件，一旦打开，该文件就会悄无声息地安装恶意工具，同时显示一个看起来很合法的诱饵文档，使受害者浑然不觉。

360 高级威胁研究所的研究人员发现了与此次攻击活动相关的多个恶意样本，并指出该组织使用 SSH 和 Tor 嵌套隧道在攻击者和受感染主机之间建立双重加密的匿名通道。

这种架构使攻击者能够不受限制地访问受害者系统，从而提取敏感数据，而不会触发标准流量检查工具或引起网络监控系统的警报。

攻击样本以名为 Iskhod\_7582\_Predstavlenie\_na\_naznachenie.zip 的 ZIP 压缩包形式提供，其 MD5 哈希值为 2156c270ffe8e4b23b67efed191b9737。

在这个压缩包中，该组织隐藏了一个伪装成 PDF 文档的恶意 LNK 快捷方式，以及一个名为 $RECYCLE.BIN 的虚假文件夹，该文件夹旨在模仿 Windows 回收站目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8nDr8ibA9Sys1Nsg3AWlIlErMqkXdqnSD7k3a8RbCiaxpibTavQic5RwvPKptAO6O41iaiajf7vtstUBwugOLfhSkYia2ibh0JZMrCzVkw/640?wx_fmt=png&from=appmsg)

一旦受害者点击了 LNK 文件，完整的攻击工具包就会在后台静默部署，同时打开真正的诱饵 PDF 文件，以分散用户的注意力，防止其被安装。

此次攻击的总体影响十分严重。一旦工具包部署到位，攻击者便能持续控制受害者的内部网络，并能够横向移动、访问敏感文件以及操作远程桌面。

包括 SMB 端口 445 和 RDP 端口 3389 在内的关键本地端口被映射到暗网洋葱地址，使攻击者能够通过 Tor 网络从世界任何地方连接，绕过所有入站防火墙保护。

Sandworm 如何实现持久隐藏访问

此次攻击活动中，技术上最值得关注的部分是 Sandworm 如何使用伪装成知名应用程序的工具，在受害者系统中植入长期访问权限。

LNK 文件触发主控制脚本 currentSessionTrigger 后，该脚本首先通过检查至少 10 个最近的 .lnk 文件和 50 个或更多活动进程来验证它是否在真正的机器上运行。

如果环境通过了这些检查，脚本会注册两个名为 OperagxRepairTask 和 DropboxRepairTask 的计划任务，这两个任务都会从默认的任务计划程序视图中隐藏，从而确保恶意载荷在每次用户登录时自动启动。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8k9tDRSzJ8gp2lGN7F2EYIHA8DUqxzaWV8rW5YkBkia921rxBMbtxhUE0tAzGe670OMgOou2vpnr9swo6Ws4s4fqqavkdvj5TBo/640?wx_fmt=png&from=appmsg)

这些任务启动了两个伪装的可执行文件：operagx.exe（实际上是 OpenSSH 守护程序）和 dropbox.exe（Tor 服务器）。

第三个文件 safari.exe 充当 obfs4 流量混淆插件，将所有 Tor 流量重塑为随机 TCP 流，以绕过企业防火墙和深度包检测系统。

第四个文件 obsstudio.exe 用作 SFTP 服务器，进行静默文件传输。SSH 守护进程配置为仅监听本地回环端口 20321，使其对外部网络扫描不可见。

Tor 服务启动后，会生成一个隐藏的 .onion 主机名。主控制脚本读取此主机名，并使用高频重试设置的 curl 命令将受害者的身份信息发送到硬编码的 C2 地址 kvk46su7d2qi6g4n43syp4zbsf2rihnc6ztj77qtc2ojvewjqvqilnqd.onion，以维持连接，从而在受害者的网络内部建立一个永久加密的影子控制通道。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

Khan安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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