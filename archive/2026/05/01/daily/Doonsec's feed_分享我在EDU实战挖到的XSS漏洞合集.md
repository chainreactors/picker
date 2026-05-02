---
title: 分享我在EDU实战挖到的XSS漏洞合集
url: https://mp.weixin.qq.com/s/MoPAhcJOkZ7pt7_mvmq__Q
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:58:59.865163
---

# 分享我在EDU实战挖到的XSS漏洞合集

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/F4N4AId99Xc95FbBtiaoTazLibwmot68NzXOK6hqPibtM4BU3dfXjyjhqBJhLaCaIMboj9ppvj4BeG0PeVsVibSudhe3eCVsO3qkMdr9SZR2oCU/0?wx_fmt=jpeg)

# 分享我在EDU实战挖到的XSS漏洞合集

原创

小帅安全
小帅安全

小帅安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责申明**

```
本公众号“小帅安全”旨在分享网络安全领域的相关知识，仅限于学习和研究之用。本公众号并不鼓励或支持任何非法活动。本公众号中提供的所有内容都是基于作者的经验和知识，并仅代表作者个人的观点和意见。这些观点和意见仅供参考，不构成任何形式的承诺或保证。本公众号不对任何人因使用或依赖本公众号提供的信息、工具或技术所造成的任何损失或伤害负责。本公众号提供的技术和工具仅限于学习和研究之用，不得用于非法活动。任何非法活动均与本公众号的立场和政策相违背，并将依法承担法律责任。本公众号不对使用本公众号提供的工具和技术所造成的任何直接或间接损失负责。使用者必须自行承担使用风险，同时对自己的行为负全部责任。本公众号保留随时修改或补充免责声明的权利，而不需事先通知。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xf2wibr0HBDdCyUKwjT9Z3dibaDKmVFGBEIw2OsfyK5n9aSbwr2YicOEwSNaXziaBiat4pZVp9czEkqbvZrBZSgtG6Dd1froYPbhWmw/640?wx_fmt=png&from=appmsg)

**点击蓝字 关注我们**

大家在挖漏洞的时候，不必要盯着高危漏洞不放。刚开始的时候可以挖一些低危/中危的漏洞，能够增强自己的信心。

下面给大家分享我在EDU实战挖到的XSS漏洞合集。

**案例1-反射XSS**

EDU不收反射XSS，我之前在哪里看到可以交到360，一个给了5快

后面我就把反射XSS全交到360，发现职校，学院这些单位的只有积分，至于给钱的需要是985、211高校等单位。

第一个：

404 not found

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XetDlSPyrqaaGs7kO3mT6Yy0QwUAzGjSUHZuaruHRNJicKfVCgAZSdjsf7n7CS4DLPyRaTxHS57GaL4mZotzLWcq16uqKd83JNM/640?wx_fmt=png&from=appmsg)

大家有时候拼接一些api，当api不存在的时候会被跳转到404页面。

比如上面这个，会跳转到SYSHome/Error?ErrMsg=

ErrMsg参数可控

http://xxx.xxx/SYSHome/Error?ErrMsg=%3Cstyle/onload=alert(URL)%3E

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XcJIE9HB1ma8ThwYfODic3S6y6ItCYXpoV1F8XJiclDaamk333OaA2PRk4ESGic3j8heAfyByibvpcw5wOa8icSM2eZTzaGT19n8AUo/640?wx_fmt=png&from=appmsg)

第二个

No such file or directory

下载文件的时候将文件名修改为一个不存在的名字，同时页面又将完整的文件名打印了出来，这个时候的文件名就是我们可以控制的了。

请看案例：

点击download下载按钮，正常它会把这个文件下载下来，然后关闭网页

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xcb348yuicMHe4qW5DOaicOkibgy3rTfNZMibkacuydaWEiceIrURjxkyU9WQM9aBonVnGkp2Utb1MGBTrCtDUl9ykIGAudQLXgB4yU/640?wx_fmt=png&from=appmsg)

这里我们鼠标放在download按钮上面复制链接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xdoqwq4bERwHhL0VGLscqbCxl3z4wvInk6cVmBeRTSdmuH6icPSicdQSg1FPM5YsGNxibAurndmOM2hxeEXEPJ8viaQ62b7jKkFkzw/640?wx_fmt=png&from=appmsg)

修改filename参数为一个不存在的文件名，这样就不会下载文件关掉页面，且文件名是我们可控的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XcAScXDicFvD8lm8aZDcH7B4U02rzqP5XKDQphD7FFGZdFuCicQ2icBPdXEUWODwTHavAgaPjWSnf7q6QR5FYlZyVyn0e711hnibHA/640?wx_fmt=png&from=appmsg)

在我写这篇文章的时候已经修复了，我之前的payload是：

/downloadfile.jsp?filemenu=\_xx&filename=</body><script>alert('XSS')</script>

再次尝试发现被拦了

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99Xfia5MviceygSxcDDicvMv5A7xkJh6lNrAtmQS4qDsQAibo1MY7TNc2AZ5iaAJlSDIQ9leLDBibPmfXM7aIez0mlU6v2bzBSW8USia658/640?wx_fmt=png&from=appmsg)

那么我看看是不是真的修了

任意插入一个payload:</tExtArEa><h1>123</h1>#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xf0BLtbzxES9mLvicSvibVuoWKicxWcvANGXMgpm2BqVibkELVR0USX7kPGiapoo5UyKicBXELxJyZWia3CU4cMYiaqBqP4ibE85oovQ7pM/640?wx_fmt=png&from=appmsg)

可以解析，那么试一下其他的标签

botton标签试一下

```
<button type="button" onclick="alert('Hello World!')">Click Me!</button>
```

出现了clike me

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xf0oCCODmExxSryOXicWHKDmpRTLvYNwJPEvYTpwOGT4za7jibMic8Sm9aiaOTRT6I798GRERL6W40fby4GSiadhQmhibznZCesxINow/640?wx_fmt=png&from=appmsg)

那么点击，成功触发

```
/downloadfile.jsp?filemenu=_xxx&filename=<button type="button" onclick="alert('Hello World!')">Click Me!</button>
```

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XdiaDtRfNU3sgYo5hdtW9yzyntYKBVe1JCTBicNeBmwp5y34vBI5tbj68ct0e5AhK1lymQ2pdfy4zhCiccvGucCbuUsf1sXEmcyZ0/640?wx_fmt=png&from=appmsg)

第三个

当点击页面某个功能点，被提示没有这个用户，也就是权限不够，跳转到user notfound，

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XdBKCAyViaC9VBsr32mr7Pz6peW62AgFH24LJlKKoBMbVbVl2LPvtr7kbYs1z86kLNxQGyrmEjicFqtlY3v3DkAia6rjibdCqLdbCU/640?wx_fmt=png&from=appmsg)

修改msg参数的值为</tExtArEa><script>alert('XSS')</script>#，访问下面的地址

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XfNmHGucIibTG3hl9JJxqsVmdArjuQHXO75VFTwWdviaa2lKqnm65JsALvoU1sE63BKuz1RpZhVxrRmBcRVpjbunq3G8Nq2oPDqo/640?wx_fmt=png&from=appmsg)

第四个

有些网站会记录你的请求头并打印在页面上面，比如X-Forwarded-For

这个网站访问的时候，会自动获取访问用户的IP并打印在页面上。

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XfBhEExFDaUT2C9lx8UUc5rdBnL2QicgVepypBytJ5x3Kh0sX7t5tibwC4G7yyLYa2uMvkTRDeOSNG7sUUI4pzlArbBsicdVUbib1Y/640?wx_fmt=png&from=appmsg)

抓包发现是由两个header头获取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XciaaoryibxsOianocZnibD3LOlYu079KHe8ia8RJ6XT1oicjfIrEykRMy1FYzEBibajvJCAUaNVR9G6jAUGwpDzDpYKHUx82XTpAKJVQ/640?wx_fmt=png&from=appmsg)

在请求的数据包加入payload

X-Forwarded-For: <script>alert('XSS')</script>

X-Real-IP: <script>alert('XSS')</script>

可以看到其中一个字段被控制了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xe4Z9VCOlZRREvDQSuXic82xibXiciazPwQjseGiaeicianicwHkcg8D66vHr35Tsia70cZicg1cchRs943LJGdTFAq5sTnu7sAWu3xDQQfs/640?wx_fmt=png&from=appmsg)

然后

右键-show-response-in-broswser

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xfm3uhU4VBrmV11FdAcjtD1HvIwcqFPQ0AhsBDptcH4LKFxVJWicy0UZUVia28OQMaZibiayzyusz2ib7nnr0uXpojfckgNesrLrnso/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XdqCZ5lldYaxNdZCB79uvxFBibMuCNqzdEibkD5uDwib4fBwicGJB6jKjOic1fbs8calEjibtraibOqic17PJr6gt2Cu4OibIgY3toEVQIQ/640?wx_fmt=png&from=appmsg)

X-Forwarded-For字段被伪造，造成了XSS

这个也是给了5快

**案例2-存储XSS**

上传文件造成的XSS，可以上传svg、xml、html、htm

第一个：

维修、报修上传图片处，没有过滤svg后缀

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99Xcjiccrwl9fVR3Q6hu1vHnCKqdPebuDmrialscGsONUYxqk1kVx7EAvPxNoNOdImxcBe92Sw3adGNhCrvziaFN60nFfBFV5ytHdib4/640?wx_fmt=png&from=appmsg)

```
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">   <circle cx="100" cy="50" r="40" stroke="black" stroke-width="2" fill="red" />   <script>alert('svg')</script></svg>
```

右键打开图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XfV56nmg9MF96d3k13fCP2Lju8henzKgJrtgtmylib3I87bnewWMILkGTwVKpibzoDAgWGWabp6E29c2vHTBnLtZ2Cg4HF6jjlWo/640?wx_fmt=png&from=appmsg)

第二个：

这是在一个群聊里面

首先使用自己的账号创建一个群组

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xd6FZGEDoxcnA8bZeiabFny1m3pzMXnnrCicgMriczR4YB6DKfaZpVSus1C41fUn4hAEf7Cu4knMmXOcZiaRCA6n6Vrepxia7kMciaG8/640?wx_fmt=png&from=appmsg)

在群组里面发送了一个xml文件，在burpsuite里面得到文件地址

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XcLUMe2YrDJwnFhxoDQg1QdnSYTJv3FtknO2j81ujAQ87osWlaJ0iaM6tp5q6v5XNBX3jXxibCGDY8NUEj7KMLDuHhFReClmfsX0/640?wx_fmt=png&from=appmsg)

访问这个xml

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XeDnrIFu8xzpwBg4ibAzwou3GGKKCNmkPWg4iaVf96pib038VArfng7u5N9km0iaZUtGYziahomY4TaN6eOluGJlwKPn8KiabkHib6R6k/640?wx_fmt=png&from=appmsg)

在群组里面直接发送html、htm、svg文件会一直发送不出去

burp一直没有响应

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XdmyN6utgOzuH6aTFbEaia8eNQricgNk5ZRCrdfohGlLicibD9rEjcv0nbeUBXqzUPbHFR153fTKo6x1klnyUiaWYGKZYIDRjZLK6BU/640?wx_fmt=png&from=appmsg)

修改filename参数为1.1成功上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XfKZVdQMdzib0FuzsMJoeZQpibeQ6nroGO0ib0MWPiaxeZNDiaicAicDF3DIJHMc6MBeibibmzl0AibxyD8r5tnOOiczjXZGkewL1PQH8yYMI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XerYTq2LsvibszsLqicHTYQ0I8V3cNl5JPvopZOyDgjl7G47ic3XfUQJAgA1VTqMmLic8RpsB6icugoACXwd2J6pw3hpnZRicGECwFGY/640?wx_fmt=png&from=appmsg)

同理也可以上传svg文件，修改fileName参数值为1.1，成功上传。

这里为什么这么改，我也不知道，随便乱试一试，结果上传成功了。

文章中提及漏洞已提交漏洞平台并已修复，请勿恶意复现

获取更多工具和实战技巧

关注 小帅安全

**往期推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XeqrffLgRnnnh9ImV3J4pZWGrKIIFXia91nm5ibNynsoJHBgxiaGlgPWk2uXDJRZQDicVH2icjHo2rCIQ2DN7raadjIEd1DIM2slicGM/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483962&idx=1&sn=ea2a00b7fa821b99422e4d893ff43cab&scene=21#wechat_redirect)

用户名/昵称内容注入漏洞

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XcPAHeE5c9M5ZC1tUJ61B8W4HrbfCh3nRmfPJKNPicLbaABsbCbJKFI3n9GeDp89ap3a4wiamLnuSibzLXxU9aQcvYdC7NqOsVkQU/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483947&idx=1&sn=5968556dc7169ee862c3842981a3a198&scene=21#wechat_redirect)

最近捡漏的一个验证码相关的实战案例分享

[![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99Xd7kwlLwpEbUGYjxibDp2xxTrOuEZQSnenPiaBSd4olCXOGlAxfFXCq1V2nnN7o3KX2akAQ4qqUhrpA5Jib4hwvzImf3gWS6WzPCI/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483882&idx=1&sn=c3203a266955b29770706abc9...