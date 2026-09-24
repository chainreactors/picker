---
title: 对抗鲁棒性的形式化保证
url: https://mp.weixin.qq.com/s/S12RHWnrmclhqKEDnaBofw
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:56:54.983895
---

# 对抗鲁棒性的形式化保证

# 对抗鲁棒性的形式化保证

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 定位：本文从信息论与凸优化视角，分析对抗鲁棒性的理论极限，给出认证方法的形式化保证与不可改进性结果，讨论Lipschitz约束方法与开放问题。面向研究者和高级安全工程师。

---

## 一、鲁棒性的信息论基础

### 1.1 鲁棒半径与模型复杂度的关系

定义模型 f 在点 x 的鲁棒半径：

```
r(f, x) = sup { ε : ∀ x', ‖x' - x‖ ≤ ε ⟹ f(x') = f(x) }
```

**定理1（鲁棒半径-复杂度权衡）**：对参数量为 p、Lipschitz常数为 L 的模型，平均鲁棒半径满足：

```
E_x[r(f, x)] ≤ O(1/L)
```

且在样本量 n 固定时：

```
E_x[r(f, x)] = O(1/√(p/n))
```

**含义**：

* 模型越"陡峭"（L大），鲁棒半径越小。
* 模型越复杂（p大）相对数据量（n），鲁棒半径越小。这是"过拟合导致对抗脆弱性"的信息论解释。

### 1.2 鲁棒性-准确性权衡的信息论证明

**定理2（鲁棒性-准确性权衡）**：对任意分类器 f，在数据分布 D 下：

```
Acc(f) + λ·Rob(f) ≤ 1 - I(Y; X_boundary) + λ·r_max
```

其中：

* Acc(f) 为标准准确率。
* Rob(f) 为鲁棒准确率（在 ε 扰动下）。
* I(Y; X\_boundary) 为标签与决策边界附近特征互信息。
* r\_max 为最大可达鲁棒半径。

**直觉**：决策边界附近的样本携带分类信息，但这些样本的鲁棒半径小。要提升鲁棒性，必须把决策边界推离这些样本，但此时边界附近的其他类样本准确率下降。

**推论**：在"特征空间中两类样本接近"的分布下，鲁棒准确率严格小于标准准确率，且差距随两类接近程度增大。

### 1.3 鲁棒性的信息论下界

**定理3（Tsipras等）**：存在数据分布 D 使得任意分类器满足：

```
Acc(f) - Rob(f, ε) ≥ Ω(ε·d)
```

其中 d 为数据维度。

**含义**：在高维空间中，鲁棒性与准确性的差距随维度线性增长。这是"高维模型对抗脆弱"的根本原因。

---

## 二、认证方法的理论

### 2.1 Randomized Smoothing的数学保证

Randomized Smoothing 将基分类器 f 转化为平滑分类器：

```
g(x) = argmax_c P(f(x + N(0, σ²I)) = c)
```

**定理4（Cohen等）**：若 g(x) = c 且 `p_c = P(f(x + N(0, σ²I)) = c) > 1/2`，则 g 在半径 R 内认证为 c：

```
R = σ · (Φ⁻¹(p_c) - Φ⁻¹(p_lower))
```

其中 p\_lower 为 p\_c 的置信下界，Φ 为标准正态CDF。

**保证的严格性**：此保证对任意攻击（不限攻击算法、不限计算预算）成立，是"认证"而非"经验"鲁棒性。

**局限**：

* 平滑分类器 g ≠ 原分类器 f，认证的是 g 而非 f。
* σ 越大认证半径越大，但 g 与 f 偏差越大，g 的准确率越低。
* 认证半径在高维空间中相对输入尺度仍很小（R = O(σ√(log(1/α)))，与维度无关但绝对值小）。

### 2.2 IBP的保守性分析

IBP（Interval Bound Propagation）逐层传播输入区间，得到输出的区间界。

**定理5（IBP保守性）**：IBP给出的鲁棒半径 R\_IBP 满足：

```
R_IBP ≤ R_true
```

且在某些网络结构下：

```
R_IBP ≤ R_true / L
```

其中 L 为网络层数。

**保守性来源**：IBP假设每层的区间独立最坏，忽略层间相关性，导致界松弛。深层网络中此松弛指数增长。

### 2.3 CROWN的改进

CROWN（CROWN-IBP）用线性上下界代替区间界，部分恢复层间相关性：

**定理6（CROWN改进）**：CROWN给出的鲁棒半径 R\_CROWN 满足：

```
R_IBP ≤ R_CROWN ≤ R_true
```

且在特定网络结构下 R\_CROWN 可指数优于 R\_IBP。

**局限**：CROWN的计算开销随网络深度增长，深层网络中实际应用受限。

### 2.4 认证极限

**定理7（认证半径上界）**：对任意认证方法 A，存在网络 f 与输入 x 使得：

```
R_A(f, x) ≤ R_true(f, x) / poly(d)
```

其中 d 为维度。

**含义**：任何多项式时间认证方法都无法精确计算鲁棒半径，必然存在多项式级别的保守性。

**定理8（不可认证区域存在性）**：对任意非平凡分类器 f，存在输入 x 使得 x 的真实鲁棒半径为正，但任意多项式时间认证方法给出的认证半径为零。

**直觉**：决策边界的精确位置在一般网络中不可计算（涉及ReLU等非线性激活的精确求根），认证方法只能给出保守界。

---

## 三、Lipschitz约束方法

### 3.1 Lipschitz连续性与鲁棒性的关系

**定理9**：若 f 是 L-Lipschitz 的（对输入），则对 ‖x' - x‖ ≤ ε：

```
‖f(x') - f(x)‖ ≤ L·ε
```

若 f(x) 的最大logit与次大logit之差为 Δ，则 f 在半径 `R = Δ/(2L)` 内鲁棒。

**含义**：控制Lipschitz常数直接给出鲁棒保证。1-Lipschitz网络在半径 Δ/2 内鲁棒。

### 3.2 1-Lipschitz网络的设计

**逐层Lipschitz控制**：网络的Lipschitz常数为各层Lipschitz常数之积：

```
L(f) = ∏_i L(layer_i)
```

设计每层为1-Lipschitz则整体为1-Lipschitz。

**1-Lipschitz层的设计**：

1. **正交线性层**：权重矩阵 W 满足 W^T W = I（正交），则 L(W) = 1。
2. **Lipschitz激活**：ReLU 的 Lipschitz 常数为1，但更优选择是 GroupSort 等保持梯度的激活。
3. **谱归一化**：对每层权重做 `W / σ_max(W)`，σ\_max 为最大奇异值。

```
class LipschitzLinear(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(out_dim, in_dim))
        self.bias = nn.Parameter(torch.zeros(out_dim))

    def forward(self, x):
        # 谱归一化：除以最大奇异值
        W = self.weight / torch.linalg.matrix_norm(self.weight, ord=2)
        return x @ W.T + self.bias
```

### 3.3 Lipschitz方法的局限

**定理10（Lipschitz-表达力权衡）**：1-Lipschitz网络的表达能力严格弱于一般网络。存在函数可由一般网络多项式表达，但1-Lipschitz网络需指数参数。

**实践影响**：强制1-Lipschitz导致模型表达能力下降，标准准确率显著低于非约束网络。

**权衡**：实际中不强制1-Lipschitz，而是控制Lipschitz常数在合理范围（如 L = 10），在鲁棒性与准确率间权衡。

---

## 四、认证方法的不可改进性

### 4.1 多项式时间认证的极限

**定理11（认证硬度）**：精确计算神经网络的鲁棒半径是 NP-难的（归约自SAT）。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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