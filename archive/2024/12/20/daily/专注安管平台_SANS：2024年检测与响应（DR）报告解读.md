---
title: SANS：2024年检测与响应（DR）报告解读
url: https://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484836&idx=1&sn=05ff688d9865a0d5bc38815a37d63725&chksm=fa002f10cd77a606c3068f8f9b0171da25f86c26a866afdc2bcd1fb5cc70ec2fc900474c2017&scene=58&subscene=0#rd
source: 专注安管平台
date: 2024-12-20
fetch_date: 2025-10-06T19:39:10.990076
---

# SANS：2024年检测与响应（DR）报告解读

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t7v7zyOTkMfu5UFByDSCYOoOFKgGqyp9kibibTPWIVuCwLgJ3TicEicSTmpQPePnfqa5gMe2Pet4WRIMC7tXb8BMIQ/0?wx_fmt=jpeg)

# SANS：2024年检测与响应（DR）报告解读

原创

Benny Ye

专注安管平台

2024年11月，SANS发表了针对检测与响应（DR）的首份调研报告。正如这份报告的副标题——安全运营转型中：检测与响应的智能化、自动化和集成化——所言，SANS认为检测与响应（DR）的未来发展方向的核心就聚焦在智能化（AI）、自动化和集成化三个方面。注意，这里的AI不仅包括以大模型（LLM）为代表的GenAI，而是指完整的人工智能（AI）和机器学习（ML）技术。

报告的主要发现包括：

* 大部分组织 （64%） 正在将自动响应机制集成到其安全运营中。
* 只有 16% 的受访者表示他们的响应流程已完全自动化。
* 59% 的受访者认为，对熟练人员的需求是实施的最大障碍。
* 47% 的受访者表示，预算限制是首要问题。
* 约三分之二的受访者 （67%） 表示，他们计划扩大人工智能 （AI） 和机器学习（ML）在威胁检测和响应方面的使用。

威胁检测

1）自动化检测工具大量使用，手动监测工作依然大量存在。87%的受访者使用了自动化辅助工具去检测威胁，但同时有66%的受访者表示他们还在开展人工的监测工作。此外，38.9%的受访者表示他们使用了AI和ML技术去检测威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfBRLUUIFWwdBZMZve7EibYgxhy0gqmQhlnHrcEUicereSZAJGbkicnrHSDglpLXRicNoPicAYGToqZjQQ/640?wx_fmt=png&from=appmsg)

2）EDR/XDR被认为是最有效的检测工具，威胁猎捕次之，认为AI/ML无效的比率最高。42%的受访者认为EDR/XDR十分有效，这与界内的EDR发展趋势相符，即威胁检测最关键的环节是端点【笔者注：譬如美国联邦政府在吃了几次亏以后强制要求部署EDR】。而XDR作为EDR的扩展，进一步增强了检测的效果。有意思的是，威胁猎捕团队以29.8%的十分有效率位居EDR/XDR之后，超过了SIEM。笔者认为，这至少表明，以人为主的威胁猎捕工作证明了人在威胁检测中的独特价值，也间接表明在自动化和AI大行其道的未来，人的工作依然占有一席之地。此外，AI/ML工具还需要进一步深化和演进。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfBRLUUIFWwdBZMZve7EibYg0mgmfCtvVXbHxvS7dgTEsk3LX3oHxOiarQic1rSrTpIdfT6cspMLxECg/640?wx_fmt=png&from=appmsg)

3）针对AI和ML应用于检测的进一步调研中，超过一半（51.2%）的人表示用到了AI和ML，但应用程度还不够深入。调查显示，只有25.3%的人表示在检测过程中深入使用了AI和ML能力。近22%的人表示仅仅使用了AI和ML的最小（基本）能力。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfBRLUUIFWwdBZMZve7EibYgxTjZCkCtDjthgz27kibHj8gU45tJZh7K0fMDU4F2Uj8v27Zvm5swvjw/640?wx_fmt=png&from=appmsg)

