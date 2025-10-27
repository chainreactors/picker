---
title: G.O.S.S.I.P 阅读推荐 2024-11-13 K-Hunt++
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499190&idx=1&sn=72d25d43880140476f83ce17b377284e&chksm=c063d36ff7145a79aba46a958d8f81d9a2a3fc180d0652150aec9c510d0a9651039e591800d9&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-11-14
fetch_date: 2025-10-06T19:19:38.960872
---

# G.O.S.S.I.P 阅读推荐 2024-11-13 K-Hunt++

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GCMemxmWKH3bK4nFyJiasl3QaOfENnMRpiahWjOL5ibOjAyU6sDdYh4qia6LerywfDV6fvAcg0mQ0CIw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-11-13 K-Hunt++

原创

G.O.S.S.I.P

安全研究GoSSIP

> 世上有两类论文，被人诟病的（然后改进的）和那些没人读的。-- 白岩松

最近突然发现G.O.S.S.I.P之前的一篇研究论文（K-Hunt @ CCS 2018）被人吐槽且改进了，而且人家还非常有心——论文的标题继承了我们之前的研究工作。除了作者之外，可能我们是全世界最有资格推荐这篇论文的，那今天必须要来介绍一下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GCMemxmWKH3bK4nFyJiasl3KwMAlKc2Vib679W3dO5dzV1IXHtekhtLZjMHq6wDJ5NDlQZJxLXMP4A/640?wx_fmt=png&from=appmsg)

这篇论文是对我们的CCS 2018论文提出的自动化密钥分析系统的改进（关于之前的工作，可以参考 https://www.inforsec.org/wp/?p=2961 的相关中文分享）。首先人家上来就吐槽说K-Hunt在GitHub上的开源项目（基于Intel PIN开发的一套分析组件）不够完整，当然这个里面确实有一些配置文件是需要手工去设置的（比如要记录的地址范围，要分析的特定指令以及相关数据），而且由于后续该项目也进入了和企业合作的范围，因此就没有精力去特别维护开源项目了，只有在交通大学来修IS308《计算机系统安全》课程的同学能够享受到指导哦（硬广，欢迎大家选课）。

接受批评，然后我们来看看作者对我们的工作进行了什么改进：作者指出，K-Hunt的一些启发式的检测特征（例如关注memory buffer的长度）可能会导致检测失效（这个我们后面会说，论文的观点不太对）；对于某些会把key和data都当成数据、用同一个函数进行处理的情况也会失效。所以作者提出了一套更为复杂的流程（如下图），也就是K-Hunt++的工作流程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GCMemxmWKH3bK4nFyJiasl3gPKb59IbNTAwwcHURaPONrib8K3rOxKvvPUd2TcS7J1lGZ9dO5pJCRQ/640?wx_fmt=png&from=appmsg)

从这个流程可以看到，K-Hunt++ 一开始还是沿用了K-Hunt的思路，即先要在二进制代码中定位所谓的“crypto block”，也就是那些负责密码算法操作的代码基本块；然后，K-Hunt++ 提出了更为复杂的定位“key loading block”这一设计；在接下来识别那些和crypto key相关的操作指令时，K-Hunt++ 增加了4类新的特征；最后K-Hunt++还增加了一个调试步骤来输出key（感觉有点画蛇添足，直接在代码插桩分析的时候输出也行吧）。下面我们来具体点评下这些步骤。

首先，第一个步骤没什么好说的，和K-Hunt的思路是一致的。到了第二个步骤，K-Hunt++ 在实现细节上写得有点草率，大概的意思是不光要关注所有crypto block，还要扩展地关注涉及到crypto key加载的代码基本块——key loading block，所以要执行一个数据依赖性分析；这部分在K-Hunt里面是没有考虑的，K-Hunt只关注数据是怎么从用户（或者外部）的输入传播到最后的使用，至于为什么要考虑这个，是因为K-Hunt++在第三个阶段（识别key）的时候，把K-Hunt那个比较粗糙的function-level的数据传播分析改成了一个细粒度的数据污点分析，但是这个其实就引发了一个问题，也是我们前面说的作者吐槽得不太对的地方。

在K-Hunt原来的设计中，正是因为使用了function-level的数据传播分析，只关注一个函数的输入和输出，所以不会被函数内部的一些局部的buffer干扰，而K-Hunt++ 虽然使用了细粒度的数据污点分析，就不可避免地要去处理各种函数内部的临时buffer，这可能也是K-Hunt++ 为什么要在第三步加入了更多的启发式分析来帮助判断到底哪个buffer才是key的原因？总之，到底是K-Hunt++ 这个设计更好还是K-Hunt原来的策略更优，要留给读者去思考啦~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GCMemxmWKH3bK4nFyJiasl3QawzeiakMsslML1cAbjgdWRGqr4lMuVIjyF2mo62FP7nibRqoWjF25gA/640?wx_fmt=png&from=appmsg)

补充一下，这篇论文是它所发表的会议（CheckMate Workshop https://checkmate-workshop.github.io/ 一个关注软件调试分析，特别是通过这类手段恢复软件中的秘密信息的小会）上的另一篇论文*Tools and Models for Software Reverse Engineering Research*的姐妹篇，作者在另一篇论文中介绍了`TREX`逆向工具箱，可以帮助进行内存搜索、密钥恢复等任务，K-Hunt++也是它的其中一个插件，大家可以去访问一下（见文末“代码”链接）。

无独有偶，在刚刚进行的r2con 2024会议（https://rada.re/con/2024/， 参见我们的公众号好友“非尝咸鱼贩”的介绍【[r2con 2024 将在油管同步直播](http://mp.weixin.qq.com/s?__biz=Mzk0NDE3MTkzNQ==&mid=2247485501&idx=1&sn=8e6a61f3552037f16d216cde74b483ee&chksm=c329f6cdf45e7fdb75560259a3d50a15b6bd9296370a6a9108ffda5834367940ba69cbe93fb7&scene=21#wechat_redirect)】）上，也有一个相关的议题，大家可以配合服用，效果更佳！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GCMemxmWKH3bK4nFyJiasl30kz8Xz4E6icHOJOUlcMPF5SyAgZXAZibh086kdxgs0dqDfTGNl0XWdOA/640?wx_fmt=png&from=appmsg)

最后，感谢远在万里之外有人关注我们的研究（想到研究成果真的会被人仔细挑刺，觉得还蛮酷的）~

---

> 论文：https://thomasfaingnaert.be/publications/Faingnaert\_2024\_KHuntPP.pdf
> 代码：https://github.com/csl-ugent/TREX

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