---
title: 【地图大师的代码审计之路 第二篇】从代码层看懂越权与未授权漏洞为何如此高发
url: https://mp.weixin.qq.com/s/mdK_IcZ5LHMz6vzd_zQeiA
source: Doonsec's feed
date: 2026-09-29
fetch_date: 2026-09-30T07:40:56.996073
---

# 【地图大师的代码审计之路 第二篇】从代码层看懂越权与未授权漏洞为何如此高发

# 【地图大师的代码审计之路 第二篇】从代码层看懂越权与未授权漏洞为何如此高发

原创

地图大师挖漏洞
地图大师挖漏洞

地图大师的漏洞追踪指南

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 地图大师的代码审计之路

### 一、概述

大家好，我是地图大师。在 SRC 挖洞或者渗透测试的过程中，**越权和未授权一直都是非常容易出货的两类漏洞**。

在黑盒测试中，我们测试越权最常见的方法其实很简单：准备两个浏览器，分别登录高低权限账号，或者两个相同权限的普通账号，然后针对系统中的功能点逐个进行测试。

比如修改请求中的用户 ID、订单 ID、任务 ID 等关键参数，或者直接使用低权限账号访问高权限接口。如果 A 用户能够查看、修改 B 用户的数据，或者普通用户能够执行管理员才能执行的功能，那么大概率就存在水平越权或者垂直越权。

以前我挖洞基本以黑盒测试为主，当时一直有一个疑问：

**为什么越权和未授权漏洞这么常见？**

理论上，开发人员只要给所有需要保护的接口统一加上权限校验，不就解决了吗？难道没有一种方案，可以直接把所有接口都保护起来？

最近开始通过代码审计的方式挖掘 CVE，在分析了几个真实项目的鉴权逻辑之后，我逐渐搞明白了这个问题。

**很多系统并不是“没有鉴权”，真正的问题往往是“鉴权没有覆盖到所有地方”。**

而当我们从代码层面理解这一点之后，再回过头做黑盒测试，会发现以前很多靠经验、靠感觉测试的东西，其实在代码里面都有迹可循。

### 二、正片

这次我们就通过一次 **Java 代码审计中的鉴权分析**，来看一下一个项目的权限控制到底是怎么实现的，以及为什么越权和未授权漏洞会如此高发。

Java Web 项目中存在很多不同的开发框架，比如 Spring Boot、Spring MVC 等。使用成熟框架开发，可以省掉大量重复工作。同样，在登录认证和权限控制方面，开发人员通常也不会从零开始造轮子，而是直接使用成熟的安全框架或者权限组件。

目前 Java 项目中比较常见的认证、授权方案包括：

**Spring Security、Apache Shiro、Sa-Token 等。**

除此之外，有些项目也会通过 Servlet Filter、Spring MVC Interceptor 等机制实现统一的登录校验、接口过滤或者自定义权限控制。

这篇文章我们不把所有框架都展开，而是选择国内项目中比较常见的 **Sa-Token** 作为例子。

我们重点研究三个问题：

**第一，一个使用 Sa-Token 的 Java 项目，到底是怎么完成登录认证和权限控制的？**

**第二，拿到一个陌生项目之后，我们应该怎么快速找到它的鉴权入口，并梳理整个鉴权逻辑？**

**第三，也是最重要的问题：明明项目已经使用了成熟的权限框架，为什么最后还是会出现越权和未授权漏洞？**

搞明白这三个问题之后，你会发现：

**黑盒是在测试“这个接口有没有鉴权”，而白盒是在寻找“哪些接口可能忘了鉴权”。**

这也是我最近做代码审计之后，对越权漏洞理解变化比较大的一个地方。

### 三、satoken是什么

**Sa-Token** 是一个轻量级 Java 权限认证框架，主要解决：**登录认证**、**权限认证**、**单点登录**、**OAuth2.0**、**分布式Session会话**、**微服务网关鉴权** 等一系列权限相关问题。他能实现的功能非常全面所以在我审计的多个开源项目中都使用了sa-token进行鉴权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DdVXYMZZ2zgR6iafLJCyeswunDda3KlhML2b10vFwCyJI87QtT5KETq6Dwymofz7gsoZv6mQmYPQfyPwRIicIrPibVsl6m2yQKHqzgx2Rw7icZk/640?wx_fmt=png&from=appmsg)

image.png

sa-token能够实现的功能如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DdVXYMZZ2ziar940jQfialyicST3ep9V9ib2F0UuP5iaF24o8icia8ZSicDicRzSm1vNWEq1IyWMOMWiaISQOkaRF46HdU8Yp2AjxwVz4VTvZwR8uRgfc/640?wx_fmt=png&from=appmsg)

image.png

使用sa-token进行鉴权也非常简单

