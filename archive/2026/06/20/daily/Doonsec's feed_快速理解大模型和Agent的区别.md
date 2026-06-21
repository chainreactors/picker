---
title: 快速理解大模型和Agent的区别
url: https://mp.weixin.qq.com/s/T3lGq4Q-FbwEUBD4Fa975w
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:45:48.899907
---

# 快速理解大模型和Agent的区别

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bCZqF8oBiayZ6a8ax9wJbpPPsmgQUCJ5mibibOYVFSO8ALF7p50fumnJ8kKV030ic10ACBjmU2ia1ianicdn4QBbK9gZpaBXSm4DBP1SbtFg4Ht3vE/0?wx_fmt=jpeg)

# 快速理解大模型和Agent的区别

原创

静观云起
静观云起

码云精炼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一 什么是大模型LLM？

LLM的本质是机器问答，最擅长的是生成文字，也就是根据输入返回文字 ，但是它有明显的短板

✅ 知识可能不是最新的，很多实时问题它并不知道

✅ 它自己不会动手，它只告诉你应该怎么做

✅ 它没有天然的持续状态，容易把中间过程忘掉

所以单独的大模型，更像一个超级会表达的问答机器，但不一定够能够把一件事从头做完

![](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayZicDib5cJkmBKrly4Hh3ic4FbCUJoliaA78zqMM0xp0wQJRjFtic0wFMM4siakUgHspKDfo4zKSyf2F90gzKib3U7Cl0WPSjEibt8XfuI/640?wx_fmt=png&from=appmsg)

二 初步认识Agent

很多人以为Agent就是工具，工具只是agent的一部分，它是一个围绕目标运行的系统，它能自己做规划，按多步推进任务，并在每一步读取结果后调整后续动作，这套能力的关键在闭环，画面里这条链路从感知开始，经由规划进入行动再到反馈，把这条闭环记住，才是真正理解Agent的第一步

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiaya8TomYHIEibYOfyUbcBMRUibINiaFQItrDruMwjVlmC3OvYiasRBRbCTdtlFA9cuVXQibpPeZnXjQsWdxIhY5thqzFqjK2vMoB58CQ/640?wx_fmt=png&from=appmsg)

三 什么是Agent？

Agent=LLM + 工具 + 反馈

✅工具为agent的手脚，真正的去查询，计算，执行

✅ 记忆，把中间状态，偏好，历史结果都记录下来，不会走一步忘一步

✅ 反馈控制，根据执行的结果决定下一步是继续执行，还是更换策略，还是重试

下图三项能力加上后让它从"会说"升级为"会做"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayYYic9rcMSptWDOloEyKvgGv7p0TRlm6ibDXNFO4JgFjPa99myTIelKpSsiaf0Rcmr2jZUicIbx66McNmW4eDMaAhLQibG9U26RmkI0/640?wx_fmt=png&from=appmsg)

工具调用(tool use)

让模型的输出不再是建议，而是触发一次真正的动作，它可以去搜索资料，运行一段代码，可以查数据库，调用API,甚至可以发邮件，创建工单。原来很多聊天的场景变成可以自动完成了。

![](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayYrBKOEibeEVMqEHfstM4JKtbyMgAXe7xsSa6wZk18yHjZHPxjtqmWvhlT1kP4ibwvsESLBNkV0yRW7117QQmYML4CEBCxxDYQuE/640?wx_fmt=png&from=appmsg)

记忆机制(memory)

短期记忆放的是当前任务的中间过程，查到了什么，下一步要做什么，上一步返回了什么结果，长期记忆更像档案库，放的是跨任务的信息，例如你的偏好，历史决策，你常用的工具的参数，需要的时候再检索回来使用，有了记忆之后，Agent才能在一个复杂任务中保持连贯，不至于每一步都重新开始。

![](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayaP927DYm6YTicYCr7sHQ0w34ya4zDj8UdDuEj1Hgfg1rs2Cibo5mH5jkuFCDtwRFpNx6fWXCDBDQeUe9VXS3KI4VPPQog74reib8/640?wx_fmt=png&from=appmsg)

推理与自我纠错

现实世界做事会经常失败，关键词搜索不到，接口报错，结果不符合预期。如果它一失败就马上停止，那它只是一个会调用工具的脚本。Agent它更像人做一步看结果发现不对就调整比喻换关键词再搜或者换一种调用方式再试一下，这种边做边调整的能力，才能在不确定的环境里把任务推进下去。

![](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiaybu1b9MOFMIcticGABq9wUSz2GMUdoYkctXeAjeahY1rxNZiccDPg1w3qmdibFg3gMq8CE34N5zl6aicspCFgaGmibe08XGrvyXPdos/640?wx_fmt=png&from=appmsg)

闭环

感知--规划--行动--反馈

✅ 感知：读取你的输入，看环境信息

✅ 规划：拆任务，选工具，排步骤

✅ 行动：真正的调用工具去执行

✅ 反馈：读回结果，判断是否达标，不达标就修正计划，当这个环境能自己转起来，我们就说它具有了Agent的味道“自主闭环”

四 Agent示例

查询北京天气并发送邮件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayYoXOrdSKXaG31IMmKszvic3LHrByrib5mu5Bcria9cicye60xKh9RMGTT8AQn1I1eqqUBxmicjsyODDNRlfUI9Md1jic2PFDmRDYsK0/640?wx_fmt=png&from=appmsg)

问题： 帮我查一下北京的天气并发送邮件

1.调用工具 get\_weather("北京")

2.获得反馈 晴 15°

3.长期记忆 检索老板邮箱地址

4.执行行动 调用send\_email()

五 总结

大模型的优势是生成文字，Agent优势是完成任务

Agent三大特点：

✅ Agent的核心是自主闭环

✅ 工具 + 记忆 + 反馈纠错

✅ 从回答问题升级到完成任务，把事情做完

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YFxLNg1Bibfnia4huCODlTdyh6PTbL1pic45RaY9PANbJVIia0XOz1gV28f9BHd4341P1lpqQwn0cRGBjHPbHYmYIQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

码云精炼

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

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