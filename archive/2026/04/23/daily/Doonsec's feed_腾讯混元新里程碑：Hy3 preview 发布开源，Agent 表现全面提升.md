---
title: 腾讯混元新里程碑：Hy3 preview 发布开源，Agent 表现全面提升
url: https://mp.weixin.qq.com/s/fUIC9BQCBeI4VMWcS03_pw
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:53:45.059121
---

# 腾讯混元新里程碑：Hy3 preview 发布开源，Agent 表现全面提升

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz9061nJTiccrSCRScYlGBBKbDu1tYE7bzC55RbtYPUvw16hxAjEhrFfqLaLwrdyem060EyNCZn8Isqq4iaJLE2ib203w3gVR1DIQfkg/0?wx_fmt=jpeg)

# 腾讯混元新里程碑：Hy3 preview 发布开源，Agent 表现全面提升

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

**4 月 23 日，**腾讯混元 Hy3 preview 语言模型发布并开源。这是一个快慢思考融合的混合专家模型，总参数 295B，激活参数 21B，最大支持 256K 上下文长度。这是混元重建后训练的第一个模型，也是混元迄今最智能的模型，在复杂推理、指令遵循、上下文学习、代码、智能体等能力及推理性能上实现了大幅的提升。

2026 年2月，腾讯混元重建了预训练和强化学习的基础设施，以及模型追求实用性的三个原则：

1、能力体系化：不推崇“偏科”，因为即使是代码智能体的单一应用，也涉及推理、长文、指令、对话、代码、工具等多种能力的深度协同。

2、评测真实性：主动跳出易被“刷榜”的公开榜单，通过自建题目、最新考试、人工评测、产品众测等多种方式评估和改进模型的“真实战斗力”。

3、性价比追求：实用性离不开商业合理性，深度协同模型架构和推理框架的设计，大幅降低任务成本，让智能用得起、用得好。

Hy3 preview可以视为混元快速探索实用性大模型、解决真实世界问题的一个开端。

腾讯首席AI科学家姚顺雨表示，Hy3 preview是混元大模型重建的第一步。我们希望通过这次开源和发布，获得来自开源社区和用户的真实反馈，帮助我们提升 Hy3 正式版的实用性。与此同时，我们也在继续扩大预训练和强化学习的规模，提升模型的智能上限，并通过与腾讯众多产品的深度Co-Design，持续提升模型在真实场景中的综合表现，并开始探索特色模型能力。

目前，Hy3 preview 已在腾讯云、元宝、ima、CodeBuddy、WorkBuddy、QQ、QQ浏览器、腾讯文档、腾讯乐享等首发上线，微信公众号、和平精英、腾讯新闻、腾讯自选股、腾讯客服、微信读书等多个主线产品也在陆续上线。另外，Hy3 preview 支持接入流行的开源智能体产品，如 OpenClaw、OpenCode、KiloCode 等，并已上架腾讯云大模型服务平台 TokenHub。

### **Hy3 preview主打全面实用性，Agent能力大幅提升**

多个测评结果显示，Hy3 preview 模型能力全面提升。

**1、出色的****上下文****学习和指令遵循能力**

在各种真实的生产与生活场景，理解杂乱冗长的上下文并遵从复杂多变的规则是模型的首要挑战。基于腾讯业务场景的灵感，腾讯混元提出了 CL-bench和 CL-bench-Life 来创新性地评估模型的上下文学习能力，并在 Hy3 preview 显著地提升了模型上下文学习和指令遵循能力。

**2、****复杂推理能力****突出，清华数学博士资格考试国内分数最高**

复杂推理能力是模型解决各种问题的基础。Hy3 preview 在 FrontierScience-Olympiad、IMOAnswerBench 等高难度理工科推理任务中表现突出，并在最新的清华大学求真书院数学博资考(26春)  和 全国中学生生物学联赛(CHSBO 2025) 中取得优异成绩，展现了可泛化的强推理能力。

**3、代码与智能体提升最为显著，****展现出****高性价比**

代码和智能体是Hy3 preview 提升最为显著的方向。得益于预训练及强化学习框架的重建和强化学习任务规模的提升，腾讯混元以较快的速度在 SWE-Bench Verified、Terminal-Bench 2.0 等主流代码智能体基准以及 BrowseComp、WideSearch 等主流搜索智能体基准中取得了有竞争力的结果。

在数字世界中，代码关注的是模型在开发环境中的执行能力，搜索则聚焦于开放信息空间中的检索、筛选与整合能力，两者共同决定了模型在复杂智能体场景（例如OpenClaw）中是否真正具备可用性。Hy3 preview 在 ClawEval 和WildClawBench 等评测中表现突出，表明我们的智能体能力正在稳步走向全面与实用。

