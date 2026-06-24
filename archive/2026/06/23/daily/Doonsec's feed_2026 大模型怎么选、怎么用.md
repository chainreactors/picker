---
title: 2026 大模型怎么选、怎么用
url: https://mp.weixin.qq.com/s/SU21bJh7dBfki8p7belb0g
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:47.366584
---

# 2026 大模型怎么选、怎么用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eGLK5ewXfq5gBDwshVYZGCY83JiaXhKepqKSW2BkmsgOOSFiaXT32fT8SnQ8HQwNK5sx7EL9QibL5AcCNbicDUKr5OydzgZQKux60vzANe8xL3U/0?wx_fmt=jpeg)

# 2026 大模型怎么选、怎么用

原创

CKCsec安全团队
CKCsec安全团队

CKCsec安全研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 这篇文章帮你了解到什么

**如果你是个人用户：**

```
1. AI 大模型现在发展到什么程度了？谁是第一梯队？
2. 我日常该用哪个？写作、编程、查资料分别选谁？
3. 怎么花最少的钱、最省心地跟上这波潮流？
```

**如果你是企业用户：**

```
1. 到底该买商用 API，还是自己部署一个开源大模型？
2. 要自部署，开源旗舰里挑哪个？硬件和许可有什么坑？
3. 要买，选谁、花多少钱、合规边界在哪？
```

时间口径：**2026 年 6 月 23 日**。模型和价格变化极快，数值只代表写作时点，最终以官网实时页面为准。

---

## 开始前：5 分钟看懂这些词

后面会反复用到一批名词。不用全记，按下面四组理解一遍就够看懂全文：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7nUuzT5Tibl0x0saQvRwsCJ3Z4ThH3fjDWib18Uf0vs59oxiaCD5HByYju8cibS5jzRlCfPYvntZpU07ftDakfTxm2HxZg1lyLSIoOac9SiczcIFg/640?wx_fmt=svg&from=appmsg)

| 名词 | 一句话含义 | 你该关心的点 |
| --- | --- | --- |
| Token | 模型计费/计量的最小单位，约≈半个汉字 | 越长的输入输出越贵 |
| 上下文窗口 | 一次能读多少内容（Context Window） | 越长越贵，不一定越准 |
| LLM | 大语言模型，处理文字、代码、推理 | 当下的“主力发动机” |
| VLM / 多模态 | 还能看图、听音、读视频 | 跨图文音视频任务要看它 |
| 推理模型 | 会“先想再答”，更适合难题 | 复杂推理/数学/代码更稳 |
| Embedding | 把文字变成可检索的语义向量 | RAG 检索的底层 |
| RAG | 先查你的知识库，再回答 | 让模型用上你的私有资料 |
| 微调 Fine-tuning | 用自己数据再训练模型习惯 | 改“说话习惯”，不替代知识更新 |
| Agent | 自己拆任务、调工具、连续执行 | 能力强但要控权限 |
| Workflow | 按固定步骤走的 AI 流程 | 灵活性低但可控 |
| Tool Calling | 模型请求外部工具执行 | 要做参数校验和审计 |
| MCP | 模型连接工具/数据的统一接口协议 | 接外部能力的“通用插座” |

最容易混的三个，一句话记住：

```
RAG      = 先查资料再答
Workflow = 按固定流程走
Agent    = 自己计划并调工具
```

生产系统里，可控性优先级通常是：`RAG > Workflow > 受控 Agent > 全自主 Agent`。

---

# 第一部分 · 现状：大模型发展到哪了（个人重点）

## 一张图看清 2026 的格局

![2026 大模型格局](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5uwuhfSM9LkFZob8dBVU1PRRuWXEuhyCywEDLribrl5CaYV9aoCmxxibjnDysIyWiakOumxVFowSy0aBhNHMbgdSXNaYzIRLlruN6wndUBib4J2g/640?wx_fmt=svg&from=appmsg)

2026 大模型格局

2026 年的格局可以概括成两条并行路线：**闭源旗舰**与**开源旗舰**。两者在多项公开基准上的差距持续收窄，但定位不同，没有“一个最好”。

