---
title: 当风云卫拥抱DeepSeek发生了哪些（一）：DeepSeek-R1安全告警分析实测获三高
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247498313&idx=1&sn=97e0013935397b2178344e07ef2d1095&chksm=e84c5c96df3bd58026d9eeba03737a7b481bddc08ffb23869f47f9d4f3195d66ed6f427de1c1&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2025-02-14
fetch_date: 2025-10-06T20:36:18.960970
---

# 当风云卫拥抱DeepSeek发生了哪些（一）：DeepSeek-R1安全告警分析实测获三高

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUaqIIz3dvSERULQoC2VaKyWJe3o6272tGn7UamwREKERXKCR3hib5BAkkwWZs5k4z9DJw5GzCjslog/0?wx_fmt=jpeg)

# 当风云卫拥抱DeepSeek发生了哪些（一）：DeepSeek-R1安全告警分析实测获三高

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUaqIIz3dvSERULQoC2VaKyWxPczwWMg0iaj9J8bWyJnwsVWFuGXrqMCtwlwQcB6r2vK9ib1ILbHj2eg/640?wx_fmt=gif&from=appmsg)

一.  前言

DeepSeek-R1作为由深度求索公司自主研发的国产通用人工智能大模型，自发布以来便备受瞩目。凭借在多项核心评测基准中的优异表现，DeepSeek-R1展现了强大的语言理解、逻辑推理和知识应用能力。

在安全运营领域，海量的告警信息给安全分析人员带来了巨大的挑战。本文将聚焦安全运营中的告警分析场景，基于DeepSeek-R1进行告警分析评测，以评估其实际应用价值。

二.  测试方法

本测试在DeepSeek-R1原版完整模型上进行。

我们在现有告警数据上进行三轮抽样，每轮抽样75条真实攻击告警和25条非攻击（误报）告警，要求DeepSeek-R1对告警的真实性和攻击结果进行分析。每轮测试中使用的prompt亦略有差异，以考虑不同的安全运营场景。

原始告警数据来自多个现实网络环境的多种探针设备，并由人类专家进行了标注。提供给模型的告警信息经过基本的预处理，包括协议字段解析、常规解码和解压缩等，以便于模型进行分析。

三.  综合结果

经与人工专家标注对比，DeepSeek-R1和风云卫在告警分析测试成绩统计如下：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaqIIz3dvSERULQoC2VaKyWWTUrbnxKDfaP51hSG9GGibQWHbhGYD0ib2schw6cictVYDBWREtqKrt7w/640?wx_fmt=png&from=appmsg)

表1：告警分析测试成绩统计

特别需要指出的是，三轮测试中合计225条真实攻击样本无一漏报。即使考虑到预处理过程降低了告警分析的难度，这依然是此前测试过的所有公开LLM都未曾达到过的水平。由此认为DeepSeek-R1对于真实攻击具有非常优秀的检出能力。

但反过来讲，目前测试中全部41个分类错误均是将非攻击行为误判为真实攻击。由此统计DeepSeek-R1对于非攻击告警的整体误报率高达54.67%。考虑到当前普遍存在的告警疲劳问题，这么高的误报率以实际安全运营场景来说是难以接受的。

通用领域LLM似乎普遍具有高估告警危害程度的倾向，这一点在此前对于包括OpenAI的GPT-4o在内的各个LLM进行测试时均有体现，并非DeepSeek-R1特有的问题。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaqIIz3dvSERULQoC2VaKyWSoZ4IQ8YFOEvGicJqFA91JgflZ2zDThPI1icL5oB3XjyhwkXf5aP7GSg/640?wx_fmt=png&from=appmsg)

表2：对通用LLM“高估告警危害”问题的量化分析（与DeepSeek无关，仅供参考）

不过，这个问题按理说并不难解决。我们已经在绿盟风云卫模型上进行了验证，只要对模型进行恰当的微调，通常可将单一环境误报率抑制到1%以下，最终取决于具体环境中业务构成的复杂程度。

