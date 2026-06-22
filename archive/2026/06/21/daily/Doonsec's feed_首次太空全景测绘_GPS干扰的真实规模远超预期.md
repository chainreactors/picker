---
title: 首次太空全景测绘:GPS干扰的真实规模远超预期
url: https://mp.weixin.qq.com/s/H1xvnrGvlakU4bUzGxFaZg
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:16:24.618426
---

# 首次太空全景测绘:GPS干扰的真实规模远超预期

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpVuQH0bP9jNUZhfxvFKWXfJlVsza61t6mKceGzRhDEO7bdLLkwaTrUKFsM42sq0RXgJgoCSneTdcDZgDTlXkMsWF1AQ2yZl8Q/0?wx_fmt=jpeg)

# 首次太空全景测绘:GPS干扰的真实规模远超预期

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](http://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

一颗实验卫星首次完成了从太空视角对欧洲与中东地区 GPS 干扰的全域测绘，最终结果让项目团队颇感意外。此前人们大多关注地面设备受到的导航干扰，而这次观测证实，远在数百公里高空的低轨卫星同样会遭遇 PNT（定位导航授时）信号的严重衰减，这种干扰足以影响卫星的正常工作与运行安全。

完成这次测绘的是 Pulsar-0 卫星，它是美国加州 Xona Space Systems 公司打造的 Pulsar 导航星座的首发实验星。这颗卫星运行在距地面 500 公里的 LEO（低地球轨道），承担着技术验证任务，为该公司今年晚些时候部署 300 颗规模的低轨导航星座铺路。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqxIYBowD2ewedEib3tXvjkbS7RWJL87rlx2CTkE0fKZp9ktOp0mHlJfb1oE6RVXo3vgibMMcZB62Vv3BicPUhcickq1BmN7ZlGNNA/640?wx_fmt=png&from=appmsg)

（图来自satnews）

Pulsar 星座的核心定位，是提供比美国 GPS 以及其他 GNSS（全球导航卫星系统）更具韧性的 PNT 服务。同类全球导航系统还包括欧洲的 Galileo 与中国的 Beidou，它们分发的 PNT 信号支撑着现代社会大量关键基础设施运转，覆盖电网调度、金融交易与石油钻探等诸多领域。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDryIaF4ib8alBeW9qCNDCQkL9oxtryu4Rr3QwtYyDdY4DJLYgA5j8xXdXRuiaQKOGchbcevelnNRSNvS5v9CwDprkBT3dRXuvfPQ/640?wx_fmt=png&from=appmsg)

传统 GNSS 卫星的轨道高度普遍在 19000 公里以上，抵达地面接收机的信号强度非常微弱，很容易被人为干扰。过去五年间，GNSS 压制式干扰 Jamming 与欺骗式干扰 Spoofing 几乎已经成为全球性问题，前者通过大功率噪声信号掩盖真实导航信号，让接收机无法正常捕获信号，后者则构造携带错误坐标的虚假信号覆盖真实信号，诱导接收机输出错误的位置与时间信息。

冲突区域更是导航干扰的高发地带。俄罗斯在其西部边境部署了干扰设备，官方称用于防范乌克兰无人机袭击，每月都有数万架飞越该区域的民航航班受到影响。中东地区的冲突各方也频繁使用干扰与欺骗手段，既用于偏转来袭的无人机，也用于隐藏海上违规船舶的位置。

Xona 计划中的低轨导航星座将采用同类导航信号体制，但信号强度会提升百倍，以此抵御这类人为干扰。作为技术验证的一部分，Pulsar-0 卫星同样搭载了 GPS 接收机，确保两套系统未来能够协同工作。去年发射升空数月后，团队首次开启这台接收机，就被欧洲与中东部分区域上空的信号衰减规模震惊。

Xona 联合创始人 Kaz Gunning 在接受Space采访时表示，飞越北美上空时 GPS 信号始终稳定清晰，但只要进入欧洲区域，就能明显察觉到异常。团队原本预计会观测到一定程度的干扰，但实际规模远远超出预期。

在受影响最严重的区域，卫星高度测得的 GPS 信号强度从常规的 40 分贝降至最低 10 分贝，衰减幅度超过 10 倍。

Gunning 同时指出，受观测轨道高度限制，这份测绘结果未必能完全对应地面用户受到的干扰强度。但数据清晰显示，在应用最广泛的低地球轨道上，GPS 信号的扰动从西侧的法国一直延伸到东侧的巴基斯坦边境，覆盖范围极广。

这一测量结果证实，地面干扰设备的作用范围足以触及低轨卫星，低轨卫星赖以同步运行时间、确定自身空间位置的 PNT 信号，并不能时刻保持可靠。

