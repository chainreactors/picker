---
title: 论文研读与思考|基于字符级CNN和强化学习的对抗性SQL注入检测
url: https://mp.weixin.qq.com/s/XjDvLDKIW8NDW3bdaLIkug
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:13:27.544136
---

# 论文研读与思考|基于字符级CNN和强化学习的对抗性SQL注入检测

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIwtic1MplaAvZpA5RajmZxT0M2dtf7pGEwTa1DAbdmbC6icrMnSK5s4TW6T5ziakQluqqwRUSYlU0g86NnWDOn5Sicjf6A201jqHUo/0?wx_fmt=jpeg)

# 论文研读与思考|基于字符级CNN和强化学习的对抗性SQL注入检测

Liu
Liu

玄枢战队-Arcane Hub

![]()

在小说阅读器中沉浸阅读

#### 原文标题：Adversarial SQLi Detection Using Character-Level CNN and Reinforcement Learning

#### 原文作者：Fucai Yu；Xusheng Li；Yang Wu；Ziqiang Chang；Gaolei Fei；Xuemeng Zhai

#### 作者仓库：https://github.com/lkdxqe/Adversarial-SQLi-Detection

#### 期刊：IEEE Transactions on Dependable and Secure Computing（TDSC）

#### 论文链接：https://ieeexplore.ieee.org/abstract/document/11419834

#### 一，主要研究问题和方案

##### 1.1 核心研究问题

近年来自动对抗性SQLI(指攻击者根据目标 Web Application Firewall（WAF）的反馈动态调整 payload)工具的出现，如AdvSQLi、RAT等，表明对抗性SQLI已成为漏洞检测和SQLI执行的关键方法。这些工具的智能特性对现有的SQLI防御机制构成了重大威胁。遭受敌意突变的有效负载可以有效地欺骗基于机器学习的WAFs，而基于规则的WAFs更容易被发现漏洞。针对这一问题，论文提出了一种基于增强特征层CNN(CLCNN)和强化学习(RL)的混合模型，该模型从模式匹配的角度出发，通过CLCNN的多尺度特征提取来检测恶意模式。

  SQLI攻击的演变：

扩展的恶意有效payload：

1 Appelt等人，采用一种上下文无关文法(CFG)，将SQLI语句结构表示为分析树，使得模块化生成语法正确的SQLI语句及其变体成为可能。

2 Liang等人，采用有效负载语料库上训练大型语言模型，并利用强化学习生成有效的对抗性有效负载。

3 Qu等人，采用CFG来解析现有的SQLI负载并执行敌意突变-这些突变保留了原有的恶意功能，同时修改了负载特征以避开目标WAF。

提高搜索效率：

1 Zhang等人，定义了一种基于关键字频率的距离函数，对距离已知无效案例较远的有效载荷进行优先排序，以提高旁路概率

2 Amouei等人，首先根据相似度对有效载荷进行聚类，然后利用强化学习将搜索集中在被证明有效的簇上，提高了识别可绕过有效载荷的效率

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxRicjFvUT2tAARjVqCoHVBoVMevBJkPbzLfwEyc3oxwia0cQS7icL0ibd9OeyLiaqBZhEaExjWMIdxVAko4Ca61iaYPmf7yRQ5BOUwk/640?wx_fmt=png&from=appmsg)

表I SQLI中payload突变的一般方案

## 1.2相关研究工作

### 突变策略相关研究：

#### 基于突变的方法：

**WAF-A-Mole** ：设计了一个优先级队列来存储变异的SQLI有效载荷及其对应的分类置信度分数(即目标分类器预测该有效载荷为恶意的概率)。在每次迭代中，该算法从队列中选择置信度得分最低的有效载荷进行变异。新变化的有效载荷及其更新的置信度分数被重新插入到优先级队列中。重复该过程，直到找到具有足够低置信度的有效载荷。

**DRL**：他们首先使用FastText在SQLI数据集上训练嵌入模型，以对有效负载进行标记化，并将其转换为固定长度的向量，作为强化学习模型中代理的观察状态。他们还使用表I中所示的变异操作符作为操作空间。他们基于HTTP响应代码手动定义了一组奖励值，奖励成功绕过的有效负载，同时惩罚那些被阻止或错误的负载。最终，该模型确定了在每个观察到的状态下要采取的适当操作。

#### 基于搜索的方法：