【笔者注】在2024年9月，SANS单独发布了一份《AI调研报告》，专门对AI在网络安全中扮演的角色进行了分析。在那个报告中，SANS表示，AI在网络安全的应用领域基本都聚焦在了安全运营上。进一步分析，主要就应用在检测与响应（譬如排在前四位的异常检测、恶意代码检测、自动化事件响应、告警富化）。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfu5UFByDSCYOoOFKgGqyp9FZGHcUpia1JfGLoWWFcTqjE4aQaHCLIryibbkS0v9kVIzFRibYglt9JYg/640?wx_fmt=png&from=appmsg)

报告同时显示，AI在安全运营领域最大的价值在于改进了威胁检测，其次是事件响应。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfu5UFByDSCYOoOFKgGqyp9CQgJKzaSQsdicl9icuRw186Vbt05wrBeXBOlg4N8KSNOhHexXnT8iatGA/640?wx_fmt=png&from=appmsg)

另一方面，这份《AI调研报告》也提及了AI在检测与响应领域应用时存在缺陷。主要的缺陷包括：AI检测也会产生误报、严重依赖受训练数据、检测新型威胁效果不佳（主要还是受训数据的问题）。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfu5UFByDSCYOoOFKgGqyp9Ey6rN9RGqOL4fC8xfibYShMUCYTYbCtLmyomfMZYYymfPEL7T9rJCiaQ/640?wx_fmt=png&from=appmsg)

最后，这份报告还给出了AI应用于网络安全领域的6大误区，其中第一大误区就是以为AI将完全取代人类。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfu5UFByDSCYOoOFKgGqyp9YjfwzK6a1cgxNwAia7fKAURaSK0kurxgGEjZI9XovhIJD50ZGpSt3jA/640?wx_fmt=png&from=appmsg)

正如笔者在《[从RSAC2024看SOC发展趋势](https://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484766&idx=1&sn=5b66715c108908d39eb92ecdc964c9f6&scene=21#wechat_redirect)》和《[从Gartner2024年北美安全峰会看安全运营的技术趋势](https://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484795&idx=1&sn=8f835c0699be66f615e7b713f67e26dc&scene=21#wechat_redirect)》中写到的那样，AI（包括GenAI）的价值（至少从中期来看）在于赋能人类、增强人类，而非取代人类。

4）调研显示，展望未来，人们普遍对AI和ML增强威胁检测寄予厚望。67%的受访者表示要增强这方面的应用，人们越发认识到AI和ML在增强安全自动化和提升威胁检测准确性方面的潜力，25%受访者表示不确定，处于观望状态，而只有8%的受访者表示不计划对AI和ML的采用。

5）展望未来，除了AI和ML，其它拟应用的先进技术还包括：行为分析（83%）、（部分）自动化威胁猎捕（64%）、预测分析（60%）、高级关联引擎（56%）。

6）针对云中的威胁（主要是针对IaaS、SaaS和FaaS的）检测，认为最有效的还是云原生工具，第三方工具次之，自研工具排第三。

7）检测内容（规则）的主要来源依次是：威胁情报平台（65%）、内部团队自行开发（62%）、安全供应商（59%）、政府主管机构（57%），以及开源社区（46%）。而在获取这些检测内容时面临的挑战方面，首要的是内容（规则）的质量和可靠性（73%），其次是兼容性（55%）、信息过载（54%）、缺乏检测相关的上下文（50%）。相反，在对外分享自己的检测内容（规则）时，只有39%的受访者表示做到了。同时，他们分享的动机主要（68%）是为了更好地获得对方的检测内容。

事件响应

1）大部分（67.8%）组织的事件响应过程都是半（部分）自动化的，但也有不小（22.7%）的组织依然采用手工过程。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfBRLUUIFWwdBZMZve7EibYgZPEfiapp9t0gTMjdqQKHicF70QUSoePj8DwBsAJf2L8sMTakEmWVSZJw/640?wx_fmt=png&from=appmsg)

2）最基本的响应工具是EDR（81.8%），其次是SOAR（60.5%）。此外，依然还有50.4%的组织还在采用手工方式连接系统、手动运行各种指令。此外，对于NDR的响应能力，具有其独特的功效，可以与EDR互补使用。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfBRLUUIFWwdBZMZve7EibYgtqdTTvCZSuvEUEH2iamhAyWs1UN9saQSenP8FmricmZxSYEPS7DTl5RQ/640?wx_fmt=png&from=appmsg)

