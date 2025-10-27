---
title: 第103篇：对一个加密混淆的java内存马的反混淆实战分析
url: https://mp.weixin.qq.com/s?__biz=MzkzMjI1NjI3Ng==&mid=2247486969&idx=1&sn=cd7f4a8ab3eb0aa2daba5cf312cf21db&chksm=c25fc282f5284b94d4bd23a0e7d717f60bc91f950b86e8143115d16021bf94919da0ca42dcb0&scene=58&subscene=0#rd
source: 希潭实验室
date: 2024-09-04
fetch_date: 2025-10-06T18:29:13.432966
---

# 第103篇：对一个加密混淆的java内存马的反混淆实战分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450CsSStZcOeGYlRQhrY2wOJr7lmic3KyDgib4tM56PicP0ZuibvbexaJzs62NDJUZAvxkegCzcIqbKxjZQ/0?wx_fmt=jpeg)

# 第103篇：对一个加密混淆的java内存马的反混淆实战分析

原创

abc123info

希潭实验室

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcCCMJ6Af2WYicgMPA32IwibF8mI2ibC9h8jaHkhxnZzZuqctMLRTxDudicA/640?wx_fmt=png)

##

## **Part1 前言**

**大家好，我是ABC\_123**。在前几周的攻防演习比赛过程中，收到了几个网友发来的Webshell文件或者内存马class文件，让我帮忙分析一下，这两天正好抽时间研究一下。在最近几年，很多红队人员早已对内存马部分代码进行层层加密及深度的加密混淆，推测是为了绕过RASP的防护。

**注：**为了防止泄露敏感信息，ABC\_123将以下截图中的关键类名、关键字、特征都进行了重命名或者模糊化处理。

## **Part2 技术研究过程**

从流量中抓取并还原出java攻击代码大致如下：通过Base64Utils可知，那一长串字符推测为base64加密，然后AESUtils是第2层解密算法。其中，AESUtils的具体实现代码我们不知道，但由于该方法只传了一个key值，可以大致推测出解密算法的具体实现。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJrwsgOnd1DJANrPxevga7j0ArXHfzAAR6jXh3AEt4TmdQ3NoOGWSRvLg/640?wx_fmt=png&from=appmsg)

如下图所示，手工编写一个AES解密方法，将上述代码中的base64密文经过AES算法解密，成功得到一个正常的序列化文件a666.ser，说明我们的解密方法写的是正确的。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJr6bsvsQuMbHvU22sSkib4YkmVycSGic3dUAb9NwBlA9Vic0bibaiav3ibP63A/640?wx_fmt=png&from=appmsg)

接下来将a666.ser文件直接以文本格式打开，先大致看一下具体内容，其中一长串字符串很容易联想到是base64加密。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJrKibMHD3waNX3BT5oGTgKGQlkn3QMW5RTDw9z2oC0oicKV6r3uZBjoHgw/640?wx_fmt=png&from=appmsg)

将上述加密字符串复制出来，使用base64解密之后发现是一堆乱码，一时间不知道错在哪里。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJr4IOaicVxLBJc4sOGicMwe6Ox2FabibejWXbWz6VW3SLErjiaLfl5LVBnaw/640?wx_fmt=png&from=appmsg)

后续以16进制重新打开a666.ser这个序列化文件仔细查看，发现在v66vg前面其实还有一个可见字符y，16进制的79对应的就是小写字母y。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJrS0WsuJod5ChoxibZnGYhHTHaSO9iaicUsJAib0M35xlh4y1hibqktUk9Oxg/640?wx_fmt=png&from=appmsg)

将字母y添加到刚才我们复制出来的加密字符的前面，以**yv66vg**开头，然后重新base64解码生成如下结果，推测应该是一个class文件。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJree4txyYiaYVicGP57KmAgoxsWYibUwZ3TpAGImj9nmef1MUPhXgvJib2iag/640?wx_fmt=png&from=appmsg)

接下来对class文件进行反编译，发现这个class文件进行了深度的加密混淆，首先看一下static静态初始代码块，结果发现全部代码都是加密混淆的，基本上是无法辨认的。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJrIFRGHVAOVs17Ic3H2icxE5YnNpz8DLrZpK7wuadCZ62HRkMQ2eD97og/640?wx_fmt=png&from=appmsg)

不着急，我们继续看这个加密混淆class文件其它方法的实现，看一下doFilter部分，大致可以看出来是一个filter型内存马。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJriarA5FpZCFPvJ5DQcTPiaKnUfniaHOZHLWhGdBYDA9hAwgBpqCsx3PTvg/640?wx_fmt=png&from=appmsg)

接下来看 **b(byte[] var1)** 这个方法，大体看了一下，推测其可能是一个解密函数，于是重点对这个方法进行反混淆。手工通过IDE依据自己对代码的理解，挨个对类名、方法名、变量名进行重命名。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJrsgiarzicP8zmOKV9QiaZOAhWsYONrrg67w65SaJBqlAM2Xh2kCz808QYA/640?wx_fmt=png&from=appmsg)

经过一系列重命名，上述加密混淆的代码改成了如下形式：很明显，如果想看到具体的代码实现，对于类似于 **a(14933, -7719)**方法的解密是重中之重。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJrVVVnBiafKGCRcvfz4Bp5YKGE7ibZjy8ZciciacJgMVfHRzMnbo0T9qf27Q/640?wx_fmt=png&from=appmsg)

接下来需要我们自己编写java代码实现解密功能，将原有的static静态代码块改造为一个 **static111**方法，放到java代码的最前面执行（这里因为经过测试，static方法里面对c和d这两个变量进行了一系列赋值，所以是必须的添加的），然后把a方法的代码也复制进去，最终输出a方法结果，发现结果是“**java.util.Base64**”。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJrjum75viarwfkILwqYr1dlicNRAeDgJicQicQ3DYX5OZcyt1va9kdOduDicg/640?wx_fmt=png&from=appmsg)

然后将原有java代码的a方法的所有值进行替换，最终将decrypt（原有的方法名叫b）这个方法的代码，完全解混淆成功，如下图示：

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJrhlMicMnTIyQLRgayXRMjVhPFV2C8Wmz71wzzrKkaV1msfVCicupjcAMQ/640?wx_fmt=png&from=appmsg)

使用同样的方法对doFilter内存马部分的代码进行反混淆，变成如下形式。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsSStZcOeGYlRQhrY2wOJrwM85ibq8COH1HZ4vH93myNLdAIEpXD5HiawSsykhVXaNiczZibrzicfDPkA/640?wx_fmt=png&from=appmsg)

解混淆之后，发现hashMap对象传递了session、request、response三个对象，很明显是冰鞋内存马的特征，也可以推测该内存马是经过改造加密流量的冰蝎内存马。此外，当User-Agent设置为Mozilla/5.0 (Macintosh; Intel Windows NT\*\*\*\*\*\*\*\*\*\*\*\*时，会走冰蝎Filter型内存马，因此这个user-agent就是流量的特征。通过流量设备筛选含有该特征的流量，即可得知攻击者具体做了哪些操作。至此，对于该内存马的分析工作就完成了。

## **Part3 总结**

**1.**  很多红队制作内存马已经开始进行java代码混淆，而且越来越复杂，推测是为了绕过RASP。

**2.**  下一篇我会继续介绍一个更加复杂的内存马解密。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**公众号专注于网络安全技术，包括安全咨询、APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**(replace # with @)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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