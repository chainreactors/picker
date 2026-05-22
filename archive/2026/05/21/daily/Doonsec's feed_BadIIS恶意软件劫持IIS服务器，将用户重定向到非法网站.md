---
title: BadIIS恶意软件劫持IIS服务器，将用户重定向到非法网站
url: https://mp.weixin.qq.com/s/HADgWzNC7UIRofmhfP6QPA
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:59:53.759480
---

# BadIIS恶意软件劫持IIS服务器，将用户重定向到非法网站

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7N8V9u26lmzqh24DGLU5ME7xSMic5a9kfhEiaUvWY7mSicMUSWfNdn91s4icsiapefFmOyus96PmQqXIuSiae4ZvvXWVl01AvKgYEOac/0?wx_fmt=jpeg)

# BadIIS恶意软件劫持IIS服务器，将用户重定向到非法网站

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

BadIIS恶意软件出现了一种新变种，它劫持微软IIS网络服务器，将用户重定向到非法网站，这凸显了由讲中文的网络犯罪集团运营的不断演变的恶意软件即服务（MaaS）生态系统。

新分析的变体以嵌入的“demo.pdb”字符串为标记，Talos 使用这些字符串来追踪其开发历史。

证据表明，该恶意软件至少从 2021 年 9 月到 2026 年 1 月一直由使用别名“lwxat”的开发者积极维护。

程序数据库 (PDB) 路径揭示了一个结构化和迭代的开发过程，包括快速更新、功能分支和有针对性的规避技术。

有些版本专门设计用于绕过 Norton 等防病毒解决方案，而另一些版本则引入了修复程序，以避免诸如 IIS“503 服务不可用”响应之类的操作错误，这些错误可能会暴露病毒感染。

Talos 以中等程度的信心评估认为，该变种并非与单个威胁行为者有关，而是多个组织共享或出售的工具，这进一步证实了其作为通用恶意软件的分类。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7MBLV9ANl7hrFOpyjU247ykibUmR99ZIRdXpbeVFSuicp74Up11RZdhYIoEcwtF57tdIzWITNIwrKx8iaB2IcPe3RAictOJ4gpkwmI/640?wx_fmt=png&from=appmsg)

Cisco Talos 在一份与 GBhackers 分享的报告中表示，他们发现了一种 BadIIS 变种，可以通过其嵌入的“demo.pdb”字符串来识别，该变种的功能类似于普通恶意软件。

BadIIS 主要针对搜索引擎优化 (SEO) 欺诈和网络流量操纵。一旦部署到被入侵的 IIS 服务器上，它就可以：

* 将合法用户重定向到恶意网站，例如赌博网站或成人网站。
* 充当反向代理，向搜索引擎爬虫传递恶意内容。
* 注入垃圾内容并篡改网站元数据（标题、描述、关键词）。
* 插入内部和外部反向链接，以提高攻击者控制的域名的排名。

威胁行为者可以配置劫持率（受影响的流量百分比），切换是否明确针对主页，并提供远程 URL 来动态获取恶意标题、描述和关键字 (TDK) 元数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7NhoKSReiarpEwO5IwKiax8RoqEyHbYGGuh1aT7w2hhZ3MkRAhHq0wzcsmfdql9GOSu3xWO1nmtzyBX1GASWQZqQ55Dx6frbrQEA/640?wx_fmt=png&from=appmsg)

例如，当搜索引擎爬虫访问被入侵的网站时，BadIIS 可以静默地提供与正常用户看到的内容不同的内容，从而帮助恶意页面在搜索结果中获得更高的排名，而不会立即被检测到。

## **BadIIS恶意软件劫持IIS**

Talos 报告是一个专门用于生成自定义 BadIIS 有效载荷的构建工具。该工具允许攻击者：

* 配置重定向 URL 和行为。
* 启用反向代理功能以进行爬虫操作。
* 定义内容劫持规则和流量百分比。
* 注入反向链接和SEO垃圾脚本。

构建者还将配置数据直接嵌入到恶意软件中，并使用简单的 XOR 编码技术混淆命令与控制 (C2) 服务器地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PJOWOn7eYMn7821Bw1K0zicYibY5YiaWu0L2X86RgBb2I1pE9ibSOV7saWaTOZSJaj0QKmibby6OCKdxicBFcJRZ8KI83wAlRSL1ZHY/640?wx_fmt=png&from=appmsg)

值得注意的是，该构建器包含一个身份验证机制，用于检查 C2 服务器是否返回特定的响应字符串“lwxat”。这个独特的标记可作为强有力的归属线索，将生态系统中的多个工具联系起来。

除了核心恶意软件之外，Talos 还发现了一套由同一作者开发的辅助工具。这些工具包括安装程序、投放器以及用于自动化部署和确保持久性的服务型组件。

有些工具以“Winlogin”之类的名称作为 Windows 服务运行，而另一些工具则使用双重 Base64 编码或自定义混淆来隐藏其活动。

新版本实现了两阶段安装过程，其中主安装程序部署 BadIIS，辅助组件确保即使删除 BadIIS 也能恢复它。

该恶意软件还会将自身复制到隐藏的备份位置，使其能够在服务器重启和安全修复尝试后幸存下来。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7N5hgLGHGickA9dZSiac02RX7ameYEE3WibnCFBVGyLMFUeNxYlw1ekx5nkmL79Jwibv0whhmmpaoFJDw8wx5iaGibgh5rpNGvENUT8A/640?wx_fmt=png&from=appmsg)

对PDB路径和嵌入字符串的分析表明，别名“lwxat”很可能是开发者。此外，提及名为“xshen”的客户也表明，系统会为特定客户创建定制版本，这符合商业化的MaaS（移动即服务）模式。

自 2024 年以来，Talos 观察到亚太地区以及欧洲、北美和南非都出现了使用此变种的攻击。

虽然趋势科技、AhnLab、VNPT 和 Elastic 等其他供应商也报告了类似的攻击活动，但策略上的差异表明多个参与者利用了相同的底层工具集。

BadIIS 的持续演变表明了网络服务器恶意软件是如何产业化的，使得威胁行为者能够通过 SEO 欺诈和流量重定向大规模地利用被入侵的基础设施牟利。

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