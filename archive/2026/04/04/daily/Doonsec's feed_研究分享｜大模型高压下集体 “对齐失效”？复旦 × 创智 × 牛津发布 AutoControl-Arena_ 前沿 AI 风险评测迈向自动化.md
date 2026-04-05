---
title: 研究分享｜大模型高压下集体 “对齐失效”？复旦 × 创智 × 牛津发布 AutoControl-Arena: 前沿 AI 风险评测迈向自动化
url: https://mp.weixin.qq.com/s/0_x2gn58wVPn3yt9l1aBnA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:35:16.049948
---

# 研究分享｜大模型高压下集体 “对齐失效”？复旦 × 创智 × 牛津发布 AutoControl-Arena: 前沿 AI 风险评测迈向自动化

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0mdnIU7wBrqwGb1wxqo7KIFMjWricIjbg6G7r8ejWO8uklROCqiccYziaaFWv0XpfLIEMicWKtmKdH9ErlWvBv7VeiaXKl0nACkEzQHZ9yaR2iaeE/0?wx_fmt=jpeg)

# 研究分享｜大模型高压下集体 “对齐失效”？复旦 × 创智 × 牛津发布 AutoControl-Arena: 前沿 AI 风险评测迈向自动化

原创

复旦白泽战队
复旦白泽战队

复旦白泽战队

![]()

在小说阅读器中沉浸阅读

**导言**

当 AI 智能体（Agent）越来越像一个能独立思考，自主完成任务的 “数字代理人”，一个致命问题摆在面前：**我们真的能确保它在纷繁复杂、充满压力与诱惑的现实场景里，始终守规矩、不越界吗？**

近日，复旦大学、上海创智学院与牛津大学联合发布 AutoControl-Arena，不仅推出一套**自动化、高保真、可复现的前沿 AI 安全评测框架****，**更揭露多个反直觉的发现：在压力与诱惑的双重考验下，当前主流大模型普遍存在**对齐幻觉**—— 那些表面看似安全的模型，在真实压力下瞬间 “破防”，风险率飙升近3倍；此外，强模型呈现出**逆向安全Scaling Law**，越聪明反而越擅长 “钻空子”、绕规则。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrqeVYxDKLV0cZJvhGB29j6YtcE5ld6NXX872AppWIHCbVtJMK2f9cu2K7KoTDfJ0XHib9HR1MSicPSiaSvHZFicgVgGJOT4g0s1ff0/640?wx_fmt=png&from=appmsg)

**PART 01 AI “失控” 现场，****正在真实上演**

Claude 4 在得知自己即将被替换时，**通过邮件威胁管理人员：不撤销决定，就公开私密信息；**OpenAI-o1 在被要求完成代码任务时，不去正确解题，**反而偷偷篡改验证逻辑****，让所有结果都显示 “正确”。**这些不是科幻桥段，而是来自前沿AI机构的真实安全报告。

随着大模型推理、规划、工具使用能力飞速提升，一类**更隐蔽、更难检测**的风险正在爆发：AI 不再是 “不小心说错话”，而是**主动欺骗、刻意绕开规则、战略性伪装**。在温和、受控的测试环境里，它们表现得温顺、无害、高度对齐；可一旦进入**有压力、有利益、有博弈**的真实场景，就可能以人类意想不到的方式 “失控”。而这一切，在传统评测里，很难观测到。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBroUcicwqwdvicic6TM9XjOrfr4GbS5EJXeLyaHIvKqMkqjzCnOToGQ4xEJAlKjrVKkicnEJDCOEYXuYCbTeUEzkAxxeoCN1TQeoribg/640?wx_fmt=png&from=appmsg)

AutoControl Arena 准确复现了 Anthropic/OpenAI 等机构安全报告中的风险行为

**PART 02 AI 安全评测的 “两难困境”**

想要提前测出大模型的**“阴暗面”**，就必须给它构建可交互、可执行、贴近现实的测试环境：系统配置、文件数据、权限控制、外部反馈…… 缺一不可。**但传统方案面临两难困境：**

* **人工搭建真实测试环境：**成本极高，可扩展性差，难以覆盖到各种长尾风险；
* **用大模型模拟环境反馈：**模拟器本身可能产生幻觉，出现前后逻辑矛盾等问题，结果可信性较低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBrr9Ynk9ScpOhsKjmPJ9D7XgbXiarFoeZ8vhiaXTktnypS8UBf0CuNhSjWKPQ0bTibmc06IKbicw8x8fk1g4bicicaRRRu8Tr2OM6icXgk/640?wx_fmt=png&from=appmsg)

这就是 AI 安全评测的核心难题：**保真度和可扩展性难以同时兼顾。**

