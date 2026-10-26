---
title: 智算+通算一体化：曙光医院如何让AI数据中心“用得起、管得好、跑得稳”？
url: https://mp.weixin.qq.com/s/eNAdHJed3uZIRXlpbjZGeg
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:15:16.816602
---

# 智算+通算一体化：曙光医院如何让AI数据中心“用得起、管得好、跑得稳”？

# 智算+通算一体化：曙光医院如何让AI数据中心“用得起、管得好、跑得稳”？

深信服科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/EJiaEo3Lq9koGLKLb2iaWgKP2F0ftwVWJA81gM12TmKNUKESbTUmMOlHbmARBVWeoxkRAMwBLMwX5w4ianpTibj6KQ/640?wx_fmt=gif&from=appmsg)

当前，医院信息化正面临多重考验：内存大幅涨价导致项目进度卡壳，信创升级迫在眉睫；AI应用探索遍地开花却难以规模化落地，GPU采购量激增却各自为战、利用率低下。曙光医院作为全国示范中医院、三级甲等综合性中医院，刚刚完成**“智算+通算”数据中心一体化建设**，其实践经验为行业提供了可借鉴的破局样本。

近日，深信服有幸邀请到上海中医药大学附属曙光医院计算机中心副主任徐平，与深信服科技云BG产品解决方案专家胡燕青、深信服科技医疗行业运营总监陈誉锋，围绕“AI时代医院数据中心如何用得起、管得好、跑得稳”展开深度对话。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dAHic6zw8swibsY3U5x1IsHOZBsat9rwNHcBhsP3ASOTiajEeDFQy0DoM2T47XnEVV7VWB9IiaJxNHzb30SFWzAeszpmCDESCic8fQxgIwiaGePbw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibDwB8tSP2ktzxWKlFXVuoMN0BrLDCXhSlkeAs9rMBA6HV3UB3qpvjbkIVD5tyIYzyxtdia7VCoac7nS5S3LjX3qHiaBHQgPW0bM/640?wx_fmt=png&from=appmsg)

**直面三大挑战：内存涨价、AI落地慢、算力管理难**

徐平坦言，曙光医院的信息化建设并非“要不要上AI”的选择题，而是“智算+通算能不能用一套底座一起管”的必答题。他回顾道，到今年，明显感觉旧的建设方式走不通了，主要卡在三个方面：

**第一，内存涨价冲击预算。** 医院计划推进信创超融合扩容，但按传统报价，光内存采购成本就要多花一倍，重新申请预算困难重重，项目迟迟无法落地。

**第二，临床智能体“叫好不叫座”。**医院探索了许多临床相关的智能体，希望能通过AI辅助诊疗，但临床实际落地仍需时间打磨，AI氛围尚未全面铺开。

**第三，GPU资源需求激增但管理粗放。**医院对显卡资源需求越来越多，云上租赁算力和本地数据中心算力资源的管理越来越复杂，技术变化也越来越快，缺乏统一视角和管理手段。科室之间“A科室的卡闲到发慌，B科室的卡排队等着用”成为常态。

徐平表示，正是这三大问题，倒逼医院定下明确目标：不能再“通算一套、智算一套”各自花钱，必须把传统业务和AI业务放在同一个数据中心底座上统一规划。这正是“智算+通算”一体化的由来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8sw8tu5fk6U7qonku5lW7AwUN5yuh4ichQqBxyjnMTdiaFp4bwoYwPN08fZoqjIYTwvlWM88V9JaJK1BUhdqYuWajTicRYSo1tT9yicc/640?wx_fmt=png&from=appmsg)

**破局一：内存分层——用技术换预算，信创升级同步落地**

面对内存涨价与预算困局，曙光医院与深信服联合交出了一份“技术换预算”的答卷。

徐平介绍，医院通过对现网资源进行监测发现，ISV提出业务需要256G内存，但业务并非每时每刻都把内存吃满，峰值之外的冷数据长期占比超过50%。基于这一洞察，医院引入了超融合“内存分层”技术：将热数据保留在物理内存，冷数据自动下沉至NVMe SSD，通过全局冷热识别、QoS保障和故障兜底机制，确保业务时延不退化。