卫星飞越这些区域时会直接失去 GPS 定位能力，对于需要精准定位才能完成拍摄的成像卫星来说，这会造成直接影响。没有 GPS 信号，卫星无法完成高度确定与位置计算，甚至无法精准对准地面的遥测指令天线，整体运行都会受到干扰。即便是 Starlink 这类大型低轨星座，同样依赖 GPS 信号来规避与其他航天器的碰撞风险。

除了人为的干扰与欺骗，剧烈的太阳风暴同样会对珍贵的 PNT 信号造成严重破坏。2024 年 5 月的 Gannon 超级太阳风暴就曾大幅扭曲导航信号，导致美国部分地区的精准农业设备连续数日无法正常作业。正因如此，技术领域一直在加紧研发备用方案，确保在 GNSS 失效时，依然能向有需求的用户传输 PNT 信号。

Xona 希望 Pulsar 星座建成投入使用后，能大幅缓解各类用户对传统导航卫星的依赖困境。按照 Gunning 的说法，依托低轨星座发射的高强度信号，现有干扰设备能影响的区域仅为当前的 5% 左右。

干扰的作用半径会大幅缩小，信号衰减的覆盖范围会下降，完全丢失信号锁定的区域半径也会同步缩减。

Xona 计划在今年 10 月发射首批 6 颗组网卫星，随后将逐步提升生产规模。该公司在今年 3 月完成了 1.7 亿美元的 C 轮融资，目标是 2027 年初开始提供基础服务。

Xona 通讯负责人 Max Eunice 向Space透露，今年年底就会有授时领域的早期客户通过间歇覆盖的方式开始使用 Pulsar 系统。随着后续发射任务推进，星座逐步组网完成，Pulsar 的能力会持续提升，为更多领域的客户解锁新的应用价值。

美国太空军与空军研究实验室（AFRL）是 Xona 最早的政府合作方，双方的合作从技术验证阶段就已启动。2023 年 8 月，Xona 获得 AFRL 授予的 120 万美元 Direct to Phase II SBIR 合同，用于验证低轨 PNT 架构与美国国家安全空间体系的整合能力，对接太空作战分析中心的战力设计需求。

2025 年 2 月，AFRL 通过 STAR-FISH 项目再授予 Xona465 万美元合同，测试 GPS 受扰与拒止环境下 Pulsar 系统的表现，覆盖无人机作战、自主地面车辆等军事场景，同时验证抗干扰、抗欺骗以及安全密钥分发能力。

2025 年 6 月，Xona 拿到太空军创新部门 SpaceWERX 颁发的 2000 万美元 STRATFI 战略资助，同时入选总额 4.4 亿美元的专项计划，成为八家核心入围企业之一。此外 Xona 还与卫星厂商 Astranis 组队，参与美国太空军的弹性全球定位系统（R-GPS）项目，该项目的目标是为美军打造传统 GPS 之外的备份导航体系，应对高对抗场景下的 GPS 全频段失效风险。

创始团队中的核心技术成员 Kaz Gunning，在加入 Xona 之前曾任职于博思艾伦汉密尔顿（Booz Allen Hamilton）。这家企业是美国情报与防务领域的顶级承包商，长期为 NSA（美国国家安全局）、CIA（中央情报局）以及国防部提供技术服务与系统集成，深度参与卫星情报、电子战以及导航安全相关的涉密项目，是美国情报体系最核心的第三方技术服务商之一。

投资方中的 Lockheed Martin Ventures，母公司洛克希德・马丁是美国 GPS 卫星的主承包商，同时也是 NRO（国家侦察局）间谍卫星的核心研制方，几乎垄断了美国军用与情报航天平台的核心供应链。该公司的战略投资通常会紧密贴合美军与情报机构的技术路线，其入局也侧面印证了 Xona 技术的国家安全价值。

PNT 能力本身就是现代情报与作战体系的底层支撑。低轨强信号导航的特性，天然适配美军 ISR（情报监视侦察）平台在高对抗环境下的作业需求，无论是侦察无人机、特种作战单位还是精确制导武器，都需要在 GPS 被干扰的环境下维持精准的定位与时间同步。

相关：

[追踪并锁定来自太空的强力GNSS干扰源](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186965&idx=1&sn=599e0e9444b7b583c2ef4529af3293cc&scene=21#wechat_redirect)

[美以空袭伊朗后，霍尔木兹海峡遭遇罕见GPS攻击潮](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451185573&idx=1&sn=5655d5479bea07a8a7a4e8e0b05d4a60&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

白帽子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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