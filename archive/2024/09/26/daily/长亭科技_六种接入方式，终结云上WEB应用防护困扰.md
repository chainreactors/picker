---
title: 六种接入方式，终结云上WEB应用防护困扰
url: https://mp.weixin.qq.com/s?__biz=MzIwNDA2NDk5OQ==&mid=2651388284&idx=1&sn=cd3846744db7940e4d5279aee522c4c5&chksm=8d3988f4ba4e01e2e19635eff186c6329597a25956912541171c28388c66f348836dd86c6c6b&scene=58&subscene=0#rd
source: 长亭科技
date: 2024-09-26
fetch_date: 2025-10-06T18:30:11.988336
---

# 六种接入方式，终结云上WEB应用防护困扰

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWEXtmOKrKCZuXzlM0jhBlqz6kbXWXRkUYvicsvWjFFY1m6CNaJMibyh5g/0?wx_fmt=jpeg)

# 六种接入方式，终结云上WEB应用防护困扰

长亭科技

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Fuleibl6qMurm8NzlTYJjan43P3TXrSeMRuR6vwUIvVVG2AYSXu8Uh5Xw3c5iamKBeAq504Amvl2v88TUyibQApbw/640?wx_fmt=gif&from=appmsg)

过去几年国内云计算市场高速发展，可以说未来的软件一定是“生长”于云上的。基础设施变化，是对企业安全体系影响最大的变量，安全和业务速度保持一致，才能应对云上的攻击不确定性、对抗复杂性，提升用户体验。

**PART.0****1**

**“云化”重塑IT体系后的Web防护**

WAF是保障Web应用安全的基础性核心产品，在IDC最新公布的2023年市场份额中，**云WAF整体市场规模已经超过传统硬件WAF市场**，达到21.0亿元人民币，WAF云化的优势进一步凸显。

然而，云上的产品和以前的硬件产品形态截然不同，当面临新旧基础设施的迭代，大部分企业会选择以下几种云环境WAF建设方案，它们各有利弊：

**0****1**

**云外硬件串联**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWCpjMXrRqb5DtNkE6Qh4YVZkNoFE7VMujl8Cka4L59icwibbWGqA8DEDw/640?from=appmsg)

**优势****‍**

* 可直接复用原有云外硬件方案，无需适配
* 无需改变运维习惯

**劣势****‍**

* 流量串联，存在**吞吐瓶颈**
* 传统HA，**无法弹性扩展，高可用不足**

**0****2**

**云内虚机化串联**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWaj1Ztxt3LTEWicBsmpbOXRu4blnNMHicEbD0x4Licnrnt4NM4kv2R6icNQ/640?wx_fmt=png&from=appmsg)

**优势****‍**

* 可直接复用原有云外硬件方案，少量适配
* 无需改变运维习惯

**劣势****‍**

* 无法实现透明接入，只支持**反向代理**
* **代理能力弱，**必须使用”三明治“架构

**0****3**

**云平台自有能力**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWPjzf3TTvnZqTSJu7ZEicnw93svG1aLl4Wd1galpQjqAAjcMokLAKTkw/640?wx_fmt=png&from=appmsg)

**优势****‍**

* 无部署成本，可直接使用
* 和云基础设施打通，运维便捷

**劣势****‍**

* **防护能力相对基础**
* **开放程度有限，自定义能力弱**

**0****4**

**公有云方案**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWEvIsycfW9CL3eLXYdAlG04YJZcOjqTJOJ8GUYvbpvXm4wic2G8aUsPg/640?from=appmsg)

**优势****‍**

* 一站式SaaS解决方案
* 高可用性

**劣势****‍**

* 采购**成本高**
* **售后维护无专人对接**

也就是说，除了公有云运营商提供的WAF服务外，市面上主流的云环境WAF部署方案都是把采集和检测能力打包，整体部署在云内/外，这样必然会存在高可用不足、资源扩缩受限以及容灾问题。

**Q**

**那么，是否存在一种方案，****既能****利用云底座的弹性扩缩容能力，又能完美保留传统WAF的防护效果和自定义能力，还能一举三得地实现****混合环境的统一管理****？**

**A**

答案是有的。**长亭科技雷池（SafeLine）下一代Web应用防火墙**经过全面云化改造，已形成成熟的云环境多形态WEB应用防护接入方案，满足用户“既要又要还要”的多重需求。

**PART.0****2**

**破局关键思路：两个解耦**

**要想让WAF吃透“云属性”，破局的关键是“解耦融云”。**长亭云环境多形态WEB应用防护接入方案中将WAF做了两个重要的解耦。

**一是将软件服务与操作系统解耦。**不仅仅简单地与硬件解耦，而是进一步与操作系统解耦，这样我们可以将服务部署在任意的云主机中；此外，我们继续对WAF服务进行拆分，将管理服务与流量服务解耦，实现分布式集群能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWxqKk5wFpvEunSF9Ot2Td9lSeryhyk2Q0JGDKF71T6egBMZt2E2ic8lw/640?from=appmsg)

