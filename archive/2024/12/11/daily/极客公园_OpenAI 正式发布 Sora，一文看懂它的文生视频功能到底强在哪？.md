---
title: OpenAI 正式发布 Sora，一文看懂它的文生视频功能到底强在哪？
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653068676&idx=1&sn=2d238cc9de1d8e9837407fc38e49e9c9&chksm=7e57e03249206924439f5c8f8d9b68f96fd07dd3a6da6978a41558ec8d9e35841d77dbbb80f6&scene=58&subscene=0#rd
source: 极客公园
date: 2024-12-11
fetch_date: 2025-10-06T19:41:39.659180
---

# OpenAI 正式发布 Sora，一文看懂它的文生视频功能到底强在哪？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5Zv43L7SXOvkk4g4Bkq4bg2YRaAEVlTVMiaLy4LUOkT0XNdtYGjClqibxtNFAIia6U3Bic4fHpyRWbHTg/0?wx_fmt=jpeg)

# OpenAI 正式发布 Sora，一文看懂它的文生视频功能到底强在哪？

原创

黎诗韵

极客公园

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZnjRmooUC2j0F96ydT6A4nm1ggl27aH9TozUDNVh8ATNZ4jaAaLoPwWNdoDNq3sojaFnUYlR7f2w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Zv43L7SXOvkk4g4Bkq4bg2PE4ACB4m9JceUg1ibOhnmf0JXB7KMKHfmCOptOoDjsKEK4g1UQjsBlg/640?wx_fmt=png&from=appmsg)

除了视频的生成，还能进行视频的无限创作。

**作者 | 黎诗韵****编辑**| 靖宇****

正如外界猜测的那样，在为期 12 天直播的第三天，OpenAI 正式发布了文生视频产品 Sora。

北京时间 12 月 10 日凌晨两点，Sam Altman 和几位 OpenAI 内部员工通过直播，展示了 Sora 的功能和实际用例。继今年 2 月释出视频样片后，Sora 引发了全球人工智能界热潮，此后国内外人工智能公司纷纷推出文生视频产品。而作为这一赛道的开创者，今天 Sora 终于揭开了神秘面纱。

**整体来说，Sora 展示的一系列产品功能，表明其在视频生成的质量、功能的独创性、技术的复杂度等方面，超出了目前的文生视频产品。**

在文、图生视频的基础功能之上，它加入了故事板（相当于通过分镜创作自己的故事）、用文本调整原视频、不同场景视频的融合等功能（相当于给视频直接加特效），整个产品功能设计似乎都在让视频更接近创作者的自我表达、帮助他们完成一个理想的镜头故事。

当地时间 12 月 9 日晚些时候，美国、以及大多数其他国家的用户，可以访问官网体验 Sora。它被包含在 ChatGPT Plus、ChatGPT Pro 的会员订阅中，无需额外付费。其中，Plus 能生成最多 50 个高级视频、视频分辨率最高达 720p、时长为 5 秒，而 Pro 则能生成最多 500 个高级视频、分辨率高达 1080p、时长为 20 秒、还能去水印。

**Sam Altman 介绍做 Sora 有三大原因：**

一是从工具性角度，OpenAI 喜欢为创意人员制作工具，这对公司的文化很重要；

二是从用户交互角度，人工智能系统不能只通过文本交互，也应该理解并生成视频，帮助人类使用人工智能。这类似于国内大模型公司谈到的，「模型每扩展一次模态，用户渗透率就会上升。」

三则是从技术角度，这对 OpenAI 的 AGI 路线图至关重要，人工智能应该学到更多关于世界的规律，这正是所谓理解物理规律的「世界模型」。

既要用技术改变世界，也要用产品促进人类创造，这就是 Sora 在做的事情。

***01***

**生成视频之外，还能分镜、加特效、无限创作**

Sora 最基础的，首先是文生视频、图生视频功能。

打开主界面，用户可以查看和管理所有的视频生成内容，并且切换网格视图、列表视图，以及创建文件夹和收藏夹，查看书签等。研究人员称这个主界面设计，是为了更好地帮助用户创作故事。

在主页面的中间底部，是 Sora 的文生视频、图生视频功能。

