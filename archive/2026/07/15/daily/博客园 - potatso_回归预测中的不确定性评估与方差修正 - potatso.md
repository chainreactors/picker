---
title: 回归预测中的不确定性评估与方差修正 - potatso
url: https://www.cnblogs.com/potatso/p/21491073
source: 博客园 - potatso
date: 2026-07-15
fetch_date: 2026-07-16T04:52:29.226103
---

# 回归预测中的不确定性评估与方差修正 - potatso

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [回归预测中的不确定性评估与方差修正](https://www.cnblogs.com/potatso/p/21491073 "发布于 2026-07-15 12:31")

## 1. 连续空间的博弈：为什么回归没有查准与查全？

在机器学习的回归预测场景中，绝大多数任务只需要模型输出一个具体的连续预测值即可。

这与二分类任务有着本质的不同。在二分类中，我们拥有“查准率（Precision）”与“查全率（Recall）”等直观的、基于混淆矩阵的硬判决指标。但回归模型本质上是一个连续映射函数，其输出结果往往是输入特征 \(x\) 经由网络层级转换（如仿射变换 \(\mathbf{w}^T \mathbf{x} + b\)）后的连续实数。由于缺乏天然的“非黑即白”分类边界，回归算法无法直接套用分类任务中那些基于对错统计的直观评价指标。

## 2. 期望与方差：欠拟合与过拟合的统计学真相

为了评估回归模型，我们假设其预测值围绕真实值呈现高斯分布。其中，**方差**对应预测值的**波动程度**，而预测值的**数学期望**则对应着**真实值**（即理想状态下的无偏估计）。

在这个视角下，过拟合与欠拟合有了全新的统计学物理画面：

* **在欠拟合（Underfitting）场景下**：模型由于表达能力不足，预测值的期望严重偏离真实值，呈现出显著的**高偏差（High Bias）**。这在直觉上很容易理解：由于模型未能捕获数据的底色规律，其预测均值与真实物理世界对不上，期望在宏观上呈现出“系统性偏差”。
* **在过拟合（Overfitting）场景下**：模型在训练集上过度拟合了噪声，表现出极小的训练方差和近乎完美的拟合度。然而，一旦面对未知的测试集，预测值的方差（Variance）就会呈爆发式增长，表现出极高昂的不确定性。这本质上是因为模型只是“死记硬背”了训练集特例，而未能提取出具备普适性的泛化关系（Generalization Relation），从而在测试阶段彻底失控。

## 3. 从极大似然到 MSE：对数似然的数值拯救

既然我们将预测值与真实值的关系建模为高斯分布，那么自然可以使用信息论与概率密度的视角来构建损失函数。在回归任务中，优化的初始目标是使所有训练样本在当前预测分布下的**联合概率（似然函数）最大化**。

在数学形式上，由于样本之间具有独立同分布（i.i.d.）属性，这表现为所有样本概率密度的**连乘积**。

假设样本 \(y\_i \sim \mathcal{N}(\hat{y}\_i, \sigma^2)\)，联合概率（似然函数 \(L\)）为连乘：

\[L = \prod\_{i=1}^N \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(y\_i - \hat{y}\_i)^2}{2\sigma^2} \right)
\]

然而在实际的数值优化中，如果数据集规模较大，成千上万个介于 0 到 1 之间的概率值进行连乘，会导致极其严重的**数值下溢（Underflow）**，导致计算机直接将其截断为 0；且计算机计算高维乘法的效率远低于加法。

为了解决这一数值稳定性与计算效率的瓶颈，我们可以在联合概率外部套上**对数（Log）函数**。由于对数函数的单调递增性，它在不改变极值点的前提下，将复杂的“连乘”巧妙地转化为 **“对数似然的连加和”**：

\[\ln L = \sum\_{i=1}^N \ln \left( \frac{1}{\sqrt{2\pi}\sigma} \right) - \sum\_{i=1}^N \frac{(y\_i - \hat{y}\_i)^2}{2\sigma^2}
\]

最大化似然函数 \(\ln L\)，等价于最小化它的相反数（负对数似然 NLL）。剔除常数项后，我们的最小化目标直接简化为：

\[\arg\min \sum\_{i=1}^N (y\_i - \hat{y}\_i)^2
\]

仔细一看，我们就会发现，其核心优化项精精准准就是我们常用的均方误差（MSE，Mean Squared Error）的定义。

