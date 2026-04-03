---
title: 记某edusrc从小程序xss到web未授权再到任意用户登录简单挖掘
url: https://mp.weixin.qq.com/s/XxTPtZbnEh8FTvyf-Jq9Zw
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:24:54.194925
---

# 记某edusrc从小程序xss到web未授权再到任意用户登录简单挖掘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQALrngYanAqGZqRB2AHTYDr8fuR3AwticOOxTz9cg25wXVF5N2RtygbAS8uBQXDUuPQHUvPU3nK9Me3rUeYry9nldlA0LzsQww/0?wx_fmt=jpeg)

# 记某edusrc从小程序xss到web未授权再到任意用户登录简单挖掘

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

信息收集

依旧小程序起手挖掘

输入对应学校的名字可以看到这个小程序

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRbLjnv99M1h2ibNmLicYicbW5dswB215YEgcVzmxP6ddrLVdYn5acp3oRrUF2mNgW5sIAxq865QV21BYxEpX1r0bvSKcMMZRGrks/640?wx_fmt=png&from=appmsg)

两个看起来就很脆的点

漏洞挖掘

点击访问登记

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSbHjNQfJ0h9IiaAjI1ibPSfMy9jspR5GlCT5VtUtc2nG4wd8b74sVibRSs0oCiabNvLwnprTSE1Kd1qkxh6cDzVvEkfQNv0EaE3o4/640?wx_fmt=png&from=appmsg)

可以看到是一个用手机号登录的框

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSibCJOouibSYlDn0lDiceRWc9yYK39u7rfAIr0ibSibqCLwbbof1ecP5pSwklcsCd5kmufbsyiaqiawwMFHrrYpme2icIBEx190Ht4d3I/640?wx_fmt=png&from=appmsg)

这里可以简单测试一下短信验证码相关的问题

不过这里并不存在，我们输入手机号正常进行登录即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT6pXNptr9DqT993PWBNicibH4bg9OEX4nQ4Ak4MNRVPdUyFhgtV4FYGNzRCVq63ENInIEzLpytWdibYQnYyUh2FlWpUPOjgbvO5g/640?wx_fmt=png&from=appmsg)

登录之后可以看到有来访预约以及查询两个功能

我们点击来访预约进行测试

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRwc7d7WvCTcUodp3GIWLsa9pXdfXqYLLQv5sG1LR41cNtnsQ6HvF5t5BgQPEL8JAYyPic9o97n5rfiaSgicG3ib4hbTl0HwuS8Z50/640?wx_fmt=png&from=appmsg)

看到一个上传图片的点

试试存储xss

但是他这个图片必须是人脸其他的图片传不上去

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQryLs5WAy9ZSeSzbIDx64JhHeKmek6SCCSvZEUuzmLey7ibc8SVRsPLeyKx75H3ZDNTxsytqnW9AAYHyUBDvU9lXLsleZhbFmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ99icgzoiaVicFo8XlVAwRD4FNhfcN3oaicerLFqDUJhD84KpSeqIvBQRPEIWgdlPsVCiajQhdffLZFBhL4VoTpaJQ7WNxNtOWEhqI/640?wx_fmt=png&from=appmsg)

直接用人脸进行上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFibCSD3TI1wria59kIiaVU9jSI3WP3KPDYictPK2KU79iaWw8tUUZn3wVoGUXJHV9qb9OAU9le7ybsRXRmx9rsO0xMicg2qHKW2kAc/640?wx_fmt=png&from=appmsg)

可以看到图片能正常上传

但是上传html之类的，会直接被waf拦截

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSYG9mjpGrhdd0nFwHOco1Tic6fdFIrmCQQeyeQHzGqngW4RRJGxl79xyEicKPoicVHBibs4jFiaAdsreMjavcruoXAzIXJw90JdYRU/640?wx_fmt=png&from=appmsg)

连接被重置，响应为空

我们上传xml试一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQJmfdibGgUQpXsEO9cvC7YpeMRa2HfNpjWyBEia6RTl8CqfCtFeqNNBFXZgFibYBxlWt2icBllvfQ9PZ4prpHdvIo4ibgj3a70NaHQ/640?wx_fmt=png&from=appmsg)

成功上传看看能不能弹窗

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTXCsbxHoR64KXvuf70vZDG1UpB6DibWoicqrpNEOuicY7Fw7hya6Qhsp0jxhOmWw055f94xvLiavlAz37ib2gW5mPrQzQFpQjYL0iaE/640?wx_fmt=png&from=appmsg)

拿下

