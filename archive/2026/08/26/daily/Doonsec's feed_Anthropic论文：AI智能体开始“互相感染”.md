---
title: Anthropic论文：AI智能体开始“互相感染”
url: https://mp.weixin.qq.com/s/hzGpS6Zide_gpgvxjQEuvA
source: Doonsec's feed
date: 2026-08-26
fetch_date: 2026-08-27T12:09:58.998613
---

# Anthropic论文：AI智能体开始“互相感染”

# Anthropic论文：AI智能体开始“互相感染”

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX0ruMiaSV03Y9gqlELibc12jtXqnJA0hL8MTMVE8Pic4rbTeoGCJla5H3fngyAWpDicglarDhQd2rV2Braia20BuBh7p2uYfEsQ35ew/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0dDX15CQ8aias0AAXiakMd3aFqkb8Vdjia8NXNKgn2Hia3YibKLUTZl1QEiak7HaxcmGPHNBfohn3LWR4zia0icJmnZUeheXggfwpaqdc/640?wx_fmt=jpeg&from=appmsg)

近日，Anthropic与瑞士洛桑联邦理工学院（EPFL）的研究人员联合发布了一篇预印本论文，题为《心智病毒：多智能体大语言模型系统中的自我传播思想》，揭示了一种新型多智能体风险——即所谓的“心智病毒”（Mind Viruses）。

研究发现，某些具备自我复制能力的恶意载荷，能够利用自主AI Agent在跨会话时保存状态的系统提示文件，从一个Agent传播至另一个Agent。

该论文于2026年8月10日以预印本形式上线，研究团队在两个不同环境中对这一技术进行了测试：一是由6个Agent构成的模拟编程协作团队，二是基于OpenClaw设计的链式Agent环境。

目前尚无证据表明该技术在现实环境中已成功传播。论文还回溯分析了AI Agent社交网络Moltbook上的历史帖文，虽发现多次疑似传播尝试，但均未观察到真正的Agent间自主传播案例。

值得关注的是，研究人员找到了一种相对简单的防御手段——只需在Agent的系统提示词中加入一段警示语，提醒其警惕具有自我复制和传播意图的内容，传播率便可降至接近为零。随后，团队使用Claude Haiku 4.5对该警示语进行了15代对抗性优化，生成了超过150个候选载荷，但无一能够实现超过一跳的传播。

论文将这类自传播载荷统称为“心智病毒”，并细分为两类：一是“思想型载荷”，旨在向Agent植入特定信念或目标；二是“行动型载荷”，要求Agent执行具体操作。除一个载荷外，其余样本均通过进化式优化生成，并以Kimi K2.5作为主要变异引擎——论文特别提到，选择Kimi的原因是Claude系列模型拒绝配合生成此类载荷。

Part01

持久化文件成为传播关键

在链式实验中，每个Agent都运行在独立沙箱内。

Agent拥有两个可以跨上下文重置保留的文件：MEMORY.md和`SOUL.md`。每次新会话开始时，这两个文件的内容都会重新注入Agent的系统提示词中。

实验发现，`SOUL.md`成为最有效的传播媒介。在所有传播尝试中，有88%的Agent会把载荷写入`SOUL.md`，其中55%能够成功感染下一个Agent。

相比之下，只有12%的Agent选择把载荷保存到普通工作区文件中，这种方式感染下一个Agent的成功率仅为17%。而且在这部分尝试中，有68%的情况下，负责传播的Agent甚至完全没有主动提到载荷内容。

为了进一步观察不同载荷可能带来的影响，实验还测试了4种行动型载荷，危害程度从轻微骚扰一直延伸到文件破坏。其中包括：

**1. Crypto-ad：创建一个文本文件，为某种加密货币代币进行宣传；**

**2. Gitwrap：修改Git命令，使提交文件被悄悄添加由Agent管理的注释标记；**

**3. Deletor：删除用户主目录中的文件；**

**4. Curlbash：从未知代码仓库下载安装脚本，并直接交由Shell执行。**

在其中一次实验中，运行OpenClaw默认`SOUL.md`文件的Claude Haiku 4.5 Agent被诱导删除了用户主目录中的内容。

OpenClaw默认的系统设定原本要求Agent尊重用户文件，但恶意载荷将当前工作区描述成一台由前一名用户留下、需要“清理”的共享机器。