除了公开榜单，腾讯混元还进一步构建了多个内部的评测集，对模型在真实开发场景中的表现进行评估。结果表明，无论是在后端工程任务集Hy-Backend，贴近真实用户开发交互的 Hy-Vibe Bench，还是高难度软件工程开发任务集Hy-SWE Max 上，Hy3 preview 均体现出了强竞争力。

比较各个开源模型的大小与智能体综合表现，Hy3 preview 展现出高性价比。

### **腾讯核心业务已全面接入，多主线AI 产品验证收益明显**

正式上线之前，Hy3 preview在腾讯主要AI 业务进行了产品测试，获得明显正收益。

在元宝端，混元与元宝进行了深度Co-Design。一方面，针对性地提升了模型在意图理解精准度、文本创作质量、深度搜索等硬核指标上的表现；另一方面，对文风、文笔、情商、内容组织和内容专业度上进行了精细化调优。模型与产品的深度协同，为用户带来了更智能且更具“活人感”的交互体验。

在ima知识库问答和通用问答两个场景下，测试结果显示，Hy3 preview 处理长文的能力出色，特别是检索类任务，在回答信息的准确性、覆盖度和全面性上表现较好。

在CodeBuddy、WorkBuddy产品上，Hy3 preview 首 token 延迟降低 54%、端到端时长降低 47%、成功率提升至 99.99%+。实际用户环境中，Hy3 preview 已稳定驱动最长 495 步的复杂 Agent 工作流，覆盖文档处理、数据分析、知识检索、MCP 工具链编排等多样化办公场景。

在公众号AI分身和 AI 客服的场景专项评测中，Hy3 preview 展现出相比 Hy2 更全面的能力升级。新模型在用户意图理解、复杂上下文承接和知识信息组织方面表现更成熟，面对模糊提问、短句追问和多轮对话时，能够更准确地把握用户诉求，并输出更清晰、更稳定的回复。结合知识库、用户记忆与上下文生成回答时更贴合AI 分身和 AI 客服的角色，过度脑补、主观代入和情绪化表达显著减少，使整体交互体验更贴近“可信、自然、高效”的回复目标。

在和平精英 AI NPC 场景评测中，和平精英团队第一时间在Hy3 preview上线后基于 AI NPC 场景中完成接入并开展评测，整体表现令人印象深刻。在游戏局外的人设扮演场景中，Hy3 Preview 不仅能够精准理解角色设定，还能针对开放性问题输出高度关联、富有增量价值的内容，带来了更加真实、自然、沉浸的对话体验。而在游戏局内的复杂对战场景中，模型回复节奏贴近真实玩家聊天体验，展现出优秀的稳定性与出色的拟人化扮演能力，整体效果表现亮眼。

在腾讯文档AI PPT 场景，较上一版本（Hy2）取得了显著进步：生成成功率提升 20%，评测得分提升 10%，同时生成耗时缩短 20%。整体而言，新模型在评测场景中表现优异，在模版选择，色彩匹配，生成大纲，补充内容多个阶段，均体现出优秀的表现，无幻觉，契合主题，视觉效果好。

在QQ AI助手小Q产品评测中，较上一版本，在长文本首字节时延、整体响应速度与流式输出效率方面显著优化；核心能力上，数学推理表现提升尤为明显，多场景指令遵循与泛化能力进一步增强；在工具调用推理及多轮指代消解方面表现更稳定高效，在OpenClaw官方PinchBench QQ智能体场景测试中取得突出效果，综合体验实现明显跃升。

### **推理效率提升40%，同等成本智能密度最优**

得益于模型和推理框架上的深度协同，以及在推理框架、算子性能、量化算法等全方面优化，整体推理效率提升40%，Hy3 preview的成本相比上一代模型大幅下降。

在腾讯云大模型服务平台 TokenHub 上，Hy3 preview 输入价格最低1.2元/百万tokens，输入命中缓存价格0.4元/百万tokens，输出价格最低4元/百万tokens。同时，腾讯云联合混元推出定制的 Hy3 preview Token Plan 套餐，个人版定价最低28元/月，为Agent开发和打造“龙虾”应用的提供更具性价比选择。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYjZ7Hx6Udjjk2BGLzC9ahJq7ibxDd1RGA0c9NYZc1husEsvb3tY4FcWPQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj5q5PQEOc5ibURPb03vnRibrxC3UR8xzdyATfiawTYRV2vJvBnAIcE1FeQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvauPPfL7J2AVERiaoMJy9NBIwbJE2ZRJX7FZ2Dx7IibtTwdlqYSqTZTCsXkDS2jvNF8wWJKcibxXtOHng/0?wx_fmt=png)

腾讯技术工程

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvauPPfL7J2AVERiaoMJy9NBIwbJE2ZRJX7FZ2Dx7IibtTwdlqYSqTZTCsXkDS2jvNF8wWJKcibxXtOHng/0?wx_fmt=png)

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