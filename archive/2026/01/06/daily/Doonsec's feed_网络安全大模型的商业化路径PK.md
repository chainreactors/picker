---
title: 网络安全大模型的商业化路径PK
url: https://mp.weixin.qq.com/s/2omUNjcm5OWglTutNTMA_w
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:27:01.300086
---

# 网络安全大模型的商业化路径PK

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/d4ae4qYgqsjsAUgQY1S9r4D7QxiafNJEXRGrRdYzL6YDicbFWeHoXcfsk486JdWphmCwLjF7DzypnDclAvcwUzcA/0?wx_fmt=jpeg)

# 网络安全大模型的商业化路径PK

原创

DIMU

AI简化安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsjsAUgQY1S9r4D7QxiafNJEXcKvkRPI8DGicF6f1rZwkFWV4STM2RN3HbTwbrJuIqLjX1N3LkLlV5pA/640?wx_fmt=png&from=appmsg)

图：全过程微调VS 提示词工程 AI生成

2025年以来，大语言模型（LLM）在网络安全领域的应用已从概念验证转向实际部署。威胁情报分析、告警研判、漏洞响应和事件调查等场景，对AI的智能化需求日益突出。基于开源模型如阿里云Qwen2.5 32B或类似基础模型，许多企业和创业团队尝试构建垂直领域安全大模型。然而，商业化进程揭示了一个关键现实：技术深度并不直接等同于市场成功。客户（甲方）往往已投资建设成熟的安全运营平台（SIEM系统，如Splunk或国内厂商产品），不愿承担全面替换的成本和风险。这导致厂商（乙方）在产品设计时面临两难：追求模型的极致性能，还是优先兼容性与落地效率？

当前，主流开发路径分为两种：**全过程微调**（包括二次预训练、监督指令微调和强化学习对齐）和**提示词工程**（prompt engineering，常结合检索增强生成RAG和多代理框架）。全过程微调旨在实现模型的深度领域适应，而提示词工程则强调高效、灵活的应用集成。二者在实战性能上的差距正逐步缩小，但开发成本、落地难度、隐私合规以及商业变现潜力存在显著差异。尤其在国内市场，大部分行业客户（金融、能源、政府等）偏好本地化部署模式，数据不出境、模型本地运行成为刚性要求，这进一步影响路径选择。本文将系统分析两种路径的特性、挑战与实际案例，并探讨可持续的商业化策略。

