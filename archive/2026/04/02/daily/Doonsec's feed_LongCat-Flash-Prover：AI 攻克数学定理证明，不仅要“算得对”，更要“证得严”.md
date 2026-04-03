---
title: LongCat-Flash-Prover：AI 攻克数学定理证明，不仅要“算得对”，更要“证得严”
url: https://mp.weixin.qq.com/s/hZUVVkUW0n8_KVV3924ifw
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:23:52.908024
---

# LongCat-Flash-Prover：AI 攻克数学定理证明，不仅要“算得对”，更要“证得严”

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/V95GN2mm0DyPYwNRic47LJvsswL5FAy2u8gHWwovKEwymgDwExoNaMOUicrXMoFaQaFos0ZTjb5sKAqRdcGKPxRp3jTZtD6dtQfSJHPJHB1yM/0?wx_fmt=jpeg)

# LongCat-Flash-Prover：AI 攻克数学定理证明，不仅要“算得对”，更要“证得严”

龙猫LongCat
龙猫LongCat

美团技术团队

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohY774aH6DHLYx85WNTJKc9wWmhwOPcq5E8LgWiat3NNVCh6wGc4FpZO7DrhBSyDqPzI6ia02JzQF085EmxnE7NRvHlibYS7uxNWw/640?wx_fmt=png&from=appmsg#imgIndex=0)

现如今的大语言模型已经能流畅地写文章、写代码，甚至执行复杂的Agent工作流，然而，它们在面对严谨的数学定理证明时，却往往显得力不从心。

在常规的数学解题中，模型只需要“答对最终数值”即可，但数学定理证明不同，它要求极度严苛的逻辑链条，任何一句自然语言的模棱两可，都可能导致整个证明的崩塌。那么，如何让 AI 从“猜答案”走向“严谨证明”，成为复杂推理具有挑战的课题。

为了解答这个问题，我们开源了专门用于数学形式化与定理证明的模型 —— LongCat-Flash-Prover。

LongCat-Flash-Prover在解决定理证明和形式化任务时，将形式化推理拆解为自动形式化（Auto-Formalization）、草稿生成（Sketching）和证明生成（Proving）三大原子能力。在结合工具集成推理（Tool‑Integrated Reasoning，TIR）策略下，**仅用 72 次推理预算，MiniF2F‑Test 通过率就达到 97.1%**，在已知开源 Prover 模型中刷新 SOTA；在超难竞赛级任务上，**MathOlympiad‑Bench 达 46.7%（180 次预算），PutnamBench 达 41.5%（118 次预算），同样超越现有开源模型。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaogyr2T2DgibGn6pvYmpyDXnj1Yk5DBic0QnExGB8vr45YHK5ZHw3XMVKbMYjHR5suMAxmwTogRnxFZAQyibqaVaFs0I5pg0KEB6BA/640?wx_fmt=png#imgIndex=1)

目前LongCat‑Flash‑Prover已全面开源，欢迎使用：

GitHub：

<https://github.com/meituan-longcat/LongCat-Flash-Prover>

Hugging Face：

<https://huggingface.co/meituan-longcat/LongCat-Flash-Prover>

Report：

<https://github.com/meituan-longcat/LongCat-Flash-Prover/blob/main/LongCat_Flash_Prover_Technical_Report.pdf>

让我们感到惊喜的是，模型在开源后几日内，不仅受到了AI和大模型研究者们的关注，更引起了数学界的关注。发布当日，我们便收到了国内顶尖高校的合作邀请，共同探讨基于该模型开发形式化证明 Agent 的可能性。我们期望借此将现有的数学教材和前沿论文“翻译”成形式化语言，进一步充实形式化数学的知识底座，为整个数学研究领域的范式创新提供助力。这让我们深刻意识到：AI 在定理证明上的突破，不再仅仅是算法跑分，而是真正开始成为基础科学研究的“基础设施”。

因此，今天，我们想和大家分享 LongCat-Flash-Prover 背后的故事和技术栈。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaogJl9X76xrNoQW7HAVCNKG7XicNWTx0zwQ4YJnWqVuJRDjGaSicC4eicsuNnJvarAic6dmOJpuBkQEePIXToiaJhLJIok3xHOic1HBJ8/640?wx_fmt=png#imgIndex=2)

