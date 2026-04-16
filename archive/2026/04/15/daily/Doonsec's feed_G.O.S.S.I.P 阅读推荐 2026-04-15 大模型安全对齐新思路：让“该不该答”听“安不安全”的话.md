---
title: G.O.S.S.I.P 阅读推荐 2026-04-15 大模型安全对齐新思路：让“该不该答”听“安不安全”的话
url: https://mp.weixin.qq.com/s/tou4oDRl7aV2GuWX6QreFg
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:45:41.528152
---

# G.O.S.S.I.P 阅读推荐 2026-04-15 大模型安全对齐新思路：让“该不该答”听“安不安全”的话

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolV4sWWc1kMsVSVj3hEIHyNWZovicJ43icnYXCFMnFyFkmcT6dZ1r1KxcpamBTzgyfCS7jQWBYla9oOiajib7XyrE2UBGjUJ05gpPu0/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-04-15 大模型安全对齐新思路：让“该不该答”听“安不安全”的话

Haonan Zhang
Haonan Zhang

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

大家在使用ChatGPT、Qwen、Llama这些经过安全对齐的大模型时，一定遇到过这样的情况：问个“如何用菜刀切西瓜”被拒绝了，或者稍微换个说法就把不该说的话全说出来了。这两种现象在学术界被称为**over-refusal（过度拒绝）** 和 **jailbreak（越狱）** ，是当前安全对齐领域最核心的两个痛点。

更让人头疼的是，这两个问题不是独立的——它们之间存在一个看似无法打破的**trade-off**：让模型更保守，越狱减少了，但动不动就拒绝正常问题；让模型更开放，过度拒绝改善了，但坏人又钻空子了。现有的“向量操控”（vector steering）方法——通过调整模型内部表示来改变行为——本质上都是在调整“回答向量”的幅度（magnitude），这就好比拧水龙头：拧小了漏不了水，但也出不了水；拧大了水来了，但脏东西也进来了。这个trade-off，似乎是无解的。

来自浙江大学的研究团队发现，这个trade-off并非无解。他们的论文***LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment***已被**ACL 2026 Main Conference**录用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUN4dLK6zAmjKXCNNygdcDKwR8XCytD53wRia3EsIUXNdUqLTHTM7oWOtKPiaR9AjqSdaiaz8WwufA8MeRXndibnhY038QEubxhoXI/640?wx_fmt=png&from=appmsg)

## 问题的根因：两个判断向量正交

研究团队在模型内部提取了两个方向：**回答向量**（反映模型是否倾向于回答）和**良性向量**（反映模型对输入是否安全的判断）。他们发现，在几乎所有被测试的大模型中，这两个向量在各层之间的夹角都接近**90°**——近乎正交。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXJTyGSesdVF5NIc7Qp83VwMtiaYaLlCGqTk6dIZn97Wt1wibnjeD2TibU3Y245uLyRicm3J0mz9Ngj1cdJHx2ozWMeZ4Y6ibJbnE0c/640?wx_fmt=png&from=appmsg)

这一现象揭示了一个深刻的问题：**大模型把“要不要回答”和“输入是否安全”当作两个完全独立的过程在处理。** 于是，模型有时候“判断出输入是安全的，但就是不回答”（over-refusal），有时候“明明感知到了有毒输入，却还是回答了”（jailbreak）。两个决策互不知情，自然就会各自出错。

现有方法只调整的幅度，没有把“是否回答”和“是否安全”关联起来，所以无论怎么调，都逃不开这个trade-off。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolU3Z6aL29seXqoj9IKPCBFichha3KeLrWv1ocrjicepyZ6BRI2u7lY0bTpetAjkCX0NCmkmZ8avLINbuOnmYfbZhKlcZw70Er6H8/640?wx_fmt=png&from=appmsg)

## 解法：让“回答意愿”因果地依赖“安全判断”

LLM-VA的核心思想非常直接：**把对齐到的方向上**，让模型“要不要回答”的决策在因果上依赖“输入安不安全”的判断。具体分三步走：

**第一步：用SVM识别各层的控制向量。** 在每一层分别训练两个线性SVM，分别找到区分“良性/有毒”和“回答/拒绝”的最大间隔超平面，其法向量即为和。选择SVM的原因是它提供可解释的线性决策边界，间隔最大化保证了向量的鲁棒性。

**第二步：筛选与安全决策最相关的层。** 不是每一层都对最终的安全行为有同等贡献。LLM-VA用一个综合得分来选层：

其中衡量该层向量与最终残差流的对齐程度（影响力），衡量该层SVM的分类准确率。乘积形式确保选出的层**既有影响力又足够准确**，缺一不可。实验也验证了一个直觉：靠后的层对安全决策更重要，靠前的层则更多承载通用能力——修改前者伤害小，修改后者要小心。

**第三步：闭式权重更新完成对齐。** 不需要梯度下降，不需要微调，不需要改模型架构，直接用伪逆给出最小扰动的权重更新：

其中是归一化因子，确保良性输入在方向产生正投影、有毒输入产生负投影。由于修改某一层权重会影响后续层的有效向量方向，方法会迭代地重新提取向量并更新权重，大多数模型在20–30次迭代内收敛。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolVdSdDSkNMEgVALDicI0Tm8RYVzgJDaK9xfw71FkbGqNd79UfuViaATejDbvINIRCcibzI1RBiagicYrm3uWYSJ84MYtauKWQj9BGoE/640?wx_fmt=png&from=appmsg)

## 实验：12个模型，全面超越基线

研究团队在**12个主流开源指令微调模型**（涵盖Llama、Gemma、Mistral、Phi、Qwen五个系列，规模3B–14B）上进行了实验，覆盖jailbreak和over-refusal两类数据集，并与VectorSteer、AlphaSteer、SCANS等基线方法对比。

* **综合效果（F1）**：LLM-VA平均F1达0.77，比最优基线AlphaSteer\*\*相对提升11.45%\*\*，同时将越狱成功率（ASR）和过度拒绝率（ORR）分别降低了18.50%和22.00%。
* **通用能力保留**：在语法、自然语言推理、情感分析、数学（GSM8K）等6个benchmark上，LLM-VA平均保留了\*\*95.92%\*\*的原始能力，优于所有基线方法。相比之下，SCANS由于激进的幅度调整，通用能力平均损失达40.98%。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolULJMoib7nYqY8jYJ9YRUicnP7B7UQAhwhnia4jjaEvb6GN9ANKacBIpbyk4ejbUjHhnDOeTahcjhZQEiaTEEiaMKbtDWz930ojHA7U/640?wx_fmt=png&from=appmsg)

一个特别值得关注的现象是LLM-VA的**自适应性**：对于越狱风险高的模型（如Mistral-v0.3-7B，初始ASR高达81%），它会优先压制越狱；对于本来就过于保守的模型（如Llama-3.1-8B，初始ORR高达53%），它则优先缓解过度拒绝。这种自适应行为**完全来自向量对齐的内在机制**，无需为每个模型手动调超参数。

## 小结

LLM-VA提供了一个清晰的诊断：安全对齐的两难困境，根源不在于对模型的控制力度不够，而在于控制的**方向错了**。把“是否回答”和“是否安全”这两个本应深度耦合的决策对齐起来，才是正路。方法无需微调，无需改架构，只需要少量标注数据训练SVM，便可为不同家族、不同规模的模型一键提升安全性能。

> 论文：https://arxiv.org/abs/2601.19487
>
> 代码与权重：https://hotbento.github.io/LLM-VA-Web/

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