**ML-Driven**：使用上下文无关文法(CFG)随机生成大量SQL测试Payload 将生成的Payload归为一个集合 将载荷发送给目标WAF测试，记录是否被拦截 用这些数据训练一个随机森林分类器(用于预测哪些Payload更容易绕过waf)。

**ART4SQLi**：将每个载荷转换为一个归一化的 k 维向量，其中 k*k* 是终结符的种类数 两个载荷之间的距离用余弦相似度来衡量 两个载荷之间的距离用余弦相似度来衡量 选择那个最小相似度最大的载荷(即最远离所有无效载荷的载荷)作为下一个测试对象。

**RAT**：先用深度嵌入网络对载荷进行智能聚类，然后在每个簇内用基于片段权重和拦截频率的评分机制筛选出最有潜力的载荷，最后用ε-greedy策略优先测试高价值簇，从而高效发现能绕过WAF的载荷。

#### 基于生成的方法：

**GPTFuzzer**：是一个"预训练+强化学习"的方法：先用Transformer学习SQLi载荷的语言规律，再用强化学习微调生成策略，使生成的载荷既符合SQL语法，又能有效绕过目标WAF。

### 检查SQLI的方案

**基于规则匹配**：基于规则的检测方法假设恶意请求的特征可以用预定义的规则来描述。每当收到新请求时，就将其与规则库进行匹配，以判断是否为恶意请求。

**基于手工特征提取：**在基于手工特征提取的检测方法中，研究人员通常根据经验知识选择各种定制特征来构建特征向量，然后使用机器学习算法进行分类。

**基于内容检测：**深度学习和自然语言处理的进步推动了对基于内容的检测方法的日益关注：Yu等人。和Kim等人。使用多核TextCNN进行多尺度局部特征提取，而Wang等人提出了一种基于多核TextCNN的局部特征提取方法。Salim等人。评估了稳健优化的BERT和DistilBERT，表明这些自然语言预训练模型在仅输入负载而不需要专家知识的情况下对恶意请求检测的准确率达到80%。此外，一些工作采用了异常检测的观点：唐等人。培训自动编码器对良性有效负载模式进行建模，通过较大的重建错误将恶意有效负载识别为异常。

### SQLI逃避检测策略

**句法结构破坏**：递归编码、嵌套注释和关键字替换等突变操作破坏了恶意模式的固有句法结构。传统的基于NLP的检测方法依赖于标记化或句法分析，当混淆扰乱预定义的标记边界或语法规则时，该方法失效。

**特征稀释和混淆：**敌意负载插入**冗余字符**、应用多层编码或执行逻辑**不变变换**，将原始恶意特征稀释为无关的噪声。基于规则的WAF无法匹配未被预定义规则覆盖的混淆模式，而基于统计特征的模型难以区分有效的恶意特征和混淆引起的噪声。

**动态调试**：对抗性SQLI攻击根据网站管的实时反馈动态调整策略。

##### 1.3 研究方案

文章提出 CLCNN + RL 的混合检测框架（Hybrid Model）：

* **CLCNN（增强的字符级 CNN）**：以字符序列为输入，不依赖分词/解析；通过多尺度卷积提取模式特征，并引入注意力机制增强对关键模式的表达。
* **RL 模块（强化学习去混淆 + 对抗训练）**：仅对 CLCNN 低置信度（不确定区间）样本执行一系列“去混淆”操作（de-obfuscation），使隐藏的恶意模式暴露；并通过对抗训练持续提升对新型混淆的适应能力。
* **决策模块（不确定区间触发）**：将二分类从“硬阈值”扩展为“良性/恶意/不确定”三段式，避免简单降阈值导致误报上升。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwshORGyLv3C4qZicA6MUg2ajDz33FmNJcr6VqLibuc71BR7u9YibN1JJcBWQW6JQZzEl4TEqS9GAVFXAZokAvFR7f0WEGLMNicAk0/640?wx_fmt=png&from=appmsg)

图1 混合模式的框架。

##### 1.3.1 CLCNN：字符级多尺度特征提取

**输入与嵌入**

* 将 payload 映射为字符序列，字符按 ASCII 编码映射到整数索引；0 表示异常字符（如传输/解码错误）。
* 统一序列长度 `s=200`（padding 或截断），嵌入维度 `d=32`，使用 PyTorch `nn.Embedding` 端到端学习字符嵌入。

**多尺度卷积**

* 卷积核尺度：`k ∈ {1,3,5,7,9}`，每个尺度包含 64 个卷积核（随机初始化），stride=1，按 `pad=(k-1)/2` 填充以保持输出长度为 `s`。
* 模式：不同尺度捕获不同长度的局部模式（短 token、关键字片段、注释/编码结构等）。

