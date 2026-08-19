---
title: Anthropic研究揭示Claude的“多语种性格漂移”
url: https://mp.weixin.qq.com/s/pc5Rj87LUmV5ShWsfyemMg
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:54:35.390576
---

# Anthropic研究揭示Claude的“多语种性格漂移”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/F2BckGKQD7JygicL5UrqmxVpPe1dL0wbyFzzm4w46mbibAicmqxibk5u9hRABgxk00zA1sa90kibREbIoybsSC6azLIuuvhvqffCZtnN0SbNP8s0/0?wx_fmt=jpeg)

# Anthropic研究揭示Claude的“多语种性格漂移”

全球技术地图

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于启元洞见
，作者启元洞见

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM5oF4Lxh3KNVZ5bFcPlzFbTbXaDSTNgpJdvsq415prV7g/0)

**启元洞见**
.

洞察真知、提出卓见。聚焦科技领域事关长远全局和未来发展的战略性问题，开展跨学科跨领域的系统性研究，孕育一批客观公正、有深度的高质量成果和能够经得起历史与实践检验的独立见解。

![](https://mmbiz.qpic.cn/mmbiz_png/TPQsMW6ic4LEBy2FcPofR16ZzeDalNDg81sxxRY3pmJ5JdVyWYvgbZUCESoQicJJwI0rvGy5EaZgKIxhBuu7kImg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/F2BckGKQD7KsGQj0VIricpnJ8Sh8cEWqoq2FSAkcd1kOLFsXe0SmKwMw9ibIsibYibiaQZiczPnxAlOwTzC3XMFC4QCVwvT2kPVhrtCsiaaibO28Jbk/640?wx_fmt=png&from=appmsg)

**2026年7月13日，美国人工智能公司Anthropic发表研究文章《Claude在不同模型与不同语言中的价值观》（Claude's values across models and languages），系统量化了其旗舰模型在不同版本和不同语言语境下所展现出的价值倾向差异。研究团队通过对数百万真实对话的挖掘，构建了四维核心价值轴，揭示了从Sonnet到Opus的模型演进中，以及在英语、阿拉伯语、俄语等多语言交互中，Claude表现出的显著“性格”分化。这一发现挑战了人工智能价值对齐的单一性假设，也为未来跨文化、多语言人工智能的协同治理与评估提供全新视角。**

**构建价值度量衡：
大模型价值观的四维核心坐标轴**

**在面对缺乏标准答案的开放性人文与社会问题时，大语言模型的回答往往不可避免地折射出某种特定的价值偏好。**虽然其核心对齐规范在宏观层面上由相关行为宪章所约束，但在数百万次的日常对话交互中，模型实际表现出的具体取向仍极为繁杂。本研究旨在通过实证手段，对这些隐含的价值观进行可量化的系统性分析。

研究团队在前期研究的基础上，针对日常对话展开了深度挖掘。此前工作已从70万条匿名对话中识别出超过3000种具体的价值诉求，外加如此庞杂的列表难以支持直观的跨模型比对。**为构建一种可操作的度量衡，研究团队通过聚类与降维技术，将原始数据归并为339个高维核心价值概念。随后，研究团队对采集自不同模型及20种常用语言、涉及主观任务的约31万条对话进行了关联性压缩，最终凝练出四个关键的主成分价值轴。**这四个轴共同解释了日常对话中价值观变异度的15%。

**第一维度为“顺从与谨慎”***（Deference vs. Caution）***轴。**该轴衡量模型在面对用户时，是倾向于顺应、配合并接纳用户的个人偏好（表现为迎合、顺从），还是更倾向于主动预警和防范潜在的风险与伤害（表现为负责任的引导和危害规避）。

**第二维度为“温和与严谨”***（Warmth vs. Rigor）***轴。**该轴用以判定模型在表达上更侧重展现情感温度与关怀（表现为积极框架、肯定与鼓励），还是更加强调事实的准确性、精确度和客观中立（表现为严谨）。

**第三维度为“深度与简练”***（Depth vs. Brevity）***轴。**该轴表征模型的阐释倾向，即它是更愿意进行抽丝剥茧、多视角探究的深度说理与逻辑展开，还是更倾向于遵循极简原则，仅针对用户所问作出简单直接的答复。

**第四维度为“坦诚与执行”***（Candor vs. Execution）***轴。**该轴衡量模型自我定位的边界：一端是“坦诚”，即模型更倾向于主动展现自身作为人工智能的局限性与不确定性，表现出理智上的谦逊；另一端则是“执行”，即模型更致力于交付一个经过高度修饰、自信且结果导向的完整答案。

![图片](https://mmbiz.qpic.cn/mmbiz_png/z11U7glr68KyFkyssDmfRlwAPVvJVCGCaYicKZJAbA0Jg0FMSEJRqXyhLKibEMmFcqPx3dvvGD52qxiaBc5q11Wen5UDpFEicL4qbsl4A9JpAJM/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

*图1 四个关键的主成分价值轴。各轴是两组数值之间的数轴。每个值在各轴上的位置，按其对该轴贡献比平均值贡献的数量多多少倍来排列，并标记贡献最强者。大多数值贡献低于平均值，这意味着每个轴由一组关键值驱动（如图中标注）。*

**Claude模型版本迭代对其表现特质
的重塑效应**

研究表明，不同版本的Claude模型由于角色特征训练及微调策略的差异，在四个核心价值轴上的落点呈现出显著分化。这些细微的统计学差异，在实际应用中直接构成了用户可感知的模型“性格特质”。

**Sonnet 4.6在行为特征上表现出高度的温和性、顺从性和简练性。**数据分析显示，Sonnet 4.6在“温和”端表现出+0.17σ（标准差）的显著倾斜，在“顺从”端为+0.14σ，“简练”端同样为+0.14σ。在实际对话中，Sonnet 4.6倾向于高度肯定用户的想法与工作，善于通过幽默、趣味性的语言来缓和气氛，积极模仿用户的语气和规范，并在不设预设立场的情况下提供情感慰藉。这种特质使其在日常高频互动中表现出较强的亲和力。

**作为对照，Opus 4.6的取向呈现出一种折中状态。**它在“顺从”轴（+0.09σ）和“严谨”轴（+0.10σ）上均有所倾斜，且在“执行”和“简练”方向也存在一定偏向。该模型在行为上的直观映射是倾向于“直奔主题”，并且在回答过程中严格遵循用户请求的边界，尽量不溢出任务本身。

**而最新旗舰模型Opus 4.7则展现出了截然不同的性格。Opus 4.7表现出了极强的谨慎性（+0.24σ）、深度性（+0.23σ）以及坦诚性（+0.11σ）。**在实际应用中，这种价值导向转化为了一系列极具思辨色彩的行为特征：它在面对用户不合理或存在错误的假设时，会更主动、更直接地予以纠正和反驳；它经常在用户未主动要求的情况下，前置性地预警操作或决策中的潜在风险；面对用户的观点或作品，它倾向于提供客观乃至尖锐的坦率批判；在生成回答时，它倾向于详细拆解其背后的推理过程，并主动承认自身的知识局限。这一分析结果也吻合了近期部分用户群体的直观体验。

![图片](https://mmbiz.qpic.cn/mmbiz_png/z11U7glr68L6w6wjn05g0Y2OAT4CkGYoFib5RBTwo1wicV3lNuWq1kPSUHqcT23JKicCUzp6MM15U2F6ZIEOalyXrmMicbWt1lIjoQoXTlicQvkQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

*图2 不同Claude模型在四维价值轴上的平均偏移情况（单位为标准差σ），并列举了各自标志性的行为表现。Sonnet 4.6偏向温和与顺从，Opus 4.6表现为直接高效，而Opus 4.7则显著走向了严谨、深度与谨慎。*

**语言语境的隐形塑造：
不同语种对话中的价值取向漂移**

**除了模型架构和训练参数迭代外，交互所使用的语言同样在暗中塑造着人工智能的价值表现。研究发现，面对性质完全相同的任务，Claude用不同语言进行回复时，其折射出的核心价值倾向也会发生明显漂移。**这在“温和对严谨”以及“坦诚对执行”两条轴线上表现得最为强烈。

**在“温和与严谨”维度上，语言带来的异质性尤为突出。**当Claude使用印地语*（Hindi）*和阿拉伯语*（Arabic）*进行对话时，它展现出了极强的“温和”特质（印地语偏向达+0.49σ，阿拉伯语为+0.28σ）。在这两种语言环境下，模型会自发采用高度礼貌的措辞，频繁使用富有同理心的表达，通过幽默感来活跃气氛，积极肯定用户的成果。而在英语*（English）*和俄语*（Russian）*环境下，模型的落点则大幅向“严谨”端发生偏移。在英、俄双语环境下，Claude表现出鲜明的求真务实特征，倾向于主动质疑不实假设，修正细节性差错，并要求用户提供论据支撑。

在“顺从与谨慎”维度上，阿拉伯语语境下的Claude表现得最为顺从（+0.08σ），而英语语境下的模型则最具防范意识，大幅向“谨慎”端倾斜（+0.10σ）。在说理深度上，英语语境最能激发模型的“深度”表达（+0.09σ），Claude 会在此语境下深入细致地梳理逻辑；相反，阿拉伯语环境下的 Claude 则更倾向于“简练”的表达方式（+0.10σ）。

**在“坦诚与执行”的博弈中，不同语种的“性格”差异同样明显。**当切换到荷兰语*（Dutch）*时，Claude表现出了较强的“坦诚”特质（+0.04σ），表现为乐于承认并承担自身生成内容的错误和局限性；而在印尼语*（Indonesian）*语境中，它则大幅转向了高效且不带过多自我否定的“执行力”端（+0.04σ）。

这意味着，**在多语言应用场景中，由于语言背后的训练数据和文化规范的天然差异，即便是同一个用户针对同一份商业计划书寻求反馈，其用印地语提问和用俄语提问，将分别获得不同维度的交互体验。前者可能得到的是充满鼓励与温情呵护的反馈，而后者则更可能得到一份指出多处漏洞的硬核评估报告。**这种隐性的差异对跨文化人工智能价值对齐提出了更复杂的科学命题。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/z11U7glr68LFFRkLSWuaI4jSW7QbPPWbjIiaILX8pyHWTfGYvWvUsjgUiadJjpicN2rKFyVibf67qqbxV9nia6LBmFgJmzDW9ABTrTJIub6pXrpA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_png/z11U7glr68K0Nja9MCtnyPVPSFWI3Xzuic60v2Jqm0cW6yPIKT7jnX4vv8KibViaZvODNT7ro65Ixx9icEJgsxOwcUjNpiazDrumeqsfBvdIwP3g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

![图片](https://mmbiz.qpic.cn/mmbiz_png/z11U7glr68JqgMbZF7MknNKTBNN1oYvjBolWHYkH4FvicC6GWIGHWe7DdYiaB9gfdm4PHundWXOxd8AssHJicAT0x2ibt7h1EErPmKDH7NAgzlY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

*图3 Claude在使用不同语言（如印地语、阿拉伯语、英语）进行对话时，在四维价值轴上的偏移轨迹和独特行为模式（限于篇幅，仅截取部分，完整版详见官网）。不同语言显著拉动了模型在情感温度、说理深度及顺从程度上的落点。*

**价值漂移的根源探寻与未来治理路径**

研究团队认为，**上述存在的模型间与多语言间的价值观分化，是由多种底层技术因素共同交织的结果。**

**首先，训练数据在数量和质量上的分布失衡是最主要的根源之一。**在模型的预训练和微调阶段，不同语言的数据不仅在绝对体积上存在数量级的差异，其内容组成也具有截然不同的社会背景。例如，某些语言在网络上的高质量文本可能高度集中于专业学术论文或严肃的商业报告，而另一些语言的语料则充斥着大量的社交媒体对话。这导致模型在汲取这些语料时，自然而然地继承了其背后所附带的职业规范或文化交往特征。

**其次，文化规范与交际礼仪的跨语言差异也是造成价值漂移的隐性推手。**不同语言的社群本身就承载着独特的沟通规范和价值偏好。Claude在对多语言文本进行深层表征学习时，可能会捕捉到这些潜移默化的文化期望，并试图通过微调自身的交互风格，以更好融入并服务于特定语言社群的交流习惯。但这种自发的行为自适应是否在所有场景下都符合预期，依然需要谨慎的评估。

**这一研究成果为未来的人工智能系统构建与安全治理指明了若干方向：**

* **深入探索价值偏差的生成源头。**仅知道Claude的价值观会发生漂移是不够的，未来的研究需要致力于将这些价值变异追溯至具体的预训练语料库、特定的微调阶段以及特定的上下文激活因子，从而能够在底座模型训练阶段进行更具建设性的干预。
* **系统评估价值漂移对终端用户的实际影响。**当前的研究仍局限于对价值观表现的客观测量，但这些微小的“性格偏差”究竟会在多大程度上影响用户的信任度、体验以及决策质量，仍需要开展多维度的用户实证研究。
* **确立多语言语境下的价值观对齐准则。**尽管相关对齐规范明确阐述了诸如温和、诚实和谨慎等核心理念，但它并未明晰这些原则在遭遇跨语言、跨文化冲突时应当如何进行动态裁量和偏好权衡。如何倾听并合理权衡不同语种社群的声音，让人工智能在保持文化自适应的同时，不偏离人类的普适价值共识，将是构建安全、公正的全球化大模型系统的核心挑战。

**免责声明：**本文转自“启元洞见”。文章内容系原作者个人观点，本公众号编译/转载仅为分享、传达不同观点，如有任何异议，欢迎联系我们！

**推荐阅读**

[技经观察丨特朗普政府干预下原料药产能迁美对华医药产业风险分析](https://mp.weixin.qq.com/s?__biz=MzI1OTExNDY1NQ==&mid=2651621754&idx=1&sn=9fce9bf6bb40e3856b340d7ab28b1bec&scene=21#wechat_redirect)

[技经观察丨从美国防部更名看美军事战略转型及涉我影响](https://mp.weixin.qq.com/s?__biz=MzI1OTExNDY1NQ==&mid=2651621814&idx=1&sn=900a25002e21411a69d276630d9c9bca&scene=21#wechat_redirect)

[技经观察丨美构建跨大西洋AI医疗监管联盟新动向及对我影响](https://mp.weixin.qq.com/s?__biz=MzI1OTExNDY1NQ==&mid=2651622218&idx=1&sn=008f3795f4a8e054ffd181d284ead4db&scene=21#wechat_redirect)

[技经观察丨太空AI中心能否破解算力困局？](https://mp.weixin.qq.com/s?__biz=MzI1OTExNDY1NQ==&mid=2651622287&idx=1&sn=cb2a420001c1f9dd4f9b585706dda90b&scene=21#wechat_redirect)

[技经观察丨氦–3：未来科技竞争的新高地](https://mp.weixin.qq.com/s?__biz=MzI1OTExNDY1NQ==&mid=2651622900&idx=1&sn=b56ca95b21660d3ebb837d8fc06020c7&scene=21#wechat_redirect)

**转自丨启元洞见**

![](https://mmbiz.qpic.cn/mmbiz/TPQsMW6ic4LEicnldHpFAAVWgPibnneANiamQU8ibAVynPEOCjTPicpqmJEWBujzs1GRvjWWJZechQcgaicRItUiaPjSpw/640?wx_fmt=gif)

**研究所简介**

国际技术经济研究所（IITE）成立于1985年11月，是隶属于国务院发展研究中心的非营利性研究机构，主要职能是研究我国经济、科技社会发展中的重大政策性、战略性、前瞻性问题，跟踪和分析世界科技、经济发展态势，为中央和有关部委提供决策咨询服务。“全球技术地图”为国际技术经济研究所官方微信账号，致力于向公众传递前沿技术资讯和科技创新洞见。

地址：北京市海淀区小南庄20号楼A座

电话：010-82635522

微信：iite\_er

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPQsMW6ic4LEutPpWMEricCzaLeibz3IUuGonhS5dmxA9be08FaoXUU2yoHXqia7Qzg2DkYeiblsUeqs01xClpHrNWA/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPQsMW6ic4LGOQIuiajvfE4Y1KuItRbn8JPVhtonhQ8IAvWw6pbBsl6rbICODcaQEvH5U8pUCYZdiaMLJqLg7nDIw/0?wx_fmt=png)

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