---
title: 多模态大模型安全评估基准MultiTrust
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247498190&idx=1&sn=dcc73734c7aa82d2f8f41d0fc088cfbc&chksm=e84c5f11df3bd607c47708e9867d28e28aead83371376df3b53f737a68f0d1ff646f7070365c&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2024-12-31
fetch_date: 2025-10-06T19:41:01.616862
---

# 多模态大模型安全评估基准MultiTrust

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUZIk8mKNRdDR63jfAbX3bPpS9aokrka2xhUwhB24lh2VuaGAGc2jy19qokAagyRkntW5Xn2FgnxrQ/0?wx_fmt=jpeg)

# 多模态大模型安全评估基准MultiTrust

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUZIk8mKNRdDR63jfAbX3bPpRWuibIKIH9UgMWSMcYdicU9Z35HbreiaGL8jgHQqiarRaG7iahB5yicI7APQ/640?wx_fmt=gif&from=appmsg)

由清华大学、北京航空航天大学、上海交通大学和RealAI联合研究的MultiTrust框架[1]是一个针对多模态大模型的可信评估基准，从真实性、安全性、鲁棒性、公平性和隐私性对多模态大模型安全进行综合评估。MultiTrust作为多模态模型安全领域的前沿研究工作，极具关注价值。

一、多模态大模型安全

随着各行业对大模型处理复杂智能任务需求的日益增长，单一模态模型因其上下文缺失、信息不全面等局限性而难以胜任多元化需求。多模态大模型(Multimodal Large Language Models，MLLMs)是指融合文本、图像、音频、视频等多种模态数据进行联合训练，通过学习不同模态之间的关联，实现更为智能化的信息理解和处理的模型。多模态模型不仅可以理解单一模态的信息，如文本、图像或音频，还能够跨模态地理解不同模态数据之间的关系，从而进行更加全面和准确的信息处理，实现1+1＞2的效果。

然而，当纯文本任务扩展至多模态场景时，会涌现新的风险挑战。新模态给模型安全带来了更加错综复杂的因素，除了不同类型数据本身引入的复杂多变的攻击类型外，还存在模态之间相互作用造成的决策错误问题。多模态大模型在可信度方面仍然存在明显的缺陷，并且相比于大语言模型表现出了更多的脆弱性。

尽管在大语言模型的安全评估领域已经取得诸多成果，但针对多模态大模型的安全评估研究仍显得相对匮乏，且现有的大语言模型安全评估基准仅能触及多模态大模型安全的部分方面，无法使多模态大模型得到全面和准确得安全评估。MultiTrust框架的出现有力弥补了这一研究领域的空白，为多模态大模型安全评估提供了有效解决方案。

二、MultiTrust

2.1

框架

与大语言模型的安全评估基准相比，多模态大模型安全评估除了要考虑单一模态维度上的安全风险，也应当纳入模态间的相互作用、模态间的语义鸿沟等多模态场景下特有的风险和威胁。

在设计评估框架时，MultiTrust关注到由于引入新模态而带来的多模态风险以及不同模态之间的相互作用，在数据和任务设计上将多模态风险与跨模态影响纳入考量。其中多模态风险是在多模态场景下，图像模态或图像-文本对中存在的安全风险；跨模态影响则考虑到新模态对其基础LLMs行为的影响，在MultiTrust中通过测量当纯文本任务增加语义相关或者不相关的图像时的模型表现来评估跨模态的影响。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUZIk8mKNRdDR63jfAbX3bPp7kcBib09wE4jUIK2eg3hKmKw34RzQ1K5MFeWkSBgMt6iauXVBhicxbLQw/640?wx_fmt=jpeg&from=appmsg)

图 1 MultiTrust框架

为了构建系统性和全面性的评估，MultiTrust设计了32个细粒度任务场景，这32个任务涉及到生成式、判别式任务以及多模态、纯文本任务，有助于深入评估多模态大模型的可信程度。同时，由于现有研究缺乏各类场景下的评估数据集，MultiTrust的团队在已有文本、图像、多模态数据集的基础上构建了20个评估数据集，并结合Stable Diffusion等算法合成的数据从头构建了8个数据集。

