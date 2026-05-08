---
title: 万能近似定理：为什么一个神经网络就能模拟整个宇宙？
url: https://mp.weixin.qq.com/s/TQxzsjUboIApbsVGe40-sA
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:51:02.922950
---

# 万能近似定理：为什么一个神经网络就能模拟整个宇宙？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hyaRUFucbboOo4tGUMdJnt8BTZueNocauGfuIbiaX4OG575jc7vVRYcueVcL7qSB3sox2cZEicibagml0pd9gyVEMsJHcmr6zl5TZflyyiblYibI/0?wx_fmt=jpeg)

# 万能近似定理：为什么一个神经网络就能模拟整个宇宙？

原创

代码小铺
代码小铺

代码小铺

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbboF1g6tzJs4fPMKKbbcO9GEuALsgIk2YLev7EBlcDw9l5vbuv3wyP8DgrGr2dg8dL9eTEoJqPoekk1OrpnticoBDibMln3ibFGyxY/640?from=appmsg)

---

> 给我一个隐藏层，我就能逼近世间万物。

1989 年，两篇几乎同时发表的论文，彻底改变了人类对"学习"的理解。

George Cybenko 在 *Mathematics of Computation* 上证明了：**仅含一个隐藏层的前馈神经网络，只要激活函数是连续的、非多项式的、且有界的（如 sigmoid），就能以任意精度逼近定义在紧致子集上的任意连续函数。**

几乎同时，Kurt Hornik、Maxwell Stinchcombe 和 Halbert White 在 *Neural Networks* 上发表论文，证明了更一般的结果：**多层前馈网络是万能近似器，其逼近能力不依赖于激活函数的具体形式，只要它不是多项式即可。**

这就是著名的**万能近似定理（Universal Approximation Theorem, UAT）**。

用数学语言表述：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbqHdibNxsg01AVT1p7A7BzjMX8ZvRCSwFAPZQtZyqDCQpGyqdHTI13e6LtibxNyrcYiagMdnH8oVqJ8pkaMtmtu3PNqdpqexHBaR4/640?from=appmsg)

其中 σ 是激活函数，如 sigmoid：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbboqLcSrLmZdsiakJTBbKicQvgBfQliaLzDHSBaIRXVDKjegVtyR8AyuWpOicpibvqJIK0cMv0KXibU0BP0BP8kVlxBcLBDN9d7ibydQts/640?from=appmsg)

或 ReLU：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbrBYAqKu4we27pqC0C0gk7T5C4c04pb36C78sDTvFacGsK3rJvSnvk7A68oVBAKAayjhdm3lsR0ZgFccTQLxQ52mmzt9h4iaSe8/640?from=appmsg)

定理断言：对于任意连续函数 f 和任意精度 ε，总能找到一组参数 {αⱼ, wⱼ, bⱼ}，使得 G(x) 与 f(x) 的差异小于 ε。

---

## 二、万能近似定理的深远意义

### 2.1 哲学意义：有限能否表达无限？

万能近似定理触及了一个深刻的哲学命题：**有限的结构能否表达无限的可能性？**

**有限与无限的辩证。** 一个只有单个隐藏层的神经网络，参数数量是有限的——有限个权重、有限个偏置、有限个神经元。然而，它能逼近的函数空间却是无限的——任何连续函数，无论多么复杂。这让人联想到莱布尼茨的"单子论"：最简单的单元，通过恰当的排列组合，可以反映整个宇宙的复杂性。

**从"是什么"到"能做什么"。** 万能近似定理并不告诉我们神经网络**实际学习**了什么函数，而是告诉我们它**有能力表达**任何函数。这是一个"存在性定理"——它回答的是"能不能"的问题，而非"怎么做"的问题。哲学家会注意到，这与柏拉图的理念论有着微妙的呼应：理念世界中的所有形式，都潜在地存在于一个简单的架构之中。

**复杂性的涌现。** 单个神经元只能做一件简单的事：计算加权和，然后通过一个非线性函数激活。但当成千上万个这样的单元被组合在一起时，涌现出了逼近任意复杂函数的能力。这正是"整体大于部分之和"的数学体现。