* **第一梯队 · 闭源旗舰**：Claude Opus 4.8、GPT-5.5、Gemini 3 Pro。综合基准靠前、开箱即用；只能按 token 付费、不能自部署。
* **开源旗舰**：GLM-5.2、DeepSeek V4、Kimi K2.6、Qwen3.5、Mistral Large 3、Llama 4。权重公开、可下载自托管；在编码、长程 Agent 等公开榜单上，头部开源已与部分闭源旗舰处于同一区间（具体名次随榜单和评测设置而变，详见第三部分）。
* **性价比 · 中小尺寸**：Gemini 3.5 Flash、Qwen3.6-35B、DeepSeek Flash、Mistral Small 4。更便宜、更快，部分尺寸可单卡部署。
* **多模态 · 专用**：图像、语音、视频、实时交互各有侧重，按能力挑而非按品牌挑。

能力上，2026 的主流旗舰普遍具备：**百万级上下文**、**长程 Agent**、**改真实仓库级的编码**、**原生多模态**——这些已是旗舰“标配”，而非某一家的独家卖点。

## 个人怎么选、怎么跟上

不用追榜，按「你要干嘛」对照「该看什么维度」，候选不分先后、自己试用后选顺手的：

| 你要做的事 | 该看什么维度 | 主要候选（不分先后） |
| --- | --- | --- |
| 写作、改稿、日常问答 | 表达自然度、稳定性 | Claude、GPT、Gemini、Kimi、Qwen、GLM |
| 写代码 | 真实仓库修复、IDE 集成 | Claude、GPT、Gemini、GLM、DeepSeek、Qwen |
| 查资料、做研究 | 是否给引用来源 | Perplexity、联网版 Gemini/GPT、自建搜索+RAG |
| 读长文档/整本书 | 上下文窗口、引用准确率 | Gemini、Claude、Kimi、GLM、Qwen |
| 想省钱/本地跑 | 价格、是否可本地化 | 各家 Flash/Lite、DeepSeek、Qwen、GLM、Mistral |

**跟上潮流的最低成本姿势**（不绑定具体品牌）：

```
1. 任选一个第一梯队产品订阅，先用熟，建立自己的判断基线
2. 关注一个中立综合榜（如 Artificial Analysis）看大盘，不必天天换模型
3. 开源阵营（GLM / Qwen / DeepSeek / Llama / Mistral 等）同样值得跟进
4. 别被“最新最强”绑架——顺手 + 稳定，往往比榜单高半分更重要
```

---

# 第二部分 · 企业核心决策：买，还是自部署？

这是企业用 AI 的第一道、也是最贵的一道选择题。先别问“哪个模型先进”，先走这张决策图：

![买 vs 自部署决策图](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4SEvdmgBKjjVlrzrFzcwONWO0X5Ufl5r7zNWNfzGEunoPvNx9IwYdQtEydyeSfGZZozk6qaaZ2ib6fHVBZ7JGH6Bicicic7ia98LgRbHaiadAWFYvg/640?wx_fmt=svg&from=appmsg)

买 vs 自部署决策图

决策顺序固定是三问：

1. **数据能不能离开自有环境？** 受 HIPAA / GDPR / 等保 / 内网隔离约束、数据绝对不能外发 → 直接走**自部署开源**，这一条能一票否决其它所有考量。
2. **用量是否稳定且很大？** 日均超过约 **1000 万 tokens** 且负载平稳，自建才摊得平固定成本；量小或忽高忽低 → **买 API**。
3. **有没有 GPU 运维团队？** 自建需要至少 1.5–2 个全职工程师扛部署、调优、监控；没有这个团队 → 买 API 或托管。

### 成本到底在哪交叉

![自建 vs API 成本盈亏平衡](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6tIvjdaAhIE27ZoCmmwDklcSSYF9cE48YS6qOAd1MuwD1mJJ6gsfJhjVWwm4j6bhaGlGIGWENJLcn5GPrd6Kr3eia9OtEtWC08QDlL5jVnibiaA/640?wx_fmt=svg&from=appmsg)

自建 vs API 成本盈亏平衡

这张图是企业最容易算错的地方：

* **量小或突发，API 几乎总是更省。** API 在你空闲时收费为零；自建的 GPU 不管跑不跑满，电费和折旧照付。
* **盈亏平衡大致在日均 10M tokens 量级**（不同测算从月 500 万到上百亿 token 不等，差距来自利用率假设）。
* **致命陷阱——真实成本不是显卡租金。** 业内共识是：裸 GPU 只占真实总成本的 30–40%，要乘 **2.5–5 倍**才接近 TCO，因为还有运维团队（1.5–2 FTE，年薪 27–55 万美元起）、电力冷却（实际是标称功率的 1.5–2 倍）、模型更新。
* **GPU 闲置 = 烧钱。** 一张利用率只有 10% 的卡，单 token 成本会膨胀 10 倍，能吃掉全部理论节省。

