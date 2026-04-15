---
title: 论文研读与思考|面向测试时强化学习的验证工具
url: https://mp.weixin.qq.com/s/xa6nJv7ysNpeWOuF8SlPhg
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:39:37.922508
---

# 论文研读与思考|面向测试时强化学习的验证工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIw6GCIKgCtfaWWXVzBLpAZP02OzCwsiaUkiao5ujTz6VsoD7F8CSB24F0oawibr8xYnVjPTpmF0s1XARc9vOUIwzQlsg3FT0OZGJU/0?wx_fmt=jpeg)

# 论文研读与思考|面向测试时强化学习的验证工具

Liu
Liu

玄枢战队-Arcane Hub

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#### 原文标题：Tool Verification for Test-Time Reinforcement Learning

#### 原文作者：Ruotong Liao*；Nikolai Röhrich*；Xiaohan Wang；Yuhui Zhang；Yasaman Samadzadeh；Volker Tresp；Serena Yeung-Levy

#### 论文链接：https://arxiv.org/abs/2603.02203

#### 一，主要研究问题和方案

##### 1.1 核心研究问题

        强化学习已经进入“经验自我进化”时代，测试时强化学习（Test-Time Reinforcement Learning, TTRL）已成为大推理模型（LRM）自我进化的前沿范式，具体来说，在典型的TTRL设置中，LRM首先生成多个推理轨迹，通过多数投票假定出正确答案，将其标注为伪标签，并由此推导出强化学习奖励。LRM根据对无标签测试输入进行的某种在线强化学习训练而进化。这模仿了人类学习的一个基本模式：通过对新问题生成候选解、采纳最合理的一个并据此更新，从而获得提升。然而，TTRL存在一个关键缺陷：**虚假但高频的未验证共识可能成为有偏且被强化的奖励信号，导致模型陷入错误模式坍缩（Incorrect Mode Collapse）**。

        具体来说，当多数投票产生的伪标签本身就是错误的时候，模型会反复强化这个错误答案，形成恶性循环即越训练越自信地输出错误结果。文章用一个简洁的例子说明：假设真实标签为C，采样出的10个预测为AABBBBCCCD，多数投票选择B作为伪标签，由此产生的奖励信号会错误地奖励所有回答B的输出，使得模型进一步偏向错误答案B。

        面对上述问题，文章主要研究：

    （1）(分析)TTRL中多数投票产生虚假共识的根本原因是什么？这种虚假共识如何导致训练崩溃？

    （2）(方法)如何引入外部验证机制来抑制虚假共识，从而稳定测试时强化学习的自我进化过程？

    为解决上述问题，文章提出了**T3RL（Tool-Verification for Test-Time Reinforcement Learning）**框架。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxFezDLqrp0eXWR0uP6SVTrTGEk7cRXVmxOHqHrFtpqtEVS7jj3GpoBpVSL06BrgMXVSpsEibUQGRSSZYUc3c7T0Z3ia821yngJM/640?wx_fmt=png&from=appmsg)

图1 T3RL的核心概念。多数投票伪标签可能是虚假的，T3RL引入验证来抑制虚假流行的伪标签。T3RL通过工具执行证据（如代码解释器）将测试时验证引入自我进化过程，用验证过的rollout稳定训练。

##### 1.2 研究方案

##### 1.2.1 背景与问题分析

**TTRL的基本流程**：给定无标签测试数据集，对每个问题x，策略模型πθ采样N个响应{y\_i}，通过多数投票获得伪标签：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxo4VdCyKmeyd21yonCP9yWJlfnraI4O1CasVk1V1yhHsrKvicbToB6ncQJQSBKwEN9OqPNo1R54YCVkfDmEgdrUBnbBd7fB834/640?wx_fmt=png&from=appmsg)

然后以伪标签y\**为基准，计算二元奖励：ri = 1[Extract(yi) = y\**]，用于GRPO等策略梯度更新。

**虚假共识的根源**：多数投票隐含了一个强假设即多数即正确。然而在数学推理等场景中，模型的系统性错误（如计算幻觉、逻辑偏差）可能导致大量rollout收敛到同一个错误答案，形成高频但虚假的共识。此时多数投票不仅无法纠错，反而会将错误固化为奖励信号，导致：

* **错误模式坍缩**：模型被奖励信号驱使，越来越倾向于输出错误但"流行"的答案
* **自我强化循环**：错误的伪标签→错误的奖励→模型偏向错误答案→更多rollout输出错误答案→伪标签更加错误

        文章将此定义为**未验证共识偏差（Unverified-Consensus Bias）**，是TTRL的核心失败模式。