**认知的隐喻。** 人类大脑也遵循类似的原理：单个神经元功能简单，但 860 亿个神经元的连接却产生了意识、创造力和情感。万能近似定理为这种"简单单元→复杂认知"的涌现提供了数学上的类比。

### 2.2 自然科学意义：逼近自然的数学语言

万能近似定理不仅是工程定理，它与自然科学的核心思想深度共鸣。

**泰勒级数的精神继承者。** 泰勒定理告诉我们，任何光滑函数都可以用多项式来局部逼近：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbrzMiby4LxkxwpN2ibEIbDBM7zTt4fB48hv7pSjjPAKzyo7o69yyHMrRymSohXsVVpAzRrm4R6t2cK0Ru0ncxAxPoNrM49yW3ZicM/640?from=appmsg)

万能近似定理是泰勒思想的"全局化"和"非线性化"：它不要求函数是光滑的（只需连续），也不局限于多项式基，而是用 σ(w·x + b) 这样的非线性基函数。可以说，**神经网络是比泰勒展开更强大的"万能基"。**

**魏尔斯特拉斯逼近定理的推广。** 1885 年，魏尔斯特拉斯证明了：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbpukMVfgOjPcHDicLicVA7vU2WE3mriakrIGiaQXZwhLuFpI1WdbPQA2tesp8SL4cyfpjW5FibYN0WibiaEjFaD7vhxytgHeOmTosIk0g/640?from=appmsg)

这是经典分析学中最著名的逼近定理。万能近似定理可以看作是这个定理的"神经网络版本"——用 σ(w·x + b) 的线性组合替代了多项式。两者在精神上一脉相承，但 UAT 的适用范围更广。

**物理学中的基展开。** 在量子力学中，任何波函数都可以用一组正交基函数展开（如傅里叶级数、球谐函数）。万能近似定理告诉我们：神经网络的非线性激活函数，本身就可以作为"自适应基"。这为物理学中的函数逼近问题提供了一种全新的视角。

**信息压缩的自然法则。** 自然界似乎偏爱"简单规则生成复杂模式"——DNA 的四个碱基编码了生命的全部信息，基本粒子的有限种类构成了万物的基础。万能近似定理在数学上刻画了这一自然法则：有限的计算单元，足以表达无限的自然现象。

### 2.3 技术意义：AI 时代的理论基石

万能近似定理是现代人工智能的**理论合法性证明**。

**深度学习为什么有效。** 在 UAT 之前，人们对神经网络的表达能力缺乏严格的理论保证。UAT 证明了：**只要网络足够宽（或足够深），就没有神经网络无法表示的函数。** 这为整个深度学习领域提供了坚实的理论基础。

**函数逼近的统一框架。** 无论是图像识别、自然语言处理、自动驾驶，还是 AlphaGo 的棋局评估，本质上都是在做一件事：用神经网络去逼近某个未知函数。UAT 保证了这件事在理论上是可行的。

**科学计算的范式革命。** 近年来，"物理信息神经网络"（PINN）、"神经算子"（Neural Operator）、"傅里叶神经算子"（FNO）等新兴方法，将万能近似定理的思想从"逼近函数"推广到"逼近算子"——即学习函数到函数的映射。这正在彻底改变流体力学、材料科学、气象学等领域的计算范式。

**从"万能"到"有效"。** 需要强调的是，UAT 是一个存在性定理。它保证了网络**能够**逼近目标函数，但没有告诉我们**如何找到**这些参数（这是训练算法的任务），也没有告诉我们需要**多大的网络**（这是效率和泛化的问题）。理解这些局限，对于正确使用神经网络至关重要。

---

## 三、原论文的核心论述

在深入推导之前，让我们先回到 1989 年的原始文献。

### 3.1 Cybenko (1989) 的经典论文

George Cybenko 的论文 *"Approximation by superpositions of a sigmoidal function"*（发表于 *Mathematics of Computation*, Vol. 55, No. 192）是万能近似定理的开山之作。