> ❝
>
> 参考量级：一张 H100 全天候租用约 月，二手买入约1.5–2 万/张。

### 结论：多数成熟团队走「混合」

不要把它当成二选一。最务实的做法是：

```
可预测的批量任务  → 自建开源，摊薄成本、数据自主
高价值/突发/探索  → 走商用 API，零运维、按量付费
```

---

# 第三部分 · 要自部署，开源旗舰怎么挑

![开源模型对比](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4OVEa1oxrUkJte8qYDxymhibsiaOTNzqobr6COGNALBiaydXI816ElKhJF6nJe5SrdVibjyXEibnxZ7TqPc0zzezmWQ4umms1rhWoCMkDaIUAAMpw/640?wx_fmt=svg&from=appmsg)

开源模型对比

选开源模型，建议按**许可 → 尺寸（硬件）→ 能力**逐项核对。下表只列可核实的客观参数，“公开侧重”一栏取各家官方定位/榜单方向，不代表高低排名：

| 模型 | 参数(总/激活) | 许可 | 上下文 | 公开侧重 | 部署门槛 |
| --- | --- | --- | --- | --- | --- |
| GLM-5.2 | 754B / 40B | MIT | 1M | 代码 Agent、长程任务 | 数据中心级 |
| DeepSeek V4 | 1.6T / 49B | MIT | 1M | 推理、代码（含轻量 Flash 版） | 旗舰数据中心 |
| Kimi K2.6 | ~1.1T | Modified MIT | 长 | 代码、工具调用、长程 Agent | 数据中心级 |
| Qwen3.5 | 235B / 22B | Apache 2.0 | 256K+ | 中文/多语、通用、生态广 | 多卡 |
| Qwen3.6-35B | 35B / 3B | Apache 2.0 | 262K→1M | 本地代码/私有助手 | 单卡可跑 |
| Mistral Large 3 | 675B / 41B | Apache 2.0 | 长 | RAG、倾向少幻觉 | 多卡数据中心 |
| Llama 4 Scout | MoE | Llama（限商用） | 10M | 超长上下文 | 注意 MAU/地区限制 |

> ❝
>
> 名次说明：编码/长程能力的具体排名随榜单（DeepSWE、SWE-bench Pro、Terminal-Bench 等）和评测设置而变，跨榜不可直接比较。上表不做高低排序，请结合自己的评测集判断。

落地三句话：

```
① 许可优选 Apache 2.0 / MIT；Llama 商用前务必查 700M MAU 上限与 EU 限制
② 别一上来就上万亿参数旗舰——先选塞得进你显卡的尺寸
③ 显存看“总参数”不是激活参数：8G→7-8B；24G→30B 级；40G+→70B 级；
   万亿旗舰满上下文≈1TB 显存，是数据中心活儿
```

> ❝
>
> 做私有化验证时，优先选能在现有显卡上跑起来的中小尺寸（如 30B 级 MoE 单卡即可），先把业务流程跑通，再决定是否上更大的旗舰或混合调用 API——这是流程建议，不是对某一款模型的背书。

---

# 第四部分 · 要买，商用模型怎么选、花多少钱

![主流模型价格速查](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6D1ibICDeJE9SiavkosB5orjpYnrgq1jv2szpVRTgnazxYdD2vXjUK1paZHMJrZHialicaicGiafEgYxFiawQsBicLFU1pFhWVnpfNytVJyuXbMFFVjA/640?wx_fmt=svg&from=appmsg)

主流模型价格速查

商用 API 的真实成本不是只看“输入单价”，关键事实（每 1M tokens，写作时点）：

