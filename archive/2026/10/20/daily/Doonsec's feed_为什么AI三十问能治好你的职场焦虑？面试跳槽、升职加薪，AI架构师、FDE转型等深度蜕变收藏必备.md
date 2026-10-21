---
title: 为什么AI三十问能治好你的职场焦虑？面试跳槽、升职加薪，AI架构师、FDE转型等深度蜕变收藏必备
url: https://mp.weixin.qq.com/s/Z5kEDZ0qnGbV9XREPPYwug
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:48:16.064238
---

# 为什么AI三十问能治好你的职场焦虑？面试跳槽、升职加薪，AI架构师、FDE转型等深度蜕变收藏必备

# 为什么AI三十问能治好你的职场焦虑？面试跳槽、升职加薪，AI架构师、FDE转型等深度蜕变收藏必备

原创

AI安全迪哥
AI安全迪哥

AI安全迪哥

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

迪哥系统整理了AI三十问，理解它，面试跳槽、AI开发、FDE转型等会有质变。或许越问越看不懂，但可以作为你的学习抓手。

注意

三十道问答，背后融合了斯坦福大学的课程、吴恩达Andrew  Ng的课程、AI厂商前沿技术报告（例如OpenAI、Anthropic、英伟达）等的知识提炼。完整掌握后，会完成在AI领域的蜕变，纯分享，没有广告、不培训、不卖课。

01Agent 的Loop Engineering

循环骨架、规划、工具接口、多 Agent、自我反思

02CccContextContext上下文与记忆Memory

窗口、Attention预算、检索、压缩、缓存与KV Cache

03AIAI的能力从哪来

SFT 与 RLHF 与 RLVR、蒸馏、MoE、数据配比、奖励函数

04推理与成本

采样参数、方差、量化与带宽、多算、延迟预算

05证据与评测

榜单污染、判官、噪声地板、消融、端到端

06安全与判断

注入、越狱、可解释性、护城河、信任校准

一、Agent 的Loop工程：会说话不等于会干活

Q01｜Loop Engineering 和 ReAct 的区别究竟在哪一层？

**答**　两者不在同一层，也不是替代关系。ReAct 是 inner loop：在单次任务内部，让模型交替输出推理和动作，工具返回的 observation 续在序列后面，管的是“这一步怎么想、下一步怎么走”。Loop Engineering 是 outer loop，坐在 harness 上面一层，管的是“这个任务做完之后还要不要继续、什么时候触发下一轮、预算烧到多少必须停、子 Agent 的结果怎么收回来”。Addy Osmani 2026 年 6 月那篇《Loop Engineering》里是两句话：“Loop engineering sits one floor above the harness.” 下一句的主语是 harness：“…but it runs on a timer, it spawns little helpers, and it feeds itself.”

说得再直白一点：ReAct 是工人干活时的“边想边做”，Loop Engineering 是车间主任设计的排班表、质检点和下班铃。ReAct 写错格式，循环还能跑；outer loop 的终止条件写错，系统就通宵烧钱。

**追问 2｜今天主流 harness 里 ReAct 的 thought 为什么“退化”了？**

**答**　因为推理挪进了模型原生的 reasoning channel，在生成时就被消化掉了，不再以 Thought 前缀的形式留在跨轮上下文里。工具调用走结构化协议，跨轮只剩 observation 和可见文本。你抓一次请求就能看到：历史里多数只有工具结果，没有上一步的推理原文。这带来的后果是：跨轮纠错不再靠“回看自己怎么想的”，只靠它读到了什么。所以工程重心必须落在 observation 的可判别性和状态外显上，而不是指望模型从自己说过的话里回头找线索。

**追问 3｜推理进了权重，工程还拦得住模型的动作吗？**

**答**　拦得住的只剩工具执行那一道闸门。文本化 ReAct 的真正价值从来不是“教会模型思考”，而是给外部留了插入点：Thought 和 Action 是两个字段，你能看完理由再决定放行、改参数还是踩刹车。推理进权重之后，中间态消失，等于把“审草稿”降级成“扣成品”。更要命的是前提反了：**Loop Engineering 的杠杆不在推理质量，而在观测质量、调用顺序、并行度和预算切分**。想靠改提示格式去修模型的方向性错误，是在错误的层上做正确的事。

Q02｜为什么给 Agent 更多轮次并不等于更强的规划？

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczMFkIZFVysicQLgtKK5XzzLA5ZKFpKH3DVr5xYezuQr0bODOmhTKLR6vO27yRBf8rIJ625r4TqusibRY9Y9fdLiaEeVv9CXTbIGbg/0?wx_fmt=png)

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