##### 1.2.1 T3RL框架

        T3RL框架一个将工具验证集成到测试时强化学习聚合机制中的强化学习框架，从而实现有依据的、更鲁棒的奖励估计。具体而言，T3RL 包含三个核心组件：

    (1) **验证器**：一个 LLM，其任务是通过将给定的推理轨迹编译成可执行的 Python 代码来验证该轨迹，并根据代码执行结果判断其有效性。

    (2) **验证工具**：一个代码解释器，负责执行生成的 Python 程序，并将执行结果返回给验证器。

    (3) **验证权重**：用于将多数投票替换为一种“验证感知的加权投票”，从而提升已验证推理轨迹的投票权重。

##### 1.2.2 验证器

##### 验证器的核心功能是把策略模型生成的自然语言推理链翻译成可以被执行和验证的Python代码。

##### 验证器的操作流程：第一步，读取问题和对应的推理过程，将其中的关键推理步骤转化为一段Python程序；第二步，将这段代码送入沙箱环境执行，获取代码运行的输出作为证据；第三步，对比代码执行结果与推理链中的声明，判断该rollout是否通过了验证，同时提取代码执行后得出的答案。验证器输出的结果包含，一是验证器根据代码执行证据推导出的答案，二是一个验证指示标记代表了是否通过验证。

##### 1.2.3 验证工具

##### 在T3RL中，验证工具以代码解释器的形式实现。它接收验证器生成的Python代码，在沙箱环境中执行，然后返回代码的运行结果。

##### 验证工具的验证操作包括：验证推理链中的算术计算是否正确、验证声称的方程解是否真的满足方程、验证排列组合的计数是否准确等。如果推理链中某个中间步骤的数值声明与代码执行结果矛盾，该rollout就会被标记为未通过验证。

##### 1.2.4 验证权重

##### 验证权重的作用让验证通过的rollout拥有更大话语权，又不完全否定未验证rollout的价值。

##### 验证权重：对于每一个rollout，如果它没有通过验证，投票权重为1；如果它通过了验证，投票权重变为ω（ω是大于等于1的超参数）。也就是说，验证通过的rollout相当于拥有ω张选票，而未验证的只有1张。所有rollout按这个加权规则进行投票，得票最多的答案成为最终的共识伪标签，用作奖励计算的基准。

##### 1.2.5完整算法

```
from collections import defaultdict

def t3rl_reward_fn (x, policy, verifier, sandbox, N, omega):
       Y = policy.sample_rollouts(x, n=N)
       vote, A = defaultdict(float), []

       for  y  in  Y :
            # (1) 验证器生成代码
           code = verifier.generate(x, y)
            # (2) 沙箱执行代码并返回证据
           evidence = sandbox.execute(code)
            # (3) 验证器解析证据
           a, v = verifier.judge(x, y, evidence)  # v ∈ {0, 1}
           vote[a] += (1.0 if v == 0 else omega)  # 未验证=1, 验证通过=ω
           A.append(a)

       y_star = max(vote, key=vote.get)  # 加权多数伪标签
       rewards = [1.0 if a == y_star else 0.0 for a in A]
       return    y_star, rewards
```

#### 二，主要贡献

        文章的主要贡献有三方面：

1. **问题分析**：系统性地识别了TTRL中的核心失败模式——未验证共识偏差（Unverified-Consensus Bias），即多数投票产生的高频虚假共识会导致错误模式坍缩。这是首个从验证角度深入分析TTRL失败模式的工作。
2. **方法创新**：提出T3RL，首次将测试时工具验证引入测试时强化学习框架，通过验证感知的加权投票机制抑制虚假共识，产生更可靠的伪标签和奖励信号。该方法具有模块化特性，可以与任何偏好优化算法即插即用。
3. **实验验证**：在3个数学推理基准（MATH-500、AMC、AIME 2024）和多种骨干模型上验证了T3RL的有效性，表明工具验证可以持续稳定自我进化过程。更广泛地，T3RL将测试时RL定位为**验证式在线数据合成（Verified Online Data Synthesis）**。

#### 三，实验设计与性能分析

##### 3.1 实验设计

**基准测试**：在3个数学推理基准上评估：MATH-500，AMC，AIME 2024

基线模型：Qwen2.5-Math-1.5B，Qwen2.5-1.5B，Llama-3.2-1B-Instruct

基线方法：Vanilla（基座模型，无训练），TTRL（标准测试时强化学习）

**实现配置**：

* 训练框架：GRPO
* 优化器：AdamW
* 验证器：1B和1.5B规模的LLM验证器
* Vote-then-Sample：64个响应用于标签估计，下采样至32个用于训练
* 最大token长度：2560（策略）；1024（验证器）
* 硬件：8块NVIDIA A100 GPU
* 训练轮次：10（MATH-500）、30（AMC）、80（AIME 2024）

##### 3.2 主要实验结果

**表1：主要结果**

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwXibThoommYhM24wAlbOJqxvkLIVeyfwQfpcmhWBjrS5fjpKg6gGfoMKqCZaicH5GtTYUchuk4iaZPiaJTczcRCqWdP5Se9bSMxicA/640?wx_fmt=png&from=appmsg)

