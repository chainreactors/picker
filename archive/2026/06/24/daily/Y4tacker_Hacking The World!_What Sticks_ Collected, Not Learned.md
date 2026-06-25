---
title: What Sticks: Collected, Not Learned
url: https://y4tacker.github.io/2026/06/24/year/2026/06/What-Sticks-Collected-Not-Learned/
source: Y4tacker:Hacking The World!
date: 2026-06-24
fetch_date: 2026-06-25T06:08:39.122283
---

# What Sticks: Collected, Not Learned

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. What Comes In](#What-Comes-In)
2. [2. When It Gets Wider](#When-It-Gets-Wider)
3. [3. People As Source](#People-As-Source)
4. [4. What Gets Built](#What-Gets-Built)
5. [5. Where the Flywheel Breaks](#Where-the-Flywheel-Breaks)
6. [6. When FOMO Hits](#When-FOMO-Hits)
7. [7. What Actually Stays](#What-Actually-Stays)
8. [8. Less, But Mine](#Less-But-Mine)
9. [9. What Works Now](#What-Works-Now)
10. [10. Build To Delete](#Build-To-Delete)
11. [11. Not Just Too Much](#Not-Just-Too-Much)
12. [12. What Sticks](#What-Sticks)

# What Sticks: Collected, Not Learned

Y4tacker

2026-06-24 (Updated: 2026-06-24)

[Java](/categories/Java/)

[Fastjson](/tags/Fastjson/), [Java](/tags/Java/)

接上篇分享 PPT 的 Plugin ([https://github.com/Y4tacker/codex-ai-ppt)补一下分享的内容，反正都不是什么私密东西](https://github.com/Y4tacker/codex-ai-ppt%29%E8%A1%A5%E4%B8%80%E4%B8%8B%E5%88%86%E4%BA%AB%E7%9A%84%E5%86%85%E5%AE%B9%EF%BC%8C%E5%8F%8D%E6%AD%A3%E9%83%BD%E4%B8%8D%E6%98%AF%E4%BB%80%E4%B9%88%E7%A7%81%E5%AF%86%E4%B8%9C%E8%A5%BF)

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305299_4b2f8cf8-63dd-49e0-9cdc-065d664c2c6a.png)

最开始，我并不打算讲这个，在最终决定这个选题之前，我大概花了一个月时间研究了很多方向。本质上，它们都是我最近感兴趣、正在探索的一些东西和技术

其中有三个选题我本来是真的打算讲的

一个叫 “代码，还是那些代码”，大纲其实都想得差不多了，但看着最近大家分享代码、工程相关的内容已经很多了，我有点想换换味道

另一个叫 “Skills 的自进化？”，这个题听起来很有意思，也确实能展开很多论文、框架和实现思路，但做到一半，我发现它对通用场景的意义不大，本质上只是把原来优化文本和 PROMPT 的思路换汤不换药

还有一个叫 “当 MCP 遇见 SKILL”，这个是我前几天捡起来在研究的东西，想法是我去年年底想到的只是一直没做实验，MCP 与 SKILLS 融合形态，将 Tools 与 Skill 通过 MCP 同源分发，但这个十几分钟就讲完了不太合适，后面写成文章再分享好了，当然还有一些个人原因想挑战下自己不想讲纯技术文

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305317_a77f5907-2153-41e8-92b1-58f033f154ab.png)

否掉这两个之后，我开始想，有没有一件事是大家都在做、也几乎所有人都绕不开的

想来想去，我发现确实有一件事：

怎么获取信息，以及怎么处理信息

尤其是在今天，人人都在讲自动化，讲个人信息飞轮的时刻，我越来越觉得，这里面有一个很容易被忽略的问题：

真正留下来的，往往不是我们收集过的信息，而是我们在筛选、拒绝、使用信息时形成的判断

这次分享也算是我过去一年围绕 “信息” 折腾之后的一次复盘，这一年里我一开始以为自己要解决信息获取问题，后来才发现，我真正需要解决的是注意力分配的问题

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305350_2035e3c8-1d37-4f13-b8b6-b3bf8ce4c317.png)

## What Comes In

先从最早的信息输入讲起，刚开始接触 AI 的时候，我发现蒸馏别人的知识是一种很快的学习方法

那还是 chatbot 时代，信息环境和现在很不一样，信息量没有现在这么夸张，且高质量内容也比较集中

从 LLM 基础知识，到大模型商业进展，再到应用案例，很多内容基本都能从几个高质量公众号、文章和推特里看到，那个阶段很多账号也还处在起号，信息量少但密度很高，主要是很有人味

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305374_f3b0444e-0eab-4efe-a969-88499d1f6bdc.png)

对我来说，这段时间是最近几年里再次让我感到学习最快乐的一段时间，更早是小时候刚开始接触网络安全的时刻

* 一方面，是因为之前每天搞网络安全确实会有点累，这个累不完全来自强度，而是来自单调重复。很多东西做久了之后，新鲜感会变少，知识带来的刺激也会变弱。
* 另一方面，是因为大模型刚出现的时候，每次迭代都能带来一种久违的耳目一新的感觉，新的能力、新的边界、新的玩法不断出现，学习是很有反馈的，而且是特别快！

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305393_d2aafccc-ac94-42d5-8c93-381f27fa3073.png)

* 那个时候我什么都想看，什么都想试，从大模型的预训练、后训练、Agent、RAG 甚至 Transformer 相关的东西，我都在接触。只要看到一个有意思的项目，就想拉下来跑一下；看到一篇讲得不错的文章，就想顺着里面的概念继续往下挖，这一阶段，随意的输入本身就会带来源源不断地正反馈

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305401_0d0a2e4f-065c-44e8-a974-c2a7bb66b5a0.png)

## When It Gets Wider

后来，事情开始慢慢不对劲，大模型还在高速发展，但针对模型本身的玩法越来越少了，我能感觉到从大模型本身获得的新鲜感开始下降，而是因为很多基础知识我已经刷过几轮了。后面再看到的很多内容，本质上是在不断巩固和复习，不同文章换一种说法，不同作者换一个比喻，新瓶装旧酒，底层讲的东西并没有变太多，新鲜感开始从模型本身转移

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305415_cb8cf45e-8fb4-4710-bea9-3c51afc6d9f4.png)

这时候我意识到，不能只看大模型本身，如果一直只盯着模型结构、训练流程，很容易陷入一种局部循环，模型当然重要，后来在 Function Call 出来以后我的注意力变成了大家正在模型之上建立什么？安全领域在怎么用它？产品团队在怎么设计它？不同公司在怎么改造自己的工作流？

也就是说，我的关注范围开始从大模型本身扩展到大模型的生态

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305424_898d6938-0722-4688-905c-f13e95c235b1.png)

但问题也正是在这个时候出现的，当我不再只看模型本身，问题就从 “学什么” 变成了 “去哪里学”

当时还没有现在这些成熟的 Deep Research 产品，我也不知道到底应该从哪些网站、哪些社区、哪些渠道系统性地找到自己想要的东西

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305434_bb6cd04d-9d27-4174-87c4-cd13f99ace7c.png)

更关键的是，我其实也没有那么清楚自己想学什么，我只知道应该关注 AI 安全，应该关注大模型应用，应该关注一些新的产品形态，但 “应该关注” 并不是一个清晰的问题，它散播一种模糊的焦虑

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305460_c71e8ab9-95a6-4259-ba70-08796c6d07e2.png)

## People As Source

Btw: 后面一年的经历也证明了确实这个还是最好的，就是人越来越忙了没时间思维风暴

刚好在那个阶段，我在外面认识了一些志同道合的人，大家都对大模型很感兴趣，而且分布在不同领域，每个人关注的东西不完全一样，有的人看模型，有的人看产品，有的人看开源项目，有人喜欢当喷子

后来我们组成了一个社群，这个社群最开始只有一个作用：分享关于大模型的各种知识

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305496_b9a9c88e-1a76-465a-a2ac-6c66ec2f0580.png)

在一段时间里，最好的信息源不是网站，而是一群分布在不同领域、愿意互相分享的人

初期效果非常好，那时候人的规模不算大，基本一天也就几十到上百条消息，群里会出现各种信息和链接：公众号文章、论文、GitHub 项目、产品体验，也包括大家自己的新奇想法

那段时间，每天饭点或者下班之后，看看群里大家在聊什么，其实已经能获得很多有价值的信息

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305505_f3cd162d-9aea-4b12-aa2f-1bcb663d6881.png)

这是一种很自然的信息分发方式，不是算法推荐给你，而是通过一群和你有相似兴趣、但关注面又不同的人，把信息带到你面前，每个人都带着自己的问题和视角进入这个环节。一个人看到的东西，可能正好补上另一个人的盲区，人在这个阶段先成为了信息入口。

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305517_71662bde-a193-4d35-8f7e-4a0068ae4f90.png)

但随着群成员规模不断扩大，问题也开始出现

首先是水平参差不齐，人一多之后，大家处在学习的不同阶段对 “什么是高质量信息” 的理解也会不一样，有的人分享的是一手资料，有的人分享的是二手解读，有的人只是看到标题觉得很厉害就转了进来；

其次是水群很难避免，很多时候大家并不是故意降低信息密度，只是交流一旦变多，就一定会混入大量上下文、情绪、闲聊和重复表达，信息密度也就开始下降

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305528_690d9ab4-3d46-4df0-894c-f318c3214c6a.png)

