---
title: 恶意软件 Stealc “横空出世”，窃密能力一流
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247534975&idx=3&sn=7175ec699c69db35886c4ae07f3c1524&chksm=c1e9c52ef69e4c381fdb2fd3d10b000491e837375d96fc1c6fe70b30e5dda2f38b2c218e4861&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-02-28
fetch_date: 2025-10-04T08:15:22.159914
---

# 恶意软件 Stealc “横空出世”，窃密能力一流

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogspRgbsEyFP3I8P1QgyPuLDMmcIG1kKKozXCiaG1pg5IZlF8e1BRpybTEwKcwwwoCK5qnHaufb2n4A/0?wx_fmt=jpeg)

# 恶意软件 Stealc “横空出世”，窃密能力一流

关键基础设施安全应急响应中心

Bleeping Computer 网站披露，暗网市场出现了一个名为 Stealc 的新恶意软件，由于大肆宣传窃取信息的能力，以及与 Vidar、Raccoon、Mars 和 Redline 等同类恶意软件具有相似性，获得行业内广泛关注。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibDCxKkPoVJvSvukHt4ya3iaD6iad5x5NdL53icSVWPXgib67fHAic0emFsEgSlHI8gUlV9eicn7vHaia1yQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

据悉，2023 年 1 月，网络威胁情报公司 SEKOIA 安全研究人员首次发现了 Stealc ，一个月后，观察到该恶意软件开始进行恶意活动。

# **Stealc 恶意软件在暗网上大肆推广**

最早，一位名叫 Plymouth 的用户在黑客论坛上发布了大量有关 Stealc 的“广告”，宣称其是一种具有广泛数据窃取能力以及具有易使用管理面板的恶意软件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibDCxKkPoVJvSvukHt4ya3iaiaTscAnRkt1CRUUiaXibuZlsUXItlgIcv5X9nhHBZDD1KjSQ293omh41w/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

暗网上宣传 Stealc 的帖子 (SEKOIA)

从“广告”内容来看，Stealc 除了能针对网络浏览器数据、扩展程序和加密货币钱包等典型目标外，还有一个可定制化的文件抓取器，能够人为设置想要窃取的任意文件类型。

发布最初的“宣传广告”后，Plymouth 陆续在其它黑客论坛上大肆推广 Stealc 恶意软件，以期向潜在客户提供测试样本，达成交易。

此外，Plymouth 还特地建立一个 Telegram 频道，专门发布 Stealc 新版本的更新日志（最新版本为 V1.3.0，于 2023 年 2 月 11 日发布），需要警惕的是，该恶意软件正在疯狂迭代中，几乎每周都会推出更新版本。

某些帖子中，Plymouth 指出 Stealc 恶意软件并非从零开发，而是基于 Vidar、Raccoon、Mars 和 Redline 等恶意软件优化而来。研究人员对 Stealc 深入分析后发现，该恶意软件和 Vidar、Raccoon 和 Mars 等确实有相似之处，几者都是通过下载合法的第三方 DLL（如sqlite3.dll、nss3.dll），来窃取受害者敏感数据。

# **Stealc 的功能**

今年 1 月首次发布以来，Stealc 更新了许多功能，其中包括随机化 C2  URL 的系统、更好的日志（被盗文件）搜索和排序系统，以及乌克兰受害者自动排除系统。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibDCxKkPoVJvSvukHt4ya3iahrsTmSUuU7MmhTj3HDw52WWdJrAm73Ebp5gmmQKSV8TLOic4moiaZgMg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

恶意软件开发时间线（SEKOIA）

SEKOIA 通过分析捕获的样本，发现 Stealc 的部分特征如下。

> 轻量级构建：只有 80KB
>
> 使用合法的第三方 DLLs
>
> 用 C 语言编写，滥用 Windows API 函数
>
> 大多数字符串用 RC4 和 base64 进行混淆
>
> 能够自动渗出被盗数据
>
> 攻击目标：22 个网络浏览器、75 个插件和 25 个桌面钱包。

部署过程中，Stealc 恶意软件会对自身字符串进行解密，并执行反分析检查，以确保其不会在虚拟环境或沙盒中运行。之后，立刻动态加载 WinAPI 函数并启动与 C2 服务器的通信，在第一条信息中发送受害者的硬件标识符和构建名称，并接收响应配置。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibDCxKkPoVJvSvukHt4ya3ia4wvyBqNLUeoNNrRmGBXcaaNvMAbxxIPLvCOPs2KyuQ4Sul5sUvTGIQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

目标浏览器的配置指令（SEKOIA）

接下来，Stealc 开始从目标浏览器、扩展程序和应用程序中收集数据，如果处于激活状态，会执行其自定义文件抓取器，最后将所有内容导出到 C2。值得一提的是，窃密活动结束后，Stealc 会把自身和下载的DLL 文件从被感染的主机上删除，以清除入侵痕迹。

研究人员观察到 Stealc 其中之一的传播方式是通过 YouTube，这些视频描述如何安装破解软件并链接到下载网站。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibDCxKkPoVJvSvukHt4ya3iahO2uJd3QXkKbKGTVeoR7RYcoFtkDdKHUS97d0jticVhliaAlkcoS7LGw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

最后，研究人员指出，这些下载的软件中嵌入了 Stealc 恶意软件，一旦用户安装程序，恶意软件就开始了“常规”工作，并迅速与其服务器进行通信。因此建议用户不要安装盗版软件，从官方网站下载产品。

**参考文章：**

https://www.bleepingcomputer.com/news/security/new-stealc-malware-emerges-with-a-wide-set-of-stealing-capabilities/

原文来源：FreeBuf

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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