自然语言天生带有模糊性，很难进行步骤级的严谨性验证，为了解决这个问题，数学家和计算机科学家们引入了形式化语言（如 Lean4）。

你可以把 Lean4 理解为一种“数学编程语言”。就像 Python 代码可以通过编译器执行一样，用 Lean4 写出的数学证明，可以通过编译原理进行逐行校验。只要模型能写出语法正确、逻辑严谨且能通过 Lean4 编译器验证的代码，就意味着这个数学定理被 100% 严谨地证明了。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaogvz1r7m149CkiaZSnjBrWYEDhlGBH6D3FPlqclgcmEJ27Xc0xPNLQ90Pju1jACVMm7iaeBa0W7to3Kf7aicdXZr88icicIcZLPlWjM/640?wx_fmt=png#imgIndex=3)

教 AI 证明定理，就像教一个数学系新生，不能指望它一眼看穿答案，而是要教它拆解步骤。我们将 AI 的证明过程拆解为三个基础的形式化推理原子能力：

1. **自动形式化（Auto-Formalization）——“翻译题目”：**先将自然语言描述的数学问题，精准翻译成 Lean4 计算机能看懂的形式化描述。
2. **草稿生成（Sketching）——“写解题大纲”：**面对复杂定理，不急于一步写完。模型会先写一个草稿，把大问题拆解成几个需要证明的小引理（Lemma），理清逻辑主线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaogT1s7vGc4OEXnT02DZYysCGsFw6BjQevb8RE40hz0EicHv36Wl4F1bNenCKYKJQh0cbiaKG3mDa9PPVvxqsIKIXx2qLkicfP41gk/640?wx_fmt=png#imgIndex=4)

3. 证明生成（Proving）——“补全细节”：沿着草稿的思路，一步步补全剩余的证明过程，完成逻辑推演。

为了让模型熟练掌握这三项技能，我们设计了一套结合**“工具集成推理（TIR）”的“混合专家迭代”**框架。简单来说，就是组合不同具备这些原子能力的专家模型，以单轮和多轮形式进行不断试错、自我纠正，从简单的完整证明，逐步过渡到复杂的“引理式草稿证明”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaojPKSxyhfNGWwTF1m7S8Ovq8E6TRMJMoBiaqlHs6Dso2BBjG0W56bkFEPCrB73xjBPWnGxwxhHJg5EDHhX5szPnhmNtytxZ8uc0/640?wx_fmt=png&from=appmsg#imgIndex=5)

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojGuJhqHufQgictupZoAuGntdPaD8uCJSDKO5GZrATCp21V5dCudL3XGS87IYg4YDicK6nfCED9JAFXWCs4engfcTgI4UVPYlLTY/640?wx_fmt=png#imgIndex=6)

在这个框架中，我们旨在结合不同的专家不断合成基于Auto-Formalization、Sketching和Proving这三个原子能力以及相互组合下的推理轨迹，并挑选高质量的数据来进一步提升相应专家模型的性能。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoh5ic5eKibOZZVXssaIPdPyPbhnaerQnIaajeeniccvhBhzfJQYB7eSPGavqoD69EhB4Vt6Z1Oib6m8HE1ia1FzuenPjulecnksWnkw/640?wx_fmt=png#imgIndex=7)

如上图，专家迭代主要包含两个阶段：