四. 运行性能和开销

作为高准确率的代价，DeepSeek-R1的运行开销非常大。

以本次测评中的统计，调用DeepSeek-R1对单个告警进行分析的平均耗时高达32.03秒，同样远远超出迄今为止测试过的所有LLM。作为参考，同等条件下，目前单卡部署的绿盟风云卫模型的平均耗时远小于十分之一。

除了模型本身的体积庞大之外，较为关键的一个因素是，作为一个内置思维链（CoT）的模型，DeepSeek-R1的推理输出中总是会包含非常长的“思考过程”。

即使测试中的prompt要求模型在有效输出中包含人工梳理的分步推理流程（并因此导致有效输出部分并不简短），DeepSeek-R1模型内置的CoT仍然占据了总输出长度的67.71%，比有效输出部分的两倍还多。

有些极端案例中，DeepSeek-R1甚至在CoT中就已经包含了一份符合预期格式的完整结果，然后又在有效输出部分中将同样的内容整个重新抄了一遍，导致了较多不必要的算力开销。

由此认为，要对所有告警都运行完整的DeepSeek-R1模型进行分类，在成本上恐怕是难以接受的。要将DeepSeek模型用于告警分析实战，我们需要探索结合小模型甚至传统规则的综合告警分析方法，而不能完全依赖单个LLM解决所有问题。

五. 对正确预测的分析

在付出了巨大的开销之后，内置CoT对告警分析的深度产生了显著的提升。即使是包含高度混淆代码的攻击载荷，DeepSeek-R1有时也能予以较为正确的分析。

例如，某WebShell文件上传攻击的原始请求节选如下，可见其中的WebShell内容经过混淆：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaqIIz3dvSERULQoC2VaKyWA9o6ianrWFvm4nuN7koEoPpetuqXiaQmFKpEgfiaoGK0UhsUaWmGkogog/640?wx_fmt=png&from=appmsg)

而DeepSeek-R1模型给出的CoT节选如下：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaqIIz3dvSERULQoC2VaKyWHB0pEPia0I7kBOkvymg5rAfgMsv8qnG7JAcAIAmCN2uicpnnQq3FxPYw/640?wx_fmt=png&from=appmsg)

我们以默认参数对上述告警重复运行了10次模型，其中有6次能够针对混淆部分给出完全正确的分析，有2次虽然结论正确但分析过程有误，另有2次未能完成反混淆分析。尽管如此，DeepSeek-R1在未经微调的情况下就达到如此成绩，已经难能可贵。

这种深度分析能力在相当程度上确保了对攻击行为检测的高覆盖率。只不过，要兼顾性能考虑，如何能让小模型具备类似程度的能力，蒸馏模型的性能能否达到预期，还有待进一步研究。

相比之下，绿盟风云卫额外附有专门的攻击载荷反混淆模块以应对复杂告警的分析，后续可以考虑和深度分析互相补足。

六. 对错误预测的分析

不过CoT也并非包治百病。长期以来，LLM应用经常受到幻觉问题困扰，这在告警分析任务中主要表现为凭空捏造攻击特征，或者强行将正常业务内容认定为攻击特征。

这种幻觉现象在此前评估的各个LLM均有出现，而在DeepSeek-R1的CoT中则体现得更加明显，例如：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaqIIz3dvSERULQoC2VaKyW9CMlWviat9TOQn8x7ePddrDK5bLiaSSnbu8VFicTkt3x8F4F8GMyH3o2A/640?wx_fmt=png&from=appmsg)

可见，明明没有找到任何攻击特征，模型却将其判断为真实攻击。本次测试中绝大多数的误报用例都包含类似情况。

现有的相关研究也表明，推理增强型的LLM相比常规模型更容易产生幻觉：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaqIIz3dvSERULQoC2VaKyWS75e3t0q5uVNp6zWCzcGzuSehrz1ADdiaWHWrqocUcJ8ZwejibVQbUNg/640?wx_fmt=png&from=appmsg)

