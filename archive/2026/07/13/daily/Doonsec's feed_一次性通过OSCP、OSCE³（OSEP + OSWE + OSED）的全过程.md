---
title: 一次性通过OSCP、OSCE³（OSEP + OSWE + OSED）的全过程
url: https://mp.weixin.qq.com/s/gu4d5gdt_TXcBu_wMa1CvA
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:44:36.940355
---

# 一次性通过OSCP、OSCE³（OSEP + OSWE + OSED）的全过程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zVE7oia7FCWibxER03OUxLDkXR6G2YdTXricFC2DibQXb3bkhdnoMoK9DRjuFibX7yfZT35obqXBCstibAzv44rNiaxWh7aa1BF0fBp2cxicVmvicMIw/0?wx_fmt=jpeg)

# 一次性通过OSCP、OSCE³（OSEP + OSWE + OSED）的全过程

OffSec
OffSec

谷安培训

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zVE7oia7FCWibHxyJtuL8sVibIFESxwOJklzAb9CicOPIMJ1XFQ4Balashnz89wdE3Qmp1ib3PX5dfKDjYYVEEmYNpWx6TdwMiaOA1CLrcszHkujY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU4MjUxNjQ1Ng==&mid=2247526316&idx=1&sn=eb61e590ae52b374cfd0c091f39bf765&scene=21#wechat_redirect)

距离我拿到OSCE³的证书已过去将近2月，一直想总结一下这四门考试，这次是个机会。回顾通过OSCP、OSEP、OSWE、OSED 的全过程，所有成绩均是在首次尝试中取得的。

**0****1**

**PEN-200 & OSCP**

刚开始时，我对性安全领域所知甚少，完全不清楚前方的道路将需要付出多少努力。之所以投身 OSCP 认证，很大程度上是受到了宣传的吸引。我听说过这门考试的难度，也读过许多人通过考试的故事。

PEN-200是OffSec非常具有代表性的渗透测试课程，也是考取 OSCP/OSCP + 认证的官方配套课程，它教会了你进攻性安全的基础知识。与 300 级别的课程相比，相当直观明了。

我的学习建议很简单：熟练掌握所有教材内容、完成所有实验练习，并尽可能多地解决各类挑战性实验题目。你越是努力学习，通过考试的可能性就越大。

经过近三个月的学习后，我尝试了 OSCP 考试，而它比我所预想的要难一些。开始考试后，一上来情况就颇为棘手，但我迅速调整了心态，并开始迅速积累分数。到了第 16 个小时的时候，一件我未曾预料到的事情发生了。我重启了机器，结果丢失了所有笔记以及之前运行过的所有命令。我并未对此加以理会，而是继续前行。到了深夜时分，仅剩几小时时间的时候，我偶然发现了考试中最大的突破点。我从头开始重新整理了自己的笔记，并在第 22 个小时时停止了操作。我睡了两个半小时，随后撰写了一份长达 105 页的报告。整个过程耗时约 16 个小时。

