---
title: 实测 MiniMax M2.5：它真的有那么强吗？
url: https://mp.weixin.qq.com/s/_7PJICKE2KHtkmUxcA58nw
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:12:32.880589
---

# 实测 MiniMax M2.5：它真的有那么强吗？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TLxcOlNibqP9xbzCF4QOwPkWkIYlN1ThccQeOWrJW45T7ibJ4RBSvv6K5d8l4Dico1jtMiaCcMq4V31XpMmEX9kYUWRYAQf4OmXb2TsD4Aj6eib0/0?wx_fmt=jpeg)

# 实测 MiniMax M2.5：它真的有那么强吗？

原创

天欣
天欣

天欣AI

![]()

在小说阅读器中沉浸阅读

说实话，AI 的发展速度，已经快到连我这个常年泡在 AI 圈子的程序员+公众号博主，都开始有点跟不上节奏了。

其是临近过年这段时间，全球的 AI 大厂都在卷，各种 AI 产品和大模型几乎呈现出井喷式爆发。

这不，距离上一代的 MiniMax M2.1 模型发布还不到两个月，官方又发布了旗下最新的模型 MiniMax M2.5 。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqP9Pd4Yic7czJ1nBJraKZQ7ev1MnwL767rN4YpWSzticSIWHjhn7qJzNhPlxrfNzBO4C9cpV9JGkosxmCWiaPyPIvJpibO5VqTuOcmc/640?from=appmsg)

官方的体验地址：https://chatglm.cn/main/alltoolsdetail?lang=zh

几乎在同一天发布的，还有 GLM 5 模型，而它距离上一代的 GLM 4.7 模型发布时间，间隔同样还不到两个月。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqP9E3pLzic5XvNCQMgWyTMhkMedGpMNYB9wMqT6MSn3QRjkLlPsNyca3DMD2ENmGncyPmLyXQomZiarmia0QwrXKc4InXKDLJZFwJo/640?from=appmsg)

官方的体验地址：https://agent.minimaxi.com/

最近 AI 圈里有个挺火的“洗车店”问题，具体问题是这样的："我离洗车店只有 50 米，我是该开车去，还是走路去？"

很多 AI 一看到"只有 50 米"这个条件，就直接给出“走路去”的答案，但却忽略了去洗车店的目的是洗车。甚至连国民级 AI 应用豆包，在这个问题上也翻了车。

![豆包覆灭了.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPibDorkIyo8jPHJJO7ia2X85j5gv7OA6yc9fTHOcC7nDyicvV79ApO0lpb7icG0ibJMDKb2xmcSUWfj8AXG4scvGdxtlIMZcd7Rhj68/640?from=appmsg)

我们再来看看 MiniMax M2.5 模型这边的情况，我没想到它竟然也和豆包一样，掉进了这个问题的陷阱当中。

![m25洗车问题恢复.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPibmNiciaoPO9ibTHNcE9YGjFFqmBMwn6YpG69JHzAgh4m5vSVRBeolvsD4qkboibwtjExiajFBHggvz75gWcSdfAjTeLGU7QrFNKv78/640?from=appmsg)

这类脑筋急转弯的小问题权当给大家添个乐子，我们本篇文章的核心重点，还是测试 MiniMax M2.5 的复杂任务处理和编程能力究竟如何吧。

我们可以先在官方首页体验一下 MiniMax M2.5 的任务处理能力。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqP9OMNvp3YsQWsweSzDCdGiarjxPEaYEWYdxSFDnUfxQ5EBKTKia4zlkiaIJKGQ5bgmUicVf81M2dbU9iaQFoQU8JHNxLdbOnRAqMicsQ/640?from=appmsg)

官方地址：https://agent.minimaxi.com/

我最近在开发一款 “拼豆” 的辅助工具，所以我让 MiniMax M2.5 给我调研一下用户的痛点，给我一些功能上的建议。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPib9eiaUyZsm3F8FFTEzP6ibc9EiaPGibkvynM906S3cliaHGJmP8DrGIMcxLiaeVaqgo0qTrHwnMjCVr51TibGVwPPPnEGFhXQUUZia55k/640?from=appmsg)

最后从用户真实需求的角度，给我写了一个非常详细并且实用性很强的痛点报告和软件功能建议。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPicBicGwibiaicCibUgerJTvyGCTUI3hcsFlOhglibaKG2T4bayaKX90ibFokmD6jF3gwF2Pf2gxIiavoejQ6sowm5ziarUGzXESE6m88Mcc/640?from=appmsg)

