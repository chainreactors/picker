---
title: 如果 MaaS 是个伪命题，大模型时代的「云」应该怎么建？
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653047178&idx=1&sn=f6df370043b25cc8042bd77502c92363&chksm=7e57343c4920bd2a20196c33852bbafb97d3a60e232129cb1146a140d5e4cf1f2ce785ff007f&scene=58&subscene=0#rd
source: 极客公园
date: 2024-07-12
fetch_date: 2025-10-06T17:44:14.836499
---

# 如果 MaaS 是个伪命题，大模型时代的「云」应该怎么建？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YTUib6Sibb1EcHPf2607ljbrmfSQhghyImQP8lWjCvic0ibtll9FHvFp5gRRjvpIriagzytuzibYFH1Qfw/0?wx_fmt=jpeg)

# 如果 MaaS 是个伪命题，大模型时代的「云」应该怎么建？

原创

ray

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YTUib6Sibb1EcHPf2607ljbrw2xBX3vwA6DjXUibuVUSFeOyUafibsCibACSoBibZMzdetXCic5icAbbySbA/640?wx_fmt=jpeg&from=appmsg)

大模型竞赛，这家云巨头不迷信万能模型。

**作者 | ray****编辑**| 郑玄****

2024 年的大模型产业，注定将是会被反复提起的历史一页。

这一年，被按下加速键的市场，刚刚过半，就已经显示出冰火两重天的格局：

算法的单模态扩展到多模态，趋势如燎原之火，让全球陷入对世界模型畅想的狂欢中醺然欲醉；

一级市场却逐渐走向熄火，投资人从向大牛要论文，变成了向企业要收入，百模齐发迅速被简化为几家独角兽之间的资本与技术持久战；

云服务巨头，则以一种标准制定者，以及顶级大模型团队背后力量的角色出现，成为市场中隐形的手。在他们的主导下，过去 IaaS、PaaS、SaaS 的角色分工，在 AI 时代被芯片层、框架层、模型层和应用层取代，又迅速进化为基础设施、工具和应用的新「三层架构」。

技术的发展，基础设施的成熟，让千行百业都产生了所有生意都值得在大模型时代重做一遍的信仰。

但如何低成本、高质量的重新做一遍，是所有企业，必须回答的关键问题。

一定程度上，今天凌晨举办的 2024 年 亚马逊云科技 纽约峰会，可以作为观察这个时代之问的最佳切口。

**01**

****没有一个模型可以一统天下，****

****MaaS 或许是个伪命题****

一个新的业内声音是，MaaS（模型及服务），或许会是一个辉煌又短暂的概念。

亚马逊云科技作为三大海外云服务巨头中最注重大模型企业业务，同时也是规模最大的一个，显然是这个观点的坚定支持者。

包括今天凌晨的纽约峰会，多个公开场合，亚马逊云科技高管们都在宣扬同一个理念：「（现实落地中），不可能依赖单一、万能的大型语言模型应对各种任务。」

将这句话，翻译的直白些，就是现实中，没有一个大模型可以一统天下。

一方面，在算法落地中，技术、时延和成本之间往往会形成稳定的不可能三角，面对不同需求，往往对应着不同的最优解法。比如与 GPT4 系列叫板的 Claude 3.5，其实一共分三个版本，其中相对轻量级的 Haiku 版本，反而凭借着低时延与低成本优势，在实际案例部署中更受欢迎。

即使单纯聚焦到技术的单一维度，「最强模型」也同样是个伪命题。依旧是拿最新 Claude 3.5 与 GPT-4o 做横向参数对比，**Claude-3.5-Sonnet 在**物理、化学和生物学**几项中超过了 GPT-4o，但是在数学、天文等科目中，则**GPT-4o 更占优。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTUib6Sibb1EcHPf2607ljbrdgEZDPLuH7kgbve2Y5CDuv1hk0KDylmlLcyFkk6vnf9tB2bupJNC5w/640?wx_fmt=png&from=appmsg)

既然需求多元、技术评价多维，那亚马逊云科技的思路，就要打赢这场仗，需要的是一场「人民的战争」，尽量接入最多的大模型在平台之上供用户选择。目前，Amazon Bedrock，已经接入了三十多家世界顶流大模型。其中既包括亚马逊自研的基础模型 (Amazon Titan)，也包括了 6 家 AI 公司的第三方模型（如 AI21 Labs、Anthropic、Stability AI 等）。