最后是沉淀困难，群聊确实是一种很适合即时交流的载体，但它并不适合长期检索。一个东西当时你看过、讨论过、甚至学过，但过了一两个月之后，如果你想重新系统地找回来，基本只能靠记忆里的几个关键词去群聊搜索，又或者说自己之前有意识地保存了下来

这时候我意识到一件事：就算信息被学习过，也应该被存下来，因为群聊里的学习，只是经过了你，没有真正留在你这里

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305537_e988c39d-7441-4730-bfe3-968e055bbd6f.png)

## What Gets Built

于是，我开始为信息建系统

当时的解决方案其实很直接，通过微信 Hook 插件创建一个微信小号机器人，大家在群里分享内容时，只要按照一些关键词前缀和固定格式发消息，机器人就能把这些内容抓下来，抓下来之后，后台处理识别，再通过大模型做一些简单分类。这个系统的目标很简单：先让信息不要散掉。

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305545_32d388a3-3633-40f5-8cc9-ab6ef461030c.png)

分类也不复杂，主要记录平台、标题、内容、时间，以及 AI 提炼出来的要点总结

这样一来，信息存储的问题基本就解决了，有了结构化的信息之后，日报、周报、月报功能也很自然地出现了。每天发生了什么，一周有哪些值得看的内容，一个月里某个方向出现了哪些变化，都可以被整理出来

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305605_1e54ee89-64e7-4241-a54d-0e1f9799b2a1.png)