![](https://mmbiz.qpic.cn/mmbiz_png/zVE7oia7FCW8Qm0kyuucicyWq0OC8oqibuONAezBSlhKhKXG3aqsjAswR6X439LXVWBrUgC5WEE54fAYHibSVOv9ALHMWO2dn0zAicR04zyKQXBM/640?wx_fmt=png&from=appmsg)

**0****2**

**PEN-300 & OSEP**

PEN-300内容扎实。它涵盖了反病毒规避的基本要点，同时涉及了一些低级别的 Win32 API 技术：通过进程注入、DLL 注入和进程空洞化技术直接将壳代码加载到内存中。目前许多此类技术已被广泛侦测到，但该课程教授的是真正重要的技能——即编写自己的工具以突破现代反病毒软件和 EDR 的防护。具体的技术方法或许在实战中可能无法奏效，但其背后的概念依然适用，并且作为规避手段的基础而言，它表现得相当出色。

它还能触及 Active Directory 系统。最棒的部分在于挑战实验室。当你将所有内容串联起来，亲眼目睹你的载荷绕过防病毒软件和 AppLocker 时，那种感觉简直令人难以置信。

我一边全职工作一边学习 PEN-300，前后花费了约 4 个月的时间才参加了考试。

考试对我来说，像是一场恶战。我一开始表现得比以往任何时候都要出色，仅用预期时间的一小部分便成功夺取了旗帜。然而，到了大约 8 小时的节点时，一切发生了改变。我距离及格分数近在咫尺，却突然遭遇了瓶颈。这是我所经历的所有考试中最艰难的一段历程。在 14 小时的节点上，我睡了几个小时，醒来后依然毫无进展，又漫无目的地耗费的 11 个小时。到了凌晨 3 点，我终于发现了自己此前所忽略的关键点。我对自己浪费如此多的时间于如此简单的事情上不能释怀，甚至此前还曾想过要放弃。

我非常想按下“结束考试”按钮。我不断告诉自己，我本应该满足于自己已有的 OSCP 证书。但我克服了内心的犹豫，一旦下定决心，分数便再次迅速提升。到第 25 个小时时，我已取得了及格成绩。我的报告共有 199 页！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zVE7oia7FCW8W76I7iayuBQJxbfF1hm9ZOgicBcxIiaKy5vWXvzib9oQ3I8NxVmLgn3ove8DiblNjq3ibCQD5mViaHY2aO3DlJ53gGyzaDEziaGgGlY4/640?wx_fmt=png&from=appmsg)

**0****3**

**WEB-300 &  OSWE**

在 OSEP 结束后，我没有休息，而是直接投入到 OSWE 中。学习 OSWE 花费了我大约 5 个月的时间，而到此时我的动力已开始逐渐减弱。网络编程对我来说始终是一个薄弱领域，为了克服缺乏动力的问题，我使用了五分钟启动法：打开电脑，打开课程资料，连接 VPN，然后决定是学习还是学习多长时间，迫使自己站到起跑线上。

OSWE真正赋予你的是一种深刻的理解力，而这正是我在实际工作中最为倚仗的能力之一。你对事物的工作原理及原因理解得越深入，就越能更好地识别、滥用并串联运用这些知识。到这时，我已经能够将来自OSWE和OSEP的诸多理念融入实战渗透测试中，以获取单个发现。

我顺利通过了所有 WEB-300 挑战实验室的测试，期间从未寻求过帮助。有些题目相对较为简单，但我烈建议您些时间自行解决它们。

OSWE考试自己都难以置信。我花了大约 36 个小时才达到及格分数线，期间几乎没有休息，最终生成的报告篇幅最短，仅有 92 页。如果论课程和考试难度课程难度，我个人认为是8/10。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zVE7oia7FCW95ytKgOXdRWfXo2ibvMEvExOjia8erpVNK4zszfkrvBcrq6o6p6245g8ETXmoRZQSfgtLfDia7mzWOmUTYtMXTexSJtY3L4OGL14/640?wx_fmt=png&from=appmsg)

**0****4**

**EXP-301 & OSED**

EXP-301是这四门课程中最为严苛的。在完成 OSWE 后，我短暂休息了一段时间，随即开始学习 OSED，但几乎立刻便遇到了障碍。这门课程要求你能够阅读汇编语言，而我此前从未阅读或编写过哪怕一行汇编代码。但是，即便信念为零也要坚决执行。

真正开始学习后，疑虑开始逐渐滋生。有几次早上，我萌生了放弃这门课程的念头。要学习的知识内容实在太多，要深入理解的内容也过于庞杂，而我渴望以一次顺利的通过为目标所具备的控制力，似乎又显得遥不可及。如果当时你让我估计一下自己成功的几率，我会说低于 5%。

几乎可以肯定，在我自认为准备就绪之前，我就已经做好了准备。而那5%的把握更多地与我的紧张情绪有关，而非我的实际技能。因此，我不再试图去预测结果，而是尽可能地投入时间学习。

