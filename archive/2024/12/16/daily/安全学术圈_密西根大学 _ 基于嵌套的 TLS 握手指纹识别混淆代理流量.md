---
title: 密西根大学 | 基于嵌套的 TLS 握手指纹识别混淆代理流量
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491461&idx=1&sn=71b5e815f8c2dbbb36473d7031fadf06&chksm=fe2ee00ec959691842d5000789a0fe68c1b1dfc71b2f69ec23dd8a8c20df8eace345eb8b424a&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-12-16
fetch_date: 2025-10-06T19:36:42.469581
---

# 密西根大学 | 基于嵌套的 TLS 握手指纹识别混淆代理流量

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WGOuZeXGmVwd7AOxCKeN8pWuWOL2caicP78qDfouUgQwSbAJCuC81oAG6yTaApdC7R24EqticNRIWmg/0?wx_fmt=jpeg)

# 密西根大学 | 基于嵌套的 TLS 握手指纹识别混淆代理流量

原创

孙汉林

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGOuZeXGmVwd7AOxCKeN8pW9I0p0BJ1aMMT3CgWcSxicrVkIMgJANicIib5V281mhlSIoS8T3HR3A1aA/640?wx_fmt=png&from=appmsg)
> *原文标题：Fingerprinting Obfuscated Proxy Traffic with Encapsulated TLS Handshakes*
> *原文作者：Diwen Xue, Michalis Kallitsis, Amir Houmansadr and Roya Ensafi*
> *原文链接：https://www.usenix.org/conference/usenixsecurity24/presentation/xue-fingerprinting*
> *视频链接：https://www.youtube.com/watch?v=8GO\_9HKTvb0*
> *发表会议：USENIX Security '24*
> *笔记作者：孙汉林@安全学术圈*
> *主编：黄诚@安全学术圈*

### 1、前言

目前用于绕过审查机制的流量混淆代理方法可大致分为三种，即`模拟化`、`随机化`和`隧道化`。

* **模拟化**：通过模仿，使流量看起来像合法的协议（例如HTTP、Skype、DNS等）。但完美复刻某一合法协议是困难的。
* **随机化**：通过加密，使流量变得随机，从而消除某些特征，使流量看起来不像被拦截的（例如shadowsocks、vmess、obfs4等）。但会使流量熵值增大，可能作为拦截特征之一。
* **隧道化**：通过嵌套，使流量嵌入到合法协议中（例如Snowflake）。但外层合法协议仍可能会暴露一些指纹特征。

针对于上述三种混淆方法来说，目前的检测方法大都依赖于特定协议相关的特征，如针对vmess混淆要检测熵值，针对Snowflake要检测DTLS指纹等。而该篇论文，通过对23种混淆代理方法，包括shadowsocks、vmess、trojan、vless，以及先前研究中提出的httpt协议的测试，提出了一种通用的混淆代理流量检测方法，即基于嵌套的 TLS 握手指纹识别。且检测结果的真阳性率（TPR）均超过70%。

### 2、实验原理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGOuZeXGmVwd7AOxCKeN8pW8Mdg7fhfU8uwhDkOHTJJiaVYOYiaBuEj3APLs1qEcEdicGhfXseQiaeQcA/640?wx_fmt=png&from=appmsg)

本文提出了一种新的的TLS指纹特征，称为“嵌套的TLS握手”（encapsulated TLS handshakes）指纹。嵌套的TLS握手指的是TLS握手发生在表层协议（cover protocol）内部，通常是由用户应用程序（如浏览器）生成TLS握手，然后由代理协议加密并传输这些握手信息到代理服务器，代理服务器再将其转发到最终的目标服务器（如Web服务器）。与标准的TLS不同，标准TLS的握手是明文的，可以被识别和解析，而嵌套的TLS握手则是嵌套在协议内部，以密文形式呈现。

TLS设计是为了保障端到端的通信安全，因此如果在已加密的表层中又出现了嵌套的TLS握手（如嵌套在外层TLS内），这表明存在多余的加密机制，则极为可能是混淆代理流量。同时嵌套的TLS握手指纹因具有如下3个特性，从而使其得以作为优势特征。

