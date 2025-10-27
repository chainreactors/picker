---
title: SANS 2024年SOC调查报告解读
url: https://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484811&idx=1&sn=18c651844e9668dd2ffa2f32db674f8c&chksm=fa002f3fcd77a629422d4e14a5a8084ffaa96300e13f67478937cd4de24717bbbbd88b68c42b&scene=58&subscene=0#rd
source: 专注安管平台
date: 2024-09-06
fetch_date: 2025-10-06T18:27:31.374949
---

# SANS 2024年SOC调查报告解读

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t7v7zyOTkMeg6iaDvFYgkZBZACQicI6mP4shbKN4rqA6seZSpNjxbhlhHLs1mTEAia93RQ5ed9Q9QpuAwicjiaZiaMJA/0?wx_fmt=jpeg)

# SANS 2024年SOC调查报告解读

原创

Benny Ye

专注安管平台

*【引言】本文不是报告的译文，是作者对报告的个人理解和解读，以及基于作者自身实践的思考。*

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMeg6iaDvFYgkZBZACQicI6mP4hj6nNYmM3V1iaObImhgbibJAKVwEb82sKzrjIN5gkQ4pjBIicgr2qxdnA/640?wx_fmt=png&from=appmsg)

2024年7月，SANS发布了2024年的《SOC调查报告》，副标题是“安全运营中面临的主要挑战”，凸显了这份报告关注的重点。报告保持了国际化的视野，访谈了全球范围内的各种类型各种行业的组织。注意，这份报告中，位于美国的受访者占大多数（403位受访者中占301位），也表明我们在阅读这份报告的时候，要结合国内的实际情况来看待，切勿简单地将观点照搬过来。同时，为了便于与笔者之前写的《2023年SOC调查报告解读》形成对比，本文采用与之相同的提纲顺序。

**SANS的关键发现**

1）在151份有效回答中，表示“不知道自己的SOC预算”的人占比最高（38%+），远高于2023年的回答比例（22%），说明组织的预算过程跟SOC团队之间出现了脱节，SOC运作机制可能存在问题。

2）67%的受访者表示他们向上面管理层汇报工作时采用了度量指标，与去年基本持平。根据笔者自己的分析，在国内这方面还比较落后，也是未来国内SOC可以发力的方向。

3）SOC团队规模（含驻场外包）主要分布在2-10人区间。国内的情况与之也基本一致。

4）SOC当前面临最大障碍是编排与自动化，其次是人手不足和人员技能不足，都跟人有关。

5）触发SOC团队启动响应的首要告警是EDR/XDR类，其次是SIEM告警。

**SOC格局**

1）基于云的SOC架构占据主流，这与Gartner多年前的判断一致。但在国内，主流架构还是还是传统的，有些号称上云的SOC不过是云上虚拟化部署，距离云原生架构还很远。当然，云原生SOC的需求也不足。

2）单一的集中式SOC部署模式继续保持多数比例。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcM5LG1V2s4mNVaY21icOeWSlAibHPpdsHr5eVWoKxX1YN4Lpe0xjV7kSU370rticxRN8ibXwPfB4tibMQ/640?wx_fmt=png&from=appmsg)

3）把所有数据都给SIEM成为一种习惯。SANS分析师表示，尽管这个发现有悖SOC实践常理，但相较于花费时间去甄别到底需要什么数据，一股脑儿先扔给SIEM更省事儿。不过，笔者看来，这种习惯显然不可取，不仅是给后续的分析处理增大了难度，传统SIEM的数据存储和维护成本也将不堪重负。这显然是一种“先甜后苦”的做法。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcM5LG1V2s4mNVaY21icOeWSsOhA9t1zW16EPxrAbypSPL24TpX3Q17nhVHBhicKSRbQg1tXkZ7qvbg/640?wx_fmt=png&from=appmsg)

不过，反过来思考，这也印证了客户渴望“简单的安全运营”的诉求。

**SOC面临的最大挑战**

下图展示了这次调研中SOC面临的最大挑战排序，首先是**缺乏自动化与编排**，接下来第二和第三位都是人的缺乏，第四是缺少企业级的可见性，“缺少与我们所观测对象相关的上下文（情境）信息”位次大幅下降，该挑战在2023年的调研中位居第一。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcM5LG1V2s4mNVaY21icOeWSTX6JNLyLic7de1KFwDouLM4g2XbGhyz2ibPsianl1V0saVHgMpTiaCAibFg/640?wx_fmt=png&from=appmsg)

下图是2023年调研的结果：

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMd5zUUZGKTAHppIBjJYOTVVibOWbXb5HQR3e8IXHqBIy9fIicLeLYicA94xgEWQ9LypUQDiaZc7QNJLwA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**SOC人员调研**

1）SOC团队规模（含驻场外包）主要分布在2-10人区间。

2）人员在职年限较上年调研结果有所增加，表现在1-3年比例下降，3-5年比例上升。

