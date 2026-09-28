---
title: 漏洞挖掘案例-任意用户接管
url: https://mp.weixin.qq.com/s/9nPkJwFP-wYUE6Eyw4lHuA
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:55:48.115732
---

# 漏洞挖掘案例-任意用户接管

# 漏洞挖掘案例-任意用户接管

原创

知名小朋友
知名小朋友

进击安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# **免责申明** 本文章仅用于信息安全防御技术分享，因用于其他用途而产生不良后果,作者不承担任何法律责任，请严格遵循中华人民共和国相关法律法规，禁止做一切违法犯罪行为。

一、前言

最近一直在研究相关的AI相关方面的信息，也有了一定的成果，好久没有自己写文章了，今天来更新一篇，同时也记录一下自己的成果，同时分享一个比较有意思的AI任意用户接管的漏洞。

二、漏洞挖掘过程

我们知道，每一个网站JS都是我们漏洞挖掘不可忽略的地方，里面往往藏了很多相关的一些功能接口参数调用等功能。

（这里在chunk中发现如下信息，不知道chunk的兄弟们可以百度一下）

这里让ai把全部的接口提取出来之后，因为没有账号，打了一轮未授权没有发现漏洞，于是着重尝试突破身份认证相关的功能点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQcLuw9F5XiaIq35zwTRB6RSxYricWTLXoeKHHCUGU4vicM3U8fv4yiawaejjDqpU42JA0kzWz4uCtlxhibnffvzf5k6EicTdI3uVPek/640?wx_fmt=png&from=appmsg)

经过提取，得到如上图所示的一些关于oauth功能点信息，这里看到是一个扫码登录的功能点。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQI9jKDzVQPslPJtXZFybXly4bC9JDRxZJ3sjzrTcBcUkr3O5qSxFhp7xtXhvDL42eexc05CQzP6BQJXfA49AQYP62BicibDiaI3k/640?wx_fmt=png&from=appmsg)

同时这里也是可以多得到一些信息，post请求方法，以及参数，这里参数不清楚，可以尝试动调或者fuzz当然这里ai大人已经给出了答案。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRUncrzJfdibC1FdYNXRvBIziaibuGYq0cTsh3MlDcUrMORulg3PJa17l6wNKowP1BXyx8DJoRvXpw2U366G5S25LfTVSYOGlF7lA/640?wx_fmt=png&from=appmsg)

这里进行传递参数之后发现回显上述信息，这里其实可以得到，权限是需要高级的，也就是说这个接口可能是未授权的，其实这一步就很细节了，如果之前人工测试的话，估计这个回显信息看一眼就直接扔掉了，但是ai给出了疑惑，此接口可能存在未授权来判断当前用户是否存在。

同时得到这个消息之后，进行反哺深入发现相关任何的关于认证的线索，在一处JS中发现如下信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTgbUHrh0GbyTETt93GGqYqiahMNZIicXYP2dhYRaTgU14DqqAshGv20p2DmQiaRaXd8ibWzOQCvFxMPzCa3vMiaIO11ZLicq0h1TdqU/640?wx_fmt=png&from=appmsg)

这里可以看出来，当status为3的时候check接口回返回token信息。

也就是说，整个扫码登录的过程，我们前段可能可以控制，配合上述的用户名枚举，然后来传一个stauts的value从而来获取对应的tokne信息。

这里再让AI分析关于判断扫码成功与否的接口在哪里，很快AI给出了答案。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRA1C15L0ZxJAfAsGticYWWnmfRVlWLQxyygbYXiciaaa6QWE5zomg4bjl8pye7YU8VJbUviaCjDIM0alWTpBibTibwg8mcmc5OibDEoM/640?wx_fmt=png&from=appmsg)

尝试进行接管用户。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQ1Cibm3owGwpQDWSgiamiaHxbH13U1CPbxVbs170gn1uNz3zPe28JsX1KJyuCxSrfzZ4QWtrdBmQAzqQFLFJHRV8JFZD6GussI3g/640?wx_fmt=png&from=appmsg)

这里首先进行通过用户获取到相关的扫码等待状态code，然后在进行对该code伪造status为3来获取token。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSSvCYhqibCuOicZ3F6aDFTSTCQ54rlDdu2xOt7dIJJD7J5fwvmWzcINZfSXlYtDX4ib8ddT14l8zltu2ic73npiaLjIwQqzQse6Phc/640?wx_fmt=png&from=appmsg)

成功得到响应为Success响应信息，同时再次通过check接口来验证当前code的扫码状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTbm15xXFuEuoL32ldCkqab9iah9MQMoDPEleibdwCCpicSVgu9efd9TichcyzVdhQUUwlUJ4vIPETspp3xP3iavoCoQ9ibiaXNTohHDE/640?wx_fmt=png&from=appmsg)

成功得到了相关的TokenValue信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Dfrm5V3o6kQ7I62AkQYsy3GxXehicHYW8MkjFUrmyIicep5xuAH8v12ShlOzUAg9uaK6U6L3tbHu5MzBuOZ058tibNkzcUBtIUYwJxTVUceL3I/640?wx_fmt=jpeg)

