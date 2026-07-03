---
title: GIAC 2026·深圳站｜快手AI工程化实践精彩回顾
url: https://mp.weixin.qq.com/s/5wogQAySxf6BfVFw1X93tw
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:45:21.862326
---

# GIAC 2026·深圳站｜快手AI工程化实践精彩回顾

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1VrT8vzV3nnWJ3Gsic966EPiaYclVxAbtVz2ZGRS6ibf4icNpZoiahYicteBXtQvpgrDNPCaYzjezYXZW6YxNpIDSwZqJUz8QXt9OoVc/0?wx_fmt=jpeg)

# GIAC 2026·深圳站｜快手AI工程化实践精彩回顾

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

作为国内大规模 AI 工程化落地的先行者，快手技术团队参加了第十三届全球智能应用开发与架构大会（GIAC）。当前，AI 正加速从模型能力竞争走向工程化落地竞争，但行业普遍面临"个人快了、组织没快"的转化瓶颈——如何突破单点提效的局限，让 AI 真正融入研发流程、稳定支撑业务创新，已成为企业研发升级的核心命题。

此次大会中，快手技术副总裁胡伟担任联席主席；快手主站 AI DevOps 负责人李思在主论坛发表主题演讲，并担任「AI原生开发工具链技术原理与效能提升」专题出品人。快手主站技术部直播业务架构负责人李宁、快手主站技术部运营质量负责人朱宝昌、快手运营研发中心大前端技术中心负责人郭云龙三位技术专家带来议题演讲，系统呈现了快手在 AI 工程化的思考、路径与落地经验。

关注「快手技术」公众号，后台回复关键词“GIAC”获取演讲PPT。

以下为本次大会中快手讲师的分享内容回顾：

##

## 一、《迈向AI Native：技术团队的范式跃迁与组织进化》

快手主站 AI DevOps 负责人李思围绕千人级研发组织的 AI 范式升级展开分享，系统介绍了快手从 AI-First 走向 AI-Native 的实践路径。围绕 L1-Copilot、L2-Agent、L3-Agentic 三级研发范式，他首先阐述了"双轨并行"的演进策略：主航道面向大规模研发场景渐进推进，快速路则在部分高价值场景中率先实现端到端自主交付。

在此基础上，他进一步分享了快手主站如何从能力建设走向结构重塑，通过信息架构重组、流程分层解耦、交付单元闭环等实践，从工程环境、研发流程、组织协同三个维度突破"个人快了但组织没快"的效率转化瓶颈，系统性地降低协作摩擦，推动 AI 从辅助工具走向交付主体。工程环境层面，他将投入重点锚定在模型无法内化的三件事——事实（让 AI 看到正确的系统状态）、判断（通过评测驱动把标准固化为系统能力）、责任（约束可见、回滚兜底守底线）；研发流程层面，将人与人的协作层和 Agent 执行层分层解耦，通过结构化 Spec 和工具化意图转化降低交接损耗；组织层面，将交付与守护分离，功能 Owner 跨技术栈闭环交付，架构师专注标准与门禁守护。

目前，快手主站 L2 已成为主流研发范式，部分场景已以 L3 模式稳定交付，交付效率实现了非线性提升。验证规模化和先锋队模式的泛化平衡仍是当前关键挑战。最后，他提出三个叩问——组织能否让看不见的品味与判断被看见、为远见与定力留出空间、为年轻人被 AI 跳过的"慢慢生长"留出机会，强调范式在变、组织在变，底色永远是每一个工程师。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XPZl2orn8FrByXRot1TJNal3U152GJMVxmfrhwibibqYBydbmRLDhDtsGON8c4rw0seicJiahkIoXY7qY5UVXHYuB5ZnGeZ4VSp1Q/640?wx_fmt=png&from=appmsg)

## 二、《让 Agent 从“会生成”走向“可交付”：快手直播客户端 Agent Verify 体系建设》

快手主站技术部直播业务架构负责人李宁围绕直播客户端场景下 Agent 验证能力建设展开分享，介绍了快手在 Verify 能力方面的技术演进与落地成果。他指出，随着 AI Coding 快速普及，研发效能提升进入新的瓶颈期——代码生成越来越快，但复杂业务场景下 Agent 是否真的把事情做对，仍然很难稳定验证，因此快手持续推动验证范式从「传统黑盒 UI 检查」向「面向业务结果的证据驱动验证」升级。

分享中，李宁重点介绍了快手 Verify 能力的核心思路与分层方法：Agent 不只是模拟用户点击页面，而是围绕业务目标，先构造可复现场景，再触发关键行为，通过运行时观测、业务状态读取、事件信号和界面结果等多维证据，判断链路是否真正生效。用不同验证层级分别解决逻辑正确性、业务链路验收、UI 实时反馈等问题，而不是把所有验证都压到传统 UI 自动化或人工自测里。目前，Verify 能力已在直播客户端等高实时、多状态、强交互场景中逐步落地，人工验收成本持续下降。

