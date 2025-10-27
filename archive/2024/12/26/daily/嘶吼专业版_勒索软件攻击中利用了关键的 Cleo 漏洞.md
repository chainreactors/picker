---
title: 勒索软件攻击中利用了关键的 Cleo 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580423&idx=1&sn=4a44563ed7ec0aafc5aaa48302756b22&chksm=e9146b3dde63e22b4167d8ad47bf789091878f5888de0896d7e3644afa417b63b98c275f1407&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-12-26
fetch_date: 2025-10-06T19:39:48.053369
---

# 勒索软件攻击中利用了关键的 Cleo 漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibibmE7O1f1vT47LaO8NURG5hBhT3KMLoNkzPvV2OpGeZIjuJSFsiaDZZbich0jBpEmzgakdE4VqhLDw/0?wx_fmt=jpeg)

# 勒索软件攻击中利用了关键的 Cleo 漏洞

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

根据 CISA 最新发现，确定 Cleo Harmony、VLTrader 和 LexiCom 文件传输软件中的一个关键安全漏洞正在被勒索软件攻击所利用。

此漏洞编号为 CVE-2024-50623，影响 5.8.0.21 之前的所有版本，使未经身份验证的攻击者，能够在在线暴露的易受攻击的服务器上远程执行代码。

Cleo 于 10 月份发布了安全更新来修复该问题，并警告所有客户“立即升级实例”以应对其他潜在的攻击媒介。目前尚未透露 CVE-2024-50623 是在野外的攻击目标。然而，CISA 将该安全漏洞添加到其已知被利用漏洞的目录中，并将其标记为用于勒索软件活动。

在添加到 KEV 目录后，美国联邦机构必须按照 2021 年 11 月发布的具有约束力的操作指令 (BOD 22-01) 的要求，在 1 月 3 日之前提出申请，确保其网络免受攻击。

虽然网络安全机构没有提供有关针对易受 CVE-2024-50623 漏洞，利用的 Cleo 服务器的勒索软件活动的任何其他信息，但这些攻击与之前利用 MOVEit Transfer、GoAnywhere MFT 中的零日漏洞的 Clop 数据盗窃攻击惊人地相似，以及近年来的Accellion FTA。

一些人还认为该漏洞被 Termite 勒索软件操作所利用。然而，这个链接只是因为 Blue Yonder 拥有暴露的 Cleo 软件服务器，并且在勒索软件团伙声称的网络攻击中遭到破坏。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibibmE7O1f1vT47LaO8NURG50UONcOLgDakz5iaVKAxSpI5b5YVAycBuwBfcc7POZRNWFYxzYG2QEHg/640?wx_fmt=png&from=appmsg)Cleo 零日漏洞也被积极利用

正如 Huntress 安全研究人员首次发现的那样，经过全面修补的 Cleo 服务器仍然受到威胁，很可能使用 CVE-2024-50623 绕过（尚未收到 CVE ID），使攻击者能够导入和执行任意 PowerShell 或 bash 命令通过利用默认的自动运行文件夹设置。

Cleo 现已发布补丁来修复这个被积极利用的零日漏洞，并敦促客户尽快升级到版本 5.8.0.24，以保护暴露在互联网上的服务器免受破坏尝试。应用补丁后，系统会记录启动时发现的与此漏洞相关的任何文件的错误，并删除这些文件。

建议无法立即升级的管理员通过从系统选项中清除 Autorun 目录来禁用自动运行功能，以减少攻击面。正如 Rapid7 在调查零日攻击时发现的那样，威胁者利用零日攻击来删除 Java Archive (JAR) 有效负载 [VirusTotal]，该负载是更大的基于 Java 的后利用框架的一部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibibmE7O1f1vT47LaO8NURG5fdfASXdpYd08ZvhO5cAw7hzCCX5BA3lKoAib1qIibTuDCibtyG51xqo1Q/640?wx_fmt=png&from=appmsg)

Cleo 攻击流程

Huntress 也分析了该恶意软件并将其命名为 Malichus，目前只发现它部署在 Windows 设备上。

根据另一家调查正在进行攻击的网络安全公司 Binary Defense ARC Labs 的说法，恶意软件操作者可以使用 Malichus 进行文件传输、命令执行和网络通信。

到目前为止，Huntress 已发现多家公司的 Cleo 服务器遭到入侵，并表示可能还有其他潜在受害者。Sophos 的 MDR 和实验室团队还在 50 多个 Cleo 主机上发现了妥协迹象。截止到目前，Cleo 发言人确认 CVE-2024-50623 漏洞已被作为零日攻击利用。

参考及来源：https://www.bleepingcomputer.com/news/security/cisa-confirms-critical-cleo-bug-exploitation-in-ransomware-attacks/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibibmE7O1f1vT47LaO8NURG5181iatCKa9Uzu6x1BFnPHVGUTKV7DvIRrLu7vMTfsEZC4ibibv5geLicKw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibibmE7O1f1vT47LaO8NURG5ozcZ5ODIhOoQK43YbEfUOliczyRYoZOwNHCcwkVH1bcyicBF9o345Dbg/640?wx_fmt=png&from=appmsg)

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