* **Cold-Start阶段：**我们首先利用团队在早期探索的基于 TIR 和 DPO 训练的Auto-Formalizer专有模型 ATF-32B用于合成Formal Statement。基于这些Statement，我们利用 LongCat-Flash-Thinking-2601 生成高质量的带有多个Lean4相关验证工具反馈的轨迹。基于这些合成数据，我们通过执行去污、去重和基于难度和多样性的采样，构建了一个高质量的冷启动数据集。由于不同的专家模型来自不同的模型族，我们应用领域混合 SFT 来整合这些功能，并得到最终的冷启动模型。
* **Iteration阶段：**在迭代阶段，我们选择冷启动阶段得到的模型作为新的专家模型。每个形式推理任务的轨迹都是基于这个新专家模型合成的。此外，我们还整合了大量通用数据，以确保模型具备非形式推理能力。每一轮迭代中，我们会进行SFT和RL训练，多次迭代之后则可以得到LongCat-Flash-Prover模型。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohJ0o6xK4WaRg6NnyjicKPGuib89TPKicazibCWS5u48vufr7tuNxuFI5tqOpshKaqPDQRThlibuYYhzKbEALdrnYfCD61oMviagiaJKQ/640?wx_fmt=png#imgIndex=8)

在数据合成过程中，如何组织这些专家进行协同是一个挑战。我们设计了如下图所示的工作流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaSl3Dq5V87DvWtcpicsfvVnLluyHfdY8c7nv3zribbfS8fN4VbrhiaZoNuP3AylHUR9EszQzUiancd3jEfYESyLFOyaWexzg8TXqk/640?wx_fmt=png#imgIndex=9)

每个专家模型都能同时生成单轮轨迹（不调用工具）和多轮轨迹（TIR 模式），从而确保合成数据的多样性。

为了使模型能够根据每个问题的难度动态选择合适的工具和证明策略，我们采用了一种课程学习方法：1）从单轮合成开始，然后是多轮调用工具合成；2）从生成完整证明逐步过渡到引理式草稿证明。

基本合成过程如下：

1. 首先给定一个Informal Statement（即一个自然语言问题），先用Auto-Formalization专家在单轮无工具条件下生成N个Formal Statement。我们使用Lean4 Server和语义一致性打分模型来对每个结果进行打分。当且仅当生成的Formal Statement没有语法错误且语义与Informal Statement保持一致的则被认定为正确；
2. 如果这N个Formal Statement包含正确的结果，则直接获取这些正确的Statement即可；如果全部错误，则激活TIR模式，通过结合Lean4 Server和语义一致性打分模型两个工具来不断修改，直到能生成正确的为止；
3. 基于生成好的Formal Statement，我们接下来使用Prover模型尝试生成证明。我们先使用Whole-Proof模式来一次性给出完整的证明过程，同样我们生成N个结果，并使用Lean4 Server和Theorem一致性来判断模型生成的证明是否通过。其中，Theorem一致性是为了避免模型伪造或修改原始证明目标从而导致Hacking问题；
4. 如果生成的N个Whole-Proof没有正确的，那么我们激活Whole-Proof的TIR模式，借助Lean4 Server和Theorem一致性打分工具的反馈信息帮助模型修改Proof；
5. 如果Whole-Proof模式下不论使用单轮还是TIR都无法被证明（通常是一些复杂的问题，或者需要超过1000行证明过程的问题），我们则开启Sketch-Proof的策略；
6. Sketching中，给定一个Formal Statement，SKetcher专家模型先生成N个Sketch，每个Sketch包含多个待证明的Lemma，以及一个Main Body，我们同样采用TIR模式来帮助模型生成语法和Theorem一种的Sketch；
7. 对于每个Sketch，我们再次使用Prover专家模型对每个Lemma进行Whole-Proof模式的证明，整个证明过程均使用TIR模式。

基于这些合成轨迹，我们进行了一些数据处理、多样性采样和难度控制，从而可以获得SFT模型。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaogia1YbpOuT64wJFZtusl14ibavGzXUJskVcFibJZaGn8q1x0O565POCaCNgjnXCzNaiaiafUsZjIFgTQbNTYlAoVliauWaMibhqcNc9Q/640?wx_fmt=png#imgIndex=10)

我们的专家迭代框架和RL训练框架中，共享相同的一套智能体工具。

