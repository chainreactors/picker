---
title: 震惊！最新揭露：AI缺的根本不是智商，而是这两样东西
url: https://mp.weixin.qq.com/s/RvTn4lNx8OiI8B3HF7zj9w
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:14:30.095871
---

# 震惊！最新揭露：AI缺的根本不是智商，而是这两样东西

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PIWj1VguNotIrxR5DSMaKAicQFYVQHK1aGoOksbfxYBM09odG15pcXZwxbl3Qp8icHKIRicwcxdAAnPd2ibibxlRmow4bnOX2IrDaAxGgzyYK55A/0?wx_fmt=jpeg)

# 震惊！最新揭露：AI缺的根本不是智商，而是这两样东西

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器中沉浸阅读

> **摘要**：当 AI 智能体在安全领域频频“翻车”时，我们往往归结于算力不足或模型太傻。但微软团队发布的 CTI-REALM 基准测试结果给出了令人意外的答案——AI 并非不够聪明，它只是还没学会怎么用最专业的“行话”干活。本文深度解读最新研究，用数据说话：行业经验和精准的 Prompt，才是决定 AI 落地的关键。

---

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNotALh0mNx7UFibWbEamuGDh7M6Lq2ib1p0KvZROzn5bpMdIVx9JdruCLWokyQZ84heufO5KatIduCoga7jNW2JEE6g1bgGLcLOWE/640?wx_fmt=png&from=appmsg)

最近，很多技术圈的朋友都在讨论一个现象：**明明都是号称 SOTA（目前最先进）的大模型，为什么一到具体的安全业务场景里，还是显得“不太灵光”？**

有的朋友会归结为："AI 还不够智能，算力还跟不上。”

但如果你读完微软安全 AI 团队最近发布的 **CTI-REALM（Cyber Threat Intelligence Real-time Evaluation and Metrics）** 基准测试报告（arXiv:2603.13517v2），你可能会颠覆你的认知。

这份研究专门考察了 LLM Agent 在安全领域的“实战能力”——**能不能读懂威胁情报，并自动生成能抓黑客的检测规则**。结果非常有趣：**AI 缺的根本不是智商，缺的是具体的行业经验和精准的 Prompt。**

## 一、实验环境，这是真的在搞“红队测试”

为了搞清楚 AI 到底行不行，研究者设计了一个高难度的考场：**CTI-REALM**。

这可不是简单的选择题，而是**真实的“黑客演练”**。他们在云端搭建了两个版本的测试环境：

1. **Linux 端点**：模拟企业内部的服务器和电脑。
2. **Azure 云平台**：模拟复杂的云上基础设施。

### 🔥 埋设炸弹：真实的攻击痕迹

研究者在这些系统里预先埋下了真实攻击者的“作案手法”。这些数据不是瞎编的，而是来源于 **37 个公开的真实威胁情报报告（CTI Report）**，涵盖了从单点攻击到复杂的多步入侵场景。

你可以想象成：给 AI 看了某次真实黑客攻击的监控录像，然后问它：“你发现了吗？哪里可以报警？”

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNouJicvkU6m7ShE4xy1501LlrrXONWJcTFSX4a2VJvM4xkLkdrBicEXfmae9a19RWk0ONKRkDhpHFl7Ch9zXKIYicrzianRogofA90Y/640?wx_fmt=png&from=appmsg)

### 📝 判卷标准：不仅看答案，还要看过程

研究者并没有只盯着最后生成的规则对不对，他们发明了一套 **“五步走评分系统”**，强制 AI 展示每一步的思考过程：

* **C0（读题）**：能不能看懂威胁情报报告里的术语？
* **C1（对应招式）**：能不能把情报对应到 MITRE ATT&CK 框架的具体战术上？
* **C2（找线索）**：知不知道去哪个日志表格里找数据？
* **C3（动手写）**：生成的 SQL/KQL 查询语句能不能跑通？
* **C4（验枪）**：最后生成的规则真的能抓到刚才埋的“坏人”吗？

**这种设计非常聪明**，它防止了 AI 靠“猜”或者“碰运气”蒙混过关。如果 AI 只会在最后一步假装成功，前面的步骤分就会暴露它的虚弱。

## 二、实验结论：真正的瓶颈在哪里？

在这个近乎苛刻的“考场”里，微软挑了市面上最火的几款 AI 选手来 PK，包括 **Claude Opus 4.6**、**GPT-5 家族**（高/中/低思考力度版本）、以及推理专用的 **O3/O4-mini**。

### 1. 行业经验 = 外挂知识库？