更多的模型接入之外，过去一年多时间里，Amazon Bedrock 还推出了一系列功能辅助模型微调与上线：如 RAG（检索增强生成）、模型微调和定制功能、开发工具 Agents、模型安全功能 Guardrails for Amazon Bedrock 等。

在此基础上，本次发布会上，针对开发工具 Agents for Amazon Bedrock，亚马逊云科技继续推出两大重磅新功能。

（1）保留交互记忆——用户与算法的每轮对话的摘要将被保留，进而在航班预定、点外卖等复杂多步骤任务中，能够自动为用户推荐满足其座位偏好、餐食选择偏好的决策。真正做到让大模型适应每个用户独特需求和偏好做到千人千面。

（2）代码解释功能上线——该功能可以在安全的沙盒环境中动态生成和运行代码片段，并能够处理复杂的用例，使得大模型能力提升到可以处理包括数据分析、数据可视化、文本处理、求解方程式和优化问题。

不过，无论是成为覆盖最广的大模型货架，还是提供最全的工具箱，都不是亚马逊云科技野心的全部。它的目标是成为整个时代的基础设施。

**02**

****亚马逊云如何布局****

****生成式 AI 的三大关键层次****

比单纯否定 MaaS 更难的，是建立新的技术与规范。

对亚马逊云科技来说，一个新的命题是，如果 MaaS 不成立，那亚马逊云科技又将如何应对来自不同客户的不同需求？

对外，亚马逊云科技选择将 AI 开发者生态做大。截止当前，亚马逊云科技已经在 200 个国家和地区培训了超过 3100 万名生态开发者，提前一年多实现了到 2025 年为全球 2900 万人提供免费云计算技能培训的目标。

对内，亚马逊云科技的答案则可以结合其在过去一年中在基础设施算力层、工具层、AI 应用层三大维度的不断拼图补全，可以窥见亚马逊云科技对整个市场的认知与针对性解法。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTUib6Sibb1EcHPf2607ljbruNbxVuLThSdqGrnibJTzsqg5FYxJ0m6aEnu3xqwTnMUVooOWQmib4Diaw/640?wx_fmt=png&from=appmsg)

算力层，做厚用于基础模型训练和推理的基础设施。这一层主要服务于有大模型训推能力的企业，为他们提供芯片、存储、网络在内的基础设施服务。高性能低成本与绿色，是亚马逊云科技的核心优势。目前已经有 Anthropic、Mistral AI、Hugging Face 等众多明星 AI 团队在亚马逊云科技进行大模型的训练。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTUib6Sibb1EcHPf2607ljbr58WHftf6C1kh7EZayIhlBbUEzXfvsTrw6hGwP8CnGWhtTZ9DsZiavew/640?wx_fmt=png&from=appmsg)

关于如何构建高性能计算集群, 一方面，亚马逊云科技继续提供来自英伟达的计算实例，英伟达多款先进算力均率先在亚马逊云科技落地，包括亚马逊云科技将提供基于 NVIDIA Grace Blackwell GPU 的 Amazon EC2 实例，以加速构建及运行数万亿参数的规模大型语言模型的性能，亚马逊云科技将提供首款搭载英伟达 Grace Hopper 超级芯片的云 AI 超级计算机，以及首款采用英伟达 GH200 NVL32 的 NVIDIA DGX cloud。这些将在 Amazon EC2 实例上可用，可以让用户能轻松扩展至数千个 GH200 超级芯片。

另一方面，亚马逊云科技也在持续投入自研芯片。针对大模型的训练与推理两个最重磅环节：亚马逊云科技的推理芯片 Inferentia 已经升级至二代，并专门针对包含数千亿个参数的生成式大模型进行了优化，与一代 Inferentia 相比，吞吐量提高了 4 倍，延迟降低了 10 倍。训练侧的加速芯片 Trainium 也同样升级到二代，专门针对超 1000 亿甚至万亿参数模型的深度学习训练打造。

在成本侧，众所周知云计算是一个典型的具有规模效应的市场，玩家市场份额越高，单位算力的平均成本就越低：2023 年，亚马逊云科技在全球云服务市场的市场占比为 31%，营收高达 908 亿美元，连续多年蝉联全球第一。其中，仅在 AI 领域：全球就有 96% AI 独角兽将产品部署在亚马逊云科技，福布斯 AI50 榜单里的玩家，也有 90% 将其产品运行在亚马逊云科技。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTUib6Sibb1EcHPf2607ljbrwp4g9wRY2qcXeR7WETdouSlhFdfxA9Ptr8iakjU5cXOPUg9DNmWI8YA/640?wx_fmt=png&from=appmsg)

