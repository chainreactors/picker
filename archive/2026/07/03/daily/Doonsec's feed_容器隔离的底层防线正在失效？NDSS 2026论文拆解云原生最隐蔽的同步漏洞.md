---
title: 容器隔离的底层防线正在失效？NDSS 2026论文拆解云原生最隐蔽的同步漏洞
url: https://mp.weixin.qq.com/s/eQNzdFwf_TAahjeCWBzbfQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:45:46.691968
---

# 容器隔离的底层防线正在失效？NDSS 2026论文拆解云原生最隐蔽的同步漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FNlvhjUaDTM2ku5bib7c7H8xkvHjhNcwQMm8cDw4nnQoBM9DqA9EklKN3PDdRtWJqfNg4PVmY80icBU7NYhgAEqwZwrzBdRxHP837Cx6VUeYI/0?wx_fmt=jpeg)

# 容器隔离的底层防线正在失效？NDSS 2026论文拆解云原生最隐蔽的同步漏洞

原创

赵玉宇; 徐誉坤
赵玉宇; 徐誉坤

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**引  子**

云原生时代，容器早已成为微服务、Serverless计算的基础设施，而Linux namespace与cgroup的协同工作，一直被视作容器隔离不可撼动的两大基石。但行业内长期以来的安全攻防，大多聚焦于单一机制的隔离缺陷或管控漏洞，却忽略了一个致命问题：当namespace共享成为云原生场景的刚需，两大核心机制的协同已经彻底脱节。NDSS 2026顶会上的这篇论文，首次系统性揭露了namespace-cgroup不同步（NCD）这一全行业级风险，不仅让Docker、Kubernetes等所有主流容器工具全线失守，更挖出4个高危CVE漏洞，彻底刷新了我们对容器隔离底层逻辑的认知。

**论文速览**

过去数十年，容器隔离的核心逻辑，始终建立在namespace与cgroup的生命周期同步之上：namespace负责虚拟资源的隔离管理，cgroup负责对应系统资源的用量限制与记账，容器销毁时二者同步释放，实现资源全生命周期管控。

但随着微服务、Serverless架构的普及，namespace共享成为降低通信延迟、简化部署配置的核心方案，却直接打破了这一同步机制。论文作者团队首次发现，共享场景下namespace的生命周期会远超容器实例本身，容器销毁后其cgroup被同步删除，但共享namespace仍被其他容器/主机持有，其中的资源彻底脱离管控，形成无限制的残留资源，这就是NCD风险的核心成因。

基于攻击模型，团队自研检测工具，对Docker、Kubernetes、Podman、Pouch等所有主流容器工具进行了系统性检测。

检测结果证实，所有主流容器工具均暴露在NCD风险之下，其中IPC、网络、PID namespace的共享场景均存在可被利用的高危风险，团队累计发现并上报了4个高危CVE漏洞和1个系统bug，相关漏洞已得到各开源社区的确认。

针对这一用户态难以根治的底层风险，团队创新性提出内核级防御方案CANs（Cgroup Associating with Namespaces），通过虚拟资源与cgroup的标签绑定、balloon cgroup残留资源接管机制，从根源上打通namespace与cgroup的协同链路，彻底消除NCD风险。实测数据显示，该方案对Linux内核基准测试的平均性能开销仅0.47%，对主流容器工具的最大开销不超过2.4%，对真实业务应用的平均开销仅3.6%，且完全兼容现有容器生态与Linux内核原生接口。

**深度解剖**

这篇论文的核心价值，在于它颠覆了容器安全领域延续多年的研究范式，实现了三个层面的关键突破。

首先，它打破了行业对容器隔离的核心共识。此前业界的安全研究，始终围绕“namespace隔离不足”或“cgroup管控不严”两大单点方向展开，却从未关注两大基石机制的协同失效问题。论文首次证明，即便namespace和cgroup本身的功能完全正常，二者的生命周期不同步，依然会造成彻底的管控失效，且这种风险比单点漏洞更隐蔽、影响范围更广。过往针对cgroup记账漏洞、namespace隔离缺陷的修复方案，对NCD风险完全无效，这一发现直接开辟了容器安全研究的全新方向。

