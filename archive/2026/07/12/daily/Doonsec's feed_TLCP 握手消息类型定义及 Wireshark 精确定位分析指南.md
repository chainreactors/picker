---
title: TLCP 握手消息类型定义及 Wireshark 精确定位分析指南
url: https://mp.weixin.qq.com/s/Fvt-QpvwdDny_kn_Q_xyag
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:25:58.112768
---

# TLCP 握手消息类型定义及 Wireshark 精确定位分析指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZaibroIiatwe36qozw8hWHjbP8a7cLiblxjMCCN8IfCib7y5LjXPakkkGLaKy2tlRa0DsF3scESeCaJccOribZabgFEWCV974aribhSmhjiczNGUm4/0?wx_fmt=jpeg)

# TLCP 握手消息类型定义及 Wireshark 精确定位分析指南

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe1KDtVUpGZ5j0kBss3Dw4OblXYPMg88BZoy1ibLTianRhepACjkeNIz4G9xCqfczRicbWhffyuxQ31mjkVOn03nHaRuniccZXgcd90/640?wx_fmt=jpeg&from=appmsg)

TLCP 握手消息类型定义及

Wireshark 精确定位分析指南

GB/T 38636 · tls.handshake.type · 国密SM套件识别

01

PART

前言与背景

BACKGROUND

本指南基于国家密码管理局发布的 **TLCP（传输层密码协议，GB/T 38636）** 标准，对握手层（Handshake Layer）的消息类型进行详细拆解。同时，为您提供 Wireshark 网络抓包工具中**精准过滤、定位此类消息**的高级实用命令。

02

PART

握手消息类型定义

HANDSHAKE TYPES

...text

握手消息类型定义如下：

enum {

client\_hello(1), server\_hello(2),

certificate(11), server\_key\_exchange (12),

certificate\_request(13), server\_hello\_done(14),

certificate\_verify(15), client\_key\_exchange(16),

finished(20), (255)

} HandshakeType;

03

PART

完整 TLCP 握手消息类型对照表（已修正）

TYPE TABLE

| 消息名称 (Name) | 枚举值 (Type) | 发送方 | 核心作用 |
| --- | --- | --- | --- |
| client\_hello | **1** | 客户端 | 发起连接，协商国密套件与随机数 |
| server\_hello | **2** | 服务端 | 确认协议版本与选定的国密套件 |
| certificate | **11** | 服务端 | 发送包含 SM2 公钥的国密 X.509 证书链 |
| server\_key\_exchange | **12** | 服务端 | 发送 ECDHE 临时公钥及 SM2 签名（实现前向保密） |
| certificate\_request | **13** | 服务端 | 向客户端请求国密证书（双向认证时使用） |
| server\_hello\_done | **14** | 服务端 | 标记服务端握手消息发送结束 |
| certificate\_verify | **15** | 客户端 | 使用 SM2 私钥签名验证（双向认证所需） |
| client\_key\_exchange | **16** | 客户端 | 发送客户端 ECDHE 临时公钥参数 |
| finished | **20** | 双方 | 基于 SM3 的 PRF 验证整个握手过程完整性 |
| (保留) | **255** | - | 协议系统保留值，不能用于实际消息 |

04

PART

Wireshark 精准定位命令及逐个代码分析

WIRESHARK FILTERS

Wireshark 中针对 TLCP/TLS 协议的过滤器需要精准无误。以下是针对所有握手包的精准过滤命令及详细代码解读。

1. 过滤所有握手记录层数据包

...wireshark

tls.record.content\_type == 22

**命令分析**：

tls：协议名称。TLCP 记录层与 TLS 记录层结构完全一致，因此使用 tls 作为前置域名。

.record：指明我们要过滤的是“记录层（Record Layer）”。

.content\_type：记录层头部的一个 1 字节字段，指示记录层内部承载的高层协议类型。

== 22：比较运算符及数值。根据 TLCP/TLS 标准，**数值 `22` 固定代表“握手(Handshake)”协议**。因此该命令等同于：**“筛选出所有包含握手内容的记录包”**。

2. 精确过滤特定的握手消息类型

Wireshark 支持直接依据握手头部字节进行精确定位。命令格式为 tls.handshake.type == [枚举值]。

| 想要定位的握手包 | Wireshark 精准过滤命令代码 | 注意事项 |
| --- | --- | --- |
| 客户端问候包 | tls.handshake.type == 1 | 握手流量的起点 |
| 服务端问候包 | tls.handshake.type == 2 | 密码套件协商成功的标志 |
| 国密证书包 | tls.handshake.type == 11 | 可在此查看具体的 X.509 证书链 |
| 服务端密钥交换 | tls.handshake.type == 12 | TLCP 国密 ECDHE 核心交互包 |
| 证书请求包 | tls.handshake.type == 13 | 双向认证的关键信号 |
| 服务端 Hello Done | tls.handshake.type == 14 | 等待客户端下一步动作的分水岭 |
| 证书验证包 | tls.handshake.type == 15 | 客户端身份合法性校验包 |
| 客户端密钥交换 | tls.handshake.type == 16 | 最终完成密钥协商的核心包 |
| 结束包 | tls.handshake.type == 20 | 握手成功建立的“通关凭证” |

3. 快速识别 TLCP 国密流量的附加技巧

由于 TLCP 并不完全通过版本号标识自己，而是通过**密码套件（Cipher Suites）**被识别出来的。

**正确的 Wireshark 套件识别命令**：

...wireshark

tls.handshake.ciphersuite contains "SM3" || tls.handshake.ciphersuite contains "SM4"

**代码分析**：tls.handshake.ciphersuite 字段存储了协商出来的密码套件名称。通过 contains "SM3" 或 "SM4"，可以快速精准地过滤出使用了国密哈希（SM3）和国密对称加密（SM4）的流量。

**标准 TLCP 国密套件名称列表**：

1. TLS\_ECC\_SM4\_GCM\_SM3

2. TLS\_ECC\_SM4\_CBC\_SM3

3. TLS\_SM4\_GCM\_SM3

4. TLS\_SM4\_CBC\_SM3

⚡ **高级实战建议**：

如果在抓包时发现 Server Hello 消息中，Cipher Suite 字段显示为上述包含 SM 开头的国密套件，则**无论 Wireshark 的协议列显示为 TLS 还是 TLCP，均可确定这是一条 TLCP 国密流量**。

我是利刃信安，网络安全和密码安全、数据安全领域的小白。

如果你觉得今天这篇有收获，欢迎点赞、在看、转发三连，我们下篇见

点赞

在看

转发

如有疑问，请联系： Mannix6

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDwLQW9Nbb5QtE0yibdww/0?wx_fmt=png)

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