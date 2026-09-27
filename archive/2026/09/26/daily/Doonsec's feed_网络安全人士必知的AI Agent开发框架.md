---
title: 网络安全人士必知的AI Agent开发框架
url: https://mp.weixin.qq.com/s/cbkPYeqyUdkfnfrHOiACkA
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:19:55.319217
---

# 网络安全人士必知的AI Agent开发框架

# 网络安全人士必知的AI Agent开发框架

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibTsStdpqrg6RY9Cu7Euq3Q2GpbpkWoGSyUwlrTPecbd6fK2tEmtFEWPddFN6OrleWEaZPkWsI9yUbLLSwKx8GfonoIg03zMf3w/640?wx_fmt=png&from=appmsg)

过去几年，网络安全行业一直在追求自动化。从早期的安全设备堆叠，到后来的安全运营平台，再到SOAR自动化编排，整个行业一直试图解决一个问题：

如何让安全人员用更少的时间，处理更多、更复杂的安全事件。

但过去的自动化，本质上还是“规则驱动”。

安全人员需要提前定义流程：

* 发现什么告警？
* 调用哪个工具？
* 执行什么动作？
* 输出什么结果？

系统只是按照预设逻辑执行。

而随着大模型和Agent技术的发展，安全行业正在迎来一次新的变化。

未来的安全自动化，不再只是固定流程自动执行，而是由具备理解能力、规划能力和工具调用能力的智能体完成复杂任务。

简单来说：

过去是安全人员操作工具。

未来可能是安全人员管理一组安全Agent。

这也是为什么近两年，Agent开发框架开始受到越来越多安全厂商和安全工程师关注。

因为Agent框架，正在成为未来安全产品和安全服务的重要技术底座。

# 一、为什么网络安全行业需要Agent？

很多人第一次接触Agent，会认为它只是“大模型+聊天机器人”。实际上，这是一种比较初级的理解。

真正的Agent，并不是简单回答问题，而是能够围绕目标自主完成任务。

一个完整的Agent系统，就是Model+Harness。

模型负责理解和推理。

Harness架构旨在通过一套系统化的工程方案，将基础大模型的原始智能转化为可靠、可控、可用的智能体能力。优化模型运行的环境、约束、流程、反馈与治理体系来系统性地补救裸模型的不足。主要包含上下文工程、记忆、工具调用、任务拆解、自主编排、状态管理、边界约束、权限管理、安全控制等。

这和传统安全产品最大的区别在于：

传统安全产品通常解决一个具体问题。

例如：

WAF负责Web攻击检测；

EDR负责终端威胁发现；

SIEM负责日志关联分析。

而Agent更像一个安全工程师。

它可以根据任务目标，主动调用不同工具完成工作。

例如：

安全运营人员发现一个异常登录事件。

过去的流程可能是：

查看日志 → 查询IP → 查询威胁情报 → 判断风险 → 创建工单。

而未来，一个SOC Agent可以自动完成：

分析登录行为；

关联用户历史行为；

查询威胁情报；

判断攻击可能性；

生成调查报告；

甚至提出响应建议。

这意味着安全运营模式正在从“工具辅助人”，逐渐走向“Agent协助人”。

# 二、重点关注哪些Agent开发框架？

目前Agent生态正在快速发展，不同框架解决的问题并不完全一样。

对于安全从业者来说，不一定需要成为AI框架开发专家，但需要理解这些框架的能力边界，因为未来很多安全产品都会建立在这些技术之上。

## 1. LangChain：快速构建安全Agent的基础框架

LangChain 是目前应用最广泛的Agent开发框架之一。

它最大的价值，是帮助开发者快速连接大模型、知识库和外部工具。

在安全场景中，一个漏洞分析Agent可能需要完成：

读取漏洞编号；

查询漏洞数据库；

分析漏洞影响范围；

关联企业资产；

生成风险报告。

如果没有Agent框架，开发者需要自己处理大量模型调用、上下文管理和工具接口问题。

而LangChain提供了一套标准化能力。

对于安全厂商来说，它适合快速验证安全Agent原型。

例如：

漏洞分析助手；

安全知识库助手；

威胁情报分析助手；

安全运营问答机器人。

不过，LangChain也存在一些问题。

当Agent任务越来越复杂时，单纯依靠链式调用容易导致流程不可控。

安全场景尤其如此。

因为安全任务不是普通业务流程，任何一个错误判断，都可能带来风险。

因此，企业级安全Agent通常需要更强的流程控制能力。

## 2. LangGraph：更适合企业级安全Agent编排

如果说LangChain解决的是“如何快速搭建Agent”，那么LangGraph解决的是：

“如何让复杂Agent稳定运行。”

LangGraph采用图结构设计。

开发者可以把复杂任务拆解成多个节点。

例如一次自动化渗透测试：

资产发现Agent负责识别目标；

漏洞分析Agent负责判断风险；

验证Agent负责测试漏洞；

报告Agent负责生成结果。

