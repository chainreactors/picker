---
title: 吃透APP逻辑漏洞挖掘思路：汇总越权、信息泄露、重放刷VIP、加固后仍挖出高危逻辑漏洞等真实实战案例
url: https://mp.weixin.qq.com/s/kX3gnGpTPU06rrJTsEyb6A
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:58:16.761335
---

# 吃透APP逻辑漏洞挖掘思路：汇总越权、信息泄露、重放刷VIP、加固后仍挖出高危逻辑漏洞等真实实战案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibrevicNauKAUJS3KPRNH6neanRJIHiaQ4aPlZ62kuFGt2xbibNMT14jPWXb8c451uwGl0zTM4DqxuoeLy7By4HfhC7znr0hrPZ8pW9jK7VhnFI/0?wx_fmt=jpeg)

# 吃透APP逻辑漏洞挖掘思路：汇总越权、信息泄露、重放刷VIP、加固后仍挖出高危逻辑漏洞等真实实战案例

Myan
Myan

渗透安全HackTwo

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**0x01 简介**

APP逻辑漏洞的逐级挖掘实战思路与全过程，从基础登录页面漏洞测试入手，逐一复现短信轰炸、无回显SSRF、订单与优惠券越权、用户信息泄露等常见高危漏洞。同时突破传统挖掘局限，针对APP签名加固防护环境展开深度测试，成功发现付费内容泄露、数据包重放无限刷VIP等高阶漏洞，全方位讲解依托业务逻辑突破安全防护的渗透技巧。

> 本文仅用于技术学习与合规交流，严禁非法滥用。因违规使用产生的一切后果，由使用者自行承担，与作者无关。

现在只对常读和星标的公众号才展示大图推送，建议大家把**渗透安全HackTwo**“设为星标”，否则可能就看不到了啦！****

参考文章：

```
https://xz.aliyun.com/spa/#/news/18760https://www.hacktwohub.com/
```

****末尾可领取挖洞资料/加圈子 #渗透安全HackTwo****

****0x02 正文详情****

记录一下自己之前所挖的APP的一些思路，主要以逻辑漏洞为主

# 挖掘思路

首先我们拿到一个APP时，首先应该要先熟悉整个APP的业务逻辑是什么样的，才有利于我们进行后续的漏洞挖掘，接下来我将从低到高的讲解挖掘过程。

## 短信轰炸

首先打开APP映入眼帘的就是我们熟悉的登录页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXw9ByenQolZlhokjUubAAhuSyyxYRiay1fYyU0NfCEtibPbhPDAiao05xPF9HLqnrbEc7RSAbujrAS0YTBwHcGmf4kaT5uZ18oMk/640?wx_fmt=png&from=appmsg)

这里首先我们便可以测试一下是否有短信轰炸，任意用户登录等漏洞。而测试发现的确是存在短信轰炸漏洞

这里填入手机号后点击获取验证码抓包如下：

```
POST /user/getCode HTTP/1.1Host: xxxUser-Agent: SM-G9810 Android25 V1.9.0.1Platform: androidAppversion: 1.9.0.1Showtest: 0Oaid: Vaid: Aaid: Imei: Androidvendors: samsungOriginalua: Mozilla/5.0 (Linux; Android 7.1.2; SM-G9810 Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36Accept: application/vnd.edusoho.v2+jsonAppbizsource: 0Content-Type: application/x-www-form-urlencodedContent-Length: 28Accept-Encoding: gzip, deflateConnection: closephone=13555555555&codeType=1
```

这里修改phone参数对上面的数据进行重复发包即可打出短信轰炸。

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXPJ3CJcic1HibuLWGviaXgAibxtwnLbPdVb1Ae5JS6lEsXhiaLeMKDILdicxGcZJGwkVd2scibOmOz8yKjdXvhQfGawbm5aicP7ZRNCMU/640?wx_fmt=png&from=appmsg)

登录页面测试完后，我们就该进入到APP中进行测试了。

## 无回显SSRF

进入APP后，注意到意见反馈这里

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAViaX1SepIBGTeEvkhK7u0XRySgFBJn0YSiaydlrPZGvknP4ibeb17lyqk06uzy0G6o1bEyv9IYGtBgR1ru1ZzGsVx1FdU0k0t5Eg/640?wx_fmt=png&from=appmsg)

意见反馈这里可以看到有图片上传的功能，可以抓包看看是否为url传图片

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVvAQIdnWC2icU4qibQPzO3NtyXZcBnqpTUSp06ibibjwtg4jIXIYWmHU6pLnj0IIic5N7xfpuvWJWoogrwGr1YKyDQM2sLNIxMLays/640?wx_fmt=png&from=appmsg)