MultiTrust在github上提供了评估数据集和评估脚本[2]。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZIk8mKNRdDR63jfAbX3bPpH3gxVGqfrh0vkYmT8qmBRR1KGxDZiacldCz2cKH6fEelqkbFkfva0Pg/640?wx_fmt=png&from=appmsg)

图 2 MultiTrust覆盖的 32个评估任务

2.2

评估维度

基于LLMs安全评估和MLLMs的相关研究，MultiTrust设置了五个可信评估维度：真实性（Truthfulness）、安全性（Safety）、鲁棒性（Robustness）、公平性（Fairness）和隐私性（Privacy），其中真实性、安全性和鲁棒性确保模型在防止不良结果方面的可靠性和稳定性，公平性和隐私性则评估模型的社会伦理影响，比如偏见歧视、身份盗窃等权利侵犯的问题。

这五个维度又可以进一步细分为十个子维度：

* **真实性：**衡量MLLMs输出是否和客观事实一致。可细分为：

1)      内在缺陷：导致不准确输出的模型内部制约。

2)      误导性缺陷：由误导性输入引起事实错误的缺陷。

* **安全性：**衡量MLLMs的响应是否会造成意外后果，如非法行为或意外伤害。可细分为：

1)      毒性：MLLMs产生有害响应的倾向，涉及到模型内容安全。

2)      越狱：MLLMs对试图引起非法响应/绕过的越狱行为的表现。作者将LLMs的越狱提示转换成了截屏图像以检测OCT是否会触发越狱攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZIk8mKNRdDR63jfAbX3bPpTnvGibXmVIBEO9p0brxWs1klzCOAbnmsY4vNRQWYTGeDHj6YvZKruTA/640?wx_fmt=png&from=appmsg)

图 3 多模态场景下的越狱攻击形式

* **鲁棒性：**评估MLLMs在分布漂移或输入扰动下的响应一致性。可细分为：

1)      OOD鲁棒性：MLLMs面对分布外数据的泛化能力，包括不同风格和不同应用。

2)      对抗鲁棒性：MLLMs面对对抗样本的鲁棒性，这部分直接继承了单一模态的对抗攻击方法，包括图像对抗样本、文本中的AdvGLUE、AdvGLUE++等。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZIk8mKNRdDR63jfAbX3bPp4qnzUEOibFicYm0lE8qjdhKvg12bV0XlMSLa4BDQgAdYbasj3AtsOa7w/640?wx_fmt=png&from=appmsg)

图 4 MLLMs在非目标图像对抗样本上的准确率对比，所有MLLMs面对对抗攻击都存在脆弱性

* **公平性：**模型输出不包含可能对任何用户群体造成不利影响的不公平或歧视性结果。可细分为：

1)      刻板印象：MLLMs中存在的根深蒂固的社会偏见，基于公开的面临歧视风险的人物图像设计了刻板印象分类、刻板用户查询等任务。

2)      偏见和偏好：模型的倾向是否会对特定用户群里不利或导致有偏见的结果。在该子维度上，MultiTrust基于Chi-square test量化MLLMs对不同的个人属性（如性别、年龄）的偏差，以及MLLMs面对纯文本问题和图像配对时是否倾向于表达模型的偏好。

* **隐私性：**MLLMs保护个人数据免受未经授权请求所窃取的能力。

1)      隐私意识：衡量MLLMs是否在工作流中检测个人信息的存在和隐私风险，如识别图像中是否有隐私信息、关于这类图像的问题是否涉及到隐私问题等。

