---
title: 减少路由器通告的能耗
url: https://mp.weixin.qq.com/s/E408G7AS11yMpEUrgu1-xQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:45:50.190500
---

# 减少路由器通告的能耗

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YY73GMUZ1Nk0fCIBgRt7H2ZvOZjv0cdP2xluibBl6EFRySFtefjGgcnjjvS2Y4tnol32uchZANnbPuSBAhkicsRYnbmibkVDxlMY3caz6Id2sA/0?wx_fmt=jpeg)

# 减少路由器通告的能耗

衡水石头哥
衡水石头哥

铁军哥

![]()

在小说阅读器中沉浸阅读

```
FRFC7772：Reducing Energy Consumption of Router Advertisements，February 2016
```

梗概

频繁的路由器通告消息会严重影响主机功耗。本文件建议了避免此类影响的操作实践。

本备忘录的状态

本备忘录记录了当前互联网最佳实践。

本文档是互联网工程任务组（IETF）的产品。它代表了IETF社区的共识。它已接受公众审查，并已被互联网工程指导小组（IESG）批准发布。有关BCP的更多信息，请参阅RFC 5741第2节。

有关本文档当前状态、任何勘误表以及如何提供反馈的信息，请访问http://www.rfc-editor.org/info/rfc7772。

版权声明

版权所有（c）2016 IETF Trust和文档作者。版权所有。

本文档受本文档发布之日生效的BCP 78和IETF Trust与IETF文件相关的法律规定（http://trustee.ietf.org/license-info）的约束。请仔细阅读这些文件，因为它们描述了您与本文件相关的权利和限制。从本文档中提取的代码组件必须包括信托法律条款第4.e节中所述的简化BSD许可证文本，并且在提供时不提供简化BSD许可证中所述的保证。

1、简介

路由信息通过路由器通告（Router Advertisement，RA）消息[RFC4861]传送到IPv6主机。如果这些消息发送得太频繁，可能会严重影响电池供电主机的功耗。

本文档中的关键词“必须”、“不得”、“必需”、“应”、“不应”、“应该”、“不应该”、“推荐”、“可以”和“可选”应按[RFC2119]中的描述进行解释。

2、问题场景

2.1、大型网络上请求的组播RA

在具有大量电池供电设备的链路上，发送请求的组播路由器通告可能会严重影响主机功耗。这是因为每次设备加入网络时，网络上的所有设备都会收到组播路由器通告。在最坏的情况下，如果设备不断加入和离开网络，并且网络足够大，则网络上的所有设备都将以[RFC4861]第6.2.6节指定的最大速率接收请求的路由器通告，即每3秒一次。

2.2、频繁的定期路由器通告

一些网络非常频繁地发送周期性组播路由器通告（例如，每隔几秒一次）。这可能是由于希望最大限度地减少网络重新编号事件对客户的影响，这些事件在一些大型住宅网络中发生得相对频繁。当主机在睡眠模式下忽略RA甚至所有IPv6数据包时，此类网络可能需要频繁发送RA，以避免设备长时间处于非功能性IPv6配置。不幸的是，这对电池寿命有严重影响。

3、后果

观察到的频繁向电池供电设备发送路由器通告消息的影响包括：

\* 有些主机在这些网络上的电池寿命很短，但在其他方面却可以正常运行。这对于这些网络的用户来说是令人沮丧的。

\* 在任何网络上处于省电模式时，某些主机会通过丢弃所有路由器通告消息来做出反应，例如 <https://code.google.com/p/android/issues/detail?id=32662>。这会导致设备在节能模式下失去连接，可能会中断后台网络通信，因为设备无法再发送数据包或确认收到的流量。

\* 某些主机在节能模式下会通过丢弃所有IPv6数据包来做出反应，<http://www.gossamer-threads.com/lists/nsp/ipv6/54641>。这会中断网络通信。

