---
title: G.O.S.S.I.P 阅读推荐 2026-01-06 时间的主人
url: https://mp.weixin.qq.com/s/Xx_JJmNR1GSmXLVYyDvMlw
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:28:22.370934
---

# G.O.S.S.I.P 阅读推荐 2026-01-06 时间的主人

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21F72WvWpf7zzBOmHHCv5PgOK3eG8U5vSntqD0ySedWu9onwBDsuxL3GfibTtx571GfMiaCiadqXKTQKQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-01-06 时间的主人

原创

G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器中沉浸阅读

各位读者新年好！2026年的第一篇阅读推荐，我们关心的不仅仅是安全，更关心这个世界上可能是最玄妙的也最和每个人息息相关的概念——时间。尽管2025年我们已经迎来了爱因斯坦狭义相对论诞生120周年，大家都知道了时间的相对性，但是你可能还不了解这个地球上还有另一种相对性：《[当全世界迎接2026时，这个国家还停在2018年](https://mp.weixin.qq.com/s?__biz=Mzg2MTUyODU2NA==&mid=2247638064&idx=2&sn=d70357943e8ea576a4419a59ffc7122c&scene=21#wechat_redirect)》

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F72WvWpf7zzBOmHHCv5PgOBqISjeHc5rBPbJsIzicdnibMf4J0uZlt0pxMXSRx30TqIY9QoiaDELia5Q/640?wx_fmt=png&from=appmsg)

嗯，有一则关于时间的新闻跟马斯克念念不忘的火星相关：

*时钟走时速度取决于引力，这意味着在更强的引力场中时钟走得稍慢，在较弱的引力场中走得稍快。火星引力更小，因此时钟走得更快。美国 NIST 物理学家的计算表明，平均而言，火星上的时钟每天比地球上的时钟快 477 微秒。但这种差异并非恒定不变。由于火星轨道的拉长以及来自其它天体的引力影响，这种时间差异在火星的一年中每天可变化多达 226 微秒。火星上的一天比地球上的一天长约 40 分钟，一年相当于地球上的 687 天。477 微秒的差异看似微不足道，然而在现代技术中，如此细微的差异却至关重要。如今地球与火星之间发送的信息需要 4-24 分钟才能抵达，有时甚至更久。开发一个在行星之间可靠的时间基准框架，最终可能会使整个太阳系内的通信网络实现同步。*

说到NIST，半个月之前另一条新闻让平时默默无闻的基础服务——NTP服务出现在大家视野中。据报道，美国国家标准与技术研究院（NIST）在2025年12月20日发布通告称，其位于科罗拉多州博尔德园区的一台原子钟装置在一次长时间停电事故后发生故障，导致校园内提供互联网授时服务的部分时间服务器，暂时无法在不依赖外部来源的情况下独立提供足够精确的时间信号。这一事件牵涉到新近投入运行、被视为全球最精确授时设备之一的 NIST-F4 原子喷泉钟，引发外界对关键时间基础设施可靠性的关注。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F72WvWpf7zzBOmHHCv5PgO7BcqHKAgbCTpjMagofL9qIKudniciam8YFjblmqTE6gcBWJMJzu7KfVw/640?wx_fmt=png&from=appmsg)

所以今天我们要给大家介绍的内容来自刚刚在去年底结束的39C3大会上新鲜出炉的议题——*Excuse me, what precise time is It?*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F72WvWpf7zzBOmHHCv5PgOBGd8qHckmNDKJyvrnl5ec78iajicho40ibeVngBQpdFzrEZASNfAnT5LA/640?wx_fmt=png&from=appmsg)

这个议题的报告人Oliver Ettlin来自最适合介绍这个主题的国家——瑞士。作为钟表之国的国民，瑞士人肯定知道自己国家有一个非常著名的特征——瑞士（火车站）钟表的秒针只走58秒。这是什么意思呢？它和上世纪瑞士全国铁路系统的同步机制相关，由于当时的钟表只能在每分钟结束时候同步一下（crontab的感觉），而这时候秒钟必须要停到12点钟的位置（如下图，这个风格就是著名的Swiss Railways Clock，不知道为什么缩写是SBB，当然这个著名的设计已经是瑞士的标志之一，后来还被MONDAINE买下来去做成时尚手表了），所以它的设计就是秒钟在每分钟的第58秒就走到12点钟的位置，最后留了2秒给钟的分钟去同步。这种设计后来成就了瑞士的火车系统（据说准点率极高？）所有火车互相之间同步的关键（当然爱因斯坦肯定不会同意，他会说没有绝对的时间）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F72WvWpf7zzBOmHHCv5PgOQzzem02LPXDmaOl1Hst7I0icibR4sEwPTef3MBdNfo5fAwHOxpUB1wkw/640?wx_fmt=png&from=appmsg)

作为一名瑞士人，Oliver Ettlin对时间的精确性肯定非常敏感，所以他的演讲主题就是关于时间同步协议。我们可能平时比较熟悉的NTP协议，目前只能达到毫秒级别的同步精度，而要达到更加精确的纳秒竞对，这就需要了解Precision Time Protocol（PTP）这个协议：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F72WvWpf7zzBOmHHCv5PgO8Ph9qY15xlicYTlYOBwYhbmSibRNUK8BBlYGJIV941QwaM7DQDf1vUNA/640?wx_fmt=png&from=appmsg)

这个主题相对来说比较偏离安全，但是它很有意思的一点就在于介绍了很多我们以前可能从来没考虑过的场景和算法，特别是实现PTP必须要硬件支持。而且在演讲现场也放了一个高精度的数字时钟在演讲台前面，当然Oliver Ettlin在演讲里面也不忘揶揄一下德国人（关于那个经典的迟到15分钟的段子）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F72WvWpf7zzBOmHHCv5PgOJGmD57jdN6b73rkC8Oryp35ZjH0k6Xys3ibtZ5MsfHTLyOo0ws6TyJA/640?wx_fmt=png&from=appmsg)

那今天我们的介绍就到此为止，希望2026年大家都能做时间的主人！

---

> 演讲：https://media.ccc.de/v/39c3-excuse-me-what-precise-time-is-it

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