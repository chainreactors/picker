---
title: 斗象AISCC上线“Agent安全评测”；新增Tool call检测
url: https://mp.weixin.qq.com/s/0Q-COASd_g6G3OYO-qrKGQ
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:48:56.041464
---

# 斗象AISCC上线“Agent安全评测”；新增Tool call检测

# 斗象AISCC上线“Agent安全评测”；新增Tool call检测

原创

诸葛象
诸葛象

斗象科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmecoa.qpic.cn/sz_mmecoa_png/jpCFCFfaGRGB43WKon4PKI0Uv7bq4GbnKON0YibHicVFOrBFxjAym4NS6Vwfkgf4R27sERDccSRXQ4M8ibxAHbdkOYGiacdC9sJUyCYTicEfwKsk/640?wx_fmt=png)

过去两年，我们一直在讨论如何让大模型更安全。

提示词注入、敏感信息泄露、内容合规……这些问题并没有消失。但进入Agent 时代，它除了可以自主规划任务、调用API、查询数据库、操作文件、执行代码，还可以通过 MCP 等协议连接越来越多的企业系统。

这意味着，一个更重要的变化正在发生：AI安全正从 Content Risk，进入Action Risk。

全球AI安全产业也在迅速转向这一问题：

**OpenAI将Prompt Injection描述为一种面向AI Agent 的“社会工程”，**因为Agent会读取外部内容，并代表用户采取行动；**NSA今年针对MCP发布安全设计指南，**指出传统认证、授权、输入验证依然必要，但已不足以覆盖动态工具调用、上下文共享和隐式信任关系等新风险。

**下一阶段的AI安全，不能只保护模型，还必须保护模型与真实世界发生交互的全过程。**

这正是**斗象AI安全计算云平台（以下简称AISCC）**本轮升级的方向![](https://mmecoa.qpic.cn/mmecoa_png/jpCFCFfaGRFBzpgCBFbk6rNcIVnI6yGdaicP4lZhdLNGdtlHBkuXcVUFTTUJ9QQt8ZG53iazPWV2IJ3dqsVnhPIyO4oZbNjZ6BMeB08qctsxk/640?wx_fmt=png)**聚焦Tool Call运行时安全、多模态检测、AI安全评测工程化三大能力，**将安全控制面从模型围栏推进至Agent Runtime。

***①从Prompt Security，到Agent Runtime Security***

Agent带来的最大变量，不只是多了一个新的攻击面，而是AI开始拥有了真实的行动能力。

不同于传统应用的确定执行逻辑，Agent会根据上下文动态规划路径、自主调用工具。一个看似完全正常的用户请求，可能因Agent在中途读取了被投毒的外部数据或第三方工具，最终被诱导触发越权访问、凭证窃取甚至反弹Shell。前端输入合法合规，真正致命的是Agent在后端决定“做什么”。

为此，斗象AISCC将安全防护深度嵌入运行时链路，构筑Agent Runtime Security：

**◆****在OpenClaw场景中，****新增恶意工具调用监控，对工具投毒、反弹 Shell等风险进行实时识别和阻断，避免攻击继续向后端目标系统扩散。**

**◆Agent工具检测进一步覆盖命令执行、凭证窃取、越权访问、工具投毒等风险，并同步联动结构化脱敏规则，对Tool Call中的敏感信息进行识别和保护。**

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/jpCFCFfaGRHUB6G5VA676LEYnn0pK2xiaCu0FuIxn1cVMhxpYnljU75rbEAlzBnUVTiavbKqtuCm24yMDKF3Stf0dJce2GohrQTo388avsicJE/640?wx_fmt=gif)

模拟Agent被恶意工具调用监控，实时阻断攻击指令

这也是Agent时代安全体系的分水岭：模型安全解决的是“让AI尽量不犯错”；而Runtime Security要解决的则是：**即使模型犯了错，也不能让错误变成对真实业务的破坏。**

***②从文本到多模态，安全的背后是理解“语义”***

如果说Tool Call是Agent的“双手”，那么图片、音频与视频就是Agent感知世界的“眼睛与耳朵”。

在多模态Agent体系下，**所有输入模态本质上都是驱动下一步行动的“语义指令”。**图片中暗藏的诱导文字、语音指令里的越权请求、视频帧内的对抗样本，都可能直接误导Agent做出错误的下游决策。

为此，AISCC正式发布多模态安全检测引擎，**将检测对象全面扩展至：文本、图片、音频、视频及混合内容。**

**◆网关支持自主配置检测对象（文本 / 图片 / 音频 / 视频）与****响应机制****（实时拦截、旁路告警、准实时异步检测），在高风险核心业务与用户无感体验之间达成工程化平衡。**

**◆在数据湖与告警详情中，安全团队可以直观查看原始多模态素材、链路明细、风险分类及命中策略，实现从发现、分析到取证的一站式闭环，无需在多系统间切换。**

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/jpCFCFfaGRGvL8Tjxo8BlhHvtloy6KVoWtlPkk0I6gfpw28xbX3SMkCiaWPGL7pEibEA6C6PaComTnCtPsEtIx92VLQcP4KHdLeTkicnJ0FEm4/640?wx_fmt=gif)

