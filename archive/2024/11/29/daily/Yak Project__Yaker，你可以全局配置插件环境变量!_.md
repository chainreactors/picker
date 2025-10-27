---
title: "Yaker，你可以全局配置插件环境变量!"
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247525652&idx=1&sn=91301a8c65604e8229d69f54ed2707bd&chksm=c2d119b0f5a690a6f4f2f38c8097f47fc72c8a3e4ae8a5be3c813e3df1d0d7f434aeacc108d2&scene=58&subscene=0#rd
source: Yak Project
date: 2024-11-29
fetch_date: 2025-10-06T19:18:08.853772
---

# "Yaker，你可以全局配置插件环境变量!"

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgP1vYqoZkEEzmUNn9oibRvPTJMBSSAHyTBYZVYys6QIqXgYBaiaIpu5lFA/0?wx_fmt=jpeg)

# "Yaker，你可以全局配置插件环境变量!"

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

周四周四，Vme50(bushi

大家好，这里是疯狂超级牛（功能上新版）

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdVlNpr7MiamEXUb761Zc1zTbd02ewBFAticJWcPRXicdkyUUY7rfbgk969qhgHGQRr0030AUMxeOF4A/640?wx_fmt=png&from=appmsg)

经常有用户问

“牛牛如何为不同插件配置相同的变量值呢？”

“能有一个一波搞定插件变量的方式就好了”

超级牛听到了广大用户的声音，默默地拿起了鞭子，走向开发团队...

于是！**插件全局变量配置功能**，上新！

那么如何具体使用此功能来配置插件的环境变量呢？

请看VCR⬇️

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgPxhq9ZDnzI4ge0SwCTAMbAvAI5yWUnoBLqzicqmJAtuUiaygZO5lqSGJQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdVlNpr7MiamEXUb761Zc1zT9j72eWfhEWEw53U7hILWy0hF7MtRjibVLZRo040MIOWVrRUeeAhpwbQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgPUYIPgCQZU3ltmg4SEZXBTyGI6tTCEdicYiaicgK40Y9SI6f8aib55I8qiag/640?wx_fmt=png&from=appmsg)

我们的设计中，使用cli的选项作为环境变量的获取接口。一个简单的例子如下

```
// setPluginEnv 是一个选项函数，设置参数从插件环境中取值key = cli.String("key", cli.setPluginEnv("api-key"))
```

获取插件环境变量和使用普通cli参数基本一致，只需要在选项里设置 cli.setPluginEnv("api-key")即可，其中传入的是环境变量的key值。

需要说明的是一旦设置这个选项，Yakit将不再提供输入，其数据必定来自于插件环境变量。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZe3GqQXluPcDicPMANsW4mUbsDxECo3qOSAhnibAHHb1b4IqxPEqSUNvSNwm4dM5scbECZ7Q9uGAXmw/640?wx_fmt=png&from=appmsg)

可以看到上述demo中为cli参数 env设置 setPluginEnv之后，参数预览处就没有对应的输入框了。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgPqV2LQ3AXsgzibM3bEXpIHl3IL1kwEPiah0rfqMibNNAtjaPnibNyucGJFg/640?wx_fmt=png&from=appmsg)

#

插件环境变量可以在两处配置 插件商店页面的配置页 和 单个插件的配置页

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZe3GqQXluPcDicPMANsW4mUbdJT8SFPF2HBYETapqPNRU5c12Wxhj3PB5TNRGtRncqY9B2XWQLUmdQ/640?wx_fmt=png&from=appmsg)

这两处的配置有一些细节的不同。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgP2ec6St5eGJrnEaRickaBtrCO2BkVY6EwjjUxOKXW5RVicBKp5zW3lVEw/640?wx_fmt=png&from=appmsg)

##

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZe3GqQXluPcDicPMANsW4mUbicdszmu5g5opiamrJQfKY5NatKt9bnntdFc5sFia4nWibMdR4ibp0sQ5s6g/640?wx_fmt=png&from=appmsg)