比如，Sam Altman 先给到文字输入，「长毛猛犸象在沙漠中行走，广角镜头拍摄」。接着，需要选择视频的画面比、分辨率、时长（5-20 秒）、以及最终生成的视频数量（最多可生成四段以供挑选）等，才能获得生成的视频。

最终，可以看到生成的视频效果非常真实、有质感，且基本遵照了输入的指令。对于 Sora 视频生成效果的出色表现，或许人们是不意外的。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Zv43L7SXOvkk4g4Bkq4bg2MNJhfxMyhKn0xFFA0tcyn7ISSZibjZOe64HKoJTPq3rPpq3nicRx9BNg/640?wx_fmt=png&from=appmsg)

输入「长毛猛犸象在沙漠中行走，广角镜头拍摄」的文字后，Sora 生成了四段视频 | 图片来源：OpenAI

但此次，Sora 还发布了一系列独有的、进阶的的产品功能。在极客公园看来，这些功能基本围绕视频的更准确表达，也就是通过分镜、加特效等等方式，让人们能通过视频创作出一个自己想要的故事。

首先是故事板（storyboard），它被研究人员称为是一种「全新的创意工具」。

从产品设计上看，它相当于按时间轴的方式，把一段故事（视频）切成了多个不同的故事卡（视频帧)。用户只需要设计和调整每张故事卡（视频帧)，Sora 会自动把它们补成一段流畅的故事（视频）——**这很像电影里的分镜、动画的手稿，当导演画好分镜、一个片子就拍出来了，一个漫画师写好手稿、一个动画就设计出来了。**

比如研究人员设想的第一个分镜是，「美丽的白鹤站在小溪中，拥有一条黄色的尾巴。」第二个分镜是，「鹤将头探入水中，并捉出一条鱼」。那他做的工作就是，分别创建这两张故事卡（视频帧)，并在两者之间设大概五秒钟的间隔。这个间隔对 Sora 很重要，给了它把两组动作连起来的发挥空间。

最终，他得到了一个完整的视频镜头，「美丽的白鹤站在小溪中，它拥有一条黄色的尾巴。接着鹤将头探入水中，并捉出一条鱼。」

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Zv43L7SXOvkk4g4Bkq4bg25SteXRTv7kfgzO0wj1TRdTWEw06JnxnDZMbUJWniafR1I77hNlx9sgg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Zv43L7SXOvkk4g4Bkq4bg2vgNpIiaTkfZg3GLRBwqkpoZYIGYBz4Ha1OJNv3b9esBichnu9bnger7A/640?wx_fmt=png&from=appmsg)

通过两张故事卡（视频帧)，Sora 生成了一个完整的故事（视频) | 图片来源：OpenAI

更为奇妙的是，在这个故事板上，创作要素不只是故事卡，也可以是直接的图片、视频。也就是说，可以将任意的图片、视频拉到故事板上，结合故事卡，对它进行创作。

以视频为例，研究人员将上述白鹤的视频切下来导入故事板，进行了剪切，这就给视频的前方和后方留出了继续创作的间隙，也就是说可以有新的开头和结尾。

这带来的想象是，故事板可以无限的创作下去。也就是说 Sora 生成的 20 秒视频，可以被不断地创造、剪切、创造……直至完全达到心目中理想的镜头。**这个过程就像一个剪辑师、导演，通过对分镜设计和镜头素材的不断生成剪辑，慢慢剪出自己心中的片子。**

和真实世界中不同，Sora 提供的素材是无限的。而和其他的文生视频产品不同，Sora 的视频是可以修改加工的。这使得它生成的视频一定会更符合用户心中的想象、创意。

这似乎正是 Sora 此次产品的核心思路：尽最大可能地，让生成的视频符合用户心中想要的创意。

这样可以更好理解 Sora 的其他功能，比如可以通过文字直接修改视频、可以无缝融合两段不同的视频、可以给视频改变画风等，这相当于是直接给视频加「特效」了。而一般的文生视频产品，可能需要不断地调整 prompt（提示词）、不断重新生成视频。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Zv43L7SXOvkk4g4Bkq4bg2sXRC4V01eS4Oyjic9FibSXsYxRxMcezl79dHGCz3Dmsc7UicGYVXaV2Vg/640?wx_fmt=png&from=appmsg)

