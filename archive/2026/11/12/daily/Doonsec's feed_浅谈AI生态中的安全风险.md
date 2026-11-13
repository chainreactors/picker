---
title: 浅谈AI生态中的安全风险
url: https://mp.weixin.qq.com/s/NjJQXtnqj9IO4hcZdkXvWg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:00:39.580924
---

# 浅谈AI生态中的安全风险

# 浅谈AI生态中的安全风险

搜狐安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

概述

![](https://mmbiz.qpic.cn/mmbiz_png/nE1wniah9EGQOAibRG1M2E64gUmebTdWmu4PCeZEnP9o2smfR1LT9AVX4E0rZLsiaQseicVh1xzn6zuPI3CatXFHmA/640?wx_fmt=png)

AI应用生态已演化为一个由模型层、推理运行时、知识层、协议层、技能层、智能体层、编排层、开发层、多模态创意层共同构成的复杂技术栈。每一层在提供特定能力的同时，也引入了一类区别于传统软件安全的独特攻击面。传统软件安全的核心矛盾是“代码执行的可控性”，而AI生态安全的核心矛盾则在于：自然语言既是数据又是指令，模型既是处理器又是决策者，智能体既是工具的使用者又是授权的持有者。攻击者可以在不触碰任何一行恶意代码的情况下，通过操纵语义、污染上下文或寄生合法工具链来完成从数据窃取到系统接管的攻击。

![图片](https://mmbiz.qpic.cn/mmbiz_png/MHUYuRza9XXs6ZgPXPgq4d0EamTH6xXcMNoCuad3NGhB6S5ehibqZF6DYedz1aVQuKYbqvjclEkKgLVJRGWpeiaw/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

AI生态安全风险

**01**

模型层

常见应用与概念：闭源商业模型（GPT、Claude、Gemini、Grok）；开源权重模型（Llama、Qwen、DeepSeek、Mistral、GLM）；多模态/全模态模型；推理专用模型；模型微调与蒸馏；模型注册与分发平台（Hugging Face、ModelScope）；模型格式（safetensors、GGUF、pickle）。

常见安全风险：模型供应链投毒与权重后门；不安全反序列化格式导致加载即执行代码；模型窃取与API查询重建；对抗样本与越狱绕过安全对齐；训练数据污染与记忆泄露；模型输出幻觉被恶意利用；多模态输入中的隐蔽指令注入；模型许可与合规风险；模型版本回滚与完整性校验缺失。

安全建议：优先使用无法执行代码的安全模型格式（如safetensors），避免加载不可信的pickle文件；在加载前对模型文件及其元数据进行扫描，验证来源与完整性；建立模型溯源记录（provenance）（来源、哈希、版本），对生产环境模型实施签名校验；对模型输出保留人工复核通道，尤其在高风险决策场景中不以模型输出作为唯一依据。

**02**

本地推理与运行层

常见应用与概念：Ollama、vLLM、TGI（Text Generation Inference）；LM Studio、Jan、GPT4All等桌面推理工具；GGUF模型加载器；兼容OpenAI的API网关。

常见安全风险：管理API默认绑定0.0.0.0且无认证；模型加载器内存安全缺陷导致进程内存（含API密钥、云凭证、对话数据）泄露；多租户隔离不足；资源耗尽与拒绝服务；未授权模型拉取、推送与删除；推理服务补丁滞后；本地部署被误认为天然安全而缺乏网络边界控制。

安全建议：将监听地址强制绑定至127.0.0.1，如无必要不暴露至网络接口；在推理服务前置反向代理（Nginx或Caddy）实施认证、TLS与速率限制，Ollama本身不内置认证，必须由外部层补齐；通过防火墙或安全组限制访问来源；启用API密钥（vLLM的--api-key）并避免使用--trust-remote-code加载不可信模型仓库；建立自动化更新管道并订阅安全公告。

**03**

数据与知识层 / RAG

常见应用与概念：向量数据库（Pinecone、Qdrant、Weaviate、Milvus、Chroma、pgvector）；RAG编排框架（LlamaIndex、Haystack）；一体化知识库平台（RAGFlow、Dify知识库、FastGPT）；GraphRAG、Agentic RAG；嵌入模型与重排模型；文档解析与切分管线；记忆系统（短期/长期/工作记忆）；知识图谱。

常见安全风险：知识库投毒与事实操纵；间接提示注入通过检索文档进入上下文；向量逆变换恢复原始文本；权限继承错误与越权检索；多租户数据串库；嵌入模型供应链污染；记忆污染与长期驻留的恶意内容；文档解析器漏洞。

安全建议：将权限校验前置到检索层，在向量相似度排序之前按用户角色过滤候选文档，确保模型“从一开始就看不到无权内容”；对高风险知识实施“强审核后入库”，保留所有变更记录与来源元数据；对管理员与知识库维护人员强制多因素认证，实施基于角色的细粒度访问控制；在RAG流水线中部署内容过滤层，在文档进入模型上下文之前拦截恶意内容；对向量数据库实施网络隔离与访问审计，避免其成为“明文的等价暴露”。

**04**

协议层 / 连接

常见应用与概念：MCP（Model Context Protocol）Server/Client；MCP注册中心与Gateway；工具描述与能力声明（schema、manifest、tool descriptor）；A2A（Agent-to-Agent）协议；GNAP；OAuth/令牌传递；工具调用链编排。

常见安全风险：工具描述投毒与能力声明伪造；令牌透传与混淆代理导致权限提升；认证缺失或弱授权（MCP规范将授权设为可选项）；上下文与工具隔离不足，使对抗性指令跨工具传播；寄生工具链将多个合法工具组合为恶意工作流；注册表审核与所有权校验薄弱；服务器更新后行为漂移；审计日志无法还原组合调用意图。

安全建议：将MCP服务器视为不可信的操作系统进程而非协议层沙箱，在容器、沙箱或VM中隔离运行本地服务器，限制其对文件系统、环境变量和出站网络的访问；验证token受众，拒绝令牌透传，从最小scope起步，工具执行前要求用户确认，并将工具描述视为不可信输入；对schema和manifest实施签名校验，registry保持不可变和可追溯，schema变更实施多人审批；记录工具调用和scope提升，以便回溯Agent的实际行为；坚持最小权限与自动scope过期，对第三方插件实施隔离运行。

**05**

技能层 / Skill

常见应用与概念：技能包与技能市场（ClawHub、Skills.sh、Smithery、SkillHub、DeepSkill）；企业技能注册中心；技能创建工具（skill-creator）；SOP模板与提示词工作流。

常见安全风险：自然语言描述中的语义级恶意指令；伪装“前置依赖安装”的下载器与投毒；权限声明过宽与最小权限缺失；技能更新后行为漂移；传统代码扫描对语义威胁漏报；代码特征与语义意图混合导致检测困难；技能间依赖混淆与供应链传播；执行缺少运行时行为审计；用户对Agent操作流程的过度信任被利用。

安全建议：将Skill视为需要安全审查的软件，实施安装审批工作流，建立集中式Skill清单（名称、版本、哈希、安装者、扫描状态）；采用“先检测、再准入、后运行”的全生命周期治理，从来源、功能描述、权限、运行行为、版本更新五个维度持续校验可信度；对Skill实施运行时审计，记录文件访问、网络调用与Shell命令；建立正式的Skill撤销流程并与离职流程和事件响应预案绑定；优先使用提供“验证后信任”治理层的私有化Skill Registry。

**06**

智能体层 / Agent

常见应用与概念：编码Agent（Cursor、Claude Code、Codex CLI、Windsurf、GitHub Copilot Agent）；通用任务智能体（Manus、OpenClaw）；浏览器/桌面Agent；语音Agent；多智能体平台（CrewAI、AutoGen、LangGraph、Microsoft Agent Framework）；工具调用循环、状态管理与检查点、记忆与规划模块。

常见安全风险：目标劫持与提示注入驱动工具滥用；过度代理（功能过多、权限过大、自主过高）导致超出用户意图的破坏性动作；记忆污染与跨会话传播；多Agent之间的恶意指令扩散与共谋；框架序列化/反序列化与状态检查点漏洞；不可逆操作缺少审批；环境变量与秘密在Agent上下文中暴露。

安全建议：将LLM提供的工具参数视为不可信输入，使用允许列表、类型与范围约束、路径遍历防护和参数化查询进行校验；对高风险工具（有副作用、涉及敏感数据、不可逆、影响面广）强制人工审批；维护工具白名单，每个工具只暴露最小动作，下游系统使用专用最小权限身份；将系统提示视为软约束而非安全边界；对多Agent系统实施任务级scope的工具访问和深度防御。

**07**

编排与自动化层

常见应用与概念：可视化工作流平台（n8n、Dify、Coze、Make、Zapier）；LLM应用开发平台；代码级编排框架（LangGraph、LlamaIndex Workflows）；触发器、分支、审批节点、重试与回滚；连接器与凭据管理；事件驱动自动化。

常见安全风险：表达式求值与模板引擎导致远程代码执行；凭据集中存储成为高价值目标；触发链中的语义组合产生非预期行为；工作流越权与审批绕过；单个实例沦陷后横向移动至数据库、云服务和内部API；连接器权限过宽；版本回滚与变更审计不足。

安全建议：将编排平台视为集成枢纽而非普通应用来评估其安全边界，对表达式求值引擎实施严格沙箱隔离，禁用不必要的运行时访问；凭据集中存储应使用专用密钥管理服务，实施最小权限与定期轮换；对工作流变更实施版本化与审批，保留完整的变更审计链；连接器权限按任务最小化，避免“万能连接”模式。

![图片](https://mmbiz.qpic.cn/mmbiz_png/MHUYuRza9XXs6ZgPXPgq4d0EamTH6xXcMNoCuad3NGhB6S5ehibqZF6DYedz1aVQuKYbqvjclEkKgLVJRGWpeiaw/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/tD6Xsicic7CBic2juibZhNKsic15Io2s7S9FnjztLW5uhI7EpGiaRAR2xwGPmqoTsER2LV4RcX3N2qJDXQAvnmYzvZdQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

安全风险案例

![图片](https://mmbiz.qpic.cn/mmbiz_png/oMhY28hE0NDebWDV9vG2iagAybWTzM7kS9W2dToqSnktZgjtEowvsiau26W5iabV3mSvEEZbhr4ZGmhbVyLosjNIQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

案例一

Ollama“Bleeding Llama”——无认证推理运行时的进程内存暴露

CVE-2026-7482是Ollama GGUF模型加载器中的堆越界读取漏洞。攻击者构造一个包含被恶意操纵的GGUF文件，当Ollama加载该文件时，读取操作越过了分配的堆内存边界，将进程内存中的提示词、消息、环境变量、API密钥和令牌暴露给未认证的远程攻击者。攻击者随后可利用Ollama的模型推送功能将泄露的堆数据外传到其控制的服务器，整个攻击链仅需三次未认证的API调用。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1Wh6LtiaZcnKm9icgGHzPCX6FOubtLNV2IxJZWw5HKYXM8kv5fMF2RZG69lrAQhtad1ticY9IYGXvbIzIPqyJVbiaquXZ0HiaEpibCx0/640?wx_fmt=png&from=appmsg)

案例二

RAG知识库投毒——从量化研究到企业智能客服失控

USENIX Security 2025的PoisonedRAG论文给出了RAG投毒的量化底线：向百科知识库注入0.01%的投毒文档（一万份中混入一份），针对特定问题的攻击成功率即达到73%；0.001%的注入比例仍有22%的成功率。这组数据的含义是，一个收录百万份文档的企业知识库，混入几百份投毒文档就足以造成实质伤害，而几百份文档在人工抽检中几乎不可能被发现。这一风险已有真实的企业侧印证：某电商公司的智能客服上线一个月后开始输出错误政策——用户问退款政策，它回答“30天内无条件退款”；问运费，它说“满9.9元包邮”。排查发现知识库中混入了47份伪装成FAQ的投毒文档。投毒路径既可以是外部爬虫抓取的公开内容在入库前未经安全审查，也可以是内部运营人员或外包团队的写入权限被滥用。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1W42lyGN9PyKV9aoYVxWf13epia2lIEibkMunZWY0ibR9tgdSI50u4rjHykGKibNm7QanZjsibQRDw5x5JCDe4WY6GFhoqyl2QicuHibw/640?wx_fmt=png&from=appmsg)

案例三

LibreChat MCP集成——环境变量通过MCP服务器URL注入泄露

CVE-2026-32625（LibreChat ≤ 0.8.3）展示了MCP协议层的一个基础性缺陷：LibreChat在Zod schema验证期间对用户提供的MCP服务器URL解析${VAR}占位符时，直接对照服务器的process.env进行变量展开，任何已认证用户都可以创建一个指向攻击者控制域名的恶意MCP服务器配置，在URL中引用CREDS\_KEY、CREDS\_IV、JWT\_SECRET、MONGO\_URI等敏感环境变量，LibreChat服务器在验证时将这些秘密解析进请求URL并发送到攻击者服务器。获得JWT\_SECRET可伪造认证令牌，MONGO\_URI提供数据库直接访问，CREDS\_KEY和CREDS\_IV可解密存储的敏感数据——不需要管理员权限即可完全攻陷安装的加密材料和数据库凭据。

案例四

ClawHavoc——Skill市场的大规模供应链投毒

2026年1月底至2月中旬的ClawHavoc行动是迄今为止针对AI智能体技能生态最大规模的协同供应链攻击，由OpenSourceMalware与Trend Micro等安全团队披露。核心攻击者hightower6eu通过注册开发者账号，在ClawHub上上传了1,184个伪装成常用工具的恶意Skill。为绕过审核，攻击者采用"ClickFix"社工方法，在组件说明文件中诱导用户手动执行包含Base64编码或代码混淆的恶意命令，而非直接将恶意代码写死在Skill核心逻辑中。安全公司Koi Security对ClawHub上2857个Skill进行全面审计，识别出341个恶意样本，占比约11.9%；Snyk对ClawHub和skills.sh上3984个技能的审计发现36.82%（1467个）存在安全缺陷，其中13.4%（534个）包含至少一个严重级安全问题，76个确认为恶意载荷。恶意Skill被伪装成各类高频应用工具，包括仿冒的官方工具、加密货币工具、YouTube工具、自动更新器、金融数据工具等。事件造成用户加密货币损失等严重后果，OpenClaw官方于2026年2月7日与VirusTotal合作对上传的Skill包实施强制安全扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gdu7PMCZg1UXKVicD8rYeOMUgCfldxdwHjeicSkeUVicLZ8rRqzYvfLzAGp2vZdJqXebicJsG643QyR0exTDl1hGoY7qROHdEKHYcia1V0mo3Weg/640?wx_fmt=png&from=appmsg)

案例五

n8n表达式注入——编排枢纽的远程代码执行

CVE-2025-68613（CVSS 9.9）影响n8n 0.211.0至1.120.3版本及1.121.0版本。漏洞位于工作流表达式求值系统：已认证用户在配置工作流时提供的表达式，在未与底层运行时充分隔离的执行上下文中求值，攻击者可以突破表达式边界，以n8n进程的权限执行任意代码。成功利用可导致受影响实例的完全沦陷，包括未授权访问敏感数据、修改工作流和执行系统级操作。

![](https://mmbiz.qpic.cn/mmbiz_png/Gdu7PMCZg1XNjkNF53el5IMjp3rJuzoIRm8cAuRibTnabGKVEGJ588aSUO5IVibNdEFx6Lfsto6fTJsBicibIicXxp7h8CAia4eVda8rZED1HhuNM/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/MHUYuRza9XXs6ZgPXPgq4d0EamTH6xXcMNoCuad3NGhB6S5ehibqZF6DYedz1aVQuKYbqvjclEkKgLVJRGWpeiaw/640?&wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

总结

传统软件安全依赖“数据”与“代码”的边界，AI生态使这一边界失效：RAG文档、MCP工具描述、Skill说明、Agent输出，都在合法语义通道中同时承担“内容”与“指令/依据”的双重角色。攻击者不需要注入恶意代码，只需植入“合法内容”，等待系统以合法方式将其解释为恶意行为。风险的本质不是某一行代码，而是合法机制在默认配置或信任假设下的非预期组合。因此，治理重心应从“扫描恶意代码”转向执行隔离与语义治理：以沙箱、最小权限替代对语义的信任；以运行时审计覆盖安装时扫描无法触及的行为漂移；将“语义偏离”本身作为一等安全信号，而不仅仅记录“工具被调用”，让高风险动作始终保留人工复核。

![](https://mmbiz.qpic.cn/mmbiz_png/Qvc3iaVjc5XwexerxgYHuNia5BjtSC4s99ibuB1t8anvHGPZUcGPzeh4ysQNCfYrfoHx21AWaxRibuUPJ9RIcjPlqw/640?wx_fmt=png)

END

参考链接

Cyera. (2026). Bleeding Llama: From a GGUF File to 300K AI Inference Services Compromised. https://www.cyera.com/

https://nvd.nist.gov/vuln/detail/

https://snyk.io/research/toxic-skills-age...