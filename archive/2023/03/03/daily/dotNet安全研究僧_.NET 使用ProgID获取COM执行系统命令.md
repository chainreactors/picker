---
title: .NET 使用ProgID获取COM执行系统命令
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487316&idx=1&sn=db187461970b1e00cf975644314e75ef&chksm=fa5aa1b9cd2d28af1b24295ef8e4d3f869048b77e68793689e3c78bcfefed2e33df7e4e2ec38&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2023-03-03
fetch_date: 2025-10-04T08:32:26.391237
---

# .NET 使用ProgID获取COM执行系统命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicCeNn6cjToicGbSOoocDae1v01PQ064rg4egFIw5Jm1TdK7jX6jrX45JerglVzobkoKwIqMCqSCGA/0?wx_fmt=jpeg)

# .NET 使用ProgID获取COM执行系统命令

专攻.NET安全的

dotNet安全矩阵

# 0x01 基本介绍

.NET Type.GetTypeFromProgID方法，用于获取指定的COM组件类型，其参数是一个ProgID字符串。ProID是一个字符串，它被用于标识COM组件，通过它可获取对代表COM对象类型的Type对象的引用，Activator.CreateInstance(),使用与指定参数匹配程度最高的构造函数创建指定类型的实例。实际使用中通常用于后期绑定，即在运行时动态地创建和使用COM组件对象。这种方式可以使得程序更加灵活，因为可以根据运行时环境来决定要使用哪些组件。例如如下demo:

```
Type shellType = Type.GetTypeFromProgID("Shell.Application");dynamic shell = Activator.CreateInstance(shellType);string calculatorPath = Environment.GetFolderPath(Environment.SpecialFolder.System) + @"\calc.exe";shell.ShellExecute(calculatorPath);
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicCeNn6cjToicGbSOoocDae1W4Fa3O37SEIAFCZNrTsyB7OnByibgj6CGics8CZEKgTbsKxpkSlXHQoA/640?wx_fmt=png)

# 0x02 Webshell

文章涉及的工具和PDF已打包发布在星球，有需要的师傅可以自取。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicCeNn6cjToicGbSOoocDae1iasuWlqGbhu00gGedZ5yKDaDEKicbZEywib7OAnRvUDZy0cqiaBoVMNsqQ/640?wx_fmt=jpeg)

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