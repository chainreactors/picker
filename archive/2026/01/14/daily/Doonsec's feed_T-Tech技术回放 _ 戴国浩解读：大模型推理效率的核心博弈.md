---
title: T-Tech技术回放 | 戴国浩解读：大模型推理效率的核心博弈
url: https://mp.weixin.qq.com/s/hCawqU1L4wSwLueFDR1KeA
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:28:42.460117
---

# T-Tech技术回放 | 戴国浩解读：大模型推理效率的核心博弈

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bYRpC4MYIVia9iakI0iaefPDTOdppXjlKNGeG94LPWLclKR0KdDyPHlcs5JHY6Hgco6XLj2MVIGRat3thFa5ibg4EA/0?wx_fmt=jpeg)

# T-Tech技术回放 | 戴国浩解读：大模型推理效率的核心博弈

Z计划支持大模型创业

![]()

在小说阅读器中沉浸阅读

以下文章来源于T-ONE创新中心
，作者邀请你学习的

![](http://wx.qlogo.cn/mmhead/SCug0ESSOH8cstVoicBF7y7sGzah5OJO35UrE4TCej6ertjbQLmia6HcXacJMfnroYz4kNvpSTiamg/0)

**T-ONE创新中心**
.

T-ONE，源自清华，链接星连。不止做孵化器，而是让科研、产业、资本真正闭环。专注早期投资与创业陪伴，欢迎投递商业计划书至symao@linkxcap.com

![图片](https://mmbiz.qpic.cn/mmbiz_gif/bYRpC4MYIVh25qblKuNeFnjBRdZeqbzOEjJwdDl5Tfllju4HzmVWsUQyicjJL9KOWJSM3apHaxErZ1evAcYmdIQ/640?wx_fmt=gif&from=appmsg&wxfrom=13&tp=wxpic&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVh25qblKuNeFnjBRdZeqbzOXdgBlia9qYsDDl9mSou3ibvaXM4AGWeHXqgz6ngqp5GKKLpUyqVTvYMw/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&wx_lazy=1#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/bYRpC4MYIViae6XgDQTURibxn9YoNV4LEpBzfmfd3h3hAOEsJrrOpicsVthujLRnyajXVx164ia4TQxlm7BiaSI72KQ/640?wx_fmt=jpeg&wxfrom=13&tp=wxpic#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVh25qblKuNeFnjBRdZeqbzOXdgBlia9qYsDDl9mSou3ibvaXM4AGWeHXqgz6ngqp5GKKLpUyqVTvYMw/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&wx_lazy=1#imgIndex=3)

***T-Tech技术回放***

上周四，T-Tech技术直播迎来了第一场重磅分享。

我们邀请了上海交通大学副教授、无问芯穹联合创始人兼首席科学家戴国浩老师，围绕 《大模型的软硬件协同与产学研协同》 这一主题，从推理效率、技术演进到创新如何真正走向产业落地，进行了系统而深入的分享。

本篇将对戴老师的核心观点与技术脉络进行整理与总结，帮助大家快速把握其中的关键逻辑。**点击「阅读全文」**，即可查看完整逐字稿并回看直播内容。

***01 一个核心技术问题：***

大模型时代，推理效率成为核心问题

过去，评价 AI 能力的标准，更多集中在“算得多快”“算得多准”；而在大模型时代，这一标准正在发生变化。Token 不只是文本单位，是如今通用基础模型、基座模型串联物理世界和数字世界的重要一环。

今天，我们真正关心的，是：**如何提升一度电产生的Token质量，即它的智力水平。**因此，推理不再是成本项，而是生产要素。

![](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVia9iakI0iaefPDTOdppXjlKNGVCZl5uUyNJb8PnXqo2MCmwTB7I4taxwrzkFPJKlUy3y7Oq2KRLxn8A/640?wx_fmt=png&from=appmsg)

随着模型能力从对话走向推理、从解题走向 Agent，推理链条越来越长，消耗也越来越高。越复杂的任务，越考验推理效率。推理效率，直接决定 AI 是否“用得起、用得久、用得广”。

也正是在这个意义上，“软硬件协同”不再是工程优化，而成为决定大模型未来的核心技术命题。

![](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVia9iakI0iaefPDTOdppXjlKNGQpqumiaZphDeicibmk5LqEicTmFZIJaGpfrUgvduTl0DG4bViaRDx7o8xWw/640?wx_fmt=png&from=appmsg)

***02 一条技术演进主线：***

推理效率是软硬件协同进化的路径

提升推理效率，绝不是某一个技术点的单点突破，而是一条贯穿模型、系统与硬件的协同演进路径。以DeepSeek为例，它改变了模型训练的方法，从传统的算法修改让硬件被动支持系统变为面向最大化硬件效率，由系统驱动模型修改得到最佳性能，这也是传统非软硬件协同和软硬件协同最大的区别。

![](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVia9iakI0iaefPDTOdppXjlKNG1OePaykZGE64by6ylmjVsq9KySU7dV2omGJjqqyXO1XGlrV94yXohA/640?wx_fmt=png&from=appmsg)

这五个层次共同构成了软硬件协同的完整闭环，真正决定了大模型推理能否从“能跑”走向“高效可用”：

算法设计层：从模型诞生之初就面向真实硬件与资源约束进行结构设计，减少“先做大、再压缩”的无效成本。

算法优化层：在模型结构既定的前提下，通过减少冗余计算和引入早退出等机制，让推理过程更“聪明”而不是更“用力”。

系统软件层：通过调度、并行、通信与算子级优化，最大化释放已有算力，利用异步的方法减少等待和同步带来的隐性损耗。

硬件架构层：围绕基座模型的特定计算特征来进行推理上的硬件定制化加速（如稀疏计算），用更少的计算完成同样的任务。

芯片集成层：通过先进封装和高带宽集成，降低数据搬运成本，从物理层面提升整体能效上限。

![](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVia9iakI0iaefPDTOdppXjlKNGJfzsLnEjUmpDwq4JQXY96wMYOdAXqBVdcznDBW3HhuQWzamaJlUs2g/640?wx_fmt=png&from=appmsg)

***03 一条产学研协同主线：***

技术如何从论文，走向产业？

如果说软硬件协同解决的是“技术怎么跑得更快”，那么产学研协同解决的是“技术如何真正被用起来”。

无问芯穹始终关注如何通过软硬协同的方式去为大模型部署落地提供一个更高效的支撑，如何在大模型时代将模型与芯片之间的闭环打通。

![](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVia9iakI0iaefPDTOdppXjlKNGCOqjEwwuv3LdAQnKKLzIbIpSrZD1AjmePxk78pjdGRFkic7FfkqIhCA/640?wx_fmt=png&from=appmsg)

真正有效的技术创新并不是单向的科研输出，而是一个从学术创新出发、沿创新链走向产业落地，并再由产业实践反向塑造科研方向的闭环过程。

软件与硬件的协同，本质上也是学术体系与产业体系的深度融合。在人工智能加速演进的背景下，希望能够支撑一类复合型人才的培养——既理解学术前沿，又熟悉产业约束，既能做软件系统，也能理解硬件逻辑，从而让创新真正转化为可持续的生产力。

![](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVia9iakI0iaefPDTOdppXjlKNG3kJ4pBnh2WPJ4qsf70uiaTIPueP4N9L1M3wqO8NZwticuXcicCELnpMdg/640?wx_fmt=png&from=appmsg)

扫描二维码

查看戴国浩分享的直播回放

![](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVia9iakI0iaefPDTOdppXjlKNG7OKZLRzHH0FSicLSqKtibKKLGRKRPWZ5qeRYPdYvr4xkaibfertgibNohA/640?wx_fmt=png&from=appmsg)

你还想听谁来讲技术？

评论区告诉我们

![图片](https://mmbiz.qpic.cn/mmbiz_png/bYRpC4MYIVgt7aqC2kwuzrSuibpO3jN7Lpt3ICUZjaBuyq7lmCR3Pw0JfAPgBWUfibKRqcmftYyuj58W8T6Lgcww/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=4)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/bYRpC4MYIVgt7aqC2kwuzrSuibpO3jN7LeJ8MHHwhTpMS9ZOe8fh1BQrBu5eJ5ohNhrWkSlNSapZzWnXeqSsaxg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=5)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/JPyOwicUdYCq7qWiaMic0hmgwPeACPdnGNmc2A0dz0iaMpLgAZDQxKm13X64HZXQ0Xear7kZHOUOFaL1EznJKIQDEA/0?wx_fmt=png)

Z计划支持大模型创业

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JPyOwicUdYCq7qWiaMic0hmgwPeACPdnGNmc2A0dz0iaMpLgAZDQxKm13X64HZXQ0Xear7kZHOUOFaL1EznJKIQDEA/0?wx_fmt=png)

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