---
title: .NET安全入门：免杀空间/类/标识符
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247494725&idx=1&sn=6dd4bad98a08379b8b6a5a32ace95bf9&chksm=fa5942a8cd2ecbbebbd28266f1aa515cc23fd52851ce3c0447c62cefdb0dc7ab5c760ed39e67&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-08-24
fetch_date: 2025-10-06T18:05:21.663464
---

# .NET安全入门：免杀空间/类/标识符

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiciavNweQv6GpcBLe0Hr4ckX3vyKZXnKLESINxSNJjSTuwdYNzIwD3ZOsbRxNE0DPS0ReaKt4004tw/0?wx_fmt=jpeg)

# .NET安全入门：免杀空间/类/标识符

原创

专攻.NET安全的

dotNet安全矩阵

01

.NET安全基础概念

**以.NET安全为主线，****命名空间、类、关键字和标识符作为构建程序的基本元素**

，它们不仅关乎代码的结构，还与代码的安全性紧密相连。本文将深度解析.NET命名空间、类、标识符基础知识以及与免杀技术之间的关联。

02

基础:空间/类/关键字

一个.NET程序由多个关键组成部分构成，这些部分协同工作，共同实现程序的功能。下面将深入解析这些组成部分，帮助读者更好地理解我们选用.NET控制台程序的架构。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiciavNweQv6GpcBLe0Hr4ckXGicql8BicqhbKjsjxebuiboXyANLFUqsUPzWRlTTaJrIeE9nmRKUFrxicA/640?wx_fmt=png&from=appmsg)

## 2.1 命名空间

命名空间是.NET中用于组织类型（如类、接口、枚举等）的一种机制。类似于文件系统中的文件夹，有助于避免命名冲突，并使得代码更加模块化，也更像生活中存储物品的大仓库。在.NET程序中，using关键字用于引入命名空间，使得该命名空间下的类型可以直接在代码中使用，而无需指定完整的命名空间路径。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiciavNweQv6GpcBLe0Hr4ckXQ78edNfDEKsicmGJZ6RUSEzhDq9dvBxVNOgLrBatYjq3y35mjllOQVA/640?wx_fmt=png&from=appmsg)

## 2.2 类

类是.NET程序的核心，是用户定义的类型，用于封装数据（字段、属性）和行为（方法、事件）。在控制台程序中，通常会有一个或多个类，其中至少包含一个Main方法作为程序的入口点。例如，Program类就是实现主程序逻辑的地方。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiciavNweQv6GpcBLe0Hr4ckXL79BKpOAeZJ66KwhU2VnuSqTM9cu94e2xlPB7eiaRW7twoo7EamjLog/640?wx_fmt=png&from=appmsg)

## 2.3 关键字

关键字是.NET语言中预定义的、具有特殊含义的单词。它们用于定义程序的结构和语法，如using、class、static、void等。在编写.NET程序时，必须遵循这些关键字的规则，以确保代码的正确性和可读性。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiciavNweQv6GpcBLe0Hr4ckX0PdU0ZnkF6rsbGVbVyafGb6SgtlEicZnDkykRubFqjdxqLZRsjRDODQ/640?wx_fmt=png&from=appmsg)

03

免杀:标识符/类/空间

在.NET安全技术中，通过巧妙地使用字符或特殊命名约定，可以在一定程度上实现代码的免杀，从而避免被WAF或者其他安全设备识别和拦截。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiciavNweQv6GpcBLe0Hr4ckXkwzHUGZQvymynmFdRiaYDBsD61yiccXQceUg3EeNnoRwwrPNQmiaZ25iaQ/640?wx_fmt=png&from=appmsg)

## 3.1 标识符

标识符是编程中用于识别类、方法、属性等元素的名称，值得注意的是，@符号在.NET中具有特殊含义，它用于字符串字面量中表示转义字符，然而，通过巧妙地使用Unicode字符或特殊命名约定，可以在一定程度上实现代码的免杀

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiciavNweQv6GpcBLe0Hr4ckXvQQaOBh5y0vpicEcJltibOvZAFGLuMf7mU5LTGF8lXLMBvboYia02PSEg/640?wx_fmt=png&from=appmsg)

## 3.2 类

命名空间是.NET中用于组织类、接口等元素的逻辑分组，有助于避免命名冲突，并提升代码的组织性。除此之外，引入命名空间的using，还有个取别名的功能，using + 别名 = 包

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiciavNweQv6GpcBLe0Hr4ckXic0UetsoQ6wgOsswMIGvia8z37BxrZhvVichvbMNeHVWzQNfvBXB3fruw/640?wx_fmt=png&from=appmsg)

## 3.3 命名空间

命名空间是.NET中用于组织类、接口等元素的逻辑分组，有助于避免命名冲突，并提升代码的组织性。除此之外，引入命名空间的using，还有个取别名的功能，using + 别名 = 包括详细命名空间信息的具体的类型，当需要用到这个类型的时候，就每个地方都要用详细命名空间的办法来区分这些相同名字的类型，当然被用来做免杀也是相当的赞。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YiciavNweQv6GpcBLe0Hr4ckX4ic9W0IibQMiaw7rPv5VWZdWHPdyMxWs0GsFZb2fR9Ya90uYgDd3icEXog/640?wx_fmt=png&from=appmsg)

04

加入.NET安全基础入门

在运营dot.Net安全矩阵星球的这段超过两年的时光里，我们见证了许许多多的.NET安全爱好者从四面八方汇聚而来。通过和这些朋友们的沟通中，我们深刻体会到不少朋友对于夯实.NET安全基础、掌握学习路径有着迫切的需求。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8iciasX3mOSk23icIyjXqibhQEUTqP70ibLOAhjfaDs0IlqiaibHdRZW3HHdzmNziaslPMzXLT9zQWVjKToQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

鉴于朋友们的广泛期待与迫切需求，我们决定创立一个专门聚焦于.NET安全基础入门体系化知识的星球—《dot.Net安全基础入门》。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibKowUhdibywicSp8xIlufYymYWHTvX2aPSpB6C3x1MHuE148pibGN5CCYOaCniaMrsa8s6dVQvPfD26g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

考虑将加入星球朋友们主要由.NET新手及零基础的学习者构成，我们经过深思熟虑，决定以**视频讲解的方式**作为主要学习桥梁，力求以更加生动直观的方式，深入浅出地介绍相关基础知识，助力每位朋友轻松入门，稳步前行。

在这里，您不是孤军奋战。我们特别设立了多个会员专属的内部星球陪伴群，加入的成员可以自由地提出疑问、分享见解、相互启发。我们相信，通过思想的碰撞与经验的交流，您将收获远超预期的宝贵财富。目前已有80+位朋友抢先预定，对.NET安全基础入门知识感兴趣的朋友们请尽快加入星球！

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8iciasX3mOSk23icIyjXqibhQE8nibEBxSljtLrQMlf3kHrLPa0Y1icR5ibodAFbTEkdLia2tSib4W6VNdEsQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

为了回馈广大朋友们的热情与支持，****特别给朋友们准备早鸟价专属的30元优惠券，券后只需 **¥99，后期价格随着内容和质量的不断沉淀会适当提高******。这不仅是对您前瞻眼光的认可，更是为了让您以更优惠的价格，拥抱日益增长的知识价值。越早行动，优惠越多，福利满满！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicQK2HsTLtQvibTFaXAhfcErpW6ibNxk8veZ2vjbaxS7l7lrxFDzJvxnvDsNJ8qzXtmvNoxQanu75HQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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