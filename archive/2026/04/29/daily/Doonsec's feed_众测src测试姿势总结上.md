---
title: 众测src测试姿势总结上
url: https://mp.weixin.qq.com/s/G4L5Q1hQ-OuPMNqKpGTmTQ
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:27:45.007747
---

# 众测src测试姿势总结上

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQopZrqgN32bibmEiav7kUzWby1jQHs8JSHwXvQ2y3hW5sV84SqwgHjUdTQX4oHv6RGnCwQaVXMDblzjnNBEy29Otl50puGT4lD8/0?wx_fmt=jpeg)

# 众测src测试姿势总结上

hkl1x
hkl1x

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:hkl1x原文链接:https://www.freebuf.com/articles/web/460765.html
```

前言

最近在打众测和src，也挖到一下洞，这里分享一些我的测试流程和思路，希望能帮助各位师傅提供新的思路，共同学习，共同进步。

### 支付漏洞

###### 支付漏洞是渗透测试的常客了，只要是商城的资产，支付漏洞一定是第一要测试的点。这里说一下测试的思路吧。

######

订单：敏感参数是否可以修改，如数量，价格等使用小数，负数，四舍五入，int最大值等

优惠券：是否可以并发领取，是否可以修改优惠数额，是否可以使用更高优惠的券，是否可以使用他人的优惠券（薅羊毛）

其他：是否可以更改订单的取消时间占据库存，是否可以使用便宜的商品购买贵的商品。是否可以突破数量或地区限制购买，

#### 数量修改

####

###### 1.测试到医院小程序

######

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboStBiaFKcRibwkicG3HSEQ3gSNYt2bViaFkJHFEyicB4BJF71amSxD9hFkiaiaSHlCsuBxQqAG2SBhMaGwNIvI7XgRtVLQQ2vPpOByyHQ/640?wx_fmt=png&from=appmsg)

###### 2.测试业务经典的购买订单业务，测试发现product\_id,attr\_value\_id,client\_id遍历都没用

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTElJMk63DT33ibUpxCJd88ciaMbhpnY0gZaBf4DHZtGZlUicybJReBsLrriampZhtqmJud3LrRrF87l07quyCVM9obNzt1KTvgg8c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSB9KBfvspw08szCagteFpBnbvjfk84VHtakyPLe3OiaYYtoQuJA2vPbGG5RicJ9Ev2IllwgahT9mc4W87j5jbO88jzVOh2LTibqY/640?wx_fmt=png&from=appmsg)

3.最后尝试修改数量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRD9TTIRka4V6cjM9bvhxs6xvo7voG9aevtqBibd42icyia63pw6hkb9Cg0iazkM1zib43SMYdlf09JCLrROohb48AicJ16keqRSC6yA/640?wx_fmt=png&from=appmsg)

4.订单生成了？！！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSrp3Cf317qSWiaiaJubhUias4bZp0ia4nMwviaIeFsMX5hXXHHP3bSp2YVgGJ42iciaqlT4YYiauOoVvgdvSyy5hK4JKiaYfI49hLJJBUM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTngRrKSDZicBzV5GVlH1t2ddg0MSPUmnJQJJ7r9IDgQuYS5URN5GGV84Cfgzn9fYSHTZMVoRVyrWH0FKyDVVLLAFEfZHucPfjA/640?wx_fmt=png&from=appmsg)

#### 任意优惠券使用

####

###### 1.定位一处商城小程序

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRndaTwM9ZMu0KIDicwtBfkteP4mlpoeIdpq5hk07LoNia0ZOXXffCFydwwPgFQcHZN1GUSdGUcML4t2ibQeBekIShzwzvB6tmFrQ/640?wx_fmt=png&from=appmsg)

2.下单后抓包查看敏感id

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQq5CQy8eGj7ZqT8kr2Jt3QX3I7l09F70PdjoPfEymo3W0DZsA1HISBrR3d6Iiaym71dzaSQmqO2yHdiaZMgQKiaFAsdAb94qvm44/640?wx_fmt=png&from=appmsg)

3.我对数量修改后端会报错尝试跟换更高优惠的优惠券也失败

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSfMFye4vImLwT08HwoaGF80iaVibIY4z9YQHY5ChfKkFoJwd5AxECAn628hgmKMKx4lic92Iacy7Iciae7nPFkT0evuGJxqI1rjsM/640?wx_fmt=png&from=appmsg)

4.然后想到那我是否可以创建一个新的账号使用别人的优惠券这是新创建的用户的优惠券列表

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQibdIlokxwosJqwFl0wOle7A2vibrDmOQMYFYedfAiaO49YibOVjvKxuOf7CFzpvn6oXESV8Ra7sySjVuPibwUAHWG9leEIicicpVIOg/640?wx_fmt=png&from=appmsg)

5.成功使用了别人的优惠券

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTukhzNJmNSWMfWgXJPpIc3GibaXsCib9zJiaNuic1b5QlrU5iadv8PfzdHuegibt4iaO6ic7K7InOPWZk6rJT168t3CcPlxUaOibYblIo4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTh3PPGJ6onvV3Um7GdSUhs0AZxGia420a8DvDmibmvTIoosAiaCjXEoh8iaCCZhtDlQe2ZG2rlmKF8ZL8UibdfzhY65prSZDH8M1sM/640?wx_fmt=png&from=appmsg)

#### 修改返回包

####

###### 这个思路是我看别人的，原理就是生成付款链接的价格是看前端的数据而不是看后端传来的，导致支付价格被修改了。

###### 1.发现一处商城

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQB4jv2OGRAunFZibHcjRP2RpblArWzO5oERqcI3kPqkp1ia6KgfY3bv62CKIrjNFziag0Zrm34EC4DKS14am0E4ZMicKwAyHIMZyo/640?wx_fmt=png&from=appmsg)

2.正常逻辑购买查看数据包发现价格查询接口拦截响应包更改数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRciaWlctOg2YPQBO9rHe6ncz6DyPrbVfTaGlQacF0G2T0NljIibjeFWgRvWx4FRvZ0umsB2KeabpmpnZZH6GXcpwW8x3rUyFEDQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTautbvBfpGcWo2fnhXVF5kxrufCI4u9mriaDRaaXTiaBYD1rslZYucAslHwGqKqRX4Xrbicbw6wMGFep8CmuwWHPkWiapZGZ2S5Dk/640?wx_fmt=png&from=appmsg)

3.查看订单

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS0UJvsjZefW5XRLfBRxDwtrsLJXY2ReyaSqnxu6HyUWTANNG8NKUDQeic6Vmhu00ibgm6S7n1pzqTLWozbQj5y0ria3uLaibwUm6U/640?wx_fmt=png&from=appmsg)

### 文件上传

###### 文件上传漏洞相对简单，主要还是看能不能上传webshell拿shell，不能的话就上传exe或者文件型xss，没啥说的，遇到waf就可以换业务点测了，根本绕不过，这里说一下测试的位置吧。

```
更换头像评论区简历上传编辑器
```

#### 评论任意文件上传

###### 1.找到一处医院小程序

######

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQRZctaQjXS0ibwxeeveIOht8WrMOSov7bbzduH9BkPz44ZiaApgSOGhdn4Eq5iasoDdbO1iaO9ocXTwytibBHdtXlLaZibufFGEKwVc/640?wx_fmt=png&from=appmsg)

###### 2.在上传区图片功能抓包

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRYGrCqcnPoAJknpPkicLQa0AOcgeNGtAxj4ml1T97zPVRF5daJqpiaSvl86pP7ic9SLIm9ZFVD6M4g6o95P0IoSKqqVFXibMiby4ck/640?wx_fmt=png&from=appmsg)

3.使用重放器更改后缀名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRXlnicDBbNsUMrOJIzFTZC9YaicFYQCE4rsE2UibickhFQ8URuoNMqxCmmOwHicBU86kItRjZFeia17ib03UqfrbtGf0pyttYuNAEeg0/640?wx_fmt=png&from=appmsg)

4.浏览器下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboREOcHCZia0jLgtQCCSmrWEBlQUzcGgkYmjFo3hnHRa1E9XFp54RG1WIvAR5gUN99J2zj5cMfPVCsPCp2YhVJIEqIhib0Mr0fnR4/640?wx_fmt=png&from=appmsg)

5.扩大危害上传pdf型xss

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRmo8w6iclLQlFqnYiaPyXawhCttSErhuaSnvJoOX6uKQT9uhVZToBr7aRTaunJYwNhyQxtia8wv4AIqRNeq0RpibbCPoBwWhoYKMI/640?wx_fmt=png&from=appmsg)

#### 头像任意文件上传

###### 1.小程序的头像编辑功能

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSuDqnicoDNuPZASX0kg2sQPLMUGgG6mUSBKgHroTZFqemOg9svbsZ90N6Q5SbyaT6zbXHgFSEGhRvfScYQATNd9wIpq0t27e8k/640?wx_fmt=png&from=appmsg)

2.exe测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRo8JucxT3V4A4w29dfiaDiaOMvf2GAiaHLGa0EYVEF0icbdicfcSCAtSEPia7y2jibTHviaeZvVOwKRkhO1kDypbiajqRRgX6SiaPSiaRS5A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSib8hfEYKyxjqiaGHplnhSIkAXuGlAtHVuEVria8ZEKUzibHV9a5O1DDM8ic2FSd3yI6GEgCRL6tU4HgrN0pE3rciaRCakCWYxWyLqo/640?wx_fmt=png&from=appmsg)

3.并且这个路径可以自定义那这个就是算高危了因为这个一定是创建了一个文件夹还可能存在覆盖的风险（这个是没有的）

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRq1T0qpAFNk8WXoBfvAWv2tuduSZwZCzRsRRqkyDjxNf9QQyro520DfBtAYG3eouZAfp2v9LuoZIqdvfJ6tWNnnGvF0kJ5k1k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRVOEzRiaJWLmaXTxMWYdzApJ0mgHztQa4icM8QlSIJJxXmvsvwWXLV4MDjgQOII9U4E9WkrGHibMwEayABv0uibFa12EGqeic6ibYw8/640?wx_fmt=png&from=appmsg)

### XSS

###### xss应该是最好测试的漏洞了，又是都不需要使用bp，主要就是先拿a标签探针一下，js解析了就继续往下面测就好了，这里说一下测试的位置吧。

```
评论区发布帖子公告pdf上传智能客服编辑器
```

#### 首页xss

####

###### 1.找到一个人才招聘网站登录后台发现求职功能编辑并发布

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSTHdzlhPQC41707j2icwuelofFxCFB4To63nesvRDdMAelVGicPlR1B3EbnRe8m2gNxK6QqA7BupIVq3LpEBMJIQ7qHDqvFOtIo/640?wx_fmt=png&from=appmsg)

2.回到首页发现js代码被解析

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS84pZ4vBdhEzFCCl0kUb8UQC3XqVyL5XB6RzveQZVBpHH9RF10hhwRB8ch5PNxgmdggZGRCibrOO3hIUB3XYQGjqE6gWWGxFOU/640?wx_fmt=png&from=appmsg)

3.在意向职务输入payload并发布

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSNjZZv5zuzXCTJOkOleOQOIc8e0wibaJgzhA2PdtVEnneRQaK4lLibjAdtX2bLmVRMVBPDVPOMASMB7QJMFfD5PNq4CPFv2qQVo/640?wx_fmt=png&from=appmsg)

4.返回主页

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSvqVKf9FDomLVccMBUW6aXDJE7kbCXmWsRCwRR8uzV5ufWz0viaiaicZBUsib2LmLWj7TJnhIUO6Pjfyk6k9liatalSOsHz36g6XLE/640?wx_fmt=png&from=appmsg)

5.因为这是一个大型的门户网站，所以主站也弹窗了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQRibuxCruiaia0Q0icePw7uL1T63X8oByfEFbic9vBcag0PVvdOvhcuD4zOTjqELU2lFYKCUO0Op2UKopibsybW2awPvnnkBThqVaoY/640?wx_fmt=png&from=appmsg)

#### XSS+Cookie弱加密账号接管

###### 1.找到一个租房网站，发现发布功能尝试xss

######

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboReGGgWh4Z609xJSX1ytfD0BFicPccR00FicxTQnTKS4zBVYJC0CTSVrf4NYVufjgxCE9j9wIcAcs45cAGmejp8LbKHYqUJjNMqA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTmhWoTsXicJD3pgibvtuCIwezh8r1GKHiaTL7UXYNLyQngnBKCg2U15rh8psIYvucoJYffRlofQFkhz5xpwc1o5QwxqgeCNDZVkM/640?wx_fmt=png&from=appmsg)

###### 2.发现解析js代码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ7gTchPxQz0JEdRJOdEQfhCS9EIY3WE4kUGqiaJ47lQE0asnXBKIxFAxgoWO9IHHutmHSI2ZoPDZFGicibEuEzyumcGhhvtP2l5A/640?wx_fmt=png&from=appmsg)

3.发现Cookie其实就是用户名和密码（md5）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQrzauTt...