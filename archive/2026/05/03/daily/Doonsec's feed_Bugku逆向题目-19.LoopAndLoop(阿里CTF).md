---
title: Bugku逆向题目-19.LoopAndLoop(阿里CTF)
url: https://mp.weixin.qq.com/s/ocYbyzytcKQgsxttjvF2lA
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:26:17.240951
---

# Bugku逆向题目-19.LoopAndLoop(阿里CTF)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6nhGiavBDP4ZTBn3GJ7qicu5DEEmVGwg0r2kUBEZp6z5QSjNNb1OtNq0dUNHmxoicFQsAjGB4gkgo1HH12clXDdOE3ehdP4gfmaGqdxdeHCSgM/0?wx_fmt=jpeg)

# Bugku逆向题目-19.LoopAndLoop(阿里CTF)

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

题目链接：https://ctf.bugku.com/challenges/detail/id/120.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4bmOfyZdNzx2Cd2YCIols9pdH6zj0C2icDtadN21FiceR9snUhUZwYcUFxfWOAQvkVOkUGNKibDhYwsHNNyGuasGP4mwMEqiaWcMHI/640?wx_fmt=png&from=appmsg)

一、题目分析

下载下来题目是一个apk文件，拖入模拟器中运行，提示需要输入正确的数字才可以出来flag。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YD3ziaibgMpmU3fj20LfXiaEoWzxQYtMlho3KibiaFXpua9ZRlwfDSQOqRoGAfkUErhicKfwbyT9RZzhTzoccXiaC5QVibMyuuticzF0Zo/640?wx_fmt=png&from=appmsg)

将APK文件拖入jadx中静态分析，发现源码中首先将输入的字符串转换为数字，然后作为check方法的参数传入，最后的结果等于1835996258时才能输出正确的flag值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZTLgOnIoEDK0kh194mpnz05PeCDFngibks33WPn1y9Yzd7eE6no1KArqH3t8emA0fzA1iaH46dKzeGPgHSzU2fOl4CBQtGianGZU/640?wx_fmt=png&from=appmsg)

这里发现check方法调用了native方法chec，chec方法来自于liblhm.so文件，将该文件拖入ghidra中查看具体方法实现情况，分析后可以知道这个方法是对check方法的第二个参数（也就是99）逐次减1，然后依次调用check1方法、check2方法、check3方法循环，最后获得计算结果数字。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YGibxBGOt7U1ZP2xF6HdErcFfSMlkxgYHbvTEOh2UO0UkKsjicSWVxQpIJq0U9iawria9Ckfqxqdso6cWzV9njwZWAPBaKVmpeSf8/640?wx_fmt=png&from=appmsg)

接下来分析这三个方法，首先是check1方法，这个方法会把input进行加法运算，本质上是加一个固定数字（从1加到99）。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Zcd6s7AN2O5thmyWg08zzlSibkT5upSqSsQVadQOvltMbwUhiaCykTRXsEDSHRJLkCZOGbJh3VkLsGBibibzuRwqNGsrwpWzk5axw/640?wx_fmt=png&from=appmsg)

然后是check2方法，这个方法判断s（也就是之前check方法里面循环减1的第二个参数）是否是偶数，偶数的话就加一个固定数字（从1加到999），奇数的话就减一个固定数字（从1加到999）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YvcO2ibiaibcpEuZ75h3W26Kpz6HZqCFXFcQp2egXqE9Jj3BaD0M0ZC2V78DZImKjlx4ibmGVyd0StrT6lIhZR5bfdGVr7MEbwn5c/640?wx_fmt=png&from=appmsg)

最后是check3方法，这个方法也是对input参数加一个固定数字（从1加到9999）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4b4DnGUWelPdQ4axqD9b9PKQA4nu1SpX7iazMHJFwXjJRxjZoPwTJeOhZMsOgIrC5GGicPYDR62N1NogicE7aKetkx03dCPC9fP3c/640?wx_fmt=png&from=appmsg)

综合以上三个方法的本质，都是加一个固定数字或者减一个固定数字，并且初始循环参数是固定值99，所以最后得到的结果是用户输入的数字加了一个固定的数字（这个数字不管输入多少都是固定的），判断该结果是否等于1835996258，那么我们只要获取到这个固定数字然后拿1835996258减去即可。

二、解题

首先需要获得这个固定的数字，这里使用frida来hook掉check方法，随便输入一个数字然后打印输出值，再打印减去用户输入数字的结果就可以得到这个固定数字（可以多试几个数字验证一下，确实是不管输入多少，都是同一个固定数字），frida的hook脚本如下：

```
Java.perform(function () {    console.log("===开始hook MainActivity===")    var mainActivity = Java.use("net.bluelotus.tomorrow.easyandroid.MainActivity")    //hook check方法    mainActivity.check.implementation = function (input, s) {        console.log("===check方法被调用===")        console.log("input:", input)        console.log("s:", s)        var result = this.check(input, s)        console.log("固定数字为:", result - input)        return result    }})
```

执行结果如图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4baIarDwCTp8qdRpUk9jA9icvWBZ7DFjx0DMicgY4ZyFZzvdDTMlstXIghAdQc3LpxiaeDqVYX76peygme6wiaicXMWjYbRTaabrZXc/640?wx_fmt=png&from=appmsg)

可以看到输入合适大小的数字时都是固定的数字1599503850，这里还有一个溢出漏洞，当数字过大溢出时，固定数字会发生改变。

然后用结果数字1835996258减去1599503850即236492408就是用户的正确输入了，我们把这个数字输入app中验证，成功获得flag。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YrtQgQ3fscgdG3wZhm6czwgqQHHficPoDLMGazoWApBKz46hjGXKibZWe595YXSrHfPz1dOONSsfD1SGGnkWibRnWteiaMFOYNicOM/640?wx_fmt=png&from=appmsg)

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