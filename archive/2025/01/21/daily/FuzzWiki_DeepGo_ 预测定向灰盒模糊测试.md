---
title: DeepGo: 预测定向灰盒模糊测试
url: https://mp.weixin.qq.com/s?__biz=MzU1NTEzODc3MQ==&mid=2247486916&idx=1&sn=6c5e8170932409049927f3b79468ae99&chksm=fbd9a678ccae2f6e581227dcdcc23e37f5f45c8fddefd134ce6a27c2a5563c29dc7126637abb&scene=58&subscene=0#rd
source: FuzzWiki
date: 2025-01-21
fetch_date: 2025-10-06T20:12:48.187482
---

# DeepGo: 预测定向灰盒模糊测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIaJwYYkgZtCzeluYicl5Gj2KXXwvDD2kiap62oUOb96arftjicmNhxyblA/0?wx_fmt=jpeg)

# DeepGo: 预测定向灰盒模糊测试

FuzzWiki

FuzzWiki

![](https://mmbiz.qpic.cn/mmbiz_gif/JchE46RGRlr92CPaC2cSiaTUCEWwOd0OucLNLlY09jGCso4gTL4BmXsBNsvOlSMv9qPopLaecg7r21KD4gBERqA/640?wx_fmt=gif)

**基本信息**

**原文名称：**DeepGo: Predictive Directed Greybox Fuzzing

**原文作者：**Peihong Lin; Pengfei Wang; Xu Zhou; Wei Xie; Gen Zhang; Kai Lu;

**原文链接：**https://www.ndss-symposium.org/wp-content/uploads/2024-514-paper.pdf

**发表期刊：**Network and Distributed System Security (NDSS) Symposium 2024

**一、引言**

定向灰盒模糊测试是一种能高效测试目标代码区脆弱性的技术。通过定义一个可测量的适应度量，定向灰盒模糊测试器可以选择有前途的种子，并给它们更多的突变机会来逐渐接近目标代码区域。

然而，以往定向灰盒模糊测试的启发式方法通常依赖于历史执行信息，对尚未执行的路径缺乏远见。例如，当使用到目标的基本块级距离作为适应度量时，对于较短距离的种子优先考虑而不考虑路径的可行性，因此，那些具有复杂约束的难以执行的路径会阻碍定向灰盒模糊测试器到达目标站点，使定向灰盒模糊测试器效率降低。

因此，作者提出了一种预测定向灰盒模糊测试方法DeepGo以解决上述问题，在如下几个方面做出了创新：

(1) 首先，作者提出了路径转换模型，该模型将定向灰盒模糊测试建模为通过特定的路径转换序列到达目标站点的过程。基于路径转换模型，作者使用序列奖励作为适应度量，以评估通过一系列路径转换到达目标站点的难度；

(2) 其次，作者设计了VEE，利用DNNs模拟路径转换，在不执行种子的情况下预测潜在的路径转换和相应的奖励，大大提高了效率；

(3) 作者提出了一种强化学习模糊测试（RLF）模型，它可以结合历史信息和预测信息，生成到目标代码的最佳路径。

(4) 作者在动作群的粒度上优化了模糊的突变策略，这比单策略优化更有效。

**二、概述**

DeepGo的基本框架如图1所示，主要由四部分组成：

1) 定向灰盒模糊组件（Directed Greybox Fuzzing Component）：定向灰盒模糊组件不断地突变种子，以产生到达目标位点的输入。这个组件包含一个静态分析器和一个模糊器。在编译时，静态分析器计算基本块级距离（BB距离），记录每个分支的兄弟分支，并测量目标程序。一旦模糊的活动启动，模糊器就会不断地改变种子来测试程序。

2) 虚拟集成环境（Virtual Ensemble Environment）：VEE用于预测潜在的路径转换和相应的奖励。VEE由DNNs组成，与强化学习组件共享历史应答缓冲区和预测应答缓冲区。

3) 针对模糊测试的强化学习模型（Reinforcement Learning for Fuzzing Model）：该模型利用强化学习模型来结合历史路径转换和预测的路径转换，以学习能最大化路径转化序列奖励的策略。

