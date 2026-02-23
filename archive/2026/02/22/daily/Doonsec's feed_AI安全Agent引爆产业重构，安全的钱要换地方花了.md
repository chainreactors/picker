---
title: AI安全Agent引爆产业重构，安全的钱要换地方花了
url: https://mp.weixin.qq.com/s/VXzEqqe2_-wL5VMVae7xeg
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:17:11.679577
---

# AI安全Agent引爆产业重构，安全的钱要换地方花了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dJ6206EMFEhu6mKhuoy4uaGnWbHtfz9U07cKKNBQ3kEJicQa2WiauWoXB6Y5yapdJp5BYNAy5je7ib44jEsKmEIxMPicR3lCm7UbJXoKllxDMpo/0?wx_fmt=jpeg)

# AI安全Agent引爆产业重构，安全的钱要换地方花了

原创

卜宋博
卜宋博

国际云安全联盟CSA

![]()

在小说阅读器中沉浸阅读

2026年2月20日，Anthropic 将 Claude Code Security 以“limited research preview”方式集成进 Claude Code：分析组件交互与数据流向，识别输入过滤缺失、认证绕过等复杂漏洞，并给出自然语言说明与补丁建议。

发布本身并不神秘：行业早已有 SAST/DAST、SCA、fuzzing、符号执行、红队审计，也早有“AI 辅助安全”。真正触发市场反应的是 Anthropic 的“事实展示”：其 Frontier Red Team 披露，**Claude Opus 4.6 在几乎不依赖专用脚手架、无需特殊提示的情况下，在开源项目中发现 500+ 个此前未知的高严重度漏洞，并能像研究员一样追踪上下文、证伪与给出修复建议。**

随后相关标的被连带抛售：传统网安公司与开发链路公司同步承压（如 CrowdStrike、Cloudflare、Okta、JFrog、GitLab 等）。

若只把它理解成“又一个扫描器抢份额”，会低估逻辑。市场在重新贴现一种结构变化：安全行业长期的“告警经济”正被推向“闭环经济”。

![](https://mmbiz.qpic.cn/mmbiz_png/dJ6206EMFEiaEibFLVCckBQrDXELTqZRoKHMbysP7kNCkib8xJWynK5X6KG87cZQQJibKpAo9yRFTNBVibIgAlg3QedNl139zCk7BqAQwdIFPibUs/640?wx_fmt=png&from=appmsg)

图1：2 月 20 日当天，网安股与 DevSecOps 标的分钟级联动下跌

**边际成本在下降，闭环稀缺性在上升**

传统网安产品的价值链大体是“发现—汇总—告警—工单—人工分析—人工修复/处置”。过去十几年，商业化优势建立在一个前提上：处置昂贵且难自动化，于是“发现”与“告警管理”更易定价，企业也愿意用叠加模块把风险“看见、列清单、能汇报”。

Claude Code Security 这类安全 Agent 的冲击点，恰好把处置链条往前推：不仅指出“哪里可能不安全”，还试图把“复现—验证—分级—最小补丁—回归证据—PR/变更建议”压成可重复流水线，并以“必须人工审批”对冲工程与责任风险。

因此，**企业持续付费的重心会从“告警数量与覆盖面”转向“可证明的结果”**：高危修复平均时延、补丁一次合并成功率、误报率、审计可追溯性与可回滚性等。过去这些更依赖组织能力与人力密度，现在开始被工具链与 Agent 工作流产品化。

这不意味着扫描器、规则库失去价值，而是更像“基础能力组件”，单独计价空间变窄；新的溢价更可能来自闭环能力与控制面能力。

**预算从“外挂安全”迁到“工程内生安全”**

短期最先变化的未必是“谁立刻丢客户”，而是采购重心：预算沿研发与交付链路移动，向能把修复落地、能让责任清晰的环节集中。

**第一条迁移：**从“扫描预算”迁到“修复流水线预算”。覆盖面仍重要，但“只报不修”的边际价值下降；企业更在意能否生成可合并的最小补丁、提供可复现证据、附带回归结果，以及风险分级与置信度是否可信。

**第二条迁移：**从“单点安全产品”迁到“平台控制面”。当 AI 能改代码、触发流水线、调用工具，它相当于高权限“数字员工”。组织会更敏感于：它是谁、能访问哪些仓库与密钥、谁批准其变更、出事故如何追责——身份、最小权限、Secrets、策略审批、审计取证会从口号变成刚需。

**第三条迁移：**从“事后检测”迁到“事前证明 + 事中监控”。修复更快不代表运行时防护消失：AI 同样在加速攻击与滥用；企业会要求把“Agent 行为”纳入可观测、可阻断范围。因此对网安股的抛售也可能被高估：替代压力与新增防护需求会并存。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEhcWMCY2jjtCM6TGCjL18ZWCicgXtLJa9vjcbf352Yogo9ZJQ8s08fcCvIGqShmIhzctK9yELVltv0RibO4xKiaBsib7vVia6QOoVQ8/640?wx_fmt=png&from=appmsg)