通过调整文字，用户可以直接调整视频 | 图片来源：OpenAI

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Zv43L7SXOvkk4g4Bkq4bg2cict5LDzzAEAy6KibYhwLzdNek0bZZzP0Wjqib8ILibtEhwiaPIWCEaqV8w/640?wx_fmt=png&from=appmsg)

Sora 能将两个两段视频合并为一段无缝剪辑 | 图片来源：OpenAI

总的来说，Sora 除了在生成视频上不出意料的出色表现之外，它还带来了更独有的视频创作产品功能，相当于给视频加分镜、剪辑、特效。这意味着，每个人都有机会创作出自己真正想要的表达，离当一个导演也更近了。

「如果你带着期望进入 Sora，认为你只需要点击一个按钮就可以生成一部电影，那么我认为你的期望是错误的。」OpenAI 研究人员说道。

他表示，Sora 是一种工具，允许人们同时在多个地方、尝试多个想法，尝试以前完全不可能的事情，「实际上我们认为这是创作者的超级特殊延伸。」

***02***

**服务大众还不单独收费，还是靠底层模型的能力**

作为文生视频赛道的开创者，Sora 的推出时间算是最晚的。对此，OpenAI 研究团队表示，为了对 Sora 进行广泛的部署，需要找到让模型更快、更便宜的办法。为此，研究团队做了大量的工作。

在直播中，OpenAI 宣布推出 Sora turbo，这是原始 Sora 模型的新高端加速版本。它具有今年早些时候 OpenAI 在「世界模拟技术」报告中谈到的所有功能，此外还增加了从文本生成视频、动画图像和混合视频等功能。这是此次 Sora 产品功能背后的技术基础。

看起来相比文字，视频的推理成本更高，但此次 OpenAI 并没有单独针对 Sora 收费。20 美元/月的 ChatGPT Plus 会员、以及 200 美元/月的 ChatGPT Pro 会员，都可以使用 Sora。

前者的权益包括最多 50 个高级视频、分辨率达 720p，时长为 5 秒，后者的权益包括最多 500 个高级视频、无限普通视频，分辨率高达 1080p、持续时间为 20 秒、并且下载无水印。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Zv43L7SXOvkk4g4Bkq4bg2gOWhibjdTSo4diay3uJOiaOctQsHcwb9El1tABHQ6q4w0dmicNsHRvpVhw/640?wx_fmt=png&from=appmsg)

不同会员对 Sora 的使用额度 ｜ 图片来源：OpenAI

Sora 对 OpenAI 的意义不止于此。团队发现，视频模型在大规模训练时会展现出许多有趣的新能力，使得 Sora 能够模拟现实世界中人、动物和环境的某些方面。「我们的结果表明，扩展视频生成模型是构建物理世界通用模拟器的一条有希望的道路。」

或许正是因此，让 Sora 尽快被大众用起来、用数据更好地训练世界模型，对于 OpenAI 最终的 AGI 梦想如此重要。

在迭代技术的路上，也顺带推动了人类的创造。

「这个版本的 Sora 会犯错误，它并不完美，但它已经到了我们认为它将对增强人类创造力非常有用的地步。我们迫不及待地想看看世界将用它来做什么。」缔造它的 OpenAI 如此说道。

\*头图来源：OpenAI

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**你用 Sora 了吗？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YD3rsTpUrmLXS1PBwt8rdOzNmdI4DG1M3BQouVPiaS3X34hnBC25s5OHc3de1EYgD9NCcJibueXqrA/640?wx_fmt=jpeg)

---

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZnjRmooUC2j0F96ydT6A4nHabbZDg2WLNfemu7N0f1DnqShdM9Rv8x2oRcnyAtiaQuicwrJJfBiaCOw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频**

刘擎：人工智能让年轻人恋爱更难了。

**点赞关注****极客公园视频号****，**

**观看更多精彩视频**

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdR72cJMO1LlDnqHHd65sWaQZqGKA5jL8UMoPJ0lY5HtnpR5EEjIQkibA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653067035&idx=1&sn=f91c596c85efad7c9fe8a5161757a8e6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdHHX5h2tNONfJjpAaBic8sH28fEs3XHnq0D95tvMy5qwZyeYria1zR1icw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653066772&idx=2&sn=35004897ecac7b77dfb4177197e3d4a1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

极客公园

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

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