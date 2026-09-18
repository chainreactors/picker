---
title: 区长分享之AI配合手工价值1700的src报告
url: https://mp.weixin.qq.com/s/U3DdCvAUHm5duOJKGxDF2Q
source: Doonsec's feed
date: 2026-09-17
fetch_date: 2026-09-18T06:51:48.309658
---

# 区长分享之AI配合手工价值1700的src报告

# 区长分享之AI配合手工价值1700的src报告

区长
区长

湘安无事

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**声明：****由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。谢谢！**

前言

最近AI引发的热潮很火呀，尤其是大佬的6000skill爆出来之后，src的竞争越来越激烈了，身为sqg的左膀右臂不得不身先士卒给大家探探路了。区长也是二话不多说先干了快1000AI进去试试水，下面是一些成果：

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EsUktYic3shDIiaqG5VkPQdDdqZMmiafib2UxQncFFx0yWibNUJwCVx0UCHZOoXVp33ay4WvkALRYw63SXNkpwNDy0SDAvzCHFs03oI/640?wx_fmt=png&from=appmsg)

后续会对skill和挖掘手法进行优化，团队的哥哥们再等一会儿。

## 漏洞分享

说了这么多，也是马上拿一个漏洞出来分享一下这个skill的具体作用。

首先对这个skill进行了一波分析，发现它主要是针对前端js进行大量逻辑分析，然后构造出一些能够未授权的请求包，下面是他分析的一些路径：

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Evibbaxs5XEZNG4ib07cQAicicZu8NvDPDnBVCH1C1LRNso1Qwt1B9anRF8sbAZkyhcGlB1T1RJP9jBgvK7kgCG9kGAal36ISffUzI/640?wx_fmt=png&from=appmsg)

这个时候你作为AI操控者，不要有“钱包换成token，ai代替思考”这种想法，尝试拓宽一下自己的思维（这部分留个白，大家可以找区长讨论一下思路）。一通头脑风暴之后发现了下面这些东西：

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Esjgoly2Dmus6WVsBbBmNxb3mccmiaI3Fco0IxKhXdQQPePBbiaZ9x69bbU1Sus0u6J2lkMt5p0ZA7MRX5A38YSwE3KP6cJQiaaz0/640?wx_fmt=png&from=appmsg)

此时去做拼接发现还是无法拿到身份证正面的图片怎么办嘞？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Eu9QrtszUSFjy4clXIYLs7dDKynicQYsDjadt7zcnnPkqQIQBlQtNMibzTmDubWFKIVJHWyJV5MkGAddicRY4OiapBGufIWfavwW38/640?wx_fmt=png&from=appmsg)

这里可以把路径复制一下，让ai跟一下这个接口，看看最后的文件落地在哪个地方

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Ev8Ctn5ZPjib2ibgrbLiaVVzoo7kqnDTevYxO1xv96XicS4OgfQDCjduDGVibKqtejpXPo1YRB4KGicyhDn3cW4AWJRL6obPo8l53IibM/640?wx_fmt=png&from=appmsg)

最后发现是个云，成功拿到信息：

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtYfibLpfKR38LdezHshwPyibCu83ic8G5ialsBrfy2uyKIQmV9yk3sV2sIzU0uOISmKQyCib2NTIJWtewoBJnn2HrAOWHMM6MJVNfA/640?wx_fmt=png&from=appmsg)

当然也是不负众望，拿到了赏金

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsCb9UG8tmIDScYiaeeOzZ5YiaK7PNRMkjjwZpJiap1pK7f1E8IgDm6oruJ59Z4mh1Ko7nR0OAaiaUKhnEYknungvM4BACeVS32RmI/640?wx_fmt=png&from=appmsg)

后记

AI使用之后一定要建立自己的知识库，比如这次用了特殊手法，可以让他把这部分内容写进记忆里，下次直接读取就可以重复使用手法啦。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvGx0aOWPwOGcSJd4tBsvoHtGkhKLhocHvZZsW1QkwiaVJ1WoVAvCK8gPt3WrEkGKqumR8V9rYCJ0mEuYqRBkHfJbN7ANhCtNbc/640?wx_fmt=png&from=appmsg)

