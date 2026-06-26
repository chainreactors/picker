---
title: 【AI安全】Claude Code接管SOC！3人团队也能7×24
url: https://mp.weixin.qq.com/s/cM8-oQaSB7U4d0KfvoJMcg
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:05:49.212591
---

# 【AI安全】Claude Code接管SOC！3人团队也能7×24

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y05UtykogHSDWg7IW3WRgmywJe9sj8FgKBtWDWJAXmrkcwqoGFFhSjiaalxQxgCRes9Ot7TWxFJvzpdLMTdo4IKrmCr6IQGoOudicJCIEgcMQ/0?wx_fmt=jpeg)

# 【AI安全】Claude Code接管SOC！3人团队也能7×24

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、3个人的SOC，为什么必须找“第二班人马”？

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

###### 免费课程持续更新

https://space.bilibili.com/452583051/lists/7870008?type=season

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

很多安全团队都知道一个现实：**真正把人压垮的，不是一次重大攻击，而是日复一日、看不完的中低优先级告警**。😵‍💫

这次引发讨论的案例，来自 ZOZO 的一篇技术实践。按照原文披露，**他们的 SOC 团队只有 3 个人**，却要面对电商业务、内部系统与安全平台持续产出的告警流。对于这种规模的团队来说，最难的并不是“是否懂安全”，而是“有没有足够的手和眼睛，去把每一条告警都看完、判完、追完”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHTr09GEcynUSIImibeLBbnkeOXXiaRHicXpOeichcYDEvJCQkBgeHxdfrTrHfiapj6AfSIvF9Kt6ibTy6IdGcqSmwFfkwd89mjYYAIDY/640?wx_fmt=png&from=appmsg)

这也是很多中小企业安全运营的共同困境：

* 📥 告警量持续增长，但 HC 不会同步增长
* 🧩 告警背后需要拼接日志、情报、历史调查记录，动作很碎
* ⏱ 值守节奏很重，重复劳动会迅速吃掉分析师的判断力
* 😮‍💨 人工排查标准不稳定，疲劳时更容易漏判或误判

**所以问题从来不是“要不要自动化”，而是“哪些环节应该先自动化”。**

**如果连初筛、归并、证据拉取都还靠人一点点复制粘贴，团队规模再翻一倍也会继续被告警拖住。**

这也是 ZOZO 这个案例真正值得看的地方。它不是在讲一个“AI 会替代安全分析师”的夸张故事，而是在讲一个更现实的命题：**当团队只有 3 个人时，能不能先给自己造一个稳定、不请假、不会抱怨夜班的“初级值守同事”？** 🤖

从公开信息看，他们并没有把 Claude Code 当成一个问答机器人，而是把它放进了安全运营流程里，承担了一部分 Tier1 级别的初动响应工作。这个定位很关键，因为它意味着：

| 传统做法 | Agent 做法 |
| --- | --- |
| 人先看到告警，再去一个个打开工具 | Agent 先接到任务，再主动调工具取证 |
| 人工拼接日志、情报、上下文 | Agent 自动汇总多源证据 |
| 人工写调查摘要和优先级建议 | Agent 先产出初版分析结论 |
| 人负责所有重复性动作 | 人更多负责复核、决策和升级处置 |

这里最值得记住的一句话是：**SOC 的瓶颈并不总在“分析能力”，很多时候卡在“信息搬运和上下文拼接”。**

**谁能先把这些高频重复动作自动化，谁就能把人从“工具操作员”拉回“安全判断者”的位置。** 🔍

所以，别把这个案例只看成“某家公司用了 Claude Code”。更准确地说，它展示的是一种组织升级方向：**当 SOC 人手不足时，不是先幻想全自动防御，而是先把最消耗人的调查链路交给 Agent 跑起来。**

# 二、这不是聊天机器人，而是一条能跑通的调查链路

很多人一提 AI 落地，第一反应还是“让模型回答问题”。但 ZOZO 的设计明显更进一步：**他们做的不是“会解释告警的助手”，而是“真的会去查告警、拉日志、调情报、写摘要的执行型 Agent”**。⚙️

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHRGefdqlKoCXv2MxH35JicsmiavR6cbPMIWa5TBunBVq4Hqfrym9kXIP9taQdy16ebc7QA1mRt7dBIF1JmYuNyibxAGtiawZDtnHUM/640?wx_fmt=png&from=appmsg)

