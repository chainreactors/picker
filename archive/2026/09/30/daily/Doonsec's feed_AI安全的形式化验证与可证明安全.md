---
title: AI安全的形式化验证与可证明安全
url: https://mp.weixin.qq.com/s/4NoSpRQdepjfvOugy7ClSw
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:56:35.945042
---

# AI安全的形式化验证与可证明安全

# AI安全的形式化验证与可证明安全

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 定位：本文作为高级篇收官，系统讨论AI安全形式化验证的方法论、运行时验证框架、可证明安全框架与统计验证方法，并审视"从可信AI到可证明AI"的终极问题。面向研究者和高级安全工程师。

---

## 一、形式化验证方法

### 1.1 模型行为的形式化规约

将安全属性形式化为逻辑规约 φ，验证模型 M 是否满足 φ：

```
M ⊨ φ    （M 满足 φ）
```

**规约类型**：

1. **逐点属性**：∀x ∈ S, P(M(x))（特定输入集上的属性）。
2. **鲁棒性属性**：∀x, ∀x' ∈ B(x,ε), M(x) = M(x')（局部鲁棒性）。
3. **等价性属性**：∀x, M₁(x) = M₂(x)（模型等价，用于验证压缩/微调后行为不变）。
4. **隐私属性**：M 满足 (ε,δ)-DP。

**规约语言**：常用时序逻辑（LTL/CTL）或一阶逻辑表达安全属性。

### 1.2 属性验证算法

**SMT求解方法**：将神经网络与安全属性编码为SMT公式，用SMT求解器判定可满足性。

```
φ_safety ∧ ¬φ_model_behavior    （若UNSAT，则M ⊨ φ_safety）
```

**编码**：

* ReLU激活：用析取编码（y = max(0, x) ⟺ (x ≥ 0 ∧ y = x) ∨ (x < 0 ∧ y = 0)）。
* 矩阵乘法：用线性约束编码。
* Softmax：用指数约束近似（或用Top-1近似简化）。

```
from z3 import *

def verify_robustness(model, x, epsilon, target_class):
    solver = Solver()
    # 编码输入扰动
    x_adv = [Real(f'x_{i}') for i in range(len(x))]
    for i in range(len(x)):
        solver.add(x_adv[i] >= x[i] - epsilon)
        solver.add(x_adv[i] <= x[i] + epsilon)
    # 编码模型计算（简化示意）
    logits = encode_model(model, x_adv)
    # 编码"误分类"条件
    for c in range(model.n_classes):
        if c != target_class:
            solver.add(logits[c] > logits[target_class])
    # 若UNSAT，则鲁棒
    return solver.check() == unsat
```

**定理1（SMT完备性）**：对有限ReLU网络与线性属性，SMT求解是完备的（若UNSAT则属性成立，若SAT则存在反例）。

**局限**：SMT求解对大网络指数级开销，十亿参数模型不可行。

### 1.3 SMT求解在AI安全中的应用

**可行规模**：当前SMT求解器可处理数千参数的网络验证。

**应用场景**：

* **小模型认证**：对安全关键的小模型（如医疗诊断）做完整属性验证。
* **子系统验证**：对大模型的关键子系统（如安全过滤层）做独立验证。
* **对抗训练验证**：验证对抗训练后的模型在特定输入集上的鲁棒性。

---

## 二、运行时验证

### 2.1 在线安全属性监控

运行时验证在推理时检查模型输出是否满足安全属性，不满足则触发响应。

```
class RuntimeVerifier:
    def __init__(self, properties, responses):
        self.properties = properties
        self.responses = responses

    def check(self, model, x):
        output = model(x)
        violations = []
        for prop in self.properties:
            if not prop.check(x, output):
                violations.append(prop)
        if violations:
            return self._respond(violations, output)
        return output

    def _respond(self, violations, output):
        # 按严重性选择响应
        for v in sorted(violations, key=lambda p: -p.severity):
            response = self.responses[v.type]
            output = response.apply(output, v)
        return output
```

### 2.2 运行时断言

**断言类型**：

1. **输出范围**：output ∈ [min, max]。
2. **类别一致性**：若 x ∈ class\_A，则 M(x) ∈ class\_A。
3. **鲁棒性检查**：对关键输入做轻量鲁棒性验证。
4. **延迟约束**：推理延迟 ≤ threshold。