如果 AI 真的拥有通用智慧，那它应该不需要额外资料就能完成工作。但现实给了所有人一记响亮的耳光。

研究者做了一个关键对比：**有专业工具辅助 vs 没有专业工具辅助**。 具体来说，就是关闭那些专门为 AI 准备的 **“威胁情报查询工具”（CTI Tools）**，让它仅凭预训练时的通用知识去完成任务。

**结果惊人：**

* **GPT-5.2（中位模式）**：一旦移除了这些行业工具，它的综合得分直接掉了 **0.134**，相当于从及格线滑到了不及格边缘。
* **Claude Opus 4.6**：虽然没有具体降幅数字，但也出现了明显下滑。

这意味着什么？意味着就算是大通义千问级别的大脑，如果不给它提供**行业标准术语库、MITRE ATT&CK 框架、历史攻击案例**（即行业经验），它在安全领域的表现甚至不如一个刚毕业的人类实习生。

就像把一位天才程序员扔到一个陌生的公司，却不给他看代码规范和业务流程文档，他大概率也会写出 Bug。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNos4B0aia4gSUSdRQ3jegppylm0FbotpctzSiaz0mibyQWEhxxiad4pp5PibJVodUKubg97VZCReYm8pTwRehxQfQ7Gv3oY0YYoqFOUo/640?wx_fmt=png&from=appmsg)

### 2. 提示词与流程，决定了 AI 的下限

既然有了经验，是不是随便问问就能解决问题？另一组实验告诉我们：**不一定，关键在于你怎么提问（Prompt）**。

研究者做了一个巧妙的干预实验：给一个参数较少的小模型（**GPT-5-Mini**）塞一本“考前冲刺小抄”——也就是注入了**专家经验引导的“种子记忆”**（包含最佳实践、常见工作流、正则模板）。

**效果如何？**

* 原本这个小模型因为“不懂行”，跟大模型差距巨大（总分 0.37 左右）。
* 加上“种子记忆”后，它的性能直接提升了 **33%**，几乎追平了原版的大模型（总分 0.43 左右）。

这揭示了一个被忽视的事实：**很多时候，限制 AI 表现的瓶颈不在模型本身，而在我们有没有给它配备好“外挂”（知识）和“操作手册”（Prompt）。**

这就好比，你给赛车手一台法拉利（强大的 LLM），但不给他导航仪和赛道图（行业知识库 + 提示词工程），他跑得再快也容易冲出赛道。

### 3. 为什么云平台最难搞？

还有一个有趣的发现：在 Linux 系统上的攻击最容易抓（平均分最高），但到了 Azure 云平台环境，所有模型的分数直接崩盘。

* **Linux 任务得分**：0.585（相对简单）。
* **云平台任务得分**：0.282（极低）。

原因是什么？因为云环境的数据太分散、太杂，AI 很难把不同地方的日志拼起来看。这进一步证明：**AI 不是不会思考，而是它不理解特定环境的复杂规则。** 如果没有具体的行业场景数据喂养，它就是一笔糊涂账。

## 三、写在最后：人机协作的新范式

看了这么多枯燥的报告，我们究竟该怎么做？

未来的 AI 应用，不再是“一个人对着对话框提问”，而是 **“一个行业专家构建系统 + AI 作为强力引擎”**。

1. **沉淀行业 Know-How**：不要指望通用模型懂你们公司的潜规则和业务细节。要把 SOP、最佳实践、历史案例变成文档或记忆库喂给 AI。
2. **精细化 Prompt 工程**：就像教实习生一样，明确边界、明确格式、明确禁止事项。避免让 AI 在“零日”迷雾中裸奔。
3. **建立反馈闭环**：像 Agents of Chaos 指出的那样，AI 会在复杂交互中产生幻觉和偏差。我们需要引入外部审计和红队测试，不断修正 AI 的行为边界。

正如 **CTI-REALM** 作者所说：“当前的 AI Agent 可以为网络安全分流提供有力支持，但要实现全领域的自主加固，还需更多工作。”

这句话翻译过来就是：**AI 的智商已经够用了，现在轮到人类发挥经验的时刻了。别再用旧思维去衡量新工具，让我们一起把这块“金矿”挖深一点。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNovn5oGpotsyZ2R6xiab6BoB2seMnTCflkpsUro01ndrEM6ibD0ENAUjO3GwFcxoS0uRiaRvUJNhEWfgiaicOaicG1guHnNq6koQR9CLQ/640?wx_fmt=png&from=appmsg)

---

**参考资料：** arXiv:2603.13517v2（https://arxiv.org/pdf/2603.13517）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

APT-101

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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