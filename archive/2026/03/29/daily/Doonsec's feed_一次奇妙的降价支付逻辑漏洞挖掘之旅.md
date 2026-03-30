---
title: 一次奇妙的降价支付逻辑漏洞挖掘之旅
url: https://mp.weixin.qq.com/s/Etpy9YrD-LJ_kyTpA3abhA
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:45:42.845598
---

# 一次奇妙的降价支付逻辑漏洞挖掘之旅

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFFYcLKXg7LZQO5PpRwJwKJYL6EVFkmZq2xcicNGUA76cS2Kkzud4MtOw3xmP7G3kdbP5ich4GfsM5KibPkMmJicZKJEVCn6W5G0HGU/0?wx_fmt=jpeg)

# 一次奇妙的降价支付逻辑漏洞挖掘之旅

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器中沉浸阅读

## 前言

记录一次支付逻辑漏洞挖掘，这个支付漏洞很细，能挖出来需要十分细心和耐心，一点点看数据包，不然真的非常容易漏下，实际上这个漏洞的出现就是由于在确定订单价格时，后端数据校验缺失导致的。

这是一个新能源汽车充电小程序，出现问题的功能时购买电池的功能点，一开始选择购电，可以选择购买30度，50度，80度。不同电量对应了不同的价钱，30度电248元，80度是380元，这个漏洞的效果，就是通过简单的替换，将购买80度电时的价格变成购买30度电的价格，实现降价。

这篇文章将以复盘的视角，一边讲解利用过程，一边分析前后端支付发起逻辑，希望和大家交流！

## 渗透开始

1. 首先进入小程序购买页面，是这样的，可以选择三种不同的电量，预约购买

   ![image-20250226135515114.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFH7ojTS6G7GiaKtWcq6hic3WCWrSQURlXOibZZibR8J0adgyvTdGcTEA9icNYumNecvaBfLftbm55bFWXFJbLSJyPVCe3k1d6OqFDj4/640?wx_fmt=png&from=appmsg)
2. 之后，点击立即预约，抓包，会发现一开始接口会发送一个priceld

   ![image-20250226140916087.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHzeTwQQEETRY8uRg6Mr9bib2eo9wGSDVM37KEQISzssSeCUcfQ8o7zVic9DojpXl4p4zJxELnZYNQfrTibH2DjZ08PsqvRmuL70g/640?wx_fmt=png&from=appmsg)

   这个接口返回的是订单的价格，看变量名好像还有一些付款方式什么的

   ![image-20250226141031299.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFoR8xibkZVDF2HibQXZgBVCMT5sHtxfnssQZNb9p6S3YhKMYUhabFBaM7kGpY4Husibtmiaib6bHzgzqamWLYYIBOqz6Mb5dibU6ybE/640?wx_fmt=png&from=appmsg)
3. 紧接着，下一个请求，这里发送的也是priceld，请求如下：

   ![image-20250226141257987.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFE7pIG0xgf4qZ4FfNxYazHrgTSdqLV72AyRDkkibatFafGRmjIBxcej56Prcib5B4d3cd4zgicsn6nib6s7T63GaV5lpYljLmX6OuI/640?wx_fmt=png&from=appmsg)

   观察返回包，返回的是价格，猜测这个接口就是返回的当前选定项目的价格：

   ![image-20250226141453698.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEF6AXia7OicbAxLnOVr4torawZ2MN2RwqPRNNNEBVOnVlYCdXpkcE9oOAY7eHmWn6Fs4I4VtZW8snrgRB4kpqD6dTw2J95vneG8/640?wx_fmt=png&from=appmsg)
4. 此时界面来到了准备确认订单的页面，如下图，价格显示的是248元：

   ![image-20250226142256705.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFG1qibZehZSlbH8qqBlH9gPF4eSkyR0sphaj8svt6iaMSvvuPAF75DJ6jS32aMibibpE4Ric2eI86Z4h912DMFW421pTa4uZkwodvgg/640?wx_fmt=png&from=appmsg)
5. 到这里就可以思考一下这个过程，首先就是选择三个充电项目，也就是三个不同的电量，选择不同的电量，点击预约，费用是不同的，在这个过程中，主要有两个请求：第一就是最开始的，会直接生成个priceld发送到后端，返回订单的金额和退款规则等等；第二就是再次发送priceld，会返回当前订单的费用总计。
6. 那么这里我们就可以设想：如果我点击第三个，提交的时候第一个请求首先得到了他的priceld，但是在发送第二个请求的时候，我将高价(80度电)的priceld替换为低价(30度电)的priceld，那么是不是就能实现降价呢？
7. 实践起来，首先点击第三个80度电，点击预约

   ![image-20250226144324583.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGu5l0lBFicexmcaibpjO3su4JGTFI0AgNzgHLy7ElVO1VFor4jSGU6X2zQ7QNfBYPdKlutKICEMLyiaLFseiasKj50ibstd4k1hAE0/640?wx_fmt=png&from=appmsg)