4) 模糊测试优化组件：为了引导模糊器采用具有最高序列奖励的最优路径转换序列，需要基于RLF模型的反馈信息来优化模糊策略。然而，优化一个单一的模糊策略可能并不能显著地引导模糊器走向最优的路径转化序列。因此，作者提出了由五个要素组成的动作群的概念，以利用MPSO算法综合优化多种模糊策略。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloY79yB3pGDkoxMeYYw6ia5PwLOeKcoZjh0SB0E10ibAuzAjaQ805AKdX2KkHXXlxUUvB6lZ2JbSNxg/640?wx_fmt=png&from=appmsg)

**图 1 DeepGo流程概述图**

**三、路径转换模型**

路径转换模型将定向模糊测试建模为通过特定的路径转换序列到达目标站点的过程。由突变产生的新种子会导致路径转换，作者使用奖励来评估路径转换对模糊过程的影响。具有最高序列奖励的路径转换序列决定了到目标的最佳路径，路径转换模型包括以下几个元素：

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIKZZtOmQyBbibSMo8dziakibkMJYd0uh6fB99Xgs42pWn1V6pgNFExtfTw/640?wx_fmt=png&from=appmsg)**图 2  路径转换模型的说明**

(1) 路径：每个路径都对应于种子队列中的一个种子，通过不同分支命中来区分不同的路径。

(2) 动作：模糊器的动作意味着在一个特定的位置使种子发生突变。作者关注于突变发生的位置，而不是它使用的突变方法。

(3) 路径转换：如果新输入的执行路径与种子上的执行路径不同，那么种子上的突变就会导(致路径转换。如果新输入的路径与种子输入的路径相同，那么突变就会导致自路径转换。

(4) 奖励：对路径转换的奖励表示由路径转换引起的种子值的变化。

(5) 策略：该策略是模糊器在每条路径中选择动作的策略，表示为与动作对应的概率列表。

作者从四个方面来衡量种子的价值，分别为：(1) 种子到目标的距离；(2) 分支反转的困难程度；(3) 执行速度；(4) 种子是否被标记为“favored”。对于单一分支反转的困难程度，作者通过兄弟分支的命中次数来进行量化，具体计算过程如公式(1)所示，其中ubr为表示一个未被探索的分支，hitbr表示在模糊化过程中记录的兄弟分支的命中。作者使用一个种子路径中所有未被探索的分支的分支反转概率的算术平均值来估计该种子分支反转的难度。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKI5MpJIwuqXIUhTZwh4ezp5J9jIcegXUvlG9sILnoQTgsNvXq5TcZ3Gg/640?wx_fmt=png&from=appmsg)

最终，作者利用熵权法计算种子到目标的距离，分支反转的困难程度，执行速度，种子是否被标记为“favored”等项的权重，然后进行加权平均得到种子的价值Vs(pt)。模糊器采取不同的动作来突变种子会导致不同的路径转换，作者使用奖励来量化路径转换的有效性。路径转换的奖励为突变前后两种子价值的差值，即r(pt, at, pt+1) = Vs(pt+1) - Vs(pt)，at表示模糊器从路径pt转移到路径pt+1所采取的动作。

在路径转换模型中，根据策略选择的动作所引起的路径转换会影响后续的路径转换序列，从而影响到达目标站点。为了评估路径转换对到达目标站点的贡献，作者将期望序列奖励定义为模糊器遵循某一策略生成的路径转换序列的期望奖励之和，可以根据公式（2）得到。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKInsuw9vcVicOHcuChBOXK2z594YLwfucrJibXQftMtmpfogLhRxv2s1pA/640?wx_fmt=png&from=appmsg)

其中，p’∼P表示从路径p转移到路径p’的概率。γ代表折扣因子，后续路径转换对预期序列奖励的影响会逐渐减少，为路径p’的转移，当路径的所有动作都只能导致自路径转换时该值为0，否则该值等于所有行动的预期序列奖励的加权平均值，可以根据公式（3）得到，其中表示在策略π下，路径p选择动作a的概率。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIC0VZnZMET4QiaU7JsebvP1lIdEke3ts0B7DAlJcXiayORP1p4GWLsheQ/640?wx_fmt=png&from=appmsg)

**四****、虚拟集成环境和针对模糊测试的强化学习模型**

**1．虚拟集成环境**