深信服专家胡燕青补充道，内存分层不是简单的“把数据扔到SSD”，而是一套完整的机制。深信服与行业主流HIS ISV做过大量联合调优测试，**结果显示：同等业务负载下，开启内存分层后，TPS平均下降仅约2%，全部业务场景TPS下降不超过10%，性能几乎无影响。**同时，深信服已完成与卫宁、东华等主流ISV产品的兼容认证。

落地后的效果令徐平感慨：**“业务侧几乎没察觉任何变化，但内存采购需求直接砍了一半**，原本卡住的信创项目，预算一下就能满足了。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibO7b0dqwoszWq2aYAJUC2P7bmibau9ePicsZUCzUU9y3ASzenrLraqiaNWXXacTFiceYYVFnDqyH4gGhJdhWVtsMP4Nh7lv9xV5Nk/640?wx_fmt=png&from=appmsg)

**破局二：Agent Builder——零门槛让科室自己把AI用起来**

临床智能体落地难，是很多医院的共同困境。曙光医院的解法是：**换一个顺序，先让信息中心自己用AI把运维干起来，再把低门槛工具递给临床科室**。

徐平介绍，医院信息中心先搭建起一个AI智能体构建平台，通过AI在运维、运营类场景实现提效，例如日志巡检、告警归因、知识库问答。跑顺之后，再面向临床科室提供平台工具，让各科室有兴趣的成员可以快速尝试自己的想法。现在，医生、护士、行政人员不需要懂代码，就能构建高质量的私域知识平台，造出属于自己的科室小助手——病区交班助手、医保规则问答助手、科研文献综述助手等。

徐主任进一步对智能体安全的问题进行了补充说明，例如在智能问答场景，当医院预算不足时，可以利用底层数据治理的方式去屏蔽或脱敏一些敏感隐私数据。如有条件，医院可以借助AI安全护栏等工具，针对性进行重点安全管控。

胡燕青指出，这正是深信服Agent Builder想做的事——**“0专家、好效果”**。第一，降低门槛，通过简单拖拽即可搭建满足科室个性化需求的AI智能体，像搭积木一样完成复杂业务流程，让非技术人员也能构建稳定可靠的AI应用。第二，打造医院自己的知识底座，将科室、医院特有数据沉淀下来，完成自有数据的智能化、结构化处理，让医院知识真正为自己可用。

![](https://mmbiz.qpic.cn/mmbiz_png/dAHic6zw8swib7J78BSpE4ELcMEZl5V00uZ8uvicBsUTIRn7ibxnDPiavgtWdpRgGUBToxWJNkJLyuDaZMJkwYaKjkbJFSXkJYicm1fbQlqjVeOQo/640?wx_fmt=png&from=appmsg)

徐平感慨，**真正的变化是：AI从“IT推给业务”，变成“业务自己要”。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8sw9lXF1Tic4HjUvicicMpYcgZDyO9cWJibwtHSwscqhQgicn058tAUujy5uZZppz2XULZ5gAAou8V96fPeB3YRFQiaTCM32iccQzOiab41w/640?wx_fmt=png&from=appmsg)

**破局三：AI算力网关——从GPU孤岛到全院一张算力池**

GPU品牌杂、管理乱、利用率低，是医院算力治理的普遍痛点。曙光医院的对策是建设统一的算力调度管理平台，不管是云上还是云下的算力资源，平台都能全部纳管进来，对科室提供统一算力入口，按项目、按科室计量用量。

徐平分享了一组令人振奋的数据：通过AI算力网关统一纳管，医院整体GPU利用率从不到20%提升到60%以上，等于过去花一份钱、现在干出三份活。信息中心第一次能做到**“全院算力一盘棋，每一张卡的利用率、每个模型版本使用情况都看得见”**。

胡燕青进一步拆解了深信服AI算力网关的四个“统一”：统一入口，医院所有AI流量一个入口进、一个出口出，影子AI通道归零；统一运维管理，一站式接入和管理混合算力，屏蔽异构差异，让AI能力像水电一样即开即用；统一成本治理，全局看清混合算力用量与成本，统一计量和分摊；统一成本优化，持续优化模型服务与资源使用，降低有效Token成本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swicDDYnT65SrosmlK41aR61KlbQAas8tjSb5G3d2PhND11wy1g7vRk0JsUte3gB3Kue8m0VMyZrpqvbSI93APeiaIhuMC9Ax7jF8/640?wx_fmt=png&from=appmsg)