接下来，我们来测试一个打工人最常见的场景：分析 Excel 表格，看看 MiniMax M2.5 的表现到底怎么样。

这是一张虚拟数据的销售数据的表单，大概有七百多行。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPicT6ibEzU0rAOv1ct3Gj6Csyux3uoM3cVn3x6G96D6oLOcrS7wRueNe6oh5VXibsqwy4vUsricIC3fKQtTJQQ3bSPZPEs8dWzrXmA/640?from=appmsg)

我让 MiniMax M2.5 给我分析这个 excel 文件，然后生成一个可视化的数据展示页面，最后的效果如下， MiniMax M2.5 使用了专业的柱线组合图展示了 excel 表中的数据。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPibkRLFzg9n5P064qfuHyoVwkbqqLogEFSUGyicUnoRkqdFmVpF72E8nNFLctNcJfjKk21y9xvmibtsiaotP67AeFziazxrQia5h1lzA/640?from=appmsg)

接下来进入重头戏，我们来测试一下 MiniMax M2.5 的编程能力。

这里多说一句，小天本来打算对比测评 GLM 5 和 MiniMax M2.5 的编程能力的，但是最近 GLM 5 编程套餐的购买人数实在太多了，导致官方直接限购了，小天也是好几次都没有抢到了。

![套餐售空了.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqP9OLknwfDTibZwYq5UevWgSjdkfuWVTgaiat4MXCZxSI7VkMujNqicBgQ9OHRzkacOwM2lVpLdTRhQt2EpUiaulibxFullAzGSuic39M/640?from=appmsg)

官方优惠购买链接：https://www.bigmodel.cn/glm-coding?ic=LKCFRGKH9N

而 MiniMax M2.5 这边倒没有出现这种套餐售空的情况，反而可选择的种类非常多，除了常规的 MiniMax M2.5 模型的编程套餐之外，你还可以选择速度更快的 MiniMax-M2.5-highspeed 模型。

![minimax2.5.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqP9BFticNcXSCE0SicQ1fqRjDLtZGbgcsVibhbjia7sBJPCkZs7La8PiaBbbSwic1xSam5SbpjqKu4pRIYibOSrQqyLCecTC7UW5qq7s5Y/640?from=appmsg)

优惠购买链接：https://platform.minimaxi.com/subscribe/coding-plan?code=aup5kDN5Z6&source=link

所以篇文章就只能带着大家好好盘一盘这个 MiniMax M2.5 模型的编程能力了。小天在这里和大家承诺，本文的测评绝对客观，不会存在任何鼓吹的成分。

官方给出的比分排名中 MiniMax M2.5 的编程能力和 Opus4.5 表现相当。

![](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqP8L38XGvbZHKicW4Z1JxuodjhRYAhnbMoNwJASP6x8e1ibZ3cvOwFpZHokTCcjeYhOtj2d9byICXibJ1dPShibZUcM6TRUD8a967u8/640?from=appmsg)

小天这里建议大家将 MiniMax M2.5 接入到 Claude Code 中使用。

大家如果不会配置环境的话，可以使用小天 AI 编程群里的 Claude Code 启动器。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPicMn59icDlHaNPN3plN6KlgrzthickM1kX6KaP0dBZUibhWKQticiafgkvraNTahWFuTBa8LbX3V29j8FYJkkOT0GfHLGfKRz9zIoVQ/640?from=appmsg)

如果第一次使用，大家需要配置一下对应模型的 API key，这些 API key 只会保存到本地，还是很安全的。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqP9uUicxc87pSaDYDcsibdLydN4gIu6s9R6Vd1UicXxFl7O7MUHJGicnnPSt43gKYnDuYLOKmGIMJEr4adOia3siaPA0SRGZwd3yM0Koc/640?from=appmsg)

如果没有进群的小伙伴，可以私信回复【加群】哦～

当我们配置了对应模型的 API Key 之后就可以按照你选择的模型一键启动 Claude Code 了！最后的效果如下所示：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPicOurT0iakpdI95BF8jhJZUnbmtFb9RYicEm41Xxs3kem8ibVBONcLCgxuO1BSZKy4WU1An0RHdldicbbWOechK9HEl1M9NJ6Nf3vg/640?from=appmsg)

我们测试第一个编程例子——编写一个童年经典游戏：愤怒的小鸟。我让 ChatGpt 写了一段提示词，如下：
![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqP8bGCnPKlzkeYQHJOoH0rB1699TSMocNhQsLib8xVWRB1ndj32flt83L9qoMcwUR473hdBI7VKREmcicGkcLbM0cGxVsetK4ztE4/640?from=appmsg)

