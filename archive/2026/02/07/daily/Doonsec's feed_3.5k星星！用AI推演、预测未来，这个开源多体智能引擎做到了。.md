---
title: 3.5k星星！用AI推演、预测未来，这个开源多体智能引擎做到了。
url: https://mp.weixin.qq.com/s/aFXqUvImHtmJ4InO5u41Iw
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:31:34.612574
---

# 3.5k星星！用AI推演、预测未来，这个开源多体智能引擎做到了。

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/l2VB7h1M5NYbuufBm0iarm76y2tdsNO8r2AQSsFgia0fL9moAHjSzpaliacKiccMOoGmXMptdyoA0pucrhibIicBwVIw/0?wx_fmt=jpeg)

# 3.5k星星！用AI推演、预测未来，这个开源多体智能引擎做到了。

Hunter取证

![]()

在小说阅读器中沉浸阅读

以下文章来源于开源AI项目落地
，作者开源AI

![](http://wx.qlogo.cn/mmhead/ps68icnpRvDXxrgcSj0NoKoqHEsg3JxLbbhkmqpCPkWv0yVFOIOJJJyTcQRBMRV9rnHGSvgYicE1s/0)

**开源AI项目落地**
.

分享有价值的开源项目，并且致力于AI项目的落地。 有软件开发、AI项目落地需求请与我联系。

![](https://mmbiz.qpic.cn/mmbiz_png/l2VB7h1M5NYbuufBm0iarm76y2tdsNO8rhPwMrRoia0icPUpw8mfw4nPic5kjwpKgFDJ3SMFBwG6zrxtZNISYKUIyg/640?wx_fmt=png&from=appmsg)

推演未来，这个词听上去还挺玄学的，但是跟AI结合在一起，却又那么合理、那么科学。

这个世界上，**每一个事件、个体都可能有着千丝万缕的联系。**

即使是一个生活非常简单的人，如果你用图来表示，那他的关系网也可能就是下图这样。

![](https://mmbiz.qpic.cn/mmbiz_png/l2VB7h1M5NYbuufBm0iarm76y2tdsNO8rhIBjpXHICB4icibKU8803iaGhStlvnUuAe4ZF3OrhDMwCD5d7D0kXaViaw/640?wx_fmt=png&from=appmsg)

没错，这就是图谱。

人为的去做这样一个图谱，是非常麻烦的，但是现在有了AI，就能快速创建一个这样复杂的图谱。

我们总是在事后说要是怎么怎么样就好了，在这个图谱里，如果我们注入新的变量，那可能就会发生蝴蝶效应，引起一系列的连环反应。

这就是今天给大家介绍的MiroFish所能做到的。

**项目简介**

**MiroFish的核心定位**是一个基于多智能体技术的AI预测引擎，抽象点说的话就是一个高保真的平行世界生成器。

你只需提供一份种子文件，可以是一份数据分析报告，也可以是一本小说，然后用自然语言下达你的预测指令，MiroFish就会自动构建出一个数字沙盘。

在这个沙盘中，成千上万个拥有独立人格、长期记忆和行为逻辑的AI智能体开始自由互动、演化，你就可以看到**个体互动所引发的群体涌现。**

**DEMO**

主页就这样简简单单的，大家玩的时候，数据量要慎重一些，模拟还是比较消耗算力。

![](https://mmbiz.qpic.cn/mmbiz_png/l2VB7h1M5NYbuufBm0iarm76y2tdsNO8r7RW3406S80spxMhUgNpFMmVYwKJfr1IYS6jkU6Ihn2h3XFChAia3vZg/640?wx_fmt=png&from=appmsg)

这就是生成的图谱，和其中某个个体的信息。

对于预测来说，真实的信息量越大，那肯定预测的结果就越准确。

![](https://mmbiz.qpic.cn/mmbiz_png/l2VB7h1M5NYbuufBm0iarm76y2tdsNO8r9gao99wvwd3icYa0BF5hs2WWmqPJOVKgnb6sqxbh5YibicKFEenMtr62g/640?wx_fmt=png&from=appmsg)

你说会不会以后算命老头都用上科技了，哈哈哈。

当图谱非常完善，这时候输入一个变量，就可以预测可能会发生的事情。

![](https://mmbiz.qpic.cn/mmbiz_png/l2VB7h1M5NYbuufBm0iarm76y2tdsNO8rIabib6tCAiaOzI47CbOCyZkNxYVKTjMWFJmrITzCj9eVpEH9cuEGKhZA/640?wx_fmt=png&from=appmsg)

这也适用于企业公关，在危机发生前，预演不同公关策略的走向，精准排雷，降低被群众唾沫淹死的可能性。

下面这是武汉大学舆情推演的示例。

![](https://mmbiz.qpic.cn/mmbiz_png/l2VB7h1M5NYbuufBm0iarm76y2tdsNO8rab0ThpRLxnIM0tMbD7iaolH0EIMlMANkX0NCIiaqIb8jPicUKGO8gPh9A/640?wx_fmt=png&from=appmsg)

下面这是对《红楼梦》结局的推演，构建了一个庞大的清代社会关系网络，贾宝玉、林黛玉、薛宝钗等数百个角色被赋予了独特的性格和记忆。

这里的DEMO就直接用作者提前录好的视频了，视频做的很好，可以当故事来看。

视频来源于文盲杜甫

**推演流程**

**1.图谱构建**

从种子信息中提取关键实体和关系，利用GraphRAG 给每个智能体注入独特的背景和记忆。

**2.环境搭建**

自动生成社会结构、人际网络，并根据你的需求设定模拟的核心参数。

**3.开始模拟**

成千上万的AI智能体在这个数字世界中自由互动，行为将引发不可预知的群体涌现。

**4.生成报告**

专属的报告智能体深入模拟后的世界，挖掘关键洞察，生成详尽的预测报告。

**5.深度互动**

你可以像玩模拟人生一样，跟世界中的任何一个AI对话，了解事件背后的深层原因。

**项目链接**

```
https://github.com/666ghj/MiroFish
```

**扫码加入AI交流群**

**获得更多技术支持和交流**

**（请注明自己的职业）**

![](https://mmbiz.qpic.cn/mmbiz_jpg/l2VB7h1M5NYbuufBm0iarm76y2tdsNO8rYOqjMoic8KnF3GpicAKnheyFhoT9NUoxnftaX06uIcNFHq65kDLDfwIg/640?wx_fmt=jpeg&from=appmsg)

关注「**开源AI项目落地**」公众号

与AI时代更靠近一点

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gq4WdY12yiaTeged5RjOZ7lx2kczflQlbzg8RXMvDm24segKwL9KECsouDJz4QAaMrM5sc2YYLxUZNX5tclvRpw/0?wx_fmt=png)

Hunter取证

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gq4WdY12yiaTeged5RjOZ7lx2kczflQlbzg8RXMvDm24segKwL9KECsouDJz4QAaMrM5sc2YYLxUZNX5tclvRpw/0?wx_fmt=png)

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