图2：预算迁移的三条曲线

**产业重估的核心：证据链 + 责任链**

暴跌会先把相关公司一起砸下去，但中期会分化。分化标准可概括为：价值来自“信息不对称”的会被压缩；价值来自“闭环交付”的会获得溢价。

**信息不对称的典型是“规则库/漏洞库更全，所以能多报”。**当模型在上下文理解、跨文件追踪与自动构造触发路径上显著进步时，这类壁垒会变薄，产品更可能沦为平台中的能力模块。

**闭环交付则是：不仅发现，还能把修复变成可上线变更，并且全过程可审计、可回滚、可追责。**护城河未必是模型本身（能力可能趋同），而是工程系统的耦合深度与治理沉淀：代码所有权、流水线、制品、签名、发布/回滚机制，以及运行时监控与处置网络。

**六类能力会吃到结构性红利**

更合理的提法不是“谁一定赢”，而是“哪些能力更值钱”。

**第一类：DevSecOps/研发交付平台。**安全 Agent 的成果要落到 PR、测试、审批、发布、回滚；掌握入口的人决定能否落地、如何兜底，入口价值可能被重估。

**第二类：身份与权限、Secrets 与策略控制面。**AI 越强越需要强治理：最小权限、分级授权、关键分支保护、敏感仓库审计、密钥轮转与泄露监测。Agent 改代码会把“内控”从财务扩展到工程。

**第三类：软件供应链可信与证明体系（SBOM、制品签名、依赖策略、可追溯构建链）**。变更频率上升会放大投毒与依赖风险，企业会更愿意为“可证明可信交付”付费。

**第四类：安全数据底座与可观测（含 Agent 行为观测）。**SOC 将同时关注工具调用、仓库读取、数据访问、自动修复动作、策略命中与越权尝试；谁能把日志变成可检索、可告警、可取证的数据层，谁就握住 AI 时代 SOC 底座。

**第五类：开源生态“分诊与治理基础设施”。**发现能力放大后，维护者处理负载会成瓶颈。Daniel Stenberg 在 2026 年 1 月宣布停止 cURL 的 bug bounty，核心原因之一是低质量报告带来的负担；行业会更强调“可复现证据包”与自动验证，而不是更多华丽描述。

**第六类：AI 安全运营（AI OpsSec）与对抗评测。**防御方拿到更强 Agent，攻击方也会拿到；企业会把提示词注入、越权工具调用、数据外泄、幻觉导致错误变更等当作一等风险，持续对抗评测与治理框架将形成新增预算池。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJ6206EMFEjV9mhPdB0vGBod5GED6LDEnGA9CzyDNHxDQGUC6UPiaqsxHFhDTe078eldhfE63nlyPpIgFnD34uyYK6rAynnWZyZQliaAJVXVc/640?wx_fmt=png&from=appmsg)

