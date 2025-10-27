---
title: 字节跳动基于TrafficRoute DNS的超千亿级调度解析优化实践
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247508213&idx=1&sn=a472c9b9686e755b6ffe2d1b280ae32e&chksm=e9d36b17dea4e201ff0de13dc72afe932587f008bf0157cc6cf97a6007e2fad97b4e2e707251&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-07-16
fetch_date: 2025-10-06T17:44:51.992105
---

# 字节跳动基于TrafficRoute DNS的超千亿级调度解析优化实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiasNSNchdYPIlQPLNiarCejeYJlvgqrq2wSBknicdJoCby0guXL33GPUgOeW6XCW0ZgL3qq6CwcuRag/0?wx_fmt=jpeg)

# 字节跳动基于TrafficRoute DNS的超千亿级调度解析优化实践

周杰

字节跳动技术团队

**「摘要：」** 本文介绍了火山引擎TRDNS在泛CDN场景中的实践经验和优化措施。内容从能力出发，详细介绍了遇到的挑战、TRDNS的优化措施、取得的效果。主要能力为以下2部分：

1. 控制台能力，包括专用的IP库管理系统、定制调度API系统
2. 定制调度能力，包括权重与分组响应、智能解析、CNAME加速、302调度、LocalDNS画像

**「Tips：文内有优惠活动，点击「阅读原文」还可以联系我们哦。」**

在直播CDN、静态CDN和动态CDN等泛CDN边缘接入场景中，通常采用DNS来作为边缘第一层的接入调度。由于边缘接入点分布广泛且容易受到外部环境的影响，导致接入点频繁变动，因此，在泛CDN环境中，DNS的基础调度功能显得尤为关键。

以字节跳动集团业务为例，在泛CDN场景下拥有日均超千亿次的解析需求，为保障业务稳定运行，应用了TrafficRoute-DNS（下文简称TRDNS）作为基础调度系统，不仅负责云解析服务，还承担了泛CDN的调度解析服务，支撑起了泛CDN日均超千亿次的解析量。

火山引擎TrafficRoute-DNS 特惠活动火热进行中，扫描文末二维码即可免费申请！

# 01控制台能力

## 1.1专用的IP库管理系统

IP库对于智能解析来说至关重要。由于CDN业务与多家运营商建立了节点合作关系，能够及时获取运营商IP网段的一手资料。每当运营商更新其IP网段，CDN系统就会希望IP库能够迅速做出更新响应。为了满足这一需求，TRDNS开发了一套专用的IP库管理系统。

该系统有以下能力：

1. IP库版本管理能力
2. IP库自定义字段打包能力
3. IP库灰度发布能力

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiasNSNchdYPIlQPLNiarCejeL4gj3GGPGFdD96yhc8o1p6U3UGlEXFamDeb9vq7DSMibVA0A6mnzWJg/640?wx_fmt=jpeg&from=appmsg)

## 1.2定制调度API系统

CDN流量调度系统采用定时任务，以分钟级频率更新调度策略，并将其转换为DNS配置文件。这些文件通过DNS调度API下发至DNS控制面系统，经过一系列数据流操作后，DNS配置信息被存储至DB中。同时，TRDNS执行秒级定时任务，主动拉取DNS控制面系统的增量DNS变更，并通过reload操作更新域名配置。这一流程确保了DNS解析指令能够在分钟级内下发并生效。详细的调度系统如图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiasNSNchdYPIlQPLNiarCejee0gNic01bG2EOTZSpqoEbhok5PZsxUepRQHyOsuFF24N9kicbdjsMEiaQ/640?wx_fmt=png&from=appmsg)

调度API是为CDN系统专门定制的，与标准API接口不同，它需要具备高性能、低延迟的能力，以应对大量DNS解析操作的需求。CDN系统通常需要在分钟级别的时间间隔内下发3000到20000条DNS解析记录的变更。为此，我们对调度API进行了多轮性能优化和调整，确保其能满足这一需求。

# 02定制调度能力

## 2.1权重与分组响应：增强容灾能力