数据包如下：

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU1DG5lS3OplegMc3yVmC1UmsweTnGBkib1nf0pl1IlKrYicoc69TRP21IqGe1nnRscVVuyRsVFASqWIBCG8Uicfe1gT549ichN83o/640?wx_fmt=png&from=appmsg)

将image参数的url先换成自己的vps看看能否请求外部链接

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAViaqVv2ibwSB37xMuAOKjtu5GXPt6U1UjGXuwBB3OGROmTUHN21gnQMSiaNPoiaZz45zJfh77wh8cuBjpRUTkxaadv6uo6RTQzSf4/640?wx_fmt=png&from=appmsg)

也是在vps中收到了请求，src中给出了ssrf的测试连接，打入后截图时间给审核验证了。

## 越权

### 越权评价他人订单

APP中的服务内容为用户下单后可以获取到对应的服务内容，而这过程中发现评价订单的接口处存在越权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUK77yUPnwXjpferYyEvdoHrqx1CRycrZHP5l4TJqxjAvopCcUf7IXNy0v5I0Q9JAGq0eicWMJIovvfV8RQckqDZzoTTx8iaA0X0/640?wx_fmt=png&from=appmsg)

这里我们下单后先不用付款，当然付款也可以，之前该APP不付款也可以直接获取到评价接口

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUibBCgRUk6PC48lLdwRrsgCjO0bibS68bUSWc0icq3nN21nDIiaHSdYSGultVicDPQicVsMxVgeGCzL39ViaaLvAoF2yqcvKQZgKaJao/640?wx_fmt=png&from=appmsg)

来到订单详情，点击去评价，填写评价内容后发表，然后使用bp抓包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUAMicIQTKjx2qZRiaEqMotOOPficCrHoC94YDicCAgPrHx8C34Vp0AO8OCKV1dX8Yjc2FCCS2vpQ2ptia6ZFV32ibGzsAtLjPVK8ooU/640?wx_fmt=png&from=appmsg)

可以看到我们虽然点击去评价了，但是由于没付款完成服务无法评价，但是我们可以注意到orderId的值只有六位数，很容易进行遍历，这里我们进行遍历

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXYOQibyialxiav1uaAQdGtdtlXsXV01qZ5F5RETtOnnk8lHt7LiathibnCqRXRt67O3mr6Gb2dRiaM7CcL4biaubyEwZWPxLbgw4c1y0/640?wx_fmt=png&from=appmsg)

可以看到遍历后可以对其他人创建的订单进行服务评价。

### 越权使用他人优惠券

我们选择一个服务进行下单并抓包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAU2PracvwZWicQHtmr210gpOyRY1d60aLZiaNweiblDCLXF1QJTcQekDdOuw0wcyb4ZlPhdK6ct6Z088F2dyLs8WC05Pqn5SfCS2g/640?wx_fmt=png&from=appmsg)

数据包如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXalUXyXZwoZEMXDSCUVT7ibAI5hwJX08tQozl7L5WkAadCrxqlEnDkp2IBUZe50lGSfuHRswKMf5b2NfkKDNRdpRoKL69mD4XQ/640?wx_fmt=png&from=appmsg)

之前我们是新用户时，系统会自动赠送一张优惠券，当时的优惠券id couponId=1085908，猜测优惠券id也是可遍历的

这里我们抓包后添加couponId=1085907

然后放包

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXlwFcKTv16cmHYtkogTkmXzmW49kQicuUAZhAEdibvCIfAKSev2ElcCr0VEqAfBoQk2Z6waLPPlSy8gMU9bl8GjhFvx1qx3uuiaM/640?wx_fmt=png&from=appmsg)

来到订单处可以看到我们成功使用了别人的新用户5折券。

## 信息泄露

我们在下单服务前可以进行沟通，沟通生成的聊天页面如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVejMz2qkm1cmwfQHfXOu6icufQSTFc9LENiaUibrUBDWkuUia1geiaWwCS1MQohUXc3jMR2SDH1UBvoGaqK8KNwZicKwOWaHonVllKs/640?wx_fmt=png&from=appmsg)

在bp中的抓包如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUTpjgRLoVVWdzyicSU25UrwoIcHCcUeckqia1qSSrBCSuQZt6emmDxfDJtZHlBVugdUIn0mlUNsCOkXErvM3Bje2NiacsE4vibdgg/640?wx_fmt=png&from=appmsg)

之前我们是新用户时，系统会自动赠送一张优惠券，当时的优惠券id couponId=1085908，猜测优惠券id也是可遍历的

这里我们抓包后添加couponId=1085907

