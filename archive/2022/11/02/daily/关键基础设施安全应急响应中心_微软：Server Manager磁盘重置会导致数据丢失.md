---
title: 微软：Server Manager磁盘重置会导致数据丢失
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247532291&idx=2&sn=5d8593253e6c91bb9edf0312594e1ff6&chksm=c1e9f352f69e7a4485d9d51a548471d3c2243eb0d189762bd30cf7c5bc21c027b6f33f75408f&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-11-02
fetch_date: 2025-10-03T21:33:07.757595
---

# 微软：Server Manager磁盘重置会导致数据丢失

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogticyUTXnCK5nb81b08tW8CeCesbsSHgePMEs5AzxlB2hkmc1NAOEawPoJg6pSG4iamibA3sEV6KiaPRA/0?wx_fmt=jpeg)

# 微软：Server Manager磁盘重置会导致数据丢失

关键基础设施安全应急响应中心

微软近日发出警告：用户在使用Server Manager（服务器管理器）管理控制台重置虚拟磁盘时，最近确认的一个问题可能会导致数据丢失。

Server Manager帮助IT管理员从他们的桌面配置和管理基于Windows的本地和远程服务器，不需要远程桌面连接或实际访问服务器。

由于这个问题，试图重置（或清除）虚拟磁盘的管理员可能会意外重置不该重置的磁盘，从而导致数据损坏。

管理员还会在Task Progress（“任务进度”）对话窗口中看到“重置磁盘失败”错误，并显示“发现多个有相同ID的磁盘。请更新您的存储驱动程序，然后重试一下。”的错误消息。

微软在一份新的支持文档中解释道：“当您使用Community Virtual驱动程序时，可能存在多个虚拟磁盘有相同UniqueId的情况。这可能会在您执行重置操作时产生问题。”

“重置操作会重置它找到的第一个磁盘。然而，这可能不是您想要重置的那个磁盘。因此，该磁盘会丢失数据。”

这个已知问题影响以下客户端和服务器Windows平台：Windows Server 2019、Windows Server 2022和Windows 11 22H2。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28Qpplladq1Aln3WX9uzzicwGy85lScoTuxfO8C2MG8Z81CFtpUN6ZN6dYYRIwY8pueX9gPQTJ4OSQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1. 虚拟磁盘重置失败（来源：微软）

**现有的解决方案**

微软为遇到这个已知问题的管理员们提供了一个解决方案，让他们可以在不用担心数据丢失风险的情况下重置虚拟磁盘。

为此，您可以使用以下PowerShell命令跨可用的Storage Management Providers（存储管理提供者）检索磁盘的设备ID（DeviceID），并通过删除所有分区信息和取消初始化它来清除磁盘，从而擦除磁盘上的所有数据：

1. 要检索磁盘的详细信息，输入Get-PhysicalDisk | Select-Object -Property FriendlyName, DeviceID, UniqueId。

2. 确认想要重置的那个磁盘的详细信息。使用磁盘的DeviceID作为命令中的Number：Clear-Disk [-Number]。

您可以在Get-PhysicalDisk支持文档（https://docs.microsoft.com/powershell/module/storage/get-physicaldisk?view=windowsserver2022-ps）和Clear-Disk支持文档（https://docs.microsoft.com/powershell/module/storage/clear-disk?view=windowsserver2022-ps）中找到关于如何使用这两个命令的更多信息。

周一，微软还发布了针对Windows 11 22H2的KB5018496预览累积更新，以解决另一个已知的问题，这个问题阻止易受攻击驱动程序黑名单被同步到运行较旧Windows版本的系统。

**参考及来源：**

https://www.bleepingcomputer.com/news/microsoft/microsoft-server-manager-disk-resets-can-lead-to-data-loss/ https://support.microsoft.com/en-gb/topic/kb5018898-server-manager-resets-the-wrong-disk-if-many-virtual-disks-have-the-same-uniqueid-5b4b7d32-e65f-469e-a266-e7dc4b22467f https://www.theregister.com/2022/10/27/microsoft\_server\_resets\_windows11/

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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