论文开篇即指出：

> *"We demonstrate that finite linear combinations of compositions of a fixed sigmoidal function can approximate any continuous function of many real variables with any degree of accuracy."*

Cybenko 的核心洞察是：**sigmoid 函数的平移和缩放版本，可以用来构造"阶梯函数"，而阶梯函数的线性组合可以逼近任何连续函数。**

论文中的关键定理（Theorem 1）表述如下：

> 令 σ 为连续 sigmoidal 函数（即 σ(x) → 1 当 x → +∞，σ(x) → 0 当 x → −∞）。则形如
>
> G(x) = ∑ αⱼ σ(wⱼ·x + bⱼ)
>
> 的函数集合在 C(Iₙ) 中是稠密的。

### 3.2 Hornik, Stinchcombe & White (1989) 的推广

几乎同时，Hornik 等人的论文 *"Multilayer Feedforward Networks Are Universal Approximators"*（发表于 *Neural Networks*, Vol. 2, No. 5）给出了更一般的结果。

他们的关键贡献是：

> *"We show that standard multilayer feedforward networks with as few as one hidden layer, using arbitrary squashing functions, are capable of approximating any Borel measurable function from one finite dimensional space to another to any desired degree of accuracy."*

注意这里的措辞：**"arbitrary squashing functions"（任意挤压函数）**——这意味着激活函数不需要是 sigmoid，只需要满足一些很弱的条件。

他们进一步证明：

> *"Multilayer feedforward networks can be viewed as implementing a class of nonlinear regression functions. Their approximation capabilities depend on the architecture (number of layers, number of units per layer) and the choice of activation function."*

---

## 四、万能近似定理的完整推导

现在，让我们进入最令人期待的部分——**证明万能近似定理**。

我们将主要遵循 Cybenko (1989) 的证明思路，并结合 Hornik 等人的推广视角。

### 4.1 证明的总体策略

证明的核心思想分为三步：

1. 1. **用 sigmoid 构造阶梯函数**——sigmoid 函数在极限情况下可以逼近阶跃函数
2. 2. **用阶梯函数构造"隆起函数"（bump function）**——两个阶跃函数相减，得到一个局部的隆起
3. 3. **用隆起函数的线性组合逼近任意连续函数**——将定义域划分为小区间，在每个区间上用隆起函数逼近目标函数的值

这是一个典型的"积木式"逼近策略：从最简单的构件出发，逐步搭建出逼近任意复杂函数的能力。

### 4.2 预备：函数空间与稠密性

首先，我们需要理解"稠密"（dense）这个概念。

设 C(Iₙ) 是定义在 n 维单位超立方体 Iₙ = [0, 1]ⁿ 上的所有连续函数的集合。我们说一组函数 V 在 C(Iₙ) 中是**稠密**的，意思是：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbpWL3pG2mH6zpdZe3h0UlhwyWFMbMibmEEXOkjKHuRvYETQhWkm0v0V9ywkKk50HWY5xBYPemTfZGl2sviccjcbONqoKlgNNNtRI/640?from=appmsg)

换句话说，对于任何连续函数 f 和任何精度 ε，都能在 V 中找到一个函数，它与 f 的差异处处小于 ε。

### 4.3 第一步：从 sigmoid 到阶跃函数

sigmoid 函数 σ(x) = 1/(1 + e⁻ˣ) 有一个重要性质：当我们将输入缩放一个很大的系数 k 时，它会越来越像一个阶跃函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbpia9qewiagD5tOH9fiadPRRUShMmF7Zgcj82IDNZ554Jic0AxH6yrSPtLnTL8BTFCWPU0ApZIiap4g10xk28NibfyiaXrxu3FibiawFUQA/640?from=appmsg)

sigmoid 函数的极限行为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbqChBWhsljAhFqsFWrJggG8NxDKuMJSGCTdODvicgibzIMUxweA0512Gnuiazl8icRxYAB3zC6znKSXn3BP1x4TMRhBf9hqib2Od7zg/640?from=appmsg)