除了"验证判断"，李宁还介绍了快手在"闭环修复"环节的进一步探索。围绕场景构造、行为触发、状态观测、结果判断和报告沉淀，快手正在推动 Agent 从"辅助编码和操作界面"升级为"能判断结果、沉淀证据、驱动修复"的研发伙伴，同时明确了 Verify 能力的适用边界——哪些场景适合交给 Agent 做自动验证，哪些仍需要人工补充判断，为端到端的智能验证能力建设打下基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1VysBTByz9YJ77XDrtxZPia6r5wgZXC9CEqDjrgvh69iadtj3thFb9zhdQPKcxDSKUkLV7VE2pCyHSXoILGvGJUPNRTbJmIurBRs/640?wx_fmt=png&from=appmsg)

##

## 三、《墨枢平台：AI 应用端到端自动化评测体系构建与工程实践》

快手主站技术部运营质量负责人朱宝昌从评测体系与平台工程双重视角，回顾了快手 AI 应用质量评测从"靠感觉判断效果"到"可量化、可对比、可归因"的范式升级过程，并分享了墨枢评测平台在规模化落地中的实践经验。

他指出，AI 应用评测的本质是将不确定的输出变为可判断的质量，其核心正从传统测试的"功能对不对"转向"智能体能否安全可靠地完成任务"。围绕这一转变，朱宝昌重点介绍了可信评测体系在标准、数据、方法三个要素上的构建逻辑——标准须定义清晰的 rubric 判定规则、数据集按风险分层管理并持续回流 badcase、方法按问题类型匹配（确定性问题用 Code 评估器、主观判断引入 LLM Judge、高风险保留人工校准），强调没有经过人机一致性、稳定性、偏差分析和成本效率四类验证的裁判模型，绝不能作为发布门禁依据。

此外，他还结合文生文 Push 文案、多模态视频理解、Agent 执行轨迹三类场景分享了实践思考，提出评测不能止步于出一份报告，而必须将结论接入发布链路变成质量门禁、让线上 badcase 自动回流形成数据飞轮，从而推动评测从静态测试集升级为持续质量治理基础设施。目前墨枢平台已支撑55+项目、拦截 badcase 290万+个，团队正推进全链路评测 Agent 化以实现标准分析、裁判构建与自动评测的全流程闭环。

![kim image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1Uibo3QuVdROHfFsIOUOhfInS5IpQwer0SvTo55HRxA8KORhxh2CzjkYFx6MDJpAo5Qs6ichLUdB9raOg6AsEUhXOdc0wKia8madA/640?wx_fmt=jpeg&from=appmsg)

## 四、《快手运营场景规模化端到端需求交付实践》

快手运营研发中心大前端技术中心负责人郭云龙围绕运营场景软件交付新模式展开分享，系统介绍了快手从低代码集成 AI 走向以 AI 为核心构建交付范式的实践路径。围绕内循环、外循环、元循环三重交付循环，他首先阐述了范式转移的必然逻辑：模型能力持续抬升、个体产能显著跃迁，但组织交付效能基本持平——"个人快了但组织没快"，问题不在人"写得快不快"，而在组织"交不交得出"。

在此基础上，他进一步分享了三重循环如何打通交付闭环：内循环通过架构提维与即时工程反馈让 AI"干到底"，外循环通过多验证原子能力编排突破 AI 伪验证陷阱让产物"敢上线"，元循环通过评测驱动的 Hill Climbing Loop 实现 AI 能力自动化爬升，系统性地推动 AI 从辅助工具走向交付主体。

目前，小需求已实现小时级无接管交付，大需求单兵产出接近小团队（16pd 完成传统约109pd ），运营场景 pass@1 从26%提升至41%，同时催生OPC 一人多栈、FDE 前线部署等新交付形态，验证了 AI 驱动交付范式转移的实际价值。

![kim image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1UYpJGhB37G8KKc5aSkeMZqFAE1Tf6seichatr6PEUghiaIloKN07NibQve5Wqoib2xrib4Y0JhlEibvP5lMpH2jiciasEJtwjtMsJk9yE/640?wx_fmt=jpeg&from=appmsg)

从 AI Native 范式跃迁与组织进化，到 Agent Verify 验证能力建设，再到AI应用评测体系构建与规模化端到端交付实践，快手此次在 GIAC 大会中的分享，集中呈现了AI在大规模研发组织中从单点提效走向体系化交付的实践路径——让 Agent 不只"会生成"，更要"可交付"和"敢上线"。

未来，快手也将持续推动AI在研发全链路的深度融合，从验证闭环到评测飞轮，从交付范式转移到组织能力进化，探索更加成熟的 AI-Native 研发与测试范式，为行业提供更多可沉淀、可复制的实践经验。

更多演讲精彩分享，欢迎关注后续内容发布！

欢迎加入【快手技术交流群】！

扫描二维码👇

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VVwKmgrr085nyhyRnKdoOgq52iarwdEHqic8OqBDibcdyOI5fuzGJz0AVJFDfCchVVr6beQ6hWMic7awbLlAU2y8x2hrTSKyJeicO0/640?wx_fmt=png&from=appmsg)

点击【阅读原文】，获取讲师分享PPT！

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZxDY5TMPs0GnTFDtpq8oAf91ZQDzvLt6LCp56JQCbFT2cT8uZquFdeJOKbmM4fucIPqtAPvMT0X4DpfpuZibic3Q/0?wx_fmt=png)

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