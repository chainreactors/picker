---
title: 盛邦安全EADA卫星互联网内生主动防御架构研发成功，研究成果发表《中国科学：信息科学》
url: https://mp.weixin.qq.com/s/HT67puHl8uatAPgRXBKZgg
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:15:17.229182
---

# 盛邦安全EADA卫星互联网内生主动防御架构研发成功，研究成果发表《中国科学：信息科学》

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qU881dbu58nau4mu4A3wvtoAUudD7zEqJDYDU9u0CB7SmKJcbbyhDI4cjTljIkw0AyVtau4nEBtynXTbTK9ic50PAwudtF4zPfTX5HJ2WnWU/0?wx_fmt=jpeg)

# 盛邦安全EADA卫星互联网内生主动防御架构研发成功，研究成果发表《中国科学：信息科学》

盛邦安全WebRAY

![]()

在小说阅读器中沉浸阅读

以下文章来源于中国科学信息科学
，作者SCIS

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM49icmUjR3ib6via9BqmYoibkmr1hu9ibXoF6UibqFQrJ4miblicw/0)

**中国科学信息科学**
.

《中国科学：信息科学》及其英文版《Science China Information Sciences》的宣传平台。

‍![](https://mmbiz.qpic.cn/sz_mmbiz_png/nlWISd01LSxMlk4OfoD1dxo8wMBUWcmyeDcfCjsz84eeVj17ct2EqhTmx14rpkx1gpQoXn1VVMMsuGkBd3sialA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qU881dbu58n7Rg7ib5ia88hJibpk5kVfjFuka0Y4JlnyiaibSqwcMJnTdRkmgy8t949ShUYmksvQJwAPkFKLItDqbxdKbasy2EQecWYJ0tNINRvg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nlWISd01LSxCAwDDQicPogBSePFv1gpakd1oh0xbYLnaroqE9GbUk7rnQVwtKVYA6icOVQBbq4LevDxnNUlY9iauA/640?wx_fmt=png&from=appmsg)

#卫星互联网安全；#主动防御；#内生安全；#SRv6；#防御架构；#合规审计

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nlWISd01LSz3xRanXiaUO0e8n5V70Rd6uPt99n4CvWRcjx8w05fxMKxwA9Wbxb3qITYs6HZOpuibXRia7jNhtz92w/640?wx_fmt=png&from=appmsg)

研究意义

卫星星座凭借广覆盖、低时延、高宽带等固有优势，已成为移动通信与应急保障等应用的首选方案，但其广域开放、边界模糊、军民混用、信道共享等特性导致攻击高频化和攻击面扩大，卫星互联网已成为网络空间攻防对抗的新战场。卫星互联网的安全问题并非单点风险简单叠加，而是贯穿星座测控、运维管控、融合通信、网络接入和全球合规五个层面的深度耦合的系统性挑战。在此背景下，将安全能力嵌入系统自身设计，使系统建设之初即具安全属性，并在运行过程中可自适应演化，实现主动防护与持续优化的内生安全能力。现有安全实践多沿用互联网流行的边界防御和被动响应范式，然而，在广域开放、拓扑剧变、主权交错的卫星互联网环境中已捉襟见肘。简单叠加零散安全能力只能形成复杂且脆弱的防线，难以抵御高级持续性攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qU881dbu58mhxIZamzn7RDWgfhZwibe8bTpXpBdtClzFerpibnsENzFNg0bE4T7ZUUWX86uXgTSCpqPgw9eS95vlgFflef4WefHGJDDjS4VWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nlWISd01LSz3xRanXiaUO0e8n5V70Rd6ur6cfeXKYatqf2UFzWN7YnmSOStXdM61JA9jajnFOwlAYKOfTEOdAZw/640?wx_fmt=png&from=appmsg)

本文工作

为了解决上述问题，本文跳出传统安全思维，结合对成熟卫星互联网体系的测量、测绘与安全分析，提出一种全新的安全范式。

本文的创新点如下：

1.系统性分析了互联网采用的边界安全和被动响应机制在低轨卫星互联网场景下的不足。通过理论建模与比分析，揭示以VPN和应用层联邦认证为代表的叠加式安全机制，其依赖的拓扑相对稳定与中间节点资源充足等假设，在低轨星座拓扑高频重构和星载资源受限条件下难以成立。

2.提出了一种扩展IPv6的分段路由（Segment Routing over IPv6，SRv6）协议的“身份-路由融合”内生防御架构（EADA）。不同于仅在应用层或接入点实施访问控制，EADA从协议层将跨域联邦身份与授权语义内生嵌入网络层转发过程，使安全属性直接约束数据包的可达路径。通过引入可验证的安全段标识，该架构在不引入新型路由协议的前提下，实现了基于密码定义的网络层微隔离技术，显著提升了共享物理网络中的逻辑安全性。

3.设计了一种面向星载资源受限环境下的轻量化验证体系，支撑内生安全架构的工程化落地。针对星地链路高时延、卫星节点算力与功耗受限等约束，本文构建了“控制—转发分离”的分层验证机制，在控制面实现跨域联邦互信与合规审计，在数据转发面完成安全标识的线速校验。建模结果表明，基于典型LEO星间链路带宽与MTU设定，该架构将SRv6协议封装开销控制在约2.4%，高并发场景下信令带宽消耗低于0.02%，并仅需占用星载FPGA约2.77%的逻辑资源即可实现微秒级线速处理。