其次，它揭露了全行业级的安全隐患，引爆了产业界的争议。团队通过GitHub API扫描发现，超15.64%的容器化项目都启用了namespace共享配置，其中深度学习、高性能计算、负载均衡等核心场景，更是高度依赖IPC、网络namespace共享，而Kubernetes Pod默认就共享多个namespace，意味着这一风险覆盖了绝大多数云原生生产环境。更值得关注的是，漏洞披露后，Docker社区将修复责任推给编排平台，Red Hat则认定这是Linux内核的原生缺陷，各方的推诿恰恰印证了NCD风险在用户态几乎无解的行业困境。

最后，它提出的CANs方案，实现了容器隔离技术的实用化突破。此前用户态的“监管cgroup”方案，仅能应对容器间namespace共享场景，完全无法适配容器与主机共享namespace的私有部署环境，而CANs首次在内核层打通了namespace虚拟资源与cgroup系统资源的映射关系，既实现了资源全生命周期的管控闭环，又保证了极致的性能与兼容性，为全行业提供了可落地的通用解决方案。

**局限与展望**

值得注意的是，论文提出的CANs方案仍存在一定的优化空间。当前方案仅完成了Linux kernel v6.2.7版本x86架构的实现，对ARM等主流异构架构的适配尚未完成，在边缘计算等异构场景的兼容性有待验证；同时，方案的资源管控主要聚焦于内存、PID等容量型资源，对CPU、blkio等时间型资源的NCD风险覆盖尚不充分。

未来，该方向有两个值得深入探索的路径：一是推进CANs方案进入Linux内核主线，完成全架构、全内核版本的适配，实现行业级的原生支持；二是扩展NCD风险的研究边界，覆盖更多类型的namespace与资源控制器，同时优化balloon cgroup的动态调度策略，更好地适配云原生弹性扩缩容、滚动更新等复杂生产场景。

**启  示**

这篇顶会论文，给国内云原生学术界与产业界带来了两个至关重要的启示。

第一，云原生安全的攻防博弈，已经从单点漏洞的修补，走向了底层系统设计逻辑的对抗。我们不能再局限于“打补丁”式的漏洞修复，更要回归基础设施的设计本源，重新审视核心组件之间的协同逻辑，从根源上规避系统性风险。

第二，在容器安全这一国际前沿赛道，国内顶尖团队的研究已经具备了与国际顶级水平同场竞技的能力。从高危漏洞的原创性发现，到底层根因的深度拆解，再到可落地的内核级解决方案，形成了完整的研究闭环，这也为国内云原生安全领域的创新提供了绝佳的范本。

云原生的安全防线，从来都不是单一组件的坚不可摧，而是整个体系的同频共振。

![](https://mmbiz.qpic.cn/mmbiz_gif/FNlvhjUaDTO2WS34jCfQjnvq2znoON10t1LA4BgLU87ZeTg914xU6ia7ektvhfZsggp9UCEpOJ9Sd3XOgkicOic5mHBPw4XraTAnSxsSOVQ0gQ/640?wx_fmt=gif&from=appmsg)

**本文仅代表作者个人观点**

**本期点评论文**

**作者：**

赵玉宇（东南大学网络空间安全学院，讲师，网络测量、网络处理器架构、交换机内生安全与物联网安全领域）

徐誉坤（东南大学网络空间安全学院，云原生安全领域）

**原文题目：**

Losing the Beat: Understanding and Mitigating Desynchronization Risks in Container Isolation

**原文作者：**Zhi Li (Huazhong University of Science and Technology), Zhen Xu (Huazhong University of Science and Technology), Weijie Liu (Nankai University), et al.

**期刊/会议：**NDSS 2026

DOI：**https://doi.org/10.14722/ndss.2026.231381**

版权与来源声明：本文依据《中华人民共和国著作权法》第二十四条之规定，为介绍、评论之目的，在此适当引用。原文版权归原作者所有。

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=other)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=other)

我们在不断努力和完善中，期待您的关注和支持！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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