**主要结论**：

**T3RL在所有基准和模型上持续优于TTRL**。这支持了文章的核心假设：验证感知的多数投票可以缓解测试时RL中的未验证共识偏差。

**在更难的问题上增益更显著**。在AIME 2024这种极高难度基准上，T3RL相对TTRL的增益尤为明显。例如在Qwen2.5-Math-1.5B上，AIME 2024增益为+3.7（相对提升21.6%），而MATH-500增益为+1.6（相对提升2.2%）。这表明在多数投票更容易产生虚假共识的难题上，工具验证的价值更大。

**跨模型一致性**：无论是数学专用模型（Qwen2.5-Math）还是通用模型（Qwen2.5、Llama-3.2），T3RL都带来了稳定提升，说明该方法具有普遍适用性。

##### 3.3 消融实验与分析

**Q1：验证如何改变共识分布？**

       文章分析了T3RL对伪标签质量的影响：

* **成功率案例**：当多数投票选出错误答案时，T3RL的代码验证可以将共识纠正为正确答案。验证通过的rollout获得更高权重，从而将伪标签从虚假流行的答案转变为验证正确的答案。
* **局限性**：在简单任务上，工具验证的边际效益有限。当任务足够简单、rollout本身高度准确且一致时，自我共识很少选错标签，验证增加了开销但未实质改变伪标签分布。

**Q2：什么可以进一步提升T3RL的性能？**

* **更强的验证器**：将Qwen-Math-2.5的验证器从1.5B提升至7B，T3RL在AIME 2024上从20.8提升至21.7，在AMC上从50.9提升至51.5，在MATH-500上从74.4提升至74.9。更强的验证器提供更可靠的答案归一化和置信度估计。
* **更大的rollout预算**：将N从16增加到64，T3RL持续改善。更大的候选集增加了解的多样性，使验证感知投票更高效：验证通过的rollout更可能出现并获得更高投票权重。

**Q3：弱验证器的失败模式**

        文章专门分析了0.5B验证器的失败情况：

**表2：弱验证器测试结果**

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxaJo1HsZicqKibVmmjcEW2rjA0pqib1xt5CUzMvMyxH0uDRcm7EvKwRrNeWymSTic8xgJiaPSNjtiaa5VvBglQREtpsXiaEc7T3pMksE/640?wx_fmt=png&from=appmsg)

       导致性能下降，主要原因有两个：

1. **盲目复制与硬编码输出**：小模型在代码注释中虚构推理过程，直接打印推理链中给出的未验证最终答案，而非真正执行验证逻辑
2. **格式与编译错误**：小模型无法持续保持有效Python语法，出现缺少import语句、格式错误、语法幻觉或无限注释等问题

       这表明T3RL需要验证器能力达到最低阈值才能有效运作；低于该阈值，验证器会成为随机噪声源而非可靠的锚定机制。

#### 四，论文的局限性与未来方向

##### 4.1 论文的局限性

1. **验证器能力依赖**：T3RL需要验证器达到最低能力阈值。如0.5B验证器实验所示，弱验证器不仅无法提供有效验证，反而会引入额外噪声，导致性能不如标准TTRL。这限制了T3RL在极小模型上的适用性。
2. **验证工具的限制**：当前T3RL的验证工具以代码解释器为主，主要适用于数学推理等可通过代码执行验证的领域。对于需要语义判断、创造性推理或开放性问答的任务，如何设计有效的验证工具仍是一个开放问题。
3. **简单任务表现较差**：在简单任务上，多数投票本身已经足够准确，工具验证增加的计算开销可能无法带来相应收益。

##### 4.2 未来方向

1. **多模态验证工具**：将验证工具扩展到更多模态（如图像验证、多步逻辑验证），以支持更广泛的推理任务。
2. **自适应验证策略**：根据问题难度和当前模型置信度自适应地决定是否调用验证工具，在简单问题上节省计算资源。
3. **扩展到代码纠错任务**：当前T3RL聚焦于数学推理的答案验证，但代码纠错场景天然具备执行验证的条件，是一个合适的扩展方向。
4. **探索进一步自我进化**：将T3RL定位为"验证式在线数据合成"范式，探索如何将验证机制更深入地融入大模型的自我进化循环中。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/lmfaAJ5WqA1sUVs3bkh8pbJCu96cmwJ5JrqlejuC2Cia3prrW7Nia2b7dibjBwqjMnLV95ibBrOQkEbm9PIDw5IvFQ/0?wx_fmt=png)

玄枢战队-Arcane Hub

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/lmfaAJ5WqA1sUVs3bkh8pbJCu96cmwJ5JrqlejuC2Cia3prrW7Nia2b7dibjBwqjMnLV95ibBrOQkEbm9PIDw5IvFQ/0?wx_fmt=png)

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