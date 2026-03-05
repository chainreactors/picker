---
title: SVM支持向量机 - potatso
url: https://www.cnblogs.com/potatso/p/19667776
source: 博客园 - potatso
date: 2026-03-04
fetch_date: 2026-03-05T04:05:53.439907
---

# SVM支持向量机 - potatso

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
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

# [SVM支持向量机](https://www.cnblogs.com/potatso/p/19667776 "发布于 2026-03-04 13:47")

如果给定的一堆向量无法区分，那就给他们通过某种程度升维，人为再造出一个维度。可以理解为创造的这个线性相关（但其实不是线性相关）的矩阵，就恰好能区分数据集。

人为给数据升维的方式成为核函数

# 数学推导

为了方便，我们假定二分类数据，是以0这个超平面对称分布。在二分类数据集画两条线，尽量让线中间的距离增大。这样尽可能区分1和-1数据。

1. **线 A (恶意侧)**：\(w^T x + b = 1\)
2. **线 B (正常侧)**：\(w^T x + b = -1\)

# 1. 找两个代表点

首先，我们在两条线上各找一个“代表”：

* 在线 A 上找一个点 \(x\_{pos}\)，它满足 \(w^T x\_{pos} + b = 1\)。
* 在线 B 上找一个点 \(x\_{neg}\)，它满足 \(w^T x\_{neg} + b = -1\)。

## 2. 算向量投影

这两条线AB的距离，我们可以认为是原点到线A和线B的和，根据点到直线的距离公式，距离为

\[d = \frac{2}{\|w\|}
\]

我们的目标是

\[\max \quad \frac{2}{\|\boldsymbol{w}\|}
\]

在数学上，最大化一个正的分式 \(\frac{2}{\|\boldsymbol{w}\|}\)，完全等价于**最小化**它的倒数 \(\frac{\|\boldsymbol{w}\|}{2}\)。

\[\max \frac{2}{\|\boldsymbol{w}\|} \iff \min \frac{\|\boldsymbol{w}\|}{2}
\]

因为模长带有根号，在一会的拉格朗日数乘法计算过程中会十分复杂。
为了让数学过程变得“优雅”且易于计算：

