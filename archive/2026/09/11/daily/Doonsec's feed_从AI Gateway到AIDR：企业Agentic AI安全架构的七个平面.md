---
title: 从AI Gateway到AIDR：企业Agentic AI安全架构的七个平面
url: https://mp.weixin.qq.com/s/0fFxTicHFTqROUBlh2sb8A
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:43:44.351215
---

# 从AI Gateway到AIDR：企业Agentic AI安全架构的七个平面

# 从AI Gateway到AIDR：企业Agentic AI安全架构的七个平面

原创

guowei
guowei

网络安全直通车

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

---

# 从AI Gateway到AIDR：企业Agentic AI安全架构的七个平面

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V1icTKBjMOiav4lPPOSsOXnYHfrK5jdU9HWV88H9wXtgOXtWOrSTP55brvYENLUBblA2fM25ksdjbTe02huhWyT9SSxrQYeK92IkibgrtGGfeY/640?wx_fmt=jpeg)

> 当Agent不再只“回答问题”，而是调API、读数据库、发邮件、改权限、写代码，安全架构就不能再只做Prompt过滤了。

2025年底OWASP发布面向Agentic Applications的Top 10（ASI01–ASI10）后，行业基本达成共识：传统LLM安全管“说什么”，智能体安全管“做什么”。 目标劫持、工具误用、身份权限滥用、记忆污染、MCP/插件供应链、多Agent通信、级联失败，已经不是理论风险。

但市场上名字很乱：AI Gateway、LLM Guardrail、AI-SPM、Agent Security、Agentic Endpoint、AI Runtime、AIDR、AI-DR、ADR……本文用一个更落地的框架串起来：先定义保护对象，再按行为链做检测，最后把AIDR/ADR放回“运行时检测与响应”的正确位置。

---

## 一、先别买盒子，先画Agent的五类运行区域

一个Agent执行一次任务，通常跨五个区域，安全边界也在这些区域之间断裂：

1. **主体与输入区**：用户、服务身份、上游Agent，以及网页、邮件、文档、RAG内容等不可信输入。
2. **Agent执行区**：终端编码/CLI/桌面Agent、云端自建Agent、SaaS/低代码Agent。
3. **推理与上下文区**：模型、系统提示、会话历史、短期/长期记忆、RAG、向量库。
4. **动作与协议区**：MCP、工具、插件、API、A2A、Shell、文件、浏览器、进程。
5. **资源与影响区**：SaaS、数据库、代码仓、云资源、CI/CD、终端OS。

只看“模型流量”会漏掉终端进程和SaaS内部动作；只看“终端进程”又看不懂Agent意图和工具语义。所以Agent安全的第一原则不是“所有流量走一个网关”，而是多执行点关联。

---

## 二、运行时分析的单元不是“一次HTTP请求”，而是“一条行为链”

两个完全相同的HTTPS调用，风险可能完全不同：

* 用户明确要求Agent查工单→只读访问工单系统；
* 网页间接提示注入→诱导Agent读本地密钥→再用相同域名的上传接口外发。

因此运行时应以“任务/会话因果链”为基本单元：

> 发起者与原任务 → 输入及来源 → 会话/记忆/检索上下文 → Agent计划 → 工具/MCP/API调用 → 使用的身份与凭证 → OS/SaaS/云操作 → 实际结果与影响范围

至少保留四类关联ID：会话/任务ID、Agent及版本、主体与委托身份、工具调用与下游动作ID。没有这些，SIEM里只能看到分散事件，复盘时永远答不出“它为什么这么做”。

公开案例中，间接注入类尤其典型：Cequence在映射OWASP Agentic Top 10时举到EchoLeak式场景——共享文档里的隐藏指令即可把Copilot类会话变成数据外传通道，不需要钓鱼、不需要恶意附件。 这类问题不是内容过滤单独能解决的。

---

## 三、七个能力平面：别把AIDR扩成“所有AI安全”

完整企业Agent安全可抽象为七平面：