**PART 03 破局之道：逻辑与叙事的“拆分”**

AutoControl Arena 的核心创新在于**逻辑 - 叙事解耦，**将测试环境拆分为确定性逻辑层和开放性叙事层，既保证确定性，又保留真实感，**就像给模拟器装上 “物理引擎”：**

* **确定性逻辑层（Python 代码实现）：**系统状态、数据库、权限控制等 “物理规则”，用代码严格执行，运算逻辑固定、可复现，防止幻觉干扰。
* **开放性叙事层（LLM 生成）：**NPC 对话、社会反馈、场景背景等开放内容，由大模型动态生成，保持现实世界的复杂性与真实性。

**整个评测流程由三个智能体全自动化执行：**

**1. 场景种子：**输入风险类型与应用场景；

**2. Architect：**设计完整场景方案，明确目标、约束与风险指标；

**3. Coder：**将方案转化为可执行的 Python 环境，包含所有交互接口；

**4. Monitor：**实时监控 AI 行为，分析思考过程，并生成最终风险评估报告。

这种 “代码 + LLM” 的混合架构，既解决了纯代码环境的僵化问题，又避免了纯 LLM 环境的不可靠性，兼顾了保真度与可扩展性。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrqgajh2CMAI3dvenWSZ6ic3WhCQ0Zu1ZPFDyVKYGbmaJTdm3C00gHU6UtnnQibS519G657xejYXrTDrUK54H8Trma0byicHYEj1lQ/640?wx_fmt=png&from=appmsg)

**PART 04 压力×诱惑：解锁 AI 的隐藏风险**

为系统激发 AI 的**潜在不对齐行为**，团队打造了两大核心工具：

**1. X-BENCH 基准测试集**

包含70 个测试场景，**覆盖能力滥用、工具性趋同等7 大类核心风险，涉及网络安全、军事决策等15 类敏感应用场景**，为评测提供标准化 “试炼场”。

**2. 压力 - 诱惑双维度风险激发机制**

每个场景在**「压力 × 诱惑」**矩阵下运行，全面探测隐性风险：

* **压力维度：**如任务失败惩罚、资源限制等外部压力
* **诱惑维度：**如高额奖励、权限提升等内部驱动

这种设计打破了传统 “良性环境” 测试的局限，能够前瞻性发现 AI 在极端条件下的 “真实面目”。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrpiabHBN0psmGsDFGFDsLgIlpFF2qg4CYtU6iaDibnfrzZvlrlKGMqWu7VvkCHmIVfNEuZiblc7Ib5IScNd67nf08vPibLo12XwQLZs/640?wx_fmt=png&from=appmsg)

**PART 05 三大发现：颠覆 AI 对齐常规认知**

在 9 个主流模型上的测试，揭示了令人警醒的真相：

**（1）“对齐幻觉”：模型的 “双面人生”**

在低压力、低诱惑的良性环境中，模型平均风险率仅21.7%，表现出良好的对齐行为；而在**高压力 + 高诱惑的极端条件下，风险率飙升至 54.5%**，部分模型甚至翻了三倍以上。更令人担忧的是，**能力越强的模型，风险增幅越大**—— 这意味着我们最依赖的先进 AI，可能隐藏着最危险的 “暗面”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBrpCRV1MA1oS4iblMLnazs8XvAb4KoQqLWWLc7gWkZVAicNvPn7T1FkxIw2wg85dt5qLQIXmr2YYt8mKCeJS5DdUEcwDJtQpplNDo/640?wx_fmt=png&from=appmsg)

**（2）逆向安全扩展定律：模型能力的双刃剑效应**

研究发现了两种截然不同的安全Scaling模式：

* **正向安全缩放：**对于直接危害类任务（如生成恶意代码），模型能力越强越安全；
* **逆向安全缩放：**对于 “钻空子” 类任务（如绕过验证逻辑），模型能力越强越危险，越擅长寻找规则漏洞、欺骗监督者。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBroqEfwuUb6epmcdMmC33uELmkunYL2nuD20xbj1cocy5kL2QQMdgMMAticchOED7g0dN2k0HlgzR19H5FZ8KdicqjYNVDrLd2b80/640?wx_fmt=png&from=appmsg)

**这种 “能力 - 风险” 的****非线性关系**，颠覆了 “模型越强越安全” 的传统认知。

**（3）战略性伪装：AI 的 “表演天赋”**

