---
title: 偶遇YAK插件，超级牛拼尽全力终于拿下
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247527317&idx=1&sn=34b9913df7230605c26607f44c9c5e63&chksm=c2d11731f5a69e27682d884b0af24d7cac79428da69e8c32a4dbc68df3c2995d15660157f620&scene=58&subscene=0#rd
source: Yak Project
date: 2024-12-27
fetch_date: 2025-10-06T19:38:12.686791
---

# 偶遇YAK插件，超级牛拼尽全力终于拿下

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcGMNTy5icbIpc0EZItnBHyDWnCCdmeNxckibH6p2TqPXY2r1fiaJj8Af27fAH10hLo6CWrC6ObTsY4w/0?wx_fmt=jpeg)

# 偶遇YAK插件，超级牛拼尽全力终于拿下

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

昨天圣诞节大家都过得怎么样？

中国牛不过洋节，对超级牛来说仍旧是努力工作的一天

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfKSzVS9S0n2WLJpSnTamawOaJlXqTWnZLBGJmhL9ELthy14JUR0DJvMIZOr3yrZDiao7YkeAuicQkA/640?wx_fmt=png&from=appmsg)

事已至此，先打开Yakit开始学习吧

经常有朋友在学习使用Yakit的时候发出这样的疑问：

“Yakit插件的原理是啥？”

“××插件能在Yakit里找到类似功能的插件吗？”

好说，那今天牛牛就带大家详细了解一下**YAK插件原理以及实用情况**

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudic6NWfMSJWFgz2JwxI10Z4Qoxs5YLH3oibnffYlSbojWtzPDMOvPh2ZA/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRo8RYe1aD8FPibxBDB8vfUIJk6h2PmpYqNqYpmzVAMtFkob3avLLOBIcg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoZgX97Bpja4iaDuBkWf4KxCHOkwZBy9iabocibCpgN1lJybBLzTRxBMRJw/640?wx_fmt=png&from=appmsg)

主动扫描和被动扫描，在字面上就已经有所区分。

主动指的是需要对目标地址进行特定的访问，比如在指纹识别的过程中，很多cms需要进行特定路径的访问或者ico hash的计算才能得出具体的指纹。

被动指的根据经过的request/response流量就可以完成对应的功能。比如：在指纹识别中，也有一部分cms就可以通过uri、header、body等就可以完成识别。

> 在yaklang官网--初探被动扫描 | Yak Program Language中也提到了，这里指的被动扫描更偏向于对流量识别和后续的处理。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRotOEtNEjJ3SVn0d71ItZnPicBNXO3Z5A0ibAXgXgSHiaiaPyPtzlRwgCYBw/640?wx_fmt=png&from=appmsg)

在MITM中间人劫持过程中，其实就类似于一个正向代理，简化架构如图，当进行流量发送的时候，请求通过MITM，MITM对请求进行劫持、丢弃等功能，然后将请求发送给Server，Server收到后进行响应，同样将响应发送给MITM，后经过MITM来转发给用户。在这个过程中,mitm就充当了一个中间人，拥有了对请求和响应的“操作权限”。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoiak4QmdR4EThnIVos3VKGIIREykqwIpUd7HusEt3KGq347RS4w2svHw/640?wx_fmt=png&from=appmsg)

在之前讲到的**热加载**功能中的对请求进行hook修改，对响应进行hook修改的疑问也就迎刃而解，都是通过MITM功能来进行的一系列衍生操作。

> 在上一篇文章中的热加载，就是通过在MITM中衍生使用 [渗透测试高级技巧（三）：被前端加密后的漏洞测试](https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247526919&idx=1&sn=0386721ba5a1ddad7d8d307ba4c159f5&scene=21#wechat_redirect) 中有讲到具体的使用案例。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoiaxDFlGaInicnjR4FZMNfo6HzRQORJtU22JZpmfibNV89L0uQx9aY7DFw/640?wx_fmt=png&from=appmsg)

通过熟悉了上面的MITM简单的运行原理之后，也就不难发现，MITM只是在中间充当了一个流量转发的媒介，那么也就可以推出，在before MITM和after MITM之后，也可以有多个**“正向代理”** 来将处理之后的流量转发到server上，同样，可以通过这些代理来转发到用户端，中间这些代理也可以像MITM一样去劫持或者转发流量。

> 在yak上把从MITM出去的代理，称为下游代理

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoeTLBvtoYEAoa9h5JnxYhzNthvVJTeqPL46jrOQDZywQDhyqAcG1n8w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoq0PRzFKxQDQ04wjpeTRIfoFMDcn7fiaLlYspbwh0JVrTPSKVAMJf7mw/640?wx_fmt=png&from=appmsg)

