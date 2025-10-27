---
title: G.O.S.S.I.P 阅读推荐 2022-10-24 Chaff Bugs
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493017&idx=1&sn=b3f37d90937c4ec2c1fd5d1c063ce540&chksm=c063cb40f7144256b9f6624d34bfb3267198d7c8a995faa66feab30328f1d6af08353d324d0d&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-10-25
fetch_date: 2025-10-03T20:47:49.719237
---

# G.O.S.S.I.P 阅读推荐 2022-10-24 Chaff Bugs

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21Ec1rQ4MVvaT6sZMGPmuulw39FyQv6JSeeqOzMIeC8y1cuibB19N50XPe2Mh5ylb5vwQJylGh7ibuoQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-10-24 Chaff Bugs

原创

胡正浩

安全研究GoSSIP

今天是程序员节，程序员最喜欢什么？当然是写代码啦！但是写代码又总是会出bug怎么办？没关系，让我们来看看安全研究人员是怎么通过加入bug来保护代码的（可不是教大家学坏哦~）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ec1rQ4MVvaT6sZMGPmuulwpKQ9pA4rM6CFTiayZ09om0ic9ickYhia49rDxZDQ2ic3t9NHYEAbNDRrZ2A/640?wx_fmt=png)

但凡谈到软件安全的防御，⼤家⼀般总会想到怎么找bug和修 bug，或者在操作系统中加⼊⼀些安全缓解措施，使得攻击的条件更加苛刻。然⽽在防御研究中，⼤家经常会忽视攻击者在漏洞分析过程中所⾯对的挑战，即：攻击者或安全研究⼈员常常需要⼿⼯分析并确认每个 bug是不是可以利⽤，⽽这个分析过程⼜极其耗时⸺每个bug常常需要上⼩时，甚⾄可能数天才能完全确认。在这篇来自RAID 2022的论文Towards Deceptive Defense in Software Security with Chaff Bugs中，研究人员（第一作者胡正浩就是我们今天的投稿人，也是曾经在G.O.S.S.I.P生活学习过的老朋友）提出了⼀种全新的安全防御⼿段：Chaff Bugs。不仅不修 bug，反⽽在程序中⼈为的加⼊成百上千个不可利⽤的 Chaff Bugs。当攻击者尝试进⾏漏洞挖掘时，他们会⾸先被⼤量的 Chaff Bugs淹没，⾃然也没法分出时间和精⼒去确认程序中真正存在的漏洞。

当然，构造 chaff bugs也需要满⾜三个条件才能达到预想的防御效果：1）必须确保不可利⽤；2）要能轻易地被攻击者发现，⽐如通过 Fuzzing或（⾁眼）静态分析，很快就能看到有bug；3）有⾜够的分析难度，即使发现程序⾥有bug，攻击者也不能在短时间内判断出这个bug是不是可以利⽤。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ec1rQ4MVvaT6sZMGPmuulwhupiaXFCYmwibrRRU66RqXjDbJTc6fQpe3OnAzMkwZvF3OtKH2qKyWaA/640?wx_fmt=png)

**威胁模型**

在chaff bugs的实现过程中，我们也考虑过开发者的感受，毕竟正常的开发者⼤概都会⽐较难以接受往⾃⼰的程序⾥加更多 bug的想法，因此我们也特别限定了我们的 threat model和我们认为可以运⽤的场景。

⾸先我们预设了开发者通常都会有程序源代码，并且也可以控制编译环境的配置。其次，我们认为软件 crash并不是个很严重的问题。尤其是⽐如⼀些多线程的服务程序（e.g. Nginx，Web browser），单个线程 crash并不会导致整个服务崩溃。最后，在这篇论⽂⾥，我们并没有对 Chaff bugs 和程序中真实存在的 bug进⾏区分。让 chaff bugs更⾃然的融⼊整体程序的代码⻛格也是我们的 future work之⼀。

**自动化**

Chaff Bugs沿⽤了作者团队发表在IEEE S&P 2016的相关工作——LAVA（https://ieeexplore.ieee.org/document/7546498）的设计，通过对⽤户输⼊进⾏动态污点分析，进⽽找出在各个程序点可控的变量，并且基于这些变量来构造只能在特定输⼊下才能被触发的 Bug。下图的代码示例是⼀个基于我们系统⾃动化插⼊的⼀个 Bug样例，其中 lava\_set函数会在⽤户输⼊中选取⼀个 4字节的 int值来有选择地触发 bug。在代码示例中我们可以看到，只有当那部分⽤户输⼊中存在 0x6c617661这个 magic值时才会触发 bug （基于栈上变量的越界写）。在 Chaff Bugs的设计中，我们也分别实现了栈溢出和堆溢出两类 bug作为原型设计的模版 bug。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ec1rQ4MVvaT6sZMGPmuulwfL0RvamxibhnQZ4f3zzcHsZtp0FicicpBOmlJ1NkPKvicgl3FUuvQuibzKw/640?wx_fmt=png)

