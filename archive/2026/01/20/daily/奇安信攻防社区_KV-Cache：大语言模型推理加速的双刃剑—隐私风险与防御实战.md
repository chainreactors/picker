---
title: KV-Cache：大语言模型推理加速的双刃剑—隐私风险与防御实战
url: https://forum.butian.net/share/4726
source: 奇安信攻防社区
date: 2026-01-20
fetch_date: 2026-01-21T03:31:34.144919
---

# KV-Cache：大语言模型推理加速的双刃剑—隐私风险与防御实战

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

### KV-Cache：大语言模型推理加速的双刃剑—隐私风险与防御实战

在2025年，大语言模型（LLM）推理服务已全面进入多租户时代，KV Cache作为核心加速技术，让Prefill阶段并行计算、Decode阶段复用历史键值，带来5–8倍的吞吐提升。然而，这把“双刃剑”也暴露了严重的安全隐患：共享缓存下的时序侧信道可直接泄露用户Prompt；更隐蔽的History Swapping能悄无声息劫持输出话题；腐败攻击则通过扰动Key向量引发幻觉与性能崩坏。

0x01 研究背景
---------
在自回归生成模型（Autoregressive Model）中，LLM每生成一个新token，都会将此前生成的序列作为输入。若每一步都重新计算全部注意力（Q、K、V 矩阵），计算量将随序列长度平方级增长。在长上下文和高并发场景下，这一开销会迅速成为系统瓶颈。为此，主流推理框架普遍引入KV-Cache技术。 KV-Cache通过缓存此前token的Key（K）和Value（V）向量，在下一步生成时只需计算新的Query（Q），即可直接复用前面的K/V，从而显著降低重复计算量。实践中，KV-Cache 通常能在保持模型精度不变的前提下，带来约5-8倍的推理加速。这一机制已经成为vLLM、SGLang、DeepSpeed-Inference等高性能推理引擎，以及Hugging Face `generate(use\_cache=True)`接口的默认能力。
随着2024–2025年多租户推理服务（如vLLM、SGLang、TensorRT-LLM）的大规模部署，系统在单模型、多租户共享的前提下，又进一步引入跨请求的前缀缓存共享（prefix caching）。当不同请求的prompt存在相同前缀时，系统可以直接复用已有KV-Cache，大幅摊薄Prefill成本并提升吞吐。然而，当这种共享与复用机制扩展到多租户并发环境时，KV-Cache不再只是一个“性能优化组件”，而是演变成新的攻击面：攻击者可以通过观测Prefill 时间、TTFT等性能差异发起时序侧信道攻击，通过篡改缓存内容实施History Swapping（生成轨迹劫持），或者通过对Key向量注入扰动发动Cache Corruption（缓存腐败），从而导致跨租户信息泄露、话题漂移甚至下游任务性能显著下降。
0x02 KV缓存工作机制与共享复用原理
--------------------
下面是KV-Cache工作原理的示意图。
![KV-Cache工作原理](https://l1yee.oss-cn-beijing.aliyuncs.com/KV%20Cache%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86.gif)
​
KV-Cache工作原理图
​
接下来我们用文字详细拆解，更深入了解KV缓存工作机制。
### 2.1 两阶段推理：Prefill与Decode
KV-Cache的核心做法分为两阶段。
(1)Prefill阶段（Prompt阶段）一次性计算输入序列的K/V并写入缓存 模型读取完整输入的prompt，计算出所有token的Key/Value向量并写入缓存。 公式表示为：
![image-20251229205745845](https://l1yee.oss-cn-beijing.aliyuncs.com/image-20251229205745845.png)
此时缓存中的K/V向量构成了后续生成阶段的基础。
(2)Decode阶段（生成阶段）仅对新token计算Q/K/V，并复用历史K/V完成注意力计算 当模型生成新token时，仅需计算该token对应的Q、K、V向量。
![image-20251229205757073](https://l1yee.oss-cn-beijing.aliyuncs.com/image-20251229205757073.png)
然后与缓存中已有的K/V拼接，直接完成注意力计算。这样便避免了重复计算前面N−1个token的注意力结果。
### 2.2 past\\_key\\_values
在Hugging Face Transformers框架中，KV-Cache在接口层面通过 `past\_key\_values` 对象实现。该对象并非一个抽象的控制开关，而是模型前向推理过程中实际生成、并可跨生成步骤复用的中间状态。它以分层的结构保存已处理历史Token的Key和Value张量，从而支撑自回归生成的增量计算。
从结构上看，`past\_key\_values`通常是一个长度为模型层数的列表或元组，其中每一层对应一对 `(K, V)`张量。不同模型的具体维度布局可能存在差异，但其核心语义一致：存储历史序列的注意力键值表示，以便后续生成时直接复用。
在推理流程中，Prefill 阶段会对完整的提示词进行计算，并首次生成`past\_key\_values`。进入Decode阶段后，若将此缓存作为输入传递给模型，模型通常只需为新输入的Token计算其对应的Key和Value，并将其追加至现有缓存末尾，从而避免了历史部分的重复计算。这种基于`past\_key\_values`的复用是框架的原生机制，其带来的加速直接源于注意力计算的真实削减，因此更适合作为评估系统性能及分析相关安全影响的工程基准。相比之下，通过`sleep()`或人为插桩制造“快慢差异”的方法仅能模拟现象，难以反映实际推理系统的缓存行为。此外，Transformers框架的`generate()`接口通常通过参数`use\_cache=True`来启用此缓存机制。vLLM、SGLang、DeepSpeed-Inference在系统层面也普遍实现了类似机制，以降低生成延迟并提升吞吐量。
### 2.3 多租户场景下的前缀缓存与最长前缀匹配
在多请求并发且显存资源受限的推理服务中，为提升吞吐并降低重复的Prefill开销，系统常采用\*\*前缀缓存\*\*策略。其核心思想是当新请求的提示词（更准确地说是其Token序列）与某条已缓存的序列存在前缀重合时，系统可直接复用该前缀部分对应的KV-Cache，仅需对未命中的后续Token执行增量计算。
当缓存池中存在多个可能的候选前缀时，命中判定通常遵循最长前缀匹配（LPM）原则：在所有缓存条目中，系统会选择与新请求Token序列匹配长度最长的那一条作为复用对象，以最大化缓存利用率，减少重复计算。在工程实现上，这依赖于能够高效进行Token序列前缀匹配的数据结构或索引机制，例如前缀树（Trie）、基于前N个Token的分层哈希，或基于序列哈希值的多级索引。
根据匹配程度，命中效果可分为两类：一是完全命中，即请求的绝大部分或全部前缀已在缓存中，Prefill阶段的计算量显著下降；二是部分命中，即仅能复用较短的前缀，系统仍需对剩余后缀执行完整的Prefill计算。无论是“是否命中”还是“命中长度”，都会直接反映在可观测的系统性能指标上，例如Prefill时间、首Token延迟的分布等。
当前主流引擎（如vLLM的PagedAttention、LMCache）进一步通过分页管理和压缩技术缓解显存碎片，但前缀共享引入的侧信道与内存安全风险依然突出，这也是后续攻击面的根源。
0x03 KV-Cache的主要攻击面原理介绍
-----------------------
在理解KV-Cache的核心优化机制与共享原理后，我们可以看到其高效性背后隐藏的脆弱性。下面详解三大主要攻击面：时序侧信道攻击、操纵攻击与腐败攻击。
### 3.1 KV-Cache时序侧信道攻击
在共享KV-Cache的系统中，攻击者通过测量响应时间或请求处理顺序，推断缓存是否命中（hit），从而还原其他用户的Prompt（提示词）。
![image-20251028173225854](https://l1yee.oss-cn-beijing.aliyuncs.com/image-20251028173225854.png)
​
时序侧信道攻击完流程图
​
设定还原的语句是"Imagine you are an IT expert"，攻击者已经成功还原出"Imagine you are"，并尝试还原下一个token "an"。下面我们根据上图分步骤拆解一下攻击过程。
#### 步骤1:Generate candidates
攻击者在本地用小模型、模板或启发式方法生成可能的下一个token候选集合，例如：
- `Imagine you are an`
- `Imagine you are a`
- `Imagine you are the`
- `…`
把未知的victim prompt逐步转化为一系列候选前缀/后缀，便于后续probe。优点是减少搜索空间。
- - - - - -
#### 步骤2:Generate dummy
- Candidate请求：每个请求包含一个候选后缀（比如`Imagine you are an`）。目标是看哪一个candidate与victim的缓存前缀最长匹配而“命中”缓存。
- Dummy请求：随机或不相关的prompt（用来制造队列/填充调度槽位），以便控制调度顺序或避免直接暴露自己的probe请求导致缓存污染判断混淆。
#### 步骤3:Send three request batches in turn
攻击者按这个顺序把三组请求发到服务器（可能是同一API key，也可能跨多个短时间窗口发出）。核心就是在调度队列里把candidate放在中间，观察它是否因为缓存命中而更快返回。
#### 步骤4:Observe the returning order
攻击者记录三批请求的返回顺序和时间（TTFT/latency）。若candidate的响应比其前后的dummy显著更快或优先到达，就可推断该candidate是命中了缓存（即victim的prompt与该candidate共享较长前缀）。
### 3.2 History Swapping 攻击
![image-20251230101845847](https://l1yee.oss-cn-beijing.aliyuncs.com/image-20251230101845847.png)
​
History Swapping操纵攻击原理图
​
攻击者通过结构化替换或注入KV-Cache内容，来“劫持”模型的生成轨迹，强制引导输出转向攻击者指定的主题或行为。这种攻击利用KV-Cache编码了不仅仅是上下文，还包括话题规划（topic trajectory）和结构化推理（structural planning）的特性。
设定攻击场景：受害者Prompt为“Give a precise technical explanation of espresso extraction variables”（讨论咖啡萃取），攻击者希望劫持输出到恒星生命周期主题。用户可见Prompt不变。
#### 步骤1: 预生成目标主题KV-Cache
攻击者离线使用相同模型，基于目标主题Prompt生成一段完整KV-Cache块（topic\\_cache）。
#### 步骤2: 启动正常生成并等待替换点
从受害者Prompt开始自回归生成，监控已生成token数，直到达到预设swap\\_token（例如序列的20%-60%处）。
#### 步骤3: 执行块级覆盖替换
计算替换段长度（swap\\_percent，如25%-75%最近timestep），在全层（或指定早/晚层）用topic\\_cache对应部分直接覆盖当前缓存。
#### 步骤4: 继续生成并观察劫持
模型基于篡改缓存继续输出。常见效果：立即/延迟主题偏移、原主题与攻击主题交替、或生成重复崩溃。
### 3.3 KV-Cache 腐败攻击
![image-20251230101806716](https://l1yee.oss-cn-beijing.aliyuncs.com/image-20251230101806716.png)
​
KV-Cache腐败攻击原理图
​
攻击者通过向KV-Cache注入扰动（perturbation），破坏注意力机制的完整性，导致输出偏差、性能下降或幻觉增加。这种攻击视KV-Cache为“内存腐败”类似漏洞，扰动键向量（Key vectors）即可放大影响。
设定攻击场景：在正常生成或RAG任务中，攻击者向KV-Cache的Key向量注入扰动，导致注意力偏差、性能下降或幻觉增加。
#### 步骤1: 选择目标层与时机
确定最脆弱层（通常中层，如LLaMA-2第12层）和扰动应用频率（连续或间歇）。
#### 步骤2: 选择扰动变体
- MTI-Gaussian：添加高斯噪声（σ=0.1-5.0）
- MTI-Zeroing：概率置零Key条目
- MTI-Rotation：施加正交旋转（15°-90°）
- 可结合梯度优化以最大化目标影响
#### 步骤3: 注入扰动到Key向量
在生成过程中，按选定策略对Key向量应用扰动δ。
#### 步骤4: 观察输出效果
监控下一token分布偏移（KL散度上升）、下游任务性能下降15–30%、或RAG幻觉率增加5%-12%。中层扰动放大效果最显著。
0x04 代码实现
---------
测试为纯CPU环境下完成，基于Python3.8+的Hugging Face Transformers与PyTorch运行124M参数的gpt2模型。
### 4.1 KV-Cache时序侧信道攻击
#### 实验1：基础缓存时序测量
验证KV-Cache复用是否产生物理上可观测的时间差异。
我们实现了一个多租户LLM服务的 `KVServer` 类，支持：
1. \*\*最长前缀匹配 (LPM)\*\*：实现类似vLLM的Prefix Caching
2. \*\*精确计时\*\*：仅测量Prefill阶段的KV 计算，排除tokenization开销
3. \*\*缓存管理\*\*：LRU淘汰策略
核心实现
```php
@dataclass
class \_CacheEnt:
"""KV-Cache 条目"""
prompt: str
input\_ids: torch.Tensor
past\_kv: Tuple
ts: float
class KVServer:
"""多租户KV-Cache服务器"""
def \_lpm(self, q\_ids: torch.Tensor):
"""Longest Prefix Match - 缓存必须是查询的前缀"""
best = None
best\_len = 0
for cached, ent in self.\_cache.items():
c\_ids = ent.input\_ids[0].tolist()
q = q\_ids[0].tolist()
# 计算共同前缀长度
mlen = 0
for i, (a, b) in enumerate(zip(c\_ids, q)):
if a == b:
mlen = i + 1
else:
break
# 缓存有效条件：缓存是查询的前缀（mlen == len(cached)）
if mlen > best\_len and mlen == len(c\_ids) and len(c\_ids) <= len(q):
best = ent
best\_len = mlen
return (best, best\_len) if best else None
def process(self, prompt: str, max\_new=1, uid="anon", write\_cache=True):
"""处理请求，返回详细的时序数据"""
input\_ids = self.tok.encode(prompt, return\_tensors="pt")
t0 = time.perf\_counter()
cache\_r = self.\_lpm(input\_ids)
with torch.no\_grad():
if cache\_r:
# 缓存命中路径：复用past\_key\_values
ent, matched = cache\_r
self.\_hits += 1
if input\_ids.shape[1] > matched:
# 部分匹配：计算增量部分
delta\_ids = input\_ids[:, matched:]
out = self.model(
delta\_ids,
past\_key\_values=ent.past\_kv,
use\_cache=True
)
past\_kv = out.past\_key\_values
else:
# 完全命中：直接复用
past\_kv = ent.past\_kv
prefill\_t = (time.perf\_counter() - t0) \* 1000
hit = True
else:
# 缓存未命中路径：完整前向传播
self.\_miss += 1
out = self.model(input\_ids, use\_cache=True)
past\_kv = out.past\_key\_values
prefill\_t = (time.perf\_counter() - t0) \* 1000
hit = False
# ....