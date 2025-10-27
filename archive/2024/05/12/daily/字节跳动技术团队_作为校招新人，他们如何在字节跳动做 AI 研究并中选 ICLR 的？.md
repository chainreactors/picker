---
title: 作为校招新人，他们如何在字节跳动做 AI 研究并中选 ICLR 的？
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247507216&idx=1&sn=f4801e6e4c526204a590ad78d1555e40&chksm=e9d316f2dea49fe4c4d83dff108795c27f64803ff9977a5ba230e06ee7f9c9a884fe6dfde11e&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-05-12
fetch_date: 2025-10-06T17:17:16.317660
---

# 作为校招新人，他们如何在字节跳动做 AI 研究并中选 ICLR 的？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ia00JJEEnxEn1VtZDJYvyubpweJ05OpKmvFrU8SF7pOkESe97FJPGlPNqwhibumlccjQydRlpb71NmdFa9XRCBPw/0?wx_fmt=jpeg)

# 作为校招新人，他们如何在字节跳动做 AI 研究并中选 ICLR 的？

字节跳动技术范儿

字节跳动技术团队

**校招生和实习生在字节跳动，工作一年就中选 ICLR 2024 ，这是怎样一种体验？**

就在 5 月 7 日至 5 月 11 日，2024 年度国际表征学习大会 ICLR 2024 在奥地利维亚纳举办。该活动是深度学习领域最重要的学术活动之一，由深度学习三巨头之二的 Yann LeCun 与 Yoshua Bengio 发起。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ia00JJEEnxEkbciaVTgDlrbhvPzLjp2JUnTTVvwt5xYv75FSmqI557jMQYssn2g4rsibicqmPZYSFUZl3IJej44pNg/640?wx_fmt=jpeg)

今年 ICLR ，共有 7262 篇论文提交，整体接收率约为 31% ，中选文章作者中，不乏字节跳动校招新人的身影。

这些同学中，有的人是实习生，有的人刚刚毕业一年左右。在公司时间虽短，却也做出了顶会成果。

**今天，我们一起看看他们是如何做到的。**

**![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEmuR5nBDlkcRY0HOpLFTicSkwoFD7Uj6lsNoIcUicjcmqoibzeY4vUzLEKVOAdb0DJtOJLupoVqZG8Yg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)**

#

# **一句话让机器人拿起西兰花**

> ****Terry 字节跳动 2022 校招生****
>
> 毕业于 JHU
>
> Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation 核心作者

这个项目立项是在 2023 年的三四月份。当时 ChatGPT 刚出来没多久，证明了其在 NLP 领域的有效性。后来大家也看到了，大模型在图像、视频生成都能用上。

但在机器人领域，训练数据相比 NLP 和图像来说少很多，而且采集难度大、周期长。我们团队希望探索新的方法，在少量数据的情况下，也能在端到端多任务操作上达到不错的鲁棒性和泛化性。

**这也是整个团队在端到端的多任务操作上的第一次探索。**

![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEkbciaVTgDlrbhvPzLjp2JUnX7MPBic4XIGa3h48Jzoy5IARznfEzlNrR6oZnnMeToKtjbjpmh9DO6Q/640?wx_fmt=png&from=appmsg)

具体来说，我们参考大模型做法，希望通过大量公开视频数据帮助机器人实现更高效的学习。最终，我们也验证了这个方法在机器人学习上面效果很好，鲁棒性、抗干扰性也更强。

我们这个模型也参考了 GPT 的做法，语言模型是根据前面的词，生成后面的内容。我们也是，让机器人根据前面的数据对后面的动作进行预判。