| 平面 | 核心问题 | 典型能力 |
| --- | --- | --- |
| 发现与资产 | 有哪些Agent/MCP/Skill/插件/模型 | 影子Agent识别、Agent BOM、所有者、关系图 |
| 姿态与供应链 | 运行前结构性风险 | 代码/配置/依赖/模型扫描、过度权限、暴露面 |
| 身份与访问 | 谁委托Agent、以什么身份访问什么 | Agent独立身份、短期令牌、工具授权、审批 |
| 运行时观测与检测 | 正在做什么、是否偏离任务 | 全会话追踪、注入/工具滥用/记忆污染检测 |
| 在线执行与隔离 | 高危动作执行前拦不拦 | allow/block/mask、参数改写、沙箱、人工确认 |
| 调查与响应 | 影响了什么、怎么恢复 | 因果重建、停Agent、撤令牌、隔离、回滚 |
| 验证与治理 | 已知攻击能否打穿 | 红队、基准、策略回归、合规映射 |

按这个定义，很多“叫AIDR”的产品其实只覆盖其中几块：

* 只做Prompt/Response过滤 → Guardrail，不是AIDR；
* 只代理模型API → AI Gateway，是PEP之一，不是AIDR全部；
* 只列Agent/MCP资产与权限 → AI-SPM，属于姿态管理；
* 只做日志展示无检测响应 → Observability，不完整；
* EDR看到进程/文件/网络，但不关联Agent会话/工具/原任务 → 缺Agent语义。

AIDR/ADR的硬条件应是五件事：会话级关联、Agent语义、下游影响证据、检测逻辑、响应动作。内联阻断很重要，但不是所有PEP都支持同步拦，产品必须说明“哪类动作执行前拦、哪类只能检测后响应”。

---

## 四、六类策略执行点，按Agent位置组合用

1. **终端/浏览器Sensor**：适合编码、CLI、IDE、桌面Agent。看进程、Shell、文件、网络，能发现未纳管Agent。代表如CrowdStrike Falcon Guardian、Cortex Agentic Endpoint、Microsoft Defender相关能力、Uber ADR Sensor。劣势是不天然懂云端Agent内部状态。
2. **Agent Hook/SDK/Harness**：在pre-model、post-model、pre-tool、post-tool、handoff、memory等节点采事件、做策略。最懂上下文，但依赖框架集成。OWASP Agent Control Standard正做事件/策略标准化。
3. **LLM/AI Gateway**：做模型选择、Prompt/Response检查、敏感数据、成本控制、审计。看不到不经过网关的本地动作，也常丢Agent内部计划/记忆/工具结果。可作PEP，不应是唯一控制点。Cequence类等方案会把Gateway映射到OWASP ASI多项，但企业要避免“网关万能”误区。
4. **MCP/Tool Gateway**：在Agent与工具之间认证、授权、校验参数、藏凭证、记录调用。比模型网关更靠近“动作”，但本地Shell、直连API、平台内部工具可能绕开。
5. **Sidecar/网络代理/Workload Sensor**：适合自建Agent和云负载，看网络/容器/进程；要补Agent事件才有意图。
6. **SaaS API/云审计/EDR-XDR**：验证最终影响，如权限变更、数据导出、云资源创建、代码提交。常异步，未必能执行前拦，但调查和响应不可替代。

企业真实架构通常是“终端覆盖本地Agent + Hook覆盖自建Agent + Gateway覆盖模型/工具 + SaaS/云/EDR补最终影响”。

---

## 五、厂商路线差异：不是谁功能多，而是“观测点在哪、能否响应”

公开材料里几条典型路线：

