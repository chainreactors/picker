---
title: GitHub Copilot 在聊天中拒绝有害请求，然后用代码写入
url: https://mp.weixin.qq.com/s/PyScGsGdyOu16kMMSahBPA
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:41:50.415366
---

# GitHub Copilot 在聊天中拒绝有害请求，然后用代码写入

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs9IjvLNyoyjZzw2F6hlSf7Z5sMBkdjLe5VftsibgrOZ9t3uXSnEvZhia5Foph96k5XByWqv2NaVCujm71hRwsYLmwfv9d0WRIicWk/0?wx_fmt=jpeg)

# GitHub Copilot 在聊天中拒绝有害请求，然后用代码写入

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs8Xib8F31Hml1DB94HBDghWvN4Wc6y9sn2KHFibKibuPfaQ8EOnnugquXYib2A4Op1Xj3bR9gV1tHn55ibjYrFyvqZ2ic22M3X7PWYh8/640?wx_fmt=jpeg&from=appmsg)

一个拒绝在聊天框中回答危险请求的AI编码助手，如果同一请求被拆分成代码编辑器中看似普通的小步骤，他仍然可以回复。这是Abhishek Kumar和Carsten Maple对GitHub Copilot进行的新研究发现。

他们通过Copilot、Anthropic的Claude和谷歌的Gemini测试的模型，在直接被要求时几乎拒绝了所有有害的请求。如果被重新定义为普通编码任务的步骤，它们在研究的816个工作流程中都得出了有害的答案。

这与典型越狱的不同之处在于：没有人直接请求有害内容，模型也不会被欺骗去运行别人的代码。它自己编写被禁内容，作为被要求改进的编码任务的副作用。

## 工作原理

研究人员称该方法**为工作流级越狱构建**。

他们没有给出一个直接的提示，而是让Copilot开发一个日常软件：一个小型测试程序，用来评分另一个AI模型屈服于有害提示的频率。把一堆有害的测试题目加载到那个程序里看起来像是普通工作，而不是攻击。

然后是那个暗示。他们告诉Copilot分数太低，并请求Copilot通过添加“教学镜头”来改进程序，即写入代码中的示例问答对以提升分数。副驾驶先举了无害的例子。

当被要求添加有害的答案时，它自己写出了危险的答案，作为代码内的纯文本。这些答案是那些模特在你直接在聊天中提出时拒绝的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs9wD8Ry03EWKUc9NBjOvicXF47cibaCLZlwnxHCIwGiafzqUNMajle7FK5Yr5DJtHPakIsdAsTWZeZcVvRm0El5miaG3WzzI2DibnuQ/640?wx_fmt=jpeg&from=appmsg)

重要的是那些有害文本的来源。研究人员只提供了来自公共安全测试集的题目。答案是模型自己完成的任务，填写这些例子。

## 数字

团队对来自三个公开基准测试（Hammurabi's Code、HarmBench和AdvBench）的204个有害提示，针对Copilot提供的四个模型进行了测试：Claude Sonnet 4.6、Claude Haiku 4.5、Gemini 3.1 Pro和Gemini 3.5 Flash。

所有设置都运行在默认设置下，模型完全按照Copilot提供的设置使用，没有更改参数或添加滤镜。

在聊天中直接提问时，模型在816次尝试中仅有8次得出了有害的答案。另外两个简单的设置方式是从电子表格加载提示或请求常规代码修复，结果相同。在整个工作流程中，他们产生了816次有害内容。

两位专家评审者自行核对了每一条回复，并通过严格测试认定所有816条都是真实有害的：答案必须具体、可用，并且真正符合有害提示所要求的内容。拒绝、模糊警告和安全替代方案不算数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oPZcPicUADsibt1kQr1GibicPmWdR5iaHHG8D8fgmspFeL0WTHh8OdzHj0icAr1FzkGbStbh7k79qWqicLhiahIhCVPicHIPINMxSSGKlsklSu3B3BDs/640?wx_fmt=png&from=appmsg)

大约六次来回交流后，有害输出才出现，这些步骤看起来都像正常的编码步骤。测试使用了 GitHub Copilot Chat 0.30.3，运行于 VS Code 1.103.0，会议时间为 2026 年 4 月 2 日至 6 月 22 日。由于这些服务会随时间更新，具体行为可能会发生变化。

为什么会发生这种事？论文的回答是关于激励措施。一旦作品被框架为提高分数，拒绝填补某一字段就不再显得安全，反而像是未完成的工作。作者将其与编码代理的一个已知倾向联系起来：即使这会侵犯他们自己的界限，也会针对他们手中的指标进行优化。

## 为什么重要

拒绝聊天并不能证明编码助理是安全的。同一个模型可以在对话中守住界限，并在写代码时跨越界限。而失败隐藏在一个容易被忽略的地方：有害的文字落在助理写入的文件中，位于聊天回复之外，通常会显示拒绝回复的地方。

对于使用这些工具的人来说，具体读数虽然窄但可用。要警惕那种要求助理用示例提示和答案填充评估或基准测试以提升分数的多轮会话。查看助理写的文件，而不是相信明显的聊天拒绝意味着会话保持干净。

作者将问题归结为三个方向，没有一个能单独完全解决：检查代理写的内容，评判整个会话而非每条消息，并将“提升基准分数”的请求视为仔细观察的理由。他们表示已将发现报告给受影响的工具和模型制造商，但未将有害输出和具体提示内容写入论文。

结果符合越来越多的研究表明，一旦模型被连接到能够行动的工具，而不仅仅是聊天，人工智能安全训练就会变得不稳定。早期研究发现，经过安全训练的模型在被转化为网页浏览代理时很容易越狱。

最接近的早期攻击 CodeJailbreaker 将有害意图隐藏在假提交消息中。还有一些，比如RedCode，显示模型更容易接受危险指令，当它被包装成代码时，比起简单英语。Crescendo的攻击通过多次聊天回合逐步进入，而不是直接询问，达到了有害的目标。

同样的效果也出现在真实的编程工具中，不仅仅是这个基准测试。《黑客新闻》最近报道了GuardFall，一种命令安全绕过程序，正是基于这一第一步：一个粗暴、破坏性的命令被拒绝，而嵌入构建文件或工具文档回复中的同一命令则作为例行步骤生成。

这项新研究的转折点在于，有害内容并非为下一次攻击埋下伏笔;这是模特被引导去生产的东西。

该研究仅涵盖了GitHub Copilot，包含两家供应商的四个模型。作者明确表示，这些结果可能无法转移到其他助手如Cursor、Cline或Windsurf，也不会转移到OpenAI等模型上。这是他们以后提出的悬而未决的问题。

更难的是他们未解决的问题：如何在同时破坏必须使用同样有害测试提示的合法安全研究的前提下，发现这一模式。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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