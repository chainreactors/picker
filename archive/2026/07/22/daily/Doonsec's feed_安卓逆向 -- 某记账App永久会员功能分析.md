---
title: 安卓逆向 -- 某记账App永久会员功能分析
url: https://mp.weixin.qq.com/s/KAWJI0MHsmpbsGRzmx6_cw
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:07:55.102234
---

# 安卓逆向 -- 某记账App永久会员功能分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Gv6JExJQjUXlzRpAhKjiaZib7pM1O715gjibKtLcrPUUkezapaVYjeyYjBSy1BETX21RIgEeYciczrMZhX1eAjYTkCW7wYibDYgMOBxhaInPzlIA/0?wx_fmt=jpeg)

# 安卓逆向 -- 某记账App永久会员功能分析

seventeenJoy
seventeenJoy

逆向有你

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明：本文仅供学习交流使用，所涉及的APP和破解版均不提供下载渠道。所涉及的技术请勿用于非法活动，否则所带来的一切后果自负。

注：所有与软件名称有关的地方已做模糊处理，请大家也不要在评论区分析app名字，毕竟软件开发者制作不易，请不要大量破解。

我们要破解的是该记账软件的永久会员功能，这个app会员判断逻辑写的比较简单，大家可适量拿来练手。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUVAG3PDHlYfb2eeTpzZ3JdbZ5djqaIia4f3qHXUgdS53KfFWdAkT1lHvic3fiawZlVsGEyzhAZ5kvkXmbVYmMxQHntdn0ibgs4ic8ec/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUUK3cJHMpKFHEla1g96YynDkP0au9OUCpaldAftrxej8PUH3m63K5STGzELGxYylKTHDhsKJtvTDA9yvFhSibGquSiaF5T8iaOk8I/640?wx_fmt=png&from=appmsg)

我们这里使用NP管理器进行软件代码分析，当然MT管理器更佳，这个看个人。

首先我们发现此App未进行加固处理，所有我们可以直接进行代码分析；因为我手机已经有了破解后的，所以我在原版app后面的包名添加了"original"以此作为区分。

我们直接全选dex文件：

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUXfViaw0ucoLicWYgmoiaELiaAUFZWAVQxaVblWc0H65JkibfUBhgbQvL8Qmqd484bNX1AF9SeNuUmRUOjFIacsav7mzKveWdbImlDQ/640?wx_fmt=png&from=appmsg)

在dex文件全选搜索“isvip”这个方法，这个方法并不是app判断会员逻辑通用的，也有ismember或者其他名称，这里也是试着搜索这个。

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUVuwea9oK2H81xsGDEGFJpSmDNC7vaobBuyJ5gCUbicYZJdaNQ9tT4zxuSrnaXz6ZnDZI4K5XFmvGtEtkDzswTrjHBibhjnZPBm0/640?wx_fmt=png&from=appmsg)

搜索出来的结果有五个，我们重点关注VIPHelper这个类的isvip方法，点进去smali代码进行查看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUUDzoYdic1zpCDzTkU42E7yK03cmEFatpQf5HjtcOfMty1E2oDtxV1Utg5VHxwGADDTeYqbYkbOEc13icHnw74iaLfe887EbPCLiaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUUbzU91cC8lThprvhsuYFozMmUCXdDibDfIAfENbdibqfMl0cEqdvAKIVMmopJhwr7keu6ib25uicfWcmN6WwRZHFmLU7DOHNWXVmI/640?wx_fmt=png&from=appmsg)

有些朋友可能不熟悉smali代码，我们可以点击上面的导航按钮，然后长按该方法把它转为java代码查看，NP管理器转java是免费的，而MT管理器这个功能收费

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUXJ092ibfUxbXMV9TNxAvCcsmmF9krQicnMhRIB6aM4cwQTcBEyWpXatViaFGcbv0icvZ8yFiafNl0bYkrOIOBRbo2dia1B23MHm03WQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUWoJbMB6PxfPtr3bcRonDowVBicOSjPIC8B2lPibtDelsibKqGSLBLALzD2LPYibPkiaUofvrEWFT9Tr8xjHoWWFNyY3EjX68pe92WA/640?wx_fmt=png&from=appmsg)