这里的配置页面拥有完整的对环境变量的增删改查能力。可以新建环境变量，即使没有插件使用。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZe3GqQXluPcDicPMANsW4mUbQI9Z2eHm5YtmBL5V791aJK7Q18GmlP8wcWygcmKoKonJ5lP28ooQ7w/640?wx_fmt=png&from=appmsg)

需要说明的是变量是**可以支持空值**的，**这与没有环境变量并不等价。**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgPpdWB1dF0oorzbTlAvBxLbbOUI99qy4R6eheib9VNEzBrRRaAZ79dgmQ/640?wx_fmt=png&from=appmsg)

##

这部分的配置是为了方便使用做出的针对单个插件的简单版配置

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZe3GqQXluPcDicPMANsW4mUbdKWxsyvic98z7VeZh7icw0e1wdHozpuJgBF7f03Rxwttx1Qkuibjo1uQA/640?wx_fmt=png&from=appmsg)

它只对本插件代码中使用的环境变量进行了展示，只提供对应的修改功能。

这里是对代码进行了解析处理，如果有代码中需要使用的环境变量没有被配置的话，会在此处提示用户。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZe3GqQXluPcDicPMANsW4mUbymx45SECibaDHa4YWhcqsnWRzb5JBPaHc53gCibcWlbTEshuDsqjVZxg/640?wx_fmt=png&from=appmsg)

点击配置即可在此处快捷配置环境变量

> 需要注意的时候环境变量的影响范围是全局，这里修改之后，所有的使用对应环境变量的地方都会受到影响。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgPia3cvs8u6WweLI1AcvLG77ic97d0Qic8to5xqsXqVkN8OfvIpk1WibfRCQ/640?wx_fmt=png&from=appmsg)

#

有了插件环境变量之后，一些情况可以有更好的解决方案。比如为简单改动插件 就可以为其添加特定的校验头。

这里使用简单的内置插件——HTTP请求走私为例

```
buildSmugglePacket = (host, newPacket) => {...}
mirrorNewWebsite = func(isHttps /*bool*/, url /*string*/, req /*[]byte*/, rsp /*[]byte*/, body /*[]byte*/) {    ...    payload = buildSmugglePacket(host, req)    println(payload)    ...    rsp, _ = poc.HTTPEx(payload, poc.https(isHttps), poc.noFixContentLength(true))~    ...}
```

假设现在进行渗透测试的一批目标中，分别添加特定的头 TestHeader，不同的测试目标的校验值不一样。

那么这个时候就可以通过环境变量进行一次通用改造。

```
header = cli.String("header",cli.setPluginEnv("testheader"))cli.check()
buildSmugglePacket = (host, newPacket) => {...}
mirrorNewWebsite = func(isHttps /*bool*/, url /*string*/, req /*[]byte*/, rsp /*[]byte*/, body /*[]byte*/) {    ...    payload = buildSmugglePacket(host, req)    println(payload)    ...    originResponse, req = poc.HTTP(standardPacket.Replace("REPLACEME_HOST", host), poc.https(isHttps),poc.replaceHeader("TestHeader", header))~    ...}
```

改造之后此参数会在插件发送测试数据包的时候添加特定的请求头值，如需改动请求头值只需，修改环境变量配置即可，无需再改代码。

修改完毕在配置页面可以看到有未配置的变量

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZe3GqQXluPcDicPMANsW4mUbzbZUviayQ4AznjENTZgPyNwONwrWFib1XsySn9wRyMpArwMtAMxGVo0w/640?wx_fmt=png&from=appmsg)

点击配置设置好环境变量之后执行插件，可以看到成功地进行请求头插入

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZe3GqQXluPcDicPMANsW4mUbErvH4OibU9sGiaFWhVPCHHyBquS5OV4G7ibvNic3I1EZibE5hgMX98kuBQA/640?wx_fmt=png&from=appmsg)

如果需要更换测试目标，只需要在配置页面替换即可。

当然，这只是一个例子用来帮助社区用户快速了解插件环境变量的用途。

实际工作中可以改造热加载插件，使用hijack系列的hook，达到”一处修改，全局生效“的效果，用户可以自行探索。

**END**

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