作者使用DNN来构造VEE来预测路径转换模型中的路径转换行为。通过训练模型，使模型能够根据输入(path, action)得到相应的输出(next path, reward)。针对预测模型的偶然不确定性问题，作者使用可训练的权值参数θ来表示下一条路径pt+1的高斯概率分布，如公式（4）所示，其中N表示高斯分布，µθ表示高斯分布的平均值，Σθ表示方差。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKI7JWvDcDiaM0zo3iaIhRj1H2yRNn7o7COWzUhcibFDuEuS0iaShiafibaeOuw/640?wx_fmt=png&from=appmsg)

作者将训练集中DNN的输出与真实标签y∈Y之间的损失函数定义为：

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIqtBzZnoxtUbJqBCqsQFozRYgZlR2JGK0Gyc7aiadlEeDVEPFMmL1kPQ/640?wx_fmt=png&from=appmsg)

训练任务是找到DNN 的权重参数θˆ，以最小化损失。

针对预测模型的的认知不确定性问题，作者使用6个相同的DNNs来构建VEE，并采用6个DNNs的概率平均值作为模型的预测。

**2．针对模糊测试的强化学习模型**

作者基于强化学习模型Soft Actor-Critic (SAC)训练了一个能通过选择动作来最大化序列奖励的模型。该模型由Actor network、Q-Critic network和V-批评网络组成。在训练过程中，通过Q-Critic network来评估期望的序列奖励，并通过V-Critic网络来评估每个路径的转移值。利用期望的序列奖励和转移值，训练Actor network来优化策略，以增加选择具有高期望序列奖励的动作的概率。训练过程中，该模型以历史执行信息和通过虚拟集成环境（VEE）预测出的可能路径转换序列作为训练输入。其中，通过虚拟集成环境（VEE）预测出的可能路径转换序列将以某一历史路径序列(p0, a0, p1, a1...pi, ai, ...an−1, pn)为基础，根据当前强化学习模型的策略选择一系列新动作a’i,a’i+1......a’i+k-1,根据原路径序列和选择的一系列新动作，虚拟集成环境（VEE）将预测出一条新的路径转换序列供强化学习模型训练，具体过程如图三所示：

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIzvvNhLkhAh4Nu7ZkriciacqjksjLv77x0GfxaqyK8LP6T4GThv9YHQoA/640?wx_fmt=png&from=appmsg)

**图 3  K步分支预测策略**

**3．基于行动组的模糊策略优化**

由于优化单一的模糊策略可能并不能显著地引导模糊器走向最优的路径过渡序列。因此，作者提出了由五个元素组成的行动组的概念，并使用MPSO算法综合优化多种模糊策略。作者在动作组中考虑到了种子选择策略，种子能量分配策略，变异中Havoc阶段的重复次数，被选择来突变种子的突变操作，被突变位置来对模糊过程进行综合优化。所使用到的算法如图四所示：

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIkicNZliaMjZB8sEcxksCSd0VFSUQ0SyBt1qFA8Dt4vtEQgYqgjIsDaGg/640?wx_fmt=png&from=appmsg)

**图 4  MSPO算法**

**五、实验设计及结果**

**(一)．实验设置**

作者选择了两个被定向模糊测试技术广泛使用的数据集UniBench[1]和AFLGo testsuite[2]，并与最先进的定向灰盒模糊器进行了比较，包括WindRanger[3]、BEACON[4]、ParmeSan[5]和AFLGo。所有实验均在24小时的时间预算内重复5次。在测试来自UniBench和AFLGo测试套件的程序时，作者使用BenchMark推荐的种子语料库中的种子作为初始种子。

**(二)．具体实验**

**实验一：到达目标代码的能力**

**图5显示了各个工具生成可以到达目标代码的第一个输入所花费的时间（TTR）。与AFLGo（22/80）、BEACON（11/80）、WindRanger（19/80）和ParmeSan（9/80）相比，DeepGo可以达到最多（73/80）。此外，在大多数的目标上DeepGo的性能优于所有其他模糊器，并实现了最短的TTR。就到达目标站点的平均TTR而言，与AFLGo、BEACON、WindRanger、ParmeSan相比，分别加速了3.23×、1.72×、1.81×和4.83×。**

