---
title: 小程序挖掘技巧&amp;&amp;某证书站案例分享
url: https://mp.weixin.qq.com/s/imt-XjvVbHnEcdsSAAme9g
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:15:00.782122
---

# 小程序挖掘技巧&amp;&amp;某证书站案例分享

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboTJlkkTpxmfjFWAx2icfhnNib6W9icM0RM4I2lQ7ziaRJVIvG258vibc3EhzCPyjm0C04p2We5Y9qa8BeOfF5mjotswJC6cLOiaicmyicM/0?wx_fmt=jpeg)

# 小程序挖掘技巧&&某证书站案例分享

原创

陌笙
陌笙

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

前言

我们在测试小程序的时候，有时候点击功能点，会跳转到浏览器，让在客户端打开，影响我们正常测试，这种情况，除了一些小程序的限制，还有可能是我们的微信配置问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR2WpQDV7MgdqyrBQtVRhJEGZjPfwzvP7MDicqYXUx4CNHRfKSV4HQsia9Xao27ic3fBVicsQ6QObUYZNAHjW0XKmV9OFWP8Eh2N9s/640?wx_fmt=png&from=appmsg)

本来我也以为是小程序的限制但是在某次指导别的师傅挖洞

看师傅报告的时候发现他点击同样的功能点就有对应的功能

而我点击就会"请在微信客户端打开"，后面问了一下微信版本还是相同的

后面查了查才发现是配置的问题，有这种情况的师傅可以像我这样解决

具体情况

比如我们在测试这个学校的时候

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR3pwBlia5POJlS0icKnghoW3Qf8qsic3sP9u5UQtHic6rVMJfeEdicCictibwEH23KVhtSgLmK299ErC03RT95mMyMNOjPaOpLQzAUia0/640?wx_fmt=png&from=appmsg)

点击平安校园可以看到正常的功能

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTrnvuwiaL98UQMRs0EO331XseAicVW2SnJqaiaVTliaUhfCEU6utpTjMLtQfc9rH3rz8VsS2qk1WZt77bx8tVqqG8AOSxcicJJeL9c/640?wx_fmt=png&from=appmsg)

但是点击水电缴费

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTsI0rvmAfwbx6E2Te6BvoleMgKshRdlbCjQ30vKAicck5jzTqhAO2NYBEvCQS6jg6OCA6Ndf8icxEicsSENj5s1fA57CC6SNEZss/640?wx_fmt=png&from=appmsg)

这个时候怎么办？

真机测试还是模拟器测试？

都太麻烦了

在微信里面修改一下这个配置

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTyCbyA2Cf4XNSc2IzC4R5lq7IiaACIUNZU3oicsibap4pP0LcpdTof70j1KhicrkR8uk0lcRoLTqVcmkhYY19y9s3bAAZGDkjFgqA/640?wx_fmt=png&from=appmsg)

把使用默认浏览器打开第三方网页关了就行

然后重新打开刚才的功能

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT1VhrFibQbRT63nXr4ybC5wjubD5VX0FTEPTTXsk4CpFN535g3Th4C5CxgwiatXdmpF0PHicdbMcbAO4xmRDynRZOWXXg0slWva8/640?wx_fmt=png&from=appmsg)

可以发现已经可以正常查看

正常测试

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ850HmOK8NZtwLXllibw25NOj0LBqUgLh1pAYuxawXyD96OvQLEyx7qH7pkS1PibslnaOmmqlQTNK8opwLOnTzrAqMA1w0YGiaIQ/640?wx_fmt=png&from=appmsg)

功能点直接多了一堆

案例分享

小程序直接搜索对应证书学校，可以看到他们的相关公众号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRVbUpqv3jtofyld2LmvF61cYX1IEcULXoWDPSNaIcZS8llhXJTk2jEJo6c4Ge7BwXf0uHWUc4DY6cafJzwUrqGTAHscOgVcGI/640?wx_fmt=png&from=appmsg)

直接点开

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQeFwKEfG6EfzVGMtB75qPz81kJdYQPCSvb6QQg0f74XhoMrxSl45ib0HtxZrzpWZm7ZQjUMgQggVWTbhtvAQ1Kbs92c21lQors/640?wx_fmt=png&from=appmsg)

在下方可以看到很多功能

我们点击在线保修

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQtRRmD9yXoCibZNnBrVWC0XzLSMc2JOpt2zlX0DkefhibTWF1vwkPoj3dJrGs156tBibib4gfxTxXpDWQqAC8L6Rgs4mY14Ft2zpE/640?wx_fmt=png&from=appmsg)

添加相关功能进行提交，注意整个过程，让流量过bp这样不会丢东西

