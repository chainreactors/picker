---
title: 手把手玩转路由器漏洞挖掘系列-ZigBee协议
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247508470&idx=1&sn=dfd1ab29e0bb1ca56156c689c03be221&chksm=fa527448cd25fd5ec170e8ee587eb3f3d1f366b9652a5b26ead1e2b8a008f1a804379faff2d2&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-10-18
fetch_date: 2025-10-06T18:53:39.801695
---

# 手把手玩转路由器漏洞挖掘系列-ZigBee协议

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnROIulAl5gAzhic8SJiccUdDz2mDsMegibt1ZBdLaFRdicibgicHHibrhDto2laWdpyF6lz9gxSibwMoQI92w/0?wx_fmt=jpeg)

# 手把手玩转路由器漏洞挖掘系列-ZigBee协议

原创

nil

山石网科安全技术研究院

## 1. 基本介绍

ZigBee是一种低复杂度、低功耗、低速率、低成本的近距离无线通信技术。它基于IEEE 802.15.4标准，主要用于短距离数据传输和监控应用。

ZigBee网络由协调器、路由器和终端设备组成，支持星型、树型和网状等多种拓扑结构。该技术广泛应用于智能家居、工业自动化、医疗监护等领域，通过低功耗和自组织网络特性，实现高效、可靠的无线数据传输。ZigBee的传输速率在10KB/秒到250KB/秒之间，支持大量设备连接，具有强大的网络容量和灵活的节点配置能力。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnROIulAl5gAzhic8SJiccUdDzEmqiaySOuBUEOLHLmmUsHvousPcjp5PG1AibRzpJTsrDTy5MrPv10mhQ/640?wx_fmt=png&from=appmsg)

## 2. 协议概述

### 2.1 栈结构

ZigBee协议组成主要涵盖了四个层次，这些层次共同构成了ZigBee网络协议栈的基础，确保了数据的可靠传输和网络的有效管理。以下是ZigBee协议组成的详细概述：

* 物理层

+ 处理无线电硬件之间的实际通信
+ 基于IEEE 802.15.4标准的无线通信技术

* 传输层

+ 管理无线链路，包括处理帧的发送、接收、超时重传、收发确认等
+ 提供了安全和管理机制，如加密、身份认证和底层设备管理

* 网络层

+ 负责多跳网络的支持，主要包括路由选择、拓扑结构和组网等功能(星型、树型和网状拓扑结构)
+ 协调器、路由器和终端设备

* 负责定义不同应用的数据格式和通信规则

+ 节点之间的路由和寻址机制，确保数据传输的可靠性和安全性
+ 不同设备之间的互相通信，允许节点在网络中相互切换

### 2.2 数据帧

#### 2.2.1 具体分布

* 物理层

+ SHR - 前导序列
+ PHR -  PSDU长度信息
+ PSDU - MAC层协议数据单元

* 传输层

+ MHR - 控制信息、序列号、寻址信息等
+ MSDU - 网络层和应用层数据
+ MFR - 帧校验序列

* 网络层

+ 网络层帧头和有效载荷

* 应用层

+ 数据和服务

#### 2.2.2 帧结构

**信标帧**

| 帧控制域 | 序列号 | 地址域 | 附加安全头部 | 超帧描述 | GTS分配释放信息 | 转发数据目标地址信息 | 帧负载 | FCS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

**数据帧**

| 帧控制域 | 序列号 | 地址域 | 附加安全头部 | 数据帧负载 | FCS校验 |
| --- | --- | --- | --- | --- | --- |

**确认帧**

| 帧控制域 | 序列号 | FCS |
| --- | --- | --- |

### 2.3 安全机制

ZigBee主要提供三个级别的安全模式:

* 非安全模式

+ 不采取任务安全措施 - 可重发、中间人攻击

* 访问控制模式

+ 只允许接入的硬件设备MAC地址存在列表中，限制无合法节点访问获取相关数据

* 安全模式

+ 支持128位AES加密算法进行数据通信加密

Wireshark里面提供的安全级别可支持预设密钥用于解析数据包

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnROIulAl5gAzhic8SJiccUdDzpg3sicuzQwG29p7ZVbzaiaiblg8mGkN4SZafsZYI0WHoZbIUgRU5Gzv3w/640?wx_fmt=png&from=appmsg)

2.4 密钥类型

* 主密钥

+ 配合ZigBee对称密钥的建立(SKKE)过程来派生其它密钥，在建立网络时生成或配置的，用于后续生成网络密钥和链接密钥。

* 网络密钥

+ 保护广播和组数据的机密性和完整性，同时也为网络认证提供保护

* 链接密钥

+ 保护两个设备之间单播数据的机密性和完整性

* 其他密钥

+ 除了上述主要密钥外，ZigBee协议还可能定义其他类型的密钥，如应用主密钥、应用链接密钥等，用于特定场景下的安全通信

## 3. 安全风险

#### 3.1 中间人攻击

ZigBee采用非安全模式，对数据传输内容没有加密，可能被窃取敏感数据内容。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnROIulAl5gAzhic8SJiccUdDzUXtB1sKA2glhbGsmzt9A3r07ibkux6osKGvNSq4RzibQOmtpEr0ABibVg/640?wx_fmt=png&from=appmsg)

#### 3.2 密钥攻击

在密钥传输过程中，密钥内容会以明文形式传输，因此可能被获取密钥信息，通过密钥对数据信息进行解密或者伪造合法接入设备。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnROIulAl5gAzhic8SJiccUdDznIXOqBjXgXa7tUUT8x22qLRczaawibiafZXGQBB0B2YL3nxDGZ1iapd1Q/640?wx_fmt=png&from=appmsg)

## 4. 总结

当前，针对ZigBee协议的攻击策略主要聚焦于其密钥安全性的薄弱环节，其密钥安全是整个Zigbee协议中最重要一环。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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