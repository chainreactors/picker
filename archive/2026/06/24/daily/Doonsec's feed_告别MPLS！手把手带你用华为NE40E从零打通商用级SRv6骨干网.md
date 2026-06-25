---
title: 告别MPLS！手把手带你用华为NE40E从零打通商用级SRv6骨干网
url: https://mp.weixin.qq.com/s/Z4u-ZdntUwHCQEvx2upb4Q
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:07:31.745663
---

# 告别MPLS！手把手带你用华为NE40E从零打通商用级SRv6骨干网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9j14GSZeRZaVhcmU244N8M29IVeXfIGpWadnBTPw0fqiaA4OYKhNyYHHQRCaTXzRLgKwRmSmfxDFCb1fW8ekDxdcZicC1jqM56icCVQCthZlVc/0?wx_fmt=jpeg)

# 告别MPLS！手把手带你用华为NE40E从零打通商用级SRv6骨干网

原创

衡水铁头哥
衡水铁头哥

铁军哥

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前言

抛弃繁杂的LDP与RSVP-TE，迎接SRv6大道至简的时代。本文教你用华为NE40E搭建纯正的商用级SRv6骨干网！详解华为NE40E骨干网重构实战，囊括P2P网络类型、Wide开销等避坑指南。从角色分离到IPv6高阶寻址，全景展现IS-ISv6收敛过程，干货满满，网工必看！

要说SRv6，我现在也算是个老玩家了。

最开始，我们使用H3C的VSR设备搭建了一张基础SRv6骨干网（[付出总有回报，全国SRv6组网实验成功了！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458854603&idx=1&sn=1d371a446628f2d8ce5253093ed323be&scene=21#wechat_redirect)），仅公众号平台就超过8万人阅读过，全网数量超过十万人。

后来，在全国劳模林实践同志提供的福建电信实验环境中，我们又使用华为NE40E设备复刻了运营商级的SRv6骨干网配置（[超越SR-MPLS！SRv6实测：基于纯IPv6数据面承载IPv4 VPN业务，体验协议简化之美](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458863205&idx=1&sn=91a7936ffb23ea3f42a2058396fa52ac&scene=21#wechat_redirect)）。

考虑到大家的实验环境有限，我们又基于Ubuntu 26.04和FRR推出了一系列的文章，从基础架构搭建（[NVUE逼我掀桌子：手把手教你榨干Linux 7.0的SRv6网络性能](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458867668&idx=1&sn=39c836a3d37ff038b3510735fc6363cc&scene=21#wechat_redirect)），到L3VPN实战（[告别MPLS！用Ubuntu+FRR+VSR徒手撸一个SRv6 L3VPN，真香！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458867766&idx=1&sn=723eba28f6f04d3aac38762fff2438cf&scene=21#wechat_redirect)），再到L2VPN实战（[跨越地域的大二层怎么通？用一个218字节报文带你看透SRv6 L2VPN转发真相](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458867809&idx=1&sn=4cb7717347a1c87ba0729186e2fd555f&scene=21#wechat_redirect)），一直到uSID压缩（[嫌SRv6报文太胖跑不动？带你在Ubuntu+FRR实战uSID微段压缩](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458868030&idx=1&sn=d90cb13b743b9188feb5eb24212e369f&scene=21#wechat_redirect)），实现了通杀，堪称低成本实战SRv6骨干网的典范。

但是，野路子终归只是敲门砖，低成本只能让大家离SRv6更进一步，对于HCIE认证或者软考认证，我们还是要回归企业级设备，例如华为NE40E设备。同时，我们还需要一张能充分展示SRv6骨干网的全新拓扑，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYZchoez6EViaMdyc7c27TbUhGSFJyNX84PQCdcc90fScDK9JPIicxIjTNfq4Iz3P0CSWUo4ZvgoD3icrDa9aTTFxDt6jh5z0Rbog/640?wx_fmt=png)

首先，还是那个老生常谈的问题，在迈入SRv6之前，我们必须拷问灵魂：为什么现有的MPLS网络必须要被革新？（[超越BE！实战演示SR-MPLS TE显式路径规划，为VPN业务提供可靠性能保障](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458863994&idx=1&sn=037a32d5d19011a822e5f1985e19db20&scene=21#wechat_redirect)）

如果你维护过跨域的MPLS VPN，或是尝试在MPLS-TE下部署过流量工程（[使用RSVP-TE配置跨域的MPLS TE隧道](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458858979&idx=1&sn=39400839ca175bbba4bf1f302b309919&scene=21#wechat_redirect)），你一定会对那复杂的协议栈深恶痛绝。LDP负责分发标签，RSVP-TE负责建立隧道，OSPF/IS-IS负责底座路由，BGP负责传递业务。这就好比一座摇摇欲坠的纸牌屋，协议之间的状态联动极其脆弱，牵一发而动全身，一旦出故障，排错难度堪称地狱级。

而今天，我们使用的这套清爽且面向未来的黄金拓扑架构，具有以下特点：

1、角色绝对分离。核心P节点只负责高速转发，边缘PE节点负责业务接入，独立的RR（路由反射器）负责全局控制面的路由分发。

2、双核心链路。所有的核心节点（P1/P2）均采用双链路上联与下联，这绝非简单的冗余，而是为后续基于SRv6 TE Policy的高带宽/低延时切片引流提前埋下伏笔。

了解了这些，接下来，让我们来一场开场重头戏，从0到1打通SRv6物理骨干网底座。

首先，拓扑中一共部署了11台华为NE40E设备，各设备的名称、角色等基础网络配置如下表所示：

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZbv3xOGVFSZ0AhjShMKLxAwlbgV6KFwLfVJqsX265Jmd53y7iaR9aQquP9WzqpnPiaMwNK5LVe6ZnQIrT5CVWhukW6CQy7FleQeo/640?wx_fmt=png)

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