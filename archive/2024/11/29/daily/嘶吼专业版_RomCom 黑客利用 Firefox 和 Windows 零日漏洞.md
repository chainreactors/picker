---
title: RomCom 黑客利用 Firefox 和 Windows 零日漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247579846&idx=1&sn=0bb37a38ab5998f595038709b86b4063&chksm=e91468fcde63e1ea605e3adce9da5489720e2d21a69c61eb7e63479b335a52d44bd7c62bbffe&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-11-29
fetch_date: 2025-10-06T19:18:06.488395
---

# RomCom 黑客利用 Firefox 和 Windows 零日漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29KLru2P0samDTV3oGjKXMMEOnEFDLqGtBEMynMAmpm0ToicmDHwUT7KwI4Vibt9Fhp26ibBCaZC74UA/0?wx_fmt=jpeg)

# RomCom 黑客利用 Firefox 和 Windows 零日漏洞

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

总部位于俄罗斯的 RomCom 网络犯罪组织在最近针对欧洲和北美 Firefox 和 Tor 浏览器用户的攻击中发现了两个零日漏洞。

第一个漏洞 (CVE-2024-9680) 是 Firefox 动画时间线功能中的释放后使用错误，该功能允许在 Web 浏览器的沙箱中执行代码。Mozilla 于 2024 年 10 月 9 日（ESET 报告该漏洞一天后）修补了该漏洞。

利用的第二个零日漏洞是 Windows 任务计划程序服务中的权限升级漏洞 (CVE-2024-49039)，该漏洞允许攻击者在 Firefox 沙箱之外执行代码。Microsoft 在本月初（即 11 月 12 日）修复了此安全漏洞。

RomCom 将这两个漏洞作为零日链漏洞利用，帮助他们无需用户交互即可获得远程代码执行。他们的目标只需访问一个由攻击者控制的恶意制作的网站，该网站会在其系统上下载并执行 RomCom 后门。

根据攻击中使用的 JavaScript 漏洞之一的名称 (main-tor.js)，威胁者还针对 Tor 浏览器用户（根据 ESET 的分析，版本 12 和 13）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KLru2P0samDTV3oGjKXMMLuzA3Zasicf8Su7HNibUYDuYxblMM7EibriadhkXc3b5DJsoyiaCg8z5evQ/640?wx_fmt=png&from=appmsg)

RomCom 攻击流程

ESET 研究员表示：“妥协链由一个虚假网站组成，该网站将潜在受害者重定向到托管漏洞的服务器，如果漏洞成功，就会执行 shellcode，下载并执行 RomCom 后门。”

虽然不知道假网站的链接是如何分发的，但是，如果使用易受攻击的浏览器访问该页面，则有效负载会被丢弃并在受害者的计算机上执行，无需用户交互。

一旦部署在受害者的设备上，该恶意软件使攻击者能够运行命令并部署额外的有效负载。将两个零日漏洞链接在一起，就会为 RomCom 提供了无需用户交互的漏洞。这种复杂程度也表明了威胁者获取或开发隐秘能力的决心和手段。

此外，这些攻击中成功利用攻击的次数最终导致 RomCom 后门部署在受害者的设备上，这使得人们有理由相信这是一次广泛的活动。根据 ESET 遥测数据，潜在目标的数量从每个国家一名受害者到多达 250 名受害者不等。

这并不是 RomCom 第一次利用零日漏洞进行攻击。2023 年 7 月，其运营商利用多个 Windows 和 Office 产品中的零日漏洞 (CVE-2023-36884) 攻击参加立陶宛维尔纽斯北约峰会的组织。

RomCom（也被追踪为 Storm-0978、Tropical Scorpius 或 UNC2596）与出于经济动机的活动、精心策划的勒索软件和勒索攻击以及凭证盗窃（可能旨在支持情报行动）有关。该威胁组织还与 Industrial Spy 勒索软件行动有关，该组织后来转向地下勒索软件。

据 ESET 称，RomCom 现在还针对乌克兰、欧洲和北美的组织进行跨行业的间谍攻击，包括政府、国防、能源、制药和保险。

参考及来源：https://www.bleepingcomputer.com/news/security/firefox-and-windows-zero-days-exploited-by-russian-romcom-hackers/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KLru2P0samDTV3oGjKXMMKhxalpg5WqQuicVvtciavic9JHDkcNnVkosqibfSCOUP7XlUJ84JE8nDiaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KLru2P0samDTV3oGjKXMMuGw2GEaNRSyW6iauE66q9Wl5XlABxmtDGCJCc79iaMx5v8V0HFcwOOjQ/640?wx_fmt=png&from=appmsg)

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