8. 之后Burp拦截开启，开始抓包，首先第一个可以看到是生成了第三个项目的priceld

   ![image-20250226145403575.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGB5ZhlicEICaicx9mVEjEl1vKxuqFEHqPlGCvgBoW47z8ibYaibqSCySeCLCianOCKIawr26K0uBmyvsA0u2YXAHwuD9ia4C2mOW0Ng/640?wx_fmt=png&from=appmsg)

   观察返回包，可以发现也是第三个项目的度数和费用，80度380元

   ![image-20250226145456432.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGZYiacSXhdvmxQ1rUFoVRPIz9FVYbAiavEsVPribvA1VpubSTOhF8LSQQ0bjQDzAJhsNYvu6w0nv9eof3zONLo4YZ1jsZ02pMdQw/640?wx_fmt=png&from=appmsg)
9. 继续抓包，可以看到此时已经来到第二个请求，通过之前的抓包，我们把之前280的priceld，替换到这里来：

   ![image-20250226150233597.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEqoCuOVD2IfSTIzMX3xd7DSiaN69241fW60MNhBRkMqbdhvfdFmtZCu7FnArMbXVnH70xPgEY43U7NFdoPFTeUFz72ia5FHqQQY/640?wx_fmt=png&from=appmsg)

   观察返回包，发现此时的数值确实变了，变成了248元

   ![image-20250226150441999.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFevAJibUdc1HKX9YykMlZ0GdSOQEgeHPjZbzzT0eACbZO7icA0WibduAliaolp1Y18e5HxicKVRCj1Q7ozTVdltBr2MvgxlVl32UNE/640?wx_fmt=png&from=appmsg)
10. 此时放掉返回包，发现前端界面的数值也发生了一些变化，请求的服务是80度，服务费是340元，但是下面的费用总和却是248元？？！！

    ![image-20250226150610241.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGknicTfd4gLxhpAHyicdmuat8rBv3wrsL5y47Jiau8r3HpibS0Q2UwJs3ib2655uZtnbuBmcRATSicGNd0N8887CdqZByQwsu2uDFpA/640?wx_fmt=png&from=appmsg)
11. 到这里非常欣喜，再稍作分析，结合上面创建预约单的两个请求，可以知道，上面两个请求大概分别控制的是这些部分的内容：

    ![image-20250226151014824.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFE3dZjGAhSzAuD4XJlYiaibNteURWoboUmPicZsUmicSdrhMeMKd253bB3Z6uXQPAibFh0eAiaz7ibZwtaMgqQZOEWGbI4v7m6daO2vLw/640?wx_fmt=png&from=appmsg)
12. 到了这里，我们通过更改请求包的方式，实现了对价格的控制，按照经验来讲，已经离成功不远了，在以往的老系统，有很多的支付漏洞价格修改，信息修改等都是通过返回包来控制，这种漏洞在现在已经非常少见了，而且大多数修改返回包只是仅仅更改了前端的显示。很难达到修改实际支付数额的效果。
13. 继续测试，我们点击确认订单，抓包，看到了这些参数，看起来应当就是预约单的内容，通过变量发现应该是当前预约单的一些信息，其中还是有priceld，我们再次修改，替换他成为248元的那个priceld：

    ![image-20250226151510625.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGg5a7ugMic2B7iaWPJh4MhIwlkqxsmGyx9fpRRoEGRMoXGe4JC7Fic2TH5Lrib2Y1vROytubA6ia2OFjQMm9a5wgdmyvib3Az5vmH8U/640?wx_fmt=png&from=appmsg)
14. 更改之后放包，这里生成了第三方支付的二维码。

    ![image-20250226151552852.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHzW2SpaXqUweyWeNPvnicibspUicAoZZRr3PKhbc3UtficUdhlnZzsS1777K4vn8cm2WWOiaIOiaOC0D1c8jTreQLJld4Yjje5Z9LLg/640?wx_fmt=png&from=appmsg)
15. 扫描后，发现确实金额变成了第一种充电度数的金额，248元，说明该系统直接向第三方支付开出了248元的订单，至此，证明支付漏洞成功利用，已经实现降价。

    ![1740554435907.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEVccUXIODasZjusZFQT3AwRl6hiafBYfacqKO4pJxhPsibBfMnficl674CZfZkXF3kUwWxj2VEGyyg6fXtib4GcpuUhdZAoySJGmo/640?wx_fmt=png&from=appmsg)

## 复盘总结

读到这里，相信你一定有一种“茅塞顿开”的感觉，是的，这个漏洞十分简单，就是因为他这个支付金额的确认逻辑是通过一个金额id(priceld)，通过简单的把A产品的金额id(priceld)，替换成其他产品的金额id(priceld)，实现”使用其他产品的钱，购买A产品“的效果。

背后的支付逻辑大概如下图

![image-20250226163344720.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGC6K3icfZF17bbYTRKOgwx1apttMia7SQg2QAPF2cFjAQjJYrutWPYiaaTfOWo6YYwGic9hibOaXn5lMLja4wPME8Q5QW04Uf9lZ4Y/640?wx_fmt=png&from=appmsg)

因此，我们就可以通过更改第二个请求的priceld，实现了修改最终订单的付款费用，达成了更改价格的效果。

实际上这个漏洞不是特别难，但是经过调研测试发现，目前这套支付的处理逻辑有很多种，各行业的生产系统都在使用，面对C端的产品出现这种漏洞非常严重，同样根据这样的逻辑我们也可以进一步引申思考，同样的逻辑可能不光出现在支付过程，也许还可能出现在其他类似的例如积分兑换等功能上。我是小安，欢迎大家对本文章展开讨论，指点，批评，感谢你的观看！

原文链接：https://forum.butian.net/share/4204

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

只会看监控的实习生

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

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