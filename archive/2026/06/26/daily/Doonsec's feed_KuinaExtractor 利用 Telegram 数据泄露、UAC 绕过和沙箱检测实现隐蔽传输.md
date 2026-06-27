---
title: KuinaExtractor 利用 Telegram 数据泄露、UAC 绕过和沙箱检测实现隐蔽传输
url: https://mp.weixin.qq.com/s/NgmBHlIV8zH0gxA66jVP8w
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:46:25.900596
---

# KuinaExtractor 利用 Telegram 数据泄露、UAC 绕过和沙箱检测实现隐蔽传输

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NWt13SdImq1IB6eNIVGuxibfasQI8f7UBdwriaoaZw6e5uFiaicD62SXGM6Nj7BL07OeVeoOWuuPoMP4YGuukMzCtWiceZDnt68iboQ/0?wx_fmt=jpeg)

# KuinaExtractor 利用 Telegram 数据泄露、UAC 绕过和沙箱检测实现隐蔽传输

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一种名为 KuinaExtractor 的新近发现的信息窃取程序已经悄然发展了六个多月，对多个平台上的用户构成了严重且日益增长的威胁。

该恶意软件使用 Rust 编程语言编写，目标是浏览器数据、加密货币钱包以及包括 Roblox、Steam 和 Discord 在内的热门服务的凭据。

这种威胁尤其令人担忧的地方在于它发展迅速，在短短几个月内就从粗糙的早期版本变成了一个完善的、隐蔽的工具。

KuinaExtractor 于 2025 年 12 月首次出现，此后经历了四个不同的开发阶段，每个阶段都增加了新的功能和更深层次的规避技术。

该恶意软件的作者似乎是一位讲越南语的开发者，代码中到处都是越南语文本，包括调试输出和系统消息。

越南境内托管的指挥控制面板以及针对越南 CocCoc 浏览器的攻击进一步支持了这一评估，但研究人员指出，这些只是佐证信号，而非确凿证据。

ThreatRay 的分析师通过比较函数级别的代码相似性，识别并跟踪了 KuinaExtractor 长达六个月，从而将数十个样本关联到一个恶意软件家族中。

根据 ThreatRay 向网络安全新闻 (CSN) 分享的报告，相同的标记在不同的版本中反复出现，包括共享的互斥体名称、二进制文件中留下的构建主机路径，以及与别名“Kuina”（后来被“k0to”取代）关联的一组一致的 Telegram 联系人用户名。

该恶意软件的开发路径异常清晰且精心策划。最早的版本就已包含绕过 Chrome 应用绑定加密的功能，该功能会伪装成 Windows 核心进程来恢复浏览器的主加密密钥。

早期版本的数据外泄是通过 Discord Webhook 实现的，而 GitHub 则被用作交付平台和通过 GitHub Actions 提供的临时远程基础设施。如今，GitHub 仍然承担着这一基础设施角色。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PiaYPby2Znpn5Vpdicaux3ia9XPYZ5spyysqM0xjZlsHhMZ89Vc8xT0s0p5yEIL2GImk6aDmlEsaMYZb6pvVXSdUv69d8NAV1sia4/640?wx_fmt=png&from=appmsg)

到 2026 年 6 月，开发商已将该项目重新命名为“k0to”，并将重点从添加新功能转移到隐藏现有功能。

最新版本使用 28 字节 XOR 加密对字符串进行封装，提供自己的证书根，而不是依赖系统的受信任存储，并添加了沙箱检查，扫描 PowerShell 窗口标题以查找分析工具。

这些变化表明，公司明显倾向于长期隐蔽发展，而不是快速发展功能。

## **KuinaExtractor 利用 Telegram 数据泄露、UAC 绕过和沙箱检测**

KuinaExtractor 在 2026 年 1 月重建时，数据外泄从 Discord webhook 转移到了 Telegram 机器人，这使得操作员拥有了更大的控制权，也使得流量更难被标记。

与此同时，第一个版本中唯一的UAC绕过方法被一个函数指针表所取代，该表提供了七种不同的绕过技术。这种冗余设计意味着，如果其中一条权限提升路径被阻止，恶意软件可以尝试多条其他权限提升路径。

1 月份的重写版本还增加了在数据窃取开始前进行大量侦察的步骤。在主要窃取程序运行之前，会执行八项硬件查询，包括使用 WMIC、WiFi 网络枚举、Windows 凭据管理器转储以及受害者 IP 地理位置定位。

该恶意软件还包含一个旨在禁用 Microsoft Defender 的循环。到 2026 年 3 月，受感染的浏览器已增至约 40 个应用程序，而绕过 UAC 的方法也转向了 SilentCleanup 技术。

在开发主窃取工具的同时，同一运营者还运行了两个后来被放弃的副项目。第一个项目名为 KuinaCookieExtractor，目标是包括 Minecraft、FileZilla 和 Telegram 在内的平台，但其窃取数据并非通过 Telegram，而是通过 Discord。

它持续存在了大约两周。第二个名为“Zenith”的实验短暂出现，它提供了一个调试版本，在受害者的桌面上留下了详细的日志，并在一个越南IP地址上提供了一个控制面板，之后便被放弃了。

这些实验表明，运营者会积极测试各种想法，然后舍弃那些不符合总体计划的内容。所有项目中代码标记、构建用户名和 Telegram 账号的一致重复使用，将每个实验都追溯到同一个人。

监控该家族的安全团队应将任何携带这些共享标记的样本视为同一威胁行为者的活动的一部分，无论二进制文件中显示的名称是什么。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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