然后正常填写信息提交，看有没有越权啥的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSD6UV0hA3MN7jXKicAOu9icJ55hMnPx7iaFEXzdcGg5hpXonzz6t6OpmXicMLVII55ibGuJVL1CDWe4ciams75Q1QFWkQEBiaXftFiav4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8d0zfuSCorhKvyqqKB1tjHD8NNqyibzEd8SjbgmicZicYHS2xouMz3qnzKcZkgc5GvXoUpLk6ZClVSP7KiamW7pGA4uorjEfon3A/640?wx_fmt=png&from=appmsg)

提交成功没什么明显的越权点

看数据包有个url可以试试ssrf

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRzVeufkeL0YiaN6SDUHCeqqWASR4ibgAcdt0HQqKr8a5dN3lvHiaY8aibCdkwxIfU7jAgloTVFNHEdEGA6bicEyYgaewbianunHM0Es/640?wx_fmt=png&from=appmsg)

又被waf制裁了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRpLQxKO6SZHjrWyXJq0JlUtpoRLjeS6hfz8lPCl7dHtpoe92aER57s3tfPiakurESfswcibM526yialoptXJSxOKwKfgLz4HY8PU/640?wx_fmt=png&from=appmsg)

可能是dnslog的问题，用bp自带的试试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRdVOWdAgHOSfZoF1icn33hKKozOdTO1cKbHdcZ5N2rPcYUSNRV3dWib0h6xWKoTKhbvaortd4ibgYFu4MUpU2T9AH0lFeVb6K2t8/640?wx_fmt=png&from=appmsg)

成功了但是没记录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT0AKDT26GD0o5nE4XAboVl30KrRdReaQ7y70z5eUaJia7cUTFBzFuRB3IAFiaicKyfrUMnJaIL8qYqSkduhf7UciaajpIAjXibTDw8/640?wx_fmt=png&from=appmsg)

只能看看别的点

后面点点功能点看看数据包

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRfyHaibia1jpgKW9K2lGtJBDicr9rIys6OgPEIna37MaBCl5Ogj6hcyFqVwMQicbiaIRGA74dlF95lK4h95QyMh6N5xn3RNs5p1e5s/640?wx_fmt=png&from=appmsg)

发现id太长了，不能遍历，而且返回的数据包是加密的

尝试滞空，改改null,\*,%之类的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTAibpqL1IrIeFyibUibLHDKlNicicoLlDRz1A7PvuY8eRj1oTKxnTGpiawKriau4oUGqydmKvgmAVANliaSaCh8ndbESUHbUkQzVicN3ick/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSXB8lHgPOCcR4y81HvkHSmOiaQXoaic3s3PKJ4R1Wob66V2HS2z9Yyd6mUjliabo3FSSF9HMqXm2svzhHVq9VHk1ibpR37d2aKxdQ/640?wx_fmt=png&from=appmsg)

这个点不好用

但是可以注意一下这个id的格式，后面可能有用

看这里有order尝试sql试试

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS7SWQ41Txo5ES7dadgmboNWWjibDB4FlRicCMj3aPSFP9soLra7JM1YPhve0Q07A7p5muSdfuxia3u9OSEnXibKwuPrxJBlH90ONw/640?wx_fmt=png&from=appmsg)

没东西

小程序就打到这里了

复制url到web看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSel9M1iayGwUoHZ50OS56jib4CQxUedNgbJPQID1YeLrUpaRgs3BKlsrM9uPv9zAh4RDXeKiaCX66vGGGcQiawbdrGfyMwhicicUUTE/640?wx_fmt=png&from=appmsg)

直接可以看到登录框

我们直接测试登录框相关思路

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTQ36nqLFgwvv4RSm0q95qPk9O0ibNTdoLy202hoDfzj2iaSk0jnlxThjTatfeRxAZiaba5WyWHw6eFrw0xVmWObYKNFyibuP0Vj2s/640?wx_fmt=png&from=appmsg)

经过测试

图形验证码存在复用可以尝试爆破

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQmxfJqSCRlxic2qbPuI71WlOxpXm8h7fiaqSGaOXARNBmrIY1Ir0t0OUn72m2UaPibCL0kPDZR4deYRAuwg2jUt1VVEJ7icQy5Ub4/640?wx_fmt=png&from=appmsg)

只要第一次输入正确后续就会一直正确

爆了一下啥都没有

看看框架，是vue，尝试测试一下接口未授权

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTvq9o4HDw0AviadC7MHnWZacYYZyy75WVDzmFyG3mJ8dXCO11fkhBiccl5HUGJ5Lescyko6qcb9iad8lqhUBsysWmG2gicKQsIpww/640?wx_fmt=png&from=appmsg)

