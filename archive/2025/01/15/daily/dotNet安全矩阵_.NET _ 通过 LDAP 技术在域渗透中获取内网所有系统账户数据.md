---
title: .NET | 通过 LDAP 技术在域渗透中获取内网所有系统账户数据
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498206&idx=1&sn=5f290cbc0e9c1a8c76d0e0cb8625cf4c&chksm=fa595733cd2ede25f81edaa97c23c5128bf81f91b9853c6992c7ea10cc5b4cccc56a8c991b67&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-15
fetch_date: 2025-10-06T20:11:04.922065
---

# .NET | 通过 LDAP 技术在域渗透中获取内网所有系统账户数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicbRRVvibkjk9ne2ZSqtkvzK6cSU838x7tiaUmrZkMazfKJvxLgqpVdic9gCUicD833A03MUuFRuEgaiaA/0?wx_fmt=jpeg)

# .NET | 通过 LDAP 技术在域渗透中获取内网所有系统账户数据

原创

专攻.NET安全的

dotNet安全矩阵

![](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YicsyG1B1VbeJmomT9X9FIp9aribEBCo7sLwiaDv02G8D2SSdJnrgU3w0AVtCas5gEC0eRicTLXKoPYsg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

在域渗透测试与红队行动中，Active Directory 作为企业网络的核心身份认证与管理平台，始终是攻击与防御的焦点。LDAP作为AD的核心访问接口，为攻击者提供了丰富的查询能力，而这一特性也被广泛用于枚举域用户、组和其他关键对象。结合 Sharp4SploitConsole 这样的强大工具，攻击者能够以简洁高效的方式，利用 LDAP 查询在短时间内收集大量的域信息，从而为进一步的攻击行动奠定基础。

01

LDAP查询语法基础概述

在Windows域环境中，Active Directory (AD) 是核心的身份验证与资源管理服务。为了高效地检索和管理AD中的数据，LDAP查询是必不可少的工具。

LDAP查询语法以过滤器的形式表达，通常用于筛选符合特定条件的目录对象。其基本结构如下：

```
```
(属性=值)
=：等于
!=：不等于
>=：大于或等于
<=：小于或等于
:1.2.840.113556.1.4.803:=：按位与
```
```

**1.1 查询SPN对象**

servicePrincipalName (SPN) 是Kerberos身份验证的重要组件，通常与服务帐户相关联。此查询可以用来枚举域内所有配置了SPN的帐户。具体示例如下所示。

```
```
ldapsearch -h <域控IP> -x -b "dc=example,dc=com" "(servicePrincipalName=*)"
```
```

**1.2 查询弱密码的账户**

userAccountControl 是一个标志位属性，每个位代表一个特定功能。1.2.840.113556.1.4.803 是按位与的操作符，此查询排除了所有禁用且设置为无需密码的用户帐户。具体示例如下所示。

```
```
ldapsearch -h <域控IP> -x -b "dc=example,dc=com" "(!(userAccountControl:1.2.840.113556.1.4.803:=1048574))"
```
```

**1.3 查询高权限的账户**

adminCount=1 通常用于标识具有特权的帐户，如域管理员和企业管理员。这些帐户被Active Directory自动标记以启用额外的安全保护，具体示例如下所示。

```
```
ldapsearch -h <域控IP> -x -b "dc=example,dc=com" "(admincount=1)"
```
```

**1.4 查询错误的配置**

msDS-AllowedToDelegateTo 定义了账户可以委派的服务列表。这在Kerberos约束委派中扮演重要角色，具体示例如下所示。

```
```
ldapsearch -h <域控IP> -x -b "dc=example,dc=com" "(msds-allowedtodelegateto=*)"
```
```

**1.5 查询委派攻击**

查询 userAccountControl 属性包含值 4194304 的对象，此项值 代表“受信任以进行委派”（Trusted for Delegation），具体示例如下所示。

```
```
ldapsearch -h <域控IP> -x -b "dc=example,dc=com" "(userAccountControl:1.2.840.113556.1.4.803:=4194304)"
```
```

02

工具实现和实战操作步骤

Sharp4SploitConsole 便是这样一款强大的红队工具，通过交互式控制台提供一系列功能，能够在域环境中高效地执行信息收集与利用操作。其中，GetDomainUsers 参数用于枚举域中的用户账户信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicbRRVvibkjk9ne2ZSqtkvzK2paiaUbceYCkQiarV3bAR24jJvfnMF4PyPFNzYMFx24akMPGe8yCbFGw/640?wx_fmt=jpeg&from=appmsg)