在常规的权重分组设置中，每个记录在同一线路下通常会有独立的权重配置，这会导致DNS解析在一条线路下每次仅能获取一个IP地址。然而，在泛CDN调度场景中，更倾向于解析记录能够轮询返回多条IP，以增强容灾能力。如果只固定返回单个IP地址，在IP异常时，由于LocalDNS的缓存，可能会导致部分客户端在一段时间内持续访问失败，即使重试也无法解决问题。

针对以上场景，TRDNS可以在打开权重后，依然可以响应多个IP。例如针对域名：test.trafficroute.com，我们可以配置两个记录组：

* A组：1.1.1.1，2.2.2.2
* B组：3.3.3.3，4.4.4.4

对于两个记录组分别进行加权：A组加权70，B组加权30。最终我们可以实现分权重响应不同的记录集。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiasNSNchdYPIlQPLNiarCejegUNY85qvTgMQgTpPRh3ibP1Q6ZZvQo65DmMeOV3libjibGFeGWzZvZ50A/640?wx_fmt=png&from=appmsg)

## 2.2智能解析

### 2.2.1运营商+地理位置解析：合理分配、高效利用网络资源

很多CDN的业务需要既有地理位置线路，又有运营商线路。有的国家不同运营商之间的互通性良好，此时，以地理位置为主导的调度策略就能满足服务需求。但在服务字节跳动这样全球化公司的多元化需求时，需要适应多个国家的网络环境，因此，TRDNS需要能够适应同时存在地理位置线路和运营商线路的复杂场景，确保网络资源的合理分配和高效利用。

针对这一需求，TRDNS定义了灵活多变的线路类型，大致可分为三级线路的匹配规则

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiasNSNchdYPIlQPLNiarCejepes0ria385QYO5q8eVlqWlOT0yZia3ib5ib2SjjckKevxibiavZncDX7PAlA/640?wx_fmt=png&from=appmsg)

我们将上述线路分成了两大类：运营商线路和地理位置线路。下面是常见的线路层级关系图示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiasNSNchdYPIlQPLNiarCejeLyhhR9oibMOWSIJPE1D9DBd7XRjTaKaSrkibnJEFj9cBpq9ic3fkAt3lQ/640?wx_fmt=png&from=appmsg)

### 2.2.2小运营商聚合：简化配置、优化地理位置聚合

为了应对国内外运营商的多样性，TRDNS支持将主流国家和地区的运营商逐一列出并纳入预设线路列表。然而，由于小型运营商不易事先获取，这种做法可能无法覆盖所有运营商。

在中国市场，CDN服务通常根据**「运营商优先」**的策略来进行流量调度。在某些情况下，我们希望能够将某地区或省份的所有小型运营商汇聚到一条BGP路上，实现类似“北京”线路的默认服务，即当匹配不到特定运营商时，流量会自动切换到这条默认线路。然而，目前大多数DNS智能解析方案在国内使用运营商线路时，尚无法实现基于地区的流量聚合，这就导致用户只能配置默认线路去做小运营商的兜底。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiasNSNchdYPIlQPLNiarCejeicnwEicWCLxg1CMnyiaBbaPFc4IrRMJDdGZuibAGoVQI9IWlFy3MNhhDOw/640?wx_fmt=png&from=appmsg)

TRDNS通过聚合小运营商线路，为CDN用户提供了一条综合性的“小运营商”线路。这意味着，CDN用户无需分别配置多条北京地区小运营商的线路，如北京电信通、北京长宽、北京教育网、北京科技网和北京华数等，仅需设置一条“北京小运营商”线路即可。这种方式统一了小运营商的地理位置，确保它们都解析到我们指定的该地区的BGPIP地址，达到了简化配置和优化地理位置聚合的效果。

### 2.2.3自定义线路：优化体验、精细化调度

在各种基于DNS的调度业务在线运行过程中，常出现调度不准确的问题。原因包括IP库准确性不足导致LocalDNS出口无法匹配合适的线路、LocalDNS横跨不同运营商或地理位置、以及CDN业务需针对特定客户端定制调度规则。

针对这些挑战，TRDNS推出了自定义线路功能，这一功能与大多数DNS云厂商实现对齐。用户能够提取特定网段并设定自定义线路。利用这些自定义线路，用户可以配置相应的解析规则。