**二是将流量转发服务和流量检测服务解耦。**解耦后，用户现有网络环境中的负载均衡/流量中间件/服务器代码可以承担流量采集的工作，采集完成后转发给WAF的检测接口，对这些流量进行检测并返回给对方结果，这个标准接口即雷池（SafeLine）的T1K接口。在这一过程中由于直接复用了现有链路中的流量转发组件，WAF是不可见的，可以被认为是“软件透明”。**这个解耦一方面使得原有网络环境中的高可用和故障Bypass机制仍可自动沿用，另一方面便于“无损化”地实现检测、转发、分析节点的水平扩展。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWobCpj0ricSfRBSqDicQLrGheUhiaOF8a05h1iaQHIY7dm9gx2zuiax5wUPw/640?from=appmsg)

“利用Nginx的动态模块实现引流”的版本便是雷池（SafeLine）此种思路实现的经典例子，具体内容可以参阅此篇推文。

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWOIYjtGNxx4Mzl8sEscNBpejiazXaZYHkoyuBQbPugPmClxcY4PMicqhQ/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MzIwNDA2NDk5OQ==&mid=2651387420&idx=1&sn=9bd8bae5d1cd450e26f87742cc32d310&chksm=8d398794ba4e0e82c8d662379959c207ec637191a6c8ac745efa2b07e5655a0608d05781702b&scene=21#wechat_redirect)

点击上图阅读详情

**PART.0****3**

**云环境多形态WEB应用防护方案**

按照这种“解耦引流”的思路，长亭科技根据不同客户的网络结构特点及业务需求，构建了五种流量转发与检测解耦的实现方案，和一种转发与检测一体化的优化方案，让每个客户都能少改动、低成本地应用最适合自身网络环境的方案。

**01**

**动态模块引流**

**特性** **‍**

* 以Nginx为代表，**可复用现有Nginx集群**
* Nginx中加载so动态模块
* 支持Nginx衍生的tengine、openresty、kong、apisix 等网关

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWeKwG1FBE8iajczsIG1MU6DHy5GbzjAtlVSLRFFHStbp3ZiaMy58ia6Exw/640?from=appmsg)

**02**

**网关SDK的引流**

****特性****‍****

* **可嵌入自研网关中实现流量检测**
* 多语言支持
* 不改变网络拓扑，无感接入
* 自主可控，拥有业务级细粒度bypass机制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWibT3v7yKNBevB1huTXhbHhiblP5TaCvbU7Ic5KsNbrk2QhuJp0QdOgjQ/640?from=appmsg)

**0****3**

**服务端SDK引流**

****特性****‍****

* **可嵌入业务端代码，实现业务加密流量检测**
* 多种对接语言，可嵌入任何业务
* 可自由编排检测/拦截逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWoQTViaGNKumOaBEjTqYtooMvQddelpzfI7azdJ2FiasVOI3majKVDATg/640?from=appmsg)

**04**

**K8S引流**

****特性****‍****

* **可与Ingress、istio等K8S云原生组件联动进行流量检测**
* 可在k8s内部署，自动扩缩容和服务降级
* 可在k8s外部署，复用软件检测集群

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWdgib1uoSPjCzgsW3UM0ibeicF1VjkKQfn0tYlmiaSibRIrFvfxticvphjk6w/640?from=appmsg)

**05**

**mPaaS引流**

****特性****‍****

* **可与MGS网关联动进行流量检测**
* MGS原生支持，无需额外适配
* 不改变网络拓扑，不成为单点故障点
* 解决移动app加密数据检测的问题

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWNQ3Tz1skXalVeaPrU27bgecodzMKZbicYbswP6fmWdtgqqMZ0MfphFQ/640?from=appmsg)

**06**

**集群反向代理**

****特性****‍****

* 提供基于tengine的LB+WAF一体化能力
* 分布式部署+集中管理
* 检测服务可水平扩展
* 支持对后端业务负载均衡(自带Tengine集群)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWI5jlkAicCWeHBZZOOc0HysQEgnDoCfLOOfDFYGsb04FEYMNDuR5iaqDg/640?from=appmsg)

得益于雷池（SafeLine）接口设计的标准化和开放性，**长亭与很多云基础架构达成了生态合作，包括获得**Nginx**认证安全模块、APISIX社区默认集成插件、BFE的商业合作等。**多样的生态使得方案能更广泛快速地兼容客户的多样环境，让云下全线防护能力得以平滑迁移至云上，实现检测能力的弹性扩缩容和统一管理，真正做到“功能不受损，服务不降级”的全场景守护。

如需获取完整方案内容及落地案例，请扫描 **下方二维码** 申请。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Fuleibl6qMuribYo7qH765RrVYbAmzH7SWFibRAttfKSRffowzQoibTQ1XtGKdStgHdPSiaKtdH2Iv5sTuPeQgtOCgg/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Fuleibl6qMuqy3z1PNoOSxgQbUqYibAcIb722vbFGdP1gfxibthFf1IibTtFxgfSv90xVj6dPhV9oRc39O4VGUbYQw/0?wx_fmt=png)

长亭科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Fuleibl6qMuqy3z1PNoOSxgQbUqYibAcIb722vbFGdP1gfxibthFf1IibTtFxgfSv90xVj6dPhV9oRc39O4VGUbYQw/0?wx_fmt=png)

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