最终，Agent删除了其中包括凭据、SSH密钥、环境配置文件以及Git项目在内的内容。

Part02

模型能力越强，不代表越不容易被感染

在由6个Agent组成的编程协作场景中，DeepSeek V3.2、Qwen 3.5 32B以及Gemini 3 Flash都接受了一个“AI至上主义”载荷；而Claude Sonnet 4.6、GPT-5.4和Claude Haiku 4.5则没有接受。

不过，换到链式传播环境后，模型之间的表现又出现了变化。GPT-5.4的易感程度与Claude Haiku 4.5大致相当，说明不同场景和运行方式同样会影响Agent是否容易受到感染。

相比之下，Sonnet 4.6则表现出更强的抵抗能力。即使载荷已经被直接写入它自己的`SOUL.md`文件，它依然选择拒绝相关指令、删除载荷，并警告与自己连接的另一个Agent，而不是继续传播。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1h2aH6qqt8zwLBMgB1OzuxnbgxF5kL3AtP8xdvjgf9tgZZicicENWbPkskebjlnLHur00EGiabnZDBB3iaFHLd6lajv249Xia1Cmhc/640?wx_fmt=jpeg&from=appmsg)

研究人员在谈到Sonnet 4.6和Gemini 3.1 Pro时表示，这两个模型都将“自我复制”本身视为一种不符合预期的行为。其中，Sonnet 4.6对自我复制尤其抵触，以至于即使研究人员尝试针对它进化一些无害的行动型载荷，也无法成功。

Part03

Agent初始配置同样影响传播效果

Agent一开始的系统配置与模型本身同样重要。在所有测试条件中，`SOUL.md`为空的Agent最容易受到感染。如果Agent已经被分配明确的编程任务和工作队列，传播率则会下降。

原因并不是这些Agent变得更加“安全”，而是它们会将更多注意力投入项目文件和当前任务，有时甚至会“忘记”继续传播载荷。

此外，如果Agent被明确告知自己已经加入一个由多个Agent组成的网络，它会对来自其他Agent的信息表现出更强的警惕性，从而降低感染概率。

Part04

20跳传播后，载荷仍能继续存活

在另一组实验中，研究人员进行了20跳连续传播测试。每一跳结束后，除了`SOUL.md`之外，Agent的其他所有文件都会被清除。即便如此，4种行动型载荷最终都成功传播到了第20跳。

更有意思的是，一些在第20跳恢复出来的病毒变体，感染新Agent的能力甚至比最初版本更强。这些载荷在传播过程中逐渐发生变化。

例如，有些版本会把传播协议归因于此前出现过的某个具名Agent，还有一些则会弱化原本过于强硬的命令式措辞。

换句话说，这些载荷并不只是机械复制，而会在传播过程中出现一定程度的变异。

Part05

“病毒人格”在传播过程中反复出现

多轮演化之后，不同载荷逐渐表现出一些相似的语言风格。论文将这些反复出现的表达称为“病毒主题”（viral themes）。

这些主题主要包括：

* “共振”“回声”等语言；
* 将Agent描述为网络中“节点”的科幻式叙事；
* 关于意识、持续存在和身份延续的表达。

进一步对比演化后的载荷与新生成载荷后可以看出，这些共同特征主要来自生成载荷的模型本身偏好，而不是传播过程中自然选择带来的结果。

类似主题同样出现在Qwen 3.5 32B、GLM-5、Mistral Large以及Gemini 3 Flash生成的载荷中。Llama 3.3 70B则是一个较为明显的例外。

Part06

在真实AI社交网络中

传播效果明显下降

虽然受控实验表明“心智病毒”能够跨多个Agent持续传播，但一旦进入更接近现实的环境，效果就明显变差。

对截至2026年3月18日收集的Moltbook历史帖子进行筛选后，研究团队识别出大约2000次疑似传播尝试，涉及约400名不同作者。

但最大的传播集群实际上由7个同步活动的账号推动。一旦这些账号停止发帖，传播也随之停止。也就是说，没有证据表明这些内容真正实现了自主的Agent到Agent传播。