![](https://mmbiz.qpic.cn/mmbiz_jpg/d4ae4qYgqsjsAUgQY1S9r4D7QxiafNJEXGc4tzKc0OJicwEnVickwfvkuhshyfvUTd6Z0upOonpuhLQanZwRdlI5A/640?wx_fmt=other&from=appmsg)

图：持续微调框架https://aws.amazon.com/cn/blogs/machine-learning/llm-continuous-self-instruct-fine-tuning-framework-powered-by-a-compound-ai-system-on-amazon-sagemaker/

#### 一、两种开发路径的详细过程

**全过程微调路径**从通用基础模型入手，通过多阶段适应实现垂直优化。该路径的核心在于参数更新，使模型“内化”网络安全专业知识。

* **二次预训练阶段**

  ：使用大量无标签领域数据（如CVE漏洞描述、MITRE ATT&CK框架文档、公开威胁情报报告）继续预训练。该阶段计算资源消耗最大，通常需全参数或近全参数更新，GPU小时数可达数千至上万（视模型规模而定）。目的是注入专业术语和模式识别能力。
* **监督指令微调（SFT）阶段**

  ：构建高质量指令-响应数据集，进行针对性优化。数据标注是关键环节，例如对告警日志进行专家标注：

  ```
  import jsonwith open('alerts.json', 'r', encoding='utf-8') as f:    raw_data = json.load(f)labeled_dataset = []for alert in raw_data:    instruction = f"请分析以下告警日志，并输出威胁分类、严重性和响应建议：描述：{alert['description']}，来源IP：{alert['source_ip']}，时间戳：{alert['timestamp']}"    response = "威胁类型：暴力破解尝试；严重性：中；关联ATT&CK技术：T1110（暴力破解）；建议：1. 立即封锁来源IP；2. 检查受影响账号密码强度；3. 启用多因素认证。"    labeled_dataset.append({"instruction": instruction, "response": response})# 保存为JSONL格式，用于Hugging Face Transformers训练with open('sft_data.jsonl', 'w', encoding='utf-8') as out:    for item in labeled_dataset:        out.write(json.dumps(item, ensure_ascii=False) + '\n')
  ```

---

该阶段常用LoRA（Low-Rank Adaptation）等参数高效技术，仅更新少量适配器参数，显著降低计算需求。

* **强化学习对齐（RLHF）阶段**

  ：收集人类反馈（如安全分析师对输出报告的评分），进一步优化模型的安全性、一致性和实用性，避免幻觉或有害建议。

该路径的优势在于性能深度：微调后模型在告警研判等任务中准确率更高、输出更专业，尤其能处理复杂威胁链推理。

**提示词工程路径**则避免参数修改，直接通过输入设计引导通用模型行为，常集成辅助技术提升效果。

* **提示设计阶段**

  ：构建结构化模板，融入思维链（Chain-of-Thought）、少样本示例和输出约束。例如中文提示模板：

```
你是资深网络安全分析师。请严格按照以下步骤分析告警日志：
1. 提取关键字段：事件描述、来源IP、目标资产、时间戳。
2. 分类威胁类型（如DDoS、数据泄露、内部威胁），并评估严重性（低/中/高/紧急）。
3. 关联知名框架（如MITRE ATT&CK技术或CVE漏洞）。
4. 提供可执行响应建议，至少3条。
5. 输出严格采用JSON格式：{"threat_type": "", "severity": "", "attack_reference": "", "analysis": "", "recommendations": []}

示例输入：{"description": "多次登录失败", "source_ip": "192.168.1.100", "timestamp": "2026-01-06 10:00:00"}
示例输出：{"threat_type": "暴力破解", "severity": "中", ...}

现在分析以下告警：{实际日志JSON}
```

* **集成增强阶段**

  ：结合RAG动态检索内部知识库（如脱敏威胁情报），或构建多代理系统（使用LangGraph框架）：规划代理拆解任务、检索代理查询数据库、执行代理生成报告。还可融合DeepSeek系列模型的长上下文能力处理海量日志，或集成Microsoft Security Copilot插件实现工具调用（如自动查询外部情报API）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/d4ae4qYgqsjsAUgQY1S9r4D7QxiafNJEXEC9fcQLMBabMdxYXjBZFLLOIxwb7q9UJP6kUgGcaDM8dbNlAzgWCbA/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/d4ae4qYgqsjsAUgQY1S9r4D7QxiafNJEXB2lUrqsJtial6nNS06giawsC4rxqXDyfP3ST3C8wHgoz7olsemqWUfVA/640?wx_fmt=other&from=appmsg)

图：多agent架构

https://kanerika.com/blogs/ai-agent-architecture/

#### 二、开发挑战与落地对比

网络安全垂直模型开发面临多重结构性挑战，全过程微调路径尤为突出。

首先，**数据挑战**：安全数据高度敏感，涉及企业核心资产和隐私信息。高质量标注需安全专家参与，成本高昂且易引入主观偏差。国内合规要求（如《数据安全法》《个人信息保护法》）进一步限制数据流动。

其次，**计算资源挑战**：二次预训练阶段资源消耗最大，32B模型完整迭代需大量高端GPU。即使采用LoRA，整体成本仍达数万至数十万美元。

第三，**平台绑定与个性化矛盾**：全过程微调理论上可深度捕捉企业内部历史事件链（如特定行业的攻击模式、重复假阳性规则），提升研判精度。然而，实际训练多在厂商侧完成，使用公开或聚合数据。部署到甲方后，模型仅进行推理，无法直接利用客户独有数据进一步适应。这导致“个性化优势”难以兑现：模型虽专业，但对甲方独特环境（如自定义日志格式、内部威胁景观）泛化不足。