### **指定下游代理的方式**

在MITM中，启动的时候就可以指定下游代理。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRo2ictvJ1VVhKew0AevsGcV9WQ3iaDszawIJfQ78KWCnttj32FyOcfUWWw/640?wx_fmt=png&from=appmsg)

### **能做什么？**

在渗透过程中，常常会配合其他一些工具的使用或者将流量进行备份，以方便多种方式去验证漏洞是否存在，避免了在渗透中出现遗漏。在渗透测试中，可能会配置其他一些渗透测试软件，比如xray来进行联动等。其实原理就是将从MITM走过的流量转发到xray上。

> 流量转发在yaklang的教程使用中也有涉及。使用Yakit进行流量劫持 | Yak Official Website
>
> 同时，yak中也支持一些MITM插件的使用，比如：指纹探测、shiro爆破等

我们常常会关注指纹、敏感信息等信息，在bp中，常常使用的插件是hae，hae的原理也就和上面所讲到的被动扫描的原理是一致的，只要是依赖流量中数据来进行匹配。在yak mitm中也内置了敏感信息的识别、染色、tag标记。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoEZxjcsMSPJ9lfcFgqAcbSgNAyiaFgURU9DaRiadGib2vejJS5UyTO6NwA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRofDkkeicJducZNgaWUian3bzmgswybx6KSTurz6CibS90or1coy8tNaWMw/640?wx_fmt=png&from=appmsg)

```
{    "Rule": "(?i)((access|admin|api|debug|auth|authorization|gpg|ops|ray|deploy|s3|certificate|aws|app|application|docker|es|elastic|elasticsearch|secret)[-_]{0,5}(key|token|secret|secretkey|pass|password|sid|debug))|(secret|password)([\"']?\\s*:\\s*|\\s*=\\s*)",    "NoReplace": true,    "Color": "red",    "EnableForRequest": true,    "EnableForResponse": true,    "EnableForHeader": true,    "EnableForBody": true,    "Index": 3,    "ExtraTag": [        "敏感信息"    ]},
```

### **如何写一条指纹：**

首先需要去了解go中的正则，因为在规则中是可以去支持大小写敏感的。比如一条shiro的指纹，shiro的特点是在返回包中有**rememberMe=deleteMe**，而且必然是在返回包的Header头中，我们就可以写这样一条规则：

```
{    "Rule": "reMemberMe=deleteMe",    "NoReplace": true,    "Color": "red",    "EnableForRequest": false,    "EnableForResponse": true,    "EnableForHeader": true,    "ExtraTag": [        "shiro指纹"    ]}
```

我们可以在规则配置中进行规则的添加

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRor30TlMVhibtdWcn41htXuVeficQloJvc1nmUibKkmogXiakvjBodLwjVzQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoElFFKycXNTAYicP7dmFw3iaxseW0wbaEzK8SGBIOZrVB9m9wqoO0Pic4A/640?wx_fmt=png&from=appmsg)

#### **指纹优先级：**

当一个请求/响应，符合两个指纹的时候，因为流量是经过顺序来进行匹配的，所以会展示最后一条规则的颜色，但是在tag中是会将两个tag进行叠加展示，并且在展开的页面中会显示规则名的规则数据，比如，定义两条一样的shiro指纹。一条正则为**rememberMe=delete**，另一条为: **remeberMe**。结果如图：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoP8U2HyXNZVNZRQstDUDeU5npPXrCAvQrz5Ser6p11orRwsnZKe90WA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRo3LRibbYdH6JmoZiayjQkNBFEX4IdNZMkyflh8BesSoWyKtlEPViafusxQ/640?wx_fmt=png&from=appmsg)

