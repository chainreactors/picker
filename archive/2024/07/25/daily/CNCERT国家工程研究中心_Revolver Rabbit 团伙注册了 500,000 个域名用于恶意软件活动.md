---
title: Revolver Rabbit 团伙注册了 500,000 个域名用于恶意软件活动
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546023&idx=3&sn=a4a3c1fd8729e2ff5da423091058ca8b&chksm=fa938266cde40b709a778811600f7ad4ad0baa3b15f142959cdfa79f9d195efb5072e326b24c&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-25
fetch_date: 2025-10-06T17:44:14.098666
---

# Revolver Rabbit 团伙注册了 500,000 个域名用于恶意软件活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nVLdoSAZoGfib9OFhdy7p7jeDZUdDLQJViahGoh5vJZCysIibjALbpx9RyHG5S8S2NZbaGzQwOsLaTg/0?wx_fmt=jpeg)

# Revolver Rabbit 团伙注册了 500,000 个域名用于恶意软件活动

网络安全应急技术国家工程中心

安全研究人员追踪的网络犯罪团伙 Revolver Rabbit 已注册了超过 50 万个域名，用于针对 Windows 和 macOS 系统的信息窃取活动。为了进行如此大规模的攻击，威胁者依赖于注册域生成算法 (RDGA)，这是一种允许在瞬间注册多个域名的自动化方法。

RDGA 类似于网络犯罪分子在恶意软件中实施的域名注册算法 (DGA)，用于创建命令和控制 (C2) 通信的潜在目的地列表。

两者之间的一个区别是，DGA 嵌入在恶意软件中，并且只有部分生成的域被注册，而 RDGA 仍保留在威胁行为者手中，并且所有域都已注册。

虽然安全研究人员发现 DGA 并尝试对其进行逆向工程以了解潜在的 C2 域，但 RDGA 是秘密的，找到生成要注册的域的模式变得更加具有挑战性。

# **Revolver Rabbit 运营着超过 500,000 个域名**

专注于 DNS 的安全供应商 Infoblox 的研究人员发现，Revolver Rabbit 一直在使用 RDGA 购买数十万个域名，注册费总计超过 100 万美元。

威胁者正在传播 XLoader 信息窃取恶意软件（Formbook 的后继者），其适用于 Windows 和 macOS 系统的变种用于收集敏感信息或执行恶意文件。

Infoblox 表示，Revolver Rabbit 控制着超过 500,000 个 .BOND 顶级域名，这些域名用于为恶意软件创建诱饵和实时 C2 服务器。

Infoblox 威胁情报副总裁告诉媒体，与 Revolver Rabbit 相关的 .BOND 域名最容易发现，但威胁者随着时间的推移已经在多个 TLD 上注册了超过 700,000 个域名。

考虑到 .BOND 域名的价格约为 2 美元，Revolver Rabbit 在其 XLoader 操作中的“投资”接近 100 万美元，不包括过去购买的域名或其他 TLD 上的域名。

Infoblox 表示：“该攻击者使用的最常见的 RDGA 模式是一系列由一个或多个字典单词和五位数字组成的序列，每个单词或数字之间用破折号分隔。”

这些域名通常易于阅读，似乎专注于特定主题或地区，并显示出多样性，如以下示例所示：

·usa-online-degree-29o[.]bond

·bra-portable-air-conditioner-9o[.]bond

·uk-river-cruises-8n[.]bond

·ai-courses-17621[.]bond

·app-software-development-training-52686[.]bond

·assisted-living-11607[.]bond

·online-jobs-42681[.]bond

·perfumes-76753[.]bond

·security-surveillance-cameras-42345[.]bond

·yoga-classes-35904[.]bond

研究人员表示：经过数月的追踪，将 Revolver Rabbit RDGA 与已建立的恶意软件联系起来，凸显了了解 RDGA 作为威胁者工具箱中的一种技术的重要性。

Infoblox 已跟踪 Revolver Rabbit 近一年，但直到最近，RDGA 的使用才掩盖了威胁者的目标。过去曾观察到该对手的攻击活动，但并未将其与 Infoblox 发现的规模如此之大的行动联系起来。

例如，事件响应公司 Security Joes 的恶意软件分析工具提供了有关 Formbook 信息窃取程序样本的技术细节，该样本拥有 60 多个诱饵 C2 服务器，但 .BOND TLD 中只有一个域是真实的。

多个威胁者正在使用 RDGA 进行恶意操作，包括恶意软件传送和网络钓鱼、垃圾邮件活动和诈骗，以及通过流量分配系统 (TDS) 将流量路由到恶意位置。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/revolver-rabbit-gang-registers-500-000-domains-for-malware-campaigns/

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