可以看到，带上相关的身份凭证之后成功获取到个人信息，完整了整个的接管流程。

最后送给兄弟们一句话，不要把AI大人的能力当为自己的能力。

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQyoKvYicu5aKkgia7k38ECySrHCy4KOegDe0mRRsQQ5ib1hZhYUrgib8MzticHLNBlvGspdUwot7r0BQ5fDeaFBz52lnV6Q1icgQgk4/640?wx_fmt=png&from=appmsg)

最后送给兄弟们一句，针对于一些skill包括渗透智能体，我个人个感觉都是一些比较死板的东西，但是好处就是给一个url不用管了，比较方便，不用太多精力，但是如果一些像zocde，codex等他会很灵活，但是会很费时间，这个就看兄弟们怎么选择了。

三、课程相关

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQSW71AFriaiapRIE79LFkHK2WNVMIZEl7DC9UJCEedC8T4ITl0ume8eMtqzmVBFFxMlfkUlN9ZvpET3khQCkBN6Gfo6TibKHzvc8/640?wx_fmt=png&from=appmsg)

同期这里第五期课程已经结束了，因为目前AI发展比较快，小朋友这里也研究了一段时间。

定下第六期为AI赋能课程，这里赋能方向暂定，渗透，审计，攻防，占位（最后还没想好）。

但是小朋友一直都是先要说服自己，再去做相关的教学，如果什么都不做，没有一些拿的出来的成果做培训也站不住脚，特别是在AI如此高速迭代的时代背景下。

下面放一些小朋友的成果截图，以及相关的第六期AI课程安排。

四、部分成果

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQjdGVXOLqeIHgqXaPt02xye8dRj8ib7T58SOzqo7uknUtiaUrk2iaGcSHlbIxLro5DJ55ezv4oRX7EC1v24fETpsSJLRicymVvUSU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kT2AUKGtwwdAicbW7sBThG5dvTZNQFibhLoJznyd45X53ENibFdn5OibSDCTrziaFTulsfhjIcsjuuP883wg3OTkzjjTb1RYJNylfNU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kS9Ufib36nFJm3ib3BfaIZvVOSFJN7qWMRvPX04a3bOGeKqkpMsc6TBIeLcJ3cUruucK3o5JibzShYY6brz82YDA3HNTYsY0QdEibE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTUIMn9QfCEJIic4icDGUz4CibvgHAO1v15YuKEFibibicmE5JVwndmEk2L1P8PtoIUSA9E27lHhOTKgkPjNfX55prBoht5GcCcsOUho/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTjmAwMhFevenGQQjLyOvQtayy2vVqN6lmmnsB4Lgm8JTEtoOiaypwdjHCS4LO7yqy1DFtIN9BnPFYLugKD9ekNX5WvNHiaqoeco/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTOkR20SvHyQQk8vsFZWef3sbA00b7iceGAibla45qzkQzVp67gGFqiaHUAu7BI41icPHOgYOoCzbHVaU1OC7z9wrT3fcNSGmJpGU8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQJ3zQ1hhALOoGx3uanOHkhSVQKbr5ou3pfEwlBjHGEpicXuAw1DZtFszRoVmjXB8PRCvhx0s1cVdEDh7FpPqYqbQ3H2FjqML0w/640?wx_fmt=png&from=appmsg)

这里还有部分相关的没有审核的漏洞就暂时不放出来了兄弟们，漏洞类型其中包含了rce以及sql注入未授权用户接管，APP，和小程序，WEB等都有，但是目前兄弟们也发现了，SRC慢慢的开始也在使用AI对安全方面进行自我消耗，个大SRC陆续关闭暂停，这也是为什么刚开始说做SRC课程最后转变为渗透课程，不仅仅是教大家如何在SRC上用AI漏洞挖掘，同时也是如果在在渗透项目当中降低自己的时间精力成本获得更有质量的交付水准，同期AI攻防目前也在筹备了，这里主要给兄弟们汇报渗透方向。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTRxkd3micVn1PMYRvKqyQVltsXVhRNPBrrUEO0wcpad1cyPo2MY0Uy138YkQia9YKRRTudQRniaVic5MUtmuDibHMyEr08GVRnsjeQ/640?wx_fmt=png&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

五、往期课程