而针对 AI 在近些年来变身高耗能行业，亚马逊云科技则在发布会上官宣，通过能效提升、增加服务器利用率以及建立光伏、风能站点，购买绿证等行为，目前亚马逊云科技已经实现全球基础设施 100% 使用可再生能源，相较计划，提前了七年。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTUib6Sibb1EcHPf2607ljbrebSynKZiaOWttVypL77hl8OLe58sMmOfbE4fTyqh6lTeiaaGax1aQeAw/640?wx_fmt=png&from=appmsg)

第二层，进一步完善中间工具层 Amazon Bedrock 以及各种附加功能。这一层，主要服务于对大模型有深度应用需求，但没有开发能力的企业。亚马逊云科技提供的除了全球主流大模型公司产品之外，同时提供各种微调、知识库、测试比较、安全等多种工具。仅过去一年半，亚马逊云科技针对不同需求，GA（正式可用）的数量有 326 个之多，是其他供应商总和的两倍。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTUib6Sibb1EcHPf2607ljbrX5HYONHohibI69Nqdh0DHKCTLYiaN3RrBzrYQhenk4eZ4NtRRzKTtIWw/640?wx_fmt=png&from=appmsg)

其中，模型微调能力，是这一层级企业对大模型需求的重中之重。此次发布会上，除了保留交互记忆、代码解释两大新功能上线之外，亚马逊云科技 还针对 Amazon Bedrock 中的已有明星模型 Claude 3 Haiku 版本，提供了微调能力。SK 电信和路透社是其微调功能最先体验者。其中，路透社通过微调，其专属版本的 Claude 3 Haiku 任务性能提高了高达 40%。

在工具侧，针对已有的 Guardrails for Amazon Bedrock 功能（帮助模型过滤有害信息与敏感信息，可拦截高达 85% 的有害内容）亚马逊云科技做了进一步升级，将其变成独立的 API，除了能够深度耦合 Amazon Bedrock 平台，同时也可以支持非 Amazon Bedrock 平台上的各种生成式 AI 模型。

另外，亚马逊云科技还为 Guardrails API 添加了一项名为 Contextual Grounding 的新功能，可以通过语境分析降低 75% 的大模型幻觉的产生。

应用层则定位于企业级生成式 AI 助手，核心产品是 AI 助手 Amazon Q 为核心的一系列开箱即用 AI 应用集合。这一层主要针对有大模型使用意愿，但不想投入过多技术精力的企业，帮助他们降低 AI 的开发成本。

本次的发布中，亚马逊云科技重点推出了一个名叫 Amazon App Studio 的新功能。通过 Amazon App Studio，用户通过对话，就能建立自己的企业级应用程序。相较传统的企业搭建应用雏形，引入大模型填充细节，Amazon App Studio 从设计源头就引入大模型，并通过可视化的方式，将应用程序搭建的代码量一步降低 80%，一个不擅长写代码的 IT 项目经理，也可以在几分钟内完成一位资深程序员几周才能解决的业务问题。

举个简单例子，一家传统企业要创建一个库存管理程序时，只需要告诉 Amazon App Studio 我要生成这个程序，然后在接下来的多轮交互中，不断细化「最高权限只能 CEO 具备」「同意按钮只能审阅者能使用」「某种类型商品出库必须经过三级审批」等等具体的要求，一个完整的程序就能在几分钟内创建完成。

理想总是很丰满，但正如同大模型百人场景的 POC 与万人场景的应用难度不可同日而语，亚马逊云科技这一套新时代基础设施的成立与否，也需要来自实践的检验。

**03**

****大模型的答案，****

****还是要回行业里找****

伴随着亚马逊云科技在基础设施、工具、AI 应用三大维度的拼图不断被补全，所有生意都值得在大模型时代重做一遍，几乎成了大部分企业的信仰。

最新发布的 Amazon App Studio，在测试期间，已经展现出了其对传统软件开发模式的颠覆：

