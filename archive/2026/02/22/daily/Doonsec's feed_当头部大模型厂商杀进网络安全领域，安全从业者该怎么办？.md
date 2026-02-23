---
title: 当头部大模型厂商杀进网络安全领域，安全从业者该怎么办？
url: https://mp.weixin.qq.com/s/U7A72ZNSQGKv2_qh91W35Q
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:17:57.734211
---

# 当头部大模型厂商杀进网络安全领域，安全从业者该怎么办？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibANIaIJODOnBJDXUic7DrNiayLlpKIh8QzwKKQaHh2ofhx8g3YbkXicjMtfOD6IqO4a6qpG3DcD12zibn9Fxavv5RHCveTyzFbbYR5ax0KdtWib8/0?wx_fmt=jpeg)

# 当头部大模型厂商杀进网络安全领域，安全从业者该怎么办？

原创

DIMU
DIMU

AI简化安全

![]()

在小说阅读器中沉浸阅读

# **零、Anthropic 安全产品推出，资本市场当天给出答案**

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOm2wTsQqQ2IG3kA02swCemlJBUcSLLG0zflLmkrfoq33D7xkM1dIwyA5icwGNXms9iafrI7n41vbuticGp1WfT5BF2rokycjibajxA/640?wx_fmt=png&from=appmsg)

没有发布会，没有大规模营销，只是一篇博客，写着：「**我们的模型在代码库里发现了超过500个隐藏数十年的安全漏洞。**」

资本市场当天就给出了答案——Okta 跌9.2%，CrowdStrike 跌6.8%，Zscaler 跌5.47%，全球网络安全ETF 跌近5%。

一家AI 公司，上线一款代码扫描工具，把传统安全厂商的市值打下去了。这不是偶然，是过去三年持续积累的一次集中爆发。而这场爆发，对在座每一位网络安全从业者都意味着什么，需要认真想清楚。

## **一、四大巨头都在网络安全里做了什么**

### **OpenAI + Microsoft：企业级AI安全的最大推手**

讲 OpenAI 在安全领域的布局，绕不开微软。

OpenAI 的核心战略路径不是自建安全产品，而是通过与微软的深度整合来实现渗透。而微软，正是用这种整合，打造出了目前企业市场最具影响力的AI 安全产品：**Microsoft Security Copilot**。

这款基于 GPT-4 架构的AI 安全助手，在功能上远超一般人的想象。微软官方数据显示，Security Copilot 每天接收超过**65万亿个威胁信号**——这个量级，传统安全工具根本不可能处理。

它能做什么？自然语言驱动的威胁调查、自动生成安全事件报告、自动给出修复建议、针对可疑用户行为的自主调查……换句话说，过去需要一个 SOC 分析师盯着屏幕干几小时的活，Security Copilot 可以在分钟级完成。

更关键的是定价策略。2025年起，Microsoft 365 E5 订阅用户无需额外付费即可获得 Security Copilot 能力。对于已经大规模使用微软套件的企业来说，这相当于"免费升级了 AI 安全能力"——门槛几乎为零。

这就是平台化战略的威力：不用让你专门为安全买单，悄悄把你锁进生态。

2025年Ignite 大会上，微软进一步推出了Security Copilot 代理（Agent）功能——AI 不再只是"助手"，开始能自主执行特定安全任务。这标志着安全运营从**"人工决策"向"AI自动驾驶"**迈出了关键一步。

### **Google：数据底牌拥有者**

Google 的胜负手不在模型，在数据。

2025年，Google 推出 **Sec-Gemini v1**，一款专门为网络安全场景优化的推理模型。这款模型整合了三个独特的数据源：

·**Mandiant**：全球顶级的 APT 威胁情报公司，Google 2022年以54亿美元收购

·**VirusTotal**：全球最大的恶意软件分析数据库

·**Google 威胁情报（GTI）**：来自 Google 自身搜索、邮件、云等全球基础设施的庞大威胁数据

三者叠加，构成了竞争对手几乎无法复制的数据护城河。在 CTIBench（网络威胁情报基准测试）中，Sec-Gemini 领先其他模型最高11 个百分点，而SecLM 安全平台在CTI-MCQ 测试中达到88.5%，比第二名高出14 个百分点。

Google 把这些能力全部嵌入了 **Google SecOps**（前身是 Chronicle）——一个整合了 SIEM、SOAR 和威胁情报的全栈安全运营平台。2025年，Google SecOps 被 Gartner 评为 SIEM 魔力象限领导者，正式进入企业安全运营的核心场景。

