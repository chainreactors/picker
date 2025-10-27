---
title: Helldown 勒索软件利用 Zyxel 漏洞破坏企业网络
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247579721&idx=1&sn=971afc08efdeab4cd0d06a7f9e64bfc3&chksm=e9146873de63e165a30c8430200b8a313541ca00ca678b55d91b9e43a6280c5d142be91a12ed&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-11-22
fetch_date: 2025-10-06T19:17:16.986156
---

# Helldown 勒索软件利用 Zyxel 漏洞破坏企业网络

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFvILVuPvlwF1AZ2E3YnBc6eOMNOEemjLof0jJibiaTvdJKy9QUC3icnWuFw/0?wx_fmt=jpeg)

# Helldown 勒索软件利用 Zyxel 漏洞破坏企业网络

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

据悉，新的“Helldown”勒索软件攻击目标是 Zyxel 防火墙中的漏洞，以破坏企业网络，从而窃取数据和加密设备。

尽管不是勒索软件领域的主要参与者，但 Helldown 自夏季推出以来迅速发展，在其数据勒索门户网站上有众多受害者。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFv5Cc5CA5I8wufkz0btpjKOKwVTsej3cZiaKY1rXoJ9dcicWmlRpB3QJbA/640?wx_fmt=png&from=appmsg)

受害者公告

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFvFpO57kfjCxRhalZTApbib4ogqzPTSicZSwkaeo6APcIvjv3EB9kkSHzQ/640?wx_fmt=png&from=appmsg)Helldown 发现和概述

Helldown 首次由 Cyfirma 于 2024 年 8 月 9 日记录，随后由 Cyberint 于 10 月 13 日再次记录，两次都简要描述了新的勒索软件操作。

360NetLab 安全研究员于 10 月 31 日首次报告了针对 VMware 文件的 Helldown 勒索软件 Linux 变体。该 Linux 变体具有列出和杀死虚拟机以加密图像的代码，但其功能仅被部分调用，这表明它可能仍在开发中。

相关报告称，Windows 版 Helldown 基于泄露的 LockBit 3 构建器，其操作功能与 Darkrace 和 Donex 相似。然而，根据现有证据，无法得出明确的联系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFvWibGyRZLzu0YC2feaKVxiaAQrmk1Ev7fjCOD8v6ksGsvSLF4bJdEOIZA/640?wx_fmt=png&from=appmsg)

配置文件相似之处

截至 2024 年 11 月 7 日，该威胁组织在其最近更新的勒索门户网站上列出了 31 名受害者，其中主要是总部位于美国和欧洲的中小型公司。截至今天，该数字已减少至 28 人，这种减少表明可能有人支付了赎金。

Helldown 在窃取数据方面不像其他组织那样有选择性，采用更有效的策略，并在其网站上发布大型数据包，一次数据包高达 431GB。

列出的受害者之一是网络和网络安全解决方案提供商 Zyxel Europe。该组织的加密器看起来并不是非常先进，威胁者利用批处理文件来结束任务，而不是直接将此功能合并到恶意软件中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFvUx9l2ZMkbqkRrv6v3qd1cmwvSJ6KPsgjp4icJRicQI0qYiaibtXLV9qibTg/640?wx_fmt=png&from=appmsg)

通过批处理文件终止进程

加密文件时，威胁者将生成随机受害者字符串，例如“FGqogsxF”，该字符串将用作加密文件的扩展名。勒索字条还在其文件名中使用了该受害者字符串，例如“Readme.FGqogsxF.txt”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFvgRNyhTs2wTKafDY9shfh4fF8c8sT4OocRWlcDkaCuVMST2kZ8EgV0Q/640?wx_fmt=png&from=appmsg)

Helldown 勒索信

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFvFpO57kfjCxRhalZTApbib4ogqzPTSicZSwkaeo6APcIvjv3EB9kkSHzQ/640?wx_fmt=png&from=appmsg)指向 Zyxel Europe 的证据

安全研究人员通过 Zyxel Europe 相关的研究发现，Helldown 网站上列出的至少 8 名受害者在发生违规时使用了 Zyxel 防火墙作为 IPSec VPN 接入点。并注意到 11 月 7 日的 Truesec 报告提到，在 Helldown 攻击中使用了名为“OKSDW82A”的恶意帐户，并且还使用了一个配置文件（“zzz1.conf”）作为针对基于 MIPS 的设备的攻击的一部分。

威胁者使用此帐户通过 SSL VPN 与受害者网络建立安全连接、访问域控制器、横向移动并关闭端点防御。

通过进一步调查，又在 Zyxel 论坛上发现了有关创建可疑用户帐户“OKSDW82A”和配置文件“zzz1.conf”的报告，设备管理员报告称他们使用的是固件版本 5.38。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFvhpqCUDblZbkt7MBwgJUbd27IeQRXp14Q45uRmGuLk4w8emAA1GSnIQ/640?wx_fmt=png&from=appmsg)

连接 Helldown 活动中的各个点

根据该版本的安全研究人员推测 Helldown 可能正在使用 CVE-2024-42057，这是一种 IPSec VPN 中的命令注入，允许未经身份验证的攻击者在基于用户的 PSK 模式下使用精心设计的长用户名执行操作系统命令。

该问题已于 9 月 3 日随着固件版本 5.39 的发布得到修复，且利用细节尚未公开，因此 Helldown 疑似获得了利用漏洞。

此外，研究人员还发现了 10 月 17 日至 22 日期间从俄罗斯上传到 VirusTotal 的有效负载，它包含一个 base64 编码的字符串，解码后会显示 MIPS 架构的 ELF 二进制文件。然而，有效负载似乎不完整。

参考及来源：https://www.bleepingcomputer.com/news/security/helldown-ransomware-exploits-zyxel-vpn-flaw-to-breach-networks/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFvT4vYU56hbZVkt5bPF7y7Hw6PTvK3EmbjrhLDL5IsfGeFomgW2khXwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic36dTM7OGaJF2Bm62GiaNFvkBmp21FWLPFCAISbRGgCSt6M492QjjIdIlySMHVaSIm5MiaNicg8uYiag/640?wx_fmt=png&from=appmsg)

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