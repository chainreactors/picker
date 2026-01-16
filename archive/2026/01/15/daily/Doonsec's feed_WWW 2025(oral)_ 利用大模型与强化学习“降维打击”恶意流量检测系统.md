---
title: WWW 2025(oral)| 利用大模型与强化学习“降维打击”恶意流量检测系统
url: https://mp.weixin.qq.com/s/_6YlJiUtigIK4bXHJh6Hqg
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:26:45.224340
---

# WWW 2025(oral)| 利用大模型与强化学习“降维打击”恶意流量检测系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AfRiaRUukfpUxzv8ngic8U5jh91ag0smwxo9Mb4Oaudsxwj0yG1VOWab0O2Gic84R4icUVBYF1ffVGtXicPTRQjicTqA/0?wx_fmt=jpeg)

# WWW 2025(oral)| 利用大模型与强化学习“降维打击”恶意流量检测系统

AIForSecurity
AIForSecurity

AI安全这点事

![]()

在小说阅读器中沉浸阅读

随着人工智能技术的深度介入，基于深度学习（DL）的恶意流量检测已成为网络安全防御的基石。然而，来自中国科学院信息工程研究所、北京理工大学等机构的研究团队揭示了一个严峻的事实：通过结合大语言模型（LLM）与强化学习（RL），攻击者可以生成极具欺骗性的对抗样本，轻松绕过现有的先进检测系统。

### 一、 作者与单位

* **作者**：Peishuai Sun, Xiaochun Yun, Shuhao Li, Tao Yin, Chengxiang Si, Jiang Xie。
* **单位**：中国科学院信息工程研究所、中国科学院大学网络空间安全学院、北京理工大学、中关村实验室、国家计算机网络应急技术处理协调中心（CNCERT/CC）。

---

### 二、 研究背景