3）SOC技能要求方面，最重要的三个分别是：使用SIEM做分析、使用EDR/XDR、漏洞修复。

4）保留员工最有效的方法主要包括“有意义的工作”、“钱”和“职业前途”三个，相较于去年排序有所变化。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcM5LG1V2s4mNVaY21icOeWSnfhu8AyCiatVIyjHAEKfknJg0YFTONutmEG7nQibMyl8lgIDcgtdKtdg/640?wx_fmt=png&from=appmsg)

5）今年新增了一个调研问题，是关于如何计算每个分析师的工作量的，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcM5LG1V2s4mNVaY21icOeWSIh0UnQ2dxR6lP7gib1J9c2fZAVav6Xic8Dib0g7dwWbsFFhqYeb1kxPQA/640?wx_fmt=png&from=appmsg)

可以发现，最主流的一种工作量计算方式是依据工单处理时长，其次是追加考虑SIEM产生的告警数量，再者还要根据SLA进行更细致的计算。

**SOC能力（流程）分析**

如下图所示，本次调研发现最重要的SOC能力【笔者注：这种能力外化表现为流程】排序为：告警（分诊和升级）、安全监测与检测、事件响应、系统安全管理、安全架构与工程，等等，与2023年的结果差异较大，但唯一没有改变的就是告警处置能力排名第一。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcM5LG1V2s4mNVaY21icOeWS2Klqy6Jy2fvp8IYlczZ1hibjvCTbekqpYhGfYqE6dkibtkORJKIXsj9A/640?wx_fmt=png&from=appmsg)

**威胁猎捕**

SANS认为威胁猎捕的基本目标是寻找告警系统未能检测到的失陷。威胁猎捕是一个在假定其它基于告警机制失效情况下的对现有数据进行调查的过程。威胁猎捕最简单最基本的形式是将新发现的指标（譬如来自安全情报的）用于历史数据的回溯查询分析。

如下图所示，SANS调查显示，威胁猎捕活动的自动化程度正在不断提升，厂商提供的自动化威胁猎捕工具越来越强大。同时，纯手工方式的威胁猎捕活动依然占比较高。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcM5LG1V2s4mNVaY21icOeWS4GZ6I5aUISibTvqTaicrYhvXlicVCichIRAq0RtSSQeb8mA3VPgEibyRcww/640?wx_fmt=png&from=appmsg)

笔者这里需要指出的是，上述猎捕过程中的查询分析不是一次性的，而是要迭代进行的，是一系列查询和调查，期间需要人的直觉和智慧的参与，最终抽丝剥茧，识别出威胁事件，并触发事件响应处置流程。如果无需人的参与就能识别出的威胁，属于检测，而非猎捕。因此，完全自动化的威胁猎捕是不存在的，我们只能将威胁猎捕的部分过程自动化。所以，笔者认为SANS报告中所指的完全自动化是指某个活动片段，而非全过程。

**威胁情报**

SANS本次调研了用户如何使用威胁情报。结果显示，最多人选择（将威胁情报用于）“事件响应”，紧跟其后的是（将威胁情报用于）“威胁猎捕”。

**SOC技术**

今年SANS分析了47种SOC技术的客户满意度，比去年多一种技术——GPT。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMcM5LG1V2s4mNVaY21icOeWSSiadwoMxX3gvBkVe1vSAUz0u29ZhLia6BQr04fOMtAiayUJwnCwvH49Aw/640?wx_fmt=png&from=appmsg)

结果表明，满意度最高的是EDR/XDR，并且超过了3分，达到了A级。接下来依次是VPN、邮件网关、SIEM、NGFW、MPS（恶意代码保护系统）、定制化或裁剪的SIEM监测用例分析，等等。相较于去年，对日志分析的满意度有所下降。

反过来，看看最不满意的有哪些，包括：GPT、AI和ML、欺骗技术，等等。对比一下可以发现，从2023年到2024年，计划实施AI和ML的SOC项目比例呈现下降趋势。报告作者认为，GPT可以极大地促进沟通和分析师对信息的理解，但还无法取代分析师。

此外，TIP和SOAR技术的满意度评分比去年有所下降，其中，SOAR满意度倒数第九。

**SOAR**

针对SOAR，笔者这里稍微展开一下。

首先，SANS报告显示SOC最大挑战是缺乏自动化与编排；其次，SOC团队对SOAR的满意度偏低。说明什么？说明SOAR对于SOC十分重要，当前需求旺盛，但现有的产品和能力无法完全满足客户需求，期望与现实之间存在较大的鸿沟。这也正如SANS召开的针对这份报告的线上研讨会上，来自DropZone.AI的创始人Edward Wu所说，现在的SOAR技术存在问题。

同时，也正如Gartner和Forrester分析师在报告中指出的，当前主流的SOAR的实施和维护成本过高，对于用户的技能水平要求较高，需要有较高的流程成熟度和代码开发水平，最终导致SOAR的投入产出比低于预期。当前SOAR正处于Gartner定义的技术谷底，同时Gartner还表示SOAR已经融入了SIEM等其它产品中成为一个功能，而不再作为独立产品和市场。