**注意力机制**

* 引入通道注意力（channel attention）对每个尺度的卷积核输出进行加权，提升“关键核”的贡献，抑制冗余核。

##### 1.3.2 不确定区间：

为避免模型输出过度极端（0/1），文章在交叉熵损失上加入额外惩罚项，抑制 `p_max` 过大，使模型更愿意把“难判样本”留在中间区间，从而交给 RL 处理。

* 损失形式：`L = L_CE + λ * mean(p_max)`（文中 λ=0.3）
* 不确定区间：`[0.4, 0.6]`
* 触发逻辑：仅当输出落入不确定区间时，进入 RL 去混淆回路。

##### 1.3.3 RL 去混淆：

**MDP（马尔可夫决策过程） 定义**

* 状态 `S`：来自 CLCNN 特征图的池化 + 空间注意力后的序列特征（用于保留位置上下文）。
* 动作 `A`：一组基于正则的去混淆操作（对应对抗工具常见混淆算子的“逆操作”）。
* 奖励 `R`：以混淆后模型对置信度提升为奖励，鼓励选择能更快让样本被高置信判为恶意的动作序列。

**Q 函数逼近**

* 采用 DQN 近似 `Q(s,a)`；为抑制过估计，使用 Double DQN。

**动作空间（混淆的逆操作）**

1) Skip：不操作，直接输出当前预测（以 0.5 决策边界）

2) Remove Comments：移除 `/* */` 与 `--/#` 行注释及其内容

3) Replace Comments：将块注释替换为固定占位（MySQL 条件注释保留 `!` 后内容）

4) Placeholder Replacement：将 `\n`、`\t` 等占位替换为空格

5) DML Substitution：替换运算符/关键字等（例如 `||` → `OR`）

6) Simplify Expressions：化简可执行布尔表达式（如 `A AND 1=1 OR 2=1` → `A`）7) SubQuery Convert：将无害子查询转为恒真结构（如 `(SELECT 1)` → `=1`）

8) Integer Decoding：Base64/Hex 等整数解码（或归一到 1）

9) URL Decoding：URL 解码（如 `%20` → 空格）

10) Case Swapping：关键字大小写归一（如 `SeLEct` → `SELECT`）

#### 二，主要贡献

1、系统地总结和验证了自动对抗性SQLI工具的潜在威胁，验证了它们在现有WAFs上的旁路性能，并指出了传统的基于MLs的检测方法的固有局限性。

2、针对敌意SQLI攻击，提出了一种CLCNN+RL混合解决方案，该方案对此类工具表现出很强的抵抗力。经过对抗性训练后，该模型在传统检测场景中获得了更高的召回率，同时最大限度地降低了性能。

3、RL模块被设计为即插即用组件。通过定制训练，它可以增强其他已部署的机器学习模型的对抗性(不需要调整现有的模型参数)，并将保护扩展到其他潜在的对抗性注入攻击(例如XSS)。

#### 三，实验设计与性能分析

##### 3.1 实验对象与数据集

**数据集（Aggregate Dataset）**

* 融合多个公开 SQLi 数据集与 Kaggle/GitHub 的正常请求数据，并包含 CSIC-2010。
* 数据分类：120,000 良性请求 + 80,000 恶意请求，按 6:2:2 划分训练、验证和测试集。

**对比模型**

* 开源 WAF：ModSecurity（黑名单）、Naxsi（白名单）、WAF-Brain（ML-based）
* ML 基线：ANN（统计特征）、LSTM、TextCNN
* 提出方法：CLCNN、CLCNN+RL

**评价指标**

* 标准测试集：F1(得分被用作主要指标，以评估标准测试集上每个模型的整体性能，因为它综合平衡了精确度和召回率，以反映整体检测能力)
* 对抗攻击测试：只用 Recall(因为输入均为恶意 payload)

**研究问题**

* RQ1：SQLI攻击是否构成重大威胁？这三类攻击带来了哪些挑战？
* RQ2：CLCNN的模式还不够好吗？为什么我们需要引入RL模块和对抗性训练？
* RQ3：如果模型针对特定的对抗性SQLI工具进行对抗性训练，他们能否有效地抵抗来自该工具的攻击？多轮对抗性训练能完全缓解该工具的攻击吗？
* RQ4：CLCNN模块和RL模块之间的任务分配是什么？他们各自的贡献是什么？
* RQ5：建议的模型可以部署在现实世界的场景中吗？其计算开销和资源消耗对于实际部署是否可接受？