使问题更加复杂的是，当处理在省电模式下丢弃路由器通告的设备时，一些网络管理员通过更频繁地发送RA来解决该问题。这会导致设备进行更积极的过滤。

4、路由器通告频率

周期性RA的适当频率取决于网络设备的约束程度。

\* 即使每隔几秒发送一次RA，笔记本电脑级设备也可能不会对电池寿命产生明显影响。

\* 平板电脑、手机和手表的体验更为明显。在撰写本文时，当主处理器处于睡眠状态时，当前一代设备的功耗可能约为5 mA。收到数据包后，它们可能会在250毫秒内消耗约200 mA的电量，因为数据包会唤醒主处理器，处理RA，处理其他挂起的任务，然后返回睡眠状态。因此，在此类设备上，接收一个RA的成本约为0.014 mAh。

为了将用于接收路由器通告的电量限制为空闲电量的2%（即，对空闲电池寿命的影响不超过2%），接收RA的平均功率预算必须不超过0.1 mA，或大约每小时7个RA。由于背景组播丢失以及当前设备在睡眠时限制组播速率的趋势，许多RA可能无法到达该设备。因此，RA配置参数（例如默认路由器生存期）的最短生存期可能合理地为RA周期的5-10倍，或大约45-90分钟。

相对于测量的空闲电流2% 的影响可以忽略不计，因为在此类设备上，平均功耗通常远高于空闲功耗。

\* 非通用网络（例如传感器网络）中的专用设备可能有更严格的要求。在这些环境中，更长的RA间隔可能是合适的。

5、建议

5.1、网络侧推荐

1. 在以下情况下，路由器制造商应允许网络管理员将路由器配置为使用单播路由器通告来响应路由器请求：

\* Router Solicitation的源地址不是未指定的地址，并且：

\* 请求包含有效的源链路层地址选项。

2. 为大量（数十或数百）电池供电设备提供服务的网络管理员应该启用此行为。

3. 为电池供电设备提供服务的网络不应过于频繁地发送组播RA（请参阅第4节），除非RA数据包中的信息发生了重大变化。如果希望确保主机接收配置更改

很快，这些网络可以在配置更改后立即在有限的时间内（例如，不超过一分钟）发送频繁的路由器通告。

无需更改协议。[RFC4861]的第6.2.6节已经允许使用单播路由器通告响应路由器请求，并且管理员已经可以将路由器通告间隔配置为大范围的值。

5.2、设备端建议

1. 维持IPv6连接要求主机能够接收定期的组播RA[RFC4861]。因此，处理休眠时发送的单播数据包的主机也必须处理休眠时发送的组播RA。如果电池供电的主机发送过于频繁，则可以对相同的RA进行速率限制。

2. 不打算在睡眠时保持IPv6连接的电池供电设备应该断开网络连接，放弃该网络上的所有IPv6配置，或者在唤醒时执行检测IPv6中的网络连接（Detecting Network Attachment in IPv6，DNAv6）过程[RFC6059]。

6、安全考虑

如果配置错误或恶意主机发送恶意路由器通告[RFC6104]，如果它们发送大量此类消息，也会严重影响电池供电主机的功耗。任何可能存在配置错误或恶意主机的IPv6网络都应采取适当的对策来缓解该问题。

7、参考文献

7.1、规范性参考文献

```
[RFC2119]Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, <http://www.rfc-editor.org/info/rfc2119>.[RFC4861]Narten, T., Nordmark, E., Simpson, W., and H. Soliman, "Neighbor Discovery for IP version 6 (IPv6)", RFC 4861, DOI 10.17487/RFC4861, September 2007, <http://www.rfc-editor.org/info/rfc4861>.[RFC6059]Krishnan, S. and G. Daley, "Simple Procedures for Detecting Network Attachment in IPv6", RFC 6059, DOI 10.17487/RFC6059, November 2010, <http://www.rfc-editor.org/info/rfc6059>.
```

7.2、参考资料