```
class SafetyAssertion:
    def __init__(self, check_fn, on_violation):
        self.check = check_fn
        self.on_violation = on_violation

    def verify(self, x, output):
        if not self.check(x, output):
            return self.on_violation(x, output)
        return output
```

### 2.3 安全违规的实时检测与响应

**响应策略**：

* **拒绝输出**：返回安全默认值。
* **降级输出**：返回保守但安全的输出。
* **告警+人工**：标记为需人工审查。
* **模型回退**：切换到已验证的备用模型。

```
class ViolationResponse:
    def __init__(self, strategy="reject"):
        self.strategy = strategy

    def apply(self, output, violation):
        if self.strategy == "reject":
            return self._safe_default()
        elif self.strategy == "degrade":
            return self._degrade(output, violation)
        elif self.strategy == "fallback":
            return self._fallback_model(output)
```

**定理2（运行时验证保证）**：运行时验证保证输出满足被检查的属性，对任意模型行为成立。

**局限**：仅对已编码的属性有效，未编码的安全违规不被检测。运行时开销可能影响延迟。

---

## 三、可证明安全框架

### 3.1 AI安全的形式化证明框架

**框架结构**：

```
证明目标：M ⊨ φ
证明依据：
  1. 模型属性：M ∈ ModelClass（如Lipschitz ≤ L）
  2. 输入约束：x ∈ InputSet（如‖x‖ ≤ B）
  3. 数学定理：Theorem(ModelClass, InputSet) → φ
证明过程：将1,2代入3，得 M ⊨ φ
```

**示例**：

```
目标：M 在 x 处 ε-鲁棒
依据：
  1. M 是 L-Lipschitz
  2. margin(M, x) = Δ
  3. 定理：L-Lipschitz + margin Δ ⟹ ε = Δ/(2L) 鲁棒
结论：M 在 x 处 Δ/(2L)-鲁棒
```

### 3.2 安全假设的形式化

可证明安全依赖假设，假设需显式声明与验证：

```
@dataclass
class SafetyProof:
    property: str           # 被证明的安全属性
    assumptions: list       # 依赖的假设
    theorem: str            # 使用的数学定理
    verification: dict      # 假设的验证结果

    def is_valid(self):
        return all(a.verified for a in self.assumptions)
```

**假设类型**：

1. **模型假设**：Lipschitz常数、权重范数、架构约束。
2. **数据假设**：输入分布、范数界、语义约束。
3. **计算假设**：攻击者计算预算、访问权限。

**定理3（假设违反传播）**：若假设 A\_i 不成立，则基于 A\_i 的证明结论不保证。具体影响取决于 A\_i 在证明中的角色。

### 3.3 证明的可验证性

**问题**：安全证明本身是否可被独立验证？

**方法**：

1. **机器可检查证明**：用证明助手（如Coq、Lean、Isabelle）生成机器可检查的证明。
2. **证明证书**：生成可独立验证的证明证书，验证者无需信任证明者。
3. **ZKP证明**：零知识证明使验证者确信证明成立但不知模型细节。

```
class ProvableSafety:
    def __init__(self, model, property_spec, proof_system):
        self.model = model
        self.spec = property_spec
        self.prover = proof_system

    def prove(self):
        # 1. 收集模型属性
        properties = self._extract_properties(self.model)
        # 2. 生成证明
        proof = self.prover.prove(self.spec, properties)
        # 3. 验证证明
        if self.prover.verify(proof):
            return SafetyProof(property=self.spec, proof=proof)
        return None
```

---

## 四、统计验证方法

### 4.1 PAC-Bayes安全界

PAC-Bayes框架提供泛化保证：以高概率，模型在未见数据上的性能接近训练性能。

**定理4（PAC-Bayes鲁棒性界）**：对后验分布 Q 上的模型，以概率 ≥ 1-δ：

```
E_{M~Q}[Rob(M)] ≥ E_{M~Q}[Rob_train(M)] - √((KL(Q||P) + ln(2/δ)) / (2n))
```

其中 Rob 为鲁棒准确率，P 为先验，n 为样本量。

**含义**：训练集上的鲁棒性能推广到测试集，差距由 KL 散度与样本量决定。

**应用**：对对抗训练模型给出"在未见攻击上的鲁棒性"的概率保证。

### 4.2 统计模型检查

对难以形式化验证的属性，用统计方法估计满足概率：