1. **平方处理**：最小化 \(\|\boldsymbol{w}\|\) 等价于最小化 \(\|\boldsymbol{w}\|^2\)。平方之后，根号消失了，变成了一个平滑的二次函数。
2. **乘以 1/2**：在前面加一个 \(\frac{1}{2}\) 是为了在求导时，把平方项落下来的那个 \(2\) 给正好抵消掉（即 \(( \frac{1}{2} w^2 )' = w\)）。

于是，最终的目标函数为：

\[\min\_{\boldsymbol{w}, b} \quad \frac{1}{2}\|\boldsymbol{w}\|^2
\]

距离只跟 \(w\) 的长度有关。这也是为什么我们只要通过控制 \(w\) 的大小，就能控制这条“马路”有多宽。 限制 \(\|w\|\) 不仅仅是为了让马路宽，更是为了防止模型过拟合。马路越宽，模型对噪声的容忍度就越高，大数定律发挥的空间就越大。

## 求解

再定义新的目标函数，目标函数中要加入对错误分类的点的惩罚

\[L(w, b, \alpha) = \underbrace{\frac{1}{2}\|w\|^2}\_{\text{前面：目标}} + \underbrace{\sum\_{i=1}^{n} \alpha\_i [ 1- y\_i(w^Tx\_i + b) ]}\_{\text{后面：约束}}
\]

目标函数追求最小值，w也要追求最小值，a这时候要追求最大值，求解拉格朗日鞍点问题。

在目标函数中，我们追求总代价最小。我们不直接使用“坐标距离”，而是使用**松弛变量 \(\xi\_i\)**。当样本分错时，函数值 \(y\_i(\boldsymbol{w}^T \boldsymbol{x}\_i + b)\) 确实会小于 1，甚至小于 0。为了抵消这个“负面影响”，我们令 \(\xi\_i \ge 1 - y\_i(\boldsymbol{w}^T \boldsymbol{x}\_i + b)\)。这意味着当分错得越离谱，\(1 - (\text{负数})\) 就会变成一个**更大的正数**。因此模型在优化过程中会受到强烈的“惩罚”，被迫回头寻找能让 \(\xi\_i\) 变小的路径。

### 软间隔

硬间隔的目标函数基于一种理想假设：数据必须是线性可分的，且不允许任何样本点违背约束。然而在处理真实的 Web 流量数据时，噪声和标注误差不可避免。如果强行追求零错误，分类边界为了适配个别‘离群’的正常样本，会导致特征空间极度扭曲。这不仅增加了模型的复杂度，更会削弱其泛化能力，使得模型在面对未知的攻击变体时反而失去检测效力。

#### 软间隔 SVM 拉格朗日函数

\[L(\boldsymbol{w}, b, \xi, \alpha, \mu) = \underbrace{\frac{1}{2}\|\boldsymbol{w}\|^2 + C \sum\_{i=1}^{m} \xi\_i}\_{\textcircled{1}} + \underbrace{\sum\_{i=1}^{m} \alpha\_i (1 - \xi\_i - y\_i(\boldsymbol{w}^T \boldsymbol{x}\_i + b))}\_{\textcircled{2}} - \underbrace{\sum\_{i=1}^{m} \mu\_i \xi\_i}\_{\textcircled{3}}
\]

1. 惩罚系数 \(C\) 决定了模型对分类错误的‘容忍度’。当 \(C\) 趋向于正无穷时，模型退化为硬间隔，任何轻微的分类偏离都会产生巨大的代价值，迫使模型不惜扭曲决策边界也要实现样本的完美划分。反之，若 \(C\) 取值极小，分类错误产生的代价被大幅削弱，模型会变得更加‘佛系’，倾向于牺牲部分样本的准确性来换取一个更平滑、泛化能力更强的分类超平面。
2. 这套公式实际上是在玩一场**‘防作弊’博弈**。由于目标函数在求最小值，如果没有 \(-\mu\_i \xi\_i\) 的约束，模型会试图让 \(\xi\_i\) 变成负数来‘刷分’。这个减号项的作用就像是一个**单向压力阀**：当 \(\xi\_i\) 为正时，它在对冲中保持静默；一旦 \(\xi\_i\) 越界变负，它就会瞬间触发指数级的惩罚，让整个函数‘爆表’。这种设计不是为了计算距离，而是为了死守 \(\xi\_i \ge 0\) 这条底线。

硬间隔，只是软间隔中C为无穷的特殊情况。既然已经不接受任何错误分类，那就不需要写上这一项了。

> “拉格朗日函数本质上是一场**参数简约性（\(w, b, \xi\) 的 \(\min\)）**与**约束严苛性（\(\alpha, \mu\) 的 \(\max\)）**之间的动态博弈。模型在努力让自己变得简单的同时，裁判在拼命寻找防御漏洞并施加最大惩罚，双方最终在‘支持向量’上达到受力平衡

### 偏导数

#### 1. 对 \(w\) 求偏导：

\[\frac{\partial L}{\partial \boldsymbol{w}} = \boldsymbol{w} - \sum\_{i=1}^{m} \alpha\_i y\_i \boldsymbol{x}\_i = 0 \quad \Rightarrow \quad \mathbf{w = \sum\_{i=1}^{m} \alpha\_i y\_i x\_i}
\]

* **物理意义**：权重 \(w\) 根本不是什么神秘的东西，它就是**所有样本点的加权组合**。
* **支持向量的体现**：因为大部分 \(\alpha\_i\) 都是 0，所以只有那些**支持向量**真正决定了 \(w\) 的方向。

#### 2. 对 \(b\) 求偏导：

\[\frac{\partial L}{\partial b} = \sum\_{i=1}^{m} \alpha\_i y\_i = 0
\]

* **物理意义**：这代表在最优状态下，所有样本点对分类边界的“推力”之和必须抵消。

#### 3. 对 \(\xi\_i\) 求偏导：

这是最精彩的部分，它揭示了你刚才纠结的那个减号的最终归宿：

\[\frac{\partial L}{\partial \xi\_i} = C - \alpha\_i - \mu\_i = 0 \quad \Rightarrow \quad \mathbf{C = \alpha\_i + \mu\_i}
\]

* **物理意义**：\(C\)（总罚款）被拆成了两部分：一部分是 \(\alpha\_i\)（维持边界的压力），另一部分是 \(\mu\_i\)（防止 \(\xi\) 变负的拉力）。
* **逻辑锁死**：因为 \(\mu\_i \ge 0\)，所以这个等式强制要求了 \(\mathbf{\alpha\_i \le C}\)。
  上式是一个标准的求极值问题。在最优解处，肯定也满足偏导数这些条件。
  所以可以直接把偏导数带入到上式中。

在最终的对偶目标函数里：因为把需要最小的条件已经删了，所以新的目标函数，就是要求最大值了

\[\max\_{\alpha} \quad \underbrace{\sum \alpha\_i}\_{\text{想变大}} - \underbrace{\frac{1}{2} \sum \sum \alpha\_i \alpha\_j y\_i y\_j (x\_i \cdot x\_j)}\_{\text{互相掐架的内耗}}
\]

1. **第一项 \(\sum \alpha\_i\)**：它确实想让权重 \(\alpha\) **越大越好**。
2. **第二项（减数）**：这是**“内耗项”**。如果两个样本离得太近（内积大），它们如果都想把 \(\alpha\) 变大，这一项就会急剧增加，反而拖累了总分。
3. **约束 \(0 \le \alpha\_i \le C\)**：这是**“天花板”**。哪怕你再想变大，最高也只能到 \(C\)。

在满足 KKT 条件的约束下，SVM 的训练本质上是在寻找那些**‘边界上的异类’**。我们并不需要关注所有的样本，而是要找出那些跨越了类别鸿沟、且彼此特征差异最大的**异类支持向量**。只有当这些代表性样本被赋予最大的权重 \(\alpha\) 时，分类间隔才能被顶向极限，从而构建出鲁棒性最强的防御边界。

## KKT约束

### 1. 偏导为零（Stationarity / 平稳性）

代表在最优解处，函数的“坡度”为 0。

* **公式 A**：\(\nabla\_w L = w - \sum \alpha\_i y\_i x\_i = 0 \implies \mathbf{w = \sum \alpha\_i y\_i x\_i}\)
* **公式 B**：\(\frac{\partial L}{\partial b} = \mathbf{\sum \alpha\_i y\_i = 0}\)
* **公式 C**：\(\frac{\partial L}{\partial \xi\_i} = \mathbf{C - \alpha\_i - \mu\_i = 0}\)

### 2. 原始可行性（Primal Feasibility / 规矩）

样本点必须落在我们定义的“势力范围”内

* **公式**：\(y\_i(\mathbf{w}^T \mathbf{x}\_i + b) \ge 1 - \xi\_i\) 且 \(\xi\_i \ge 0\)
* **理解**：这是最基本的物理约束，即样本要么分对，要么乖乖交罚款 \(\xi\_i\)。

### 3. 对偶可行性（Dual Feasibility / 裁判立场）

拉格朗日乘子不能是负的。

* **公式**：\(\alpha\_i \ge 0, \quad \mu\_i \ge 0\)
* **理解**：力只能往“把样本推开”的方向使，不能把样本往禁区里拉。

在拉格朗日乘数法中，\(\alpha\_i\) 是为了处理**不等式约束** \(g(x) \le 0\) 而引入的。

* **方向一致性**：我们的目标是最小化 \(f(w)\)。如果某个约束 \(g(x) \le 0\) 被违反了（即 \(g(x) > 0\)），我们希望拉格朗日函数 \(L = f + \alpha g\) 能够产生一个巨大的**正向惩罚**。
* **数学锁死**：只有当 \(\alpha\_i \ge 0\) 时，这个惩罚才是有效的。如果 \(\alpha\_i\) 可以是负数，那么当违规发生时（\(g > 0\)），\(\alpha \cdot g\) 就会变成负数，反而帮模型减小了总分。这在逻辑上是荒谬的——相当于“越违规，分越低”。

### 4. 互补松弛性（Complementary Slackness / 灵魂）

这是最神奇的一条，它决定了**谁才是支持向量**。

* **公式 A**：\(\alpha\_i (1 - \xi\_i - y\_i(\mathbf{w}^T \mathbf{x}\_i + b)) = 0\)
* **公式 B**：\(\mu\_i \xi\_i = 0\)
* **直观理解**：**“乘积为 0”意味着两者必有一个为 0**。
  + 如果点不在边界上（括号不为 0），那么推力 \(\alpha\_i\) 必须是 0（不是支持向量）。
  + 如果推力 \(\alpha\_i > 0\)（是支持向量），那么点必须正好压在边界上（括号为 0）。
    在拉格朗日目标函数中，若样本点远离边界且分类正确（安全区），其约束项 \((1 - \text{距离})\) 会产生一个巨大的负值。此时，若盲目追求目标函数最小化，模型会产生给该点分配巨大权重 \(\alpha\) 的冲动，试图利用这个负项来“刷低”总能量。

然而，这种“投机行为”直接违背了对偶问题中 **\(\max \alpha\)** 的核心指令。由于负号的存在，\(\alpha\) 越大，函数值反而越小。为了实现**最大化**，掌握 \(\alpha\) 生杀大权的裁判会执行“清零政策”：既然你分得太好、不需要惩罚，那就剥夺你的权重。

在 \(w\) 追求最小与 \(\alpha\) 追求最大的极限拉锯下，双方达成了冷酷的平衡：**安全区的样本权重 \(\alpha\) 必须归零**。这意味着模型最终实现了**解的稀疏性**——只有那些“踩在红线上”的支持向量才有资格决定防线的走向。

## SMO求解

SMO 的精髓可以用一句话概括：**“既然一次性搞不定 10,000 个变量，那我就每次只抓两个出来‘掐架’，直到大家都不再吵架为止。”**
\*\* 为什么是两个？\*\*

* **约束限制**：还记得 KKT 条件里的 \(\sum \alpha\_i y\_i = 0\) 吗？
* **逻辑闭环**：如果你只改一个 \(\alpha\_1\)，为了维持总和为 0，你必须同时改另一个 \(\alpha\_2\) 来抵消变化。所以，**两个变量是能进行优化的最小单位**。

核心目标是解这个 \(\alpha\) 的极大值问题，同时满足两个约束：

1. **等式约束**：\(\sum\_{i=1}^{n} \alpha\_i y\_i = 0\)
2. **边界约束**：\(0 ...