---
title: Cicada3301 勒索软件的 Linux 加密器针对 VMware ESXi 系统
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546770&idx=2&sn=6cd7b330538f692c55e1e00c224e934b&chksm=fa938153cde40845ed7bacf94d12e55779ffbc935287f43bcaf11b57a084e7e7b78c99cc045d&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-09-06
fetch_date: 2025-10-06T18:27:58.352785
---

# Cicada3301 勒索软件的 Linux 加密器针对 VMware ESXi 系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lJAmZkIgtjYeooEmhZq2juBSia0picDHLg8miarvRXzxX2WUWBAvpUUia6riazR07cjAz4TqUodfoRHtw/0?wx_fmt=jpeg)

# Cicada3301 勒索软件的 Linux 加密器针对 VMware ESXi 系统

网络安全应急技术国家工程中心

一个名为 Cicada3301 的新勒索软件即服务 (RaaS) 行动迅速在全球发起了网络攻击，已在其勒索门户网站上列出了 19 名受害者。

这项新的网络犯罪行动以游戏命名，该游戏涉及复杂的加密谜题，并使用相同的徽标在网络犯罪论坛上进行推广。然而，其实两者之间没有任何联系。

Cicada3301 RaaS 已于 2024 年 6 月 在勒索软件和网络犯罪论坛 RAMP 的论坛帖子中首次开始推广该行动并招募会员。

然而，外媒早已注意到 Cicada 攻击，这表明该团伙在试图招募分支机构之前是独立运作的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29cdFX3Apjp7ob65jyJEGMlQJGFhNlj3ucHdbjawWzTiaNPtq99mfy9R8Q9PZIcic5I7LQyiatQmSaLA/640?wx_fmt=png&from=appmsg&wxfrom=13)

Cicada3301 勒索软件运营商在 RAMP 论坛上寻找附属机构

与其他勒索软件操作一样，Cicada3301 采取双重勒索策略，即入侵公司网络、窃取数据，然后加密设备。然后利用加密密钥和泄露被盗数据的威胁作为手段，恐吓受害者支付赎金。

威胁者运营一个数据泄露网站，将其用作双重勒索计划的一部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29cdFX3Apjp7ob65jyJEGMlnXgPjexb4ZHLjT0CZQ9exricof2RjJFdbaMLEUJ29aMLiaJoPCc9SccQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Cicada3301 勒索门户

Truesec 对新恶意软件的分析显示，Cicada3301 与 ALPHV/BlackCat 之间存在显著的重叠，表明可能是由前 ALPHV 核心团队成员创建的品牌重塑或分叉。

这是基于以下事实：

·两者都是用 Rust 编写的。

·两者都使用 ChaCha20 算法进行加密。

·两者都使用相同的 VM 关闭和快照擦除命令。

·两者都使用相同的用户界面命令参数、相同的文件命名约定和相同的勒索信解密方法。

·两者都对较大的文件使用间歇性加密。

具体来说，ALPHV 在 2024 年 3 月初实施了一次退出骗局，涉及虚假声称 FBI 正在进行的打击行动，此前他们从 Change Healthcare 的一家附属公司窃取了 2200 万美元的巨额付款。

Truesec 还发现有迹象表明，Cicada3301 勒索软件行动可能与 Brutus 僵尸网络合作或利用该网络对企业网络进行初始访问。该僵尸网络之前曾与针对思科、Fortinet、Palo Alto 和 SonicWall 设备的全球规模 VPN 暴力破解活动有关。

值得注意的是，Brutus 活动是在 ALPHV 关闭运营两周后首次发现的，因此从时间线来看，这两个组织之间的联系仍然存在。

# **VMware ESXi 面临另一个威胁**

Cicada3301 是一款基于 Rust 的勒索软件，同时具有 Windows 和 Linux/VMware ESXi 加密器。作为 Truesec 报告的一部分，研究人员分析了勒索软件操作的 VMWare ESXi Linux 加密器。

与 BlackCat 和其他勒索软件系列（如 RansomHub）一样，必须输入特殊密钥作为命令行参数才能启动加密器。此密钥用于解密加密的 JSON blob，其中包含加密器在加密设备时将使用的配置。

Truesec 表示，加密器会使用密钥解密勒索信来检查密钥的有效性，如果成功，则继续执行其余的加密操作。

其主要功能（linux\_enc）使用 ChaCha20 流密码进行文件加密，然后使用 RSA 密钥加密过程中使用的对称密钥。加密密钥是使用“OsRng”函数随机生成的。

Cicada3301 针对与文档和媒体文件匹配的特定文件扩展名，并检查其大小以确定在哪里应用间歇性加密（> 100MB）以及在哪里加密整个文件内容（<100MB）。

在加密文件时，加密器会在文件名后附加一个随机的七个字符的扩展名，并创建名为“RECOVER-[扩展名]-DATA.txt”的勒索信，如下所示。

值得注意的是，BlackCat/ALPHV 加密器也使用了随机的七个字符的扩展名和名为“RECOVER-[扩展名]-FILES.txt”的勒索信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29cdFX3Apjp7ob65jyJEGMluX7CyFLEricN0bOm3gaWIHCQRk7SntVOJff65aC8wbKcUwQ3V8K3w2Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Cicada3301 勒索信

勒索软件的操作员可以设置休眠参数来延迟加密器的执行，从而可能逃避立即检测。“no\_vm\_ss”参数还命令恶意软件加密 VMware ESXi 虚拟机而不尝试先关闭它们。

但是，默认情况下，Cicada3301 首先使用 ESXi 的“esxcli”和“vim-cmd”命令关闭虚拟机并删除其快照，然后再加密数据。

```
esxcli –formatter=csv –format-param=fields==\”WorldID,DisplayName\” vm process list | grep -viE \”,(),\” | awk -F \”\\\”*,\\\”*\” \'{system(\”esxcli vm process kill –type=force –world-id=\”$1)}\’ > /dev/null 2>&1;for i in `vim-cmd vmsvc/getallvms| awk \'{print$1}\’`;do vim-cmd vmsvc/snapshot.removeall $i & done > /dev/null 2>&1
```

Cicada3301 的成功率表明攻击者经验丰富，且目的明确清晰。这进一步支持了 ALPHV 重启的假设，或者至少利用了具有勒索软件经验的关联方。

新勒索软件专注于 ESXi 环境，凸显了其战略设计，旨在最大限度地破坏企业环境，而许多威胁者现在将企业环境作为获利目标。

Cicada3301 将文件加密与破坏虚拟机操作和删除恢复选项的能力相结合，确保可以发起影响整个网络和基础设施的高影响力攻击，从而最大限度地给受害者施加压力。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/cicada3301-ransomwares-linux-encryptor-targets-vmware-esxi-systems/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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