## 4. 异方差建模：打破“大锅饭”假设

在上述传统的 MSE 损失函数中，我们默认了一个极强的先验假设：所有样本的噪声分布是恒定且一致的，这在统计学中被称为**同方差性（Homoscedasticity）**。

然而在实际的工业场景中，不同样本的观测噪声和预测难度往往大相径庭。例如，模型对于特征清晰的样本 A，预测把握可能高达 70%；而对于充满噪声干扰的样本 B，预测把握可能只有 50%。

为了让模型能够自适应地表达这种对不同样本的“信任度”，我们需要打破同方差假设，引入异方差（Heteroscedasticity）建模。此时，每个样本的方差 \(\sigma\_i^2\) 不再是一个全局固定的常数，而是作为一个随着输入 \(x\_i\) 动态变化的自适应变量。

在工程实践中，我们通常会构造一个**多输出模型（Multi-Output Model）**——模型的主干网络在末端分裂出两个并行的输出头：一个输出头负责预测传统的均值 \(\hat{y}\_i\)，另一个输出头则负责预测该样本对应的方差 \(\sigma\_i^2\)。为此，我们需要对损失函数进行重新推导。

由于每个样本的方差 \(\sigma\_i^2\) 都是动态变化的变量，样本 \(y\_i\) 的概率密度函数写为：

\[y\_i \sim \mathcal{N}(\hat{y}\_i, \sigma\_i^2)
\]

此时，所有样本的联合概率密度（似然函数）中，方差 \(\sigma\_i\) 必须留在连乘符号内部，无法作为常数提出来：

\[L = \prod\_{i=1}^N \frac{1}{\sqrt{2\pi}\sigma\_i} \exp\left( -\frac{(y\_i - \hat{y}\_i)^2}{2\sigma\_i^2} \right)
\]

为了进行数值优化并防止下溢，我们同样在外部套上自然对数（Log），将其转化为对数似然函数：

\[\ln L = \sum\_{i=1}^N \left( -\frac{1}{2}\ln(2\pi) - \ln(\sigma\_i) - \frac{(y\_i - \hat{y}\_i)^2}{2\sigma\_i^2} \right)
\]

在机器学习中，我们通过最小化负对数似然（NLL，Negative Log-Likelihood）来训练网络。剔除与常数 \(\ln(2\pi)\) 相关的无用项，并将 \(\ln(\sigma\_i)\) 转换为 \(\frac{1}{2}\ln(\sigma\_i^2)\) 方便方差头直接输出，我们最终得到了多输出模型的自定义损失函数：

\[\text{Loss}\_{\text{NLL}} = \frac{1}{N}\sum\_{i=1}^N \left( \frac{(y\_i - \hat{y}\_i)^2}{2\sigma\_i^2} + \frac{1}{2}\ln(\sigma\_i^2) \right)
\]

## 5. 贝塞尔修正：警惕模型“虚高的自信”

引入异方差机制虽然在很大程度上赋予了模型表达“预测把握”的能力，但这些自适应输出的方差和概率，在数学逻辑上真的绝对可靠吗？答案是否定的。

在统计学中，我们对预测值自身波动的度量通常被称为**标准误差（Standard Error）**。根据标准误差的推导，当我们在缺少总体真实均值 \(\mu\)、只能用样本均值 \(\bar{X}\)（在模型中表现为预测值 \(\hat{y}\)）作为替代物来估计方差时，所得到的样本方差是一个典型的**有偏估计（Biased Estimate）**。

在期望意义上，直接计算出的样本方差会系统性地缩水：

\[E[s^2\_{\text{biased}}] = \frac{N-1}{N} \sigma^2
\]

也就是说，未修正的方差系统性地**偏小了 \(\frac{1}{N}\) 比例**。为了消除这一偏差，我们必须引入**贝塞尔修正（Bessel's Correction）**，将计算分母由 \(N\) 修正为 \(N-1\)，从而使方差估计重回无偏状态。

这一数理统计事实引出了一个至关重要的工程推论：**在未经修正前，神经网络预测出的方差在理论上是系统性偏小的；相应地，基于该方差算出来的“置信概率”必然系统性偏大（即模型表现出虚高的自信度）**。

因此，多输出模型预测出的方差，在实际工程落地时，理论上必须要进行一次置信度校准与修正，才能作为真正可靠的决策依据。

## 6. 从方差到区间：如何绘制预测的“安全罩”？