对我来说最困难的部分在于逆向工程。如果没有扎实掌握汇编知识，我的 OSWE 直觉就会接连产生误报。我不得不放弃这种方法论，重新开始。遵循输入步骤，逐步进行探究。弄清每个函数的功能、其使用方法以及它可能如何被串联到原本并非其本意用途的某个环节上。

转折点在于 DEP。当我开始将 ROP 工具串联起来以绕过 DEP 时，整个局面终于豁然开朗，我的逆向工程能力也随之显著提升。实验室里的环境颇为艰苦。刚开始时，我一度怀疑自己为何要从事这类工作。到了第三遍时，整个过程实际上已显得颇为可控。

如有需要，你也可以选择有经验的培训机构获得指导。系统化的学习路径和导师反馈有助于提高备考效率。

经过约 8 个月的学习后，我满怀信心地步入考场，准备迎接我这辈子最艰难的考试。然而，我却在 11 个小时内取得了及格的成绩。这无疑是我在 OffSec 参加的考试中最轻松的一次。尽管我仍连续超过 30 个小时未眠，但考试的难度几乎让我感到有些失望。因为，我一路都抱着最坏的预期。最终的报告仍长达 223 页，这更多地源于旧有习惯而非考试本身的要求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zVE7oia7FCWicsco8MRuPXkeqNeic4GoErn1ic0YbvIkuviaqCU5voIP4SrKcFllLgVS9T4gzBwaRjaR2edCDDawNDeGutamCuicRSoNia0zu8TL1E/640?wx_fmt=png&from=appmsg)

如果非让我说这门课程的难度，我认为课程难度：9/10，考试难度：5/10。

**我想告诉所有初入行者的话：**

即刻开始吧！如果你打算考取一门认证，请尽快付诸行动。要比你以为自己需要的那样更加努力地学习。

制定好计划！提前决定好你打算学习多长时间、考试期间会睡多久以及会休息多少次。然后尽力按照计划执行。

切勿轻言放弃！不要提前结束考试，也不要拒绝给自己尝试的机会。

经历了四门课程、四场考试以及大量凌晨五点的闹钟提示后，OSCE³ 课程终于结束了。这是迄今为止我所经历过的艰难挑战之一，同时也是为数不多的愿意从头再来一次的尝试之一。

![](https://mmbiz.qpic.cn/mmbiz_png/zVE7oia7FCW8e3mnZk3mvxEDibESuUwicfSf7Bhn5d6ibDGn60WE6P6scgXEibF2f2viaMgcEpWhyyaLRicyjByRnlODmCBzblKpmSD9n1HZkIF0UM/640?wx_fmt=png&from=appmsg)

近期我并无计划再获取另一项 OffSec 认证，但我的学习之路远未结束。在这个领域里，我还有很多东西想要学习、构建和破解。倘若我日后再参加 OffSec 考试（或许会考虑OSAI、OSEE）我将继续全力以赴！

![](https://mmbiz.qpic.cn/mmbiz_png/zVE7oia7FCW8QgfnvPo54qZfFNNPrfDhTolwgkJRbTiconcHDMkWjOyAZicLMAsjOmg5hbaxwa68iah1ZxibSXAvvcabevacYS5KIaqqicuqY2icpA/640?wx_fmt=png&from=appmsg)

探索 OffSec 系列认证课程

折扣LAB | 申请免费试听学习 | 早鸟价优惠

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zVE7oia7FCWibIXlEHpPbfmvHpicsuxYyJzZlKkWcpD6AFE7vPaJdHefr52FRZIIUVOWknib3NOSepcFcydo9BV9CUKvsRVArFqbp5D3pD7GD0c/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n8GpemzlNRRPCPicjnsMiaP3hsxsAuIwfnzj8lWQkiaADkpE5KsicnRuFJToeuJEQD7Coe6CribkeC3Oenr3FAnEGyQ/0?wx_fmt=png)

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