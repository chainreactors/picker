---
title: no money 获得openclaw同款推送
url: https://mp.weixin.qq.com/s/4c7pRNi2Ti45ItuKJNSiGg
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:27:22.217076
---

# no money 获得openclaw同款推送

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nUP9S9ZvnnvRGF6kBGlEp22QBsVLbg8Fp3Id4eODTG5es8Lz6bkqtLlXcDTlnxVfLibYLKQiabDIicfibLoRfCibS9ibYT3GfZWpMVtsqA7iaCibyDI/0?wx_fmt=jpeg)

# no money 获得openclaw同款推送

小叶Sec

![]()

在小说阅读器中沉浸阅读

以下文章来源于雪中茉莉
，作者雪中茉莉

![](http://wx.qlogo.cn/mmhead/00GYaClAoOpLgaBjsoNia4Uglz9iaibRuUhGhmm8ocxu28BeMaSkIibHVoHicib3Guc6jUwB2Tk4QafME/0)

**雪中茉莉**
.

每一个漫不经心的今天，都算是未来的一部分。

## no money 获得openclaw同款推送

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nUP9S9ZvnnsyzbxeDCUa91ROlr8Gfia20b6gto6Z97icPoAsdZv56T0btbkfD4iah1EQiaiaSmKAeQNOWB8Ru9kzPo9pOicQNv0dsAiankzV5jNbdg/640?wx_fmt=png&from=appmsg)

笔者没有跟风`openclaw`，我认为`openclaw`对于一般人来说用处其实不是很大，都是一些噱头，但是技能装的越多确实越厉害，token同样越危机。其实也有解决办法，例如采用GPT号池来反代出api🥰，还能用最顶级模型，还是那句话我懒得搞。

我又想获取到`openclaw`一样的定时推送，其实这个功能很早就有了，但是之前的需求一直不是很大，下面教大家如何进行推送。

### 飞书配置

笔者这里选用飞书，当然你也可以选择钉钉之类的。

首先我们创建飞书群组

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nUP9S9ZvnnuDwP8qQvcwG3gbr78VgrGqDQKPHcv4HPvv4aTVqZnI9iayUwMfI6QO88ica4PAFsQDZy3nibE8bJEb0nfSuWKs9fJFJ0Qx0oNAicI/640?wx_fmt=png&from=appmsg)

之后进入到设置中添加机器人，之后通过webhook进行交互

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nUP9S9Zvnnvfsr0dOZNBhNkyu78ODDtpttSCjWrpdXhUEOsySiaskCbjcB9oZhV9sgq5lqJglTySAmGfWJGUokqjnYvBnFGRTYfRL5BeQLA4/640?wx_fmt=png&from=appmsg)

选择**「自定义机器人」**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nUP9S9Zvnntv7zkw0ibhmSQqia1OUPZYaeiaicoibNoU8V2Nq5TxcvBmTrX4ZTk1xiaicxQFbXsScpOIVqdkvWlF3A3k7GTjptrhcJuicrFgQbu4bick/640?wx_fmt=png&from=appmsg)

添加完之后，我们就可以获取到webhook的链接了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nUP9S9ZvnnuSQF2eT76OND32QCJ0VwPWicYjZZ2p2piaRW8xYHUn2MgAF1Xx0bygLHrj61kq8o4sMpibuIvopvLHiaicMiaZmJWiarsyJbBv0icWarQ/640?wx_fmt=png&from=appmsg)

### Github Action

这里采用我们的`Github Action`来执行我们的自动化任务，当然你也可以使用`Cloudflare`的自动化这种同类型产品。

爬取你想要获取信息，笔者这里就是为了获取ai资讯，但是每天看x，微博之类的太累了。

我决定直接爬取一些聚合站点，这里就不告知爬取的是谁了，避免给到他人服务器压力。

直接让`codex`帮我写好小脚本，同时通过mcp传入项目，记着这里选择**「私有」**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nUP9S9ZvnnvrUr0xJkk6X2icyxVBfedjXsxv1cH1iaGZXzqsZtTCK0Ric0wtzyJlxOUa7muZXHha2icXOJ9X6SnWDIzQwzytiaE80tiaq6gx6RqDc/640?wx_fmt=png&from=appmsg)

直接将我们刚刚拿到的webhook地址丢给`codex`就好。

他还会帮你验证是否成功，最终效果如图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nUP9S9ZvnnsaTiblNYoWBTpUx5Tzx2LoVeKItwMvTK56tqDePZYUQmJjFibfhpKibpUpW1icIy15R1Aib7GSgtsKhwpMXsIicO7A0KxC1mtYF8cB8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/nUP9S9Zvnntn6M8Mu5St2v2XYFMsFFvibtciaI74AVN9MI9BTy7Rp0VR38ic5F3z8hzabCjFgJuQq7QOWzfFbrsMEbp8e8A3MrM9gicDFHSTalI/640?wx_fmt=png&from=appmsg)

### 扩展

当然这里如果你想要获取最新资讯，不吃二手信息，你也可以自己写一个消息聚合平台，实时爬取各大网站的一些最新的ai资讯，还可以配上一些本地小模型去实时总结，之后同样可以通过刚刚的飞书webhook进行推送。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7cwYsJwE4IyPczNesOwRdnluVLvWzdawcOwwibmTlUeEhIhM8kTYj8XgMe87atk9icaFOGu6icVZ09msmzgL2X7ww/0?wx_fmt=png)

小叶Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7cwYsJwE4IyPczNesOwRdnluVLvWzdawcOwwibmTlUeEhIhM8kTYj8XgMe87atk9icaFOGu6icVZ09msmzgL2X7ww/0?wx_fmt=png)

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