当然团队的宝子们可以不急，毕竟玩ai比较吃渠道和money，咱团队的宝宝大部分是童鞋，可以等我和sqg出最新攻略skill就可以啦。

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EswPBzsUpIlCpG5RS0daOhq5m3LyiaoXnJD7VHRXcvhzAPnscGjxLtoicYvDNnVPsfQw3U5icvR8TibZOA5Sz6fHjArBLksg1CpHas/640?wx_fmt=png&from=appmsg)

## 深情版edu+src培训

深情哥这里是有edu+src培训,更新了ai的一些，将以前的思路和ai进行的结合，交大家如何使用ai挖edu或者挖赏金src,我们更注重交学员如何使用ai快速挖洞和学习ai的思路，而不是异想天开让ai猛猛出洞，这样子会让自己的渗透能力退化的，我们不能成为ai的奴隶，而是ai的注入。课表如下：(或者加我wx:azz\_789了解)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9EuGBYM7SgELibLtVLNhFr7gSbsob0gmYIygssYZMhKf9mYu5w7ibjI0RgqNrLcHCJsz4crjnNwTB8L8qDGtKdAT8WcTeq26kmEKk/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

```
https://www.yuque.com/denghanhan/qqby5b/tmde5e8qwdysm5zz?singleDoc# 《深情版edu+src培训课表(2688)且赠送审计版+ai版》
```

### 【edu漏洞挖掘实力展示top2】

湘安无事团队一直都是edu漏洞平台的top2如图，都是离不开深情哥和区长的培养。(学员专享：对于表现好的同学，贡献比较多的会打印团队证书发放)2023年到2025年的证书~

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9EsLfONYLvvUFEDHIGnLNfH5Y3j0pEtpF5jXQNibuRCHafARLgfSdPC4cxkARU7R7N0SQOgIibntFeRBvA0bY7DYNnW5DbBAH1lNU/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=21)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9EvRGgH2qLnAiaavPjGFnk5cEibAgIANopm88bzajMF7rJ6ShQtgg9hwvyHiccXcibWEjSg980h3NRxjq71hFxS59Pvickx1uoAmaSfA/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22)

![图片](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Etc99qmia2erPHibkf0SNePxEPJia3cj2yDmunnyqLKqFeHwnOBqNumH6roVYuvql2eFxIAVkhT4V6knqXr9JziaOzj6RAaTiabOc64/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

#### 深情哥edu漏洞挖掘成果

我们导师深情哥实力，深情哥edu漏洞平台top10发送证书奖励

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Es3DGoTlEZRlu8XuQzXVPlBektrl7xtGuknD8p8pakHrxXCwDSicJibnsvPXYuSXXU8eMdSicYv1icouBmg35UgXrDyS0qJXdrGmE0/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=24)

深情哥都挖了快2000多个漏洞，难道还不能带飞嘛，嘿嘿。我的edu证书太多了，可以看后面放的截图。现在不怎么挖了，因为现在都是带学员挖edu漏洞~

![图片](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Esz7fJ4lrLD9yOmB4aaWx9ib9YSjXr6zVVrT86XJ8JBick7liaYJgTJ7ePy121xcvurEofmWffuk9ApWZjsplLvhWnM596Wh0pA4o/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=25)

![图片](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Et83pptqOlhT0q7n7aIwx6syAZVBNepicXphiawNXSSDXmf8rYcXIylyYACf72jicWghzN6cJQy3VvxIdt8rboRgzUDnIBWYFtqLw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=26)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuicFV4vKczE7icuPshXmD9nkK7bMmTpG9dOeFs4cfo5ftzZ3JgHj5ZQVq0XGZWQ8sdHO9I4wMnicywAvBtOrVz10Rp4M7u0Ep2icY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=27)

