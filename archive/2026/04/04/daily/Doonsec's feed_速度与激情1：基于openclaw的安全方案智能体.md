---
title: 速度与激情1：基于openclaw的安全方案智能体
url: https://mp.weixin.qq.com/s/EcCmmjdKoME5JonEgUwv8g
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:45.456777
---

# 速度与激情1：基于openclaw的安全方案智能体

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibANIaIJODOlB6hlOG6VlsYG1EmjlVNKXibkg04iazXuRtFmZ8sAOVQ1iaYzHw8cUaW1sljkK8T9YDmJfibovmB2FaibPibKFjG6kBjj2ibxf9s0pYI/0?wx_fmt=jpeg)

# 速度与激情1：基于openclaw的安全方案智能体

原创

DIMU
DIMU

AI简化安全

![]()

在小说阅读器中沉浸阅读

这是「速度与激情」系列第1篇，聊一件最近投入生产的事：用 OpenClaw 把安全售前能力做成可复用的智能体，让写方案、做汇报从「按天算」变成「按分钟算」。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOll8vND5tkRmUm2IoBic0f5ibwzh9M1ZcvVE4z4SUtBicKAT0D8MN0Ja3tYywObGCeMYO7lyIW8c7ib6MQ7kA9rOdDQLGNQiceGl7N8/640?wx_fmt=png&from=appmsg)

安全售前要同时懂多领域、又要快速出 PPT 和 Word，人力永远不够。若只靠单次对话让大模型「写一篇」，你会得到：结构飘忽、数据不可信、版式无法进客户会议室的材料。

我的目标是把能力**产品化**：身份清晰、技能可插拔、产出路径固定、效果可复现——这样才是**生产力**，而不是偶尔灵光的玩具。

## Skill 设计：坚持四件事

Skill 不是「多写几段提示词」，而是一套**可执行契约**：

**1. 说明书与脚本分离。** 每个 Skill 有自己的 `SKILL.md`：什么时候激活、输入要什么、输出是什么、依赖什么命令；真正干活的是脚本。改版时优先改**数据与说明书**，脚本保持稳定，减少「一改全崩」。

**2. 用结构化规划代替自由发挥。** 售前材料最怕「想到哪写到哪」。我的做法是：智能体先产出一份 **slides\_plan.json**（或等价结构）——每页写什么、用什么布局类型、关键数据与标题是什么；再由脚本按布局渲染。这样**内容可追溯、可 diff、可回滚**，也方便你做评审。

**3. 规范驱动，而不是模板堆砌。** 从真实汇报材料里抽象：配色、标题栏、卡片层次、图表与正文的比例；写进 Skill 的设计原则里（例如：内容页统一标题栏样式、布局类型要轮换、架构图优先用形状拼建以保证中文可读）。**模板会僵化，规范能组合出不同客户的故事。**

**4. 内置 QA 意识。** Skill 里会要求生成后自检：布局是否单调、要点是否过多、表格是否溢出。这不是形式主义，是减少返工成本——**省下的时间才是提效。**

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOmNh6KYjNVm39cXgde4HOq4siaHNv5hsgBnGZfibrxTHFYEyFOtHdma7SbVsnuTIfsmkJmTk5AfFaVye4gb1icDesKrnS4VXdfKXI/640?wx_fmt=png&from=appmsg)

## 从飞书一条需求，到反问、再到成品 PPT：完整流程

这是实际跑通时的链路，方便你对照自己的协作工具改造：

**第一步：飞书侧发起需求。** 用户在群里 @ 智能体，用自然语言说明意图，例如：面向某单位领导的「AI 重构安全」汇报、页数、侧重点（合规 / 架构 / 案例）、是否需要配图等。需求越具体，后面越少返工。

**第二步：智能体反问，补齐关键信息。** 若信息不足，智能体会主动追问（而不是瞎编）：受众是谁、汇报时长、必须出现的政策或术语、有无现成数据、交付物是「精简版」还是「投标级」等。这一步的价值是：**把「模糊一句话」变成「可执行的规格」**，避免生成一堆用不上的页。

**第三步：规划与确认。** 智能体根据追问结果，整理出章节结构、每页布局类型建议、是否需要架构图/流程图/数据图，并（在理想情况下）给你一版「目录级」确认；你点头或改两句，再进入生成。