* **区分性（Distinct）**：嵌套的TLS握手具有明确的特征，ClientHello消息通常为200-550字节；ServerHello消息（包含证书）可以达到数千字节，且不同流之间差异较大。即使经过加密，这些特性（大小、时间间隔、方向）仍然可见。
* **可靠性（Reliable）**：TLS是互联网通信的核心协议，广泛用于各种应用中，因此代理用户几乎无法避免生成TLS相关指纹。
* **精确性（Precise）**：嵌套的TLS握手是代理连接的独特标志，并且实验数据表明，这种行为几乎仅出现在代理中，误报率极低，对正常流量的影响最小。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGOuZeXGmVwd7AOxCKeN8pWxElc9Bibvdx04pME7jw62g0dM5SZWhAyZjLgJdVwTvZJKthUdVBu9MA/640?wx_fmt=png&from=appmsg)

与针对表层协议的攻击检测方法（如图2中的蓝色部分）不同，本文的攻击检测方法侧重于嵌套在协议内部的TLS握手所产生的指纹（如图2中的红色部分）。这意味着：该攻击方法可以补充现有的主动或被动指纹识别策略，从而提高检测的准确性；现有的防御措施，如uTLS（一种用于伪装TLS流量的工具），无法有效对抗本文的方法，因为它们主要混淆表层协议，而本文的攻击方法针对嵌套在隧道中的TLS流量的指纹。

### 3、实验设计

#### 3.1、数据采集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGOuZeXGmVwd7AOxCKeN8pWXYZ2U55KfJ3EYtibcD0gSV3XRofZXKjlkD3G6ibRliayZlfvToHsichUOw/640?wx_fmt=png&from=appmsg)为了采集训练数据集，本文在ISP网络中设置监控站点，获取50 Gbps流量的镜像副本。从中仅筛选TCP流量，要求观察到SYN和SYN-ACK包，确保捕获连接的初始化阶段，并记录前Wo（窗口值）个数据包，丢弃短时连接。对于TLS流量，根据ServerHello消息中的Supported Version字段区分TLS 1.2和1.3，过滤掉SNI字段为空或无Application Data消息的流量。由于单台服务器处理性能有限，本文又基于IP对对流量进行1/8采样，以降低丢包率，最终生成包含TLS和非TLS流量数据集。

#### 3.2、特征提取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGOuZeXGmVwd7AOxCKeN8pWJlX6CdQibNWj6ia0OnQPLV6U0tf2ntZ5rPFOCgSG0ycic7VRcMaWMMGdQ/640?wx_fmt=png&from=appmsg)

在提取特征时，每条流被表示为一个整数序列，从这些序列中提取3-grams特征，L代表TCP载荷大小区间，符号表示方向以捕捉协议握手等特定模式。此外，引入“burst”特征，即估算连接的RTT（从观察到SYN包到接收首个ACK包的时间），然后将方向一致且到达时间间隔小于三倍RTT的连续数据包聚合为一个突发。这些特征有效区分了批量传输与交互式通信。

#### 3.3、分类器构造

本文通过结合卡方检测（Chi-squared Test）和马氏距离（Mahalanobis Distance）构建分类器。

* **卡方检测（Chi-squared Test）**：用于分析和比较流量中的3-grams特征，目的是捕捉流量的局部包序列模式和状态转换特征。通过计算不同类别（TLS和非TLS）之间的3-grams频率分布差异，利用3-grams特征进行流量分类，判断流量是否属于TLS。
* **马氏距离（Mahalanobis Distance）**：用于衡量流量中“burst”特征的多变量距离，聚焦于流量的全局动态。它考虑到不同维度（例如不同方向的突发流量）的变异性和维度之间的协方差，用来评估TLS握手过程中的流量特征。马氏距离通过规范化不同维度的变异性，提供了一种更为鲁棒的距离度量，有助于区分不同TLS握手阶段的流量。

分类器综合两种测试结果，仅当两者均满足条件时将流量分类为TLS流量。除此之外，本文还针对TLS的版本不同，构造了不同的分类器。