作为全球审计龙头，德勤成为 Amazon App Studio 第一批吃螃蟹的用户。在其首席顾问 JB McGinnis 看来，德勤的客户来自全球各地不同行业，每个客户都有不同的任务和流程要求，借助 Amazon App Studio，只需几句话就能轻松地从想法转变为应用程序，整体运营效率与客服服务质量被极大提升。

医疗大数据及分析服务提供商 HealthVerity 也成为了最早尝到 Amazon App Studio 甜头的客户。过去公司需要至少安排五名程序员开发和维护公司的低代码平台，依然无法满足安全合规需求，App Studio 则做到了对开发人员时间精力的完全解放，普通员工也能在几分钟内构建自己的应用程序。

即便在合规要求最严格的金融市场，上云、用 AI 也早已成为共识。

早在 2022 年，从 MRX 期权交易所和债券交易所 (NBE) 开始，纳斯达克就已经逐步将其北美市场的业务迁移到亚马逊云科技 之上，到了去年，纳斯达克又将旗下另一家期权交易所 GEMX 迁移到 亚马逊云科技，上云后，延迟改善了 10%，纳斯达克整体能处理的消息流量比五年前增加了四倍，每条信息的成本降低了 80%。Amazon Bedrock 帮助下，纳斯达克的分析师进行市场信息提炼、分析的时间减少了 33%。

生物制药领域，大模型则彻底颠覆了过去百年的行业生产模式。

拜耳在医疗保健和农业领域拥有 150 多年的历史和专业知识。在这一领域，伴随着全球人口的急剧膨胀，地球粮食总产量需要增产至少 50% 才能满足人类所需。这一背景之下，在技术开发侧，拜耳选择合作亚马逊云科技，通过 Amazon Q，拜耳减少将模型从概念验证过渡到生产和最终业务采用所需的开发周期，降低了 70% 以上拜耳开发了图像分析管道将开发人员的开发时间降低了 70% 以上。

以上并非个例，基础设施的迭代升级正推动行业应用的爆发，形成正向循环，所有生意在大模型时代被再次重构，正成为现实。

**04**

**结尾**

关于这一轮大模型热潮，过去相当长一段时间，市场都将最多的目光放在了算法本身的进步之上，随之而来，Open AI、Anthropic、Stability AI 在内，一众明星算法公司被捧上神坛。

产业链的力量，在一定程度上被忽视了：从底层的芯片、云服务，到中间层的模型，再到最上层的应用，整个大模型产业链的各个环节之间，如同互相嵌合连接的精密传动仪器，任何一个环节的进步与迭代，都会掀起整个市场的涟漪不断传导扩散。

其中，云服务等基础设施范式的存在，如同整个板块的地基。地基之上，算法可以从 CV 火到 NLP，体量可以从最初的十几层网络增长至如今的大模型，内容维度也可以从文字、图像上升到视频。

但一个常识是，上层的算法应用越想改变世界，最底层的地基就要越稳固。

亚马逊云科技的进步，也是整个大模型产业链不断向前飞奔过程中，被极大低估的一环。

参考资料：《拥抱云原生加速推进数字创新 选择亚马逊云科技从容迈向新时代》https://baijiahao.baidu.com/s?id=1792572052533259617

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**直播预告**

超！难！抢！票！的 Bilibili World 2024，我们来了！

作为国内二次元「浓度」最高的大型线下活动，这里有今年最热的鬼灭、芙莉莲，米家的原神、星铁、绝区零，还有 60+ 独立游戏，各种酷炫的动漫、电竞、游戏周边，以及各路 Coser 大神……

抢不到票？未满 18 ？不耐上海 40℃+ 高温？没有关系！7 月 12 日（周五）12:30，来极客公园视频号直播间，二次元老炮带你暴走 BW2024！

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZkjI3IMzly92iayZ4G4QNxseLFBFzNavqJeh2dAbdmDpsoN8oeO3E8Oe8fsuRYmic4uNwgabOJh8IA/640?wx_fmt=jpeg&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5abLUyFJSR0O8reNmMOWnMKZlxT0YSjx1rV1RCS4XcJ6dAs4y6HuicYLQck2LMYjRV8DpkEicgObyuw/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653047092&idx=1&sn=4c7b5959e9bd09ef9a9eb08e9cb64b0e&chksm=7e5734824920bd9402166ee296ef768716ee87ec4ea2bf7e3eecd02d8c608c45b1c314dff0ad&scene=21#wechat_redirect)

...