但这个系统依赖人的积极性，只要大家愿意分享，它就有价值；一旦大家不分享，或者分享质量下降，它就会变弱。一开始通过群成员的分类分级做了多个群来缓解，但我们也知道，不可能永远靠人来收集信息，我开始逐渐从被动走向了主动，在这个过程中我也逐渐意识到，从社群里挖掘信息，本质上只是一个过渡阶段，它真正的意义应该是在我没有形成自己的长期主观判断之前帮我观察：大家关心哪些方向？有哪些长尾但高质量的信息源？哪些内容会引发讨论？哪些内容只是看起来热闹？正好在做微信 Hook 的时候积累了一些爬虫的经验，这个东西很自然而然地推了下去

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305612_61ee3903-4983-4a04-8c2f-75003bd28224.png)

后面我们就开始把绝大多数信息平台整合到一起，做了一个专门的爬虫，这个阶段，我开始把信息处理拆成几个维度

1. Deep Research：纵向钻取，追求深度和系统性，需要完整的知识体系和上下文
2. Wide Research：横向扫描，建立知识地图，快速发现关联和盲点
3. Point Research：高效获取可执行方案，偏向 Just-in-time learning

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305621_0e2469fb-8409-4193-b685-301ae405adce.png)

围绕这三个方向，我构建了一个所谓的信息飞轮

围绕这三个点，逐渐地我构建了一个所谓的信息飞轮，信息进来之后，会被分类、总结、归档、检索、再加工，最后服务于具体问题，并形成一个反馈循环；

某种意义上，它实现了 “信息找人”。至少它让信息不再完全散落在各个角落，也确实解决了一部分 “存” 和 “找” 和 “自动迭代” 的问题，后面很长一段时间里我都沉迷于迭代这套系统 (真累啊 00)

BTW: 当然其实这段时间里我还顺便用过各种各样地免费地知识库产品，毕竟能有现成地就懒得自己造轮子，但是他们生态都或多或少地比较封闭，并且只能解决其中的一小环节，这里不展开了毕竟不是产品调研文

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305636_b5afedf0-c541-4883-a068-c2cc733b5f93.png)

直到后来我发现，问题又不对劲起来了

## Where the Flywheel Breaks

从直觉上看，这套逻辑非常顺：

* 既然信息太多，那就把它们存进知识库
* 既然人找信息效率低，那就用向量检索和大模型帮我找
* 既然原文太长，那就让 AI 总结
* 既然我记不住，那就让系统替我记住

但真正用下来之后，我发现真正难的不在存、找、记，而在判断这个信息真的有没有用，毕竟越往后信息量越来越大了，到后面我慢慢就应付不过来了，有以下问题

![image.png](https://watcha.tos-cn-beijing.volces.com/prod/user/uploads/10005770_1782305653_8022637c-1468-4aca-a428-5ff79fa24e33.png)

1. 存下来，不等于属于我：知识飞轮最容易制造的一种错觉是，只要我把它存下来了，它就属于我了 (收藏等于学会)。但实际上不是。它只是被收集了，不是被理解了。它存在数据库里，不代表存在我的判断里；它能被搜索到，也不代表能在我需要的时...