![](https://mmbiz.qpic.cn/mmbiz_png/DdVXYMZZ2zhiaZJMQiazqdLsrZH0SkuspoGPjZn4uZfDG3V9INWGGmFtpbsrfRPWvUu3btp4vIVR4HZagRLMjgpPicnzwVXQVxXSfk9v6TjHiag/640?wx_fmt=png&from=appmsg)

image.png

大家可以着重关注下sa-token的对于路由的鉴权（路由新手师傅就理解为路径即可）

![](https://mmbiz.qpic.cn/mmbiz_png/DdVXYMZZ2zjxnveiasKRSNM5OKCQeJSo398IK2EK0iaOZwf8vfATQ0LkBFbiauOLic8FmNy6WZLJiaQZSX5pmjLWeEg0HAViaNcOeOktZb9JBjjHM/640?wx_fmt=png&from=appmsg)

image.png

### 四、来一个案例学会分析satoken鉴权分析

（1）分析项目是否使用了satoken

我们如何知道一个项目是否使用了satoken，如果这个项目依赖包使用了maven我们可以直接查看根目录的pom.xml搜索**sa-token**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DdVXYMZZ2ziaWpibCIMqNv5eksZibzpsicvIgg0M7ljd9oJXiat8nHSY72RZFXMoIpe9CIBLNVWEXViaKibicJnLpm7oszOqxoDkclG3AbmJMuJpwyg/640?wx_fmt=png&from=appmsg)

image.png

或者通过idea编辑器右侧的maven插件查看是否存在sa-token（这个插件太好用了，还可以用来分析是否使用了存在漏洞的插件版本）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DdVXYMZZ2zjEdibCNHJt6x3P2G6gValDPDfaDicY3KQ99EHuKfT8BJsXeeibLxiaybqt0NLJ2l4XCOzqrg1WmRwcMYPgYAkEM8KEOlWs2yYpy28/640?wx_fmt=png&from=appmsg)

image.png

（2）分析项目如何进行鉴权

搜索过滤器和拦截器，过滤器来自servlet拦截器来自springmvc两个如果项目使用的话都有固定的实现方法

```
过滤器全局搜索：implements Filter
拦截器全局搜索：implements HandlerInterceptor （定义拦截器）
SpringMVC配置器：implements WebMvcConfigurer （查看里面是否注册了拦截器，只有注册了拦截器，定义的拦截器才能被使用，比如在里面搜索addInterceptors【添加拦截器】）
```

此项目未使用过滤器使用mvc拦截器调用了satoken框架做鉴权，还写了一点自己的鉴权，但是总体上接口鉴权等还是使用sa-token的能力

