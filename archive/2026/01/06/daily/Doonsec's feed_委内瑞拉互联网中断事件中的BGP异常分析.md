---
title: 委内瑞拉互联网中断事件中的BGP异常分析
url: https://mp.weixin.qq.com/s/k7LU0mm6h0Dqlp6sSbqqAQ
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:26:52.436870
---

# 委内瑞拉互联网中断事件中的BGP异常分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073GSXXVeVTic2xuz97ptJIy1NcCWQ2Y5qUazaIHP97hs66t77UicPQXxAQ/0?wx_fmt=jpeg)

# 委内瑞拉互联网中断事件中的BGP异常分析

原创

黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

2026年1月2日至3日，委内瑞拉发生了一次全国性互联网中断（blackout），几乎所有主要网络服务提供商的连通性大幅下降。

根据Cloudflare Radar公开监测平台的数据，此次中断持续数小时，影响了银行、通信、政府服务以及普通用户的互联网访问。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073qtpqf8xtkeop7hPm9s8DDI7WbZHjsp9V9S0lRQfhttSMWmBoGgG1bQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073EFxEAs28lQXHxnn9HkmbDoY7WNTJrzPuoRmqwtib1mOpWpPfyL7QbRg/640?wx_fmt=png&from=appmsg)

https://radar.cloudflare.com/routing/as8048

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073QLoNxxbaEUg0xtDo2yjqORSmqP7nYhnNFysyBZXpmDukTIAJba3cug/640?wx_fmt=png&from=appmsg)

这网站数据非常清晰，黑鸟推荐多多使用。

与此同时，国外网络安全研究人员观察到委内瑞拉国有电信运营商相关自治系统（AS）出现的BGP路由异常，引发了技术社区的广泛讨论。

事件背景与BGP异常概述

边界网关协议（BGP）是互联网骨干网用于交换路由信息的协议，其核心功能是帮助不同自治系统（AS）之间选择最优路径。

BGP异常常见形式包括路由泄漏（route leak）和路径预置（path prepending）。

路由泄漏指某个AS错误地将从一个对等方学到的路由重新公告给另一个对等方，路径预置则通过在AS路径中重复自身AS号来人为延长路径长度，从而降低该路径的优先级，常用于流量工程。

此次事件中，Cloudflare Radar检测到委内瑞拉国有运营商CANTV（AS8048）的多个IP前缀出现了异常路由公告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073BNOCiaFqjhcNuIZ46kMcUgst5iabicTEl7giazicLbaGpiap3WBnQ0c0Sm2w/640?wx_fmt=png&from=appmsg)

具体表现为：

部分原本应直接通过CANTV传输的流量，被错误地经由意大利运营商Telecom Italia Sparkle（AS6762）和拉美海缆运营商GlobeNet（AS52320）转发，且AS路径中CANTV的AS号被重复预置10次。

需要注意，委内瑞拉总统被捕时间约为1月3日凌晨5点，也就是说，BGP路由泄露事件是发生在被捕前。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073hic9ouTxxXV7E5BVOQ9xia4vhYM96YgTqamzp1ZDQd9tWz3aQT7T6Dpg/640?wx_fmt=png&from=appmsg)

其他异常如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073oQFuC4kUk3Nl1zkLEkQIA8EbKlcElLj0LqqNCIMmN2csDW1zRksPEA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073zxtWxc9qIggrhJx4U9Lq3CpJmklpYFAkksYs7PXELbJp1h5T0aG5FA/640?wx_fmt=png&from=appmsg)

受影响的前缀主要属于委内瑞拉本地ISP Dayco Telecom（AS21980），这些前缀承载了银行、邮件服务器等关键基础设施。

两份公开技术报告对该异常进行了详细记录：

1、Low Orbit Security的《Radar #16》（作者Graham Helton）提供了纯技术分析，指出异常发生在中断前后，时机“值得注意”，但未做出恶意结论。

https://loworbitsecurity.com/radar/radar16/