```
代码审计培训介绍&广告区域

二、第五期课程（已完结）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dJGuszYr5iaRGiaZURAxJAROibCh1sjaZictcbC4iasuuOgCMQSDSwrG5Wfrx2QgfvKx8icDhm0gIia8fN6mThehEK8ww/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=121)

第五期课程仍然是以代码审计为主，本次课程还是为三个语言的代码审计0-1讲解，目的为帮助学员完成0-1+1的白盒（代码审计）漏洞挖掘，并且在出货的基础上再+1去出高质量的漏洞（例如组合拳RCE、前台相关漏洞等）。

1

课程周期

开课周期预计到：三个月左右（直播+录播）

课程大纲

本次课程分为PHP、JAVA、NET代码审计为直播+录播，为了照顾一些基础较为薄弱的师傅新增基础~技巧~番外（录播课程）。

01

PHP&JAVA&NET代码审计 (直播+录播)

之前课程大纲主要为xxx实战案例，本次课程大纲着重体现思路方向，并非取消了实战部分，实战部分之多不减。

PHP课程目录

✅  第一节课：多框架初识&路由认识&参数传递

✅  第二节课：多框架&鉴权分析&认证与鉴权&鉴权方式

✅  第三节课：多框架&常见漏洞函数&回显&非回显

✅  第四节课：注入漏洞&常见位置&实战审计注入类漏洞

✅  第五节课：前台RCE漏洞审计&漏洞案例技巧讲解

✅  第六节课：门户网站CMS&网络设备&审计经验讲解

✅  第七节课：多框架&鉴权对抗&权限绕过技巧&案例分析

✅  第八节课：组合拳RCE漏洞分析&漏洞组合拳利用&案例

✅  第九节课：PHP下反序列化漏洞&魔术方法&pop链分析

✅  第十节课：PHP下反序列化漏洞实战&phar协议RCE案例

JAVA课程目录

✅  第一节课：Servlet&Spring Boot&Spring MVC&Struts2

✅  第二节课：多框架下&拦截器&认证鉴权&组件鉴权分析

✅  第三节课：多框架下&权限绕过&鉴权对抗&案例分析

✅  第四节课：常见漏洞函数&案例分析&审计技巧

✅  第五节课：前台漏洞审计&组合拳rce漏洞&技巧&案例

✅  第六节课：反序列化&CC链利用&反序列化漏洞利用

✅  第七节课：Ognl&SpEl&EL表达式注入&漏洞案例

✅  第八节课：内存马简介&内存马原理分析&内存马注入方式

✅  第九节课：RMI&JNDI注入&JNDI注入漏洞利用&案例

✅  第十节课：组件漏洞&shiro&fastjson&log4j分析&利用

.NET课程目录

✅  第一节课：初识.NET&Web From & MVC架构框架分析

✅  第二节课：Web From&MVC框架&鉴权分析&认证方式

✅  第三节课：多框架下&鉴权对抗&权限绕过分析&案例

✅  第四节课：注入漏洞分析&文件操作类漏洞&实战分析

✅  第五节课：常见漏洞位置&前台漏洞审计&漏洞案例讲解

✅  第六节课：组合拳RCE漏洞分析&组合拳RCE案例讲解

✅  第七节课：.NET反序列化漏洞初识&反序列化漏洞原理

✅  第八节课：.NET安全反序列化链&反序列化触发场景

✅  第九节课：.NET反序列化漏洞案例&反序列化漏洞分析

02

基础~技巧~番外（录播)

该篇章为长期更新

1

基础篇章

1、由于之前上课时部分师傅存在一定基础，刚开始的课程部分师傅认为自己可以跟的上等问题，导致时间的浪费。

2、同时有一定的师傅存在无法搭建源码，以及软件下载等问题，于是将这种基础问题，统一归纳为基础篇章，供师傅们学习，节省师傅们时间提升学习效率及课程质量

3、同时面对部分学员频繁提出的一些问题，针对该问题同样会进行解答，并且进行录制上传至基础篇章中。

2

技巧篇章

1、随着自己技术的进步也了解到了一些新型的技巧或者手法，例如sql注入的某一个技巧，但是重新讲解又浪费大量时间，特地新增了技巧篇章，将单独的技巧进行讲解。

3

番外篇章

1、自己在第四期讲过一些逆向相关，并且还存在相关的一些好的案例，得到了挺多师傅的认可，例如某APP接管存储桶等案例，于是之后在有好的案例将进行上传更新。

课程思维导图

![图片](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQc6EJ84iabOyZW9zXBA8OhdzTicXH97thEzlibk2CsOT9ucJd56w81QLZ7BT92w5IlaDwjA7iaUDpPKt4ib3yFY4YJicCo80TIh9C3M/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=122)

常见疑问&课程讲解

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xblgvfap0kicWhU0Yu7COibQdbBuJvJL4V8ZibyDFtoZ1DjX4PlAzgHXV1Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=123)

第五期课程收费多少？

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xbn64xklaibRPwn8iadq2gzV1us6KUbIGdxlicMkhBo7loMRbVQ5bDnPZqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=124)

本次课程收费仍然是1688，并且还是承诺一次报名后续不再进行任何二次收费保障（包含内部平台，以及后续推出一系列内容均可观看）。

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xblgvfap0kicWhU0Yu7COibQdbBuJvJL4V8ZibyDFtoZ1DjX4PlAzgHXV1Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=125)

什么时间段上课，上课周期是多长时间？

![图片](https://mmbiz.qpic.cn/mmbiz_png/TN05MmJLxMpA2RBXPMibJ9EsZG9K2Y9Xbn64xklaibRPwn8iadq2gzV1us6KUbIGdxlicMkhBo7loMRbVQ5bDnPZqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#img...