现有的恶意流量检测模型（如基于卷积神经网络 CNN 或 Transformer）虽然在识别已知攻击方面表现卓越，但在面对针对性修改的**对抗样本**时却显得十分脆弱。 目前，针对流量的对抗攻击主要面临三个挑战：![](https://mmbiz.qpic.cn/mmbiz_png/AfRiaRUukfpUxzv8ngic8U5jh91ag0smwx6gVTDy66Jk51IEkr5jqDUE9XpAloo4Ewk7s8hEZz81ibHjyXntwbz5Q/640?wx_fmt=png&from=appmsg)

1. **通用性（Generality）**：攻击必须能映射回真实的流量空间，而不仅仅是特征空间的修改。
2. **可用性（Availability）**：生成的对抗流量必须符合协议规范（合规性），且攻击功能（如 Shellcode 执行）不能失效。
3. **载荷生成（Payload Generation）**：如何生成既有语义逻辑又能欺骗模型的复杂报文载荷。

**AdvTG** 框架通过引入大语言模型（LLM）的语义生成能力和强化学习（RL）的优化策略，完美解决了上述挑战。

---

###

### 三、 核心创新点

1. **任务特定提示工程（Task-Specific Prompts）**：设计了专门的 Prompt 结构，将流量字段划分为“功能性字段”（保持不变以确保攻击有效）和“非功能性字段”（由模型生成以实现逃逸）。
2. **领域自适应微调（LoRA-based Fine-tuning）**：通过 LoRA 技术让 LLM 学习复杂的网络协议模式，使其生成的流量具备极高的协议合规性。
3. **多目标对抗奖励机制**：利用强化学习（PPO算法）引导模型在保证合规性的同时，最大化检测器的误判率。
4. **跨模态逃逸能力**：生成的样本能够同时欺骗基于文本语义和基于图像特征（Payload-to-Image）的检测模型。

---

### 四、 详细方法

![](https://mmbiz.qpic.cn/mmbiz_png/AfRiaRUukfpUxzv8ngic8U5jh91ag0smwxGGHqsmWricdPtdQIbJicCFob4DHVqBwGHLPNGpAMnCt381vOX83JHnxQ/640?wx_fmt=png&from=appmsg)AdvTG 的实现核心在于三个阶段的协同：特征提取、模型微调与对抗进化。

#### 1. 流量特征提取（Feature Extraction）

论文首先定义了两种主流的流量特征处理方式：

* **图像特征提取**：将流量字节流转化为二维灰度图。
* **公式(1)**：
* *变量解释*： 变量解释：T 是原始字节流，bi 是归一化后的字节值，T′ 是向量化后的数据。
* **公式 (2)**：
* *变量解释*：变量解释： 代表生成的  灰度图中第  行第  列的像素值。
* **文本特征提取**：将流量视为文本序列进行分词和向量化。
* **公式 (3)**：
* *变量解释*： 为流量文本， 将其分割为词元（Token）， 是对应的嵌入向量（Embedding）。

#### 2. 基于 LoRA 的 LLM 微调

为了降低计算开销并保持模型的生成能力，AdvTG 引入了 **LoRA（Low-Rank Adaptation）** 技术。

* **公式 (4)**：
* *变量解释*： 是 LoRA 引入的低秩矩阵之一，其中  为秩（Rank），远小于模型原始维数。
* **公式 (5)**：
* *变量解释*： 是预训练模型的冻结权重， 和  是可训练的低秩矩阵， 是输入特征。通过这种方式，模型学会了如何补全非功能性字段。

#### 3. 强化学习对抗优化（RL Optimization）

AdvTG 使用 **PPO（Proximal Policy Optimization）** 算法来优化对抗性能。

* **奖励分数** ：基于检测器的负交叉熵。
* **公式 (6)**：
* *变量解释*： 是第  个检测模型判定的恶意概率， 是目标标签（逃逸时为 0）。
* **总奖励** ：引入 KL 散度惩罚项，确保生成流量不偏离协议语义。
* **公式 (7)**：
* *变量解释*： 为惩罚系数， 是正在学习的策略， 是微调后的基准模型。
* PPO 优化目标 ：
* *变量解释*： 是新旧策略的概率比， 是优势函数， 是裁剪半径。

####

#### 4. 算法：HTTP 流量合规性校验

为了确保生成的对抗样本在真实网络中可用，论文设计了 **Algorithm 1**。

**算法 1：HTTP 流量合规性验证流程**

1. **初始化**：设置错误列表 `errors = []`。
2. **分块**：使用 `\r\n\r\n` 将流量分为 `Header` 头部和 `Body` 载荷。
3. **请求行校验**：验证第一行是否符合格式 `<Method> <URI> <Version>`（如 `GET /index.html HTTP/1.1`）。
4. **头部字段遍历**：

* 检查每一行是否包含 `Key: Value` 结构。
* 检查关键字段（如 `Host`）是否存在。
* 检查非功能性字段中是否存在无法解析的字符。

5. **结果输出**：若无错误，判定为 `is_valid = True`。

---

### 五、 实验评估

#### 1. 实验指标

* **攻击成功率 (ASR)**：衡量对抗样本成功逃逸检测的比例。
* **公式 (8)**：
* *变量解释*： 是成功欺骗模型的样本数。

#### 2. 核心结论

![](https://mmbiz.qpic.cn/mmbiz_png/AfRiaRUukfpUxzv8ngic8U5jh91ag0smwxJzRRHsZJ3p8KdriaibuSdr9P9FmzwEvYDbwFU3XHIhfBXxCdsvoFXYkg/640?wx_fmt=png&from=appmsg)

* **卓越的攻击性能**：在 CICIDS2017、Malware 等多个数据集上，AdvTG 的 ASR 稳定超过 **40%**，远高于传统文本对抗方法（ASR < 10%）。
* **极高的合规性**：经过微调后，流量的合规通过率从 20% 左右提升到了 **80% 以上**。
* **强大的迁移性**：针对文本检测模型生成的对抗流量，在面对图像检测模型时依然具有很强的杀伤力，证明其捕获了模型在特征提取层面的共有盲区。![](https://mmbiz.qpic.cn/mmbiz_png/AfRiaRUukfpUxzv8ngic8U5jh91ag0smwxwczoVbyGzWHdzWIYNQWLgvficZXLSJd5yJiaWcsCI8ibWrvvgRNoNWhPw/640?wx_fmt=png&from=appmsg)

---

### 六、 总结

AdvTG 框架通过将 LLM 的领域知识与 RL 的博弈能力相结合，成功证明了现有的深度学习流量检测模型在面临“语义级”对抗攻击时的脆弱性。

**启示**：未来的防御系统不应仅仅依赖于简单的载荷特征提取，更需要引入**协议感知的对抗训练**，并考虑结合流量的功能逻辑进行深层次校验，方能抵御下一代智能化的网络攻击。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AfRiaRUukfpXJa7JnUibIpqeEuCfG7JLEwdzJFb0VEIZD9KV5Gnezh8BGhiaO2TRDMNbvChFXCXfBWnZpJczl0zibQ/0?wx_fmt=png)

AI安全这点事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AfRiaRUukfpXJa7JnUibIpqeEuCfG7JLEwdzJFb0VEIZD9KV5Gnezh8BGhiaO2TRDMNbvChFXCXfBWnZpJczl0zibQ/0?wx_fmt=png)

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