3）对已确认威胁的响应时长主要（41.4%）集中在分钟级，其次（32.6%）在小时级。总体上，83%的受访组织事件响应时长在秒级到小时级之间。SANS对这个结果表示满意。笔者认为，可以看出，要想进一步缩短响应的时长，自动化是必然的路径，而智能化则是对自动化的再加速。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfBRLUUIFWwdBZMZve7EibYgIETqhRViciazx2icPdqcyR7DpHXYXGc8yPhVHibahlptzZRxTBaYYCqiclQ/640?wx_fmt=png&from=appmsg)

4）64%的受访者表示他们的安全运营部分集成了自动化响应工具/系统，16%的受访者则表示他们完全实现了这类集成，但还有15%的受访者表示没有任何这方面的集成。

5）自动化的检测到响应工作流程的最常用策略是预定义的剧本【笔者注：非特指机读剧本）】— 74% 的受访者使用它们来标准化和简化响应操作。64%的受访者采用自定义的集成和自动化脚本，62%的受访者采用SOAR工具，还有35%的受访者表示采用了AI技术。

6）在自动化的检测到响应工作流程领域，对于未来的首要事项，68%的受访者表示将加强剧本，65%计划提升SOAR工具的集成，52%计划定制自动化脚本。此外，还有38%的受访者表示计划采购新的开箱即用的集成化解决方案（譬如XDR）。

7）在威胁响应优先级方面，首要（41%）考虑的因素是威胁的严重性级别，其次（29%）是对业务的影响程度，第三是受影响的资产类型。

检测与响应团队架构

调查显示，将检测与响应职能放到一个团队的比例和将检测与响应职能拆分到两个不同团队的比例相当（都是48%），并且有48%的受访者对当前组织结构设置表示十分满意或满意。这表明，对于检测与响应团队的设置方式没有绝对的好与坏，各有利弊，主要还是要结合组织自己的实际。

对于未来，近50%的受访者倾向于采用混合式的团队结构，即综合整合式单一型团队团队和专业化分工型团队两种形态。而希望建立分工型团队的受访者比例略高于希望建立整合型团队的受访者。

笔者发现，放眼国内，当前主流的威胁检测与响应团队大都采用分工型组织，在工作职责上大都分为监测组、研判组、处置组，或者类似地划分出一线运营人员和二线运营人员，通过专业化、层次化的分工和操作规程串联起完整的威胁检测与响应过程。这种方式是否就是最佳？尤其是在人员不足的情况下，会显得捉襟见肘。同时这种分工在某种程度上也给初级的运营人员设置了一个无形的天花板，容易造成职业倦怠。那么，还有其它选择吗？什么时候可以，以及如何采用整合型团队或者混合型团队呢？对此，国外同行们进行了不少实践。譬如，Google的Anton Chuvakin基于SRE（站点可靠性工程）提出了整合型威胁检测与响应团队的思路，而Forrester的Allie Mellen基于检测工程（DE）的生命周期理论也提出了整合型团队的设计思路。另一方面，随着包括威胁检测与响应在内的安全运营工具的智能化、自动化和体验水平的不断提升，也为更高效的团队架构设计提供了支撑。

威胁检测与响应预算

42%的受访者认为其威胁检测与响应的预算紧张，21.5%表示不足。对于未来，42%的受访者预计预算会适度增长。这个结果，对国内适用吗？不得而知。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfu5UFByDSCYOoOFKgGqyp9icBakaOLVtJFbgy9x9eIlaI2hFIToIiaSa4ibxpHHSELjiaR1BSaozsG9A/640?wx_fmt=png&from=appmsg)

检测与响应团队绩效度量

1）度量检测与响应团队的绩效对于向领导层阐释网络安全工作的价值和有效性至关重要，组织基本上都建立了自己的KPI指标体系。其中，67%的受访者采用了MTTR（平均响应时长），52%采用了MTTD（平均检测时长），其它关键指标还包括检测的事件数量（64%）、解决的事件数量（58%）。

2）针对这些指标，大家对其有效性的评价普遍不高。只有26%的受访者认为他们的指标很有效，还有39%的受访者认为他们的指标有效性一般般，依然存在较大改善空间。此外，51%的人认为他们在获取指标所需数据方面面临挑战。

