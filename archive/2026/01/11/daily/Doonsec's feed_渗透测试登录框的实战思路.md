---
title: 渗透测试登录框的实战思路
url: https://mp.weixin.qq.com/s/Lt5-Kmu8qhxm3iFeyvc9Fw
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:36:54.586982
---

# 渗透测试登录框的实战思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ib2sSCPqpElIib3iaDmyN422SjM1zEMTceppYrYLOh9FCvyDkibicKvjyd3KQNKNbZ1rXdicEeZ6CibbY6xwuHh4DdyMQ/0?wx_fmt=jpeg)

# 渗透测试登录框的实战思路

原创

做一安全

做一不做二

![]()

在小说阅读器中沉浸阅读

当你看到一个站点有以下的特征，你会如何测试？

开局还是一个登录框

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepejlw5pianL42P2XLaNk5RzkuFzBWIuZSHpU2ia5U2H1nPHO36HrVnUIQ/640?wx_fmt=png&from=appmsg)

指纹里面的年份

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepovETGHRbdhNicYz2oQVQ6amsX09m9BZUWtJWxYrTI5ZkaynuibMibfv9w/640?wx_fmt=png&from=appmsg)

还有相关中间件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepSlhkyt96b8JGWXKZSK3rliaMS53W4wUH61qLJrgoNonrBhsZNg9JYGA/640?wx_fmt=png&from=appmsg)

第一反应，没有验证码，肯定是测暴力破解来着，但是这里是没有的，还能测什么再想想？

登录错误的这个弹框，xss几乎也可以排除掉了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepCvXYT8ibd0mZ0jiaxewsibHmFiaJHOwqWhAPK7fTNLfDgmfPsjWQI8Sn7w/640?wx_fmt=png&from=appmsg)

通过js查看，这个请求的url也是固定的，不安全的跳转几乎也是不存在

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepM2ib1xicj0dria9m8cIED3IVgsqzWqYnrRv4GEibXbkEdSHmUpzMngQu9A/640?wx_fmt=png&from=appmsg)

js审计，也是干净得很

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepKjG18V6cVSeraqiclcicsYDJzTpQia5oBxLxUvqpBiatdZVQZxiaKxmwD3g/640?wx_fmt=png&from=appmsg)

上面提示的用户名或密码错误!，请问这个时候还可以测试用户名枚举吗？

思考思考？

肯定不能单看表面，测了才知道

输入admin提示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepqlxlXOJEeMFRGvlVxE49diarghe4Q2qTx8dZ7lzhYvRE3QIJMCFzsow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepH3cd0jia7R8TL3Nd5DdiaKMWPw8NWHHORicvibcxudUFdGPric4n7RuVw2A/640?wx_fmt=png&from=appmsg)

那换一个呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepQvdiazIEB8f17w2hM4UmjZgfIFJ6ZOjQHq29hmn2Qq5jz49HR0LLttQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepFffM1sibAnQXbaFczz0y0gnL0QpSkUBdWJMFwPicUqJiasAVJLibAd24Jg/640?wx_fmt=png&from=appmsg)

这说明了啥，代码写得实打实有问题的，没有统一返回报错的信息，用户枚举这不就来了，混个低危先；

还可以测啥，几套下来，没东西就看看指纹的信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepOlxwEKmDcmzfX8icc3iawHJbPky41eTaCwUicAJU4Z3Y4IIj8x49xqFRw/640?wx_fmt=png&from=appmsg)

通过测试，确实是台windows的服务器，看后缀也可以确定是台IIS搭配着asp.net服务的，根据这些搭配，在你的脑海里，应该出现一些漏洞的，然后根据自己的想法去测试；

不同的人有不同的思路，我喜欢去看看其他的端口还存在什么

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepEAdDCZxTf6Ws9JWu1PbnIyjyShdQzceyjbEJHLwDQkD2kkriaiaASkPw/640?wx_fmt=png&from=appmsg)

这个几乎可以判断了，这台服务可能是开发商提供的，里面部署了一堆系统，通过这点也可以判断，大大提高拿下这个站点的可能，毕竟旁站越多拿下的概率就越大，这个留着先，优先看原站；

还是这个登录框，可以测注入，不仅限于sql注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepwbCBG4N5CianTevTBhLAQ76vDcMx3RdCqzXRLwyJvJib979cddEO0kSw/640?wx_fmt=png&from=appmsg)

通过返回的包，看到是存在相关waf的字眼的，可能获取数据不容易

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepqTE3UNmVNgNXCnNfktibg2WtQQTkOICgO8Oly1gOdotiacWrRIxcrE9A/640?wx_fmt=png&from=appmsg)

但是，得先去测

破坏原来的语句，发现直接报错出来了，这里可以百分之80确定是有注入的，并且是个字符型的；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepibsjibX9Dxtss0RUu4ryBwGQ7YfHlV4fdkerMHOZibQuTHj2tdYaacicWA/640?wx_fmt=png&from=appmsg)

发现可以成功注释

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepZYv4sN7BupYp5SMWzvZxPb9SicqC6JsXcylANrQbPKgn01DSrr0OicAA/640?wx_fmt=png&from=appmsg)

这个报错的信息，老师傅应该就是一眼看出来是什么数据库，看不出，你还不会去百度吗？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepHia5Wr04fA2oU1nUsyazK9bItDG2xT5A26qZ5pHbaTXHUPbqibXfBMyA/640?wx_fmt=png&from=appmsg)

确定了数据库，接下来就好办了一些

先测一手堆叠，测1秒，返回发现是2秒，2秒3秒才返回，可以确定了；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepbPxKIV6BW0juGThVQbMwQeUrSXhlibPQOAtGbkSZpL1tBgZaqNZn7KQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepuK8Gozvc8fatK6fHhibznVuMtQ8UFoF7ysVFFK4icPuK8qtAb95elYBQ/640?wx_fmt=png&from=appmsg)

相关漏洞已提交至平台处理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIib3iaDmyN422SjM1zEMTcepMoVAM7ibogajibHEwrA7gZLDLZQicVsLHSZufOe60ibiaIwmGm1cyap7JHw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIkAGXPaY1cUmnbNpRIfibjryGtRxSosWONFACVz84jGiab8MCe9dMJySjNpTTaOYYnGVubONmtBDXg/0?wx_fmt=png)

做一不做二

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ib2sSCPqpElIkAGXPaY1cUmnbNpRIfibjryGtRxSosWONFACVz84jGiab8MCe9dMJySjNpTTaOYYnGVubONmtBDXg/0?wx_fmt=png)

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