以上种种叠加到一起，说明SOAR革新的时候到了。自动化和编排本身没有问题，有旺盛需求，但是SOAR技术需要变革，需要更加简单易用，更加智能，易于实施和扩展。

为此，DropZone.AI等公司提出了用GenAI去改造SOAR，但又面临另一个问题，即SOC团队对GPT等AI技术的满意度水平更低。如何在SOAR中应用好GPT和AI还需要仔细斟酌。同时，有的公司从低代码/无代码开发的角度去降低剧本的开发门槛，或者内置更多开箱即用的剧本，等等。还有的公司也在思考对剧本进行分层，让剧本更易于组装。如此种种，都是为了降低SOAR的使用门槛。对于SOAR技术的未来，笔者充满信心，而不论其是继续作为独立产品，抑或成为一个能力（功能），如UEBA那般。

**事件响应**

调查显示，最满意的技术是基于端点的响应能力，而最大挑战（最不满意）来自于对抗性欺骗技术。

**SOC度量指标**

定义度量指标已经成为大部分SOC的共识，不仅可用于衡量外包工作成效，更是为了SOC团队向上汇报工作成效之用。下图展示了一些常用的内部度量指标：

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMeg6iaDvFYgkZBZACQicI6mP4qJUffeKvic74NdkY3dEGib39RFw4KzWEmYH53WFGypxke8msokXzJ6Tg/640?wx_fmt=png&from=appmsg)

可以看到，“处理的事件量”是最常用的指标，其次是MTTD/MTTC/MTTE、彻底根除率、发现所有受影响的资产和用户的时长、应知事件与未知漏洞的比率、可避免事件数量、依据IOC全面检查信息系统的彻底性和准确性、威胁行为体溯源数量、安全事件导致的业务停机时长或怠工时长、一个班次关闭的事件量、数据丢失发生数量与阻止数量的比率、事件造成的经济损金额。

**小结**

透过这份报告，可以发现：

从技术发展路线上看，国际（尤指美国）趋势是云化SOC，同时，SIEM依然是SOC的核心部件，但EDR/XDR的地位凸显，成为重要的告警来源，并且满意度最高。而SOC迫切需要发展的技术和能力在于SOAR所代表的自动化和编排，但SOAR当前技术水平未能达到预期。威胁猎捕在SOC中越来越普遍，也越来越成熟。SOC对AI和ML（包括GPT）也产生了兴趣，但真正上马智能SOC的还是少数，大部分都在观望。

从运营成熟度上看，国际上的现状是：自营+外包已经成为SOC运营的主流选择，主流SOC团队的大小也稳定在2-10的区间，解决人手短缺的问题主要还要靠自动化技术。此外，大部分SOC组织都制定了度量指标，在面向管理层和董事会的汇报中都会用数字说话，以证明SOC取得的实效，从而获得管理层对SOC的进一步投资。值得注意的是，出于对数据复杂性的畏惧，大部分客户选择先将所有数据一股脑儿扔给SIEM处理，笔者认为这是一个隐患。解决之道恐怕不能从用户侧去考虑，而更多要从技术架构上加以考量。

反观国内，根据笔者的观察，受限于客户实际环境，云化SOC也就刚刚起步，而SOAR（尤其是独立SOAR）在国内的发展空间显然更大，GenAI应用于安全运营更多还是概念验证阶段，MSS服务（尤其是MDR）还任重道远。

【参考】

[SANS 2023年SOC调查报告解读](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484680&idx=1&sn=83d86c286a3072137d14a936cf86f098&chksm=fa002fbccd77a6aae4a84f82541ec6d7be90d5965913afe784cd481a41ac708ea9cf95ebf455&scene=21#wechat_redirect)

[SANS 2022年SOC调查报告解读](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484450&idx=1&sn=27c3c6e51febebd4ed1a13fa2f85307d&chksm=fa002e96cd77a780251bdec3b12e2fbea2e013d19495d01c33b7aaac9323cbabe4274077e999&scene=21#wechat_redirect)

[SANS 2021年SOC调查报告解读](http://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484366&idx=1&sn=ba64aedd9b67d98fa619db281105cf65&chksm=fa00297acd77a06c53139348d4b69c713712c8ee8054871436ab9ff1a386f65983e4144134d8&scene=21#wechat_redirect)

预览时标签不可点

个人观点，仅供参考

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMepicSn33np52HRygZK2DSdFuVV6ibZQQESNfWcyP8lrVECk9GEVloZQdj7FJbib6tvyt5nh36XxJeicA/0?wx_fmt=png)

专注安管平台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMepicSn33np52HRygZK2DSdFuVV6ibZQQESNfWcyP8lrVECk9GEVloZQdj7FJbib6tvyt5nh36XxJeicA/0?wx_fmt=png)

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