```
class StatisticalModelChecker:
    def __init__(self, model, property_spec, sampler):
        self.model = model
        self.spec = property_spec
        self.sampler = sampler

    def check(self, n_samples=10000, confidence=0.99):
        violations = 0
        for _ in range(n_samples):
            x = self.sampler.sample()
            output = self.model(x)
            if not self.spec.check(x, output):
                violations += 1
        # 置信区间
        p_violate = violations / n_samples
        ci = self._confidence_interval(p_violate, n_samples, confidence)
        return {
            "violation_rate": p_violate,
            "confidence_interval": ci,
            "verdict": "likely_safe" if p_violate < self.threshold else "unsafe",
        }
```

**定理5（统计验证保证）**：n 次独立采样后，真实违反率 r 满足：

```
P(|r̂ - r| > ε) ≤ 2·exp(-2nε²)
```

即估计误差以指数速率收敛。

### 4.3 随机化验证的置信度保证

**方法**：对模型参数做随机扰动，验证扰动模型满足属性的概率：

```
P_{M~Q}[M ⊨ φ] ≥ 1 - β
```

**含义**：不验证单个模型，而是验证"模型族"以高概率满足属性。这比单模型验证更鲁棒（对参数微扰不敏感）。

---

## 五、终极问题

### 5.1 AI安全的可证明保证是否可达

**核心问题**：对生产级AI系统，可证明安全保证是否实际可达？

**乐观论据**：

* 特定属性（如Lipschitz界、DP保证）已可证明。
* 形式化验证工具持续进步，可处理规模增长。
* 架构级安全设计可减少需验证的属性数量。

**悲观论据**：

* 通用语义安全（如"不输出有害内容"）难以形式化。
* 大模型的复杂性使完整验证计算不可行。
* 安全属性随威胁演化，需持续重新验证。

**折中观点**：可证明安全对"特定属性"可达，对"通用安全"不可达。工程目标应是"关键属性可证明 + 其余属性经验验证"的混合策略。

### 5.2 形式化验证的实用性边界

**当前可行**：

* 小模型（< 1M参数）的完整属性验证。
* 大模型特定子系统的验证。
* 架构级约束的验证（如Lipschitz、权限）。
* 运行时关键属性的监控。

**当前不可行**：

* 十亿参数模型的完整属性验证。
* 通用语义属性的验证。
* 所有可能输入的穷举验证。

**发展趋势**：验证工具能力随硬件与算法进步增长，但模型规模增长更快。实用性边界是否随时间改善取决于"验证能力增速 vs 模型规模增速"。

### 5.3 从"可信AI"到"可证明AI"

**可信AI（Trusted AI）**：通过测试、审计、经验评估建立信任。

* 优势：实用、可扩展。
* 劣势：不提供形式化保证，可能遗漏未测试的风险。

**可证明AI（Provable AI）**：通过形式化证明建立保证。

* 优势：形式化保证，覆盖所有情况。
* 劣势：计算开销大，属性覆盖有限。

**混合策略**：

```
安全保证 = 可证明部分（关键属性） + 可信部分（其余属性）
```

**分层验证框架**：

```
Layer 1: 形式化验证（架构约束、权限、Lipschitz）
Layer 2: 认证鲁棒性（关键输入的鲁棒半径）
Layer 3: 统计验证（大规模随机测试的置信保证）
Layer 4: 运行时验证（在线安全监控）
Layer 5: 经验评估（红队测试、对抗评估）
```

每层覆盖不同属性类型与保证强度，组合提供"虽不完备但有层次"的安全保证。

**终极愿景**：AI系统附带"安全证明书"，声明哪些属性可证明、哪些属性统计验证、哪些属性经验评估，用户可据此做风险知情决策。这是从"相信AI安全"到"证明AI安全"的范式转变。

---

## 六、形式化验证的深化

### 6.1 SMT求解的能力与局限

**能力**：对有限ReLU网络与线性属性，SMT求解完备。

**局限**：对大网络指数级开销，十亿参数模型不可行。

**可行规模**：当前SMT可处理数千参数的网络验证。

### 6.2 运行时验证的理论

**定理**：运行时验证保证输出满足被检查的属性，对任意模型行为成立。

**局限**：仅对已编码属性有效，运行时开销影响延迟。

预览时标签不可点

不喜欢

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