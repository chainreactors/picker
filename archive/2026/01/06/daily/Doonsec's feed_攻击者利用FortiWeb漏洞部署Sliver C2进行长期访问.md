---
title: 攻击者利用FortiWeb漏洞部署Sliver C2进行长期访问
url: https://mp.weixin.qq.com/s/sA007cm0KmkfpinrXvjXPg
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:28:35.085475
---

# 攻击者利用FortiWeb漏洞部署Sliver C2进行长期访问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pcgSUGCDdKLLdGuRqvP8FpSHD8A0rA4KWia9BzG32WTicwoicUCvGSibvpjPibxP27kVYXUU5dBLWVQchP4a5JgUzmw/0?wx_fmt=jpeg)

# 攻击者利用FortiWeb漏洞部署Sliver C2进行长期访问

原创

网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

威胁研究人员发现了一场针对多个大洲 FortiWeb 网络应用程序防火墙的复杂攻击活动，攻击者部署了 Sliver 命令和控制框架来建立持久访问并建立隐蔽的代理基础设施。

该发现源于对 Censys 上例行开放目录威胁搜寻过程中发现的暴露的 Silver C2 数据库和日志的分析，揭示了一项精心策划的行动，该行动利用了过时的 FortiWeb 设备中面向公众的漏洞。

威胁行为者利用多个 FortiWeb 设备上的公共漏洞获得了初始访问权限，特别是针对 5.4.202 到 6.1.62 的过时版本。

研究人员发现证据表明，攻击者利用React2Shell (CVE-2025-55182) 以及未知的 FortiWeb 漏洞来破坏受害者的基础设施。

FortiWeb漏洞利用缺乏概念验证代码，这表明威胁行为者可能瞄准的是零日漏洞或利用尚未公开披露的武器化漏洞。

## **基础设施**

调查确定了两个主要的C2域：ns1.ubunutpackages[.]store 和 ns1.bafairforce[.]军队，两者都托管了Sliver实例。

该威胁行为者展示了高明，创建了冒充合法服务的诱饵网站、虚假的Ubuntu软件库以及伪造的孟加拉国空军招募页面。

对C2创建时间戳的分析显示，首个域名注册于2024年9月，但受害者的入职速度在2025年12月22日至30日间急剧加速，仅八天内就攻破了30个独立主机。

对手通过 systemd 服务和监督者配置修改建立了持久化，将 Sliver 二进制文件伪装成系统更新进程（位于 /bin/.root/system-updater）。

为了便于命令执行和横向移动，威胁行为者部署了快速反向代理（FRP）和一个伪装的微型SOCKS代理，被重新命名为“cups-lpd”，绑定在515端口，伪装成合法的CUPS Line Printer Daemon。这种欺骗战术展现了相当严明的作战纪律。

![Sliver 数据库中与 FRP 服务器相关的 IP 地址。](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKLLdGuRqvP8FpSHD8A0rA4KOGKnkPf3XakrvQgT0mGpkN2VYEOZg0xUq4xIeN7bjQicbleYUC8df9w/640?wx_fmt=png&from=appmsg)

受害者分析显示，巴基斯坦和孟加拉国是重点攻击目标，金融和政府部门有多名受害者。

选择以孟加拉国为主题的诱饵基础设施与观察到的受害者所在地相吻合，这表明此次行动更有针对性，而非机会主义。

分析该二进制文件，我们可以看到它将在 515 端口上暴露 SOCKS 服务，值得注意的是，这是合法的 Linux CUPS 行式打印机守护程序将监听的预期端口。

![Linux CUPS 行式打印机守护进程。](https://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKLLdGuRqvP8FpSHD8A0rA4KWbpIwoibkGsqDVTuSfdt6cKPiaMLWpUKtQSUf5clBslmiaCTM81wcTjcQ/640?wx_fmt=png&from=appmsg)

然而，更广泛的威胁在于一个基本的安全盲点：FortiWeb设备和类似的边缘设备通常缺乏内置的端点检测和响应 (EDR) 功能，而且组织很少部署售后安全工具。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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