然后放包

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXNZiceLWpj8lFIa0MwAATYfty9wwh8f0PyBdAhIwf53ibdiblBcNcRCicjLp7KNtyYZ1qDqoiaXDUya74XU0eFqMUn55poPZvGgRJo/640?wx_fmt=png&from=appmsg)

来到订单处可以看到我们成功使用了别人的新用户5折券。

## 信息泄露

我们在下单服务前可以进行沟通，沟通生成的聊天页面如下

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXp6tTfuNaNXnug72iabP7x3OHhhibuhh0B3NRT4qunT9GCDDO3Orj7KMqYOfnWBmYGSO9k7hxsyjJR9rekGLFEGQB6CWjfWCp1U/640?wx_fmt=png&from=appmsg)

在bp中的抓包如下：

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVU8ovr45v29LuViaqRxOTu1lhv2pjusj34xI2jGLD3ZibBHwUmSr8mRTtqhcS1cQodeEjP1ywgcibCY8RKaCDiafbEPDiaY56ukLMk/640?wx_fmt=png&from=appmsg)

可以看到数据包泄露了服务者的手机号码，而服务内容主要也是通过虚拟号码电话进行服务，这里直接泄露服务者的真实手机号，并且imId也可以进行遍历。（当然就算不遍历也可以想查哪个人直接点开聊天框即可通过传入的上面的数据包直接确定）

# 后续

某APP在被提交了上面的多个漏洞后痛定思痛，对APP进行了签名加固防篡改，假设我们在不进行签名绕过的情况下还能挖到漏洞吗？能挖到高危漏洞吗？

# 挖掘思路

## 付费内容泄露

在平台上有着一些vip才能使用的服务课程如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXlz0kFqImiajID3Pt97Sic5wn8slyQ58o78315YbXfgxeotjnlcstgjaKagckvl9WcqhuEwoDD2kXPsYO1k9GCGy0MpTH3r3qto/640?wx_fmt=png&from=appmsg)

但是我们其实在点入上面的页面时，bp抓的数据包里面就已经包含有了vip课程中需要用的的mp3网上链接了

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVPXNnqWnJ35OR4cQmoKbl7iaczmUVAiaJdNUtibv7o57TSnJTzekKbgrqWyRmCD2uZSu14cPpzPLibMpHKOWO5kqrWoY3ictncM6CI/640?wx_fmt=png&from=appmsg)

课程内容是直接挂到阿里云服务器下的，我们可以直接访问使用，完全不需要充值vip

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUZoGPz1KjSa6Ltw3hVTdnoWaibqIyVzYS1o3lzD1ySAu48cniaJWllXC94zr0ysV9yE9QGroJp27sC2foWE1jibibbI8d0IcOMfRY/640?wx_fmt=png&from=appmsg)

## 无限刷取网站vip

APP上有一处邀请有礼

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU6wAQaxw9GwnvpsluXR5lliaGF9HLC6vj45mm2hdRY5wLD3ib84aaMwF7fShHPduPPIrYNiaZxSxtw14J9ib1TnqnU5kDmicDqLa3Y/640?wx_fmt=png&from=appmsg)

这里点击邀请有礼后会可以获得一张邀请的截图，发送后扫码可以得到下面的url

```
https://test.com/cashback/investMidPage?userId=950485&sourceId=6&userRole=1
```

我们可以直接将上面的url发送到微信中，然后点击链接会跳转到小程序

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVM5hr4s7H036bpa3NTZIqs1EQho2DuP8ByKwk8UEBqwsVQtUDwniaARPTsN5b7GmdQKxdw4ojbmhoDfGONVK3Xpu13HgT3oAK4/640?wx_fmt=png&from=appmsg)

这里点击填入账号会提示邀请绑定成功，绑定成功后bp数据包会有下面这条数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUvnn4ibU9K41J8uqyIrD1JnicGuowD4cx2c71NIpSSEgSkY0ESDfuN4oktqtT6l5klbyqKm7gjbriaL5KD2WxfPnhFpPtyb6ZSCY/640?wx_fmt=png&from=appmsg)

```
POST /applets/userRegister?sign=B43369DA38154CD9757706E3B709682C×tamp=1729442602682 HTTP/1.1Host: xxxContent-Length: 110Devicetype: 0Xweb_xhr: 1Usertoken: Usepaltform: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11275Content-Type: application/jsonAccept: */*Sec-Fetch-Site: cross-siteSec-Fetch-Mode: corsSec-Fetch-Dest: emptyReferer: xxxAccept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9Connection: close{"referrerId":"950485","code":"","mobile":"13555555555","sourceId":"6","stuInfo":"","timestamp":1729442602682}
```

发现这条数据包会在用户绑定好手机号后给该手机号用户+7天会员，而最重要的是该数据包可...