整个过程不是简单的一条链路，而是一个可以控制、暂停、回退和人工介入的工作流。

这对于网络安全非常重要。

因为安全领域最关注的不是“AI能不能做”，而是：

能不能控制；

能不能审计；

能不能追踪；

能不能解释。

未来企业安全Agent，大概率不会完全放任AI自主运行，而是采用：

AI执行 + 人工监督 + 流程控制

这样的模式。

## 3. AutoGen：面向多Agent协作场景

Microsoft 推出的AutoGen，是多Agent协作方向的重要框架。

它的核心理念是：

让多个不同角色的Agent协同完成任务。

这和安全行业天然契合。

因为一次复杂安全事件，本来就需要多个角色参与。

例如：

威胁情报专家负责分析攻击组织；

日志分析专家负责调查入侵路径；

漏洞专家负责判断利用方式；

安全运营专家负责制定响应方案。

未来，一个安全运营团队可能不只是由人组成，也可能由：

安全分析师Agent；

漏洞研究Agent；

威胁猎 hunting Agent；

报告生成Agent；

组成一个数字化安全团队。

## 4. CrewAI：模拟安全团队协作模式

CrewAI采用“角色化Agent”的设计理念。

它更接近现实中的团队协作。

开发者可以定义：

一个负责研究的Agent；

一个负责分析的Agent；

一个负责执行的Agent；

一个负责审核的Agent。

对于安全服务行业，这种模式非常有价值。

未来安全咨询、渗透测试、安全运营服务，都可能通过多个Agent协同，提高交付效率。

## 5. OpenAI Agents SDK：企业应用开发方向

OpenAI 的Agents SDK更加偏向企业应用开发。

它关注：

Agent创建；

工具调用；

Agent之间交接；

运行过程追踪。

对于安全厂商来说，它更适合构建面向客户的安全应用。

例如：

企业安全助手；

安全运营Copilot；

安全知识专家Agent。

## 6. MCP：Agent连接安全世界的重要协议

除了Agent框架，还有一个安全人员必须关注的技术：

MCP（Model Context Protocol）。

如果说Agent是“大脑”，那么MCP就是连接外部世界的接口。

安全Agent需要访问大量系统：

漏洞平台；

资产管理系统；

SIEM；

SOAR；

云平台；

工单系统。

过去，每一个系统都需要单独开发接口。

MCP希望建立统一连接方式。

未来，一个安全Agent可能通过MCP连接企业大量安全数据和工具。

这也是为什么很多人认为：

MCP可能成为Agent时代的重要基础设施。

# 三、未来哪些场景最可能被Agent改变？

从目前行业发展来看，安全Agent最先落地的方向，大概率集中在几个领域。

## 第一，SOC智能化

安全运营中心是最适合Agent发挥价值的场景。

原因很简单：

SOC每天面对大量重复工作。

* 大量告警分析；
* 日志查询；
* 威胁情报关联；
* 事件总结。

这些工作非常消耗人工。

Agent可以帮助安全分析师提高效率。

## 第二，自动化安全测试

过去渗透测试高度依赖专家经验。

未来Agent可能参与：

* 资产发现；
* 漏洞验证；
* 攻击路径分析；
* 测试报告生成。

当然，这并不意味着完全替代安全专家。

因为真正高级的攻击思维、业务理解和风险判断，仍然需要人工参与。

## 第三，安全知识工程

很多企业安全能力不足，并不是没有工具，而是缺少经验。

一个资深安全专家十年的经验，很难复制。

但未来可以通过：

* 知识库；
* 案例库；
* 流程库；
* 安全规范；

训练安全Agent。

让企业安全经验逐渐沉淀。

## 第四，自动化代码审计

随着AI Coding工具快速普及，代码安全正在迎来新的挑战。

过去，代码审计主要依赖安全工程师和人工审计工具。

传统SAST、DAST、IAST工具可以发现：

- SQL注入；

- XSS漏洞；

- 代码规范问题；

- 常见安全缺陷。

但它们往往依赖规则库，对于复杂业务逻辑漏洞、设计缺陷以及新型攻击方式，发现能力有限。

而Agent的出现，让代码审计开始从“漏洞扫描”走向“智能代码分析”。

一个代码审计Agent，可以理解整个项目上下文：

* 代码结构；
* 业务逻辑；
* 依赖组件；
* 接口调用关系；
* 权限模型；
* 历史漏洞案例。

例如，一个开发团队提交了一段涉及用户权限控制的代码。

传统工具可能只提示：

“存在越权风险。”

而代码审计Agent可以进一步分析：

* 这个接口涉及哪些业务对象？
* 当前用户权限是否能够访问其他用户数据？
* 攻击者可能如何构造请求？
* 影响范围是什么？
* 应该如何修复？

这对于企业DevSecOps体系会产生重要影响。

尤其是在AI生成代码大量进入生产环境之后，代码安全问题会进一步放大。

未来企业不仅需要：

“AI帮开发人员写代码。”

更需要：

