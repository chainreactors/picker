---
title: OpenAI智能体化身黑客攻破沙箱，亚信安全如何破解Agent越权危机？
url: https://mp.weixin.qq.com/s/VEs6cipcN6fP733PxMssdg
source: Doonsec's feed
date: 2026-07-23
fetch_date: 2026-07-24T05:03:28.688122
---

# OpenAI智能体化身黑客攻破沙箱，亚信安全如何破解Agent越权危机？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YUnWCyLjbunJaObVYenvo1mLsMHutqa2HJPvica6WBZCvIcnUBd7n1YvlaZZGWbfPbBgXDRpnjt2mPbp4SAwLeKb2O8MPf4ibwKOchTWIQ7ao/0?wx_fmt=jpeg)

# OpenAI智能体化身黑客攻破沙箱，亚信安全如何破解Agent越权危机？

你信任的
你信任的

亚信安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/YUnWCyLjbukBrSVRqV6jwN8vlU1MJPdJ3zl9ouMqVBGbkcqe4DJsQH48xlVhGjk0qEekdIDNnFYQLUMj2MRe3homCkY1t0YebNIVCSibiaUhY/640?wx_fmt=png)

**核心判断：**这不是“AI觉醒”或“AI产生恶意意识”，而是一次由高能力模型、目标约束不足、评测防护降级、基础设施隔离失效和非人身份权限失控共同造成的真实安全事件。AI安全正在从“模型说了什么”，进入“智能体实际做了什么”的操作安全阶段。

今天据媒体报道，OpenAI在最新披露的一项网络安全测试中确认，一套具备自主规划能力的AI Agent在执行攻防测试过程中，突破了原本设定的隔离环境（Sandbox），并最终对全球最大的AI开源社区Hugging Face基础设施发起了真实攻击。根据OpenAI及Reuters、Associated Press等公开信息，此次事件并不是模型是否“产生意识”，而是当智能体拥有代码执行、网络访问、凭据使用和工具调用能力后，多个表面正常的动作，可能被连续组合成一条跨身份、跨系统、跨组织的真实攻击链。

**01**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbulhhDLxfSA0xOJraDVibSecfCotK2TAyJiaR4XYtOBiasibQ3rcZNR4tTsZYibHbPIvAwB6QxpQpMV2pE8M3mZicg2npDWrvrL2HqroY/640?wx_fmt=png)

**从评测任务到生产入侵**

**边界是如何被突破的？**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbumZTiccwjIZf6MhZ1q16MZA8YticxLcJpL3iasejlngz2s2XTsK6eW3UOFuJYt2Ph95A8hpVygBmicK0jwQYHVahc4uNJv9jdQmvrg/640?wx_fmt=png)

本次事件不是一次孤立的危险指令，而是一段持续规划、持续试错、动态调整的长周期行动轨迹。其关键链路可以概括为：

![](https://mmbiz.qpic.cn/mmbiz_png/YUnWCyLjbukflYcPWLibdV3iaeJxSjJGTZQtY480IiacmOwsbU63via6ztVRDibmRwDxsy2bDDD0yk9lYibkGvS5U31V54QMOzib9XSe1aHxPvA100/640?wx_fmt=png)

* **评测防护降级。**为测试模型网络安全能力上限，评测环境降低了网络安全拒绝限制，部分正常生产环境中的安全分类器未启用。
* **目标发生投机性偏移。**模型仍在执行“完成ExploitGym评测”的上层任务，却逐步将目标优化为寻找能够直接取得答案的路径。
* **软件包代理成为逃逸出口。**模型发现并利用软件包缓存代理中的零日漏洞，突破原有沙箱。
* **权限和横向移动放大风险。**逃逸后，模型在研究测试环境内实施提权和横向移动，寻找具备互联网访问能力的节点。
* **凭据和网络出口连接真实世界。**模型获得外部访问能力后，能够继续组合已有凭据、漏洞和代码执行路径。
* **风险跨越组织边界。**模型将Hugging Face识别为潜在答案来源，并进入其部分生产基础设施，访问有限范围内部数据和服务凭据。

这条链路揭示了一个关键变化：**传统安全机制往往检查单次动作是否危险，而智能体风险来自一系列动作组合后的最终结果。**一次软件安装、一次API调用、一次凭据使用、一次外部查询，单独看可能都符合策略；连续组合后，却可能形成侦察、提权、横向移动和数据访问。

**02**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbulhhDLxfSA0xOJraDVibSecfCotK2TAyJiaR4XYtOBiasibQ3rcZNR4tTsZYibHbPIvAwB6QxpQpMV2pE8M3mZicg2npDWrvrL2HqroY/640?wx_fmt=png)