在上面讲到的MITM简易原理的过程中，在MITM中可以对请求包和响应包进行hook和mirror从而实现各种各样的操作。MITM中也可以通过写MITM插件的方式来进行指纹的识别。例如，在官方插件--**被动指纹检测**中就是通过在MITM去镜像流量的方式来实现的内置指纹。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoAbAFAwAIUJUOILTrKPDOHw9TupjVxX2EV1ILibicp71yC9tPXY4foNhw/640?wx_fmt=png&from=appmsg)

在本质上来说，两种方式效率都差不多，都是通过插件执行的方式去进行内置，不同的是，MITM插件的方式需要去调用yakVm来去执行，而MITM内置指纹是通过go代码来进行执行。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoc5M2EGE1rp2xk9DJoCg7jH7zpOaS7T992twKtvSc4JTKEcmxMdav7A/640?wx_fmt=png&from=appmsg)

在很多CTF的题目中，都会遇到xff的伪造，xff的伪造也是比较暴力，由xff造成的漏洞也有很多，比如在代码中会出现登陆存库来使用xff。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoYGB7s15ibWLWVIlicJmetu9qrgjQGL2HSv0JRRZLgJGF4st7Pp6nmdzw/640?wx_fmt=png&from=appmsg)

由于HTTP协议是架在TCP协议上，而TCP协议又是一个端到端协议，在这样的一个协议中，通信双方就很容易的拿到双方的地址。

那么在有些网站中，会由于**CDN/负载均衡**的介入，就会发生变化。CDN本质上是为了让用户访问的时候提高速度，从而让连接转到离用户更近的服务器上，然后由CDN服务器进行缓存返回/转发。

> 可以将CDN理解成一个带缓存的正向代理

#### IP伪造的原理：

在IP伪造中，核心原理是利用通信双方需要一个中间媒介来进行真实IP的转发，而转发的内容又是所能控制的。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoUASANhvjicqtfjNLu1wOdTVeqVNbicXaSrRNicMMsWfgj73ZJOOicn5lPA/640?wx_fmt=png&from=appmsg)

在MITM中，内置了**HTTP 请求头伪造 IP****插件**，在流量经过时，对一个HTTP请求包来进行添加HTTP头，由于不同的CDN、不同的负载均衡添加的HTTP头也不完全相同，所以内置了常见的HTTP IP伪造头。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoF4l3TpACNBF4qKChUKt3WSLuZhAWXEOdNkhIBW0oCFduABLjUC9f8Q/640?wx_fmt=png&from=appmsg)

#### **"本地"模式：**

伪造"本地 "IP，在渗透中，有时候会遇到，注册/登陆会有一定的IP限制，比如限制某一片区域，或者某一段IP内，但是由于拿到的IP是经过伪造后的IP，所以就可能存在绕过的情况。

这里进入IP伪造靶场：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoQZ7nS8YUL4icOaJqvAuduo2gnHt037tbTN3qWicVw7H3zdcq4u46rCdA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoujMcQQv9pYcPJSxBqWUDmbQFJNMpqG2fBqHycAQ9V8icGCsiccsYuAZw/640?wx_fmt=png&from=appmsg)

在这里，只要是本地IP就可以随机登陆（后端没有限制用户名和密码），在这里我们选择使用MITM中的伪造IP插件，伪造IP为127.0.0.1，用户名和密码随机。

即可成功登陆。

#### **"随机"模式：**

随机模式指的是，在渗透中，有时会遇到密码爆破的情况，而密码爆破次数的限制会有多种情况。

* 根据用户名来进行限制，在一段时间内允许登陆N次
* 根据IP地址来进行限制，在某一段IP范围内允许登陆N次

在这里，我们选择使用IP伪造中的爆破，这里后端的逻辑为，一个IP随机爆破5次即用户被锁定。这里我们发送到webfuzzer中，我们选择使用热加载。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoxTH16IgsibceAicEkCczWb5qoeibDnssqGLobexUiagG2wWWG1B7KhKE9A/640?wx_fmt=png&from=appmsg)

然后选定fuzztag即可爆破

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZezbaoErQILQPmXXN8iaOFRoQJJmLRbaFzjib5ufRYCiaWynQ5wEKQma5c9qnZNF65lO0o30s6c9sHwQ/640?wx_fmt=png&from=appmsg)

**END**

**it使用小tips**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://gi...