点了几个路径进行查看，都会重定向到登录页面，让登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRicmxFXqtkSKTt0Enc7nnCZRaFvqmpsuiayYicKOnIwpROjJLbKF8qeiauRsBM9FF8D3UT0B8Jk5GFzR0Kiba8ibNZ21ibaSWhvGNW78/640?wx_fmt=png&from=appmsg)

其他利用点没有还能怎么打？

可以想想，我这里复制接口，进行简单构造

利用bp有token的数据包进行fuzz

但是我这里只是演示 /#/这种路由一般用bp跑不出来东西

查了一下

```
核心原因：# 后面的内容不会发送给服务器Vue 的 /#/ 路由属于 Hash 模式。在 HTTP 协议中，# 及其之后的部分被称为“锚点”（Hash/Fragment），这部分内容仅由浏览器（前端路由）内部使用，不会被包含在发送给服务器的请求中。地址栏显示：https：//target.com/#/admin/user实际发送的请求：GET / HTTP/1.1结果：Burp 收到的响应是根路径 / 的页面内容，而不是你期望的 /admin/user 接口数据。2. 常见误解：混淆了“前端路由”与“后端接口”/#/ 后的路径通常只是 Vue 用来切换页面组件的前端逻辑，而不是后端的真实 API 地址。错误做法：直接爆破 https：//target.com/#/api/getData。正确认知：真实的 API 接口通常定义在 # 之前（如 https：//target.com/api/getData），或是通过 XHR 异步请求发出的。
```

```
解决方法抓取真实请求：在浏览器按 F12 打开“开发者工具” -> “网络（Network）”标签，点击页面功能，观察实际发送到后端的请求 URL。修改爆破目标：使用上述抓取到的不含 # 的真实 URL 作为 Burp 的爆破目标。检查必要参数：确保补全了 Cookie、Token 或请求头，否则即使路径正确也可能因鉴权失败而无内容返回。
```

实际效果，可以看到确实没东西

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSibS8wzyK4viarD0UpYA4c7gkqhZ5w615iceqW3NBusumz0F0uRUibl4QOdpupVp2Ce4WvamzD59IQp88T2CkUJPDvz6RhGeUlicHo/640?wx_fmt=png&from=appmsg)

登录框，抓个包就能看出来，请求的是/#/login

实际走的是

demo/base/back/login/no\_check/login?name=&password=&code=&verification\_code\_id=c61ebb5d-4082-4944-adb4-232c1718fe9b

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSWJTOxL7FoyibWVjYSRSMCQsMnia6Ugj5JPkjJJ1FCSpDcnM7npOQNjX8ibFr7gWKlnkwYgHRwquxJ2Uy5QUD5KOGcibYDqHSsZgA/640?wx_fmt=png&from=appmsg)

我们把/#/去掉使用burp试试

有些接口能用了，很多不能用，估计是二级路由的原因，我这里就不测试了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTZfQm2A9nmic5QPOqeRVibb6iacfD4H9jMdb4hUnw7AsbjZ6EdsJ2ylX1dRBWv97EiaUzAlRmdmQa7EpXYtz2Zdx9phEbb2Q8ypkw/640?wx_fmt=png&from=appmsg)

我还是推荐直接使用浏览器打开

可以一个一个点，也可以url多开

这里又有一个问题，直接访问有鉴权，看不到内容

我这里直接复制小程序登录后的，cookie 给这个插件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSnYTabujxCYalsPj8qYlvwNrBgtrqqlLkibBwoSTqv8niaWeWb3jDLJyOpZcJ8dbm4C26ZmjSxB5xLMT3Fd1s8kOpTmbwIhav9k/640?wx_fmt=png&from=appmsg)

再次尝试访问刚才的接口，有内容了，访问一点铭感的看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR2T38vI9HTaq8CSvHSDhvsBrUX58QKWVI8iajJMPjaUtcRwBldia8qugO1kXPD0LpmF0Rs1NCc8PiadebtqjXsYnFibKrqUVYgibOA/640?wx_fmt=png&from=appmsg)

直接可以看到，全校的教职工以及服务人员信息

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQjlfEmvt3aR1wDHPML5nZBOONS1CeG6KjbbTBRBuLf5reAUs7qqx7zYibAzbZQjiabBreHa0CBHzuhwg9LcSmMpSZ6kkMEia9pk8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTRDDRfk88H7yTz9J2RqaFLGGPSngLe4MVHHNTibBmmJMgGfayxbPeciae7qjfv5FGcnDbmiceIavic0PVGunWXXle...