---
title: 手把手玩转路由器漏洞挖掘系列-ZiggBee协议
url: https://www.4hou.com/posts/6MmQ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-24
fetch_date: 2025-10-06T18:47:08.808632
---

# 手把手玩转路由器漏洞挖掘系列-ZiggBee协议

手把手玩转路由器漏洞挖掘系列-ZiggBee协议 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 手把手玩转路由器漏洞挖掘系列-ZiggBee协议

kkk
[行业](https://www.4hou.com/category/industry)
2024-10-23 12:46:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)69695

收藏

导语：当前，针对ZigBee协议的攻击策略主要聚焦于其密钥安全性的薄弱环节，其密钥安全是整个Zigbee协议中最重要一环。

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

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?HJOVTOIx)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/98f79ba32940c0b6cefd012e336c1911.jpg)

# [kkk](https://www.4hou.com/member/RPoV)

NEURON

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/RPoV)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)