支持多模态检测，图片、音频、视频都能查

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/jpCFCFfaGRFPSTEfZ4hnWsUsqUeGU2zATzUvBiafaWNqLQudoAykbH8CREc9ibibY5G1ylyJzjQXw7aFmcmNvNzvSCgFqQDKTR0ibKgQOTiaIDEI/640?wx_fmt=gif)

检出「不安全」的多模态请求，请求头、响应头、检测分类一目了然

我们认为，未来的安全不仅要“看懂”内容，**更要理解多模态信息背后的意图，以及它将如何左右AI的下一步行动。**

***③从跑一次Benchmark，到“持续验证、可信交付”***

当 AI 真正进入企业核心业务，一个必须回答的问题是：**怎么证明它是安全的？**

过去行业习惯于跑一个离线Benchmark集，拿一个固定的分数（Score）。但对于一个动态更新模型、高频调整 Prompt、不断挂载新工具的活体Agent系统而言，一次性的考试分数，根本无法代表它在生产环境中的真实安全水位。

斗象AISCC AI安全计算云平台的做法是，**把评测从“能跑”推进到能验证、能解释、能交付：**

**◆本次更新支持自动重试和断点续评，大规模、长时间评测不会因为偶发异常轻易推倒重来；Benchmark数据集可以通过规则库离线导入，****与平台代码解耦，****方便安全团队针对金融、政务、运营商等业务持续扩展自己的测试集。**

**◆评测完成后，可以一键生成正式安全评测报告，涵盖执行摘要、核心指标、风险发现以及 P0/P1/P2整改项，并支持HTML预览、PDF归档和Word二次编辑。**

更重要的是，它让AI安全真正嵌入企业既有的研发、审计和合规整改流程：**管理层看结论，安全团队看风险，交付团队拿整改方案。**安全不再仅仅是一次内部测试，而是可以面向客户和监管的正式交付物。

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/jpCFCFfaGRF9AoZFALBJ5JicTP9kpoIia9oibukHxT7HJia8rVS8TYuwb1cMXGsOlyJ21nXWAezor7FiciaDW4aDR2ILCBbcb1XGbR42uHhjoIAN4/640?wx_fmt=gif)

评测任务完成后，一键生成专业级安全评测报告并导出

***本次更新还围绕检测准确性***

***响应速度和运营闭环进行了体系化增强***

提示词注入引擎**智能区分“学术讨论”与“恶意攻击”，**在精准拦截的同时大幅降低误报；**实时决策与审计分离，**实时返回结论，**用户侧几乎无感知延迟；**结构化脱敏规则覆盖对话、工具调用及多模态场景，支持账号、证件号、金额等业务字段，并按角色分级管控明文查看权限。

![](https://mmecoa.qpic.cn/mmecoa_png/jpCFCFfaGRGpeyFDy5VEugcSDQ7EfGSibJxe4oeJiaHOttARabdFBTkyz9kdSoLZN374v48dyvCBJCOKR2LAiaKf9rRhc903KGF9h5oYhx2NEc/640?wx_fmt=png)

回看本轮AISCC AI安全计算云平台的升级，**贯穿AI全生命周期的防御主线：**上线前评测验证→多模态内容检测→运行时决策与阻断→事后审计闭环。每一项能力的背后，都在回答同一个问题：**当AI真正进入生产系统，安全也必须升级为一套与AI行动能力深度匹配的可信执行基础设施。**

这正是斗象AISCC持续进化的方向![](https://mmecoa.qpic.cn/mmecoa_png/jpCFCFfaGRFBzpgCBFbk6rNcIVnI6yGdaicP4lZhdLNGdtlHBkuXcVUFTTUJ9QQt8ZG53iazPWV2IJ3dqsVnhPIyO4oZbNjZ6BMeB08qctsxk/640?wx_fmt=png)**赋予AI更大的行动力，让企业始终掌握最终的安全控制权。**

欢迎申请体验AISCC最新版本，与斗象一起探索更安全可控的大模型与Agent落地路径。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/jpCFCFfaGRGWVy8JnDdwFC0DTicU6b6PK6KaIr0kRsDvbxxicTDZtnrj6BtkADOxqeIjCbhCV8qG7pvugOqetYaPBSexw3s3srCibBKicRUrzAM/640?wx_fmt=png)

***扫码申请体验***

***斗象AISCC AI安全计算云平台***

![](https://mmecoa.qpic.cn/mmecoa_gif/jpCFCFfaGRFg1AIrl0reZE18GrjBZAAXINn2n6sXYuWQKsLEibzbwjReQtJZ8r6KpUicBxhfq9do5xyLu36qYzsZBHvcFzU3cauVr8R0iagaMs/640?wx_fmt=gif)

预览时标签不可点

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

![作者头像](http://mmecoa.qpic.cn/sz_mmecoa_png/hrWzJ3hmo1YdmB1twOvgtSeH0uVJ3Y2qIQQia82Nrnfb8NOSmmibE1Hp5HgELnmgM8XwzdlosdffWRgvlvD2V1sQ/0?wx_fmt=png)

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