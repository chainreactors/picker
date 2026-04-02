---
title: Axios供应链攻击事件再追踪：线索直指Lazarus组织
url: https://mp.weixin.qq.com/s/RvykbFFq-zCaZOOax_ofCg
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:22:24.953680
---

# Axios供应链攻击事件再追踪：线索直指Lazarus组织

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Emmib7pWXrXLWo8qDhvtqibMj1gn3TQfXl6O4KQZEL4e8Z52WGaMlMw2AloxWrArao7ygNGib2mlMjO4sZc5ibDEDQbPUVjF2A03yUpYLmVsQrQ/0?wx_fmt=jpeg)

# Axios供应链攻击事件再追踪：线索直指Lazarus组织

高级威胁研究院
高级威胁研究院

360威胁情报中心

![]()

在小说阅读器中沉浸阅读

此前，我们发布了《[Axios npm供应链攻击威胁分析报告](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247508054&idx=1&sn=53087fd771552eb8c5c0144dc7db8400&scene=21#wechat_redirect)》，系统性披露了攻击者劫持维护者账号、在package[.]json中注入“幽灵依赖”plain-crypto-js@4[.]2.1、通过postinstall钩子释放跨平台RAT等核心技术细节，并给出了详细的时间线、IOC指标及应急响应建议，迅速成为行业内重要的参考资料。

本次报告，我们继续对事件进行进一步的追踪披露，并结合360安全大脑的最新威胁情报数据，进一步开展归因分析。

一、概述

axios是一个基于Promise的HTTP客户端，在JavaScript和Node.js 生态系统中被广泛使用。

2026年3月30日，axios遭遇供应链攻击。攻击者成功劫持了维护者账户(jasonsaayman)，在npm官方仓库发布了两个恶意版本（axios@1[.]14.1和axios@0[.]30.4），通过注入恶意依赖plain-crypto-js@4[.]2.1，该包此前并不存在，且从未被axios代码实际导入。其唯一目的是执行一个安装后脚本，该脚本会释放并运行一个针对macOS、Windows和Linux的跨平台远程控制木马（RAT）。恶意版本在npm上存活约3小时后被下架。

结合360安全大脑数据，我们将axios入侵事件与我们跟踪的一起Lazarus组织活动关联起来，二者使用多处相同的命名及相似代码结构。同时，axios入侵事件使用的样本与早期被披露的RustBucket恶意组件存在关联。因此我们认为此次axios入侵事件归属到Lazarus组织。

Lazarus组织长期通过感染npm包的方式进行供应链攻击，依据以往攻击手法，攻击人员预先通过求职/招聘/面试等方式向开发人员投递钓鱼链接/被感染的工程项目，致使开发人员被攻击，随后攻击者再通过窃取开发人员账号发布被污染的工程项目，以实现供应链攻击。

# 二、归属研判

在我们持续监控Lazarus组织的活动中，该组织发起了一项攻击活动，在该活动中，受害者被从消息平台例如Telegram引诱到会议相关诱饵中，例如Zoom会议，随后下发及诱导执行PowerShell相关脚本从而可以多平台上执行实时命令和窃取凭据。Daylight也披露过同类活动，将其跟踪为GhostCall活动。

在之前攻击活动中，攻击者使用的样本(ea3192f64b9988889d5f8c61be637d2a)名为“c:\programdata\system.bat”,从恶意域名microsmeet[.]xyz和bluyy[.]com下发载荷。经过分析比对axios入侵事件们发现:

* 样本的命名与命令行基本一致;
* 建立的注册表项 Run 项均是MicrosoftUpdate;
* 与Daylight报告披露的Lazarus组织的基础设施一致。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXLlQYrp6ibZ3OVAqz1h5ibQVJo3FJpcZzPeRoDXQW4nTMx8Ly1kvyl26bGmcxZorw6xQRm0OJ4ohF0MyaAyr8GEjkAdGtxdbF8vo/640?wx_fmt=png&from=appmsg)

图1 089e2872016f75a5223b5e02c184dfec与ea3192f64b9988889d5f8c61be637d2a样本命令行一致

因此我们以强烈的信心将axios入侵事件与我们持续跟踪的Lazarus组织活动(也称为GhostCall活动)关联起来。

其次，在2023年4月21日的报告中，Jamf Threat Lab披露了名为“RustBucket”的 macOS 恶意软件变种。该报告披露第三阶段载荷(182760cbe11fa0316abfb8b7b00b63f83159f5aa)包含webT模块。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXIZ2RE5pUNOesXUUJYl0zibtvhfXdOaENEoSGdYpicLDtLyu2pNu1EQ4zZGL8Icv5Tiax3HCPXVKibCe0aDYNg3Nzj0qSSZwQmdu74/640?wx_fmt=png)

图2 RustBucket样本模块信息

在分析axios入侵事件，我们提取了macOS平台样本的构建信息，可以看出项目名称为macWebT，与上文webT字符串同类。

1. /Users/mac/Desktop/Jain\_DEV/client\_mac/macWebT/macWebT/
2. /Users/mac/Library/Developer/Xcode/DerivedData/macWebT-hlbytmqtodqtmmfrlgcunsjzzmop/Build/Intermediates.noindex/macWebT.build/Release/macWebT.build/Objects-normal/arm64/main.o (raw binary string)
3. /Users/mac/Library/Developer/Xcode/DerivedData/macWebT-hlbytmqtodqtmmfrlgcunsjzzmop/Build/Intermediates.noindex/macWebT.build/Release/macWebT.build/Objects-normal/x86\_64/main.o (raw binary string)

因此，我们认为此次axios入侵事件是Lazarus组织所为。

# 三、处置建议

参照此前报告：《[Axios npm供应链攻击威胁分析报告](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247508054&idx=1&sn=53087fd771552eb8c5c0144dc7db8400&scene=21#wechat_redirect)》

**附录 IOCs**

kenaikoda[.]com

teams.onlivecall[.]com

23.254.204[.]101:80

3f47643c7a5cbf132f46b4cba75d1aa3

db07741e586bfae526730c592a2ffe6a

ea3192f64b9988889d5f8c61be637d2a

41372946fe231c73750428700f6015fb

**360****高级威胁研究院**

360高级威胁研究院是360数字安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

360威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

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