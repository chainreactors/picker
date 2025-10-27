---
title: 以拉丁美洲为目标的银行木马盗取多达90,000份账户凭证
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535648&idx=2&sn=80790335fe7dc387dd187f9eb531a9a7&chksm=fa93fae1cde473f7b1269aedb3591419e8fcc11302afd2239ea4edf3c2908c6086852b1e9e5d&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-23
fetch_date: 2025-10-04T10:24:26.713186
---

# 以拉丁美洲为目标的银行木马盗取多达90,000份账户凭证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kTNyvzk9k844Qzzgh3MEzKKVKXFZlqoFExmgjKoINcGDednJbPDs6tm1KOkO9u9b95Y4xQjNtxmQ/0?wx_fmt=jpeg)

# 以拉丁美洲为目标的银行木马盗取多达90,000份账户凭证

网络安全应急技术国家工程中心

一个名为Mispadu的银行木马与多个针对玻利维亚、智利、墨西哥、秘鲁和葡萄牙等国家的垃圾邮件活动有关，其目的是窃取凭证并提供其他有效载荷。

拉丁美洲网络安全公司 Metabase Q 的 Ocelot 团队在与黑客新闻分享的一份报告中表示，这项活动于 2022 年 8 月开始，目前正在进行中。

certutil 方法使 Mispadu 能够绕过各种安全软件的检测，并从超过 17,500 个独特的网站获取超过 90,000 个银行账户凭证，其中包括许多政府网站：智利 105 个，墨西哥 431 个，秘鲁 265 个。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6zQ7MPicAJ1N0W1a5B98Gl4MMJZUvS8VPNCVaW9whUHkgYaTYibicahVskY3532WwIf5Fp1OoED4q2tA/640?wx_fmt=png)

Mispadu（又名 URSA）于 2019 年 11 月首次被 ESET记录，描述了其进行货币和凭据盗窃以及通过截屏和捕获击键充当后门的能力。

“他们的主要策略之一是破坏合法网站，搜索易受攻击的 WordPress 版本，将它们变成他们的命令和控制服务器，从那里传播恶意软件，过滤掉他们不想感染的国家，丢弃不同类型的基于被感染国家的恶意软件。”研究人员 Fernando García 和 Dan Regalado 说。

据说它还与其他针对该地区的银行木马有相似之处，例如Grandoreiro、Javali和Lampion。涉及Delphi 恶意软件的攻击链利用电子邮件消息敦促收件人打开虚假的逾期发票，从而触发多阶段感染过程。

如果受害者打开通过垃圾邮件发送的 HTML 附件，它会验证该文件是从桌面设备打开的，然后重定向到远程服务器以获取第一阶段的恶意软件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QmbJGbR2j6zQ7MPicAJ1N0W1a5B98Gl4MJe4j6uVO86KoLlCiaAOeGaCRMRmtTlAiciat9feyBqsw9CSdKKKxVpLUQ/640?wx_fmt=jpeg)

RAR 或 ZIP 存档在启动时旨在利用流氓数字证书（一个是 Mispadu 恶意软件，另一个是 AutoIT 安装程序）通过滥用合法的 certutil 命令行实用程序来解码和执行木马。

Mispadu 能够收集受感染主机上安装的防病毒解决方案列表，从 Google Chrome 和 Microsoft Outlook 窃取凭据，并促进检索其他恶意软件。

这包括一个混淆的 Visual Basic Script dropper，用于从硬编码域下载另一个有效载荷，一个基于.NET 的远程访问工具，可以运行由参与者控制的服务器发出的命令，以及一个用 Rust 编写的加载器，再反过来，执行 PowerShell 加载程序以直接从内存运行文件。

更重要的是，该恶意软件利用恶意覆盖屏幕来获取与在线银行门户和其他敏感信息相关的凭据。

原文来源：E安全

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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