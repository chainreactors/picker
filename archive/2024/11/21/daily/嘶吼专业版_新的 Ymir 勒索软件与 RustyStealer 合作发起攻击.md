---
title: 新的 Ymir 勒索软件与 RustyStealer 合作发起攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247579681&idx=1&sn=8eeb803cd6c50fef47e025138c3548b4&chksm=e914681bde63e10db4e3df99b76d58e69aa9e326cdc7505d2b5b515f2cfcae2fbf62b03b66fa&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-11-21
fetch_date: 2025-10-06T19:16:57.704092
---

# 新的 Ymir 勒索软件与 RustyStealer 合作发起攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibeqwjiavqe3n7ibfm4R2DlA6X1ib5luzBvAhOnADrB7CzBGglEUlZ1rVaaaaBR1F0Eaj4urtgGViaG1w/0?wx_fmt=jpeg)

# 新的 Ymir 勒索软件与 RustyStealer 合作发起攻击

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一种名为“Ymir”的新勒索软件家族在野外被发现，它对之前受到RustyStealer infostealer 恶意软件危害的系统进行加密。

RustyStealer 是一个知名恶意软件家族，首次记录于 2021 年。据在事件响应期间发现 Ymir 的卡巴斯基研究人员称，这种新型勒索软件以其内存中执行、在代码注释中使用非洲林加拉语、使用 PDF 文件作为勒索信息及其扩展配置选项而闻名。

尽管卡巴斯基发现证据表明 Ymir 连接到可能促进数据泄露的外部服务器，但勒索软件并不具备这种功能。

目前已确认勒索软件操作于 2024 年 7 月启动，当时它便开始攻击世界各地的公司。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibeqwjiavqe3n7ibfm4R2DlA6gibKq9XYl9snAZWdaNmW62RoLGyh01dKp3jhABURTnaiam70h1jlncSQ/640?wx_fmt=png&from=appmsg)Ymir 关注 RustyStealer 感染

卡巴斯基的分析显示，Rusty 窃取者在 Ymir 部署前两天已渗透到目标基础设施内的多个系统。RustyStealer 本质上是一种凭证收集工具，它使攻击者能够通过破坏可用于横向移动的合法高权限帐户来获得对系统的未经授权的访问。

使用 Windows 远程管理 (WinRM) 和用于远程控制的 PowerShell 等工具可以促进跨网络的横向移动。同时，攻击者还安装了Process Hacker和Advanced IP Scanner等工具。

接下来，他们执行与 SystemBC 恶意软件相关的脚本，并与攻击者的基础设施建立秘密通道，可能用于数据泄露或命令执行。

在巩固立足点并可能使用 RustyStealer 窃取数据后，Ymir 勒索软件作为最终有效负载被丢弃。

Ymir 是一种新型 Windows 勒索软件，完全从内存运行，利用“malloc”、“memove”和“memcmp”等功能来逃避检测。

启动后，它通过获取系统日期和时间、识别正在运行的进程以及检查系统正常运行时间来执行系统侦察，这可以帮助确定它是否在沙箱上运行。接下来，它根据硬编码列表跳过文件扩展名，以避免导致系统无法启动。

Ymir 使用 ChaCha20 流密码（一种先进且快速的加密算法）来加密受害者系统上的文件。加密文件会附加一个随机扩展名，例如“.6C5oy2dVr6”，并且从包含加密文件的所有目录中 Ymir 二进制文件的“.data”部分生成名为“INCIDENT\_REPORT.pdf”的勒索字条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibeqwjiavqe3n7ibfm4R2DlA6y5C48o7MZicnL0iaaCm6hyKLlBLX0LicibePVAUee2yKRrpH4rrGRvhKzQ/640?wx_fmt=png&from=appmsg)

Ymir 勒索信

该勒索软件还会修改 Windows 注册表“legalnoticecaption”值，以在用户登录加密设备之前显示勒索要求。

勒索信声称受害者系统中的数据被盗，卡巴斯基推测这可能是使用 Ymir 之前部署的工具发生的。

最后，Ymir 扫描系统中是否存在 PowerShell，并利用它删除其可执行文件以逃避识别和分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibeqwjiavqe3n7ibfm4R2DlA6w3CHw11f5FfSC9qMOe9oEJmh9wCL9ZwS6ib5a129ZFdQ9XjFo2lhIkA/640?wx_fmt=png&from=appmsg)

Ymir 的执行过程

Ymir 尚未建立数据泄露站点，但恶意分子可能刚刚开始积累受害者数据。卡巴斯基认为，Ymir 使用信息窃取程序作为访问代理可能很快使这个新的勒索软件家族成为广泛威胁。

参考及来源：https://www.bleepingcomputer.com/news/security/new-ymir-ransomware-partners-with-rustystealer-in-attacks/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibeqwjiavqe3n7ibfm4R2DlA6PkjKtr1jJ9EOkoDeoff0XwAibKb2poNHkpjjiaJdPic8UgjHicIwmpvasw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibeqwjiavqe3n7ibfm4R2DlA6tcibKnzUcPoDb6FnBLCy32c8XL01mIskiayrofFQ4hB5XOeeQb5KlicYw/640?wx_fmt=png&from=appmsg)

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