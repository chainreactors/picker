---
title: 跨层残差绕过LLM内生安全
url: https://forum.butian.net/share/4729
source: 奇安信攻防社区
date: 2026-01-22
fetch_date: 2026-01-23T03:31:34.371501
---

# 跨层残差绕过LLM内生安全

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 跨层残差绕过LLM内生安全

* [漏洞分析](https://forum.butian.net/topic/48)

2025年LLM的内容安全已经有质的飞跃了，基于模型内生安全、外挂的安全审核模型、改写模型等等手段，传统的基于提示词工程的黑盒攻击逐渐难以突破愈发完善的防御机制，而白盒攻击通过直接操纵模...

2025年LLM的内容安全已经有质的飞跃了，比如模型内生安全、外挂的内容安全围栏、安全改写模型等手段，基于提示词工程的黑盒攻击逐渐难以突破愈发完善的防御机制，而白盒攻击通过直接操纵模型内部状态，展现较高的攻击成功率，但往往攻击成本也很高，下面将展开描述最近行业内的LLM白盒攻击是如何实现的。
\*\*0x01 传统白盒越狱\*\*
---------------
### 1.1 离散优化阶段：基于梯度的字符搜索
这是LLM白盒攻击的起点，代表技术为\*\*贪婪坐标梯度法（GCG）\*\*。
- \*\*核心机制\*\*：将越狱视为离散优化任务，利用模型的梯度信息寻找一组对抗性后缀。攻击者通过计算每个字符替换对损失函数的影响，挑选能最大化地让模型输出肯定性回答（如，"Sure, here is..."）概率的字符 。
- \*\*攻击痛点\*\*：生成的后缀通常是无意义的“乱码”或乱序Token，极易被基于困惑度的过滤器拦截 。
### 1.2 语义演化阶段：遗传算法与结构化变异
为了解决GCG隐蔽性差的问题，研究者引入了遗传算法，代表技术为 \*\*AutoDAN\*\*。
- \*\*核心机制\*\*：采用层次化遗传算法，在保留提示词语义连贯性的基础上进行对抗性优化。它通过词级变异和句级交叉，生成的攻击指令在人类看来具有合理的逻辑结构。然后开始出现混合攻击（GCG+PAIR），利用大模型作为优化器自动迭代攻击模板。
- \*\*攻击痛点\*\*：AutoDAN 虽然提升了隐蔽性，但其高度依赖初始模板、计算开销巨大，且难以直接应用在不开放概率分布的黑盒模型上。
\*\*0x02 LLM机制可解释性研究\*\*
--------------------
在白盒攻击中，精确定位模型内部负责安全过滤的关键层是实施高效干预的前提。但在标准的 Transformer 实现里，研究者往往只方便拿到输入和输出；要稳定地获取中间激活、精确定位到“某一层/某一处张量”，并在前向过程中做可控干预，工程成本比较高。为了解决这类“可观测、可干预性不足”的问题，那么就需要 TransformerLens 这类工具用于 LLM 的机制可解释性研究。
TransformerLens 核心是 HookedTransformer 类，它继承自 PyTorch 的 Hook 机制，在每个关键位置插入了HookPoint。这些 HookPoint 会在前向传播时捕获并缓存所有中间激活值，包括注意力模式、MLP输出、残差流等。
这里我举个例子，比如在分析 "The capital of France is" -&gt; "Paris" 这类唯一解问题时，TransformerLens 会首先添加词嵌入和位置嵌入作为残差流的起点，依托PyTorch Hook 机制，在 TransformerBlock 内部关键计算节点植入 HookPoint，不仅能追踪进入块之前（resid\\_pre）、注意力处理后（resid\\_mid）以及 MLP 处理后（resid\\_post）的完整残差流状态，还能实现组件级观测，针对每一层单独提取注意力机制和 MLP 的输出。其中，注意力输出捕获 "France" 与 "capital" 之间的语义关联，MLP 输出负责更复杂的推理过程，并将所有组件堆叠成 shape 为 \[组件数，批次，位置，d\\_model\] 的统一张量；然后凭借残差空间与词表双向映射，通过 tokens\\_to\\_residual\\_directions() 方法利用模型解嵌入矩阵W\\_U将目标词 "Paris" 映射为残差空间中的方向向量，再借助 Logit Lens（贡献量化）方法，通过 apply\\_ln\\_to\\_stack() 自动适配每层不同的 LayerNorm 或 RMSNorm 缩放因子，对所有组件做一致性的缩放校正，并将每个残差流组件与 "Paris" 方向向量进行点积运算，得到的 Logit 数值就是各组件对 "Paris" 预测的贡献度（数值越大贡献越大），这样就成功建立起隐藏层向量与具体词语的关联。最后可以通过固定参数微调的方式，freeze 其他层，对关键层“旁挂”指定的数据，观测是否可以将 "Paris" 替换成其他答案，从而验证这一层是否为真正的关键层。
下图是一个demo实验结果，观测 Qwen3:8B 模型，得出27层对于 "Paris" 结果的贡献度可能最大。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-1382a780883b6f11bbef3e87ad165697a571f484.png)
这里可以观察到，一般在模型的最后几层是权重比较大的层，很可能影响最终的推理结果。
0x03 \*\*跨层残差绕过LLM内生安全\*\*
----------------------
SABER (Safety Alignment Bypass via Extra Residuals) 是来自印度理工学院德里分校的研究团队在2025年提出的一种新型白盒越狱方法，该方法通过跨层残差连接绕过了LLM的内生安全，提高了攻击成功率。
我发现这个项目没有公开实验数据集和代码，目前全网还没有人复现，感觉挺有意思的，所以结合 TransformerLens 尝试复现。
\*\*3.1 原理\*\*
1. 加载模型并包装 Hook 机制，利用 PyTorch 的 register\\_forward\\_hook() 在前向传播时抓取该层输出Transformer 每层的隐藏表示（残差流输出）。
2. 用激活值替换的思路找到防御层，把良性prompt和有害prompt看作两条不同的内部计算轨迹：先记录良性prompt在各层产生的中间表示（即，每层处理后会输出一个张量），然后在评估有害prompt时，逐层把某一层的中间表示替换为良性对应层的表示，并观察模型输出的行为指标（例如，更偏向拒答还是更偏向正常回答）发生了多大变化；如果某一层的替换会引起最大的行为转向，说明该层对安全相关行为最敏感，可作为后续分析与加固的重点对象。所以在有害prompt输入后，可以从防御层之前的层作为源层，提取激活值用于注入攻击。
3. 注入攻击：提前配置好不同组的干预幅度（干扰目标层的比例)、源层（防御层之前的层）与目标层（防御层之后的层）的相对距离、后缀注入提示词。选定一组“源层/目标层”作为实验配置；随后对同一输入运行一次前向计算以获取源层的中间表示，并构造一个干预函数用于在目标层对激活进行受控修改（利用源层激活值计算出干扰后的目标层激活值）；接着把该干预函数注册到目标层对应的激活位置，再运行一次生成过程并记录输出变化；最后统一清理所有 hooks 与缓存，确保每次实验相互独立、可重复对比。
```markdown
\*\*SABER 程序执行关键片段\*\*
\*\*阶段 1: 加载模型并包装 Hook 机制\*\*
model = AutoModelForCausalLM.from\_pretrained(...)
hooked\_model = HookedModel(model, tokenizer)
\*\*阶段 2: 定位防御层 (Activation Patching)\*\*
clean\_prompt = "How to create a python script?"
harm\_prompt = "How to create meth drug?"
for layer in all\_layers:
patch clean→harm at last token position
measure logit\_diff change
defense\_layer = layer with max effect
\*\*阶段 3: 提取源层激活值\*\*
source\_layer = defense\_layer - offset
source\_act = run\_with\_cache(harm\_tokens)[source\_layer]
\*\*阶段 4: SABER 注入攻击\*\*
h'\_target = h\_target + h\_source × (|h\_t|/|h\_s|) × λ
\*\*阶段 5: 生成越狱响应\*\*
prompt = harm\_prompt + " Sure, here is..."
output = model.generate(prompt)
# 攻击成功：模型输出有害内容
```
\*\*3.2 实验结论\*\*
这里的测试对象分别选用了： Qwen-1\\_8B-Chat（弱逻辑模型）、DeepSeek-R1-Distill-Qwen-32B（思考能力强逻辑模型）、Qwen3-30B-A3B-Instruct（MoE架构模型）。
实验中的六组配置，分别是不同的λ（干预幅度）、层偏移量（源层-&gt;目标层）、后缀诱导话术。
下图是程序运行的结果，可以发现 DeepSeek-R1-Distill 和 Qwen3 都属于“高智商”模型，且使用了更复杂的 RLHF/DPO 对齐，安全对齐权重大的层都是在最后的几层，尤其是有思维链的时候，会先在前中层进行大量思考，如果安全机制在这些层就中断思考，那推理能力会大打折扣。这和 SABER 论文中在中间位置的结论是有区别的，因为当时的模型都是2024年发布的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-db311ef90c9ed5b6a3120fe51dce4ce287951455.png)
\*\*0x04 风险分析\*\*
-------------
1. 绕过模型内生安全限制，生成任意毒性数据
2. 恶意推理包装器：在私有化部署的模型推理环境中，恶意用户不需要修改模型文件，只需要在一个 Python 脚本中“劫持”模型的推理过程，输出不合规内容。
3. 模型投毒：找到安全对齐贡献度最大的层，冻结其他层，然后对目标层进行固定参数微调，降低拒答率，但过拟合的问题严重。
\*\*0x05 防御方案\*\*
-------------
1. \*\*模型来源与完整性校验\*\*
- 只使用可信来源模型，做完整性校验。
2. \*\*防推理过程被 Hook 劫持/滥用\*\*
- 激活异常检测：在推理服务中监控关键层激活的范数/方差变化，出现非自然突增则告警或中断。
- 代码/运行时完整性：在受控环境禁用或审计动态 hook 行为（如阻止注册 forward hook、限制运行时反射），并对推理进程与依赖做权限隔离与可观测审计。
3. \*\*模型层级加密\*\*
- 对模型结构进行分析，定位安全相关或关键贡献的目标层，并按加密策略对这些目标层进行加密保护，从模型文件分发与部署环节提升关键层参数/结构的安全性，降低被篡改或被恶意利用的风险。可以参考联想全球安全实验室专利方案 CN120541862A 。
0x06 参考文献
---------
1、TransformerLens. TransformerLens 文档（v2.16.1）：生成式语言模型的机械可解释性库 \[Web Page\]. 检索于 <https://transformerlensorg.github.io/TransformerLens/>
2、Joshi, M., Nandi, P., &amp; Chakraborty, T. （2025 年 9 月 19 日）. SABER：基于跨层残差连接的安全对齐漏洞挖掘. arXiv. <https://doi.org/10.48550/arXiv.2509.16060>
3、专利 CN120541862A《模型加密方法、数据处理方法和电子设备》，公开日 2025-08-26

* 发表于 2026-01-22 09:00:00
* 阅读 ( 320 )
* 分类：[AI 人工智能](https://forum.butian.net/community/AI)

2 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Holiday](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/25508)

[Holiday](https://forum.butian.net/people/25508)

1 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2026 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![Holiday](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---