![](https://mmbiz.qpic.cn/mmbiz_gif/ia00JJEEnxEn1VtZDJYvyubpweJ05OpKmXwch5AgBqJSXLR6iaXctu82VC2UwNkvfibttucYBIs6NFjDDicEnib2zTg/640?wx_fmt=gif&from=appmsg)

接下来是验证思路，这也不是我一个人完成的，而是由不同背景的同学一起参与完成。

有同学做学习算法、数据集，有同学负责硬件，即机器人本体，也有负责机器人控制的同学，还有的同学负责进行测试。我主要是做学习算法和测试这块。

面对各种问题，相关同学就会来一起积极帮助调试，很多方法也是由不同背景的同学提出，我们一起去验证对比，大家一起把事情完成，这样的协作沟通其实让人感到轻松一些。

而且 Leader 也会帮助我们，为大家选出真正有价值的研究课题，**我们的课题是前沿的，研究方法也是前沿的，加上公司提供了丰富的计算资源。我觉得，还是非常难得的。**

最兴奋的还是经过很多次尝试后，终于成功的那一刻。想想看，跟机器人说一句话，它就可以帮我做一件事，比如，从一些蔬果中拿起西蓝花，放到盘子里去。这让我们觉得很有成就感。

后面就是抓紧时间，去探索机器人的能力边界在哪，比如去做更复杂的任务、增加干扰物、变换背景完成任务等等。

![](https://mmbiz.qpic.cn/mmbiz_gif/ia00JJEEnxEn1VtZDJYvyubpweJ05OpKmbicQ91iazYjkCG0TrkAESDJEkcNdX7WVWvrB8dnJpml2bBq0SSbO7iaibg/640?wx_fmt=gif&from=appmsg)

**这个项目里，大家工作都是奔着很高的目标去的。就算方法已经达到了 SOTA ，但我们还是会想，哪些地方可以做得更好一些？这个方法是不是足够通用？**

感觉在字节跳动， Leader 跟你的讨论，与在学校导师跟你探讨思路、一起解决问题是一样的。遇到困难，大家也会坐下来一起讨论：问题出在哪儿，哪个方法对，哪个方法不对。

跟在学校不一样的是，加入公司后，我开始更多去思考什么项目对公司和产业更有价值，这也是我进入公司这一年的变化。

**![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEmuR5nBDlkcRY0HOpLFTicSkwoFD7Uj6lsNoIcUicjcmqoibzeY4vUzLEKVOAdb0DJtOJLupoVqZG8Yg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)**

#

# **做高质量的研究，而不是刷论文**

> **Paul 字节跳动 **2023**校招生**
>
> 毕业于中科院自动化所
>
> Image Background Serves as Good Proxy for Out-of-distribution Data 核心作者

我做的研究是分布样本检测，在大模型时代，算一个比较小的研究方向。

![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEkbciaVTgDlrbhvPzLjp2JUnyzOtAOfjfUxtLZO2GDKqHGXPAg7MnRQVuCWOTnINKfibp5UaENgUCnQ/640?wx_fmt=png&from=appmsg)

分布样本检测其实应用很多。拿猫狗分类举例，一方面要去分辨是猫还是狗，另一方面，也要分辨图片到底属不属于猫或狗，不然就是分布外样本。

一开始我就想，能不能探索一种方法，从图像本身获取分布内和分布外特征。也就是说，将目标所在部分作为正样本，其他部分背景作为负样本进行模型训练。这样做出的模型在分类上，应该有非常好的鲁棒性，且也适用于现实。

后来证明，这个思路是有效的。其实这篇文章，团队其他同学也给了我很多帮助，包括提供了效果更好的方法，也从论文撰写和排版角度，提供了不少建议。

![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEkbciaVTgDlrbhvPzLjp2JUnGvAiay7pwDLqG5TbEibLbJhzNAx7aMjmtlaWBgYUtwsLhlP3wSb8ONzg/640?wx_fmt=png&from=appmsg)

应用方面，这个成果也能与多模态结合，比如，多模态模型目前在看图答题时，常会出现“胡编乱造”问题，明明图片没有的物体，它会说有。这个成果的结合，能减少幻觉产生的。

加入之前，我也在其他公司实习过，感觉字节跳动这边工作时间灵活，对不同习惯的研究工作者来说，比较友好。

另一方面是字节跳动的 Mentor 都非常资深，而且在日常工作中，他们不会随意将自己的想法强加给你，团队对研究是非常开放的， Leader 不会阻止你去探索。

**只不过，比起“水”文章，我们还是倡导大家探索前沿技术，**做真正让人眼前一亮的工作。****

**![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEmuR5nBDlkcRY0HOpLFTicSkwoFD7Uj6lsNoIcUicjcmqoibzeY4vUzLEKVOAdb0DJtOJLupoVqZG8Yg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)**

#

# **第一次试验，我们就有很大希望**

# **继续做下去**

> **Jory 前字节跳动实习生**
>
>  NUS 在读博士
>
> AdjointDPM: Adjoint Sensitivity Method for Gradient Backpropagation of Diffusion Probabilistic Models 核心作者

**这篇论文是我在字节跳动实习期间做的。**

一开始有想法，是在 2022 年底，那时各种生成模型比较火，尤其扩散模型。

我们就想，能否将一些预训练好的判别模型与生成模型结合，这个是我们最初的灵感。

具体思路是，根据生成的图片，让判别模型算出 Loss 数值，再用 Loss 微调扩散模型参数，以生成更符合要求的图片。

举个落地的例子来说，我们在亚马逊上看到的图片可能美感不够，或不符合审美要求，其实，可以用预训练好的审美评价模型去微调生成模型，再让生成模型生成商品图，这样美感就更好。

![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEkbciaVTgDlrbhvPzLjp2JUnFY7lbRiadWQv36XlzjX6kDFILvAbqdQibqV5Asj0ibibCRzL9kW1kbtTJQ/640?wx_fmt=png&from=appmsg)

这个项目是 Mentor 提出了大致的框架，我去进行尝试。

**我们的设想其实是个比较数学的方法，原本不确定是否有效，没想到，第一次试验效果就还可以，这也给了我们很大希望继续做下去。**

另外一个同学对视觉任务特别了解，代码能力也很强，给我提供了一些技术支持。当然，公司科学家也在背后支持我们整个团队。

这当中，我负责自己去跑实验，有困难就可以找大家解决，毕竟他们经验比较丰富。

在微调网络参数的过程中，我们希望优化整个过程，把算力要求降下来，也是大家一起商量，聚焦文字信息嵌入关键层，Cross Attention 层，这样就容易一点。

![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEkbciaVTgDlrbhvPzLjp2JUnkXyb9uEBkoiaj2GxTtuQia1Libz6jpOlVtU9Cnh7Uhefh9TX4n4eE6yyA/640?wx_fmt=png&from=appmsg)

**图注：采用论文方法，生成的小狗面部细节与小鸟羽毛细节更贴合左侧参考图片**

来字节跳动实习前，我一直都在纯研究的机构里，刚进入字节跳动时，最大感受就是——公司里技术交流特别多，大家每天都在分享、讨论科技界有什么最新的、让人眼前一亮的模型。

这当中，我也开始理解了业务驱动的感觉，更看重应用，收获了新视角，对自己后续发展也有很大帮助。

**![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEmuR5nBDlkcRY0HOpLFTicSkwoFD7Uj6lsNoIcUicjcmqoibzeY4vUzLEKVOAdb0DJtOJLupoVqZG8Yg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)**

# **加****入我们，****一起探索**

# **AI 的价值与乐趣**

#

上述内容仅仅展现了字节跳动在机器学习、大模型、具身 AI 等方向成果的一小部分。

本届 ICLR 2024，字节跳动共有 20 余篇论文入选，相关同学来自智能创作、ByteDance Research、豆包大模型团队等业务线。

**如果你也对 AI 、大模型、机器人等研究工作感兴趣，想在务实高效的氛围里，和优秀的人，一起做高质量、有价值的前沿研究，欢迎加入我们。**

**长按下方二维码，或点击阅读原文，投递简历。**

![](https://mmbiz.qpic.cn/mmbiz_png/ia00JJEEnxEkbciaVTgDlrbhvPzLjp2JUnZL3dE99UGLs9Yzia9On2nk4CF4A0h6Q4hib1HqvzMGXfH3GtXxo91rUg/640?wx_fmt=png&from=appmsg)

注：本文提及同学均使用化名。

****字节跳动更多技术应用****

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ia00JJEEnxEkdflMKACCibfCSBwaL7Eu2IpWiaspaNBiaF7eKbsywNvJ6nicFgl6oq2h2icyZj74Q2YedGNGvTUTiaPCw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzI5OTY2OTY4MA==&mid=2247490270&idx=1&sn=c5d16da6e95802cbd8fb0e66e14e668e&chksm=ec925b01dbe5d2173d0af6da648e1d69fe518838e18a6d10651a2b959304b63b6dc947a2d6e8&scene=21#wechat_redirect)

[用扣子 / Coze 揭秘吴恩达的 4 种 AI Agent 设计模式](https://mp.weixin.qq.com/s?__biz=MzI5OTY2OTY4MA==&mid=2247490270&idx=1&sn=c5d16da6e95802cbd8fb0e66e14e668e&chksm=ec925b01dbe5d2173d0af6da648e1d69fe518838e18a6d10651a2b959304b63b6dc947a2d6e8&token=377210967&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ia00JJEEnxEn1VtZDJYvyubpweJ05OpKmOXGjJ6USUQzuuqiaOMuW9eK09YxOhFnNmRNqSoFpkOvhnttQT4ONx9g/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MzI5OTY2OTY4MA==&mid=2247490332&idx=1&sn=40b5d983995d9b66fd105a45ad743e94&chksm=ec925ac3dbe5d3d5d5949e1bb925b6d6de893b1637cbc7971ee1c543e746cdada8756bc4a94a&scene=21#wechat_redirect)
[自回归超越扩散！北大、字节跳动 VAR 范式解锁视觉生成 Scaling Law](http://mp.weixin.qq.com/s?__biz=MzI5OTY2OTY4MA==&mid=2247490332&idx=1&sn=40b5d983995d9b66fd105a45ad743e94&chksm=ec925ac3dbe5d3d5d5949e1bb925b6d6de893b1637cbc7971ee1c543e746cdada8756bc4a94a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/ia00JJEEnxEnE1KQd4Y91V4mThiab0WXe7Q5jU5j3AbwnaTpicuMRkY2o4BgSBaafmAwXQKlaBgaPJGQgdKBLDg8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**点击「阅读原文」，一起来做高质量、有价值的前沿研究。**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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