当我们利用贝塞尔修正或校准算法得到了无偏的预测方差 \(\sigma\_i^2\) 之后，接下来的核心问题是：**如何将这个抽象的方差，转化为业务上看得见、摸得着的“安全区间”？**

这在数理统计中，精精准准对应着**区间估计（Interval Estimation）**。

由于我们已经假设预测值 \(y\_i\) 围绕预测均值 \(\hat{y}\_i\) 服从高斯分布 \(\mathcal{N}(\hat{y}\_i, \sigma\_i^2)\)，我们可以对其进行标准化转换，使其符合标准正态分布：

\[Z = \frac{y\_i - \hat{y}\_i}{\sigma\_i} \sim \mathcal{N}(0, 1)
\]

对于给定的置信水平（Confidence Level） \(1 - \alpha\)（例如 \(95\%\) 的置信度，此时显著性水平 \(\alpha = 0.05\)），我们希望找到一个对称的区间，使得真实值落在该区间内的概率恰好为 \(1 - \alpha\)：

\[P\left( -z\_{1 - \alpha/2} \le \frac{y\_i - \hat{y}\_i}{\sigma\_i} \le z\_{1 - \alpha/2} \right) = 1 - \alpha
\]

通过简单的代数变形，我们可以直接推导出预测值在 \(1-\alpha\) 置信度下的**预测区间（Prediction Interval）**：

\[[\hat{y}\_i - z\_{1 - \alpha/2} \cdot \sigma\_i, \quad \hat{y}\_i + z\_{1 - \alpha/2} \cdot \sigma\_i]
\]

这里的 \(z\_{1 - \alpha/2}\) 是标准正态分布的分位数，**在实际工程中，我们不需要进行复杂的积分计算，直接通过查标准正态分布表（Z表）即可获得**。

常用的置信水平与对应的 \(z\) 值如下：

| **置信水平 (1−α)** | **双侧临界值 (z1−α/2​)** | **物理意义（安全罩范围）** |
| --- | --- | --- |
| **\(90\%\)** (\(\alpha = 0.10\)) | **\(1.64\)** | 模型有 \(90\%\) 的把握，真实值不会超出 \(\pm 1.64\sigma\) |
| **\(95\%\)** (\(\alpha = 0.05\)) | **\(1.96\)** | 模型有 \(95\%\) 的把握，真实值不会超出 \(\pm 1.96\sigma\) |
| **\(99\%\)** (\(\alpha = 0.01\)) | **\(2.58\)** | 模型有 \(99\%\) 的把握，真实值不会超出 \(\pm 2.58\sigma\) |

### 🛠️ 置信区间的工程校验：PICP 指标

画出了置信区间，我们如何评估模型预测的区间到底准不准呢？在工业界，我们通常在测试集上使用区间覆盖率（PICP, Prediction Interval Coverage Probability）进行定量评估：

\[\text{PICP} = \frac{1}{N\_{\text{test}}} \sum\_{j=1}^{N\_{\text{test}}} \mathbb{I}\left( y\_j \in [\hat{y}\_j - z \cdot \sigma\_j, \,\, \hat{y}\_j + z \cdot \sigma\_j] \right)
\]

其中 \(\mathbb{I}(\cdot)\) 为指示函数（若真实值落在区间内则记为 1，否则为 0）。

* 若 **\(\text{PICP} \approx 1-\alpha\)**（例如在 \(95\%\) 置信度下，测试集实际覆盖率为 \(94.8\%\)）：说明模型预测的方差非常诚实，区间估计极度精准
* 若 **\(\text{PICP} \ll 1-\alpha\)**（例如在 \(95\%\) 置信度下，实际覆盖率仅有 \(70\%\)）：说明模型预测的方差严重偏小，模型依然处于“盲目自信”的危险状态，必须进行更强力的方差校准。

通过将“动态方差”转化为“置信区间”，我们不仅给出了点预测数值，更在物理层面上为模型输出画上了一道自适应的“安全罩”。这对于自动驾驶、医疗诊断及量化交易等高风险业务的稳健决策，提供了真正的底层支撑。

posted @
2026-07-15 12:31
[potatso](https://www.cnblogs.com/potatso)
阅读(4)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fpotatso%2Fp%2F21491073&targetId=21491073&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202512/35695-20251205182619157-1150461542.webp)](https://ais.cn/u/3Qf22e)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)