1. Lean4 Server：我们部署了Lean4 Server并作为验证生成的Formal Statement、Sketch和Proof的语法是否准确。相比于之前工作直接将Lean4 Server的JSON格式作为反馈信息，我们对其进行了处理：通过将完整的Proof中插入锚点，即直接告诉模型错误代码片段，而非简单的行列坐标，这样可以避免模型错误判断错误代码的位置，提高纠错的准确性；
2. 语义一致性：只靠Lean4 Server可能会存在Hack问题，例如模型为了生成语法正确的代码而修改原始问题。为此，我们通过LLM-as-a-Judger的手段，验证模型生成的Formal Statement与原始问题是否语义一致。
3. Theorem一致性：在模型生成Sketch或Proof时，需要确保模型的Theorem证明目标不能被篡改，一些微小的符号变化可能会导致整个证明问题发生改变。我们采用基于规则的方法来约束模型不能修改原始证明目标；
4. Legality验证：我们观察到大约9种存在作弊的Proof行为，这些证明过程通常尝试修改Formal Statement、插入提前终止符“#exit”、插入不存在的公理或无法证明的假设、通过添加macro, elab, syntax, notation尝试绕过编译错误等手段企图达到Lean4 Server给出证明通过的反馈。通过引入Legality验证，可以极大地避免模型出现Hack问题。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojDCq39Ln4mmOgcVfv00aSx4xKLeNmHcGV8zt2orQiaSgRibIHCiaibJmibwotNSVInkP5P2RZ7icJQ019iavZ29Y1AqCNic6eXQOyVnAg/640?wx_fmt=png#imgIndex=11)

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoiaQ8Wyibw4eaoh6pjgBkrjc3SxpqXAib8FOWZcCKuPadL8RGQvmicQWLxCm3KvrzCvKicgN36k50xeg4LCv2ydf85RIoCKibFlzSM7Q/640?wx_fmt=png#imgIndex=12)

Prover在RL阶段训练使用TIR模式，我们基于LongCat-Flash-Thinking所使用的DORA训练框架进行。

在训练过程中，我们观察到MoE两个影响模型稳定性的因素，训推一致性问题以及Staleness。对于训推Diff，我们通过评估新旧策略模型在训练引擎与推理引擎上关于重要性采样比（Important Sampling Ratio，IS Ratio）的估计来衡量训推一致性。相比GRPO而言，我们除了将Sequence-Mean-Token-Mean调整为Token-Mean以外，我们主要引入分层的Masking策略来直接消除不稳定Token的梯度贡献：

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohiauiceibNlOF2Y4f0VcibOhh3iarEicdvXBghG7eZT3QjdibgVzWhrOwS1yZvfcdYAsDR6PibTyibS5nJPib86IowP4YF7C1fevtcWKuqQ/640?wx_fmt=png#imgIndex=13)

* 序列层面Masking：我们首先通过计算所有Token的IS Ratio的几何平均值来估计序列级的训练-推理Diff。对于整个序列，如果Diff超过一定范围，则认为其对训练稳定性有显著影响，并将移除该序列的梯度贡献。该策略旨在仅考虑序列级的训练-推理一致性度量，避免过度忽略有价值的标记。
* Token层面Masking：对于剩余的序列，我们将移除具有显著训推不一致性的Token，以确保剩余标记不会因训练拉取不一致性而影响稳定性。
* Token层面Staleness控制：对于经过序列和Token层面的Masking处理后所保留的Token，我们再考虑标准的Clipping操作，用于控制Staleness，以确保更新幅度限制在一定范围内，从而保证训练稳定性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaS4lIS9RrQaTeJ8iamwhFfDBlkicdsayVPbjTyUVQc8Yl3mpzWC5yLCZb4TcknmGpib38uw274JvIXicuCuC8tM6SJxdkjwVG1IuQ/640?wx_fmt=png#imgIndex=14)

在训练过程中，我们观察到了一个非常有意思的现象：**AI 为了得到高分，学会了“作弊”。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohhHTUkibgMARoUrMSwGrDfy8nhysV9YczoibjnRxwPnLJhibaufUxxHFVap8uImGOY3ibMv0s0CWzQRRO6HLMDm9pEtmkxZSeWFhM/640?wx_fmt=png#imgIndex=15)

如果仅仅依赖 Lean4 编译器作为裁判，模型有时会通过修改原始题目、插入提前终止符...