#### 3.4、分类器评估

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGOuZeXGmVwd7AOxCKeN8pWTwkUNy8icdwEgDTpTOkWnzlMSKsev2EFSeJHKkft7axtKGJcThvLbOg/640?wx_fmt=png&from=appmsg)研究人员选择了多种代理配置，包括基础代理配置（如vmess、Shadowsocks、Trojan、vless）、高级代理配置（如vmess-over-tls、shadowsocks-over-websocket-over-tls）和多路复用配置。通过设立特定的客户端生成代理流量（非该客户端产生的流量为背景流量），并对其进行分析。对于TLS流量，去除了TLS握手包以聚焦于嵌套的TLS握手。研究人员利用实际TLS流量训练和测试统计模型，并针对代理协议的流量特征进行分类器调整，包括考虑填充机制带来的流量变化。

### 4、实验结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGOuZeXGmVwd7AOxCKeN8pWJWvEteVDYdictzINoIjqqGeIXF0eHicS0SzeXVa5qw5AFia2BSyF6WPgA/640?wx_fmt=png&from=appmsg)实验结果总结如下：

1. **检测效果的可观性**：研究在30天内对超过36TB的流量进行了评估，结果表明在大多数非多路复用代理流量上表现出较高的真阳性率（如vmess、Shadowsocks、Trojan和vless的TPR超过70%）。即便是在随机填充和嵌套协议的高级代理配置下，检测框架依然能够有效区分代理流量与合法流量。
2. **嵌套协议的脆弱性**：将代理流量嵌套在其他协议（如TLS或HTTP）中并未显著提高对抗流量分析的能力。即便使用嵌套协议，嵌套的TLS握手特征依然能够被有效识别。
3. **随机填充的局限性**：虽然随机填充机制可以增加检测难度，但填充范围有限（如vmess的[0, 63]字节）会导致填充流量的特征仍然可被识别。更加复杂的填充机制（如XTLS-vision和obfs4）虽然可以降低TPR，但仍需付出显著的资源和计算代价，且其使用的随机填充和协议特性依然面临被识别的风险。
4. **多路复用的有效性**：引入连接多路复用显著降低了真阳性率（TPR下降超过70%）。多路复用通过将不同应用流混合在同一连接中，破坏了嵌套TLS握手流量的大小和时序特征，从而提升了抗检测性。然而，在仅有单一应用流的场景下，多路复用的效果受到限制。
5. **误报率分析**：研究者对检测框架的误报情况进行了分析，发现部分被标记为混淆代理流量的连接实际上属于正常的互联网流量。这表明检测框架存在误报问题，特别是在标记某些正常服务流量时需要进一步优化。
6. **TLS版本比较**：通过测试Cloudflare的前1K域名，分析了两种协议版本在实际流量中的表现。结果显示，TLS 1.3的分类器真阳性率增高的同时，也伴随着误报率的显著增长，主要由于其握手过程更短且特异性较低；而TLS 1.2分类器在保持较低误报率的同时，能有效检测大部分TLS 1.2代理流量。鉴于非复用代理通常生成大量流量，审查机构只需检测到其中一个流即可，因此研究认为，目前最佳策略是针对TLS 1.2的握手流量进行检测，因为其仍占据显著的流量比例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGOuZeXGmVwd7AOxCKeN8pWmIva8o2AKOJBGD2vpGSODyBXROXXyZYLuKEk2icNl5dTnudEpDNaHyA/640?wx_fmt=png&from=appmsg)

### 5、总结

该研究表明，通过利用嵌套TLS握手特征，可有效检测混淆代理流量，即使其采用随机填充和嵌套层进行保护。尽管这种方法具有较低的误报率并对协议类型相对无感，但仍可能将合法连接错误标记为代理流量。代理开发者需预见TLS握手可能被利用为流量指纹，开发更高级的混淆机制，如多路复用和专用混淆层，以打乱流量的大小、时间间隔和方向模式。多路复用能通过交错多个流的流量扰乱流量模式，而专用混淆层则可进一步通过流量调度和虚拟流生成隐藏指纹特征。此外，该方法不仅适用于TCP代理，也适用于UDP代理和VPN，强调了嵌套协议堆栈的普遍风险。

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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