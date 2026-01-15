---
title: 星链在伊朗：卫星互联网在电子战中的技术分析
url: https://mp.weixin.qq.com/s/mZkjATxViB9FM54lnWyt-Q
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:28:28.495482
---

# 星链在伊朗：卫星互联网在电子战中的技术分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkoPHnS0wic0picNaTP4FGXBj6Ou5PcTBne1l8SCY9HMqeDvDJFWicB84GI8gqG3hFpkrdicyKKNhGNQOA/0?wx_fmt=jpeg)

# 星链在伊朗：卫星互联网在电子战中的技术分析

原创

黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

2026年1月，伊朗出现大规模网络访问限制，在这一背景下，SpaceX公司的Starlink卫星互联网服务被激活，并提供免费接入，成为部分用户绕过网络限制的工具之一。

该情况出现后，当局迅速采取技术反制，包括信号干扰和设备管理。这场技术互动呈现出典型的动态调整特征，体现了卫星互联网在复杂网络环境下的应用潜力与挑战。

自2026年1月8日起，伊朗全国互联网连接率降至较低水平。黑鸟仅从网络分析出发，不进行其他角度的讨论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkoPHnS0wic0picNaTP4FGXBj6ibJNPLa3Bts38LcDBiaDXPqsI5aFw4SZyDcyrurVltKgNphIUDwN2yKQ/640?wx_fmt=png&from=appmsg)

12月，互联网畅通无阻，作为国家骨干网的TCI每天进行120万次路由更新，稳定地维持着国家互联网的运转。

1月8日 03:00 UTC ，BGP 通告数量在短短几小时内从 120 万条激增至560 万条，过滤规则相互冲突，路由混乱不堪，网络开始自我崩溃。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkoPHnS0wic0picNaTP4FGXBj6yBFdmcuMMV8AMxIwQ1X7kRiar8Ey6iaM46HgmkmhVqEEcKF3gsnqZlFA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkoPHnS0wic0picNaTP4FGXBj6ibIv6X4byHDvNs9MPzBNPN3M9N9vlG3zwANqL00PQq4x3Uw3zZBWbsA/640?wx_fmt=png&from=appmsg)

此时，伊朗所有主要网络流量都同时飙升。

Irancell、MCI、Rightel、Shatel、Afranet等十个网络，几乎同时故障。目前判定，1月8日是对完全断开连接的压力测试，BGP撤回事件揭示了由于核心网关被强制执行「过滤优先，路由其次」的策略而导致的路由泄露。

IPv6的流量直接归零，原因疑似因为过滤设备无法正确处理 IPv6 流量，所以你懂的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkoPHnS0wic0picNaTP4FGXBj6D4OGwvLP6CCHYpxjAHpv4iaUiaDiaGXmnQonefLMicPLFcwkAk0Dt8DcDg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkoPHnS0wic0picNaTP4FGXBj6XEic6GH7ibxOZOzuEbIicTf36Lwrz6btR1oXDHEV60w4GQxkPzHZ3ibjOA/640?wx_fmt=png&from=appmsg)

基于上述现状，轮到了星链环节。SpaceX早在2022年就曾为伊朗地区开启覆盖。2026年1月13日，随着网络限制加剧，Starlink宣布提供免费服务。相关组织报告称，新用户可获得更长的免费接入时长，并称此举有助于用户获取信息。NasNet等志愿者团体证实，已与Starlink技术团队合作，推动服务改进。

NasNet宣布经过与Starlink和美国官员的协商，伊朗地区Starlink服务永久免费，仅需开启设备即可连接。 Starlink终端（相控阵天线设备）通过自动对准低轨卫星，提供高速连接。

Starlink设备在伊朗属于受管制物品，官方禁止进口与使用。但通过各种渠道，数万台终端进入伊朗，主要途径包括境外运输。志愿者团体如NasNet指导用户安装、共享连接（使用路由器多用户分流），并提供配置建议。当局已加强对设备的监管与回收。

基于此，伊朗使用专业电子设备针对Starlink的Ku/Ka波段信号及定位系统。主要手段为信号干扰，其可导致卫星信号出现较高丢包率，尤其影响上行链路。社交媒体技术讨论指出，干扰主要采用GPS/GNSS欺骗或阻塞，以及Ku/Ka频段射频直接干扰，造成30–80%的丢包率，特别针对上传链路。

此外还有手段为定位干扰，例如广播虚假定位信号，使终端波束偏移，使得连接不稳定。

而星链的反制主要依赖软件更新：

通过空中升级调整频率分配、信号编码、波束管理。

NasNet报告称，近期星链更新使德黑兰地区丢包率从35%降至10%，但情况可能随时变化。Starlink团队周末推送快速软件更新显著改善干扰，但强调这是持续的技术调整过程。

技术分析指出，Starlink凭借低轨卫星密集覆盖具有一定优势，但面对专业级干扰仍存在局限，视频通话等高带宽应用受影响较大，而文本消息仍可通过。 下图为星链干扰模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkoPHnS0wic0picNaTP4FGXBj6EWx5gfriblnf4XMntBcAyheFeOG4s3edJJLTNltEY84sEyQOSAwHXlA/640?wx_fmt=png&from=appmsg)

短期内，Starlink可能通过进一步软件更新提升连接稳定性（如更好地应对定位干扰）。

但当局也可升级干扰手段，或加强设备管理。

目前，这仍是一场技术层面的动态博弈：一方控制地面网络，另一方利用太空资源，却难以提供完全稳定的连接。

星链为伊朗的网络环境带来了一种新技术选项，同时也揭示了卫星互联网在复杂条件下的边界，可以明确，星链=核弹级战略武器。

此外，黑鸟通过网络调研，发现一些相关信息，以下内容仅供参考。

网传伊朗部署军事级GPS干扰器Murmansk-BN和Krasukha-4系统，据称为俄罗斯提供，多份报道指出伊朗使用了俄罗斯起源的先进电子战系统，包括Murmansk-BN（长距离干扰）和Krasukha-4（多频段干扰，主要针对Ku/Ka波段和GPS）。这些系统据称通过IL-76运输机在2025年交付伊朗，并在乌克兰战场上证明有效。

媒体报道称这些系统“speculation”（推测）或“unconfirmed”（未确认）描述被部署，社交媒体也广泛讨论这些型号作为干扰来源，部分报道用。

没有公开卫星影像或官方承认完全证实这些具体型号在全国部署，但技术特征（如高功率宽带噪声和GPS欺骗）与这些系统匹配。

伊朗确实部署军事级干扰（主要GPS欺骗+射频噪声），导致Starlink严重降级（80%+中断在高峰期）。

这是和平时期首次大规模针对商用LEO卫星的电子战。

目前仍然在对抗之中。

请自行存档。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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