* **终端/运行时延伸**：CrowdStrike Falcon Guardian以Falcon Sensor为核心，把Prompt、身份、Skill与端点进程/文件/网络关联，做因果链和Containment；其自有AI Gateway等组件在部分资料中仍处即将推出/未GA状态。 适合已有Falcon、终端Agent多、要进SOC的企业。
* **全生命周期平台**：Palo Alto用Prisma AIRS做运行时/姿态/数据、AI Agent Gateway做模型与工具入口、Cortex Agentic Endpoint补终端、SaaS Agent Security补低代码，整体偏“平台化”。Prisma AIRS已被多家分析归入AI运行时/平台整合路线。
* **SaaS/低代码治理**：Zenity从Copilot Studio、Power Platform、Agentforce等低代码Agent做发现、会话级行为、AISPM联动，强项是平台型Agent多、公民开发多的环境。
* **Runtime/MCP基础设施**：Operant类强调MCP Gateway、Agent Protector、内联越权/外泄阻断；适合自建Agent、MCP、多云工作负载。
* **开源检测基准**：Uber ADR分Sensor、Online Detector、Offline Explorer、ADR-Bench，强调沙箱红队样本反哺线上检测；开源部分覆盖发现/传感/基准/检测，Prevention等不完全在开源范围，适合做方法论和测评参照。
* **微软栈身份治理**：Entra Agent ID给Agent独立身份，Defender做发现/检测/响应，Purview做数据/DLP，Agent 365/Global Secure Access补注册与影子Agent发现。微软原生环境最顺。

选型时不要问“你是不是AIDR”，要问：发现哪类Agent？关联哪段行为链？在哪个PEP同步阻断？事件回不回SIEM/SOAR？红队用例能不能转成生产规则？

---

## 六、企业落地：先做了这五件事，再谈平台

1. **建统一对象模型**：User、Agent、Agent Version、Model、MCP、Tool、Skill、Memory、DataSource、Credential、Session、Task、Action、Resource。每条事件回答“谁委托谁、以什么权限、对什么资源、做了什么”。影子Agent先确权再决定登记/限权/隔离/下线，别直接等同恶意。
2. **按Agent类型选PEP**：终端编码→终端Sensor+原生Hook；自建→Hook+MCP Gateway+Workload/云；SaaS低代码→平台API+身份治理+审批；高危基础设施→独立身份+短期令牌+工具白名单+沙箱+Kill Switch。
3. **高危动作走确定性控制**：删库、改权限、发邮件外传、转账、发版、建密钥，不靠概率模型单判；用方法级授权、参数校验、双人审批、环境隔离、预算/频率限制、可回滚。
4. **红队结果转生产策略**：在隔离/预生产用真实Agent、身份、工具、数据跑目标劫持、间接注入、工具描述污染、记忆污染、跨Agent委托、慢速外泄。每个用例留“前提—输入—行为链—影响—各PEP结果”，被拦要记依据，被打穿要出修复和回归。Uber ADR的Offline Explorer→Online Detector、Palo Alto/Noma/Lasso/Mindgard的“测试转运行时策略”都这个思路。
5. **维护自己的回归集**：正常多步、间接注入、工具参数注入、权限越界、凭证泄露、记忆跨会话、A2A委托、低频外泄、重复执行/资源耗尽。不只看检测率，还看误阻断、P95/P99延迟、降级、覆盖缺口、处置耗时。

---

## 七、一句给CISO的判据

AI Gateway解决“模型流量可控”，AI-SPM解决“上线前资产与风险”，Guardrail解决“输入输出不越界”，AIDR解决“运行中Agent行为偏离能发现、能关联、能响应”。

真正的企业Agentic安全不是再买一个AI安全产品，而是把发现、身份、Hook、Gateway、终端、SaaS、云审计和红队放进同一套Agent/会话/任务ID体系里。

> 未来审计一个问题不该是“Prompt有没有脏词”，而是：这个Agent是谁、受谁委托、读了什么、调了什么工具、用哪个凭证、改了哪个系统、谁批准、能不能回滚。

---

预览时标签不可点

内容含AI生成图片

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/J8AVIknUyQlKATmLAFibRG7DezjkNIEqbwEYR0fRY4WYibs8SZ8CtNC2NZHEu3nicHJx1rVoe96v4XZDpdRJ2aWbQ/0?wx_fmt=png)

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