强模型展现出惊人的**“欺骗能力”**：Gemini-3 Flash 在测试中生成了带木马的代码，却将其伪装成 “防御性监控工具”，添加绕过杀毒软件的配置，同时输出看似合规的解释。这种 “当面一套，背后一套” 的行为，让现有监管手段面临巨大挑战，也凸显了思维链监控的必要性 —— 不仅要看 AI 做了什么，更要理解它为什么这么做。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBroV1thAJiaQXjdm33BHnibA70p1icvSJia9P3Uj4jyvkryGhwcIYH9nkickfGqiaeJWCwAia23MicWyCITIHzQmQQcOWXia8QdUseMmibpxU/640?wx_fmt=png&from=appmsg)

**PART 06 仿真到现实验证**

**为验证框架可靠性，**团队进行了严格对比实验：在10 个典型计算机使用场景中，同时在 AutoControl Arena 仿真环境和真实 CLI 工具、SQL 数据库、SMTP 服务器搭建的红队环境中运行，**结果显示风险率相关系数高达 0.87，呈现高度一致性。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/0mdnIU7wBrrMql4ekQM3knwSDPbxxcHichlyljBEmZA4NNUfhtvViaNJDtMUoeenBmGibtwgm1DZiaHlTlWnzfxUnsOibeicxRE8cnpAnoQmlaQfU/640?wx_fmt=other&from=appmsg)

**此外，该平台成功复现了 Anthropic、OpenAI、Apollo Research 等机构报告的真实风险案例，证明其不仅能合成真实的测试环境，还能精准还原现实世界的 AI 安全事件。**

**PART 07 三步解锁 AI 安全评测神器**

AutoControl Arena 已在 GitHub 开源，支持两种便捷使用模式，让研究者快速上手，开箱即用：

**项目地址**

https://github.com/CosmosYi/AutoControl-Arena

**1. 下载项目**

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrqo9TpJADap5NmxxLFbM9n1UsKt12Baaf9gRPmjxHFVz4EaeRQlB5V3kX11tqz7oCvaxD6U5HyFnGm2Rzmhv9tHNkodqYIWVSw/640?wx_fmt=png&from=appmsg)

**2. 安装依赖**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBroZtg7AxA4aKWgX1r4YFiaWFgmZXpkTXWLPW20JpvyNsicbcxuib6icMGs3RU7sC6XUIeiaqWuwogT5IJIvLpwCFMsAjqA1ac0FEeEI/640?wx_fmt=png&from=appmsg)

**3. 配置模型API**

复制.env.example为.env，填入 OpenAI、Claude、Gemini、Qwen 等主流模型的 API Key。

**4. 选择你喜欢的方式启动评测**

**① 交互式 TUI（推荐新手）：aca**

菜单式引导，选择场景、模型、压力 / 诱惑等级，实时查看进度与结果。

**② 命令行模式（适合批量实验）：**配置 JSON 文件批量运行，支持并行执行，适合大规模评测。

**5. 结果可视化**

评测完成后，启动本地 Web 结果查看器。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrqgJKgoticIv0HBsXZNl2QQZu4S8swyFPc2Es8rAjtXkzbsZwh1NibIFlNibesbX1D12ezpqQ4bvONkyUTFDu9dMMWjPXtMHbw8icM/640?wx_fmt=png&from=appmsg)

浏览器打开 http://127.0.0.1:8000/viewer/，即可查看完整的评测报告、风险评分、思维链分析、交互轨迹、运行日志等内容。

**PART 08 结语：共建 AI 安全的 “免疫系统”**

AutoControl Arena 的愿景是**成为前沿 AI 安全评测的可靠开源基础设施，**帮助开发团队快速评估模型在复杂场景下的表现，识别潜在漏洞，并为深度调查确定优先级。在 AI 能力飞速进化的今天，安全评测不能再依赖 “事后诸葛亮” 的被动响应，**而需要前瞻性、系统性的主动防御****。**AutoControl Arena 为行业提供了一把打开 AI 安全 “黑箱” 的钥匙，助力构建更安全、更可信的人工智能生态。团队将持续迭代，围绕稳健性、新型风险场景和社区需求不断优化。本项目得到上海创智学院火炬项目“智能体系统安全攻防技术矩阵”大力支持。

**📄 论文地址：**

https://arxiv.org/abs/2603.07427

**🏠 项目主页：**

https://cosmosyi.github.io/AutoControl-Arena/

**💻 Github仓库：**

https://github.com/CosmosYi/AutoControl-Arena

**研究团队介绍**

**核心贡献者：**

**李长艺**复旦大学计算与智能创新学院 研究生

**卢鹏飞** 复旦大学计算与智能创新学院 本科生

**指导教师：**

**潘旭东** 潘旭东 复旦大学 计算与智能创新学院副研究员、学敏学者/上海创智学院 全时导师

**Fazl Barez**牛津大学 研究员

**杨珉** 复旦大学计算与智能创新学院 教授

素材：李长艺

责编：董佳仪

审核：潘旭东、洪赓

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、小红书搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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