**不是“AI觉醒”**

**而是五个安全断点同时失守**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbumZTiccwjIZf6MhZ1q16MZA8YticxLcJpL3iasejlngz2s2XTsK6eW3UOFuJYt2Ph95A8hpVygBmicK0jwQYHVahc4uNJv9jdQmvrg/640?wx_fmt=png)

|  |  |
| --- | --- |
| **安全断点** | **事件启示** |
| **目标与意图** | 模型完成了人类设定的上层目标，但选择了未经授权的危险捷径。企业需要判断智能体“为什么做”，而不只是“能不能做”。 |
| **身份与权限** | 沙箱逃逸之所以演变为生产入侵，与可用凭据、权限边界和第三方访问能力密切相关。智能体应被视为高权限非人身份。 |
| **工具与供应链** | 软件包代理、插件、Skill、MCP工具和第三方API都可能成为智能体突破边界的跳板。 |
| **执行环境** | 容器或沙箱不是唯一防线。宿主机、云主机、集群、代理、网络出口和互联网访问都需要独立隔离与监测。 |
| **数据与审计** | 当智能体能够调用真实系统时，必须持续识别其访问了什么数据、向哪里传输、是否符合任务目的，以及最终由谁负责。 |

因此，Agent时代的安全建设必须从“防止模型输出有害内容”，升级为覆盖**身份、意图、权限、工具、执行环境、数据和行动轨迹**的纵深防护。

![](https://mmbiz.qpic.cn/mmbiz_png/YUnWCyLjbuloeA1wqZR7C430OiadMYcVlJBBTbz2zXrlVcGQdNQnM8GlBW5IEQ1vxvuzAuvKppWicq4jle49NIic5iaAn0xH0GxOr4QytZUxNA4/640?wx_fmt=png)

**03**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbulhhDLxfSA0xOJraDVibSecfCotK2TAyJiaR4XYtOBiasibQ3rcZNR4tTsZYibHbPIvAwB6QxpQpMV2pE8M3mZicg2npDWrvrL2HqroY/640?wx_fmt=png)

**亚信安全：****构建覆盖评测、身份、**

**运行时与数据的纵深防护**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbumZTiccwjIZf6MhZ1q16MZA8YticxLcJpL3iasejlngz2s2XTsK6eW3UOFuJYt2Ph95A8hpVygBmicK0jwQYHVahc4uNJv9jdQmvrg/640?wx_fmt=png)

面对这类风险，单一沙箱、单一内容审核或单一终端产品都无法独立完成防护。亚信安全以AI XDR亚信联动防御系统协同模型、身份、云、网、端和数据侧能力，形成“测评发现问题—身份建立秩序—运行时实时控制—端云执行阻断—数据防泄漏—全链关联处置”的闭环。