之后我们看到这个页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS0A9eedRXjVHlTJHSLj7cjcxgZS9n6EtM5aGIQSPIqUl2GeXibg9DkD2TDh3gHcXhib1yslKmgoOssibjGftGCqIkvtFBMRtQ8KM/640?wx_fmt=png&from=appmsg)

点击这个订单查看详情

这个时候历史数据包可以看到这个接口

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSYiaqmaLcuvmgz06Dk1eHcy3Yg8DicLxQNnibkIC0c9ngjuzO6hBTthoOv8Imowo3XCKSlia0MrRaibnrWnUlkTkhrsDhxz05bH5MQ/640?wx_fmt=png&from=appmsg)

发送到重放模块

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTsN4ib80mEs6dibf6XM9PhzDOqAZu0x7xhbiafLtQJfJevbGd6E1J6AUE3Y1micrpsQgRERjG0vXsuu9s2dvnLdlutGv085oby7rU/640?wx_fmt=png&from=appmsg)

看到id我们应该想什么？

必然是越权，修改越权可以看到他人的订单信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ2TDS3PwuhC79ab3gPnJNeqfpSrEBVamGOT7DzPeg7mY0bpmxHClanZriaia4CXOebgWnqNwbw8bM9X6NsCSVhTcSH43ukkLl3c/640?wx_fmt=png&from=appmsg)

越权的一些思路

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRk9mje75kyVy39OBBzGiaNp1ibYNb1TpVFydKOwMlcNUKNkehJ3sB7NRQV5L7ibNRawa6H2SuOHfBnicTyOEECfC1ibG1DAx0Dg40U/640?wx_fmt=png&from=appmsg)

如果是src已经可以提交，且不会忽略edu就不一定了

一般一个功能有越权其他功能应该也不会鉴权

我们回到刚才的页面，点击撤销保修

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSr8dJHZ3mIAfE6gemG9plpKBQnAJUvXnAS7Q5031gn8qNH30C6bhwXbk2xhbdEPicmW93fgd2mAjAUickHEKJ81FNicaFhwtoZSY/640?wx_fmt=png&from=appmsg)

点击确认撤销

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTDKhLscu5GjGgqlX1k32IqDoG8cjHg8k996EE192zW5RgyZHh2ZnnmhT1ClogtSNKLS7MxVzznQLr0HMmehuZTNjlzibJhDQhA/640?wx_fmt=png&from=appmsg)

看历史数据包，依旧有id

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSCGpYnhQ2xSAo8RbJtEoFB9Ccu1cK9bzSqn1ypBYXC7hMMLhiaRXKgUg4QOe7GvNKL6x1020OS5Dibp3j6hPoWY5Zt7f6r3aSqQ/640?wx_fmt=png&from=appmsg)

这个时候在换一个账号登录，创建一个订单，拿到id,在这里替换就行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS6raxWqMDMd5t1mTicwDPVLJKaKdL5LbejY1BRZWGShQ7C1Qqoaq9o4lGYibbxOZTiaSZILEOluuhehKw5DsiagpyUT1IA9Lnia4T8/640?wx_fmt=png&from=appmsg)

依旧成功，但是注意这里是双因子鉴权

路径里面的数字和参数里面的数字都要修改

取消成功后再次取消验证，发现会显示，工单已取消

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSJXpXUhibdu9R1Txknkjo9vP0GUoV4DfHjfzYxVmSOhvlvJPlNo49xTibqHKRW4VsaxhzCbjRLGMgH7QCufZTJianlRghspmibLyA/640?wx_fmt=png&from=appmsg)

通过遍历可以取消系统内所有用户提交的订单信息

这个时候就没理由忽略了。。

交流群

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTK9XL3n9rx1ntXfFnAsQdvia4hmiarCs0P4lyrL0xzWxfoLt0pvzVev66m708JYS21sZunDbWcVaVkk51KqRkQSdWdkgemnggy0/640?wx_fmt=jpeg&from=appmsg)

广告：  cisp pte/pts &nisp1级2级低价报考。

陌笙安全交流圈子+陌笙src挖掘知识库+陌笙安全漏洞库介绍 （加入圈子送知识库+漏洞库）

如果觉得合适可以加入,圈子的价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。。

圈子福利

漏洞挖掘1v1指导,我给指定站,你测试之后出报告,我根据报告总结你不出洞的问题,以及看漏洞点和总结，当然你可以自己找站，我来帮你完善总结思路。（不包过，思路为主，主要针对小白，大师傅就没必要了，主打性价比，帮师傅们快速提升，挖到第一个edu洞。）

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboR7v3GgENCXPfzwrkTKCyTu5CqOHyDR8OYWSXCfN1PmCjibjGpF1eMPfTuyXy3Am2v80V9c2JPI24C22dZq7KamHjG1XDzVmndw/640?wx_fmt=jpeg&from=appmsg)

