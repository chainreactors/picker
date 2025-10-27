---
title: .NET内网实战：通过 findstr 快速获取数据库连接密码
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498317&idx=1&sn=a5fbee0aae201e4dfbe1b11cd8875574&chksm=fa5954a0cd2eddb64b0d918c03c9bcd317a860e08c6e4b8154b1b5af1c4146c88ad78be379c2&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-20
fetch_date: 2025-10-06T20:09:27.195115
---

# .NET内网实战：通过 findstr 快速获取数据库连接密码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8BMpj9YFSbJMRoY97L1hdPDrcgD3BFPq2ibsuvKQDAZA7NQyQSA6icC5BOeSIw4wSS3XicVV6iciaHImQ/0?wx_fmt=jpeg)

# .NET内网实战：通过 findstr 快速获取数据库连接密码

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过findstr快速获取数据库连接密码》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有300+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8BMpj9YFSbJMRoY97L1hdPdmNoyJ6jnXWe5emfOHSXWoDeMfT4HMZsiatQ6U5hCkW3Wm7cZ1Ptc4w/640?wx_fmt=png&from=appmsg)

03

原理分析

在渗透测试和红队活动中，获取应用程序的配置文件是获取敏感信息（如数据库连接字符串、用户名和密码等）的关键步骤。我们可以利用 findstr 命令结合 .NET 语言来查找和提取配置文件中的这些敏感信息。

## 3.1 MSSQL

在 .NET 中通常搭配MSSQL数据库，连接数据库的信息存储在web.config或者app.config，具体配置可参考如下所示的内容。

```
```
<connectionStrings>
  <add name="DefaultConnection" connectionString="Data Source=localhost;Initial Catalog=MyDatabase;User ID=sa;Password=P@ssw0rd;" providerName="System.Data.SqlClient" />
</connectionStrings>
```
```

## 3.2 MySQL

MySQL 在某些 .NET 项目中也很常见，其连接字符串支持多种字段定义方式，常见的标准形式如下所示。

```
```
Server=127.0.0.1;Database=MyDatabase;User=root;Password=P@ssw0rd;
```
```

在某些驱动程序中，比如 MySql.Data.MySqlClient，User ID 是 User 的别名，两者功能完全一致。因此，也可以替换成这样。

```
```
Server=localhost;Database=MyDatabase;User ID=root;Password=P@ssw0rd;
```
```

值得注意的是 ，虽然 User ID 与 User 功能相同，但不是所有 MySQL 驱动都支持 User ID，推荐优先使用 User，以确保兼容性。

## 3.3 findstr命令

findstr 是 Windows 命令行中的一个强大工具，用于在文件或输出结果中查找指定的文本模式或字符串。我们在命令行窗口，输入 findstr /? 查看所有的参数以及含义，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8BMpj9YFSbJMRoY97L1hdPPe08Vah2B7zAa7XISB3J0Bg2r5WLI8EHCZNkQ3ao3gibKYxGfgAAZlw/640?wx_fmt=other&from=appmsg)

其中参数 /C 表示查找完全匹配的字符串，并且可以指定多个 /C: 参数分别查找不同的字符串，比如常用的搜索命令如下所示

```
```
findstr /c:"User ID = " /c:"UID=" /c:"UID= " /c:"UID = " /c:"Password = " /c:"PWD="  /si *.config *.txt
```
```

另外， 参数 /s 表示在当前目录及所有子目录中搜索，确保可以找到所有相关文件，/i 表示忽略大小写，确保查找字符串时不会因为大小写差异漏掉结果。

实战中，可以使用 System.Diagnostics.Process 类来启动一个新的进程，执行命令行中的 findstr 命令，获取其输出，并将结果打印到控制台，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8BMpj9YFSbJMRoY97L1hdPRibiaiaakibPzCKP82qoByQzq8IClJByrqKIweM7iaIroAic5MVOJg4ibiaZ0Q/640?wx_fmt=other&from=appmsg)

综上，通过使用 .NET 和 findstr 命令，我们能够在多个配置文件中自动化地查找和提取敏感信息。这个方法既简单又高效，特别适用于渗透测试和红队活动中快速扫描配置文件，帮助快速定位潜在的安全漏洞。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

04

**欢迎加入.NET 电子报刊**

我们的小报童电子报刊【.NET内网安全攻防】也开始运营，引入小报童也是为了弥补知识星球对于轻量级阅读支持的不足，为用户读者提供更佳的阅读体验。如果您对阅读体验的需求比较高，那么可以订阅这个专栏。

本次电子报刊《.NET 内网安全攻防》专栏，内容主要有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，可细分为以下8个方向。

```
1） .NET 安全防御绕过
2） .NET 本地权限提升
3） .NET 内网信息收集
4） .NET 内网代理通道
5） .NET 内网横向移动
6） .NET 目标权限维持
7） .NET 数据传输外发
8） .NET 目标痕迹清理
```

原价899，现在限时只需59元，永久买断！目前已有280+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQoa5OnhetdDKdnd36lG844cFIWNaib1adpRCXOJbRb6mVicfic8tLqXl9Pw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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