根据技术博客与二次解读内容，这套方案至少串起了五层能力：

1. 🛰 **告警源**：Splunk 负责收集与分析日志，输出 Notable 等安全事件
2. 🧠 **情报源**：OpenCTI 提供 IOC、攻击者、战术技法等威胁情报
3. 🔌 **工具接口**：通过 MCP，把 Splunk 与 OpenCTI 暴露给 Claude Code 可调用
4. 🧵 **Agent 编排**：Claude Code 根据任务目标调用不同命令、分派 SubAgent
5. 📣 **协同与处置**：Slack 回写调查结果，SOAR 继续承接后续自动响应

如果把这套机制说得再直白一点，它做的是下面这件事：

> **把原本散落在多个系统中的调查动作，重新编排成一条可执行、可复用、可循环触发的工作流。**

这和“聊天机器人”最大的区别，在于主体发生了变化。过去是人去开工具；现在是 Agent 接收目标后主动调工具。👀

原文中提到的几个典型命令，非常能说明问题：

* `/notable-response`

  ：围绕某个 Splunk Notable 做调查
* `/threat-hunting`

  ：基于 OpenCTI 报告触发威胁狩猎
* `/slack-alert-triage`

  ：从 Slack 告警线程中取回事件并完成初筛

而真正让人眼前一亮的是周期化执行：

`/loop 1h /slack-alert-triage 1h`

这行命令意味着什么？意味着**Agent 不再只是“被叫来帮一次忙”，而是变成一个可以按小时巡检、主动找未处理告警的值守流程**。🕐

**一旦告警抓取、日志检索、情报查询和摘要输出都被串成了闭环，7×24 小时值守就第一次从“排班问题”变成了“流程问题”。**

当然，流程能跑起来，不等于模型自己什么都能做。博客里还提到两个很重要的 SubAgent：

* `log-search-agent`

  ：专门负责从 Splunk 拉日志
* `opencti-agent`

  ：专门负责从 OpenCTI 拉威胁情报

这背后其实体现了一个非常成熟的工程思路：**不要让一个大而全的 Agent 承担所有细节动作，而是把高频检索拆给更窄职责的子代理。**

**SubAgent 的价值，不只是提效，更是让每个动作的边界更清晰、模板更稳定、错误更容易控。** 🧱

如果从安全运营视角看，这套架构最有价值的并不是“酷”，而是“实用”：

* 能自动补齐证据上下文
* 能统一摘要格式与调查口径
* 能把分析师从大量重复点击中解放出来
* 能让一个小团队也拥有接近连续值守的处理节奏

说到底，**AI Agent 真正的落点不是“回答得像不像专家”，而是“能不能把一条原本靠人手搓的流程稳定跑完”。**

**一旦工具、数据和协同链路被打通，模型的价值才不是停在嘴上，而是开始体现在产出上。** 🚀

# 三、真正关键不在模型多聪明，而在边界划得够不够狠

**🎯【真正关键不在模型多聪明，而在边界划得够不够狠】**

这一节真正关键的不是「真正关键不在模型多聪明，而在边界划得够不够狠」这个概念本身，而是它背后的判断路径、执行边界和可复用方法。

它怎样落到真实安全团队的工作流里？哪些细节会直接影响 AI 代理的可靠性？

加入 `Oxo AI Security 知识星球`，可查看本节完整内容，系统掌握「真正关键不在模型多聪明，而在边界划得够不够狠」的完整拆解与实战用法。

📚 **AI 文献解读：最前沿的 LLM 安全论文深度剖析。**

🐛 **AI 漏洞情报：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。**

🛡 **AI 安全体系：从红队攻击到蓝队防御的全方位知识图谱。**

🛠 **AI 攻防工具：红队专属的自动化测试与扫描工具箱。**

🚀立即加入 **Oxo AI Security 知识星球**，掌握 AI 安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

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