**2.1 具体使用方法**

运行以下命令启动 Sharp4SploitConsole，在工具启动后，输入以下命令进入交互式控制台模式。

```
```
SharpSploitConsole.exe
Interact
```
```

再输入 GetDomainUsers 命令以枚举域用户信息，执行此命令后，工具会查询域控并返回所有用户账户的详细信息，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicbRRVvibkjk9ne2ZSqtkvzKux8icpSZryNxia7Fk1uZrQnDHC9vwX4NLHsbnbrRBA9G46SiaicZ8VnMuA/640?wx_fmt=png&from=appmsg)

综上，Sharp4SploitConsole 是红队进行域环境渗透的强大工具，其中 GetDomainUsers 命令提供了快速获取域用户信息的能力。红队可利用此功能定位高价值目标并制定攻击计划。同时，防御方需要加强账户管理与监控，确保域环境的安全性，文章涉及的工具已打包在星球，感兴趣的朋友可以加入自取。

03

公众号安全技术精华内容

从漏洞分析到安全攻防，我们涵盖了 .NET 安全各个关键方面，为您呈现最新、最全面的 .NET 安全知识，下面是公众号发布的精华文章集合，推荐大伙阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8A7Qhn1ssuqNzv0iceS7ZhOuZ0AO4P1eFeG2xTdR2V6GWibiaxO2RenUJzrwOfvsdqofibI6H2uY0CLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497429&idx=2&sn=a07599921eeb651ce005f57ed350be5e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497498&idx=2&sn=00900a0c29c85b41fe6a586d7e5c3571&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9tl26Kh2sQYI9guTCflSwQP8Gs9z7iamicOvlQv4UYzjwd378D03h7yEYFtZ6xA74qicInoed7qpBWg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495167&idx=1&sn=9280c55fdc7c9146e549be470cf9f120&chksm=fa594312cd2eca04bfe8fd1fd3890b389d9c700b9b69d897f919addac399bab4f4d2e55f6b4f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

04

欢迎加入.NET 安全矩阵星球

**4.1 .NET 安全社区**

目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最专业的技术知识库之一，超 **1200+** 成员一起互动学习。星球主题数量近 **600+**，精华主题 230+，PDF文档和压缩包 300+ 。从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的实战指南和最佳实践。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9AiaXibTRdEnEfYuQx76FjZVjmyEWtIaDuDePFFmyRqggiaq2k47pLoib9GZtUCOhaP40WPlhvbiaKZVg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**4.2 20+个专栏文章**

星球文化始终认为授人以鱼不如授人以渔！星球整理出**20+**个专题栏目涵盖 **.NET安全 点、线、面、体等知识范围**，助力师傅们实战攻防！其中主题包括.NET  内网攻防、漏洞分析、内存马、代码审计、预编译、反序列化、WebShell免杀、命令执行、工具库等等。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa90SJRuwnLy9uZV4icrXiaZlJPQlYJWXTw8HCrF9oTcE3DDgrdFnXo2BA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**4.3 星球海量的工具**

截至当前，dot.Net安全矩阵星球社区汇聚了 **600+** 个实用工具和高质量PDF学习资料。这些资源涵盖了攻防对抗的各个方面，在实战中能够发挥显著作用，为对抗突破提供强有力的支持。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaqVZW8XsALVA4FNiaj32q8npN82VSeqSKb4fQvLiczFNs0099VRFVQwPA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopa63ZXbX3YXLwoeNnjStcRtTbU9hoe6ecO5hhkj2apG1I6tKlkpz5GaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**4.4 星球专属成员群**

我们还有多个成员专属的**内部星球陪伴群**，加入的成员可以通过在群里提出问题或参与论的方式来与其他成员交流思想和经验。此外还可以通过星球或者微信群私聊向我们进行提问，以获取帮助迅速解决问题。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopaAiaouHb6HYza539m9v0ykDoD2JezaArDZBPlJInuabf6XsduzVcjZ0Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**4.5 入驻星球的大咖们**

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多**高质量的.NET安全资源**，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicAg36pkFaC2P1KW0L5NV1HOssmysrPnrP1fzr2rFOmy8lA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**4.6 欢迎加入我们**

dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。**星球门票后期价格随着内容和质量的不断沉淀会适当提高，因此越早加入越好！**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xRheDpQ7NsESosdNZUopag09JtYcKpucjZPAlfeqC1ovcQvhrkemAzbURDaVF3InmpQshiatDnyQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt...