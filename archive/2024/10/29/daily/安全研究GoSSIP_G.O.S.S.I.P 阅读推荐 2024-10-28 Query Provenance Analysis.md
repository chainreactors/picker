---
title: G.O.S.S.I.P 阅读推荐 2024-10-28 Query Provenance Analysis
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499071&idx=1&sn=a6a9fad5adf1abe00646e49cae902683&chksm=c063d3e6f7145af08b042eb2f55fdbea86e580f33975d60492809716ce1d535db75ba5f8d1dc&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-10-29
fetch_date: 2025-10-06T18:51:33.139698
---

# G.O.S.S.I.P 阅读推荐 2024-10-28 Query Provenance Analysis

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GNqP1cJnp2Q9ZrL9PWwaUjwjdm9pw6IJ3Gz6ibNE6hYda8Vph6MwVnuGhf2BibibJC1Pxws3PaqSiaTQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-10-28 Query Provenance Analysis

Shaofei@PKU

安全研究GoSSIP

新的一周开始了，今天我们介绍北京大学计算机学院操作系统实验室完成并投稿的，关于使用溯源分析技术（Provenance Analysis）保护深度学习模型的工作**Query Provenance Analysis: Efficient and Robust Defense against Query-based Black-box Attacks** ，这项工作已经被S&P 2025接收。该工作深入研究了针对云端模型的黑盒攻击（Query-based Black-box Attacks），发现了现有检测与防护技术的本质缺陷，进而提出了一种基于查询溯源分析的高效且鲁棒的实时防御技术，QPA。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNqP1cJnp2Q9ZrL9PWwaUjNm72RLicWMXMicHhCyVwfFCwJtookphQ20o1fTRN7M3YnxspzleokpJA/640?wx_fmt=png&from=appmsg)

该论文研究了在云端模型易受黑盒攻击的情况下，如何保护模型安全。模型运营商将模型部署在云端，为用户提供服务。用户可以通过API向模型提交请求，并得到模型的返回结果，这些结果可以是分类任务的最终标签或标签的概率分布。攻击者可以利用这些返回结果的信息，对请求进行微调，经过多轮迭代后，生成针对该模型的对抗样本，从而对模型安全构成重大威胁。为了保护模型免受黑盒攻击，研究者们提出了状态防御模型（Stateful Defense Model，SDM）。他们发现黑盒攻击的查询具有很高的相似性，因此可以对模型的请求进行相似度审查。对于识别出的黑盒攻击查询，系统会拒绝返回模型的真实结果。这种防御方法会对每一个查询请求进行特征提取，并将这些特征存储到数据库中。当系统接收到新的查询请求时，会将其提取的特征与数据库中的历史查询进行相似度匹配。如果相似度高于一定阈值，则认为新查询属于黑盒攻击的查询序列，并直接拒绝服务。尽管研究者们不断改进特征提取算法，以提升SDM的性能和鲁棒性，但仍难以有效应对更具针对性的适应性攻击。本文发现，黑盒攻击的本质特征是攻击序列整体的相似性。基于这一观察，我们提出了基于查询的溯源分析技术（Query Provenance Analysis，QPA），为模型安全提供了更鲁棒、更高效的保障。

**适应性攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNqP1cJnp2Q9ZrL9PWwaUjPfpIvIgursohr6XQxC62c8rlzHptBS56QHfhYtoVzLvZ2LtHd2qvgg/640?wx_fmt=png&from=appmsg)

适应性攻击（Adaptive Attack）是攻击者为了降低查询间相似性，从而逃避SDM的技术。传统的适应性攻击可以被称为查询遮蔽策略（Query-blinding Strategy），该策略采用常见的图像变换技术，如旋转、平移和亮度调整，因此可以在不修改攻击算法本身的情况下轻松应用。然而，这种策略往往会影响攻击的效果，可能导致成功规避检测但攻击成功率降低。近期，CCS 23的一篇工作提出了更加复杂的适应性攻击策略Oracle-guided Adaptive Rejection Sampling（OARS）。它利用防御模型泄露的判别信息，可以感知模型的判别边界并自适应调整攻击参数以逃避检测。OARS利用二分搜索找到最佳步长和噪声分布，生成与之前查询最相似但不会触发SDM的查询。该技术可以对现有非适应性攻击算法进行微调，大大提升了攻击算法的成功率，并具有较好的泛用性。与查询遮蔽相比，OARS是一种高级的自适应攻击，它利用防御模型SDM泄露的判别信息自适应调整攻击方向，将对抗最新SDM的攻击成功率从几乎0%提高到接近100%，因此需要更鲁棒的防御模型。

**QPA框架**

作者认为导致目前SDM失效的原因是它们均依据“单点相似度”特征进行防御，即将新查询与历史数据库中所有查询计算相似度，取最高的相似度与预先设定的阈值相比较。但是这种判别逻辑很容易被攻击者感知并逃逸，攻击者可以通过启发式策略调整攻击的步长和方向，生成与之前查询最相似但不会触发SDM的查询，所以难以被现有SDM检测与防御。针对这个问题，本文提出了使用“序列相似度”作为黑盒攻击序列的本质特征，即黑盒攻击序列整体上具有的相似性难以被适应性攻击规避，尽管适应性攻击为了逃逸现有SDM检测可以弱化单点间的相似性，但为了使攻击尽快收敛，攻击序列中查询的产生仍然要以之前查询为基础，因此序列相似度依然存在。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNqP1cJnp2Q9ZrL9PWwaUjIkYy1icicJicIRN8KL6uYNKiav5sIdUjUN8VLAvMib9kKjUNY6cyCiaf41Sg/640?wx_fmt=png&from=appmsg)

基于“序列相似度”这一核心特征，本文提出了QPA方法。该方法通过相似度构建查询溯源图（Query Provenance Graph），并定期对其进行分析和检测。查询溯源图以查询为节点，边的属性为相似度值。在构建阶段，每当接收到新查询时，将其与最相似的历史查询相连。在分析阶段，通过基于统计和GNN的两阶段检测，筛选出异常的查询溯源图，并更新内存中的异常集合（Anomaly Set），将异常图中的节点加入异常集合中。在实时监测过程中，如果当前查询与异常集合中的历史查询最相似，则将当前查询判定为黑盒攻击相关的查询并加入异常集合。由于引入图结构会带来额外的性能开销，为保证防御系统的实时性，我们采取了动态管理策略，将可疑的查询溯源图存放在内存中，而其他低可疑的查询溯源图则存储在硬盘上的数据库中。

**实验与结论**

作者对传统非适应性攻击和适应性攻击的防御效果在四个数据集上进行了评估，并将QPA与最先进的SDM防御进行了比较，实验结果表明，QPA在非自适应和自适应攻击方面的防御鲁棒性和效率均优于基线方法。具体来说，QPA将OARS的攻击成功率（ASR）降低到4.08%，大约是基线方法的20倍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNqP1cJnp2Q9ZrL9PWwaUjoaqjwJS4TEgsmurKU1RH5BBUv20zSiaFTiaWvibGCmhsFsLicJoBlu25zw/640?wx_fmt=png&from=appmsg)

此外，QPA的吞吐量比基线方法高出最多7.67倍，延迟比基线方法低11.09倍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNqP1cJnp2Q9ZrL9PWwaUj7kTLsiaJ9taMiaLqcicQibwSaFb4V4rknGHafoN99qxpibhj6RKfTjubXgw/640?wx_fmt=png&from=appmsg)

作者还探究了QPA在相似正常查询、多攻击混合等真实场景下的鲁棒性，实验结果表明QPA可以有效检测出混合的黑盒攻击。对于相似的正常查询，QPA仅有0.23%的误报率，而基线方法BlackLight和PIHA 的误报率分别为31.68%和23.66%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GNqP1cJnp2Q9ZrL9PWwaUj8GxE7oqToUxPOEHHIGxYXGGiaDc1CACuPXqYibPribJ0XnLx44VpsQ0Fg/640?wx_fmt=png&from=appmsg)

**未来展望**

针对云端模型的黑盒攻击与防御是一个经典话题。本文针对传统的图像分类任务提出了新型防御机制。不同任务的模型有不同的输入类型和攻击方法，因此存在广泛的研究方向，如语音模型和大语言模型（LLM）等。作者认为，模型系统的保护可以分为输入层保护、模型保护和输出保护三部分。输入层保护是其中重要的一环，可以有效抵御基于输入的攻击，例如对抗性攻击和数据投毒攻击。通过在输入层引入精心设计的预处理步骤，可以提前识别和过滤掉潜在的恶意输入。在模型保护方面，研究者们探索了多种技术，包括对抗性训练和基于可信执行环境（TEE）的保护，以增强模型的鲁棒性和隐私性。至于输出保护，它关注的是如何确保模型的预测结果不被恶意利用。例如，通过引入差分隐私技术，可以在不泄露模型信息的前提下，发布模型的统计信息，从而保护模型。未来的研究可以进一步探索这些防御机制的优化和集成，以及它们在不同类型的云端模型和攻击场景下的有效性。此外，新的攻击手段和防御策略也将不断涌现，这要求研究者持续关注这一领域的最新进展，并开发出更为先进的保护技术。

论文链接：https://arxiv.org/pdf/2405.20641

代码链接：https://github.com/0xllssFF/QPA

投稿作者介绍：

李少飞，北京大学四年级博士，导师为陈向群教授、郭耀教授和李锭助理教授，研究领域包括APT攻击检测与溯源、系统安全和模型安全，已在S&P、NDSS、CCS等多个计算机领域国际顶级会议发表多篇CCF-A类学术论文。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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