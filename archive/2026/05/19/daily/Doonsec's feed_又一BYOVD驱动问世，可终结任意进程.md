---
title: 又一BYOVD驱动问世，可终结任意进程
url: https://mp.weixin.qq.com/s/IbolDd0Llcfa2kffjlhRkg
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T05:59:10.063178
---

# 又一BYOVD驱动问世，可终结任意进程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibXL9MCj2GqNn2tvSEic9MRQ521ScxW6cHK8XaeyFIYoLjDQZOEjfNJmn3riczFhosEBlT6MJPPKxOjVlELDhtcNQrhAUNF2QY7WCPicg02LXVo/0?wx_fmt=jpeg)

# 又一BYOVD驱动问世，可终结任意进程

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 又一BYOVD驱动问世，可终结任意进程

### 一、背景

日常研究发现，一个联想驱动被公开[1]可用于BYOVD攻击，具备终结任意进程的能力。代号`Phantom Killer（幽灵杀手）`。

经过复现，在安装了某国产"杀毒"软件的 `windows-11-x64-24H2`下，整个过程没有受到任何阻止。由于该驱动非常知名，杀毒软件可能默认白名单。

![PhantomKiller复现](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqMerawrMnicLkLiaia2d9TEJYZ4kAARibC6mxsia3R4HxP13xJDrFDGSbTVQ0h4ftAZR5kZdHzBS5Sxdnck6vXnSoRKOdvJtjzV0Qf0/640?wx_fmt=png&from=appmsg "null")

PhantomKiller复现

> BootRepair.sys可能是联想电脑管家附带的合法驱动程序，推测应该是用于系统修复/启动修复功能。该驱动没有DACL，意味着任何用户/进程都能与这个驱动通信，包括低权限用户。二是暴露危险的 IOCTL 命令0x222014，该IOCTL接受一个 4 字节的 PID 并调用ZwTerminateProcess。作者发现了这个缺陷并公开了技术细节。

![驱动信息](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqPjP3C3ib13hO9g2Sp3J1lDI7FJd1gkyavsMax0icyYnpD2CgYDF6cdzicNpeM75fsx3JickHJxsbftYtMw3Yrm6iaUCRepjSflQCjg/640?wx_fmt=png&from=appmsg "null")

驱动信息

| 字段 | 值 |
| --- | --- |
| 文件名称 | BootRepair.sys |
| SHA256 | 5ab36c116767eaae53a466fbc2dae7cfd608ed77721f65e83312037fbd57c946 |
| 签名者 | 联想（赛门铁克 Class 3 SHA256 代码签名 CA） |
| 编译时间 | 2018-01-03 |
| 架构 | x64 |
| VT 检测结果 | 0/71 截至5月19日23点 |

![VT 检测结果](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqMpm6JkZsGrTKQHEN3t7BJyQaZ0dQ3JJnMrlgiaUzjIhzQibN6Dfj8Wb2gNrpvWybHu8p07WkmlnWdEUTJwDhY4g4pxvP3SVayt4/640?wx_fmt=png&from=appmsg "null")

VT 检测结果

完整报告：幽灵杀手：逆向工程并利用联想驱动程序终止EDR进程[2]

---

### 二、修复方案

对于杀毒软件厂商，无非是将其拉黑。对于红队，估计马上会被加入到BYOVD全球集合BYOVD[3]。不过话说回来，可以跟着学习下这篇文章别人怎么做的。

### 三、总结

一个合法签名的内核驱动，可能比勒索软件更危险。它的存在不是特例，而是硬件与工具厂商普遍缺乏安全开发生命周期（SDL）经验的缩影。从戴尔的 dbutil\_2\_3.sys 到联想的 BootRepair.sys，再到技嘉、华硕等多个厂商的类似问题，攻击者早已将“合法驱动滥用”作为提权和持久化的标准手段。

---

### 四、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

* • 仅可用于已获得书面授权的目标系统测试；
* • 遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

---

#### 引用链接

`[1]` : *https://github.com/redteamfortress/PhantomKiller*
`[2]` 幽灵杀手：逆向工程并利用联想驱动程序终止EDR进程: *https://medium.com/@jehadbudagga/phantom-killer-reverse-engineering-and-weaponizing-a-lenovo-driver-to-terminate-edr-processes-9191cd06374f*
`[3]` BYOVD: *https://github.com/BlackSnufkin/BYOVD*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

白帽子安全笔记2.0

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

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