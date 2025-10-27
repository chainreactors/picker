---
title: 新的 Voldemort 恶意软件滥用 Google Sheets 来存储被盗数据
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577870&idx=1&sn=60a05966e00af529f131b525a18d31b8&chksm=e9146134de63e8229bfea3adea630b4c2441b9c67cc4038bebc9130b6322c9b92ee68aed9188&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-09-10
fetch_date: 2025-10-06T18:28:55.126314
---

# 新的 Voldemort 恶意软件滥用 Google Sheets 来存储被盗数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o286D2JgTfcMdYFhoesYdD4XrWTX5HdJ4Tibiby3vLw4JibWfz53oGZibOnjfa9uic8Sm1FukzosHytRwDw/0?wx_fmt=jpeg)

# 新的 Voldemort 恶意软件滥用 Google Sheets 来存储被盗数据

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一项新的恶意软件活动正在向全球传播一种之前未曾记录的后门“Voldemort”，主要冒充美国、欧洲和亚洲的税务机构。

根据 Proofpoint 的报告，该活动于 2024 年 8 月 5 日开始，已向 70 多个目标组织传播了 20,000 多封电子邮件，在其活动高峰期一天内就达到了 6,000 封。

超过一半的目标组织属于保险、航空航天、交通运输和教育行业。此次攻击活动的幕后威胁者尚不清楚，但 Proofpoint 认为最有可能的目的是进行网络间谍活动。

此次攻击与 Proofpoint 在本月初描述的攻击类似，但最后阶段涉及了不同的恶意软件。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o286D2JgTfcMdYFhoesYdD4XtWPWH0de14E54RCQLeibLIzCez6JaxkXl9m6nenyxyY9SjhlyAM3pYQ/640?wx_fmt=png&from=appmsg)冒充税务机关

Proofpoint 的最新报告称，攻击者正在根据公开信息制作网络钓鱼电子邮件以匹配目标组织的位置。

网络钓鱼电子邮件冒充该组织所在国家的税务机关，声称有更新的税务信息并包含相关文件的链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o286D2JgTfcMdYFhoesYdD4Xib9y26FnqXdnDAoaIBicAicvG0AuQnTozfWtqLgPpwp2Vy8hcfuDxia5Bw/640?wx_fmt=png&from=appmsg)

攻击活动中使用的恶意电子邮件样本

点击该链接会将收件人带到托管在 InfinityFree 上的登录页面，该页面使用 Google AMP Cache URL 将受害者重定向到带有“单击查看文档”按钮的页面。

单击按钮后，页面将检查浏览器的用户代理，如果适用于 Windows，则将目标重定向到指向 TryCloudflare 隧道 URI 的 search-ms URI（Windows 搜索协议）。非 Windows 用户将被重定向到一个空的 Google Drive URL，该 URL 不提供任何恶意内容。

如果受害者与 search-ms 文件交互，Windows 资源管理器就会被触发，显示伪装成 PDF 的 LNK 或 ZIP 文件。

search-ms: URI 的使用最近在网络钓鱼活动中变得很流行，因为即使此文件托管在外部 WebDAV/SMB 共享上，它也会看起来好像位于本地的下载文件夹中，以诱骗受害者打开它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o286D2JgTfcMdYFhoesYdD4XQEp2k7cFWREP8rPzDhxZzia9Ojib3KQK6P0KxsaQnuBrQvfM2mDtNByw/640?wx_fmt=png&from=appmsg)

使文件看起来好像位于受害者的计算机上

这样做会从另一个 WebDAV 共享中执行 Python 脚本，而无需将其下载到主机上，该脚本会执行系统信息收集以分析受害者。同时，会显示诱饵 PDF 以掩盖恶意活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o286D2JgTfcMdYFhoesYdD4XB6IdD97DgoibhLFiaNibOTGEtU158xTKKt1H8hV9PClkNObSiaVwp449fQ/640?wx_fmt=png&from=appmsg)

转移受害者注意力的诱饵 PDF

该脚本还下载合法的 Cisco WebEx 可执行文件（CiscoCollabHost.exe）和恶意 DLL（CiscoSparkLauncher.dll），以使用 DLL 侧加载来加载 Voldemort。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o286D2JgTfcMdYFhoesYdD4XtWPWH0de14E54RCQLeibLIzCez6JaxkXl9m6nenyxyY9SjhlyAM3pYQ/640?wx_fmt=png&from=appmsg)滥用 Google 表格

Voldemort 是一个基于 C 的后门，支持各种命令和文件管理操作，包括渗透、将新的有效载荷引入系统以及文件删除。

支持的命令列表如下：

**·**Ping – 测试恶意软件与 C2 服务器之间的连接。

**·**Dir – 从受感染系统检索目录列表。

**·**Download – 从受感染系统下载文件到 C2 服务器。

**·**Upload – 从 C2 服务器上传文件到受感染系统。

**·**Exec – 在受感染系统上执行指定的命令或程序。

**·**Copy – 在受感染系统内复制文件或目录。

**·**Move – 在受感染系统内移动文件或目录。

**·**Sleep – 使恶意软件在指定的时间内进入睡眠模式，在此期间恶意软件不会执行任何活动。

**·**Exit – 终止恶意软件在受感染系统上的运行。

Voldemort 的一个显著特点是，它使用 Google Sheets 作为命令和控制服务器 (C2)，对其进行 ping 以获取在受感染设备上执行的新命令，并将其作为被盗数据的存储库。

每台受感染的机器都会将其数据写入 Google Sheet 中的特定单元，这些单元可以通过 UUID 等唯一标识符指定，从而确保隔离并更清晰地管理受感染的系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o286D2JgTfcMdYFhoesYdD4XE5yeXT39cFPoVumGibA6JEiaeT2Pxiazcf0I8a8gtkU96rmcZT64BMHow/640?wx_fmt=png&from=appmsg)

请求从 Google 接收访问令牌

Voldemort 使用嵌入了客户端 ID、密钥和刷新令牌的 Google API 与 Google Sheets 进行交互，这些都存储在其加密配置中。

这种方法为恶意软件提供了可靠且高度可用的 C2 通道，同时还降低了网络通信被安全工具标记的可能性。

由于 Google Sheets 在企业中广泛使用，因此阻止该服务也不切实际。

2023 年，黑客组织 APT41 曾被发现通过使用红队 GC2 工具包将 Google Sheets 用作命令和控制服务器。为了防御此活动，Proofpoint 建议将对外部文件共享服务的访问限制在受信任的服务器上，在不需要时阻止与 TryCloudflare 的连接，并监控可疑的 PowerShell 执行。

参考及来源：https://www.bleepingcomputer.com/news/security/new-voldemort-malware-abuses-google-sheets-to-store-stolen-data/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o286D2JgTfcMdYFhoesYdD4X1NXSspMfYiax76D62ib4M8icBGzkvE14zk1jOUQBjZ9vCTiaPQvJSZ1YRg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o286D2JgTfcMdYFhoesYdD4XvKsAev9qhKkXKAfR5wMTkqLhXia0YAxXmTZHxyxmDBNwseHV6tgT4Ag/640?wx_fmt=png&from=appmsg)

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