有一个真实案例：某金融机构接入 Google SecOps 后，检测响应时间从 2 小时压缩到 15 分钟，同时处理的数据量扩大了22 倍。

但 Google 的产品并非无懈可击。安全研究员 Viktor Markopoulos 的测试发现，Gemini 易受"ASCII 走私攻击"影响——攻击者在邮件里插入极小字号的隐藏提示词，当用户让 Gemini 分析该邮件时，AI 会同时执行这段隐蔽指令。由于 Gemini 已深度整合进 Google Workspace，能访问用户的邮件、日历和文档，这个漏洞的潜在危害被进一步放大。

讽刺的是，Google 认为这属于"社会工程学手段"而非安全漏洞。这一态度，本身也是一种风险信号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOkVESBHXkH6WI5wgyFQRQPSicmyPUtkVShM12icu1GeoJY22F6iakic8V712hppagg9TQzq4cDlGpc6xq6U8VD0bLIUXwhvmDk2lJk/640?wx_fmt=png&from=appmsg)

### **Anthropic：掀桌子的人**

Anthropic 在安全领域的声名，有一半来自他们自己主动"坦白"的事情。

2025年8月，Anthropic 发布报告，承认发现黑客试图利用 Claude 进行网络犯罪，包括编写钓鱼邮件、生成恶意代码、规避安全过滤器。Anthropic 表示系统已成功阻止这些滥用，并将整个过程公开，帮助业界理解风险。[利用大模型发起大规模网络安全攻击](https://mp.weixin.qq.com/s?__biz=MzI5NTQ3NzIxMw==&mid=2247485789&idx=1&sn=90ad50849bc3755550e7662c71848635&scene=21#wechat_redirect)

没有哪家同量级的 AI 公司会主动公开这种事。但这正是Anthropic 的策略——**用透明度建立信任**。

这种信任，在2026年2月变成了产品：**Claude Code Security**。

它不是基于规则的静态扫描工具，而是像一个真正的安全研究员一样，用语义推理去分析代码中的业务逻辑漏洞——那些 Veracode、Checkmarx 这类工具因为依赖规则引擎而永远找不到的漏洞。Claude Opus 4.6 已在真实代码库中发现了超过 500 个"隐藏数十年"的安全缺陷。

这对传统 SAST/DAST 工具的杀伤，是代际层面的，不是用优化能填平的差距。

### **xAI Grok：与政府合作**

Elon Musk 的 xAI 走了一条完全不同的路。

2025年7月，**Grok for Government** 上线。xAI 与美国国防部签署了价值上亿美元的合同，Grok 4 将以IL5 安全级别（可处理受控非机密信息）部署，面向全部300 万国防部人员——这将是历史上规模最大的政府AI 部署。

从产品能力上看，Grok 的核心优势是实时联网能力和 X（原 Twitter）平台的庞大实时数据流，在威胁态势感知和开源情报收集方面具有独特价值。但在企业级商业安全市场，xAI 目前尚无专项产品布局。

和 Google 同样存在安全短板——安全研究人员的测试表明，Grok 也未能通过 ASCII 走私攻击防护测试。

xAI 的逻辑很清晰：企业安全市场你们去打，政府那块超高门槛、极少竞争的蛋糕，我来拿。Elon Musk 的政治影响力，在这个场景里就是最有价值的"竞争壁垒"。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibANIaIJODOloyoqfKiar1V5z37SQFVedKDln6NDY1PQkltGRcagjmibMAcy1yOCahEWibj31UQibXBXOBAcqd3z8mgAEjxxDwIo2dJoKwzw4Aow/640?wx_fmt=jpeg)

## **二、战场差异**

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOmgkSBTHFkduHNN0qFzEwyjZTIdaTXM5MVQkAhfgjftBUuynfaKUSCvicZE0UwSuRgQOLYxpXeNKDapRJaEH9zffkaMAhEgv8Ig/640?wx_fmt=png&from=appmsg)

图：四大厂商能力与定位对比

**漏洞检测能力**：Anthropic 最激进，Claude Code Security 直接对标并超越传统 SAST 工具，是当前对传统安全厂商冲击最大的一个。

**威胁情报深度**：Google 断层领先。Mandiant + VirusTotal 的数据资产是短期内无法被模仿的。