**第四步：生成规划文件并执行脚本。** 将确认后的结构写入 slides\_plan（JSON），调用 PPT 技能脚本，输出到固定目录。

**第五步：交付与微调。** 成品是可直接打开的 `.pptx`，文字与形状可编辑；若客户现场要改标题或数字，改 JSON 重跑或直接在 PowerPoint 里改都行。

整条链路的核心是：**自然语言入口 + 结构化中间层 + 确定性渲染**，而不是「模型一次吐一个文件」。

## 成品展示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOmeLllA2VZYSeh3B7BDjUWT1icZdt91A2ZMlNmtRXsCricj25NJTXfRB5AE5h5wMYBzJxvx9VGJZiczmPRrzqfQ6kZn3rNLMscCbs/640?wx_fmt=png&from=appmsg)

图：在飞书里面输入需求（可直接语音输入）

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOlKDLJos5Jx4wZRXrobZO1V2FXdvvicEPkOU2F19lYhp6OHRuwO6bq0gMvVMQLcnZ5kQpxGxnfQEJUyIrCyF8X0H2QW3cQibQicyQ/640?wx_fmt=png&from=appmsg)

图：最终输出的ppt

## 效果：从「天」到「分钟」意味着什么

同一需求可以先出精简汇报版，再扩成完整方案版；交付节奏从以往数天压缩到**分钟级**，版式统一、可直接交给客户微调——本质是把个人经验变成**可复制的产能**。
但请把「快」理解为：**把重复劳动自动化**，而不是把专业判断外包给模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOlLuVqfG3vu1jpo4kKX3hLh52NAibXNAlrJ8ulQp1vzgUWNHyHGufx4Fy5CbQtJmLdklMKKEGOOIz9sC3zCtjCvP0kVvAWHpclA/640?wx_fmt=png&from=appmsg)

## 一点真心话：用 AI 的体感，有时像「吸鸦片」

最近密集研究、使用 AI，有一点心得想分享。

盯着 AI 写代码、写方案的**每一步**，你会很爽，但**时间也在动**。如果人的能力不进化，很容易被带进**不断试探**：换一个提示、换一个模型、再试一次工具链——好几个小时就过去了，问题没本质推进，只有**虚假的忙碌**。这和「鸦片」的类比在于：**快感来得快，代价是时间与生活体验被悄悄吃掉。**

举个真实例子：某次做规划，先说是**内部规范**一顿操作；走不通，又说是**外部规划**再一顿操作；还是不行，最后又回到**内部规范**——**反反复复**，没有一条清晰的主线。若人不在旁边做「拍板人」和「架构师」，只跟着 AI 来回试，就会在这种循环里空转。

## 结尾：不必焦虑，要学会驾驭生产力

AI 化势不可挡，**焦虑没有用**，有用的是三件事：

1. 1. **把 AI 当生产力工具**，明确自己的价值定位——哪些事交给自动化，哪些事必须你亲自判断、对客户负责。
2. 2. **保持学习与迭代的习惯**：学新工具、学新框架、也学**如何提问、如何验收、如何说「不」**。
3. 3. **主动平衡**：在保持学习的同时，多和**身边的人、大自然**打交道，注重**人生体验**。技术再强，也只是生活的一部分；**学会平衡**，才不会被工具反噬。

希望你在「速度与激情」里，抢到的是**时间**，而不是**焦虑**。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOn2EMyEMlfRNpA60V0eSjhzGpNgJlAlVhsc0x2VVP5GFg0MLwXbywOqJTWFTPUibkAsBEKTk2VZeibvLqsYTjsXvm8cInvxuhJbQ/640?wx_fmt=png&from=appmsg)

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsiaxrJrtBWmqoVLfOmHIGZtJG9aYmICG4neEFJV1Ylb0sSIkLF7bKF4GN1Vicibuo3DzDHWibVsBtEvwg/0?wx_fmt=png)

AI简化安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/d4ae4qYgqsiaxrJrtBWmqoVLfOmHIGZtJG9aYmICG4neEFJV1Ylb0sSIkLF7bKF4GN1Vicibuo3DzDHWibVsBtEvwg/0?wx_fmt=png)

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