| 模型 | 输入 | 输出 | 关键提示 |
| --- | --- | --- | --- |
| Claude Opus 4.8 | $5 | $25 | 1M 上下文默认开、输出上限 128K；缓存命中约 9 折、Batch 半价 |
| Claude Sonnet 4.6 | $3 | $15 | 日常主力，质量/成本平衡 |
| GPT-5.5 | $5 | $30 | **超 272K 输入触发翻倍** ；Batch/Flex 半价 |
| Gemini 3 Pro | $2 | $12 | **超 200K 上下文阶梯涨价** |
| Gemini 3.5 Flash | $1.5 | $9 | 低成本档，缓存输入 $0.15 |
| GLM-5.2 | $1.4 | $4.4 | 也可买 API；缓存输入 $0.26 |
| DeepSeek / Qwen / Kimi | 低区间 | 低区间 | 中文生态，价格普遍更低；以各自官网为准 |

省钱优先级（顺序别搞反）：

```
1. 先砍掉无效上下文/RAG 片段（最有效）
2. 开上下文缓存（命中可省约 90%）
3. 简单问题走小模型，复杂问题才走旗舰
4. 离线批量走 Batch（通常半价）
5. 限制输出长度
6. 最后才考虑换更便宜的模型
```

> ❝
>
> 算一笔账：企业知识库问答，单次输入 ~3600、输出 ~800 tokens，每天 1 万次 = 日 3600 万输入 + 800 万输出 token。这种稳定大量的场景，正是该认真比「缓存价 + Batch 折扣」、甚至评估自部署的临界点。

各家官方价格入口：Claude · OpenAI · Gemini · Z.AI/GLM

---

# 第五部分 · 用到哪个地方：场景 → 模型映射

![不同任务选不同模型](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6QKibzVnicjbDU5qjpmfo0duXtoKp42CURD4ZJYmpSavthl6gBlicVkUvNUBfW5XWHJdl5tfMk4hSfeRFnvpkqgtqTpptWphkgibBYlEpTNQaZTg/640?wx_fmt=svg&from=appmsg)

不同任务选不同模型

一张表把“什么好、用在哪”说清：

候选均不分先后，按你自己的评测集和约束二次筛选：

| 业务场景 | 买（商用 API） | 自部署（开源） |
| --- | --- | --- |
| 客服/通用问答 | Claude、GPT、Gemini | Qwen、GLM、Llama、Mistral |
| 代码助手/Agent | Claude、GPT、Gemini、GLM API | GLM、DeepSeek、Qwen、Kimi |
| 企业知识库 RAG | Claude、GPT、Gemini | Mistral、Qwen、GLM、Llama |
| 长文档处理 | Gemini、Claude、Kimi | Llama（超长）、GLM、Qwen |
| 低成本批量 | 各家 Flash/Lite、DeepSeek API | Qwen 中小、Mistral Small、各家小模型 |
| 数据不能出域 | —（不适用） | 任一可自托管开源：Qwen / GLM / DeepSeek / Llama / Mistral |
| 多模态 | GPT、Gemini | Qwen-VL、GLM-V |

---

# 第六部分 · 安全与合规边界（企业必看）

![安全限制矩阵](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM63Skv8ia1NDsCQibEnDt0xc2oxInicf0qUVG7wJwg8l81G1RHsfaulB8ibibOPu67ZTcF7vs7YN9VAXbU2fxib9t3r1x1aCeF69tIZfnDMvpCqLV7A/640?wx_fmt=svg&from=appmsg)

安全限制矩阵

“买”和“自部署”最大的区别之一，是**责任边界**：

* **买商用 API**：内容安全、滥用防护由厂商兜底，但你要接受它的内容政策和拒答边界；敏感/研究类场景需要设计授权与审计流程。
* **自部署开源**：限制更可控，但**安全护栏、审计、滥用防护全部要自己做**——数据自主的另一面是责任自担。

无论买还是自建，企业级 AI 平台至少要有：

```
模型路由 · API Key 管理 · 成本统计 · Prompt 模板 · RAG 知识库
权限隔离 · 工具调用审计 · 数据脱敏 · 评测集 · 安全策略 · 回滚机制
```

---

## 一页纸总结

**个人：** 任选一个第一梯队产品用熟 → 写作看表达、代码看 IDE、研究看引用 → 同时关注开源阵营进展，但别被“最新最强”绑架。

**企业：**

```
数据不能出域 / 强合规   → 自部署开源（先用能单卡部署的中小尺寸验证）
量小 / 突发 / 没运维团队 → 买商用 API（空闲不花钱）
稳定大量 + 有团队        → 混合：批量自建，高价值走 API
```

选型口诀：

```
先问数据与合规，再问用量与成本，最后问运维能力；
能力相近时...