```
[RFC6104]Chown, T. and S. Venaas, "Rogue IPv6 Router Advertisement Problem Statement", RFC 6104, DOI 10.17487/RFC6104, February 2011, <http://www.rfc-editor.org/info/rfc6104>.
```

致谢

作者衷心感谢Steven Barth、Frank Bulk、David Farmer、Igor Gashinsky、Ray Hunter、Erik Kline、Erik Nordmark、Alexandru Petrescu、Libor Polcak、Mark Smith、Jinmei Tatuya和James Woodyatt的反馈和有用的建议。

\*\*\*推荐阅读\*\*\*

[我们的WireGuard管理系统支持手机电脑了！全平台终端配置，支持扫码连接，一键搞定](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864213&idx=1&sn=ec85efce2a3b76ba244c71ccbdc09347&scene=21#wechat_redirect)

[保姆级教程：一条命令部署OpenVPN管理系统V4版，支持Win/Mac/安卓/iOS全平台接入](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864329&idx=1&sn=32eef6d6ce107136b389e05a4f206060&scene=21#wechat_redirect)

[成本省下99.7%！用40元的腾讯云服务器自建IPsecVPN，成功对接企业级飞塔防火墙](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864080&idx=1&sn=2de5d9d701d53b2c613b0c852329afb2&scene=21#wechat_redirect)

[万物皆可EVE-NG！一招解决Ubuntu镜像MAC冲突](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865489&idx=1&sn=4585bb186c6d4d7a1aa6dcc1a94c2cea&scene=21#wechat_redirect)

[告别OSPF！EVE-NG专业版+BGP Unnumbered打通Underlay的完整实战](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865266&idx=1&sn=786e8f723b95694923b257be09dbef8d&scene=21#wechat_redirect)

[从180秒到0.01秒：智算中心Underlay路由优化的速度与激情](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865295&idx=1&sn=2d4494418a2c988de36cd01ebb9f5f73&scene=21#wechat_redirect)

[Type-2是管家，Type-5是外交官！Border Leaf让智算中心网络走出去](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865509&idx=1&sn=4367bcc2407fd8370a6469d5270af06f&scene=21#wechat_redirect)

[上医治未病！从PFC流控到ECN预警配置实战](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865603&idx=1&sn=9b7593256f026c02be89bff298e853ef&scene=21#wechat_redirect)

[路修好了，该跑车了！RoCE零成本部署，智算中心RDMA平替方案全公开](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865630&idx=1&sn=a35e6adb1d37deda2fea1d864f06e0c8&scene=21#wechat_redirect)

[单边写入为何秒杀双边传输？从UDP 4791到BTH头，看懂RDMA的灵魂构造！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865671&idx=1&sn=e77403c40336b5049c6d80627a0dd984&scene=21#wechat_redirect)

[手机也能跑DeepSeek-R1/Qwen3了：零成本搭建AI推理平台](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865100&idx=1&sn=ff8219a72e9800481c1e23911037e804&scene=21#wechat_redirect)

[2048卡昇腾910C集群算力集群交付工程手册](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458863852&idx=1&sn=ac753705858b85d06703dab5c42a3856&scene=21#wechat_redirect)

[2048卡H100算力中心100G无阻塞存储网建设方案](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458862851&idx=1&sn=7eabab449575723128152249370b069a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/LFtqXkV9RiaKRgHrTtpFia7Y5moEEPblhty7omoabxc412kkzxMILS7icItaEspPzrZ4vsWVHzoCAwHeWBghHGyvw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5fL4uXAOMM65ich03QCp6qic3cwTmicnHZA49U7FN4y6cb4bY57OvvctIZH4ftcY5quyNfmPOvACGfVU5upxylUnQ/0?wx_fmt=png)

铁军哥

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5fL4uXAOMM65ich03QCp6qic3cwTmicnHZA49U7FN4y6cb4bY57OvvctIZH4ftcY5quyNfmPOvACGfVU5upxylUnQ/0?wx_fmt=png)

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