![](https://mmbiz.qpic.cn/mmbiz_png/qU881dbu58l3ejpKgK1A79TQR5DB9rJtEM7tF3ywXSMapywMI1HzV48caBzaZtuVMXyicpLRaVQxicpibeyMepWklSsr4HdxAWtoyvEsM9YticU/640?wx_fmt=png&from=appmsg)

EADA通过其分层联邦信任模型，提供了一种以内生机制为核心、面向跨域协作的解决思路。鉴于卫星互联网涉及多方利益主体，基础设施规模庞大，覆盖全网的内生安全体系难以一次性构建。为此提出一条以信任边界逐步外延的分阶段演进路线，通过由域内闭环内生向跨域受控互信的渐进演进，支撑EADA架构的工程化部署。

![](https://mmbiz.qpic.cn/mmbiz_png/qU881dbu58k9fAmZ2PewUkIficI7ku02ViabQXBiaTbzwT17oFsPzicu7jqpOp34Vdic8xInkE8nEkIyLLVqiaq7r7dJTbE6688K2lRMapZoXG2Qw/640?wx_fmt=png&from=appmsg)

阶段一：域内闭环信任。EADA在初期部署于单一运营商控制的自治域，运营商在可控节点引入SRv6控制平面与统一身份体系，实现域内流量的网络层零信任转发与抗毁防御；跨域通信通过VPN实现。此阶段信任边界严格限定于域内，对外部网络仍表现为标准IP自治系统，旨在构建不依赖域外节点的可信内生基座，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qU881dbu58kvetVQ0yh3MibvQOic5JcbX5eTGWcUda7looHx5vY0VzjPmGsibibCk3uNlIaOHes3Bh4w977muWv0OlMGdWHlbjcbjfxaGJicKW4Q/640?wx_fmt=png&from=appmsg)

阶段二：有限信任协作。随着多星座互联需求增加，EADA通过标准化API引入意图驱动的跨域交互机制，实现有限信任协作。外部实体不参与底层协议，而是通过标准化接口提交携带身份凭证的业务意图，不涉及具体网络配置。边缘网关作为信任代理，验证授权后将意图映射为具体的SRv6逻辑隧道。除该隧道外，域内拓扑资源对外部保持不可见，从而在实现业务互通的同时维持网络层的强隔离。

阶段三：跨域联邦信任。信任边界通过策略映射在域间受控扩展，通过对BGP（Border Gateway Protocol）等域间路由协议进行扩展，使携带联邦令牌的SRv6报文可跨域转发，将内生安全能力由单域延伸至多域协同环境。系统在保障各运营商数据主权与策略自治的前提下，实现了跨域业务的受控运行与全网漫游。此阶段的跨域治理遵循“对等意图协商”模式，避免集中式控制引发的主权冲突；同时内置分级降级策略，若高等级SRv6联邦协商失败（如因策略冲突或接口不可达），连接将自动回退至“BGP路由+IPSec VPN”的传统互联模式，优先保障基础业务的全球连通性。具体演进阶段如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qU881dbu58lNILGmlJIlviauuiboEaydKOIuNjPlQynjtAxA61ymUMITRJ16Oic4tGwq1h1Nn94sJMtibvqA14ibIVKdHeBbsCCFXACp5QibtF8TE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nlWISd01LSz3xRanXiaUO0e8n5V70Rd6uU7I4K4szon90cXPE0FqMQZDLpFniasDwgThJCzZqibk97BntFOQrFblA/640?wx_fmt=png&from=appmsg)

实验结果

基于典型LEO星间链路带宽与MTU设定，该架构将SRv6协议封装开销控制在约2.4%，高并发场景下信令带宽消耗低于0.02%，并仅需占用星载FPGA约2.77%的逻辑资源即可实现微秒级线速处理。

在假定有效续签时长 T renew=75s，本文分析了在不同平均中断时长 T outage下，令牌续签的失败概率，结果如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/qU881dbu58kfia3icbnqx85pG4FSkDXLjPokpSHtrIoDUNsMLTTkzwtf6o84fqPNONtiafjfK89TCKmrBJ2nBByGw4Do09pENhaibB8A60Wqrf0/640?wx_fmt=png&from=appmsg)

结果表明，EADA的“重叠窗口”在常规网络抖动下失败概率极低，即便在数十秒级的严重中断条件下仍能保持较高的业务连续性。

针对LEO频繁链路切换导致路由失效问题，本文选取检测时间为30ms作为典型工程参数，旨在验证EADA相比传统协议在收敛时间上数量级的优势。

![](https://mmbiz.qpic.cn/mmbiz_png/qU881dbu58njIr2QP2kib7SPhLw5PZGwiacWG9PDUoVTubpibeL6aV21jQiaEgOkYw6tISW6SKmnrGQQjSL3ic4YlhdQibSJG9jGlrjChRLq4ndng/640?wx_fmt=png&from=appmsg)

如上图，随着星座规模增大，EADA的收敛曲线几乎呈平线，稳定维持在低损耗区间。这一结果定量证明，EADA成功解耦了“网络规模”与“故障恢复速度”的依赖关系，显示出其在超大规模天基网络环境下的可行性与可靠性。

本文出版在《中国科学：信息科学》2026 年第 3 期 “卫星互联网安全专刊” 上。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/r9c6R4tUf9uB7HdX3A7N29rSpIE18nYeDa9Wmic7TdmEgtBje8ZXEWq0yVtDsMUjVODjCgn7Gy5iccMugG2ibS7Cw/0?wx_fmt=png)

盛邦安全WebRAY

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r9c6R4tUf9uB7HdX3A7N29rSpIE18nYeDa9Wmic7TdmEgtBje8ZXEWq0yVtDsMUjVODjCgn7Gy5iccMugG2ibS7Cw/0?wx_fmt=png)

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