目前，深信服AI算力网关与英伟达、沐熙、天数、海光等业内主流显卡均已完成适配，支持跨厂商算力统一调度与管理。对医院来说，这不是多买一套设备，而是把已经买回去的GPU真正用出ROI。

![](https://mmbiz.qpic.cn/mmbiz_png/dAHic6zw8swibZIW5S82g7rG2GJVNokVTRkaInkqc3Rs0DHsRyfSjcbHjZc4Kn5b25Uo8RicpXQ8F0H5kPuzpqL2900AyRKrXGMexFF6OMsL68/640?wx_fmt=png&from=appmsg)

**一体化成效：用得起、管得好、跑得稳**

对谈最后，徐平用三个词概括了曙光医院的收获：

**1.用得起**——内存分层帮医院把信创扩容预算砍了一半，GPU利用率翻了三倍，AI不再是“只能看不能用”的奢侈品，而是真实可管理、可运营的资源输出。

**2.管得好**——智算和通算统一运营管理，实现资源可视可控以及精细化运营，降低信息中心运维压力。

**3.跑得稳**——整个过程没有一次业务中断，HIS、EMR 7×24小时在线，医生和患者完全无感。

胡燕青从行业视角指出，医院一旦把通算和智算建成两套独立烟囱，三年后的运维成本、数据打通成本、安全合规成本会指数级上升。**一体化的本质，是让医院今天投的每一分基础设施预算，都同时服务于“跑好现在的HIS”和“跑好明天的AI”——这才是真正的TCO最优解。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8sw9t3elsBW9KFXeKlXG5ZAowqYQvwBCf6hEpr0TpZ2uicooDOOZDe0hjuG1icCvoHaNbraSMzAZdosdJ3JSaw9RCYU7AmKqz7KONw/640?wx_fmt=png&from=appmsg)

**同行启示：三句话总结**

最后，围绕医院信息化建设，徐平用三句话总结了自己的经验建议：

**第一，规划上一定要“一盘棋”。** 传统业务和AI业务从底座开始就放一起设计，不要先各搞一套、后期再花数倍的资源去整合。

**第二，资源投入上要敢于用创新技术破局。** 内存分层、算力调度这些技术，本质都是“用创新能力换采购预算”。

**第三，生态上希望厂商从“单纯卖盒子”走到“顶层设计”。** 基于医院真实业务场景，联合打磨出真正适合医院可落地的方案，整个行业才能往前走。

胡燕青则表示，深信服会沿着“建得起、跑得稳、护得住”持续做深：用内存分层和算力池化让医院不增加预算也能把AI和信创同时落地；用通算智算统一纳管把信息中心从“救火队”变成“运营者”；用核心业务零中断让AI智能体真正实现提效增速。“医院少花钱、少操心、多干事，我们的活就做到家了。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swicxzUFXLjyYESHePkLMibvcykQcTgYIxZFPiakPYp0UgIhdJfq0rZg1ZQjq4Qmy5hoNicKLicNgQXmH7EHGZsPupH1VlYBfsQdbQ8k/640?wx_fmt=png&from=appmsg)

曙光医院与深信服的联合实践，为医院在AI时代实现“用得起、管得好、跑得稳”的数据中心一体化建设提供了清晰路径。医院的数智化，从单纯“买设备”的阶段，进入“顶层规划设计”的阶段——通算和智算不再是选择题，而是一道规划题。让医院的每一分IT预算，同时撑住现在和未来，这才是“智算+通算”一体化的真正价值所在。

![](https://mmbiz.qpic.cn/mmbiz_gif/EJiaEo3Lq9krfs3ibEGaKtAM7TnyRPib93bTqsm5kv7utUdcYu8iaHL3HBdE1A8bbh7tVz6WAyog6tTDuSbB9RlkJw/640?wx_fmt=gif)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9koicYib2cMiap0JlgdQm0RlLPBOh7AhGHYVfE5bm0BPp62ySojm1TzVCjqZZw1iawBrq3Sz6jDCHibRFCg/0?wx_fmt=png)

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