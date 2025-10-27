---
title: G.O.S.S.I.P 阅读推荐 2023-03-22 无人机坠落
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494633&idx=1&sn=6c7f6a982b261ebb4a664ec404854ee2&chksm=c063c530f7144c26572138206ea046b03f66a321d2d1d3506d9f78ea96fd09460626dcb3a0ec&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-23
fetch_date: 2025-10-04T10:23:36.312183
---

# G.O.S.S.I.P 阅读推荐 2023-03-22 无人机坠落

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlkBRQyOYsZk011OAT87a0UI6x4CvFS7KPWeic50eFywvrJAYXICVRDFtA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-22 无人机坠落

原创

G.O.S.S.I.P

安全研究GoSSIP

两个星期前，我们为大家介绍了一篇利用无线干扰的方式破坏电动汽车正常充电的安全研究论文——[G.O.S.S.I.P 阅读推荐 2023-03-08 大破CCS](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494435&idx=1&sn=51eb1eda83d66db9fd313bca3b67125e&chksm=c063c5faf7144cec8425de61266b289fe39ec543a243bfdf7b1a5b2c727b6a2f319b46219c4d&scene=21#wechat_redirect)，今天介绍的这篇论文 *Paralyzing Drones via EMI Signal Injection on Sensory Communication Channels* 和那篇论文类似，讨论了如何利用电磁干扰（electromagnetic interference ，EMI）来让无人机坠落

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlkFfrjVEuA74Y08j7D7QywscvZAg2MWOShCYRypH6LAH4tRl5yNIyg9Q/640?wx_fmt=png)

本文作者调查了针对无人机的各种信号干扰方法，发现已有的方法有很多缺陷。例如大功率电磁脉冲干扰会让无人机的元器件烧毁，而利用GPS信号欺骗的方法来干扰无人机飞行，往往会把一片区域内其他依赖GPS的设备也一起影响了。于是作者在本文中瞄准了无人机传感器单元（inertial measurement unit，IMU）和控制单元之间的数据传输，发现了这种数据传输很容易被EMI信号影响。也就是说，在IMU和控制单元之间存在一条“EMI path”，一旦攻击者将EMI信号对准了无人机，就可能瘫痪传感数据，继而导致无人机失控。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlk1TccSZBualbiawbpCK8HDia1NNboZzoTko2pCo13TqfoXLFJlJCSQ4tQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlk83CyaibZ9ArQQfYRUwnod8mSMLHtQ0Ze8XibIg6yTSCMC8GjicDUMDJSQ/640?wx_fmt=png)

其实从原理上，这种攻击并不复杂，主要就是针对嵌入式开发中常用的 I2C 和 SPI 通信进行干扰，研究的主要难点在于如何产生精确的数字信号（特定的频率、特定的波形），针对下图中的关键位置，让干扰的效果最大化（很明显，受到物理学的限制，干扰信号的强度会随着距离急剧衰减）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlkbW9rQjDx3yjJzicmEGdknn4YkFqfniak8xiaIY5SczyiapWEq4xOmRIibOA/640?wx_fmt=png)

作者提出了一系列的分析流程，首先是要分析I2C和SPI通信怎么样容易被干扰，这部分内容相当的经验主义，反正作者就是说我们做了bla bla一系列实验然后就确认了这些通信确实可以被干扰（同时吐槽一下论文里面各种低像素的图）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlkylsn0mmcq1HebwRhIMs91cyR9bkpce9NHib4icn9BrUrXGiae1VXqmUeA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlkMxCzRj5MowBIup4KVfM1EaD7fS9nzVTBmH4GDqsSGUMTlwCGdlQEqw/640?wx_fmt=png)

既然信号传输可以被干扰，接下来就可以拿各种设备来测试干扰信号对无人机的定量影响，下图是作者的实验配置：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlkTUawibxIvowzZiaJibqaM7KezUNqMBv3hx39wpDhN6SiaZlTCJK5hWt0oA/640?wx_fmt=png)

作者又是放出了一大堆**非常低清**的实验数据图，表明在多种无人机（以及它们使用的不同的芯片）上均可以成功触发EMI攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlkOaEhCdrxNyVJ6icuGiakpauN9HOqJM1iakAlIq5fSgxycCfVyCRBAKJgQ/640?wx_fmt=png)

不过，光是说这种攻击“可行”显得太没有说服力，我们肯定更关注的是攻击距离和成功率，作者的实验数据里面相对比较好看的是对Arduino开发板的测试结果，但是这个大家肯定都不关心。至于针对现实的无人机，首先看看开源飞控硬件Pixhawk 4的受影响程度：作者弄了一个比无人机大很多的天线对着被攻击的无人机（下图，注意这个是作者弄的网站上的截图，不是论文里面的低清图……），然后说可以让悬停的无人机掉下来，但是对信号功率的评估，作者讲了很多啰里啰唆的话，最后说需要100瓦的发射功率，在50厘米的距离上才能攻击成功。而且我们可以从Fig. 18里面看出来，距离每增加1米，基本上功率就是需要10倍往上翻。很显然，这种实验再做下去就是搞电磁武器了，作者也只能弄了个公式估算了一下，要在100米开外成功攻击Pixhwak4硬件或者大疆硬件的无人机，分别需要147.756千瓦和310.70千瓦的发射功率……

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlklhymClf4t2TE6wvY8tonlxF6jxCHh5XvRIVmQ5LB4t6gXbY6gpq9mw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HvUWXASEiaQyHqU6bgINYlkrul5L5mXeUG2ky6Gu3M6MKs9Q2Y2o320xQc31cKMWo72C1Xn8s6XWw/640?wx_fmt=png)

再次吐槽一下，这篇论文写得就像大学本科时候我们做物理实验时候提交的实验报告，全是数据没有太多insight，但是如果你去看作者给这篇论文配的网站你就会赞叹，这简直就是《走近科学》，大量的视频资料让人目不暇接，那就让我们搬运一些视频，大家看看短视频更加喜闻乐见 ^\_^

第一个视频——rotor控制命令的干扰

第二个视频——针对静止不动无人机的电磁干扰（**注意，这个视频非常吵！！！**）

---

> 论文：https://www.ndss-symposium.org/wp-content/uploads/2023/02/ndss2023\_f616\_paper.pdf
> 网站：https://sites.google.com/view/paralyzing-drones-via-emi （论文能发表，网站忽悠水平很重要）

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