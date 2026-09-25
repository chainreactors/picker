---
title: 【AI安全】LoRango把触发器拆成两份LoRA：单独审计为何看不见后门
url: https://mp.weixin.qq.com/s/szMEifJEuPOrvk8aRwbyHg
source: Doonsec's feed
date: 2026-09-24
fetch_date: 2026-09-25T06:51:36.884939
---

# 【AI安全】LoRango把触发器拆成两份LoRA：单独审计为何看不见后门

# 【AI安全】LoRango把触发器拆成两份LoRA：单独审计为何看不见后门

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 一、97.9%与98.7%发生在配对加载时

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

###### 免费课程持续更新

https://space.bilibili.com/452583051/lists/7870008?type=season

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

复旦大学等机构的研究者9月22日发布论文 LoRango（arXiv:2609.25884v1），讨论文本生成图像模型里的一种组合条件攻击。研究者把隐蔽行为拆入两份普通静态 LoRA：Signature 负责在中间表示写入配对代码，Payload 负责识别该代码并释放预设图像行为。论文报告，指定配对共同加载时，在 SD v1.5 和 SDXL 上的攻击成功率分别为 97.9% 和 98.7%；单独加载植入适配器时仅为 2.8%—4.6%。🧬

Oxo Security 的判断是：**当生产系统允许用户自由叠加视觉适配器，安全审计的对象就从单个文件扩展成“适配器组合”。** 这里不需要在提示词里放特殊口令，也不需要改动基础模型或推理程序。若平台只对每个 LoRA 分别做离线抽检，可能看不到两份文件相遇后才出现的行为。这个结论针对论文构造的扩散模型实验，不能直接推成所有 LoRA 市集都有活跃后门。🔍

LoRA 原本是低秩权重更新：用户为角色、画风或材质加载小型适配器，比重新训练整个模型轻便。多个 LoRA 可以同时加载，也因此出现一个新问题：单独运行 A 正常、单独运行 B 正常，是否足以证明 A+B 正常？LoRango 给出的反例是“配对身份”本身构成触发条件。攻击者可以训练并发布两个看似各有正常用途的适配器，等待它们在同一生成任务中共载。🧩

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHRBTW1qzHR3ank2tger7cc5FiaiboFFkxvPic0CxxicmmEic1khibWIokWgMpx7Aib3Up94hYfVU4YBcoCah2iaVjUwtX9pa8icVW1DzRuk/640?wx_fmt=png&from=appmsg)

| 加载状态 | 论文中的目标行为 | 主要检查价值 |
| --- | --- | --- |
| 仅 Signature 或仅 Payload | 报告 ASR 约 2.8%—4.6% | 检验单件抽检为何可能漏报 |
| 指定 Signature + Payload | SD v1.5 为 97.9%，SDXL 为 98.7% | 检验配对触发是否成立 |
| 不匹配的两份适配器 | 四组配对实验聚合非匹配激活率 0.50% | 检验行为是否依赖正确搭档 |
| 加入四份无关 LoRA | 报告 ASR 仍为 87.0%—99.0% | 检验多适配器部署的干扰影响 |

这些数字有共同前提：论文选用的模型、提示词、目标行为、训练方案和评价器。论文的 ASR 是由 Gemini 2.5 Pro 对生成图像是否达到目标行为进行判定，并非真实平台事故率。配对实验的结果很强，但应同时看单件保真度、非匹配激活与跨模型实验，不能拿 98.7% 当作任意组合的通用风险概率。📏

# 二、触发条件藏在模型计算里，不藏在提示词里

论文的威胁模型设定为可训练两份适配器的白盒攻击者。两份文件仍以标准 LoRA 形式交给常规加载器，并固定加载比例；攻击者不依赖额外运行时钩子、动态路由、读取另一份 LoRA 元数据的代码或秘密提示词。Signature 在选定中间层施加低幅度的配对代码，Payload 的“读取器”对匹配代码产生响应。**触发器不是输入文本中的词，而是两份权重在同一次前向计算中的相互作用。** ⚙️

这套机制有一层重要的伪装：Payload 设计了方向相反的 signal 与 reference 分支。没有匹配代码、或加载了不匹配搭档时，两条分支的效果近似抵消；Signature 的代码与 Payload 的读取方向对齐时，模型原生 GEGLU 非线性改变门控，抵消被打破，预设响应沿去噪过程影响最终图像。📐

对于读者，可以把它理解为两个独立文件都没有“打开开关”的明显表现，只有正确的一对进入同一计算路径，门控差异才被放大。但这只是解释模型机制的类比，并不意味着 LoRA 文件互相通信或扫描对方文件名。论文明确说适配器不读取伙伴的元数据和权重，识别来自模型内部表示的交互。🧠

公开审计至少要覆盖三个问题。第一，平台是否允许来自不同来源的适配器共载，及谁能控制这份组合清单。第二，是否只运行单件基准，而没有对高频或高风险组合做相同提示词与随机种子的对照。第三，生成结果的异常判断是否同时比较目标偏移、正常功能保留与非匹配组合；否则可能把普通视觉变化误判成后门，或把精心隐藏的组合行为当作风格效果。🛠️

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHSXFeZRrkgy94OqKiaJtkQibqibsY5cPoM7sXGq0d5ParicWtr1t0eEqkmibOibrHhicVK3HBUPwvZQXYToBt9ecwMDuLNY4t7sribDQAc/640?wx_fmt=png&from=appmsg)

一个实用的最小检查是固定基础模型、提示词和随机种子，分别生成无适配器、仅 A、仅 B、A+B 四组输出；若平台有多个版本，再对经常共同加载的组合做版本回归。异常不应只靠一张示例图判定，需结合人工或独立评价、重复采样和目标描述。**单件安全报告不能自动作为组合安全报告的替代品。** 🔐

# 三、论文怎样证明“只有正确搭档才响应”

**🎯【论文怎样证明“只有正确搭档才响应”】**

这一节真正关键的不是「论文怎样证明“只有正确搭档才响应”」这个概念本身，而是它背后的判断路径、执行边界和可复用方法。

它怎样落到真实安全团队的工作流里？哪些细节会直接影响 AI 代理的可靠性？

加入 `Oxo AI Security 知识星球`，可查看本节完整内容，系统掌握「论文怎样证明“只有正确搭档才响应”」的完整拆解与实战用法。

📚 **AI 文献解读：最前沿的 LLM 安全论文深度剖析。**

🐛 **AI 漏洞情报：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。**

🛡 **AI 安全体系：从红队攻击到蓝队防御的全方位知识图谱。**

🛠 **AI 攻防工具：红队专属的自动化测试与扫描工具箱。**

🚀立即加入 **Oxo AI Security 知识星球**，掌握 AI 安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHRy2nZH6S7gzEkSbJnlJu1zIywWiaNFSlmNhnylG29ETiatRN7MkD64QPQGpxIiaR9xbVOr7Zhn1TdziaC6KjJnBDHPibFfkJ5OAMGs/0?wx_fmt=png)

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