图1：DeepSeek-R1与V3模型的幻觉测试对比，可见R1模型的幻觉现象尤为严重[1]

要想充分发挥DeepSeek-R1的优势，真正落地应用到安全运营场景中，我们可能需要引入系统化的外部方法来抑制模型的幻觉问题。

七. 其它发现

即使不考虑分类准确率，前置CoT也使得有效输出部分变得更加精炼。

此前包括GPT-4o在内的模型测试中，LLM总是在告警分析的输出中包含大量与分析结论无关的垃圾内容。以往的应用实践中，我们通常通过添加自我修正步骤（即要求LLM对自己输出的分析结果进行一次检查修订）来缓解该问题。

DeepSeek-R1虽然也会产生类似的垃圾内容，但其CoT机制使得这些垃圾内容被隔离在“思考过程”之内，而不向最终用户呈现。虽然与传统方法没有本质上的区别，但流程上还是得到了简化。

八. 后记和展望

本次评测着重评估了DeepSeek-R1在安全告警分析场景中的能力表现，揭示了其显著优势与亟待改进的短板。虽相较于绿盟风云卫展现出更高的覆盖率，但也同时面临误报率偏高和性能开销过大的问题。尤其DeepSeek-R1内置思维链（CoT）机制使其能够深度解析复杂攻击载荷，在真实攻击检测方面展现了卓越的准确率。然而，高误报率和高运行开销严重制约了其直接落地的可行性。

展望未来，以下方向值得进一步探索：

1、模型轻量化与优化：通过知识蒸馏或模型剪枝技术压缩模型规模，降低算力开销；优化模型推理流程，压缩CoT输出长度；针对性微调模型以期减少误报。

2、构建综合分析框架：整合AISecOps体系，结合外部知识库、资产信息、威胁情报等，由轻量模型或规则引擎完成初步筛选，仅对疑难情况调用大模型进行深度分析，从而平衡效率与精度。

尽管当前DeepSeek-R1尚未达到直接替代传统安全分析工具的水平，但其在复杂攻击检测方面的潜力已不容忽视。通过技术迭代与工程优化，我们期待其成为下一代智能安全运营体系的核心组件之一。

如果您发现文中描述有不当之处，还请留言指出。在此致以真诚的感谢。

参考文献

[1]Forrest Bao,Chenyu Xu,Ofer Mendelevitch. DeepSeek-R1 hallucinates more than DeepSeek-V3, 2025[Z/OL]. (2025). https://www.vectara.com/blog/deepseek-r1-hallucinates-more-than-deepseek-v3.

内容编辑：创新研究院 吴复迪
    责任编辑：创新研究院 舒展

本公众号原创文章仅代表作者观点，不代表绿盟科技立场。所有原创内容版权均属绿盟科技研究通讯。未经授权，严禁任何媒体以及微信公众号复制、转载、摘编或以其他方式使用，转载须注明来自绿盟科技研究通讯并附上本文链接。

**关于我们**

绿盟科技研究通讯由绿盟科技创新研究院负责运营，绿盟科技创新研究院是绿盟科技的前沿技术研究部门，包括星云实验室、天枢实验室和孵化中心。团队成员由来自清华、北大、哈工大、中科院、北邮等多所重点院校的博士和硕士组成。

绿盟科技创新研究院作为“中关村科技园区海淀园博士后工作站分站”的重要培养单位之一，与清华大学进行博士后联合培养，科研成果已涵盖各类国家课题项目、国家专利、国家标准、高水平学术论文、出版专业书籍等。

我们持续探索信息安全领域的前沿学术方向，从实践出发，结合公司资源和先进技术，实现概念级的原型系统，进而交付产品线孵化产品并创造巨大的经济价值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUaqIIz3dvSERULQoC2VaKyWULiamum0I7IickwbxPI2BmYWYnPOsV512Y2micGEp69cS4aSibcu8sTYYQ/640?wx_fmt=jpeg&from=appmsg)

**长按上方二维码，即可关注我**

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