**Chaff Bugs的不可利用性**

Chaff bugs的核⼼之⼀就是确保我们插⼊的 bug是不可利⽤的。为此，我们分别设计了两种策略来保证这点：策略⼀是通过对恶意数据进⾏限制（overconstrain dataflow），从⽽确保 Chaff Bugs中的栈溢出和堆溢出所覆盖的数据（或指针）是在⼀个安全的范围之内。下图的代码示例是⼀个简单的 chaff bug例⼦，示例中我们在程序的不同位置分别插⼊了不同的代码⽚段⽤来对恶意数据分段进⾏限制（如 Dataflow部分所示，DUA为攻击者可控的恶意数据），最终我们将恶意数据限制成 32位的NULL值，并在插⼊的 Chaff Bug中将其转化为⼀个 32位的空指针引⽤。即使尝试触发这个 Chaff bug，攻击者也只能触发⼀个不可利⽤的 crash。策略⼆则是通过引⼊⼀个新的变量（unused variable）来构造溢出。当 Chaff bugs 被触发时，我们构造的内存溢出最终只能覆盖到这个新引⼊的变量，所以这个 bug既不会导致 crash，也不可能被⽤来进⾏攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ec1rQ4MVvaT6sZMGPmuulwfMNiaJ1C3TN8ovbBibv2QIF2oIRtjZ31g4xgl8VYiayD7L4Suahyibv38Q/640?wx_fmt=png)

**数据流混淆：增加（⼈⼯ /⾃动化）分析难度**

我们的第三个任务是要增加攻击者分析 Chaff Bugs的难度。毕竟 Chaff Bugs的终极⽬的是想要浪费攻击者的时间，如果攻击者能够轻易地分析出 Chaff Bugs是不可利⽤的，那样也⽆法达到我们预想的防御效果。因此，我们⼜在不可利⽤策略的基础上，额外设计了两个数据流混淆策略。

对于 over-constraint dataflow，我们把对于恶意数据的限制代码拆分成多个部分，并分散在程序的各个地⽅，从⽽使得攻击者难以通过单个的限制代码来判断恶意数据是否可以被⽤来构造利⽤。不仅如此，我们还⽤ opaque constant以及⾮线性的运算来进⼀步混淆数据流的限制，即使攻击者想⽤ solver来解也可能⽆法顺利解决。

另外，对于 unused variable，我们设计了另⼀个策略，通过在函数调⽤链中加⼊额外函数参数来制造⽆⽤的数据流分⽀。如下图所示，当 Chaff Bugs被触发并溢出了 unused variable时，我们将这个 unused variable进⼀步赋值到我们新添加的函数参数。攻击者在分析这个 bug时需要回溯整个函数的调⽤链来确认这个变量确实没有在程序的其他地⽅被⽤到了，从⽽也增加了分析难度。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ec1rQ4MVvaT6sZMGPmuulwe1ibHJO2yajFVynLWV9K6lSLHmoyvamDQzTDiaaow4pZZiccOSQIib8yYg/640?wx_fmt=png)

**实验**

在实验设计中，我们在 Nginx，file，和 libFLAC三个程序⾥各插⼊了不同数量的 Chaff Bugs进⾏测试。我们分别统计了每个程序中可以插⼊ Chaff Bugs的数量及其在各个程序中的分布情况，并且针对不同的⾃动化漏洞挖掘以及分析⼯具，Chaff Bugs能否有效地误导攻击者等等。更详细的数据和实验分析可在论⽂中（https://dl.acm.org/doi/abs/10.1145/3545948.3545981，10月26日之后在线公开可访问）找到。

**Bonus**

作者举办了⼀届公开的 ChaffCTF（chaffctf.com），其中选取了⼀些⼩型的程序，并在其中加⼊了数⼗个到数千个不等的 Chaff Bugs，并制作成了 CTF题⽬。虽然⽬前⽐赛服务器已经下线，但感兴趣的朋友可以在这⾥找到所有的⽐赛题⽬以及完整的 writeups：
https://github.com/HighW4y2H3ll/chaffctf\_chal

同时，作者公开了制作⽐赛题⽬的 toolchain以及 Chaff Bugs系统源码：

https://github.com/HighW4y2H3ll/chaff

⼤家也可以⾃⼰动⼿构造⾃⼰想要的 bug，然后插⼊到⾃⼰喜欢的程序中去。

---

最后，欢迎大家关注本周即将在岛国塞浦路斯上的第二大城市（考考你这是哪里？）召开的RAID 2022学术会议，尽管前往此地的难度堪比回国，但是我们的一作还是义无反顾地抵达了美丽的地中海，期待他的精彩报告！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Ec1rQ4MVvaT6sZMGPmuulw0QtiaiaYBUOV0Gcs1Fw0iag5iaYNhT2VfpnshR53CIKqibtFav7Dm1dBKNQ/640?wx_fmt=png)

论文地址：https://dl.acm.org/doi/abs/10.1145/3545948.3545981

预览时标签不可点

阅读原文

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