图3：新赢家画像矩阵（控制面 × 闭环交付）

**双刃剑效应会把“治理”推到更前面**

对行业保持客观，必须把反方向说清楚。安全 Agent 的双刃剑效应是工程现实：同样的能力既能加速防御，也能加速攻击；自动化既能降低 MTTR，也可能放大错误变更的事故半径。Anthropic 强调“人类审批”，实质是在承认：AI 进入变更链路后，责任与审计必须可追溯，否则企业不会让它进生产。

开源维护者负载危机同样现实：缺少最小触发输入与可复现证据的报告将被拒收，分诊与自动验证会成为必需能力。

![](https://mmbiz.qpic.cn/mmbiz_png/dJ6206EMFEhEQ1pb5m7yeaKH9ZIh7LQic0xwxB9kEsoCIW03HB4xibPUEhoicaVNAShK6rSVj6chST1R0gfnY5lmXic45pm1hzp0fmYuhZ4l0CM/640?wx_fmt=png&from=appmsg)

图4：从“告警指标”到“结果指标”的迁移

**行业形态：分化比“替代”更可能发生**

未来 12 个月，最常见现象是“全面加 Agent，但质量参差”。差距来自验证与闭环：能否稳定复现、压住误报、给出最小补丁、在 CI 跑出可信回归证据。经历几次“AI 修复引入回归”后，企业会更愿意为策略控制、审批链与审计链付费。

未来 24 个月，预算结构更清晰地重排，安全组织向“平台化”转型：把安全变更做成流水线成为核心能力，安全与研发边界继续模糊；单点工具仍存在，但更多以平台组件形态存在，定价权向掌握入口与闭环者集中。

未来 36 个月，Agent vs Agent 将成为常态：攻防两端都更快。**行业竞争从“谁检测更全”转向“谁治理更强、证据更硬、处置更快、责任更清”。**安全需求不消失，但利润池向闭环、控制面、证据与治理集中。

**估值换挡**

这场震荡的本质不是安全价值消失，而是价值中心迁移：从“发现风险”到“交付安全”，从“告警数量”到“修复证据”，从“外包检测”到“内生治理”。未来三年的赢家未必是模型最强者，而是掌握闭环入口与控制面能力的玩家；停留在告警与报表逻辑的厂商将面临定价权流失、平台化或被整合。

安全从未如此重要，但赚钱的方式已经变了。

本文作者：卜宋博，CSA大中华区研究协调员，观安信息安全专家

**大会预告**

**第九届CSA大中华区大会暨前沿人工智能安全峰会将于4月2日在上海举办。**大会以 “智·数·盾：构建韧性数字未来” 为主题，聚焦AI基座安全、可信数据流通与协同治理，通过前沿报告发布、标杆案例分享及年度荣誉颁发等系列活动，与您一同探索韧性数字未来的下一个前沿。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dJ6206EMFEiaqTJNfxichEQXJaJcQGERevictxwMcTJ5oQ5tv8DZ78Qd7JcMtU5TqyTEic8lwq745LmGwESu0HiawrgrqFribsZoVxt23vHbkamck/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dJ6206EMFEiaunNDicauWnsVKQgztD3zjiaqMH8LME3YwKoD5xQ85DQBkuzovrK4jHuibahaq4lz8ZoBeEOgLB2o8ibQ0N3WN3K6UuB3ialBevn1Y/640?wx_fmt=jpeg&from=appmsg)

扫码报名CSA GCR大会

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Atw1J8F68p5KiaFqiav31cr04yNib3LYJQr8icP8AOhorLFK4A5FQxavZVN0a03shJMibfe1uo0kicXia3XOmJ1S384VQ/0?wx_fmt=png)

国际云安全联盟CSA

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Atw1J8F68p5KiaFqiav31cr04yNib3LYJQr8icP8AOhorLFK4A5FQxavZVN0a03shJMibfe1uo0kicXia3XOmJ1S384VQ/0?wx_fmt=png)

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