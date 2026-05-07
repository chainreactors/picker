---
title: G.O.S.S.I.P 阅读推荐 2026-05-06 DARPA 拖拉机简史
url: https://mp.weixin.qq.com/s/thM_py_h0AJnqVNN9ZdWfg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:24:53.718881
---

# G.O.S.S.I.P 阅读推荐 2026-05-06 DARPA 拖拉机简史

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolXANLAgRcKsRocCfXhDOLnpfwW8Op8boicibwZ8AED1xshapHnDnyOhss66alEKLEss0icoUms8EeTaOG0oAyOMRkSTQrB3nO93Tw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-05-06 DARPA 拖拉机简史

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolWmf43m5ibXiawMUdzQiaS1RjKBBic8Yjjc9rSTicLHLjlSRWIoJoJf3Ih41NapqBZnlRtewwbuLEn1dKyQoFeCbicpsQt1jUnDAT96A/640?wx_fmt=png&from=appmsg)

有一本叫做《乌克兰拖拉机简史》的书，在俄乌战争之前估计听说过的读者不多，而之后估计也都是一些喜欢政治军事的网友去“误读”然后弃坑，其实它是一部黑色幽默文学作品，喜欢文学的读者可以去自行搜索和阅读~

今天我们介绍的内容其实和文学以及乌克兰没什么关联，纯属蹭一下这本书的~~热~~冷度。那今天的推荐是来自NDSS 2026的keynote speak环节，由Dan Wallach（应该是之前在Rice University，现在去了DARPA？）给大家做的报告*Solving the Memory Safety Problem, Once and for All*

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolX4JyQ9TlHGr2icP2qAnmibkNY1ib2CP08YmAjE7NClWTBv6tAACNktH3l0aCb9hm5tRxtjRr8BxQOOBtYYjuWTiaLNC3BNY67HoIU/640?wx_fmt=png&from=appmsg)

这个报告之所以和《乌克兰拖拉机简史》有那么亿分之一的关联，是因为DARPA在2024年启动了一个“拖拉机”项目——即“TRanslating All C TO Rust”（缩写为TRACTOR）的项目。不知道还有没有读者记得公众号的一篇很古老的推荐（额，其实也就是5年前，不过那时候还属于前AI时代，一转眼恍如隔世，）《[G.O.S.S.I.P 学术论文推荐 2021-12-13 Translating C to safer Rust](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247488177&idx=1&sn=96e907bee360b7bf00806a40a384fc02&scene=21#wechat_redirect)》，在那一期的推荐中，我们介绍了一个叫做`c2rust`的工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolWfUA4EVWBnRraEdiaiacwRLiaL3PP9eP4ZuyribiaWBXrzUXCslYcibibuy5xztrn18Q5du4m1TaQX4dk1uS7LUub64pGTOhuYkXPvb4/640?wx_fmt=png&from=appmsg)

而DARPA和Dan Wallach教授肯定是看了我们的公众号（~~很有可能，Dan Wallach教授此前的研究论文也cite了我们的工作~~ 不要脸），于是在2025年6月启动了TRACTOR项目，意在推动研究人员去开发把现有的C代码翻译成Rust代码的自动化工具。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXPdBNJCGgBBGIbxGEMWP1HJhsNuqL0UftDInu52FmgghWdjb1rmlzNnf62lSzxntzM6oLyCnnCKicMwRqZ3tG566OUGQpktS0c/640?wx_fmt=png&from=appmsg)

可能你要问，为什么是Rust？因为DARPA此前进行了各种尝试，下面这一张幻灯片（响起了夏奇羊的try everything）里面列出来了之前的各种安全加固技术路线，当然每个路线估计DARPA也投入了不少钱，那也不差再拿出来一笔钱资助下一个新idea（嗯，Rust）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolVdd8QjCguGXLxyWNxoZS44pZm8AoYuCVaGy4J35M1CYeyUcBnoGiapt23mlGnqGX2Vm4GDVMuMRQ0KaZILKQWMicNQHxkeZvlh4/640?wx_fmt=png&from=appmsg)