**企业落地成熟度**：Microsoft/OpenAI 体系最高，Security Copilot 已无缝嵌入企业 Microsoft 365 生态；Google SecOps 次之，已有成功案例；Anthropic 产品刚刚起步；xAI 主打政府而非商业。

**安全可控性**：Anthropic 最强，"宪法式 AI"方法论在 ASCII 走私攻击测试中表现优异；OpenAI/Microsoft 中上水平；Google 和 xAI 在防护测试中均有明显短板。

**对传统安全市场的破坏力**：Anthropic 最直接，正面进攻SAST/DAST；Google 整合替代 SIEM/SOAR；OpenAI/微软布局深远；xAI 差异化绕道，暂无正面冲击。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOlEZQL18atCIjAG4piawicB1OSwCCFjCw1Ic3T6tyrkSjOBT7NoOaT64ppfOicujvKyYiboC1WibTrGcW1oHeib6NrBtIMnrPvtUhS9I/640?wx_fmt=png&from=appmsg)

根据瑞银2026年网络安全展望报告，CISO 们的预算优先级已经说明了一切——**防火墙**类产品仅有 33% 的受访者计划增加预算，而**云安全**（62%）、**身份安全**（59%）、**安全运营与分析**（55%）预期强劲增长。这正是 AI 重塑安全产品优先级的直接体现。

三、对整个行业的真实冲击

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOmdc22WiaAPoemBwHFNheHXGmTWftWUJ10lujjJaXlmTBuZE4b6sT2QUH2VAX0HibuNcuYDZicm5hOAhTYpaRlnLCicN7VJ4x58iaqA/640?wx_fmt=png&from=appmsg)

图：大模型的进入正在重构行业格局：从产品边界的模糊到价值链的重组

### **被正面打穿的：传统漏洞扫描工具**

Veracode、Checkmarx 这类工具的核心逻辑是"规则匹配"——你告诉它某类写法有风险，它就扫描这类写法。但它无法理解代码的业务逻辑，无法发现那些"规则上没问题、业务上有漏洞"的安全缺陷。

Claude Code Security 的逻辑是"语义推理"——它像一个懂业务的安全研究员，从攻击者视角推导出潜在漏洞路径。这不是同类工具之间的竞争，而是代际差异。

Anthropic 发布当天，JFrog、GitLab 等开发安全工具提供商的股价也出现明显波动，投资者用行动表达了判断。

### **被加速替代的：SIEM 传统厂商**

Splunk、IBM QRadar 的核心价值是"数据聚合+规则告警"。Google SecOps 已经证明，AI 可以让分析师用自然语言查询日志，让检测响应时间从2 小时缩到15 分钟。

更关键的是：AI 大幅降低了 SIEM 的使用门槛。以前需要专业培训才能运用的工具，现在可以用自然语言提问。这让企业的 SIEM 选型逻辑发生了根本性改变。

### **被压缩的：初级SOC 分析师岗位**

告警分类、日志分析、事件摘要……这些 Tier-1 的基础 SOC 工作，正在被 AI 快速自动化。

Gartner 预测，到2026年超过 80% 的企业将在安全运营中部署某种形式的 AI 助手。这意味着同等工作量所需的初级分析师数量，会持续收缩。

岗位不是消失，是要求变了——会用 AI、能监督 AI、能在关键节点做决策，成为新的基础门槛。

### **最容易被忽视的风险：攻击者也在用AI**

Anthropic 的官方报告揭示了一个令人不安的现实：技术资源匮乏的威胁组织，现在也能借助AI 发动大规模、高复杂度的攻击。

2025年11月，研究人员记录了首例**AI 策划的网络攻击活动**——AI 自主完成了80-90%的攻击战术操作，成功入侵约30个目标组织。这不再是假设，这是已经发生的事。

防御方的工具在升级，攻击方的门槛在降低。这个不对称，才是整个行业最深层的挑战。

> ⚡ 攻防失衡风险：低资源攻击者能力跃升：Anthropic 在披露案例时明确指出："技术资源匮乏的团体现在也能发动大规模、高复杂度的攻击。"这意味着网络犯罪组织、小型国家行为者的攻击能力门槛将大幅下降，防御方面临更加不对称的竞争环境。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOniaXkmiaot4IgcLUUhfNAjSR6mftgZHyxK8wPxVeTyBKApuc7Hn4m0ITxmFIHibnOPwcGZa0nwicicdCL5WUUURG8m8UBeJ9GFialY0/640?wx_fmt=png&from=appmsg)

