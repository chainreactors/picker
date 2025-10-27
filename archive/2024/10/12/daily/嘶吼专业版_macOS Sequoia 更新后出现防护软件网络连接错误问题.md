---
title: macOS Sequoia 更新后出现防护软件网络连接错误问题
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578346&idx=1&sn=51d9643dbd82fa2ab3dbae0bbab3ed2b&chksm=e91462d0de63ebc6f1fdb6f958ca83ad8ff1cf5d008f02a60b2531633afe0a336ffa27ee1afd&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-10-12
fetch_date: 2025-10-06T18:53:48.616777
---

# macOS Sequoia 更新后出现防护软件网络连接错误问题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o287AxT53oZpP2iaqEDQ7iaghenS2ZoVWnTia5HaJESaka1F9iaqfNAlyluCUJ9S6Jayee9t1eQGK2trcg/0?wx_fmt=jpeg)

# macOS Sequoia 更新后出现防护软件网络连接错误问题

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

macOS 15“Sequoia”的用户在使用某些端点检测和响应 (EDR) 或虚拟专用网络 (VPN) 解决方案以及 Web 浏览器时报告网络连接错误。在停用这些工具后问题得到解决，这表明网络堆栈存在不兼容问题。

受影响的用户描述了 CrowdStrike Falcon 和 ESET Endpoint Security 的问题，以及防火墙引起的数据包损坏，从而导致 Web 浏览器 SSL 失败或无法使用“wget”和“curl”。

9 月，苹果发布了 Sequoia，称其为“全球最先进的桌面操作系统的最新版本”。在一份非公开公告中，CrowdStrike 表示由于 macOS 15 Sequoia 的内部网络结构发生变化，建议客户不应升级，直到发布完全支持 macOS 15 Sequoia 的 Mac 传感器为止。

据报道，SentinelOne 支持还警告用户不要立即升级到 macOS Sequoia，因为最近发现了可用性问题。

人们还发现了 Mullvad VPN 以及他们用于远程工作的企业 VPN 产品存在间歇性连接问题，但据了解 ProtonVPN 在最新的 macOS 版本上运行良好。

虽然苹果公司尚未回应有关这些问题的新闻请求，但据 macOS 15 发行说明显示，该操作系统防火墙中的一项功能已被弃用，这可能是导致这些问题的原因。

Application Firewall settings are no longer contained in a property list. If your app or workflow relies on changing Application Firewall settings by modifying /Library/Preferences/com.apple.alf.plist, then you need to make changes to use the socketfilterfw command line tool instead (124405935)

谷歌还在最近的 Chromium 错误报告中指出这一变化导致了问题，他们表示需要改变谷歌 Chrome 检测 Mac 防火墙设置的方式，改用“socketfilterfw”。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o287AxT53oZpP2iaqEDQ7iaghebuicDpibQobkfp5uGcLwwhM2nEzaoickjibZS2ySIk1GcIQvEVdUVrD2yQ/640?wx_fmt=png&from=appmsg)可能的解决方案

ESET 已针对升级到 macOS Sequoia 后遇到连接丢失问题的用户发布了一份咨询报告，建议用户导航至系统设置 > 网络 > 过滤器 > 并从列表中删除 ESET 网络。重新启动系统后，网络连接应可正常运行，ESET 产品应可正常运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o287AxT53oZpP2iaqEDQ7iagheagNyEZFVTM0xicNFMNS0nzE5NrnV0QwUlmfNxYDOuzVibjAVpsNEelBw/640?wx_fmt=png&from=appmsg)

从 macOS 过滤器中删除 ESET

该安全供应商还指出，这仅适用于 Endpoint Security 版本 8.1.6.0 及更高版本以及 ESET Cyber Security 版本 7.5.74.0 及更高版本，因为 macOS 15 不支持任何旧版本。

有安全研究员在一篇博客文章中提供了一个解决防火墙引起的问题的临时解决方案，但用户需要将其应用于他们使用的每个应用程序。

他强调了内置防火墙无法正确处理 UDP 流量的问题，在许多情况下会导致 DNS 故障，并提出了一个不太理想的解决方案，即“打漏洞”来解除令人困扰的限制。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o287AxT53oZpP2iaqEDQ7iaghe9BSuODLycvRWiaz5oFbfgEODqOYOfTa4sEpjMfBlNUP335cRZHmx7Vw/640?wx_fmt=jpeg&from=appmsg)

与此同时，Mullvad VPN 表示，他们已经意识到用户在最新的 macOS 版本中遇到的问题，并正在积极努力寻找解决方案。

如果您使用 EDR 安全产品、VPN 或依赖严格的防火墙配置，建议暂时推迟迁移到 macOS 15，直到问题得到解决。

参考及来源：https://www.bleepingcomputer.com/news/apple/macos-sequoia-change-breaks-networking-for-vpn-antivirus-software/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o287AxT53oZpP2iaqEDQ7iagheYmXjtEL5MxcUzj0hsRobxOxvs0XV5BOpzeSRXkFe3u0LzicKTW8m3zg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o287AxT53oZpP2iaqEDQ7iagheQhABK9U1ZA4NXGTxRjbqJ2yoytJRc0iabRP9eMDR4Kwk8DbW9hVjakw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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