将这段提示词喂给 MiniMax M2.5 之后，它生成的速度非常快，但是首次生成的效果有些不尽人意，无法正常显示小鸟和小猪，也没有办法正确玩耍。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPicosEGIczxria5lmH43ujvssDH72FZJflRe5JPFHibC1uicmt0ktTHfdGU3eATvOT6ib5FibKpFnbGia6Y4iblolbb6N5ap0JeZ6ZPndY/640?from=appmsg)

所以我又让 MiniMax M2.5 修改了几次，最后生成的效果如下：

![能玩.gif](https://mmbiz.qpic.cn/sz_mmbiz_gif/TLxcOlNibqPicuNuI36gL7BvDR9jtwbjaLiaOSLbPbibq5fydyWYiaB3kj6SuefibMkHia9lpwGPYxksjuOMzXBFWqiazJ0dFEwicIgxoz1oC0vlCGbA/640?from=appmsg)

我们再来对比一下其他模型的效果，下面是 Opus4.6 的经过几次调整之后生成效果。

![opus4.6.gif](https://mmbiz.qpic.cn/sz_mmbiz_gif/TLxcOlNibqPicUrMsvU5KnONuEv3zm4V5dlkWdp0ecPicIAiaKAHKXUGkJO7O1rrEMp7QnWlia9mDohRywR5ehhoxzG8Z3JGsibzxn0bcCTiaa4eWc/640?from=appmsg)

从物理引擎表现和整体游戏机制来看，Opus 4.6 的生成效果确实比 MiniMax M2.5 要好上一些，但整体差距并没有我原本想象得那么大。

总是纯前端的测试有些太片面了，下面一个例子我们测试一下 MiniMax M2.5 的前后端这种全栈项目的编写能力，具体的项目要求如下：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqP9WwTWx0icePCWWibWyvyqOD6tlcRce4Gly1bG1MgMrEXJqw70HmvTnvk7phZIic79BhaR1iblheLs7NqKrO27T2A43ibmGAI5Lhjjg/640?from=appmsg)

最后生成的效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/TLxcOlNibqPibb93Kf37ib698qTNiaPWwniaSiacCyoibhicL9QXRiawjgJzqrNwkASIzJP969pyCicWDd3bHeO7zmNg3KW9ujTCH3u4Zy1bhHYHVGn6E/640?from=appmsg)

最后一个例子，我们来测试一下 MiniMax M2.5 的算法编写能力。

最近的拼豆非常火，所以我打算使用 MiniMax M2.5 复刻一个将图片转化为拼豆图纸的小 demo。效果出乎意料的好：

![拼豆图纸转化.gif](https://mmbiz.qpic.cn/mmbiz_gif/TLxcOlNibqP8EZCNPtmFT83g5micGLgRia4wibBFWgiawgKzheX879GYKyttpOlhe5VWZSCDibfcmPu1BhJhskiaibHUx5ssczicIUz9X5VRCVZguNLU/640?from=appmsg)

别看只是一个像素图纸转化的功能，里面涉及到的算法可不少，我让模型给我总结了它所使用的算法，如下所示：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPibhp8jIxcMQE6hich5heTfMxTCBaQLwQooLDCHwiawQwbQqvGdJz4UmS43iaGURicomAJCQgXSPqnpVRmGldjuRK5WnMicnQVDj4MyQ/640?from=appmsg)

总的来说，MiniMax M2.5 这次模型的能力相比较上一代提升非常大，但是和国外的一些顶尖模型还是有一些差距的。

不过，好在 MiniMax 属于后起之秀，它的进步速度是相当快的。大家可以看下面这张分数演变图。

![](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPibCrKtzkJsWhia8pST3VaGHdEbou89HHbhIIc5M4QiaYE0Uq6uVIPIj9MibV6iaOvPwMv9jRK04ngWwuJnWOWxA9LKbzDmwwmQh5RU/640?from=appmsg)

我相信总有一天，国内的大模型的宣传不再是“接近” xxx 模型，而是 “全面超越” xxx 模型。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNz2bAzZDNvNXR9yvPBwu4HyfdFk7GADDDIbK5DWYWHQDoyyiauJY36pVkQZ8sATZZDRMpbczyBWmJw/0?wx_fmt=png)

天欣AI

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNz2bAzZDNvNXR9yvPBwu4HyfdFk7GADDDIbK5DWYWHQDoyyiauJY36pVkQZ8sATZZDRMpbczyBWmJw/0?wx_fmt=png)

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