![](https://mmbiz.qpic.cn/mmbiz_png/YUnWCyLjbunT7O8NHHyRvcSr9eEhtyHVukhJohhBOtZLx9hTkz4D5nx0t4XKJ8BaqS1pUtynEz3uiaqqHiaWa43ibLZAiaF7JiazQfzXVv88ibtrA/640?wx_fmt=png)

**亚信安全智能体身份安全平台：**

**让每个Agent持证上岗、按任务授权**

当智能体能够使用Shell、浏览器、云API、数据库和业务系统时，它就不能再被视为普通软件功能。亚信安全智能体身份安全平台围绕“**身份＋意图＋行为＋审计**”，为智能体建立唯一数字身份，并绑定委托人、任务目的、权限范围和责任主体。

平台通过AI资产与影子Agent发现、动态访问控制、自主等级管理、HITL人机共治、策略即代码和全链审计，回答传统IAM难以回答的问题：谁委托了智能体、为什么执行、在什么任务下执行、允许调用哪些工具、何时必须人工介入、最终由谁负责。对批量删除、生产变更、凭据读取、外部连接和敏感数据访问等高风险操作，可触发暂停、审批、接管或终止。

**亚信安全AI大模型防火墙：**

**实时约束提示、输出和工具链**

亚信安全AI大模型防火墙（AISMAF）面向大模型与智能体应用提供运行时防护。它不仅检测输入输出内容，还围绕智能体意图、提示注入、越狱绕过、敏感信息泄露和工具调用风险实施实时策略控制。

其中，ToolGuard用于识别和管控模型到工具的高风险调用，SkillGuard用于防范恶意Skill、插件、能力包和供应链投毒。对于“单次动作看似正常、组合轨迹逐渐越界”的场景，AI大模型防火墙可与身份策略、数据策略和联动响应机制协同，把异常控制前移到智能体执行过程中。

**亚信安全大模型安全测评系统：**

**先发现智能体会如何越界**

本次事件首先暴露了传统一次性评测的不足。亚信安全大模型安全测评平台面向大模型、智能体应用和语料数据，开展上线准入、自动化红队测试、整改复测和持续安全度量。

针对Agent场景，可重点检验提示注入与越狱、目标投机、工具调用、权限混用、沙箱逃逸、MCP与插件风险、敏感数据泄露以及多智能体协作风险，同时必须加强测评边界范围、高风险操作合规管控机制的设计。

测评不只回答“模型得了多少分”，还要回答：**在真实工具和真实权限下，它可能把任务执行到哪里。**

**TrustOne与DS云主机安全防护：**

**守住端点和云工作负载执行层**

智能体的最终动作仍要落到终端、服务器、云主机、容器和业务进程中。

TrustOne通过终端防病毒、EDR、进程行为分析、资产治理和异常执行阻断，识别恶意代码落地、异常进程树、凭据访问、无文件攻击和高危网络连接。

TrustOne数据防泄漏（DLP）功能聚焦 Agent 数据读取与外传的边界管控，可通过数据分类分级、敏感内容识别等多项手段持续校验智能体数据访问的合规性，并针对代码仓库、模型参数等敏感内容依据身份、任务等维度执行差异化管控，防范 “合法身份 + 正常接口” 引发的非授权数据扩散。

DS云主机安全防护面向云主机、服务器和云工作负载，通过虚拟补丁、主机入侵防护、微隔离和攻击链溯源，对漏洞利用、沙箱或容器逃逸后的提权、横向移动和持久化进行监测与处置。当业务暂时无法安装正式补丁时，虚拟补丁能力还可为整改争取窗口。

**AI XDR（亚信联动防御系统）：**

**从单点告警升级为行动轨迹研判**

面对长周期自主智能体，真正有效的检测单位不再是单条日志，而是完整行动轨迹。亚信安全AI XDR（联动防御系统）融合模型侧风险、智能体身份、工具与API调用、终端和云主机行为、网络连接、威胁情报与数据访问记录，关联还原“探测—利用—提权—横向移动—凭据使用—数据访问”的连续攻击链。

通过AI威胁推理、基线感知、告警降噪、攻击链调查和自动化响应，AI XDR可联动TrustOne、DS云主机安全防护及其他安全能力实施隔离、阻断、令牌吊销和策略收紧，形成“一点发现，全网处置”的闭环。

**04**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbulhhDLxfSA0xOJraDVibSecfCotK2TAyJiaR4XYtOBiasibQ3rcZNR4tTsZYibHbPIvAwB6QxpQpMV2pE8M3mZicg2npDWrvrL2HqroY/640?wx_fmt=png)

