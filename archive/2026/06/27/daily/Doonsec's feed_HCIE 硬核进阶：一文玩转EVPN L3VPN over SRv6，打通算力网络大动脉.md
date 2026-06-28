---
title: HCIE 硬核进阶：一文玩转EVPN L3VPN over SRv6，打通算力网络大动脉
url: https://mp.weixin.qq.com/s/cl3UlQfGZ1Wat9vYGAmRWw
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:13:24.428163
---

# HCIE 硬核进阶：一文玩转EVPN L3VPN over SRv6，打通算力网络大动脉

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9j14GSZeRZag5XBiaIHQsFuOkpW4w85fzu11pA7rtiaWvHrB8l3VTo5jUAkzBmbetD8m7DVsickyMqOaMRu1XPV3QEkGohrsibVLynZic3ibpE7Cc/0?wx_fmt=jpeg)

# HCIE 硬核进阶：一文玩转EVPN L3VPN over SRv6，打通算力网络大动脉

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

基础网络通了怎么跑业务？本文带你在华为NE40E上部署BGP EVPN L3VPN over SRv6 BE，解密End.DT4 SID底层原理，从VRF划分到BGP邻居建立，全景演示EVPN接管传统L3VPN的极简配置。告别私网标签，一张纯IPv6网络搞定所有业务，网规工程师进阶必看的硬核实战指南！

我们之前配置了基于Ubuntu 26.04和FRR搭建SRv6 L3VPN的实验（[告别MPLS！用Ubuntu+FRR+VSR徒手撸一个SRv6 L3VPN，真香！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458867766&idx=1&sn=723eba28f6f04d3aac38762fff2438cf&scene=21#wechat_redirect)），相比于使用企业设备的配置（[验证成功！翼航仿真实训平台完美支持SR-MPLS L3VPN等前沿技术，网络学习利器](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458863151&idx=1&sn=1ccbf3bd4f684ab5ed25b3ee3b6c3fed&scene=21#wechat_redirect)），相对更简单易懂。

在SRv6 BE隧道贯通之后（[告别无脑敲命令！一文吃透SRv6 Locator规划法则与BE隧道打通](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458868386&idx=1&sn=1fce2a1e24fce01140e142f0c8c5783a&scene=21#wechat_redirect)），对于很多干了十来年的传统网络工程师来说，刻在DNA里的操作可能就憋不住了：快！上LDP协议，起L3VPN，分发私网标签！（[MPLS小实验：利用LDP动态建立LSP](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458858116&idx=1&sn=a7ac7de53aecf802aa8a1d4a59739682&scene=21#wechat_redirect)）。但在这个面向未来的网络架构里，MPLS标签体系已经被彻底抛弃。

今天，我们沿用之前的黄金网络拓扑，将组网中的3台CE设备利用起来，用来模拟涵盖三个地市的BGP EVPN L3VPNv4 over SRv6 BE的配置，打通端到端的真实业务承载。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYdnqnwM7RojibJSBpbezJ07pRnE5xqGd6d3b3iaDNbDEM2tdldnzWGiaY8lLfKywTZGPrFibJsUYgSUXZKQ4gBTlHbwseE7EQp7kY/640?wx_fmt=png)

拓扑中一共部署了11台华为NE40E设备，各设备的名称、角色等基础网络配置如下表所示：

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZbAFDP66Vb8Jic9HFLicLdcjb7vmvm3drjrsOD6NnuIUwGhPsN23hndlKa2o4vXpHTTSuBrA4ibn8ZTBica13ibqmcu8ibSggIsxkicdo/640?wx_fmt=png)

骨干网设备之间的完整接口互联表信息如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbIKEiadp7LdDS7GDFCFdxIAAyRichAN9f3dMqicicPzPxATPJcFjxtoApleF8B6UQzVAyGQ2P2WhpWds7NZUrnUGOJTn9Hib4fibcow/640?wx_fmt=png)

CE设备的接入信息如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZDIxuAle5nJiaUXeg7dR9afLzPibRic64hic9N7og6ysJvibhLvldztTLiaP0hqhWFVbic8EnHZkszicMe4sibpqauLDu17w8ZLTJdlTY8/640?wx_fmt=png)

接下来，我们将用EVPN接管L3VPN，打通客户节点CE1、CE2与CE3之间的端到端内网，并一步步揭秘私网路由是如何在纯IPv6报文中完成神秘封装的。

回顾之前的L3VPN配置，我们是没有使用EVPN的，那为什么今天又用上EVPN了呢？

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