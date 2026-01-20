---
title: 重塑传统自动化漏洞挖掘的Multi-Agent框架攻防一体化实践
url: https://forum.butian.net/share/4719
source: 奇安信攻防社区
date: 2026-01-19
fetch_date: 2026-01-20T03:33:45.608364
---

# 重塑传统自动化漏洞挖掘的Multi-Agent框架攻防一体化实践

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

### 重塑传统自动化漏洞挖掘的Multi-Agent框架攻防一体化实践

* [安全工具](https://forum.butian.net/topic/53)

前段时间在某大厂做安全研究时，针对SDLC的重复性审计工作结合大模型Agent思索了一些可行的思路，便在不断摸索中构建了一个Multi-Agent的协同漏洞挖掘框架系统，目前个人使用来看对于开源的web应用的实战效果相比传统的SAST、DAST以及纯LLM的漏洞挖掘工具来说还是很不错的，便记录此篇框架实现思路和当今Agent赋能漏挖的可行性与优势供师傅们交流指点....

重塑传统自动化漏洞挖掘的Multi-Agent框架攻防一体化实践
================================
前段时间在某大厂做安全研究时，针对SDLC的重复性审计工作结合大模型Agent思索了一些可行的思路，便在不断摸索中构建了一个Multi-Agent的协同漏洞挖掘框架系统，目前个人使用来看对于开源的web应用的实战效果相比传统的SAST、DAST以及纯LLM的漏洞挖掘工具来说还是很不错的，便记录此篇框架实现过程和当今Agent赋能漏挖的可行性与优势供师傅们交流指点....
0x00 传统漏洞挖掘的困局
--------------
当前针对Web应用后端的自动化漏洞挖掘技术主要受困于“覆盖率”与“准确性”难以两全的矛盾：
- 传统的静态分析技术虽能提供全量的代码覆盖，但由于缺乏对程序运行时状态和复杂业务逻辑的语义理解，往往导致海量的误报噪声，极大地增加了安全工程师的审计成本
- 而动态应用程序安全测试虽能在黑盒方面挖掘漏洞更具真实性，却受限于黑盒视角的路径探索能力，难以触及深层业务逻辑，会存在很多漏报
- 目前大语言模型的出现为代码语义分析带来了新的契机，但受限于Context Window 的约束以及生成式模型固有的幻觉问题，直接依赖原生LLM进行大规模代码审计往往导致分析结果碎片化且缺乏可信度，并且直接将代码喂给大模型容易受与漏洞无关代码的影响
0x01 探索漏洞挖掘框架的新出路？
------------------
在探索新的框架实现时，我们可以思考是否能将黑白盒的现有技术互补结合来引导漏洞挖掘？以及我们可以看到几年LLM与Agent相关技术如MCP、RAG的工程化落地，能否用LLM赋于框架更好的语义理解和丰富的上下文能力，再通过Agent做一套自动化流程？
为突破上述技术瓶颈，我在探索新的漏洞挖掘框架时也看了一些目前学术界的相关LLM赋能的研究与github开源的技术实现，总体的探索方法还是在论文与现实实践中思考各个方面的优势与缺陷，最终确定做一个\*\*基于Muti-Agent协同的智能化漏洞挖掘框架\*\*：构建一个从静态分析到动态验证的闭环生态。技术上引入MCP 来作为连接LLM推理能力与静态分析工具的桥梁，利用RAG 技术通过构建高质量漏洞专家知识库来校准模型判定，深度缓解LLM的“幻觉”与知识盲区；同时，结合运行时自动化的流量Fuzz模糊测试技术，将白盒的逻辑推演与黑盒的攻击验证深度融合，减少漏洞的误报和漏报。
这里放一个当时挖到的有CNVD证书的水洞，通过项目上传与聊天，自动化分析审计出多处SQL注入漏洞，并且能够给出攻击POC，以及后续完整的修复方案
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-010db0700cef3b1c4e0e0ac4a07adb932b45c6cd.png)
0x02 框架核心：打破黑白盒壁垒
-----------------
该框架核心架构旨在重构传统安全检测的边界，提出了一种 “白盒语义指引黑盒，黑盒动态验证白盒”的深度融合范式。框架并非单一工具的线性叠加，而是一个基于Multi-Agent编排（Agent Orchestration）的异构系统。
- \*\*白盒分析维度\*\*：框架引入了MCP作为智能体的执行接口，驱动底层的静态分析工具与正则匹配引擎，对代码AST进行初步扫描，快速锚定潜在的危险函数调用Sink。为解决静态分析中常见的上下文缺失问题，进一步融合了RAG 技术：通过引入高质量的博客记录的高精度漏洞知识库，系统能够为大语言模型提供特定漏洞类型的\*\*完备的Context上下文\*\*与判定依据，从而在保持高代码覆盖率的同时，抑制传统模式匹配带来的误报，实现了从“语法”到“语义”的代码的全面理解提升。
- \*\*黑盒验证维度\*\*：框架构建了运行时的自动化\*\*Fuzz模糊测试\*\*。该模块独立承担着对Web通用漏洞（如XSS、SQL注入）及敏感信息泄露的覆盖任务。当白盒Agent发现疑似逻辑漏洞时，通过黑盒上的Fuzz可在流量侧生成针对性的变异Payload进行动态优化，通过分析HTTP响应状态来实证漏洞的可利用性。
我认为将静态视角的逻辑推演与动态视角的攻击验证相结合的机制，能极大地提升了漏洞检测的置信度，实现了真正意义上的全链路攻防评估，刚开始时候画的大致架构草图，仅贴示了主要功能，一些细节实现并未展示：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-3dd8d7144395335cfcfd9ef5b5fdcdbf4bc9c341.png)
0x03 智能化Agent设计细节
-----------------
### 1. \*\*Static Orchestration Agent\*\*：基于MCP协议的异构工具编排
在传统的LLM应用中，模型往往被禁锢在文本交互的孤岛中，难以触及本地庞大的代码仓库，且面临着Context Window对海量代码理解的限制。本框架设计的\*\*漏洞定位Agent\*\*，本质上是一个 \*\*静态分析增强型智能体(Static Orchestration Agen)\*\* ，通过引入MCP与构建Prompt定义角色任务将LLM从被动的文本生成者转变为主动的工具使用者，通过静态分析获取代码结构中的丰富语义上下文
#### MCP驱动的“深层感知”
不同于简单的API调用，MCP协议使得Agent能够理解工具的输入输出Schema，实现复杂的推理链条：
- \*\*工具与模型的语义对齐\*\*：通过定义标准化的MCP接口，将底层的静态代码分析工具封装为LLM可调用的能力。
- \*\*意图驱动的执行\*\*：构造合适的CoT思维链Prompt让Agent根据当前的分析任务代码（例如“寻找未授权访问漏洞”），自主决策调用何种工具、传入何种参数。这可以让Agent模拟安全专家的思维过程，主动去探测代码中的漏洞点。
#### SINK点定位与攻击面收敛
针对LLM处理大规模代码时的“大海捞针”难题，高效定位漏洞利用链
- \*\*SINK点精准锚定\*\*：Agent并不直接阅读全量代码，而是利用MCP驱动底层扫描器，基于AST解析和高精度的正则模式，快速提取代码中的\*\*SINK点\*\*（需要根据不同语言类型的不同漏洞进行扩充分类）
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-c0eb5562551621505ab399c7b24ceb1443dfc0d1.png)
- \*\*代码切片与上下文聚焦\*\*：一旦定位到SINK点，系统会通过静态分析工具获取sink点污染的上下文Code Slice，并且做到变量语句级，将无关语句统统移除(这里详细的实现师傅们可以去阅读Joern等工具的源码和他的论文，主要在于CPG代码属性图的构建和后向切片等算法技术)。极大地收敛了分析范围，过滤大量无关业务代码，确保输送给LLM进行深度研判的每一行代码都具有潜在的安全价值（无论是控制流还是数据依赖流都对漏洞的存在有潜在的约束和影响）。这不仅大幅降低了Token消耗，更显著提升了后续漏洞验证的准确性。
### 2. \*\*Contextual Reasoning Agent\*\*：基于RAG的领域知识增强与检索优化
作为本框架保障检测精度的核心组件，校验 Contextual Reasoning Agent承担着“校验”的角色。针对通用大语言模型在特定安全领域存在的\*\*专业知识匮乏\*\*与\*\*逻辑幻觉\*\* 问题，本模块引入RAG 技术，人为构建了一个可随时扩展的领域专家知识文档库，通过实时注入精确的先验知识来约束和校准模型的推理过程。
#### RAG知识库的结构化重构与向量化
为了让非结构化的安全知识能够被机器高效理解，摒弃粗暴的文本截断，采用基于Markdown语法树的\*\*结构化清洗策略\*\*。系统依据标题层级对海量的漏洞PoC、修复方案及原理分析文档进行逻辑切分，确保每个Chunk都包含完整的语义单元
例如一个简易的MARKDOWN文档：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-0871baf539cecf0d3fb5b24fcc67236bd3298cd9.png)
#### 动态滑窗与重叠分块策略
在知识切片过程中，为了规避硬切分导致的\*\*语义断层\*\*，切片策略采用\*\*基于重叠策略（Overlapping Strategy）的动态滑窗机制\*\*：
- \*\*语义连贯性保障\*\*：设定固定的Token阈值作为基础窗口大小，同时引入预设比例的重叠缓冲区。每一分块的末尾段落会被完整保留并作为下一分块的起始上下文。
- \*\*边界信息无损传输\*\*：这种机制确保了跨越分块边界的逻辑描述（如一段跨越多行的代码逻辑或长难句的漏洞解释）不会被割裂，保证了向量检索时上下文信息的完整性与连贯性。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-35db206ea217c058fa2e21296c6ab119475cf265.png)
#### 向量检索与推理运行
采用all-MiniLM-L6-v2模型作为Embedding引擎。该模型在保持低延迟推理的同时，在多语言的语义相似度任务上有更好的泛化能力;数据库采用集成Qdrant向量数据库，支撑大规模向量的高并发检索
- \*\*上下文感知的推理校准\*\*：当定位Agent上报疑似SINK点时，校验Agent会提取当前代码特征，在向量库中实时检索最相似的Top-K个历史漏洞模式和修复示例。这些检索结果被作为增强上下文 注入到LLM的Prompt中，迫使模型基于检索到的“事实依据”而非单纯的概率预测进行最终判定，减少了误报的产生
0x04 动态流量FUZZ
-------------
我从以往的安全研究触发，针对通用型漏洞的工具做了大量的调研，并基于BurpSuite原生API开发了自动化Fuzz工具如：反射性和存储型XSS、SSRF、CORS、敏感信息泄露等（同时也是在锻炼开发能力，也让日常重复性漏洞渗透工作能够做的更高效），再结合MCP集成给Agent。该模块并非简单的随机测试，而是作为一个流式检测组件，实时拦截、解析并重放业务流量，对潜在漏洞动态扫描。而对于敏感信息泄露则是比较容易 ，针对Spring Boot Actuator、Swagger UI、Druid Monitor等常见中间件的指纹来做识别。同时，结合模式匹配，对响应包中的JWT Token、阿里云AK/SK、AWS凭证等高熵字符串进行实时监测，有效发现硬编码或调试信息泄露。
下面挑了几个通用型漏洞的Fuzz来做简单做下原理解释
### 1. 通用XSS漏洞的自动化Fuzz
比如针对XSS反射型和存储型漏洞，开发时采用了全量参数解析+动态污点标记的检测策略，确保对异构http包结构中参数的全面覆盖。
- \*\*深度参数提取与结构化解析\*\*：
不仅仅局限于URL Query参数，还有针对JSON、XML、Multipart-form等多种数据格式的解析器。能够递归遍历HTTP Request Body中的每一层嵌套结构，提取所有用户可控的叶子节点作为Fuzz入口。
- \*\*唯一性污点标记\*\*：
为了解决并发扫描时的结果混淆问题，引擎摒弃了静态Payload，转而采用动态生成的\*\*唯一性测试标记\*\*。
- \*\*Payload构造\*\*：Timestamp + RandomStr + Vector（例如：CurrentTime等高熵字符串）
- \*\*状态映射表\*\*：内存中维护一张高并发的HashMap，记录RequestID &lt;-&gt; ParameterName &lt;-&gt; UniquePayload的映射关系。
- \*\*响应回显与验证\*\*：
发送测试请求后，引擎自动捕获HTTP Response，通过高效的字符串匹配算法检索之前的唯一标记。一旦检测到标记回显且上下文未经过滤（如HTML实体编码缺失），即判定存在可疑XSS漏洞，并自动关联原始请求数据生成漏洞条目。
（当时研究设计思路时绘制的草图）
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-e9d1113b7a450857fdbde0b6d110f319d88fa8c8.png)
### 2. 访问控制与配置缺陷的CORS漏洞检测
自动化Fuzz HTTP请求头中的Origin字段，构造包括恶意第三方域名、特殊字符（如null）及子域名在内的多种变异Payload
- \*\*高危利用判定\*\*：当响应头Access-Control-Allow-Origin和攻击者Payload一样或为小写null，且同时存在Access-Control-Allow-Credentials: true时，将其标记为高危漏洞。此类配置允许攻击者绕过同源策略（SOP）窃取用户敏感数据
- \*\*严格语法校验\*\*：针对协议规范的边缘场景进行校验，例如检测到Access-Control-Allow-Origin: Null（大写）时，引擎会自动识别其为无效配置（浏览器不识别大写Null），从而将其作为无效处理
以及服务端错误配置导致Access-Control-Allow-Origin始终和Origin一样，这里放一张示例图便于理解：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-fdd5d429734662d993d7c57dcbba36b261a75d8d.png)
0x05 构建认知型安全智能体的未来图景
--------------------
在对Multi-Agent探索自动化漏洞挖掘实践的探索过程中，其实我们一直在试图回答一个核心问题：如何在安全攻防领域，构建一个具备“感知-推理-决策-行动”完整闭环的智能系统。目前的Agent主要还停留在“检测与验证”阶段，之后更完备的阶段是自动化\*\*环境的感知探索与白盒源码的结合\*\*，以及能够基于当前的Shell环境或数据库权限，自主规划后续的横向移动与权限提升路径。另一个重要的方面是\*\*自适应Payload生成\*\*：比如利用强化学习反馈机制，让Agent在面对WAF拦截时，能够动态调整Payload的混淆策略，实现智能化的WAF绕过
希望本文的实践能为各位师傅提供一种新的视角供师傅们交流指点～

* 发表于 2026-01-19 10:00:01
* 阅读 ( 518 )
* 分类：[AI 人工智能](https://forum.butian.net/community/AI)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Bear001](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b803fb899b4c2f8e207d6cf1872b0d60bc290b5.jpg)](https://forum.butian.net/people/33847)

[Bear001](https://forum.butian.net/people/33847)

Web安全

8 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2026 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请...