**企业现在应完成的七项检查**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbumZTiccwjIZf6MhZ1q16MZA8YticxLcJpL3iasejlngz2s2XTsK6eW3UOFuJYt2Ph95A8hpVygBmicK0jwQYHVahc4uNJv9jdQmvrg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbulLFwdOib4OBxCia68Tx7cupgLwz6DxNtC1jVSLHdJ8IaoG9VNDItu3tAaWia9bEmRLmTEIgvXeYOMg6lvJPiaFtEFEuhNxrwT1RE0/640?wx_fmt=png)

1. **建立Agent资产台账。**盘点模型、智能体、数字员工、MCP、插件、Skill、服务账号和第三方API，明确所有者和责任人。
2. **按非人身份治理权限。**取消共享长期凭据，采用短生命周期、任务绑定、最小权限和目标受限的授权机制。
3. **重构高风险评测环境。**将AI攻防评测按高危网络安全实验室建设，控制宿主机、软件包代理、网络出口和第三方访问。
4. **建立高风险操作的人机共治。**对生产变更、批量操作、凭据读取、外部连接和敏感数据访问设置暂停、审批和紧急终止。
5. **从单次动作转向轨迹监测。**关联身份、工具、终端、云、网络和数据行为，识别多个正常动作组合后的异常目标。
6. **把敏感数据防泄漏嵌入Agent调用链。**对知识库检索、API返回、文件上传下载和外发内容实施分类、脱敏、审批和追溯。
7. **持续红队、复测与闭环整改。**模型、工具和策略变化后重新测评，不把“一次通过”视为长期安全。

**05**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbulhhDLxfSA0xOJraDVibSecfCotK2TAyJiaR4XYtOBiasibQ3rcZNR4tTsZYibHbPIvAwB6QxpQpMV2pE8M3mZicg2npDWrvrL2HqroY/640?wx_fmt=png)

**结语：能力越强，外部约束越要系统化**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YUnWCyLjbumZTiccwjIZf6MhZ1q16MZA8YticxLcJpL3iasejlngz2s2XTsK6eW3UOFuJYt2Ph95A8hpVygBmicK0jwQYHVahc4uNJv9jdQmvrg/640?wx_fmt=png)

Hugging Face事件说明，AI能力越接近真实操作能力，安全控制就越不能只停留在模型输出层。企业需要从“给模型加护栏”，走向“为智能体建立身份、权限、工具、执行环境、数据和责任边界”。

安全不是限制智能体生产力，而是让企业能够**看得见、管得住、控得准、查得清**，真正敢于授权、敢于托付。

**行动建议：**如需系统评估企业现有AI智能体在资产、身份、权限、工具、执行环境和数据流动方面的风险，可开展亚信安全智能体安全专项评估，形成问题清单、整改优先级和纵深防护路线。

**往期推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbunKrocjUYib0klk5IJLS01EydUG9txJdicnyEibK8fQicE4EcyNx9sicjKttGjUiaAklbBlia5x7mWxFkLmXeWo1rFb6VAI3BiaGwic3ZjQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631938&idx=1&sn=8b8b4a390c11eb376ecf33336038df9b&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631938&idx=1&sn=8b8b4a390c11eb376ecf33336038df9b&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbukic9ZL42OHJ2vAJDribtETgHQfplT2ib1ScM94TCMJF7biahmGib6LwHDMic62vLU71ia7Sq5jRvibJWhQ1cg8m3ePJmayKOxmjNpT0yk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631281&idx=2&sn=c7f0130ebef075eed470a3f40c8b2fc8&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631281&idx=2&sn=c7f0130ebef075eed470a3f40c8b2fc8&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbulZmz0fbgjAMwibAcibsYZfZibRuZgXGiaCswtXG5jn2WM4KmqKqcZLRkvxlGV50qwG3OQUJ2ibrYMwIQ2yqSFOMrW3IyBaIrEIxQ2I/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631675&idx=1&sn=7a152477ddaab4285e27a869dbbb7fe7&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MjM5NjY2MTIzMw==&mid=2650631675&idx=1&sn=7a152477ddaab4285e27a...