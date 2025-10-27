---
title: 新型APT组织CloudSorcerer瞄准俄罗斯政府
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247544810&idx=3&sn=d97510e8e11881fff644917260d0f722&chksm=c1e9a3bbf69e2aadcca603f0f2bb57580d1738a5c67bf1a4dfc15c7819b2a2860552bb6ae2ed&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-11
fetch_date: 2025-10-06T17:45:14.554027
---

# 新型APT组织CloudSorcerer瞄准俄罗斯政府

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogtuzSJicNnRQtibYkLm0tgR3GALuia2XuK948Bbptbk3NlJ3y6apgPGtZcfrUYCKoNLzC9QBaicCsr7hg/0?wx_fmt=jpeg)

# 新型APT组织CloudSorcerer瞄准俄罗斯政府

关键基础设施安全应急响应中心

网络安全公司卡巴斯基发现，一个名为 CloudSorcerer的新型APT组织通过滥用公共云服务，对俄罗斯政府机构实施攻击并窃取数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogtuzSJicNnRQtibYkLm0tgR3GfVjohRq2DbekmFNZuDroRticzHCwbTpbr5qSiaribVLVuqzclia9AJyvJQ/640?wx_fmt=png&from=appmsg)

卡巴斯基于 2024 年 5 月发现了这一活动，攻击者采用的技术与 CloudWizard 相似，但指出了恶意软件源代码的不同之处，称这是一种复杂的网络间谍工具，通过Microsoft Graph、Yandex Cloud和 Dropbox 云基础设施进行隐形监控、数据收集和泄露。

该恶意软件利用云资源作为其命令和控制（C2）服务器，通过使用身份验证令牌的 API 访问这些资源。此外，CloudSorcerer 还使用 GitHub 作为其初始 C2 服务器。目前尚不清楚用于渗透目标的确切方法，但初始访问被用来投放基于 C 语言的便携式可执行程序二进制文件，该二进制文件可用作后门、启动 C2 通信，或根据其执行的进程向其他合法进程注入 shellcode。

卡巴斯基指出，该恶意软件能够根据所运行的进程动态调整其行为，再加上它通过 Windows 管道使用复杂的进程间通信，这进一步凸显了它的复杂性。后门组件旨在收集受害者机器的信息，并检索指令以枚举文件和文件夹、执行 shell 命令、执行文件操作和运行其他有效载荷。

此外，恶意软件的后门组件能收集受害者机器的信息，并获取枚举文件和文件夹、执行shell命令、执行文件操作和运行其他有效载荷的指令。

C2模块则连接到一个GitHub页面，该页面充当死区解析器（dead drop resolver），以获取一个十六进制字符串，该字符串指向托管在Microsoft Graph或Yandex Cloud上的实际服务器。此外，CloudSorcerer没有连接到GitHub，而是试图从一个基于俄罗斯云的照片托管服务器获取相同的数据。

由于使用 Microsoft Graph、Yandex Cloud 和 Dropbox 等云服务作为 C2 基础设施，并使用 GitHub 进行初始 C2 通信，显示这是通过精心策划的网络间谍攻击。

总体而言，CloudSorcerer 后门是一种强大的工具，使攻击者能够在受感染的机器上执行恶意操作。目前卡巴斯基已发布用于检测CloudSorcerer恶意软件的入侵指标（IoC）和Yara规则。

**参考资料：**

https://thehackernews.com/2024/07/new-apt-group-cloudsorcerer-targets.html

原文来源：FreeBuf

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