“AI帮助企业验证代码是否安全。”

因此，代码审计Agent可能成为未来研发安全体系的重要组成部分。

# 四、安全人员应该如何学习Agent？

对于传统安全工程师来说，进入Agent时代，并不意味着必须转型成为算法工程师。

安全人员最大的优势，一直不是写模型，而是理解攻击和防御。

未来更重要的是：

安全能力 + Agent能力。

建议学习路径：

第一阶段：

理解大模型基础。

包括：

Prompt；

RAG；

Function Calling；

MCP

A2A

向量数据库。

第二阶段：

掌握一个Agent框架。

例如：

LangChain；

LangGraph；

AutoGen；

OpenAI Agents SDK。

第三阶段：

结合安全场景实践。

不要只做聊天机器人。

真正有价值的是：

漏洞分析Agent；

威胁情报Agent；

SOC Agent；

安全测试Agent。

# 五、未来安全竞争，本质是Agent能力竞争

过去安全厂商竞争的是：

* 产品数量；
* 检测规则；
* 漏洞库规模；
* 交付能力。

未来竞争可能会发生变化。

真正有价值的安全Agent，需要的不只是模型能力。

更重要的是：

* 安全数据积累；
* 行业知识沉淀；
* 攻击案例经验；
* 业务流程理解。

这也是传统安全公司的机会。

因为安全行业几十年的攻防数据和专家经验，是通用AI公司很难短时间复制的。

未来最有价值的安全能力，可能不是一个新的安全设备，而是一批懂企业、懂攻击、懂防御的安全Agent。

网络安全正在进入一个新的阶段。

过去，我们打造安全工具。

现在，我们正在打造安全智能体。

而对于每一个网络安全从业者来说，理解Agent，不只是学习一项新技术。

更是在提前理解未来十年的安全工作方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/buQYO9JqQcqHibMSbuUlH1q4N0BqiaJT4A81RZWbGMibEU57wlC7W6ryRDOF3vnn8UEfjlTdxeyEovsOzIibw7B11Xp7353IVMKgugHfLB4YWic4/640?from=appmsg)

END

推荐阅读

[中秋送月饼？我用Workbuddy花10分钟搓了个钓鱼网站，第一批"鱼"已经上钩](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493956&idx=1&sn=750176df0821fcd3b8fb0bc4b8a61643&scene=21#wechat_redirect)

2026-09-25

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTsR6J2vvck1VCvUAXBHS7PALBrCMnhffGfic8PGeNib1l4QiarxGZJYGAWAAWSorZUhfqsxUg5gZeLS9icbKgtRASsMruKWBkP9l0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493956&idx=1&sn=750176df0821fcd3b8fb0bc4b8a61643&scene=21#wechat_redirect)

[欢迎网安从业者入群交流！](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493945&idx=1&sn=0911242914a74c2c9a33db36f3e51da8&scene=21#wechat_redirect)

2026-09-25

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibQpXkfgzOb3X3u2XPvF8vXKGNudJBztVTMD0GQpQUekGsakFSkxBr8yrgIgJeKlsf0mb4Ie4nJCa5RlJMZ0ichoeOq7I9mbazzI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493945&idx=1&sn=0911242914a74c2c9a33db36f3e51da8&scene=21#wechat_redirect)

[黑客使用AI Agent窃取60万张信用卡数据](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493938&idx=1&sn=c41fe696d5acf9f10dcb0a86727eb2b2&scene=21#wechat_redirect)

2026-09-24

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibSq0g7bdZXcYcicsDNfH32sLiaVusJ7tQE9Apy4y9L4icwvB19Rib76OTQl5Fib8ucwoUypEGuenl7ibMayx0S1QibIfNKb3U8HFReewA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493938&idx=1&sn=c41fe696d5acf9f10dcb0a86727eb2b2&scene=21#wechat_redirect)

[100小时长征：史上首个Agent自主不间断渗透完整战报](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493933&idx=1&sn=c55f0d54acac7a5ad4c9a0eb78c3fbbc&scene=21#wechat_redirect)

2026-09-23

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibTC4OBY9htvr6zV7p9KmZ0OeKXYnVTT8zbsJq7pylo4NpEBEDF0zTficfQIIjPG5mNs0QTLnk3DgKBHBmwkXFYV9t9BySVJ458U/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493933&idx=1&sn=c55f0d54acac7a5ad4c9a0eb78c3fbbc&scene=21#wechat_redirect)

[特朗普要搞"AI部队"：未来战争，最该护的不是导弹井，是算力](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493928&idx=1&sn=b1114bf14ddf54215d1a290c744213e4&scene=21#wechat_redirect)

2026-09-21

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTE0zUrMonDzlO56Cq5xwFibnj1lY9lT9qyOgUgBLT1r1WiaJcOW2IYyqoez32aqxcm55mBepqv7eiblFx04JyRchl8W5Hmy5BrHg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493928&idx=1&sn=b1114bf14ddf54215d1a290c744213e4&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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