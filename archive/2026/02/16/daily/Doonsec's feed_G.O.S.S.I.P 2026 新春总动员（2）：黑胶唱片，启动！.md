---
title: G.O.S.S.I.P 2026 新春总动员（2）：黑胶唱片，启动！
url: https://mp.weixin.qq.com/s/6fkU0hgBfVKdV2PTun2LuQ
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:16:11.601976
---

# G.O.S.S.I.P 2026 新春总动员（2）：黑胶唱片，启动！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eQ0Wf6rqolUcwpn5opwzPSl5E9U9xN2FBH7X6Liak1pGMkicU6GKTIibZ6f18UZXSofWUCeIL11DZ8n95miaCduojlHsH7vDNiaACUicGsOmeTtB4/0?wx_fmt=jpeg)

# G.O.S.S.I.P 2026 新春总动员（2）：黑胶唱片，启动！

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器中沉浸阅读

今天是除夕，G.O.S.S.I.P 编辑部首先给大家拜个年，祝大家新年万事如意（这里就不再贴AI生成的图片了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVzFicjDLFroxpqYIgWickqkEMqBib4RvssI1MMESuibxwrTu0yACsjWxd4WcVY4tKXiaDexQetIQao5u6c3cycwbEONlJha4RPNibSg/640?wx_fmt=png&from=appmsg)

---

黑胶唱片是一种传统的存储介质，和数字化的存储介质不同，黑胶唱片是用模拟化的方式（黑胶唱盘的凹凸）来记录声音，因此具有独特的质感和声音特点，也吸引了一大批的拥趸。

虽然我们很多人都是木头耳朵，但是这并不妨碍我们把一首歌转成数字信号，更重要的是，这声音可以让一台40年前的古老机器——IBM PC Model 4860焕发新的活力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolWOiaR4kKHIJUvic2skfOEkgtExZ1liczswfUSSicmmvKhibUHn3nBLpgAiaF0Mib0d2L77mbIumzgkVwbmQiakYPROjNtFAUhBHyQiahaw/640?wx_fmt=png&from=appmsg)

IBM PC Model 4860是IBM在1984-1985年期间推出的一款（很不成功的）个人电脑产品（如果你想了解更多，可以访问这个网页看看更多的细节：https://boginjr.com/electronics/old/ibm4860/），它的神奇之处在于原生支持盒式录像带（cassette，知道这个的读者可能已经不多了？）作为存储介质。而我们今天介绍的这个故事的主人公Jozef Bogin甚至还不如这台电脑年纪大——他是一名来自斯洛伐克的31岁的工程师，他的爱好是研究复古计算机，之前曾经制作了一个支持FreeDOS的bootdisk——BootLPT（在作者的另一篇文章里有详细介绍： https://boginjr.com/it/sw/dev/bootlpt-86/ ，本来是支持IBM 5150 PC的），这次直接把BootLPT移植到了黑胶唱片上并支持4860型号~

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolU9XrjgRo8pKQQDl1bAicXTwAD1XgN4iafZmt6zmJ9oiaOhJKkfFIM3OSV5ogG8Md2GQg7xHPKAASk2Lba4Q18HA7iaHosdp2bib8Q4/640?wx_fmt=png&from=appmsg)

把数字内容编码到黑胶唱片上很有意思（也颇具挑战），首先是要考虑到后续怎么读取，不过IBM 4860很厉害，它的BIOS支持原生从录像带接口读取数据并启动，因此只需要把唱片机的模拟信号转接给它（有一个“IBM cassette tape”-protocol 直接可以利用）就好。不过这里我们要考虑到黑胶唱片会有失真（数字信号表示我不背锅），为了保证数据不要出错，这里还要搞一些Hi-Fi发烧友的设置来保证数据能够无失真还原（应该是调整了采样频率之类？），这些内容我们并不熟悉，如果有熟悉的读者欢迎看看原文并给大家介绍介绍。

最后就是直接播放声音然后让PC启动了！大家可以看看前面的视频，当然也可以去下载这段bootloader+FreeDOS kernel回来当成你的助眠音乐！

https://boginjr.com/misc/bootdisk.flac

是不是很有意思？你别说，我敢保证AI肯定会很喜欢这种声音的！

原文：https://boginjr.com/it/sw/dev/vinyl-boot/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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