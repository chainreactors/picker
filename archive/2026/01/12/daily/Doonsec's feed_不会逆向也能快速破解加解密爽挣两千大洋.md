---
title: 不会逆向也能快速破解加解密爽挣两千大洋
url: https://mp.weixin.qq.com/s/XKHrnfxyxKT4x9hfd_4c0w
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:28:03.294115
---

# 不会逆向也能快速破解加解密爽挣两千大洋

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuYVDPaJnBJBU4pJLtvHYFGqapKticv0Dwwgrnr2BXRNZKzVrIiach7AUCpiaWziancOFENtibjxBofSqPg/0?wx_fmt=jpeg)

# 不会逆向也能快速破解加解密爽挣两千大洋

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

以下文章来源于隐雾安全
，作者zero

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM726qqnXD4ibQaXQjLVHp9Gxyv9TJsiaWicUIvUnjPWalVYA/0)

**隐雾安全**
.

隐雾，为您提供职业成功的关键。

**不会逆向也能快速破解加解密**

**爽挣两千大洋**

这是一次海外的众测项目，主要测试目标是app和管理后台，由于我开始的时间比较晚，越权类漏洞已经收满了，所以也就放弃了可能漏洞比较多的管理后台的测试，主要看一下app。

首先抓包尝尝咸淡

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b22TLic3EeJLGe0gwpwuKzmXROVdnOiaic6GsJGLdticclUIaArf4kwwMQ8g/640?wx_fmt=other&from=appmsg)

可以看出，目前的问题主要有两个，一个是响应体加密，一个是请求体疑似验签，所以要想想测试这两个是必须解决的。这里首先确认一下是不是真的有验签，我们拦包修改一下请求体，看看app有什么显示

这里我们随便修改几个参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2RGztDdiaQ6UyOf9UEC0ohThZWZnyspDNoDNbdyKqotx8Bn5f52Yo4xA/640?wx_fmt=png&from=appmsg)

修改之后吐司提示下面的内容，我们翻译之后的结果是 "请求无效"，那说明大概率这个签名不是个摆设，应该是请求体里的所有参数都参与加签的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2XpozOX67qfhTypeBYzj3j5CNiblK8XablECHD7oHrklyK25UlxUH2IQ/640?wx_fmt=png&from=appmsg)

那这个时候，我们该怎么办呢，我就是个脚本小子，不会逆向啊

不要慌，我们可以使用下面的这个工具(此处应有广告) 算法助手Pro

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b20bt8VSib6JmicOuDmGoMWyJb52k5tuhg1BTs4iaQtGhGvu9P3ecVT59Yw/640?wx_fmt=png&from=appmsg)

大家可以前往工具作者的 微信公众号获取，链接-> https://mp.weixin.qq.com/s/JPzjpQ3ZoY7cd5K1ZywTZA

进入算法助手之后，我们勾选上目标的app，然后勾选后面的几项

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2tnicjq6ibOKz3tXWMutJJaGHY3hfP2465dM5vhz6ETJ9YpRNFDnNCpxw/640?wx_fmt=png&from=appmsg)

之后点击右上角的 重启app，即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2nePLjEUrF6BNhS3QLQ5wibdRT3jM5AjYOLXUDlEZmicBXWykgS4B0YZw/640?wx_fmt=png&from=appmsg)

此时我们在看burp的响应包，把这里加密结果复制出来，在算法助手里面搜索，就可以搜索出相关的日志

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2PdtzujIOoW5AHoW1MibZwltZmokcmAN8triaoxJxq5UnBKChlC10XCYw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2ETSUiciarqiaeHajVichR7zogxAhbuwXjianYUGI7ediaKHq96dSjzkWsmnw/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2MJIdtdnpVFOgia945GIbvSiaZ6ggv96qLicRPMibzxxtLa7eyknkGGAnog/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2Yj3dl75a7QuiaIGvykGj9y1fY43VUQrEiccXwhG9AhgGiaY7ib8ECvxvDA/640?wx_fmt=png&from=appmsg)

我们点击任意一个进去看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2yLLgfHRdPp2eiaGF3U67vz4KmtbKXkXSN1eMS4j7zrI72FS6ib3W78vA/640?wx_fmt=png&from=appmsg)