例如，假设LocalDNS出口IP地址5.5.5.5是小运营商A租用中国移动的出口。若沿用既有的CDN配置线路，小运营商A的用户可能会被解析到中国移动节点。通过自定义线路功能，TRDNS单独拉出一条自定义线路：5.5.5.5/32。匹配到此线路的请求将被引导至小运营商A的节点，从而优化其用户体验并节省跨运营商的带宽使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiasNSNchdYPIlQPLNiarCejeDrSribhFpzjLXD4mJsBxAgEoUFEdicaREsK2eDdyyJlZfrVTjTRmLtGw/640?wx_fmt=png&from=appmsg)

### 2.2.4基于质量的调度（动态线路）：优化下载速度

在某些调度场景中，业务方通过大量网络探测，收集众多IP地址至边缘节点的网络性能数据。由此，业务方能够构建一个客户端IP与目标边缘节点间的网络质量地图。

鉴于这种情况，业务方可能需要创建大量自定义线路，其数量有时与IP库规模相当。大量的自定义线路配置会给系统的存储资源和计算能力带来了额外压力。为缓解这一问题，TRDNS与业务部门合作，采用了一套具备质量标识（MPID）的IP库来解决这个问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiasNSNchdYPIlQPLNiarCejevrtfqZDE0ibAvgkO59C3sBdzABqmbxyiaWSVZGGorHYppwvrXGlZh3sQ/640?wx_fmt=png&from=appmsg)

在原有的DNS IP库的基础上，对IP数据打上根据探测得到的MPID标识。CDN调度平台可以配置自定义线路、MPID线路以及地理位置/运营商线路。在字节跳动内部的CDN质量调度实验中，采用了上述的MPID线路进行局部优化调整，在越南地区进行了对照实验，资源平均下载速度可以提升约5%~10%。

## 2.3CNAME加速：解析速度约提升30%

CDN系统通常通过CNAME接入业务域名，有的系统为了方便调度，会对业务域名设置多级CNAME。例如，业务域名A要接入CDN，其解析配置可能为 A CNAME B，同时 B CNAME C。在这种情况下，递归DNS通常要对每个CNAME的域名单独进行递归迭代，才能从权威拿到最终的A记录。

但当域名A、B、C都属于同一权威集群时，我们可以对这部分的解析响应做加速。当权威DNS收到请求A后，能够直接将后续的CNAME B、CNAME C和响应IP一并返回给递归DNS，这样的操作称为CNAME加速。对比分析图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiasNSNchdYPIlQPLNiarCejeqAZQPAwRgfgibJ2Acd3qvlRHICrOJBiaLsEJse2wXPs63V5oNSKbcFZw/640?wx_fmt=jpeg&from=appmsg)

分析上述对比可知，实施CNAME加速的系统相较于未加速的系统，能够根据CNAME链的长度减少递归DNS至权威DNS的往返时间（RTT）。然而，在实际系统中，由于根域迭代的影响，可能会产生额外的延迟。

在实际的生产环境中，这种差距通常不会如此显著。这是因为递归DNS会缓存查询结果，多数DNS请求能够利用到这些未过期的缓存，避免递归DNS与权威DNS之间的额外交互。在特定环境和特定CDN业务场景下，启用CNAME加速后，我们观察到DNS解析速度大约提升了30%。

## 2.4302调度：减少配置量、降低系统资源消耗

在CDN调度系统中，302调度会对边缘节点的调度进行重定向。这种重定向会根据最优调度决策动态访问一个节点。例如，用户访问某一个边缘节点后，边缘节点对访问资源重定向到另外一个边缘节点，基于安全考虑，302重定向通常采用HTTPS访问。

由于边缘节点的数量庞大，可能达到十万甚至百万级别，每个节点IP对应一个DNS记录，这会导致DNS记录数量激增，占用大量DNS系统资源。为了解决这个问题，TRDNS系统提供了一种自适应的智能解析机制。用户只需将解析地址嵌入域名中，TRDNS即可自动解析地址并作为响应返回。例如，用户请求1.1.1.1.bytedance.com，TRDNS会返回1.1.1.1的A记录。

