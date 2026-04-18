---
title: Python爬虫之某站JS加密逆向分析
url: https://mp.weixin.qq.com/s/bvfN3F24nRRcXhvYZ7qNRg
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:29:16.155903
---

# Python爬虫之某站JS加密逆向分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lFfjZayicKlElo64EUUMbHyrGricLkEtFIRFvWCWvqBurMQXu1YkOhXTqiaNIm3OTCr8H9iaZ7qhqGicSCnT4oqOMUZx788ickUEw1e9wKekWIhJA/0?wx_fmt=jpeg)

# Python爬虫之某站JS加密逆向分析

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于潇湘信安
，作者程哥

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6fpNgxJic72iaxuNHwNA0BooiblUaaQuiavCyr7GWWPulUHw/0)

**潇湘信安**
.

一个不会编程、挖SRC、代码审计的安全爱好者，主要分享一些安全经验、渗透思路、奇淫技巧与知识总结。

实现的目标：可以通过JS加密逆向后，得到加密参数，请求获取数据。此方法同样适用于被前端JS加密的用户名、密码爆破。

**被爬取的网站：**某某数据网

```
https://www.***.com/industry/newest?from=data
```

**JS加密逆向分析**

首先，分析获取数据的API。抓包，发现是：

```
https://www.***.com/api2/service/x_service/person_industry_list/list_industries_by_sort
```

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7ShAAfickQjhlkve9NkvIXBAgGMp3qWFqGzybXHzBqSjez8eJtTYREFYQ/640?wx_fmt=png)

这个网站不存在分页，是鼠标下滑动态加载数据的，所以利用selenium爬虫效率低，效果也不是很好。

当然如果是菜鸟，最好还是利用这种方式。

先爬一下看看，发现返回的数据是加密的，先不管他。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7SzejKO98DKthLuVSpEktXMNcMZAPquMa9C5chHlYqxB8yLv0Z6wVhUA/640?wx_fmt=png)

我们分析请求参数，发现是两个加密的请求参数，分别是payload和sig。

如果把这两个参数去掉，或者这两个参数是错误的，则request无法返回正确的数据。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7SEicic4QY2sr2zS5dV4B3sh9VHeBibsbWy2u4R4vqkqJq6yKNF4hmzskVQ/640?wx_fmt=png)

所以，需要对这两个进行JS逆向，还原加密算法。

经过调试发现规律如下。

找到了sig的地方，下断点：

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7Sw3NzgJ9zicTRice0ibXgicOOibrP9eWnGtZnNbZlRY19ateRA1R3zoHpEog/640?wx_fmt=png)

调试截图如下（只截图了payload的方法）：

**Payload加密分析：**

首先是payload加密，payload加密前：

```
{sort: 1, start: 40, limit: 20}
```

需要“翻页”动态加载数据，只要需要更改start即可，这个表示是开始条数，limit表示一次加载20条，比如60、80、100、120等等。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7SaLOHRGic27ia5ehJHZG7IIicAYPyPgRNSibYCP372DDePqVFGHFF1AlXog/640?wx_fmt=png)

第1次进入e2(e) ，进去前e还是明文的payload，进去了\_u\_e(e)  返回t    '{"sort":1,"start":40,"limit":20}'  值没变。

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7SibicOROdVPmO7P3CVfxTmG2OvVB0WibaqGQuXT2Q9kBu0iciccOuv7HKftQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7SUia0PZBqVaFEgkdqR5FZAxWjC8JneUvHFjErx8Aia7MR4LTQ8CA5Zv3g/640?wx_fmt=png)

接着返回e2(e)继续执行for循环，返回的值如下。这个时候，payload被加密了，但是还不是返回的值，继续下一步调试。

```
",\x177WB:d`ym{1L$'=\x10n\x02\x04\x15p8[ '&olw\x022"
```

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7S9zTHFZbnBaUibqvG8ATATENH1jfozJwnWHzm0sYkRDMq97jxHnN0bLw/640?wx_fmt=png)

接着到了第一次进入e1(e) 中，这个时候e就是加密后的payload传进去。返回u，就是加密的payload了。

```
LBc3V0I6ZGB5bXsxTCQnPRBuBwYJfnZeJCM7OXR/AH8q
```

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7Svvnb9lF6HU8TQ22jzFX0e1XWRMvumcAhv5sojNs5EygpVmlicib3tklg/640?wx_fmt=png)

这个是只要payload不变，加密值就不变，还是相对比较简单的。

**sign加密分析**

sign的值是把加密后的payload值加上常量\_P拼接后，作为参数，传到sig(e)中去，payload+\_P如下：

```
LBc3V0I6ZGB5bXsxTCQnPRBuBwYJfnZeJCM7OXR/AH8qW5D80NFZHAYB8EUI2T649RT2MNRMVE2O
```

这里的e就是加密后的payload，而sign调用的方法是md5(e + \_p).toUpperCase()，结果是：

```
1268D4D682CF9D0C6C3CB4D6E4C3C87F
```

new t(!0).update(n)[e]() 是payload + -p这个常量：t.prototype.update = function(e) 实际就是这个函数

他又调用了hex函数  finshed函数  调用了 hash函数

```
LBc3V0I6ZGB5bXsxTCQnPRBuBwYJfnZeJCM7OXR/AH8qW5D80NFZHAYB8EUI2T649RT2MNRMVE2O
```

跟踪分析发现，就是一个普通的md5加密函数，然后转换成大写。这个就可以不用JS实现，直接python实现MD5加密。

使用Python去实现以上两个参数的加密，修改原来的python脚本如下：

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7SicvcRsdRrFicKy0eqj1IrrQicshpPsT0lZCsDbJCFW0NkpGOQJ7CJbd6Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7SwcQUgTvD0dibXyGtGjnj7jGANknJGPTYqsuvgefCMGpfGiaqsebM2iaew/640?wx_fmt=png)

再次请求：

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOfOXObwaG5niaYDFYb0lys7S3edxJ88EKJr3cUeUzjTP0TTxTAWsKMkahwsDaDZeDA7VupRic6eXUrA/640?wx_fmt=png)

发现返回的值是d，也是加密的，可以使用拦截技术，获取到JS解密函数，解密d得到明文。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15)

学习网安实战技术，戳“阅读原文”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

蚁景网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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