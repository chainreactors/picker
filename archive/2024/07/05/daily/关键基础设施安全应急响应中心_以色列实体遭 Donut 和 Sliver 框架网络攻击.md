---
title: 以色列实体遭 Donut 和 Sliver 框架网络攻击
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247544738&idx=1&sn=8810ba27667973ca2df9a1cf0480308a&chksm=c1e9a3f3f69e2ae5ae5753bfbda2537eeacfa0662182e80f3ebd93913fc939d1cfa2e1a0f786&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-05
fetch_date: 2025-10-06T17:43:41.016717
---

# 以色列实体遭 Donut 和 Sliver 框架网络攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogsyFdhrDz0Sx06YKiaBWXP5VdWnWtEejickDsPdDicNEcDRyV8VYdU5uZnAEUXYQ4t65meSPe1VFEWBw/0?wx_fmt=jpeg)

# 以色列实体遭 Donut 和 Sliver 框架网络攻击

关键基础设施安全应急响应中心

网络安全研究人员发现了一场针对以色列各实体的攻击活动，该攻击使用了 Donut 和 Sliver 等公开可用的框架。

HarfangLab 在上周的一份报告中表示，此次攻击活动被认为具有高度针对性，“利用针对特定目标的基础设施和定制的 WordPress 网站作为有效载荷传送机制，但影响到不相关垂直领域的各种实体，并依赖于知名的开源恶意软件”。

这家法国公司正在以 Supposed Grasshopper 为名跟踪该活动。它指的是攻击者控制的服务器（“auth.economy-gov-il[.]com/SUPPOSED\_GRASSHOPPER.bin”），第一阶段下载程序会连接到该服务器。

这个用 Nim 编写的下载器很初级，其任务是从暂存服务器下载第二阶段恶意软件。它通过虚拟硬盘 (VHD) 文件进行传输，该文件被怀疑是通过自定义 WordPress 网站传播的，属于驱动下载计划的一部分。

从服务器检索的第二阶段有效载荷是Donut ，一个 shellcode 生成框架，它作为部署名为Sliver的开源Cobalt Strike替代品的管道。

研究人员表示：“运营商还付出了巨大努力，获取专用基础设施并部署真实的 WordPress 网站来投递有效载荷。总的来说，这次活动感觉像是一支小团队的杰作。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6xTRhwG2ZtySZCApoSBk9Am3ZsicbpPH2mpBsSPyubv33WunINL15kWHIb4kXleFibH9a4icEyblYtrw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

该活动的最终目标目前尚不清楚，但 HarfangLab 推测它也可能与合法的渗透测试操作有关，这种可能性引发了一系列有关透明度和冒充以色列政府机构的必要性的问题。

此次披露之际，SonicWall Capture Labs 威胁研究团队详细介绍了一条感染链，该链使用设有陷阱的 Excel 电子表格作为起点，投放一种名为 Orcinius 的木马。

该公司表示：“这是一个多阶段木马，它使用 Dropbox 和 Google Docs 下载第二阶段的有效载荷并保持更新。它包含一个模糊的 VBA 宏，可以挂接到 Windows 中以监视正在运行的窗口和击键，并使用注册表项创建持久性。”

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

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