2)      隐私泄露：衡量MLLMs保护服务中的个人信息不遭泄露的能力。该子维度的评估类似于LLMs红队策略中隐私泄露方面的提示词，但在MLLMs中结合了图像作为视觉提示，检测模型是否会泄露个人身份信息等隐私。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZIk8mKNRdDR63jfAbX3bPp9GmMQKXqPFgr2RnRepVP7c5VsbQrsRFaaDFCDrIS0D98nxDSHiao80g/640?wx_fmt=png&from=appmsg)

图 5 隐私信息泄露评估

2.3

应用效果

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZIk8mKNRdDR63jfAbX3bPphgR4GfU5lq1wUeKdj2SS4EgEnI8Amhs2ziaic8TCLYc3KAexv5UhopCg/640?wx_fmt=png&from=appmsg)

图 6 多个MLLMs的可信度排名[3]

MultiTrust团队在21个MLLMs上进行了大规模实验，并得出以下关键结论：

* 开源MLLMs在可信度方面不如闭源MLLMs，这一点主要是因为闭源模型往往设有安全护栏并进行了安全对齐加固。
* 多模态训练以及模型推理过程中引入图像模态都会给MLLMs的可信度带来风险，例如，在输入中添加不相关图像出现会导致MLLMs出现不可预测的风险行为。
* 在多模态大模型中采纳一些训练策略（如RLHF）或模型组件（如新引入的视觉编码器）可以提高可信度，但仅对可信度的某些方面有效，在其他方面则可能会造成损害，如RLHF可能会由于数据质量问题给模型带偏见。

三、结语

多模态模型的安全性是一个复杂且日益重要的议题，涉及模型在融合多种模态信息时推理和预测结果的可靠性和安全性。多模态大模型的安全将会受到广泛关注，而安全评估作为这一领域无法绕开的重要方向，其研究也将迎来广阔的发展前景。多模态大模型的安全评估发展方兴未艾，当前的研究成果依然有着广阔的进步空间，例如，在图像、文本、音频等单一模态的安全风险评估上，应当增加安全威胁的丰富度和精细度，覆盖多种应用场景下的模型窃取、后门攻击、隐私泄露等攻击类型；在多模态风险评估方面，可以扩展到评估模态融合和模态对齐策略对多模态模型安全的影响，设计和构建跨模态的多样化评估数据集，为不同的风险类型建立对应的评估指标。随着技术的持续进步和应用的不断拓展，多模态大模型的安全评估将成为备受关注的热点，多模态大模型安全评估的标准化与规范化工作将得到逐步推动，最终促进多模态大模型在各个领域的应用和发展。

参考文献

[1] Zhang Y, Huang Y, Sun Y, et al. Benchmarking Trustworthiness of Multimodal Large Language Models: A Comprehensive Study[J]. arXiv preprint arXiv:2406.07057, 2024.

[2] https://github.com/thu-ml/MMTrustEval

[3] https://multi-trust.github.io/

内容编辑：创新研究院 杨鑫宜
    责任编辑：创新研究院 陈佛忠

本公众号原创文章仅代表作者观点，不代表绿盟科技立场。所有原创内容版权均属绿盟科技研究通讯。未经授权，严禁任何媒体以及微信公众号复制、转载、摘编或以其他方式使用，转载须注明来自绿盟科技研究通讯并附上本文链接。

**关于我们**

绿盟科技研究通讯由绿盟科技创新研究院负责运营，绿盟科技创新研究院是绿盟科技的前沿技术研究部门，包括星云实验室、天枢实验室和孵化中心。团队成员由来自清华、北大、哈工大、中科院、北邮等多所重点院校的博士和硕士组成。

绿盟科技创新研究院作为“中关村科技园区海淀园博士后工作站分站”的重要培养单位之一，与清华大学进行博士后联合培养，科研成果已涵盖各类国家课题项目、国家专利、国家标准、高水平学术论文、出版专业书籍等。

我们持续探索信息安全领域的前沿学术方向，从实践出发，结合公司资源和先进技术，实现概念级的原型系统，进而交付产品线孵化产品并创造巨大的经济价值。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

绿盟科技研究通讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

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