---
title: .NET 调用 ShellWindows 执行系统命令
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487333&idx=1&sn=83b01902a6bcf9b736394ea987a6a4db&chksm=fa5aa188cd2d289ec4db2d88690decc915c738cfa9f92a7ea3ee1291ea3c3c7893dab4f8d8de&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2023-03-07
fetch_date: 2025-10-04T08:49:35.262035
---

# .NET 调用 ShellWindows 执行系统命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibBZAjKYozW3KDSw70zMicPCWaJT064ice6vJk4VzwHHiahqa9jpHuaN5UvOn6hm6EfcLKUeVbM0s6fw/0?wx_fmt=jpeg)

# .NET 调用 ShellWindows 执行系统命令

dotNet安全矩阵

# 0x01 基本介绍

.NET调用ShellWindows对象实现命令执行，ShellWindows是Windows Shell的一部分是一个COM对象，可以通过该对象获取当前打开的所有Windows资源管理器窗口，在.NET中，必须添加对SHDocVw库的引用来使用ShellWindows对象

```
添加引用 ->com->MicroSoft Internet Controls
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibBZAjKYozW3KDSw70zMicPC4mb1lp9dbnKr8tJg2U7AAwNggdDd6tBvr7CqVMSBJU20o6YeialrLDw/640?wx_fmt=png)

在使用ShellWindows对象时，可以使用Item方法获取当前打开的所有Windows资源管理器窗口，.NET使用Document对象Application.ShellExecute方法启动计算器，核心代码如下

```
ShellWindows shellWindows = new ShellWindows();            object empty = Type.Missing;            string calculatorPath = "calc.exe";            string args1 = "";            string workDir = "";            shellWindows.Item().Document.Application.ShellExecute(calculatorPath, args1, workDir, "open", 1);
```

运行时成功弹出计算器，欢迎对.NET安全关注和关心的同学加入我们 [dotNet安全矩阵] ，在这里能遇到有情有义的小伙伴，大家聚在一起做一件有意义的事。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibBZAjKYozW3KDSw70zMicPCXxUWdWVTK8zZ9mYlzh96gAia6gF25ia0LmbhxhveFnw7LichXAiaicyia6jA/640?wx_fmt=png)

# 星球优惠活动

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。经过运营团队成员商议一致同意给到师傅们最大优惠力度，**只需99元就可以加入我们。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCkETPR6LWmyhiccY1ufjKmWB9qia1vPukNHnh2Rg5sHFGobrzX0FS1Zd0Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布**很多高质量的.NET**安全资源，可以说市面上很少见，都是干货。其中主题包括**.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库**等等，后续还会倾力打造**专刊、视频**等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibHErRN3IhgSaicia7Rl5SF0plpcuicd0KG8Cn7vGczlBRtvSJvicWejH7TOro6AGLQ627SvVzxzBnphg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58UeoxTMuRezdHEJu6Hp08Xgm2F49cyBI1zlcj5XqLJK8zedWlUjibYmia3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

dotNet安全矩阵知识星球 — 聚焦于微软.NET安全技术，关注基于.NET衍生出的各种红蓝攻防对抗技术、分享内容不限于 .NET代码审计、 最新的.NET漏洞分析、反序列化漏洞研究、有趣的.NET安全Trick、.NET开源软件分享、. NET生态等热点话题、还可以获得阿里、蚂蚁、字节等大厂内推的机会

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