![](https://mmbiz.qpic.cn/mmbiz_png/DdVXYMZZ2zj03fxGESZpYeRPxDAXvPZE11DvW7ibXviaueOWpaSlcLOQgzHkpHfliaj3Z6a1NZ4O2OI0GibL7uib9KMFsSAIG5Bl56GNFudGTYh8/640?wx_fmt=png&from=appmsg)

image.png

分析拦截器搜索

`implements WebMvcConfigurer`

发现排除了一个白名单接口列表，剩下的所有接口都要鉴权/\*\*

![](https://mmbiz.qpic.cn/mmbiz_png/DdVXYMZZ2zjj3b7k1GgYqGicrncBG4kjTO32TyPo90re1JicvNab2EQ1oPreUq2yB11LJ3yy5wqAYoPgIxnKOGHHj5YKUN0Ut0atc1ZBeFT6o/640?wx_fmt=png&from=appmsg)

image.png

**通过分析白名单就可以知道swaggerui这些页面默认都是用户可以直接访问的，这下你懂为什么挖洞过程中那么多可以扫到swagger了吧**

![](https://mmbiz.qpic.cn/mmbiz_png/DdVXYMZZ2zgPEia9KDIia9E4aLEXFA3shArsxqpkZGYeA2ojZv2aljFhP2AVWcqWsQIybYOialpH5LxVBsr6xHD4tibYYRIjZyq3KibRtgy77HUA/640?wx_fmt=png&from=appmsg)

image.png

注册的拦截器如下

![](https://mmbiz.qpic.cn/mmbiz_png/DdVXYMZZ2zhFCpYpG0n4bWOb7JTRVWOVO1Yrna1HibBYcp8AHV48ibvy3pPmGYlfdlAd9Z3lq63GQBNYib2p48Yjia9cqggegVpRgWuInXl0ydw/640?wx_fmt=png&from=appmsg)

image.png

跟进去后就是spring mvc过滤器的实现，里面有校验登录和校验权限的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DdVXYMZZ2zghk9bKE2hA795Ab2TLwgROj6tgHy8yNMulg9EniciaBwwSDBOKyYjiaSiavqJbGeDibXB6l9IDcH5AMYNxXicT08icsY12RSlhicZianqA/640?wx_fmt=png&from=appmsg)

image.png

跟进去大概意思就是判断和校验登录是否成功，具体是什么用户权限，如果验证存在问题就抛出异常

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DdVXYMZZ2zju84Ca6MCn1yuQocLKJXziawRJYKicF6Vk6BaPUBMZ7fvmebVNeSOwwdto0Hsfbibu0VG9BRTHpZGeZcELtxmCNjTkPx4LiacSx1c/640?wx_fmt=png&from=appmsg)

image.png

### 四、路由分析

随便搜索一个路由抓登录包也行或者搜索springboot路由关键字@Getmapping、@Postmapping、@RequestMapping等，点击显示该模块的所有端点

![](https://mmbiz.qpic.cn/mmbiz_png/DdVXYMZZ2zgJyWiatVlSkPlWRibG8jesic72RaK7L0Rl3j4XoYxpYjHS2pSJwPdXelPXiad1PT2b5RJVm8PX7e0VseD70yTDoCSAQjt4EVcVHSw/640?wx_fmt=png&from=appmsg)

image.png

点击所有便可以都展示出来走了注解的，如果有的接口走了servelet也是不行的，一般肯定是都走注解的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DdVXYMZZ2zjWDQNsRfnFzMVDyBDTl6KlX20utYBiafibBIiaqYyLjE36icyrnADkLicIucVP5QHLRPJucd7UnD2iaym86GTia9W5NVMHYu5ye1OPKk/640?wx_fmt=png&from=appmsg)

image.png

先看sa-admin模块的路由，发现很多都有satoken的鉴权

![image.png](https://mmbiz.qpic.cn/mmbiz_png/DdVXYMZZ2zhzOicYfoiaLkA6VKHQ8g5kh6icCMl18VnSA6ozxSvXe9FjtAmEzEtgpxYrXPsDeedIYYDGWOou5HSWL2icjRFIgxCH42Z9d0nVAyg/640?wx_fmt=png&from=appmsg)

image.png

但也有很多没有的，这种就是着重分析未授权和越权的对象、路由分析，很多没有注解的地方就是产生越权漏洞的地方！！找到这样的地方然后把项目启动起来，用一个低权限的账号直接请求接口，即可实现垂直越权的增删改查，对于未授权和越权的区别来说，未收取就是未作登录验证或者说误把敏感路由加入了忽略白名单，现在你也动手试试吧！

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/DdVXYMZZ2ziaW4W0JKrEGsUVVLR4jUa8jnuMkQoOrENbF9aeokPk47WxYcm8CMibqqGpDDG7ib9Ka2kT1HesMTYDR7ricXrrRXwfcabibKEyiaRBM/640?wx_fmt=png&from=appmsg)

image.png

### 五、总结

通过分析代码我们可以得知，该项目存在全局登录鉴权，也就是说你没有登录的情况下只能看swagger相关的页面，但是登录后，有很多路由，程序员都忘记添加@SaCheckPermission注解进行鉴权，导致我们只要登录任意一个账户就可以实现垂直越权。从而发现很多的越权漏洞。所以总结来说就是开发工程师在开发过程中可能做了总体鉴权，但是一些后加的功能或者细致末节的功能忘记添加鉴权注解（此处仅以sa-token为例，有的框架是不用注解进行鉴权的）换位思考，我们也不可能每个地方都能非常细心。所以结合白盒审计我们更能理解某些黑盒漏洞为什么在漏洞挖掘过程中占比较高。

通过代码分析可以发现，该项目实际上已经实现了全局身份认证。也就是说，在未登录的情况下，除 Swagger 等被放行的资源外，大部分业务接口都无法直接访问。

但进一步审计登录后的接口时会发现，部分路由虽然要求用户处于登录状态，却没有配置对应的 `@SaCheckPermission` 权限校验。这就造成了一个典型的问题：**程序验证了“你是不是一个合法用户”，却没有进一步验证“你是否有权限执行当前操作”。** 因此，攻击者只需要登录一个普通低权限账户，就可能访问原本仅允许高权限角色使用的接口，从而形成垂直越权漏洞。

这类问题在实际项目中非常常见。开发人员可能已经在框架层面完成了统一的登录认证和基础权限控制，但随着项目不断迭代，新功能、新接口不断增加，一些后续添加或相对边缘的功能可能遗漏具体的权限校验。本文以 Sa-Token 的 `@SaCheckPermission` 注解为例，实际项目中的权限控制并不一定通过注解实现，也可能采用拦截器、过滤器、配置文件或代码逻辑等方式完成。

从开发者的角度来看，这种问题其实并不难理解：当一个项目拥有数百甚至数千个接口，并且长期处于多人协作和持续迭代的状态时，很难保证每一个新增接口都始终正确地配置权限控制。而权限校验一旦出现遗漏，就可能直接产生未授权访问或越权漏洞。

这也是白盒代码审计非常有价值的一点。通过代码，我们不仅能够发现某一个具体的越权漏洞，还能够进一步理解漏洞产生的根本原因。再回到黑盒漏洞挖掘中，就更容易理解为什么**越权、未授权访问以及其他访问控制类漏洞会长期成为高频漏洞类型**——很多时候，问题并不是系统完全没有鉴权，而是鉴权覆盖得“不够完整”。

最后，我是地图大师，感谢你的阅读！

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GHet7yDwHiaMaYh9wC7acaQIAZYUZ5CxCsmQTJIzhNA5Zw4wbcdHtqCFNqqZFjdvoeLicQyC76icdqbR3y9pLGF4A/0?wx_fmt=png)

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