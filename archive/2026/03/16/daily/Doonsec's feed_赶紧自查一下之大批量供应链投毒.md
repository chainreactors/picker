---
title: 赶紧自查一下之大批量供应链投毒
url: https://mp.weixin.qq.com/s/QzCsVKKt1-Ju_V0qdHWi_Q
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:11:38.893115
---

# 赶紧自查一下之大批量供应链投毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/72I8gAalpPX1d64t8IWd3ia0P6XbhtNzhd9ULR5qO84ISHicwSwofpsEZeCR3kYFpiadSyCzd8ibdUhjiarVcwJIMib3LJYsPVu676NyzXcnDnTb0/0?wx_fmt=jpeg)

# 赶紧自查一下之大批量供应链投毒

原创

pippybear
pippybear

安全无界

![]()

在小说阅读器中沉浸阅读

最近公司部分github仓库忽然爆出一些奇怪的文件，开发大佬给到我后，也是第一时间分析，发现确实是木马脚本。关键是这个脚本是咋起来的呢，按道理不应该呀。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPX4eE16w6WFYEWhYEep2E4RC9oGuIJAskY9gnQNYx5vlF4Lhe3clLDKnlzicJYedoR2O4SwWtqclYPEaAg1g0HWyWrGUrF6S1XY/640?wx_fmt=png&from=appmsg)

看了一下github的commit，发现是某位同事强行push到主分支的commit中携带的，看到这里的时候，心想完了，同事电脑中毒啦。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPXVunNXsUGnqV37xS8ricomzia1fGqfN3uBOficCNxNrFcZfJz1S3nWOovvNaHZ14B1yiaf6R6lU70oDqqsClrXicJsChdVznCto2h8/640?wx_fmt=png&from=appmsg)

立马跑去同事那里看看他的电脑情况，结果一看，还真是，存在一个持久化进程（node -e “恶意代码”）。并找到持久化进程的plist，进去一看，好家伙。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVTmxXxFdtMNP7TEXV2dyiaOY2OKuxZg1pIezjgeTBU7B5murc8mZ1mwDxSJI9NxsCexRicA8379ExGXLEyYjicWzIUKn5ftgWJa8/640?wx_fmt=png&from=appmsg)

删除掉后，确定病毒程序不再起来后，大概分析了一下这个恶意代码，大概行为是在被感染机器上建立外链，并提取敏感信息以及安装一些浏览器插件来提取request数据等，另外就是挖币（emmmmm）。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPXzDGOOkRg6u4iages4POq7rlLBm29pOVNAFmu42NWbmcxtUFqgSwTlqHOsYqcYCwjVtOWouNkHeAI5ThNQJkhj1PSvXu11RQa0/640?wx_fmt=png&from=appmsg)

回过头查了一下github的log，以及机器log，行为在发现前就已经依稀开始出现，好在排查风险的时候发现这些被push成功的，最终ci的时候不是被拦截了就是报错了，没有真正push到应用环境中（不幸中的万幸）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPW6rg7BAwbWm2hfEHaZqxJcficVyeKoHeooLSX1earqo8LlSoWFE0pJlEgt9ia1SDWcnJgrJwicJTI2ZtCKYACtd9jCfl08GN2lzw/640?wx_fmt=png&from=appmsg)

但是通过排查却还无法明确定位是什么依赖组件导致的。github上一搜，好家伙，这是集中作案呀。

Python木马检索：

```
eNq9W19z3MaRTyzJPrmiy93VPSSvqbr44V4iUZZkSaS
```

JS木马检索：

```
w=w.codePointAt(0),w>=0xFE00&&w<=0xFE0F?w-0xFE00:w>=0xE0100&&w<=0xE01EF?w-0xE0100+16:null
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVvJ4bADXMPH6kiasxEndtc82zGzgYOqLHXymXZkVRJqLVUlfd1qonwVFesUqPgoLI8GyvEDrTgI7vI5RyegmcT9yvU79C8z8LM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPVaoUkc8umtxvorPk5UbMOibK2cFQfv3yomBmTjnT0v1MltM94fRCpic95mkkwib9icyqicQzfpORUkjW1icDRRx7NG9CkKd7x7icz9F8/640?wx_fmt=png&from=appmsg)

简单查了查发现是源自GlassWorm的一波大规模攻击。集中在2-3月，看中招的不少，很不幸里面有我们，又很幸运的是影响面可控。简单看了一下Extensions，高达72个，各位大佬也赶紧看看自家有没有被污染吧（被污染Extensions地址：https://socket.dev/blog/open-vsx-transitive-glassworm-campaign#Indicators-of-Compromise-）。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gRWFX6SiaQE368qzz3ruUmbnpAzmoIcmWYrXOnic1DzRllicgLMZ3NZ49q4CG4Tq7mmIkL8oyibfLfMqw/0?wx_fmt=png)

安全无界

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ib9b5DLqe7gRWFX6SiaQE368qzz3ruUmbnpAzmoIcmWYrXOnic1DzRllicgLMZ3NZ49q4CG4Tq7mmIkL8oyibfLfMqw/0?wx_fmt=png)

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