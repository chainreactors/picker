---
title: edu小灶案例之泄露上w敏感信息&有意思的证书站报告案例
url: https://mp.weixin.qq.com/s/YNt_gDIj4QnrdcORPlcaVg
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:21:56.046500
---

# edu小灶案例之泄露上w敏感信息&有意思的证书站报告案例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2H5NbRQmn0o4icClRiaM5ghg9vvgrhZm3yExy5Wdu9dm4qZ01vJPcjXGg/0?wx_fmt=jpeg)

# edu小灶案例之泄露上w敏感信息&有意思的证书站报告案例

原创

湘南第一深情
湘南第一深情

湘安无事

![]()

在小说阅读器中沉浸阅读

**声明：****由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。谢谢！**

## **前言**

某天学员滴滴深情哥，说普通权限登陆进入，改一下admin就可以看到1w的学生信息了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2s4k3UsXiblRGFaIggc7aKXj4ly0GkAYtySfoyLErvCyrTq2b8JTLmDA/640?wx_fmt=png&from=appmsg)

本来想让他找一下接口去看，后面觉得应该是路由守卫的问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2vadZWS2krorCSM2OQDh7cS9FUxIcfD5hvJeVHDm8FSsHqG3HndiaM0g/640?wx_fmt=png&from=appmsg)

比较好奇带着疑问开一下小灶

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2X7EkqTguEbs3XbPicfpU8vCiaZsibvYwovj8kYia8nucF0psQCx1NUuRhg/640?wx_fmt=png&from=appmsg)

## **学员第一个edu小灶案例**

首先还是老样子，学员直接弱口令进去了。123456，888888。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2KUlsXFjybtWkK0Bg6wfFMc4HLwBrZnwibRqZp3EmmJp5yIu6IRkbEEA/640?wx_fmt=png&from=appmsg)

登陆进去明显有个地方，可以有个地方点进去看到所有学生的敏感信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj22CvWkiaFZsCib6bNia1DcLnvCbQsOPR1EE9NKH8b7P94WwXOyAJvXjpcw/640?wx_fmt=png&from=appmsg)

但是很不巧，没有权限，猜测是路由守卫

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2KPt40sBuR1nn9jQu3JSg8UnQokQkPtu4ZGBn6u3wxWbHGnIy2ib8ybg/640?wx_fmt=png&from=appmsg)

看了一下其他功能点，点击学生信息没有敏感信息泄露，sfz也没有

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2PbMYbtIjKmIOZAk3mt0CicRXfedodeNS5iaJDjIgDPoYb4VFibx7PZ8JQ/640?wx_fmt=png&from=appmsg)

看了一下框架，大概率是vue的，这时候我们直接找锚点就可以了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2EGXnyrHgPV2fzibNPzpUmTtWrJlegiaJdYFvIyO5ypCZQMRicX1ITorUQ/640?wx_fmt=png&from=appmsg)

点击学生信息他是

```
/student/studentinfoSimple
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2Aictia4fH3NrWQDtgbtWrlNvkqWUInTMVsnWaNtdG9vicEzgOU15dicHzA/640?wx_fmt=png&from=appmsg)

我们直接f12查看一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2PeLBSUibqQxIKuJNmj7ZIQEbMArFAanic9ZIr7eGNV1BKHZMqGwiaF7ag/640?wx_fmt=png&from=appmsg)

可以看到有这些vue,如果开发过vue应该知道这是什么，我们直接提取出来。

```
/student/studentForArrange/student/studentForCommunitySelect/student/studentSelect/student/studentTableSelect/student/studentinfo/student/studentinfoArrange/student/studentinfoDrop/student/studentinfoGraduate/student/studentinfoSimple/student/studentlist
```

直接访问，发现是404,当时就懵逼了，我觉得没啥问题

```
https://xaws.com/#/student/studentinfoGraduate
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2Bh35mLh4sypOic3q2naSgxC1axpp8kMfdDZ15B9GkQ7LXjCJYApRKeA/640?wx_fmt=png&from=appmsg)

但是！天无绝人之路！/student/studentlist直接泄露了sfz

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2QXBm5kfXOpK7OIyibu1iaB4N1GuCu7oIgDS5ubEORUib2Oz6UC9CJGdDQ/640?wx_fmt=png&from=appmsg)

差不多1w多条，直接让学员交了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj29HiauAIu0f5A6XQURRGqXMOhbBSU4yopf7cc3p455ZHOhUMk3JyepVA/640?wx_fmt=png&from=appmsg)

其实有工具的，也不用我们去找的。今天给学员讲一下怎么用。

```
https://github.com/Ad1euDa1e/VueCrack
```

后续让学员直接交了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj29BzZruxGJMUicka8RIpA79PW2PajcRlrPZYFCPU9nTB7UbqGyEOtYhA/640?wx_fmt=png&from=appmsg)

拿下了7个rank

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2Ufwtcl9DS79sf9aEMqaYcbEiaA38HSFRskSFfdSCiaC2icTWHA2GlvcSA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2L0SHLj2gf04QEjZBlMQejKnM1a9tXn8QncUc7D7XMmaGhlP9Jo0l4Q/640?wx_fmt=png&from=appmsg)

