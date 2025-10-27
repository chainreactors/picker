---
title: 勒索软件团伙滥用 Microsoft Azure 工具窃取数据
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578112&idx=1&sn=f776ef9d2598596856c997b1b30fed92&chksm=e914623ade63eb2ca4f45e7dbad2b8ca84b2693a8fcf180a04f9196cdbf6079a167cef85c7f5&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-09-25
fetch_date: 2025-10-06T18:27:23.201728
---

# 勒索软件团伙滥用 Microsoft Azure 工具窃取数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28pTe2EhLR0FGuAQu11DBlkIgibNbK9PQGicyBq4syNibNaXcUcezMFsoKMUiaWRTDy4QYARnSPMxxjyQ/0?wx_fmt=jpeg)

# 勒索软件团伙滥用 Microsoft Azure 工具窃取数据

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

BianLian 和 Rhysida 等勒索软件团伙越来越多地使用 Microsoft 的 Azure 存储资源管理器和 AzCopy 从受感染的网络窃取数据并将其存储在 Azure Blob 存储中。

Storage Explorer 是 Microsoft Azure 的 GUI 管理工具，而 AzCopy 是一个命令行工具，可以促进与 Azure 存储之间的大规模数据传输。在网络安全公司 modePUSH 观察到的攻击中，被盗数据随后被存储在云中的 Azure Blob 容器中，威胁分子随后可以将其传输到他们自己的存储中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28pTe2EhLR0FGuAQu11DBlk26WlyiaeS1tarxt1Z3SyM5eiacElSjGdVjgztxibyuk6Jfv9iatmD25ecg/640?wx_fmt=png&from=appmsg)

Azure 存储资源管理器界面

然而，研究人员指出，攻击者必须进行额外操作才能使 Azure 存储资源管理器正常工作，包括安装依赖项和将 .NET 升级到版本 8。此举也表明勒索软件操作越来越关注数据盗窃，这是威胁分子在随后的勒索阶段的主要手段。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28pTe2EhLR0FGuAQu11DBlk3s1icWv6bUCBNBs4T10NoPoyxYD3EREaWWAWAHEsGchjLPegQMMibfdg/640?wx_fmt=png&from=appmsg)为什么选择 Azure

虽然每个勒索软件团伙都有自己的一套泄露工具，但勒索软件团伙通常使用 Rclone 与各种云提供商同步文件，并使用 MEGAsync 与 MEGA 云同步。

Azure 是企业经常使用的受信任的企业级服务，不太可能被企业防火墙和安全工具阻止。因此，通过它进行的数据传输尝试更有可能顺利通过且不被发现。

此外，Azure 的可扩展性和性能使其能够处理大量非结构化数据，当攻击者试图在最短的时间内窃取大量文件时，这一点非常有益。

modePUSH 表示，它观察到勒索软件参与者使用多个 Azure 存储资源管理器实例将文件上传到 blob 容器，从而尽可能加快这一过程。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28pTe2EhLR0FGuAQu11DBlk3s1icWv6bUCBNBs4T10NoPoyxYD3EREaWWAWAHEsGchjLPegQMMibfdg/640?wx_fmt=png&from=appmsg)检测勒索软件泄露

研究人员发现，威胁分子在使用存储资源管理器和 AzCopy 时启用了默认的“信息”级别日志记录，这会在 %USERPROFILE%\.azcopy 处创建一个日志文件。

该日志文件对于事件响应人员特别有价值，因为它包含有关文件操作的信息，使调查人员能够快速确定哪些数据被盗（UPLOADSUCCESSFUL）以及可能引入了哪些其他有效载荷（DOWNLOADSUCCESSFUL）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28pTe2EhLR0FGuAQu11DBlkia3ibTN26TBD0JsAYsrpIFIZah0raYjqPGIlLddU04GZvWkWpfhFDDxQ/640?wx_fmt=png&from=appmsg)

数据传输成功日志

防御措施包括监控 AzCopy 执行情况、到“.blob.core.windows.net”或 Azure IP 范围的 Azure Blob 存储端点的出站网络流量，以及对关键服务器上的文件复制或访问中的异常模式设置警报。

如果企业已经使用 Azure，建议选中“退出时注销”选项以在退出应用程序时自动注销，防止攻击者使用活动会话进行文件窃取。

参考及来源：https://www.bleepingcomputer.com/news/security/ransomware-gangs-now-abuse-microsoft-azure-tool-for-data-theft/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28pTe2EhLR0FGuAQu11DBlkZDsCYMzB93zOJouwNFvT8BicynJX8tdp6VKTK8VeQAQiahLxtyW39LyA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28pTe2EhLR0FGuAQu11DBlkDwxxEIm3Z53IfGa2RCFtOeicNpB5DNicfqhbpFjfFveDXhOfqa2cW8ibg/640?wx_fmt=png&from=appmsg)

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