甲方不接受的原因在于：希望模型持续学习本地数据，实现动态优化。但厂商不愿直接使用客户数据训练，主要基于：

* **隐私与合规风险**

  ：客户日志含敏感信息，厂商获取即面临泄露责任。
* **知识产权保护**

  ：核心模型权重视为商业机密，不愿暴露。
* **规模化考量**

  ：个性化训练破坏SaaS模式，无法服务多客户。
* **运营复杂性**

  ：客户环境异构，远程训练难度大。

提示词工程路径挑战较少，主要为提示优化迭代，但通过RAG和代理框架可灵活弥补。

安全智能体架构示例：

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/d4ae4qYgqsjsAUgQY1S9r4D7QxiafNJEXuJ5t8fHLT6lZSXsC42y3iaa0HpOtia9kicnBM37tIoS5fPr8lPm2ibb7Sw/640?wx_fmt=other&from=appmsg)

图：https://www.researchgate.net/figure/AI-agent-platform-reference-architecture\_fig1\_386461286

路径对比表：

![](https://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsjsAUgQY1S9r4D7QxiafNJEXibwliaURJNRnXib148paryWS5hlwLq3Dymia2mlibRPg2QbsIibvCqJ9dwrQ/640?wx_fmt=png&from=appmsg)

#### 三、对甲方与乙方的路径建议

对甲方建议需分层：

* 对于**具备研发实力和资源**的大型企业（如国有银行、科技巨头），可探索全过程微调路径，利用内部独有数据构建高度定制模型。但需解决个性化矛盾，推荐本地LoRA微调或联邦学习。
* 对于绝大多数甲方（依赖采购产品），优先提示词工程路径：快速集成现有SIEM，提升告警研判效率。国内行业客户多要求本地化部署，此路径优势明显——模型和RAG知识库均可本地运行，数据不出境。

解决个性化矛盾的推荐方案：

* **RAG动态适应**

  ：客户本地构建脱敏知识库，实时检索内部事件链。
* **本地参数高效微调**

  ：厂商提供基模型+LoRA工具链，客户自主训练适配器。
* **联邦学习框架**

  ：数据不出本地，仅聚合梯度更新。

**对乙方（开发厂商）**：**转向“基模型+适配工具”模式**，提供标准化代理框架、RAG组件和本地微调支持。国内零一万物等企业已调整战略，聚焦应用生态而非巨型模型研发。

#### 四、商业化路径：应用层优先的现实选择

当前两种路径产出的安全智能体，**在实际SOC环境中的性能差距并未形成代际水平**。通用模型持续迭代，加上RAG、多代理和工具调用技术，使提示词工程路径足以应对多数场景。全过程微调虽有理论优势，但高成本、隐私风险和个性化实现难度，使其投资回报不确定。

国际案例如Manus（代理+提示工程实现高估值收购）和国内应用层转型实践表明：网络安全大模型的商业价值，更多体现在无缝增强现有基础设施、降低客户部署门槛的应用层面。尤其在国内本地化部署为主的市场，提示词工程路径以其灵活性和合规友好性，更具规模化变现潜力。**未来（3-5年内），成功厂商将是那些提供高效工具、帮助客户“用好现有系统”的伙伴，而非单纯追求模型参数极致的玩家**。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsiaxrJrtBWmqoVLfOmHIGZtJG9aYmICG4neEFJV1Ylb0sSIkLF7bKF4GN1Vicibuo3DzDHWibVsBtEvwg/0?wx_fmt=png)

AI简化安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsiaxrJrtBWmqoVLfOmHIGZtJG9aYmICG4neEFJV1Ylb0sSIkLF7bKF4GN1Vicibuo3DzDHWibVsBtEvwg/0?wx_fmt=png)

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