为了大家看的清晰，我使用jadx把这部分代码给大家查看

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUWvGoicH1XSCOMM591DR8EEjqqfDvFNCEvdgBf6HX0no7ZKX7icJLSZckZXmh7kJDySXYF2PTrhklRLKdlYRicJCKRbafamabRhAY/640?wx_fmt=png&from=appmsg)

这里的逻辑就是判断是否登录，未登录直接返回false，如果登录进行判断IS\_VIP这个变量是否为true，下面的逻辑就是判断vip类型，比如你是月费，年费还是永久会员之类的。然后关注z这个变量的赋值，它是通过判断我们vip是否已经过期，但如果前面是vip也不会走到这条语句了。所以我们直接在smali代码里面让这个isvip函数永远返回true就可以了。

```
const v0,0x1return v0
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUXOpiazMofWs6ZFiaKtqVKNV20ibvBtGcbqr3z2ib41koTtW3Ne1icyU8Qmbp55UahFMI7q2UsBzTF7qSOYf7NCTFsb5Ds0pAZnPY90/640?wx_fmt=png&from=appmsg)

然后我们继续查看VIPHelper这个类的其他方法，发现还有一个isForeverVIP方法，我们猜测这里判断我们是否是永久vip，也给它在smali代码里面返回true，还有一个isOver方法，看逻辑也是判断我们vip是否已经过期，但如果我们是永久vip的话，哪还有过期这一说呢？这里可以进行修改为false，这里不作修改。

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUVtbW9NGJUj32utKD7dIFXZa0PLDETyluj4cXdRU0eu26Jae9dou3nW97xLTc2fj5vUPrCAZWBSkqr37jVqXeLiauBrg5ykRR3Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUXzt3LzRnuloswdFY8IklOicE4Aq0gYDanzkx1RcdeXIhtbkPvkGF20dqwBO1DGQgN9OqGfc4SB9G6r8atbjfyA8sY0Q93YD2W0/640?wx_fmt=png&from=appmsg)

我们改好这些以后一路返回点击保存，重新打包以及编译签名app，随后进行安装即可。

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUWYum2JENAdpGiabesaNA6ybSUsYuNSEXntnQbEPRfia1HIWWoafN23MeGYrXXdsibrib41SicZUHgjibibZJNsLdgEbSqBqiaOa0iawF7c/640?wx_fmt=png&from=appmsg)

安装过后我们发现，主页我们就已经是永久会员了，那么是否真的可以使用会员功能了呢，我们还得进行验证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUXehmcvNDqEpNqdaBibOhwfM0jo1pqtLZibMLN8qQdhnlLhPibDjkNFXtMPia1aufMuT2ykC5vU9LIzc5kjibRft2JVAe51zNslLib2s/640?wx_fmt=png&from=appmsg)

点击会员才能使用的装扮，发现可以修改成功：

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUUXkl36m1wYp1hmV6PqdXoTSA1ApsoHFOcwhfVd1Ig3AsDey1vu3cTcNSyo6NnRVEtjbiaGGQsZhiaSrPNoyW9coqv48S6Sd9EicM/640?wx_fmt=png&from=appmsg)

那么是否我们就已经做完了呢？我们发现账本却不可以添加三个以上，这是为什么？我们明明已经是会员了为什么这个功能却受限了？

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUWjtLENq7GXPG0TVibZvK3Bzias2FjljpBW2CGaBN70KZmk9pP9FLu52xk1nlQnyDSeHYefSYgSriaQdXtefxG3ceBdLo4v822IoM/640?wx_fmt=png&from=appmsg)

我们借助算法助手pro，定位这个弹窗实现的调用栈，具体操作如下：

1.打开需要注入的应用的总开关

2.打开控件文本赋值记录，打开log捕获，把原本app进程关闭，重新启动后再触发这个弹窗

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUW2nGic0CfLfnqfmX90DGicwU8P1c09DcmuF1s5ec7SKzE3P7D1eCLZ85FJYPoo0hCN86FwIXo2kG8YgQsEN9gBW38oeSp95DfMY/640?wx_fmt=png&from=appmsg)

然后我们在应用日志里面看到了这个弹窗的调用栈：

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUVvbdlicHvZHoSbnq7PDRKcRsniaLTwGGo5579vLbn84PwA5AxAZA3N31kAQOEMiacF6nOjJcjk7c3MJEGjHWsLaQoFSWwYdLNoy4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUWeeNFibOFUdiacrhTzIGQmzLK1YJgH3HueNv4lf7HBSzSMEWWg0nJQzdYhdAdASb5dCqQial8Eyibskr1t0C1c9KS2CcKhyZbNCvg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUVMfXYHMsywIkgmXf2zkHFCWt7CpFzcYCyniaYDrBEAreBVkLsHeOibiar8oX9Pu0ib2G1hiaIxhOicneaGUr3a4L8V00X4gT7PpwLrg/640?wx_fmt=png&from=appmsg)

我们复制这个弹窗前面的类名，按照之前步骤选择全部dex进行搜索类名，然后再搜索方法名：

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUXeJFb1LndgibFRDibYAmL7FDaZaiaLIP2Dl9z6JbgdzmiaUXia5KlxiaeTpZJSrTB50iarINtGUEmtuFxCfIFKbPNVS6nI8FX8JLNfGA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUW6DZcNPZWXnq2tjnem2JhhjFqaXnrajmJqTtkSRicsdiaySOCCfveByI3HxRTRlnouiaCTFksswVuIBTljJuJbNcUERc2CvuzJhc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUXDA3jakZcLm1uu0E75PHopT1jkKO583VKTtusZHvdRSVskSpPd4L8LNTkGiadGtia0mBsBmCcwWefMzNmjIq4JcaHhHice0joFuA/640?wx_fmt=png&from=appmsg)

还是为了反便阅读，我使用jadx把代码截下来给大家：

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUUANYEll5ibsvpDGWtsuJibJeic9WFMq8kiahxXcc7Vt3MfMMM88x7KxsdCTyQDtroF5pDugTVlpwmRw40RNywFgCo0Nh5yKzFsBhA/640?wx_fmt=png&from=appmsg)

我们猜测是在这里，然后我们一样在smali代码进行修改：

```
const v0,0x0return v0
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUWwyHpx9DPj4TJBOYicWhac7oboLLVe98r4Q6YyiaTqqoO6MibdDcla3ucVV4EIzsoVnHCibwmia7VoicJLYccJ5BxyHpne2YTQZBepQ/640?wx_fmt=png&from=appmsg)

