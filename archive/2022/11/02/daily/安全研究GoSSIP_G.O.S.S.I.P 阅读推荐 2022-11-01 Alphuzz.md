---
title: G.O.S.S.I.P 阅读推荐 2022-11-01 Alphuzz
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493107&idx=1&sn=9acb47c1cb6bb1d8053ff9548f8bc19b&chksm=c063cb2af714423cf4238fd13b735bc178c1a3829938b9476bf363ad47f779a8c08c0f77f145&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-11-02
fetch_date: 2025-10-03T21:33:09.715074
---

# G.O.S.S.I.P 阅读推荐 2022-11-01 Alphuzz

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3FlIchwJ4tzoPbK6RxLKsia20ib6Q1ibd8cg86Mh3f1djL5nLuaNiaPNsMbw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-11-01 Alphuzz

Yiru@WHU

安全研究GoSSIP

十一月的第一篇论文推荐是来自武汉大学赵磊老师团队和[加州大学河滨分校尹恒研究组](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247483824&idx=1&sn=3e2e02cfdd8b0fa247fe6de2d7860c96&chksm=c0602f69f717a67f366e998e612fd1670d9972238f591e67240b6502efe0c9cea6d47314aa7b&scene=21#wechat_redirect)合作并投稿的关于种子调度的最新研究工作Alphuzz: Monte Carlo Search on Seed-Mutation Tree for Coverage-Guided Fuzzing，目前该工作已经被ACSAC 2022录用。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3FcQOjDtQeD0h3Juvialjo2ZICBOxPxk4xZZgENHEXs4BbomKgKSKQSZQ/640?wx_fmt=png)

**研究背景**

种子调度，即在种子池中选择出一个种子作为后续种子变异的基础的这一过程，在基于代码覆盖率的模糊测试中十分重要。其重要性主要体现在选择出的这个种子决定了模糊测试探索程序状态的方向。具体而言，种子调度选出一个种子后，模糊测试沿着它覆盖的路径，通过种子变异尝试覆盖其邻接的未覆盖路径。不同的路径引导模糊测试探索不同的程序代码区域。

研究人员提出了很多种子调度策略，通过设定的指标来衡量种子的价值，并且选择最优的种子。比如：AFL倾向于选择小的、执行时间短的种子；FairFuzz优先选择覆盖低频分支的种子；AFLFast给覆盖低频路径的种子更多的能量，EcoFuzz优先选择新生成的种子以及变异过的贡献高的种子。

然而，已有的种子调度策略往往只关注单个种子的特征，忽略了种子之间的关系对模糊测试的影响。在这篇文章中，作者论证了种子之间的变异关系对种子调度的影响，并基于种子之间的变异关系提出了一种新的种子调度策略。

**提出的方法**

**1. 种子变异树**

在这篇文章中，作者发现种子之间的变异关系对种子调度十分重要。正如前面所说，种子变异可以视为沿着种子覆盖的路径探索其邻接的未覆盖路径。因此变异关系可以体现种子覆盖的路径之间的关系。作者利用种子之间的变异关系，构建一个“种子变异树”。树上的每一个节点表示一个种子，每一条边表示变异关系。如种子t1经过变异生成种子t2，那么在树中，t1就是t2的父节点。这样构建出的种子变异树可以视为程序执行树的一个近似。在同一个子树下的种子代表了程序执行的一个方向，不同的子树代表程序执行的不同方向。图2展示了不同的种子调度策略的示意图。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3F7LUwgBkOY6Zz0jdORzwKJDyLLZNjcQiaY9nPRIIOMrBBOvgP7zgtYXw/640?wx_fmt=png)

在种子变异树中内部节点有两个角色，一方面表示一个种子，另一方面表示以它为根节点的子树。因此，作者将内部节点按角色拆分，在内部节点下加一个变体子节点，即该子节点代表原有的种子，而内部节点表示一个子树。树型结构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3FZ7042sNPJXaO2TYcaWEIqxnYRF3fS8YGy06O4Fdq6r2pYqia4rWyc4A/640?wx_fmt=png)

**2. 种子调度策略**

种子变异树上的种子代表了程序执行的不同方向，如何在不断增长的种子变异树中快速搜索出最优的种子、如何随着模糊测试的演化更新种子变异树、如何平衡种子调度的探索和开发是种子调度面临的挑战。

作者提出了一个基于蒙特卡洛树搜索的种子调度策略，并设计了基于UBT算法的种子分数计算方法。种子调度的整体流程如图4所示：每轮从根节点开始向下搜索，计算当前节点的子节点的分数，选择分数最高的子节点继续向下搜索，每次选择分数最高的节点，直到选中的节点为叶子节点，本轮种子调度结束。选中的种子经过变异生成的有趣测试用例根据种子变异关系增加到种子变异树中，然后从新添加的节点到根节点的反向路径上的所有父节点更新被选中的次数以及覆盖的分支，以指导下一次种子调度。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3FE3Q0wXlE7vb0qfrAM5DNvMn8mD1oQQL8fBdUImPCTej9ibZZeibkJtHw/640?wx_fmt=png)

3. 种子分数计算方法

作者基于UCT算法设计的种子分数计算方法如下。公式的左边表示种子已有的平均收益，公式右边表示种子的潜在收益。具体而言，   是种子或者一个子树中所有节点覆盖的所有分支或者一个叶子节点覆盖的所有分支，  是种子选中的次数，  是父节点选中的次数。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3FZaC0NHLDmzgQBnticpcCDLK5ibiasLOrLDgdBwFRftl6osZ5tm8lRKg7g/640?wx_fmt=png)

**实验评估**

作者分别在AFL和AFL++的基础上实现了两个方法原型工具Alphuzz和Alphuzz++，并且在三个数据集（CGC，UniFuzz以及12个real-world程序）上开展实验。实验中用于比较工具有两组，一组是基于AFL的工具，包括AFL，AFLFast，FairFuzz，EcoFuzz，另一组是基于AFL++的工具，包括AFL++和AFL++-HIER。

作者从代码覆盖率、漏洞发现数量、吞吐量、参数k的影响等方面开展实验。部分实验结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3FCGopWInZM1wxkhPCnYAbmOoyoMibJBE0bDOxl0DWAlvu2Y6f0Fqibw2g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3FpRIbuibBcqQibhSYMichLTpsCgGKLVbuqnstURxsTTEalfvvUiceDibv5UQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3FywicibZuBNM5uy7m8Cicjg3lxZ4EHibrL1m1TqNMzSNPs3ndOfRibObgASw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ezgv0zEoQ9VzibId1cJnT3F00sS6YTPbZgpia7kgjnN7Quw8XRdjQEFqoGhhDd2ibPBjtBJB1xCP4aQ/640?wx_fmt=png)

**总结和讨论**

Alphuzz和Alphuzz++在代码覆盖率、漏洞发现数量方面相比已有工具都有提升，并且对吞吐量和参数k进行了讨论。此外还发现了三个新的CVE。但是实验部分对于参数k的讨论不够全面，还需考虑不同的运行时间、程序特点、测试目标等因素。

论文获取请联系武汉大学赵易如同学

联系邮箱：zhaoyiru@whu.edu.cn

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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