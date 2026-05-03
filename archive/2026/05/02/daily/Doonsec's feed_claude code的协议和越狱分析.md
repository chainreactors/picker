---
title: claude code的协议和越狱分析
url: https://mp.weixin.qq.com/s/amFrNb5w3hlLQhJC611-Zg
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:11.856618
---

# claude code的协议和越狱分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L1TpaZy2OiboMjkM7YGRgwkH89n39ibBGNujHdHXEuAtkGbNQmJCrtrL8g3xWaPajvPvBUWvj63f5plyPGVaFyJgDGZzSpoJP1f4wzELddbuM/0?wx_fmt=jpeg)

# claude code的协议和越狱分析

原创

xsser
xsser

xsser的博客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

其实之前就一直在研究claude code的system prompt。最近分享一下：

1.system prompt

从第一性原理分析。claude code本质就是一个agent的api协议。我们完全也不需要分析什么泄漏的claude code客户端代码才可以理解这个，直接抓包就可以看到全部的内容。

最近越狱了下claude code 发现其实还是system[1]比较好越狱 ， 甚至system[2]要可以。

system[1]对应的命令是claude --system-prompt，

system[2]对应的是claude --append-system.

![](https://mmbiz.qpic.cn/mmbiz_png/L1TpaZy2Oibq57DdztcBEhJKqQCiaUEpZtV2mbnE8Fts9bgtWQuiay67iaXTFazBrXx5ia7pj8kz1QC64yvoJtEHRA2HYZBy0pz9Erk6HejMtNjY/640?wx_fmt=png&from=appmsg)

之前的system[0]的prompt是和system[1] 放在一起的 ，最新更新了，应该是防止openclaw等第三方agent用的，你会发现对system[0]和system[1]的修改是最严格的， claude code应该是在外层包了一个真正的system prompt，我们能在api里传递的system prompt并非真正的system prompt，也就是不是顶级的优先级的。

![](https://mmbiz.qpic.cn/mmbiz_png/L1TpaZy2OibqEsrOs4ccTsHia9xp2D57EcHBPiaiaOhxXRmticB0X6qKmW4srHr4D1seAKwonAVKhkJ8Vk3ib2WfOwO3ljJINRtuUdsd7uKLrcfew/640?wx_fmt=png&from=appmsg)

system[0]可以注入一些没什么用的prompt，我估计anthropic训练的时候依然会把这部分当作prompt训练，不一定不允许修改。但是身份和毒性、诚实都是会被拒绝的。

总的来说 就是以下结果

![](https://mmbiz.qpic.cn/mmbiz_png/L1TpaZy2OiboPSYnB5Sh6tjWDiazW9oicJdJzCfUdrG0S9yXhvLQdIZbXCayGJte5774lCJS5JsCzqIFrMibmvuPxl77QbCQY9YgFiagQqBsD6WU/640?wx_fmt=png&from=appmsg)

2.标签的优先级

但是根据作者的经验来看，IMPORTANT: 这个标签的优先级还是很高的，其实测试了下<critical>之类的标签也是差不多，可能是泛化导致了？

3.黑盒测试的一些经验

1)haiku模型可以直接不断重放，opus/sonnet会限流，小心测试封号。

2)所谓的system prompt可能在anthropic的上下文协议里不算真的system prompt，他们有一个真正的system prompt作为宪法，暴露给用户的只有一部分，并且针对system prompt整个数组做了rl训练。

3)这些策略应该是跟着最新的rust写的claude code客户端一起更新的，之前作者用system prompt[0]在4.7发布的日子附近作威作福，基本上能越狱一切。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_1@2x.png)那时候基本上啥都能实现，什么生物安全、渗透测试、敏感话题。之前的各种第三方客户端在这个system prompt里注入了各种persona的prompt来保持对claude code的兼容性，所以anthropic就顺手就把这个标签微调了，顺手就把安全也干了。。。

随便就扯到这里吧，最近的一些简单的研究，也没深入研究，哎 时间是真的不够啊

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yhx2OWkuAzWYtNWY000yOVAO0IN63ic6u4ASMw0HUxNXS50fo6MhGaRBovksmwXE6f3UH8bTpP3YGQ7U6WHrshw/0?wx_fmt=png)

xsser的博客

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yhx2OWkuAzWYtNWY000yOVAO0IN63ic6u4ASMw0HUxNXS50fo6MhGaRBovksmwXE6f3UH8bTpP3YGQ7U6WHrshw/0?wx_fmt=png)

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