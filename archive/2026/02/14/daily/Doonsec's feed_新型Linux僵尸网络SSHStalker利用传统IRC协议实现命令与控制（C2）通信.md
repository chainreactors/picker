---
title: 新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信
url: https://mp.weixin.qq.com/s/NKYrtLHgPvBcemi6DdYCrw
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:21:57.518114
---

# 新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fHEm7hZn9HKNBIy8XhwMPTZI7eCPFeF0xpubia6onbawnHGbN7Pk8lMZNDAn0EgOUHzoJvpvvKTrF9vqbn8ElCTnr1Idic8kIxpfvnAaCmvgU/0?wx_fmt=jpeg)

# 新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信

胡金鱼
胡金鱼

嘶吼专业版

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

安全研究员最新发现的一款 Linux 僵尸网络 SSHStalker，采用IRC（互联网中继聊天）通信协议实现命令与控制（C2）操作。

据了解，该协议于 1988 年问世，在 20 世纪 90 年代达到普及高峰，成为当时用于群组与私密通信的主流文本即时通信方案。技术社区至今仍青睐其实现简单、互操作性强、带宽占用低且无需图形界面（GUI）等特点。

SSHStalker 僵尸网络并未采用现代化命令与控制框架，而是依托经典 IRC 机制运行，例如使用多个基于 C 语言编写的木马程序、多服务器/多频道冗余设计，更注重韧性、规模化与低成本，而非隐蔽性与技术新颖性。

研究人员表示，这种思路也体现在 SSHStalker 的其他攻击行为中，例如使用特征明显的 SSH 扫描、每分钟执行一次的定时任务，以及大量距今已有 15 年历史的漏洞（CVE）。

据悉，安全研究人员实际发现的是一个特征明显、拼凑而成的僵尸网络工具包，融合了传统 IRC 控制、在主机上编译二进制程序、大规模 SSH 攻陷以及基于定时任务实现持久化等手段。简单来说，这是一套优先规模、注重可靠而非隐蔽的运营模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fHEm7hZn9HKusCJtu5tibbxAzP0NibOXs7aBQ4c5ziaWxhD629LIPrQHLY3zWkpibZgJhBNEzTwugGfeyXLqvI4yogYREjpJs8fTibFjaKmGvtzg/640?wx_fmt=png&from=appmsg)

受感染主机 IRC 频道

SSHStalker 通过自动化 SSH 扫描与暴力破解实现初始入侵，其使用的 Go 语言二进制程序会伪装成知名开源网络探测工具 Nmap。

被攻陷的主机随后会被用于扫描更多 SSH 目标，形成类似蠕虫的传播扩散机制。

研究人员发现了一份包含近 7000 条僵尸网络扫描结果的文件，均来自今年 1 月，攻击目标主要集中在Oracle Cloud等云服务商。

SSHStalker 感染主机后，会下载 GCC 编译工具，在受害设备上直接编译恶意载荷，以提升程序可移植性与规避检测能力。

首批载荷为基于 C 语言的 IRC 木马，内置硬编码的控制服务器与频道信息，将新受害主机纳入僵尸网络的 IRC 控制体系。

随后，该恶意软件会下载名为 GS 和 bootbou 的压缩包，其中包含用于统一调度与按序执行的不同木马变体。

持久化机制通过每 60 秒运行一次的定时任务实现，该任务采用看门狗式更新逻辑，检查主木马进程是否运行，若被终止则重新启动。

该僵尸网络还集成了针对 2009—2010 年版本 Linux 内核的 16 个漏洞利用程序，在暴力破解获得低权限用户访问权限后，用于实现权限提升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fHEm7hZn9HJ7L0FBf9A6kXRfu4KX5ksdIAaNNIcSKDcYoKiaeRW7QxMd3D4gswjooG5oCKo7jGAPUEgnNnIicox9QvehHibbkiaofpHdCFoicth8/640?wx_fmt=png&from=appmsg)

攻击链概述

在牟利方式上，该僵尸网络会窃取 AWS 密钥、扫描网站，并集成了挖矿程序，包括高性能以太坊挖矿工具 PhoenixMiner。

僵尸网络同样具备分布式拒绝服务（DDoS）攻击能力，但研究人员表示暂未观测到相关攻击行为。事实上，SSHStalker 木马目前仅连接控制服务器后便进入闲置状态，表明其仍处于测试或囤积访问权限阶段。

研究人员尚未将 SSHStalker 归属到特定攻击组织，但发现其与 Outlaw/Maxlas 僵尸网络体系存在相似之处，并出现多项与罗马尼亚相关的特征线索。

威胁情报机构建议，在生产服务器上应部署针对编译器安装与执行行为的监控方案，并对 IRC 类型的出站连接设置告警。来自异常路径、执行周期极短的定时任务，也是高度危险的预警信号。

安全研究人员提出了一些防御建议，例如关闭 SSH 密码认证、从生产环境镜像中移除编译器、强制实施出站流量过滤，以及限制从 /dev/shm目录执行程序等举措。

参考及来源：https://www.bleepingcomputer.com/news/security/new-linux-botnet-sshstalker-uses-old-school-irc-for-c2-comms/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fHEm7hZn9HLxeffeicezBTEWTYO8QKYjIc4YmiciaTS1icLu9c62457fhqVakm96en3cWLFoXojdiawzktnfUkKPrtDydzurSJDN9Ge7Tap0AJTg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/fHEm7hZn9HJm18oosAzy6GKLia2zNkMtD6UhDdIoiauibQWPUuVwSiafib7BZMia1HhVcbPQL2l2tMmIJwbiaryOQztX0AExiciaM1eHJYBML3grsRpg/640?wx_fmt=png&from=appmsg)

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