最后我们发现有三个账本以上了，于是app整体会员逻辑修改完成!

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUUkUQFia0IEj6EmXtYHOAWBfUqtBzZniaFMocXcdZEGnwcfOkBVhvkCkzXlfz0Phm4LLqt2lgWSt15DQFPeGk5Cz2jtvFDgWliaZQ/640?wx_fmt=png&from=appmsg)

存在的问题：

1.App启动时页面是强制登录使用的，当然可以通过跳过登录Activity进行跳过，我也试了跳过，但是最后功能还是无法使用，也可能是我不才，可能望各位大佬进行尝试了。

2.后面我同学跟我说它手机号无法登录，提示md5码未配置，这个可能是签名校验什么的，我没有进行去签处理，但是邮箱登录没有问题，网上有很多临时邮箱可以使用。后面各位大佬有解决方法的话，希望可以不吝赐教！

最后：小弟也是初入Android逆向，很多地方不懂，写的不够明白，如果教程写的啰嗦望各位海涵，希望大家一起进步

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUW8nYgl3TwYDLB2oS6JjHygvaqsMknlsO5OqM2LgFuibD6tMKLGW9LZlicQ7Mx2W3Wadd4XiavbeYE0fWmnf0olWCFUpu8xIpFMYU/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/mmbiz_jpg/Gv6JExJQjUV5BeE7JZ6LCrzEP7aMmdvc9tfrqHcr3uqFmaV8CWlC1BgE7WCEh0yTGAd5mvlqkgWLWE1c4CJZfBxclAwEibMAJPGf2m8ZxckI/640?wx_fmt=jpeg&from=appmsg) |

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/WJRHqUiaud0ouQQFouib41PSeoKKZO7mHSXDQ01XdAqPlLVKZD1yyPlfnErolowiaaDic5GDnU7B2GNhkou8PGqaCQ/0?wx_fmt=png)

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