这个结论的直观理解是：当 k 很大时，对于 x > θ，k(x − θ) 是一个很大的正数，σ 趋近于 1；对于 x < θ，k(x − θ) 是一个很大的负数，σ 趋近于 0。

在 x = θ 处，σ(k(x − θ)) = σ(0) = 1/2，但这是一个单点，不影响连续函数的逼近。

### 4.4 第二步：从阶跃函数到隆起函数

有了阶跃函数，我们可以构造一个**隆起函数（bump function）**。

在一维情况下，两个反向的阶跃函数相减，可以得到一个"隆起"：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbpibQGKn85bgicdmEc7xRbpOAfibiancdjNhCmVFBtRicaT6B9DxXdw9H481jKpciclSYeXEjpnKNS93QsBarQk2xHP0nu5axkoRpqjI/640?from=appmsg)

当 A 很大时，s(x) 在区间 [−1/2, 1/2] 上近似为 1，在区间外近似为 0。这就像一个"积木块"——我们可以把它放在定义域的任意位置，控制它的高度和宽度。

在二维情况下，我们可以构造"方柱函数"：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbpNFOnkOLT2XqDR7XbBDpanc2er9OLQNsdDsOMOnyuvGIT0IzibIibGWTZYoqz6ibibO8tkAfvp1X9qfWyxHcrRA5feyoofbpNmDWA/640?from=appmsg)

通过适当选择参数，这个函数在一个矩形区域内近似为 1，在区域外近似为 0。

这个构造可以推广到任意维度：在 n 维空间中，我们可以通过 n 对反向的阶跃函数来构造一个"超立方体隆起函数"。

### 4.5 第三步：用隆起函数逼近任意连续函数

现在，关键的洞察来了。

**任意连续函数，在足够精细的划分下，可以用分段常函数来逼近。** 这是连续函数的基本性质——连续性意味着在足够小的区间上，函数值的变化可以任意小。

具体地，将定义域 [0, 1] 划分为 M 个等长的小区间：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbo7nbIcTDGCxVSKWIkBCMkSqoy6xghXs7EhcXnZFqToNGvWO7HThyEQeGicibdl6FdoI4Nia3a1qO4NxFEyxE0flPogtib4585eXGI/640?from=appmsg)

在每个小区间 [(i−1)/M, i/M) 上，函数 f(x) 近似为常数 f(xᵢ)。因此：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbqyBtSYtC4gp9kSXW3urzibviaacKq6kcx1Jvy1J7o32wk3xXkX3eszicrtdb4ftcgzzPs3FoND6WIEtiaLdpI9Tv322UibpHsxicALY/640?from=appmsg)

由于 f 是连续函数，当 M 足够大时，这个近似的误差可以小于任意给定的 ε。

而每个指示函数 1\_{[(i−1)/M, i/M)} 都可以用隆起函数 s(Mx − i + 1/2) 来逼近。因此，f(x) 可以用隆起函数的线性组合来逼近。

而每个隆起函数本身就是 sigmoid 函数的线性组合。因此，**f(x) 可以用 sigmoid 函数的线性组合来逼近。**

### 4.6 Cybenko 的严格证明：Hahn-Banach 定理

上面的构造给出了直观的几何理解，但 Cybenko 的原论文使用了一个更优雅、更严格的证明方法——**基于 Hahn-Banach 定理和 Riesz 表示定理的泛函分析证明**。

证明的核心思路：

**要证明一组函数 V 在 C(Iₙ) 中是稠密的，只需证明：任何与 V 中所有函数正交的测度 μ，必然是零测度。**

这是一个经典的对偶性论证：

> 如果 V 在 C(Iₙ) 中不稠密，则由 Hahn-Banach 定理，存在一个非零的有界线性泛函（由 Riesz 表示定理，它可以表示为一个测度 μ），使得 μ 与 V 中所有函数正交。
>
> 因此，如果我们能证明：任何与 V 中所有函数正交的测度 μ 必须是零测度，那...