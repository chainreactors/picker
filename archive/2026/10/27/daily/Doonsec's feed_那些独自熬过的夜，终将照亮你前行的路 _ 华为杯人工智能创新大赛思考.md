---
title: 那些独自熬过的夜，终将照亮你前行的路 | 华为杯人工智能创新大赛思考
url: https://mp.weixin.qq.com/s/Ob89QttMs3ft7nBkbzLenQ
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:40:58.278591
---

# 那些独自熬过的夜，终将照亮你前行的路 | 华为杯人工智能创新大赛思考

# 那些独自熬过的夜，终将照亮你前行的路 | 华为杯人工智能创新大赛思考

原创

czl
czl

玄枢战队-Arcane Hub

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

其实我对华为杯是有一定的阴影的。在往年，我们参加华为杯网安决赛的时候，团队在答辩时设备出现了问题，直接影响到了我们最终的结果。所以从那次以后，华为杯一直都是我心里的一道坎，即使我拿到了很多其他的奖项，我也一直希望能够在华为杯上证明自己。

这一次，我们做到了。本次华为杯研究生人工智能创新大赛共有来自全国高校和科研院所的5637支队伍报名、提交有效作品4662件，最终305支队伍晋级全国总决赛。在企业赛题“智能终端多模态输入感知与识别及个性化应答”上，我们是唯一进入全国总决赛的团队；在最终的决赛，我们拿到了全国二等奖，华为赛题专项奖一等奖，成为全国仅有的5支获得该专项奖一等奖的团队之一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIxfGtmnsNk95RN0vh9XabR738tvvNyd0udyMicEeF4dGwnDVysEQDQNC1ibqFdlJmDBOySPFdMkxR4Q6uf6aDaExiaxrMShehMnGE/640?wx_fmt=jpeg)

回望整个比赛过程，我们其实走得非常不容易。从7月份以后，团队的事情越来越多，所以其实我们并没有太多的时间去精雕细琢，整体算下来，倾注在这上面的时间连两周都不到。虽然我们投入的时间并不长，但这两周也是通宵达旦，踩了无数的坑，熬了几个通宵，最终才完成这个作品。

我们最初选择赛题五，其实也是想要探索多模态感知识别这方面的技术。一开始的时候，我们并没有觉得这个赛题有很大的难度，因为本身我们也做过一些类似的模型训练、多源异构数据处理的工作，但是“纸上得来终觉浅”，我们在实际去想要完成这个赛题的时候，仍然遇到了很多的困难。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwuOBAvBLO63dKhj0U7EMcYvjjrx6GArwF3l6QiaLRN589rHxG53y9wyo77yXEvvnz0ibgSuhDCyIicRVKlQ6v38DdSUw4BlIDKu0/640?wx_fmt=png&from=appmsg)

赛题其实可总结为一个核心的问题，即如何在资源受限与隐私保护的条件下实现对用户意图的精准识别与个性化反馈。这里其实有几个冲突的点：

①资源受限：不仅仅是端侧资源受限，云端的大模型也限制在14B以内，模型能力的限制会导致它能做到的事非常有限，有时即使我们给到模型的输入是正确的，模型本身也会给出错误的答案。我们如何去用这个14B级的模型，如何设计模型训练微调的路线，本身就是一个难题。

②隐私保护要求：赛题有严格的隐私保护要求，我们本身又做的是终端操作场景，需要实时的去感知用户能够看到什么，因此我们如何去做端侧感知、提取和脱敏，如何在端云协同推理的过程中保护用户的数据安全，成为了技术难点之一。

③意图感知与个性化反馈：在云侧模型只能看到用户脱敏后的结构化证据的情况下，如何精准的从结构化证据中识别用户意图，如何从多轮的交互中沉淀用户画像，实现个性化的反馈和应答。这一步的设计，直接影响到的是用户核心的体验。

④赛题的公开评测要求：赛题要求模型在公开的数据集上训练和评测，对于我们的场景，并没有比较合适的公开数据集能用。再者，公开数据集评测的情况和我们端到端产品的情况本身就存在一定的差距，公开数据集本身是静态数据（图片、音视频等），而我们端到端产品链路上会有更多的感知手段（如Windows UIA，Android Accessibility等），这导致了我们训练评测与端到端产品链路之间存在天然的断层。

因此，如何在赛题的这些要求下，找到一个平衡的点，就成为了最大的难题。在早期的训练与架构探索上，我们其实下了非常多的功夫，经过了多轮的训练和方案的迭代，才最终形成了作品的设计。这些背后的努力，评委看不到的，是我们在决赛中展现不出来的。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxw6UlfdhygX968wCB4ct9DV3VVRjEsaZ5He8HaTWO93Lg4bd1AUAzTcoPnIszzgdJQKuicnkq7Yl5jQ2tnwB23g5iaaxlZicwCVc/640?wx_fmt=png&from=appmsg)

在设计之外，还有更多的困难。因为决赛时间正好和今年的华为杯研究生网络安全创新大赛、全国密码技术竞赛的作品提交时间相冲突，我们在这一周同时要交5个作品，还要兼顾决赛的PPT、答辩训练，因此我们度过了非常难忘的一周。但是好在，最后的结果并没有辜负我们。

最终上台领奖的时候，是我感受最深的时候。望着大屏上我们的名字，站在台上望着下面的人群，聚光灯照在你的身上，这一刻，我觉得我们所有的努力都有了意义。对于我们做技术的来说，能够被别人认可你的价值，是最令人触动的。不管是项目还是比赛，我们经历了太多被质疑、被轻视的场景，即使你付出了再多的心血和努力，很有可能在别人眼里，你做的东西就是一文不值的。但是这次，我们的努力没有被辜负，虽然在主赛道我们没能拿到一等奖有点遗憾，但是这个华为专项的一等奖已经对我们的成果给出了最大的认可。

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIyibroTtUicg4RTCGe5lHT0tQTlV9XSRcZRoaKPunp1k8nVHMUibYEoVR8CEqC748wnvCicvM4VZqUJT1DicP4CXNvlLLrQwBxRrUGM/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIzEq4Sn0X1KiahVh6wEa2TqicjGwRfqRCiciaDoxES3UYAicD4KwNBcicOMMiboAfNNkmOubUA5lBjzBbVuQMfvrWxxicPSvgSrmicNBSZo/640?wx_fmt=jpeg)

从确定方向，到架构设计，再到开发落地，最后到决赛答辩，这每一个阶段，都离不开我们团队每个成员的辛勤付出和努力。我相信，每一段路都不会被辜负，那些独自熬过的夜，终将照亮你前行的路。

荣誉并非终点，探索仍在继续。面向行业难题的持续探索，才是玄枢团队真正的征程。山高路远，探索不止。玄枢，继续向前。

PS：这次华为之夜我们也大丰收了，连着抽到一等奖、二等奖和三等奖，连吃带拿的来进货来了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Lol.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Lol.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Lol.png)。

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIwkuRcRwicE8LH2m94EC2iak9u0JmT2q7ruiau1H8IuDhAQkLIvSI5zPpia1y985erkEh8mVg7VsYtScJb0kgoEYPH3wcDJtjnAic8I/640?wx_fmt=jpeg)

预览时标签不可点

修改于

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/lmfaAJ5WqA1sUVs3bkh8pbJCu96cmwJ5JrqlejuC2Cia3prrW7Nia2b7dibjBwqjMnLV95ibBrOQkEbm9PIDw5IvFQ/0?wx_fmt=png)

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