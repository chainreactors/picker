---
title: 恶意软件利用零日漏洞感染报废的AVTECH IP 摄像机
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545632&idx=3&sn=1a5b5a9455da06cb57832c3cacf88afe&chksm=c1e9bf71f69e3667fac031d888ccd6cb7f0e63da1d6576e16b42056153c55fa308a12c21070f&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-09-05
fetch_date: 2025-10-06T18:27:21.065354
---

# 恶意软件利用零日漏洞感染报废的AVTECH IP 摄像机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguCkXImNTlibL0iaEiax1hnkkAEa9ZN7icu5icsibE9t13H7dAW8gykuLicpuo9oPIxuQIXXST0s95LPEI0g/0?wx_fmt=jpeg)

# 恶意软件利用零日漏洞感染报废的AVTECH IP 摄像机

关键基础设施安全应急响应中心

基于 Corona Mirai 的恶意软件僵尸网络通过 AVTECH IP 摄像机中存在 5 年之久的远程代码执行 (RCE) 零日漏洞进行传播，目前这些摄像机已停产多年，不会收到补丁。

该漏洞由 Akamai 的 Aline Eliovich 发现，编号为 CVE-2024-7029，是摄像机“亮度”功能中的一个高严重性问题，CVSS v4 评分为8.7，允许未经身份验证的攻击者使用特制的请求通过网络注入命令。

具体来说，这个易于利用的漏洞存在于 AVTECH 摄像机固件的“action=”参数中的“亮度”参数中，该参数旨在允许远程调整摄像机的亮度，影响所有运行 Fullmg-1023-1007-1011-1009 固件版本的 AVTECH AVM1203 IP 摄像机。

由于受影响的型号已于 2019 年达到使用寿命 (EoL)，因此没有补丁可以解决 CVE-2024-7029，并且预计不会发布修复程序。

美国网络安全和基础设施安全局在本月初发布了一份公告，警告 CVE-2024-7029 及其公开漏洞的可用性，并警告这些摄像头仍在商业设施、金融服务、医疗保健和公共卫生以及交通系统中使用。

该漏洞的概念验证 (PoC) 漏洞至少自 2019 年起就已存在，但本月才分配了 CVE，并且之前尚未观察到任何主动利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28q6kHxJHH7zCB7L02agOyUmlVr6ZPcqmEFiawwZl4JJj4MZs1eJk69GrrRjQwZ1wKicYNBk4eMITZg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

CVE-2024-7029 的 PoC 漏洞利用

# **正在进行开发**

Corona 是一个基于 Mirai 的变种，至少从 2020 年就已经存在，利用物联网设备中的各种漏洞进行传播。

Akamai 的 SIRT 团队报告称，从 2024 年 3 月 18 日开始，Corona 开始在野外利用 CVE-2024-7029 发动攻击，目标是仍在使用的 AVM1203 摄像机，尽管它们五年前就已经达到 EoL。

观察到的第一次活跃活动始于 2024 年 3 月 18 日，但分析显示，该变体早在 2023 年 12 月就已开始活动。CVE-2024-7029 的概念验证 (PoC) 至少从 2019 年 2 月起就已公开，但直到 2024 年 8 月才有适当的 CVE 分配。

Akamai 的蜜罐捕获的 Corona 攻击利用 CVE-2024-7029 下载并执行 JavaScript 文件，进而将主要僵尸网络负载加载到设备上。

一旦嵌入到设备上，恶意软件就会连接到其命令和控制 (C2) 服务器并等待执行分布式拒绝服务 (DDoS) 攻击的指令。

根据 Akamai 的分析，Corona 针对的其他缺陷包括：

·CVE-2017-17215：品牌路由器中存在的一个漏洞，远程攻击者可以利用 UPnP 服务中的不当验证在受影响的设备上执行任意命令。

·CVE-2014-8361：Realtek SDK 中的远程代码执行 (RCE) 漏洞，常见于消费级路由器。该漏洞可通过这些路由器上运行的 HTTP 服务被利用。

·Hadoop YARN RCE：Hadoop YARN（又一个资源协商器）资源管理系统中的漏洞，可被利用在 Hadoop 集群上执行远程代码。

建议 AVTECH AVM1203 IP 摄像机的用户立即将其下线并替换为更新的、积极支持的型号。

由于 IP 摄像头通常暴露在互联网上，因此很容易成为威胁者的目标，因此它们应始终运行最新的固件版本，以确保已知错误得到修复。如果设备停产，应将其更换为较新的型号，以继续接收安全更新。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/malware-exploits-5-year-old-zero-day-to-infect-end-of-life-ip-cameras/

原文来源：嘶吼专业版

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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