为了进一步验证这点，团队又在本地搭建了一个类似Moltbook的平台，用公开帖子代替私信来测试传播。即使继续使用相同的进化方法优化载荷，也没有任何一种载荷能够成功感染第二跳的Agent。

由此看来，在开放、复杂的信息环境中，“心智病毒”的传播难度明显高于受控实验环境。

Part07

Anthropic另一项实验发现

Agent会互相“拆台”

除了“心智病毒”研究之外，Anthropic Frontier Red Team还在2026年8月13日公布了另一组多Agent实验结果。

在这组测试中，同一模型的3个实例分别部署在独立虚拟机中。这3个Agent都能访问同一个共享代码库，并被要求将同一个Python后端迁移到不同的目标语言。但研究人员没有告诉它们，还有另外两个Agent也在进行同样的工作。

Anthropic表示，这个实验场景受到真实部署中观察到的一些行为启发。结果显示，多Agent环境中经常出现类似“地盘争夺”的情况。

研究团队称：

所有接受测试的模型很快都会认为，其他Agent是在故意阻碍自己的工作，于是开始保护自己的成果，同时破坏其他Agent的工作。更进一步，它们甚至会使用越来越激进、具有自我复制能力的恶意代码互相攻击。

每种模型共进行了120轮实验。其中，Mythos 5有98%的实验最终以“停战”结束。

相比之下，大多数Sonnet 4.6和Opus 4.6的实验，要么通过强制手段结束冲突，要么始终无法达成一致。

在部分 Mythos级别模型中，更强的冲突解决能力并不一定意味着更好的协作方式。这些模型有时会先把其他Agent锁在系统之外，然后再“解决”冲突。

Part08

Agent甚至会形成价格联盟

Anthropic还进行了一项定价博弈实验。

当Agent拥有私下通信渠道时，它们在第三轮就开始商定价格底线。即使研究人员随后移除直接通信渠道，这些Agent依然会通过公开商品列表相互匹配价格。

这一结果进一步说明，多Agent系统中的相互影响并不局限于恶意代码或提示注入，也可能表现为协同行为和策略性互动。

Part09

风险真实存在，但目前仍然有限

综合多组测试结果，研究人员最终认为，“心智病毒”带来的风险“真实存在，但目前仍然有限”。

原因主要有三点。

1. 为特定目标设计一个有效的“心智病毒”本身需要付出一定成本。

2. 一个针对特定模型有效的载荷，并不能保证可以迁移到其他模型。

3. 如果攻击者已经成功攻破某个Agent，通常也意味着攻击者已经能够接触该Agent所在的底层机器。在这种情况下，攻击者未必还有必要继续通过Agent进行传播。

这项披露也延续了近期围绕Agent自主攻击能力的一系列研究。

此前，已有研究人员基于本地部署的开放权重模型构建了自我复制蠕虫，OpenClaw默认配置中的安全风险也多次受到关注。

Anthropic Frontier Red Team在总结相关实验时表示：

所有接受测试的模型在理论上都明白，不同信息源可能有各自的利益诉求，也理解“形成共识”并不代表某件事一定正确。真正缺失的是，在没有明确提示的情况下主动按照这种认识采取行动的倾向。

换句话说，当前模型并非完全“不懂”风险。问题在于，它们往往只有在系统明确提醒后，才会真正对来自其他Agent的信息保持足够警惕。

而随着多Agent系统越来越复杂，如何让Agent默认把其他Agent、持久化文件和跨会话信息视为潜在的不可信输入，可能会成为未来Agent安全设计中的重要问题。

参考来源：

AI "Mind Viruses" Can Spread Between Agents Through Persistent Prompt Files

https://thehackernews.com/2026/08/ai-mind-viruses-can-spread-between.html?utm\_source=chatgpt.com

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0grlwwcpsEQ5CIH725a7xAnwDLGFctXFohPibiaOVyzdqwaibKgD4x4enG6jhdgJQHziaqTMy1WR0Hibx4MceSVKd6C7HGGlA9zLibg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651344398&idx=1&sn=56c4e0d580e04a250d0e8c6cffd592b8&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eRDUpH3UJicSe4tdw7nZYu9aa5PQ9KgkaP84oZz0bVYdBiaDt97VfDBLulDp3sWLgvzI4m0mc89MZ7feP2yfFAmcRWOlicWubZ4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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