**![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIoyTwBP9ib12t8BoUfGnblg7Bibb9WQFZQXQ07L2h3vficWHUWZ7ur0CUw/640?wx_fmt=png&from=appmsg)**

**图 5  DeepGo和其他模糊器在UniBench数据集上的TTR比较**

**实验二：漏洞挖掘能力**

在20个漏洞中，DeepGo（19）比AFLGo（14）、BEACON（13）、WindRanger（16）和ParmeSan（14）暴露的更多。此外，在大多数目标（14/20）上，DeepGo的表现优于所有的基线模糊器，并达到了最短的挖掘目标站点中（已知或未公开的)漏洞所花费的时间（TTE）。关于挖掘漏洞的平均TTE，DeepGo与AFLGo、BEACON、WindRanger和ParmeSan相比，加速速度分别为2.61×、3.32×、2.43×和2.53×，具体实验结果如图6所示。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIib5vTLbLtEJyvy2aN5bU8hCSXh2YqNMlEzHeDzSKBC2eJuUaR3wYRmw/640?wx_fmt=png&from=appmsg)

**图 6  DeepGo和其他模糊器的TTE比较**

**实验三：VEE的有效性**

作者计算了所有程序的所有路径转换的预测概率（AAPP）的平均精度和预测奖励（AAPR）的平均精度，如图7所示。从0.5小时到24小时，AAPP和AAPR的准确率均大于80%，AAPP和AAPR在48个时间点的平均值分别为92.57%和91.10%。这表明VEE可以限制预测路径转换的概率和奖励的偏差。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIMrGs5kdJOM1U3M2XhkBS0rI5qyo71jYqK3W8SH9uH2mMTicp1mcictlw/640?wx_fmt=png&from=appmsg)

**图 7  预测的奖励和路径转换概率的准确性**

**实验四：强化学习模型和模糊测试优化组件的有效性**

作者删除了DeepGo的强化学习模块和优化组件模块形成了一个新的模糊测试工具DeepGo-r。作者使用DeepGo-r和DeepGo来测试来自UniBench的20个程序，并每30分钟计算出所有程序的所有路径转换的奖励。在每个时间点，获得了20个项目的平均奖励（即AR）如图8所示。DeepGo的AR明显高于DeepGo-r。在每个时间点，DeepGo的AR平均比DeepGo-r的AR高4.26×。这说明化学习模型和模糊测试优化组件可以引导模糊器得出最优的路径转换序列，更快地到达目标位置。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKI976oibicuTjOulR1WftrcvCJs97t2CrGzXHpM3D4MgesJZpaBq56g6vw/640?wx_fmt=png&from=appmsg)

**图 8  DeepGo-r和DeepGo的AR对比**

**实验五：消融实验**

作者从DeepGo中删除VEE，形成一个新的工具DeepGo-V，并在UniBench上运行DeepGo-V和DeepGo-r进行TTR实验，实验结果如图9所示。根据TTR的结果，DeepGo（73/80）分别比DeepGo-v（32/80）和DeepGo-r（18/80）可以到达更多的目标站点。此外，DeepGo在到达目标站点的平均TTR上分别比DeepGo-v和DeepGo-r高出2.05×和3.72×。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlo3rBemKyJicqPXKJ5epxOKIncbwTP3gQTbDweFPdmIgL4ibfWbb7ibvsWSFB3F8QZX2NicibaVKsNlDYA/640?wx_fmt=png&from=appmsg)

**图 9  消融实验**

**六、总结**

作者提出了一种预测性定向灰盒模糊器，它可以结合历史信息和预测信息，引导定向模糊测试选择最优路径到达目标站点。作者先将定向模糊测试建模为通过特定的路径转换序列到达目标站点的过程。突变产生的新种子会导致路径转换，而与高奖励路径转换序列对应的路径表明通过它到达目标位点的可能性很高。然后，为了预测路径转换和相应的奖励，使用深度神经网络构建了一个虚拟集成环境（VEE），逐步模拟路径转换模型，并预测尚未采取的路径转换的奖励。为了确定最优路径，开发了一个模糊强化学习（RLF）模型来生成具有最高序列奖励的过渡序列。RLF模型可以结合历史路径转换和预测路径转换来生成最优路径转换序列，并结合策...