陌笙src挖掘知识库介绍（内容持续更新中）

```
信息收集弱口令漏洞任意文件读取&删除sql注入漏洞各种逻辑漏洞url重定向漏洞命令执行漏洞反序列漏洞未授权访问漏洞挖掘XSS漏洞挖掘CSRF漏洞挖掘dns域传送漏洞SSRF漏洞挖掘EDUSRC挖掘案例分享经典常见漏洞复现等各模块不在一一介绍
```

edusrc

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQnu4nW2B6yibZw9xtCZV3mz9T0RiaegrnQbrkPN9K6MmuOEgVAyGxNvYQbP8ibmpsv7vQrkZDQFEnBvMiasFAMDFAicJAIyvcCrHic4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQnuBhAKicDz7O0I514LJKMNpZDlJQIIGvfib7HKWheKRfmZdzMzbn68CnEvadbtJwgtficShGARp4wQM5j5UhvMje1mlGPStB58U/640?wx_fmt=jpeg&from=appmsg)

src挖掘基础知识

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboT4ibkLJNNa0HA9o4BLCmlqTG1cia8XbBuX35VU3PD8ellIA2GcQQScjaBFPHVbMKqGibZrgUdLpyHbMLl51Yencpic1AL4G3g8a5o/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQkY3kQH91B4gYTGY4En9NWc7Rw1P8AEKoPib0pafSCvGSqEfSUd71WLACV7ibkJPMubI2PzzPggB5kobfJDjodUam1WWtO2v4Rk/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQE2hEVIwic1JdKXjAvV643o5DCg6icYNODJDWuRxic5wbtPD19pdsIZIt8kANOEYJNFicV4TmtPH7icpE9Y3AjJon0oicoibictCArdA8/640?wx_fmt=jpeg&from=appmsg)

陌笙安全漏洞库介绍

```
1day&0day分享EDUWeb应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞开发框架漏洞开发语言漏洞操作系统漏洞数据库漏洞网络设备漏洞等
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboTTZew0YHtPpDKj0nNHkWumxYhM4AWT1IcicYengasC1hqDZEH6apvoYbUicZxmEXqaP2KHN12sLpE1sfJsFkcsP0YDnuQfRwJFM/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboRiaYMwt3UwQHJoAtQPLhqUncQmQBwRlqg6aGAsWmsibZnAQSt8dw3SfEzbaiagM7hsWJjCZWticq8937yn2W9H8Z349DbGuOicHD8E/640?wx_fmt=jpeg&from=appmsg)

圈子介绍

```
1、src挖掘思维导图，信息收集思维导图，edusrc挖掘思维导图，以及后续的红队&面试思维导图&自己网安笔记等持续更新2、2025-2026的edusrc实战报告包含证书站和非证书站以及2025之前的各种优质报思路分享3、各种src报告思路分享（内部&外部）4、分享各种src挖掘&edusrc挖掘培训资料&视频5、不定期分享通杀、0day6、有圈子群可以技术交流以及不定期抽取证书&免费rank7.分享各种护网资料各家安全厂商讲解视频&精选实战面试题目8、各种框架漏洞技巧分享9、各种源码分享（泛微、正方系统、用友等）10、漏洞挖掘工具&信息收集工具&内网渗透免杀等网安工具分享11、各种ctf资料以及题目分享12、cnvd挖掘技巧&CNVD资产&src资产分享&补天1权重资产分享&fofakey共用13、免杀、逆向、红队攻内网防渗透等课程分享14、漏洞库&字典以各种内容不在一一说明15、cisp-pte/pts&nisp一级&nisp二级&edusrc证书内部价格15、如果有漏洞挖掘问题或者工具资料需求可以找群主(尽量满足)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSY2pbvbP3qGAlW8O43bRvAISCxZm4UDTRsaMVbJKTsjfTMTDlq6qNBcVs4tkl4UzgqGz5ag81baU1rusKE09J9T6cMVliaibibwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTrLRQpTicOR7bzyNiajiapVJgyMiaYlEDBVU87YXMnanOFWsCYN3cCVGsKkibzV9dMryvbFXBb4Z3472ib27RJ1Xq1HnKJIp5u49GYQ/640?wx_fmt=jpeg&from=appmsg)

目前560多条内容，扫码查看详情，持续更新中。。

如果觉得合适可以加入，价格不定期会根据圈子内容和圈子人数进行上调.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQAD39Tr6hXUIic3ruKMtCkPcUQPfbat6V7d6EUdC26Ntn053G07hnsdSWVuU6nShEv7rOsP1GwQtticGgD5ic8VJMziaNhn1njvibo/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![]...