#### 中国地质大学聘书

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtibsdGf3qgcftrHCfibVt3Aibvf6a1a7heAjJ56FgibvUmMBZckha5Njk6Bx5CaV0flIRp4HsVSuMsrbiaU50kxWRR4vaNNfkG9A1Y/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=28)![图片](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EsaTg5gvNZrXJAicpOmUkDbp02Ql1NS32T7HibhzLFjoEMA7AYAUaxPpBt9JSYmXicb9QodiaweYWQuMSJvjLyQoUTPgZKyvVZptCc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=29)

#### 各个学校的感谢信

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9Es1AvsXoORZicqJa7oMdXmksYAKPKaI3ctIrTVl0TJeD4r5HfP0uic2ueOFEicZ3V4fbfSticCxibZicWYva7C81IyEMjXkibS8K3pmXk/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=30)![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsxRfp3BuOhibKwica8Zvb1GS9yCnqWBYTicg09s6mqgibHToMSRXnMibNAtmJnIyTWiaOFM3ccibVibnbEq9OicSDVfMfRyfCLRznaIO5o/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=31)![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Esuu1Heq09sE08UicALwokkYJFDcYVJqhdPcMRD4ibvhrjYTibHEwxRILrzbbHibPsWg6Q0a4ibc3IrhVJbmEaUg0awWiaIrE0QT9UVA/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=32)

#### cnvd实力展示

![图片](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EuwQqkprncIzyS5XOCWCD1OdjZiaBJLqlXZ5nFQSDXiby9PCQpHsxQ42NxjMXV0YrOU5rs95fBbxyauYVhHSf6fMw5xia9V9fAQEg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=33)

#### edu攻防实力展示

2025年带学员打了两次攻防，都是第二名，第一次奖金1w，第二次奖金2w。

#### ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvRY0aCJQ9WAb5c2XIjnuKib9VJykMMHFVQefFptaia92ibtZkXJPX8RddUAzlQS4EPqFh3iakIMkGDu6Sb1YuCDMDVpcZia5VdKJ30/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=34)![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsJhp9cib5CPngN0gkw3kpAicHBGXdnU45RLibrQ4Xn0q9iahBoO81gCBDwFpDfGtlOMNTxrHJkP5rUmERjL62h8yISyLdB2HmJZTA/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=35)

其中拿到的edu攻防奖金都和学员成员瓜分了。**2026年也打了两次但还没打钱**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsoDqBqf5IxuZXicbVYoDGwMFUowziaicnIN8KR1uvib20PCJkCucYEtM2vu6ibgJ5AWrUhEKhClEtaLmopxz028Dia7G5UyNLWkXrMg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=36)![图片](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EsRDMMZq9dcJX1c7BJrb3d92kM1CyuIse17WdKnBVGAPh5SmsHFS0sHDib7RO0kzQWIcmcruw2LTLObx1do3Ltkl0AFtlicvDvNw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=37)

#### 个人年榜top10

![图片](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvLn2j39bbPiaomcNTAPkcNanFSlmDqichg5s4ZDIj0wk2DRjTquu0TEsvqmSZDOvBENrSWF77oXicbBNK1C7xwg2lSSG0PlaU0OY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=38)

#### edu漏洞平台带领团队第二名

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Euib3rMc2Mwksb8EKVJ4xc9sWgR2tKaaibXaIZGjp0PZZZzkNYeWt5ByaCDwNPWAKNVKicOcCuqxXUiarib77bibEBHiaBIWSNdT2oOx0/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=39)

### 【赏金src漏洞挖掘实力展示】

#### 深情哥漏洞盒子赏金50w挖掘展示,我不只是只挖edu鸦！！！！

![图片](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtlsOia6t8v2uStrKIwq9dyDmlWX3wQFY8pbxETnXy4SR0h2oQOUKW44LpRtPJqqRqzLWSyF6okIh8nknyxiaibn5CQiaBKMw...