CDN的边缘节点是动态变化的，部分现在归属于火山引擎/字节跳动的IP，半年后可能是归属其他公司的不可控节点。而不可控节点如果部署了非法/黑产服务，可能涉及安全隐患。2023年Q3，我们为CDN系统开放了域名加密能力。即针对这种场景的域名，用户可以加密包含IP信息的部分，然后用加密后的信息组成目标域名。权威DNS收到目标域名的解析请求后，会按照约定算法解密IP信息，从而做出期望的A/AAAA记录响应。另外，加密域名通过过期时间机制控制其生效时间，提高系统的安全性。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiasNSNchdYPIlQPLNiarCejeB1O8CSu5Co2g0YsTbue3ialiauo8ibic0XgQY2IfJGjlf3bR0LlTnoA5lQ/640?wx_fmt=jpeg&from=appmsg)

## 2.5LocalDNS画像：精细调度

权威DNS一般只支持到省份运营商的线路级别，这个调度粒度在大流量场景下可能无法满足业务需求。一方面，可能存在某些省份运营商的流量过高还要继续分流的情况；另一方面，权威DNS的线路识别依赖于客户端IP归属线路，而客户端IP在权威DNS侧通常是LocalDNS的出口IP，LocalDNS出口IP一旦识别错误，就会导致调度的错误。

如果我们有一套系统，可以对全国乃至全球的LocalDNS进行分析，得到每个LocalDNS的出口IP，以及每个LocalDNS对应的客户端IP/客户端流量。那我们就可以针对LocalDNS的出口IP做自定义线路，实现对于单LocalDNS集群的流量调度，这个也是权威DNS调度理论上可以达到的最精细调度。而这套系统的重点，就是需要分析出每个LocalDNS对应的客户端IP。即任意给定一个客户端IP，我们都可以知道要调度哪个LocalDNS会对这个IP的流量生效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiasNSNchdYPIlQPLNiarCejearAZwBiaC0tSfSg6J59tXFeNtbT0hvHGDNAiaicciaD1IwvHnanA6KwTZw/640?wx_fmt=png&from=appmsg)

TRDNS设计了一套基于CDN 302调度的LDNS画像系统，其核心思路在于：

1. 客户端请求CDN 302服务器时，CDN可获取真实的外网客户端IP，解决了权威DNS无法直接拿到客户端IP的问题。
2. CDN 302服务器拿到客户端IP后，把客户端IP信息放进重定向的域名内。例如重定向到目标www.bytedance.com，客户端IP是1.1.1.1；则302调度系统会把域名改为1-1-1-1.www.bytedance.com。
3. 客户端发起对于1-1-1-1.www.bytedance.com的域名解析请求，权威DNS拿到该域名。在权威DNS侧事先约定bytedance.com的解析是302调度/LocalDNS画像的域名，则我们拿到这个DNS解析请求后，可以知道客户端IP是1.1.1.1，然后可以记录到日志内；另外，权威DNS也可以记录下LDNS的出口IP。
4. 日志分析系统/数仓可以拿到客户端IP和LDNS出口IP的映射关系，基于这个数据，权威DNS可以结合自定义线路，做LDNS级别的流量调度。

# 写在最后

DNS是互联网最基础的寻址服务。当服务部署在多个地址时，如果DNS服务总是能够快速选出最优服务地址返回给访问者，用户体验会得到明显提升。在泛CDN环境中，DNS的基础调度功能不仅是一种技术手段，更是实现高效、安全、可靠内容分发的核心中枢。

从字节跳动超千亿级调度解析优化实践中，火山引擎TrafficRoute DNS经过业务验证，目前部分功能已向外部用户开放。同时，火山引擎TrafficRoute解析调度套件提供了从公网到私网、从递归到权威的全链路DNS服务以及基于DNS的流量调度服务，包含了云解析（DNS）、云调度（GTM）、私网解析（PrivateZone）、移动解析（HTTPDNS）、公共解析（PublicDNS）。

目前域名与网站特惠活动火热进行中，欢迎微信扫码抢购！

* 域名注册与转入低至1元
* SSL证书低至1折
* DNS版本1元升级
* HTTPDNS资源包1折起......

多重优惠活动等你来！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOiasNSNchdYPIlQPLNiarCeje7YY1LEJcu3btnqrLehVcSO36QLpBsYjWsVXqf92Kiapnhw4lorvZTzw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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

...