可以看出，这里已经把所有的 aes解密参数给出来了，而且看样子都是固定值，不是随机变的，OK 那么就差一个 签名了，相同的办法，把 签名的值复制到算法助手里面，找一下签名算法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b24xoyhRicG7ppkyHIR4qfvkOOZxjxzIEjOYEhibFJ3GxHS5ZoVwP9Nh9g/640?wx_fmt=png&from=appmsg)

这里签名的内容可以看出来是整个请求体加上一个随机码，但是这个码肯定也是可以在请求包里面携带的，要不然服务器没办法验签了，所以我们在请求体里面搜一下，看看是什么部分

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2PfQQynt3RVRcs1HJIj5RtO8F15iaQ0oHdXkzgX0uCMrwy7WkK7f7AXQ/640?wx_fmt=other&from=appmsg)

可以看出，是这两个请求头拼接出来的，那么 验签和加解密算法的所有参数我们都齐了，下一步就是写脚本让burp可以对响应体进行自动解密，对请求体进行重新加签了

这里就用到了 Galaxy 插件，具体用法大家感兴趣可以参考，往期文章 https://mp.weixin.qq.com/s/IjyA23w-puiztmXNr0Tqfw 这里就不再进行赘述了

最终的效果就是下面的这样

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2ouYtJItpIXbBKuorUNcjCibfpia9y3zKvuL2s0gVMwWVwOFWohQOd0wA/640?wx_fmt=other&from=appmsg)

同时，由于可以自动加签，也就使得爆破、遍历、替换等行为可以自动化，也就为我们获取到后面的两个漏洞打下了基础

首先是一个请求频率限制绕过，这是在我操作的时候发现的，请求的次数超过一定数量后，就会统一报错"请求太多"，这里想到的主要是下面三种可能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2V1hBHQ9VdJYKzlpriccfPPibb3uiauYprdSV8xRqFTZahCQfiaTjDRibOxA/640?wx_fmt=other&from=appmsg)

1. 按照请求ip进行限制

2. 按照请求包里的 Deviceid 请求头进行限制

3. 按照复合参数生成指纹进行限制

我首先测试的是修改 Deviceid 的值看会不会绕过，但是没有

第三种不太好猜是哪些参数，所以我先测试了 ip 的可能，在burp上设置一个上游代理，然后设置全局规则，来达到修改我们ip 的目的，然后再次发起请求就正常了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b278KCUGbGicFDGABwoeQicLkIQaRiax16wK7JLd6d9NYGewrbe6beZEGHQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2VtQgrvcEe9iaKa7ppsOE7dcGRzdic0xeg52OJW8GFBFIlx4TO4ChjPibA/640?wx_fmt=png&from=appmsg)

那么提到伪造ip，那就不得不尝试一下 xff漏洞了，我们直接来试一手，添加一个自动添加请求头的配置，然后再测试发现可以了，OK 一个漏洞到手

(由于写文章的时候漏洞已经修复了，所以以下截图使用报告里的截图)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b20twkIic9EEGy8rPUQge4e0D7TYsDlrEVniaDWOlNxJPNS5yL94vk599g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2JcvNxOF2CNFicrmibCufcVzm0EqEZiaU2mkuFDyYI6VVj4lP2OIfOC4Ww/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b24Mqc0VRicLmMILKLgJFIHEicmHoic8MZDBANAWwtwpmaPIx7owlPmROtw/640?wx_fmt=other&from=appmsg)

那么现在限制我们爆破的三个主要问题已经都解决了

1. 请求体加签

2. 响应解密(看是否爆破成功)

3. 请求频率限制

那我们肯定是要测试一下登录处的短信验证码爆破的

直接开整，这里我们在自动解密脚本里面添加了生成随机ip的部分，来利用上面的XFF漏洞绕过请求限制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2OMncpsqxMXmmHrzT1tSFG3jpsC9rIkxjI7PTXZ19luILLuETWcHvnw/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wBZOUYx99e54ZXK95fE7b2PIcSvUcnEgoJEREhjP5eMYJDdoiaZYK9YSRqGxsXCiaY4TUtmNpe3yuQ/640?wx_fmt=png&from=appmsg)

好了  又一个任意账号接管到手。

后续由于摸鱼时间到了，所以也就没有继续深挖了，也是上班时间赚了个外快

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuYVDPaJnBJBU4pJLtvHYFGq32ZHFLBKQnSmGBwiccKo1xviaVMXUtNjK7ASPSGLtmGib4Ab7Cu5nNylA/640?wx_fmt=jpeg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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