和之前DARPA的项目类似，TRACTOR也是让不同的team来互相竞争（嗯，我们在国内管这个叫做“~~养蛊~~赛马”），而不同的队伍可以使用不同的技术路线，有的用机器学习主导，有的队伍则是走传统的程序分析路线。参赛的六支队伍有的来自大学（华盛顿大学、耶鲁大学、威斯康星大学），有的来自企业（Intel、Galois、Aarno Labs）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXzgbcaARICriaNIzdRSJ56T0eeFqGriaQwqGQrZHiakuHVAK3ibFwobwdaNEEhiaZeE86WiavDLUCsHRN9HEiasj1J0K9Tqm7oOa3fgs/640?wx_fmt=png&from=appmsg)

这个项目进展到现在，可能大家最关心的问题（也是现在网络上论战最多的点，大家对AI的态度也可以分为“降临派”、“拯救派”和“幸存派”）就是**到底人类还有没有必要去研究代码翻译这个事情**。很多人都觉得，现在反正把代码直接扔给AI让它改就完了，Anthropic都已经开始营销大模型直接写编译器、写浏览器和写操作系统了，区区一个C翻译成Rust代码的任务有什么值得研究的？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUv284icr44ytaaFtEKCo6UxxVVjLic0yJoBNN2eNb9AlNzumtZe7kUFIpLiaPjOnzfC3wH4h0HOqPr1QFn1iaFYia2h9iaYTryYA2Mk/640?wx_fmt=png&from=appmsg)

实际上今年2月，TRACTOR项目出了个中期报告，大家可以去GitHub上看看这个报告的PDF，里面关于各家队伍的技术细节和实际的测试（测试是请了MIT Lincoln Lab作为第三方测试机构，https://www.ll.mit.edu/r-d/projects/translating-all-c-rust-tractor-benchmarks 还准备了专门的benchmark）

> https://github.com/DARPA-TRACTOR-Program/Reports/blob/main/First\_TRACTOR\_Evaluation\_Report.pdf

从下面这个正确性评估来看（注意这里评估用的是GPT 5.0，而且没有什么特别的环境，就是给两次prompt机会，第一次是要求它翻译，第二次是把报错信息反馈给它让它改），其实那个最naive的C2Rust的效果反而很有竞争力，这就有点尴尬了。。。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolWDdLDNSlMULlId0j5UFNE2Q7eUhkUSWmP6zHNTlibpXKbKCGKphMu5j5v1bvCFubBRlF7ehFKqSsB32UPc9YwtBichRSicoojZ5o/640?wx_fmt=png&from=appmsg)

评估报告里面有很多关于各家技术出错的细节（比如谁容易在翻译阶段出错，谁在运行阶段出错更多），感兴趣的读者可以去看看。我们只简单介绍下翻译后的Rust代码和原始C代码的性能对比，从下面的表格可以看出，基本上翻译后的这个性能开销都在可接受的范围（最多也就不到30%）。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXu6r2b6lGticDfN9ONxkEG4U1DHCELjBRYyiaueN5ylwibca7AnQDckhY5wr7fXUTZMar5gxsm7DJfgKoRIPn91ucLOhqpIxqsdg/640?wx_fmt=png&from=appmsg)

不过（某些技术路线）翻译后的Rust代码有一个问题：内存占用开销会大大增加，例如LLM翻译的代码，最极端的情况下会比原C代码使用的内存增加137.64倍……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXIPBCCNsiaTUIcd2amXpYqhPibqJDLBuOhsY19YoAe1notnsSmZQhib4uicRYSj41KXYAtX7DPMAg8hJ6LWX7HwlHJL3B9tTR2nV4/640?wx_fmt=png&from=appmsg)

那么，究竟C代码翻译成Rust代码更好，还是说在LLM时代，人们又一次找到了银弹——直接用AI去检测代码漏洞（嗯，不需要夏奇羊来唱try everything了）~~~

---

> Slides：https://www.ndss-symposium.org/wp-content/uploads/NDSS-2026-Keynote-DWallach.pdf
> TRACTOR项目主页：https://www.darpa.mil/research/programs/translating-all-c-to-rust

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