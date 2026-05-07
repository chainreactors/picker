---
title: Bugku逆向题目-20.easy-100(LCTF)
url: https://mp.weixin.qq.com/s/3EyTjcAqqiPAtTCwFG336Q
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:29:21.690606
---

# Bugku逆向题目-20.easy-100(LCTF)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6nhGiavBDP4anmrX2BhxIuVnmQAX7ZueJ8k9uOwKfNWGdNDjicicdXFCZo80nSha7RAbMfIkTnS8XzibkAQv8XEpcU3hFSS10vTPWOOkTzGN1GQ/0?wx_fmt=jpeg)

# Bugku逆向题目-20.easy-100(LCTF)

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、题目链接

https://ctf.bugku.com/challenges/detail/id/121.html

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bdXAMle2t20dMJ5X8ewcKzXgVy7humODpxC3BMwyAm3icZ7waiagxZlL55ySwgKILOQ6lpnrwwAFz2kTulWdKSPPZJiaUep1x89w/640?wx_fmt=png&from=appmsg)

二、题目分析

    下载下来题目文件解压，是一个apk文件，拖入模拟器中运行，需要在文本框中输入字符串判断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4b2Q1Vmt0J8Xx0BVia2SKxMayNOyhVOkh1iaR0Y8kMFib1773ibbwh23mKe6NG6shFp1tsdm1LhfNbZAAGwSkWKpF1iam1KiaQxwCbeA/640?wx_fmt=png&from=appmsg)

    拖入jadx中静态分析，可以看到应该是被简单混淆过，各种类都是字母表示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4b2icZzWSaN9A3icb8F9Nyu8nmeHLlEczicOF3exOZqJPchaKAeEY3ITuhf9iaibFpDicicmmAquub1axZ61cIxRnYCmb734XPQA3xFpI/640?wx_fmt=png&from=appmsg)

      找到MainActivity类分析源码，可以看到先读取了一个图片url.png，然后截取赋值给字符串v（具体内容未知），然后给button按钮绑定的点击事件是类d。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YLtdaDYSS3qL4WEnxGKraoXN293WFaZeFBqicnogFOjZPXoQnNoABkpOWOvheSQ6tB5uDmJicgf6u35nnxsiaic6JMNnmicXcG4TEo/640?wx_fmt=png&from=appmsg)

    分析类d的源码，可以看到调用了MainActivity里面的方法a来进行判断是否正确，传入的参数第一个是刚才是字符串v（从图片里面获取的），第二个参数是用户输入的字符串。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YST3ia4ZSMRapt9m6vmc4R2sDvWfA1MdteYTkXmWxfBwyIRvk60I5T9pHgqqsjIhCdI66QHF9ZGtojiboiciaYiao56CHy2qtxQK8E/640?wx_fmt=png&from=appmsg)

MainActivity里面的方法a调用了类c里面的方法a来获取一个字符串，然后跟后面是字节数组转换成的字符串进行比较，相同则返回true。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Z32D2btN1CXqUaSgia8RSJUicrmhNXFhLtgcTTaWCeCHPhraT6tFZYsJg0ADibuArWgs6YoiccFXqLE8FZPLNGuqt7couJSwU7wqQ/640?wx_fmt=png&from=appmsg)

然后查看类c的定义，类c中定义重载了两个方法a，两个参数的是刚才被调用的方法，在该方法里面通过类c中另一个单参数的方法a获取了一个字符串（对图片中获取的字符串进行了相应的转换），然后实例化了类a为aVar，然后aVar调用了自己的方法a，传入的是刚才转换后的字符串转换为的字节数组，然后再调用方法b。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Z2W9JQzlW8yN7VBN7ONhlB46SdrATWKbhvNsYXmLCHQicpGSfrjQqiaVTuQ7pfl0lcfFa45PutDb6FhDgFziaDNXZWHXOTEMjOJM/640?wx_fmt=png&from=appmsg)

查看类a的定义，可以看到里面是一个aes加密，使用ecb模式，密钥就是刚才从图片里面获取的字符串转换成的字节数组。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aiadKqta3BxjiadrPHuZv1HqgjqqKtfjeMsvvgiciaiadOIibPtnBDWumqpPvmmKh7t5Na3Lnwt7Kd4fFiacRws4qDZ6m12HTzbLycTU/640?wx_fmt=png&from=appmsg)

三、解题

通过上述分析，用户输入字符串后通过aes加密，加密后跟一个字节数组做比较，相同则成功。所以我们现在解题只需要把密钥找出来解密那个目标字节数组即可。

接下来使用frida进行hook，把类c的两个方法a给hook掉来获取密钥值，hook脚本如下：

```
Java.perform(function () {    console.log("===开始hook MainActivity===")    var c = Java.use("com.example.ring.myapplication.c")    var a = Java.use("com.example.ring.myapplication.a")    c.a.overload('java.lang.String', 'java.lang.String').implementation = function (str1, str2) {        console.log("c.a(str1, str2)被调用")        console.log("str1:", str1)        console.log("str2:", str2)        return this.a(str1, str2)    }    c.a.overload('java.lang.String').implementation = function (str) {        console.log("c.a(str)被调用")        console.log("str:", str)        var result = this.a(str)        console.log("key:", result)        return result    }    a.b.implementation = function (p) {        console.log("a.b(p)被调用")        console.log("p:", p)        var result = this.b(p)        console.log("crypt result:", result)        return result    }})
```

运行结果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Y2fkEW2anz6YCTBicAvibvVXic9N2JC5RkNsfYvtkMxS5RTRxENVyKoBTn1O42jOlmRiaNdwOnbpPdLHtYK6JfRIe6JoPP7H6dLSA/640?wx_fmt=png&from=appmsg)

可以看到密钥是htsii\_\_sht\_eek.y，然后打开cyberchef，使用aes解密目标字节数组（这里我把目标字节数组转换成了16进制形式）。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZfFK8E3k2l2fju0qhsibgSraxV6cZlYxTYUlZuc5Qk7Vx5HJ2fZx3iczUtODSJZgoAaV1slPCaaYialopjugd1q296aFppX0PPXU/640?wx_fmt=png&from=appmsg)

成功拿到flag。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ubxw8wJEYdluKbaN4LDwroa6C5W8flqTtNkiaZBpt9ibcVXJTlDmAHJHcR5TBR7AREPYETB3XUJF6v692P7GaD5A/0?wx_fmt=png)

SPEEDCoding

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ubxw8wJEYdluKbaN4LDwroa6C5W8flqTtNkiaZBpt9ibcVXJTlDmAHJHcR5TBR7AREPYETB3XUJF6v692P7GaD5A/0?wx_fmt=png)

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