3）与行业标杆进行对标分析（benchmarking）为度量指标（KPI）提供了更丰富的价值，因为对标分析可以让组织了解自身在同行中的水平。调研显示，仅有23%的组织实现了这项工作的常态化。笔者认为，随着指标度量的深化，对标分析意义越发凸显。否则，组织只能跟自己的过去比，无法进行同行间的比较，不知道行业的发展水平，不知道某个指标值多少才是好，多少才是差，可能还在为自己取得的“成绩”沾沾自喜，或者花费了过多的精力试图在低效的方向上进行改进。

4）掌握并度量检测覆盖情况对于旨在保持稳健安全姿态的组织至关重要。调查显示，大部分（64%）的组织会主动评估自己的检测覆盖和能力，但还有23%的组织没有做这个工作。如果不做常态化的检测覆盖评估，组织防御的盲点风险就高。74%的受访者采用ATT&CK框架来进行检测覆盖评估，采用威胁情报报告的比例是72%，采用攻击测试方式的比例是62%。

5）调查显示，不同组织的度量周期差异较大。29%的受访者表示他们每月评估一次（SANS认为这个频次有点低），每天评估的有9%，每周评估的有22%（SANS认为这个频次的性价比比较高），还有14%表示每个季度评估一次。

6）在度量指标改进提升方面，54%的受访者选择了实时监测能力，52%选择了高级分析与报告工具，50%选择了更好与其它安全工具集成，49%选择了常态化技能培训与评估，48%选择了采用更好的度量指标。

面临的挑战

1）调查显示，误报（FP）是检测网络威胁过程中面临的最大挑战，近64%的受访者做出了这个选择，排在挑战第二位的是数据量问题。笔者看来，误报直接导致告警疲劳，降低安全事件响应效率，浪费了响应人员的宝贵时间，引发职业倦怠。

![](https://mmbiz.qpic.cn/mmbiz_png/t7v7zyOTkMfu5UFByDSCYOoOFKgGqyp91lUJ0jMLic2OAS74cAiasQ2O8S1xrsbib6hZzGdRNphW3Pr9B2MCIxVibg/640?wx_fmt=png&from=appmsg)

2）在威胁有效的检测与响应能力方面，组织面临的最大挑战是预算制约（47%），其次是人才选育留、技术限制、合规要求。

总结

1）威胁检测与响应过程的自动化至关重要，82%的受访者使用了EDR，以及67%的组织使用了半自动化的响应系统证明了这一点。与此同时，人在检测与响应过程中的作用必将越来越重要，不要期待100%的自动化，而要不断平衡人与自动化之间的任务分工。

2）人们对AI有较大的期待，但当前AI的效果还有待提升。

3）近一半的受访者表示预算不足是他们保持有效检测和响应能力的最大障碍。笔者认为，放眼国内，在经济增速放缓的大背景下，安全投资增速必定也受到影响，如何盘活存量安全投资将越发重要，而盘活的关键就在于提升安全运营的效益。另一方面，网络安全与数据安全的法律法规和监管要求仍然在持续提升。这就要求包括检测与响应在内的安全运营更加高效，更加能够证明其价值。

4）误报（FP）是检测网络威胁过程中面临的最大挑战。短期内，应优化检测内容（规则），并要求供应商改进以减少误报。

5）对更全面的DR度量指标和更好地集成安全工具的需求凸显了该领域不断发展的格局，组织必须不断调整其策略以应对内部和外部压力。

6）当组织展望未来时，人们清楚地认识到投资于高级检测和响应功能的重要性，重点关注增加 AI 和 ML 的使用，改进与 SOAR 工具的集成，并加强培训计划以建立内部专业知识。

【参考资料】

[SANS：2023年事件响应调查报告](https://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484725&idx=1&sn=8d318b47e9dced09f5862dda65427ad6&scene=21#wechat_redirect)

[SANS 2024年SOC调查报告解读](https://mp.weixin.qq.com/s?__biz=MzUyNzMxOTAwMw==&mid=2247484811&idx=1&sn=18c651844e9668dd2ffa2f32db674f8c&scene=21#wechat_redirect)

预览时标签不可点

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
赞...