图：基于AI的网络攻击的生命周期

## **四、产品战略、人才市场、营销格局的系统性变化**

### **产品层面：三大转变**

**从"规则"到"语义"**。AI 安全产品正在推动安全工具从特征匹配向语义理解的根本性转变。这不是渐进改良，是技术代际更替。

**从"孤立产品"到"平台生态"**。Microsoft Security Copilot 与 Microsoft 365 的绑定策略已经成为行业新标准。CrowdStrike、Palo Alto Networks 也在加速平台化整合，试图在 AI 时代维持竞争力。瑞银报告指出，CrowdStrike 年度经常性收入（ARR）已突破 40 亿美元，其 Falcon 平台模式被视为"云原生+AI"的成功路径。

**从"工具"到"代理"**。Security Copilot 代理、AI 自主安全响应……安全运营的自动化程度正在快速深化。瑞银预测，CrowdStrike、SentinelOne 等厂商可能在2026年首次披露"智能年度经常性收入"（agentic ARR）数据，AI 代理的商业化拐点或许近在眼前。

从"平台"到"专项"：两条路径的分叉：

**路径A：垂直专项工具（Anthropic / OpenAI）**

直接切入安全领域特定任务（漏洞检测、代码审计），与传统安全工具正面竞争。优点是价值主张清晰、冲击力强；风险是边界模糊可能带来监管和责任问题。

典型打法：Anthropic 的 Claude Code Security 免费开放给开源社区，快速建立品牌与信任，再向企业付费转化。OpenAI 的 Aardvark 同样对非商业开源项目免费，通过"公共品"定位积累声誉。

**路径B：平台级整合（Google / xAI）**

将安全AI 能力嵌入更大的平台生态（SecOps、政府平台），通过生态锁定实现护城河。Google 拥有 Mandiant + VirusTotal 的独特数据资产；xAI 拥有 X 平台实时数据和政府合同。

典型打法：Google 将 SecOps 定位为整合 SIEM+SOAR+TI 的"终极平台"，通过 Gemini 提升用户黏性而非直接替代；xAI 以高安全认证（IL5）为壁垒，锁定高门槛政府场景。

### **人才层面：480万的缺口和七类新岗位**

工业和信息化部教育与考试中心等机构联合发布的《AI时代网络安全产业人才发展报告（2025）》给出了一组核心数字：

**2025年全球网络安全人才缺口达480 万人，同比增长19%。**

AI 没有缓解人才短缺，反而在创造新的需求。报告首次列出了"AI 驱动的网络安全岗位图谱"，七类新兴职业值得关注：

·**智能体架构师**：设计和构建 AI 安全代理系统

·**模型安全红队**：专门测试和攻击 AI 模型以发现漏洞

·**提示词安全工程师**：确保 AI 系统免受提示词注入攻击

·**AI 合规审计师**：随 AI 监管趋严，需求将大幅增长

·**AI 风险顾问**：评估和管理 AI 应用的安全与合规风险

·**数据合成专家**：生成高质量 AI 安全模型训练数据

·**智能防御架构师**：设计集成 AI 能力的新型安全体系

从薪酬来看，A股上市安全公司人均年薪24 万元人民币，高出非上市企业 50%。高级AI 安全岗位的溢价更为显著，薪酬普遍高于传统安全同级别岗位。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOksnCPHwp7yLxrJE58DrB61U4e9ZNZnBPClBxYrawia3U8YEy7S7o5KESBhOdzg0jBFqff72KiaBABgTyIg56sFadob3XDgZBK7w/640?wx_fmt=png&from=appmsg)

图：安全 AI 交叉人才成稀缺资源

### **营销层面：叙事范式的根本转换**

传统安全厂商的营销核心是"功能参数"——吞吐量多少、规则库多大、检测率多高。

AI 安全产品的营销核心是"效率跃迁"——响应时间从 2 小时到 15 分钟，分析师效率提升数倍。

Microsoft 最擅长这种叙事，把 Security Copilot 定位为"机器速度、规模防御"，成功重新定义了企业客户对安全产品的期望值。

订阅制定价也在加速普及。传统的"买断式"安全软件正在让位给"订阅+AI 能力持续升级"模式。用户支付的不再是软件许可费，而是持续获得 AI 能力的权利——这种定价逻辑，也在改变用户评估...