## **学员第二个edu证书案例**

开局一个接口文档泄露，学员的运气真的逆天了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj24FAbp29kSLibLbSy8IzRKoEibj9kkc3AlVe7AiaibicCNLBotFKhoI4uycg/640?wx_fmt=png&from=appmsg)

发现了好多好多接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2Q2gvdLdvUSQDGJE1xnrxWFlJicnAvicdgmzq6kMpmce1MVnxziadu772g/640?wx_fmt=png&from=appmsg)

直接用sqg给安排的学员的hae规则提取即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2z4c6Ew8bVrtvBUHfF2gcpqicwbq7EtOwhaenp3z6k5GYPcHqvIj0HXA/640?wx_fmt=png&from=appmsg)

直接发现有接口泄露某个凭据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj26rm35cbMMvRIWKShlfBCPAnF39wicoRtfqMBFqUrQHwkpUvHV6EibAFQ/640?wx_fmt=png&from=appmsg)

这不就是sqg上课说的腾讯云的临时token嘛，不就是AKID开头的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2FVmwzN90QoyCTPV4QwvicaoN70WfeuMTuNsrov5855EHUeAJec1iapvQ/640?wx_fmt=png&from=appmsg)

直接拿着纷传的脚本梭哈就行了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2aczASfkQ9BB4rtiaQryZt2MuuquRwA1gTrT4Ne8blyZW4iblaIicniaI7g/640?wx_fmt=png&from=appmsg)

相当于可以查看腾讯云oss上面，所有的文件了，脚本可以直接生成表格，挺好用的，在github上面可以搜到，学员可以去纷传领取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2LSHns6EAcpNeNKasmF6LRCjaIJKQs1OgHK6mz1fdmWviaYyLCMTEZ3Q/640?wx_fmt=png&from=appmsg)

这个证书刚上几分钟，学员直接拿下高危了，直接安排kfc了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYsh2kZA8h8yF82iap4JI0Dj2jKDrwicnlVrEzRoQTAt94wJMxSZIDic0UFJrMLYMMZnN0adxlEB9pqlw/640?wx_fmt=png&from=appmsg)

湘安无事之深情哥版edu+src培训(广告)

已经搞深情哥版edu+src培训一年了，感谢大家的支持，湘安无事团队再去年年也是拿下了年度top2,也已经带领很多学员拿下超多edu证书和src赏金具体可以看看我的培训课表里面。**培训内容包括edu挖掘，赏金src挖掘，安全实习小灶讲解，hvv渠道内推，nisp和cisp证书超低价哦~(深情哥wx:azz\_789)**

[深情版edu+src培训讲解](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493987&idx=3&sn=ce496c44e8344ae9d815201771770108&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/S2ssjS1jNYu6RvXIS2dibk70FUGibd8rUlPAppwgl5kfNe9YGG5sBO9bcELPEV1lDicZ13vgDmK2GWHyNjDoJ88ag/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=28)

[服务号存在注入之有意思的edu漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494659&idx=1&sn=e357db59d806c93f3a5a36b5c312b335&scene=21#wechat_redirect)

[学员投稿之edu漏洞的JS逆向解密导致任意密码重置](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494634&idx=1&sn=7cc83a90badea88d7d7d25583bd0c419&scene=21#wechat_redirect)

[最近学员小灶总结之双十二特惠](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494604&idx=1&sn=80f030c8114ee3287036586c670289c9&scene=21#wechat_redirect)

[卡顿页面导致三本edu证书现世之学员案例分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494572&idx=1&sn=14c21f1cae87dbdbf2ca5c4b10533f5d&scene=21#wechat_redirect)

[看完这场EDU通杀刷屏，连我自己都沉默了](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494535&idx=1&sn=113dd5e17065def94a5dacad361176b3&scene=21#wechat_redirect)

[edu证书站挖掘之学员分享案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494524&idx=1&sn=bff39f27ea27bccb884e832603acda92&scene=21#wechat_redirect)

[如何快速挖掘低微漏洞-项目挖掘总结版](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494500&idx=1&sn=2da7aa0d40075b462eb27695f2da9e83&scene=21#wechat_redirect)

[公众号接管漏洞之偷偷加](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)[小姐姐微信](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)

[辅助学员审计案例-php代码审计](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=1&sn=2feaf2786717c2c577fe0b5230cbc58f&scene=21#wechat_redirect)

[学员-补天800赏金报告分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=2&sn=c54ea91e0b3dc79f48f54f931df413c0&scene=21#wechat_redirect)

[从js逆向到sql注入waf绕过到net审计-edu证书漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494171&idx=1&sn=0d589d01dfbb068e53f9ad9c22676d7a&scene=21#wechat_redirect)

[空白页面引起的高危src漏洞-再次绕过](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494082&idx=1&sn=6d1cc92a049d28b5395d417e0a5203a5&scene=21#wechat_redirect)

[空白页面引起的高危src漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494061&idx=1&sn=bfb1406138041fcba8286811aa7ac6e1&scene=21#wechat_redirect)

[难忘的优惠劵漏洞(深...