##### 3.2 标准数据集性能（Raw Model）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIwo6FRSE3Wtia7BemEYblaQUHiazLxF94KJK8s291fHrwJKU75MBS87O5ryswP9toF0m4msZIRY9OllvEzkxNZfgfkbj2miaBrkso/640?wx_fmt=png&from=appmsg)

表II 准确率(Accuracy)精确度(Precision)召回率(Recall)、评价得分(F1)。

    表II展示了各模型在标准测试集上的性能对比，证明论文提出的CLCNN和CLCNN+RL模型在常规检测场景中达到了与基线模型相当甚至更优的水平。

##### 3.3 对抗工具威胁评估（RQ1）

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwHrUpjxSB2slt6qHHUY8QF9JZv1sm4ndZD67GT6odX0De4tEMhU9ZfKPW7LXNvOiaSJeum5j84Uib8ZZdK6eBPSLqNDX1ic97OJM/640?wx_fmt=png&from=appmsg)

表 III表明：

* **规则型 WAF**：变异攻击影响较小，但**搜索型**能快速定位剩余可绕过样本，使 Recall 大幅下降（例如 ModSecurity 在 RAT 下 Recall 降到约 51.57）。
* **传统 ML/深度模型(ANN/LSTM/TextCNN)**：对**变异型工具**非常脆弱，Recall 常出现 40% 级别下降；对未知生成数据集也可能显著退化。
* **CLCNN/CLCNN+RL**：整体对变异/搜索/生成更稳(如 CLCNN 在 GPTFuzzer 数据集上 Recall 99.99)，体现字符级模式学习对混淆的天然抗性。

文章给出的结论(Answer to RQ1)：

* 搜索型工具能更高效地绕过规则型防护；
* 变异型工具能有效改变特征并绕过 ML-based；
* 生成型工具仍有冗余/有效性问题，但趋势上值得警惕。

##### 3.4 为什么需要 RL（RQ2）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxrezQJ2FD1QRtCbTvn8Kn9Cf09NHNuMwTQSIXiak2YzPZUNxjXJaibpMf8PicWPODJwP6AFoibDjzjt7Ggoy65mKzMr1zEExrZH6E/640?wx_fmt=png&from=appmsg)

图2 原始模型针对各种敌意SQLI攻击的性能指标说明。

如左面板显示CLCNN对抗变异攻击的能力远强于LSTM/TextCNN，但仍有约11%的高度混淆载荷无法检测，因此需要引入“不确定区间 + RL 去混淆”，把困难样本交给可更新的动态模块处理，并通过对抗训练持续增强。

##### 3.5 对抗训练效果（RQ3）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIx6odp44joNcZwicJiafzIvv1KUApvavSnBKangvClSQ7sh0jtBxHyqjGq67pL0lSTeqcLDb9FpPYfZCUYNkx5kLqNafiaLApKUia0/640?wx_fmt=png&from=appmsg)

表 IV 表明对抗性训练可以增强模型对不同对抗性SQLI工具的抵抗力，但代价是整体性能。但这些模式都不能完全克服这种攻击。在经过多轮对抗性训练后，我们提出的混合模型在面对特定的对抗性工具时接近其“回忆”极限，同时经历了较小的整体性能下降，而CLCNN+RL 在多轮训练后，对多个工具的 Recall 持续抬升，并且整体退化更小。

##### 3.6 CLCNN 与 RL 的任务分工（RQ4）

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzH2kjBEAcSlmUbYeLdPU4WWMJGakGMwibLKBc6oUulruJpibTAaNlqy9Chvo08d1dc3iaqCXSdsWo0sjReJJcibrkGoWPr6NhyDic4/640?wx_fmt=png&from=appmsg)

作者统计 RL 触发比例与效果（表 V/VI）：

* 约 **80%** 的样本由 CLCNN 高置信直接处理，且准确率通常 **>99.5%**；
* 约 **20%** 进入 RL；RL 对变异型工具产生的高度混淆样本效果更显著(对抗场景中子集准确率可达 95%+)。

说明大约80%的有效载荷直接由CLCNN模块分类，平均准确率超过99.5%。在剩余的20%的有效载荷中，RL模块有效地处理了基于突变的工具生成的有效载荷，平均准确率超过95%。

##### 3.7 部署开销（RQ5）

![](https://mmbiz.qpi...