2、TechPlanet后续文章《BGP Anomalies Reveal Digital Fingerprints of Venezuela's Political Crisis》在复述相同技术细节的基础上，将异常置于委内瑞拉政治动荡背景中讨论，但同时引用专家意见：“这很可能只是误配置，没有明显恶意迹象”。

https://techplanet.today/post/bgp-anomalies-reveal-digital-fingerprints-of-venezuelas-political-crisis

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073dPKoQibSm4K0m9emoLgwdtboqYsMZ91UsDvAeNegGYqib4XGF7rONeYQ/640?wx_fmt=png&from=appmsg)

涉及主要公司与组织介绍

CANTV（AS8048）Compañía Anónima Nacional Teléfonos de Venezuela（委内瑞拉国家电话公司），成立于1930年，是委内瑞拉最大的国有电信运营商，负责全国固定电话、移动通信（品牌Movilnet）和宽带互联网服务。

作为国家基础设施的核心组成部分，CANTV控制了委内瑞拉绝大多数国际出口带宽，在互联网连通性方面具有主导地位。

Telecom Italia Sparkle（AS6762）Telecom Italia Sparkle S.p.A.（简称Sparkle）是意大利电信集团（Telecom Italia）的全资子公司，总部位于罗马，专注于国际批发电信服务。

该公司运营全球性的海底光缆和陆地网络（品牌Seabone），为欧洲、 mediterranean 地区以及拉美提供高带宽骨干连接，是全球Tier-1运营商之一。

GlobeNet（AS52320）GlobeNet Cabos Submarinos S.A.是一家专注于西半球海底光缆系统的运营商，总部位于巴西，拥有超过23,000公里的双环冗余海缆网络，连接北美（美国）、南美（巴西、哥伦比亚、委内瑞拉、阿根廷等）。

GlobeNet最初由巴西电信运营商Oi建设，现由投资基金管理，主要为拉美地区提供低延迟国际带宽。

Dayco Telecom（AS21980）Dayco Telecom C.A.是一家委内瑞拉本土互联网服务提供商（ISP），成立于2000年代，主要为企业、政府机构和金融机构提供专用线路、数据中心托管和互联网接入服务。

其网络高度依赖上游运营商CANTV的国际出口，在此次事件中，其托管的关键基础设施前缀成为异常路由的主要对象。

目前社区讨论核心如下：

1、路径预置10次是CANTV的常规流量工程实践（历史BGP数据可证实），目的是将流量导向更优路径，而非吸引流量。

2、路由泄漏最可能源于CANTV路由策略配置过于宽松，导致在主路径失效时意外导出备用路由。

3、缺乏任何劫持或中间人攻击（MITM）的技术证据。

少数评论承认异常与政治事件重合的时机“巧合”，但强调在无额外证据前，应优先采用最简单的解释：误配置而非故意操纵。

还有一些评论围绕情报角度，例如发起相关攻击可得到大量的流量数据用以分析情报数据，以及展开的一些讨论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073HPjwicWqVIRD57kXkibBpicRxwnaUJXkwxnB8pzVxYe7dcGydp90mrKNg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia073wfwQM95hibUvILsRdF3yG0tvkBLdQbeeDTap6vucsW85Zmma2sTuQvw/640?wx_fmt=png&from=appmsg)

委内瑞拉2026年1月互联网中断事件中的BGP异常，凸显了全球互联网骨干网的固有脆弱性，即BGP协议本身缺乏强认证机制，误配置或潜在操纵均可能产生类似现象。

事件提醒各国运营商加强路由安全实践（如ROV过滤、IRR注册），同时也反映了地缘政治不稳定地区互联网基础设施的特殊风险，未来若出现官方调查或更多原始BGP转储数据，或可进一步澄清异常成因。

上述可以说是没得出什么好结论，最大的价值可能就是推荐Cloudflare Radar进行学习了。

最后Ai科普一下BGP的脆弱性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkp9ceiahuxpFkhxr1zcfia0730niaLkYRuvhbHDLO4pJ9tmTCBchKSdJgBLCFTjQ9aHOxiarQh8lm1AOg/640?wx_fmt=png&from=appmsg)

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