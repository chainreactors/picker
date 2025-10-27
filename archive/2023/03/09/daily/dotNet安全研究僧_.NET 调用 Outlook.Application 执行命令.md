---
title: .NET 调用 Outlook.Application 执行命令
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487347&idx=1&sn=9ee2620467cb6613f54509b08f56ddb2&chksm=fa5aa19ecd2d2888c6c180556898ac9b7fb31cf38775497d9250ce9f969cc55a258aec85e4eb&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2023-03-09
fetch_date: 2025-10-04T09:02:11.290691
---

# .NET 调用 Outlook.Application 执行命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibMO6KIPianauTEAGzZ7J7WvVAN7CUtKXNClHrPqBtCVdjgEELDrsFygTn0YbjxGd0250meQVAgJ0w/0?wx_fmt=jpeg)

# .NET 调用 Outlook.Application 执行命令

专攻.NET安全的

dotNet安全矩阵

# 0x01 基本介绍

Outlook.Application对象是Microsoft Outlook的COM对象模型中的一个对象，可用于在.NET中编写Outlook插件或自动化Outlook。该对象表示Outlook应用程序本身，并提供了一组属性和方法，用于管理Outlook中的各种对象，通过Outlook.Application对象，您可以创建、读取、发送和管理电子邮件、安排会议、创建联系人等。以下是Outlook.Application对象的常用属性和方法：

```
Application.ActiveExplorer: 返回当前活动的资源管理器对象。Application.ActiveInspector: 返回当前活动的Inspctor对象。Application.CreateItem: 创建并返回一个新的邮件、联系人、任务、约会等项目。Application.GetNamespace: 获取指定名称空间的Namespace对象。Application.Session: 返回表示当前Outlook会话的Namespace对象。Application.Quit: 退出Outlook应用程序。
```

在使用Outlook.Application对象之前，您需要先在.NET项目中添加对Outlook的引用。可以通过“添加引用”对话框中的“COM”选项卡中选择“Microsoft Outlook 15.0 Object Library”来添加对Outlook 的引用

```
using Outlook = Microsoft.Office.Interop.Outlook;
```

# 0x02 实战演示

自.NET调用Outlook对象实现命令执行，前提需要目标主机上安装了Outlook，使用Outlook.Application对象的CreateObject方法创建Shell.Application对象，将calc作为参数传递给ShellExecute方法，并使用shellObj对象的InvokeMember方法调用ShellExecute方法，代码如下

```
Outlook.Application outlookApp = new Outlook.Application();object shellObj = outlookApp.CreateObject("Shell.Application");object[] shellArgs = { "calc.exe" };shellObj.GetType().InvokeMember("ShellExecute", System.Reflection.BindingFlags.InvokeMethod, null, shellObj, shellArgs);
```

需要注意的是由于Outlook.Application对象和Shell.Application对象都是COM对象，因此在使用它们时需要小心处理COM互操作方面的问题，所以在上面的代码中，我们使用了反射技术来调用Shell.Application对象的ShellExecute方法。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibMO6KIPianauTEAGzZ7J7WvtjC6aXtM6MaTxlzSHhGaNpuSZuDxh7ol1x0ibdOicZNKS8ptqcRWsBOg/640?wx_fmt=png)

# 星球优惠活动

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。经过运营团队成员商议一致同意给到师傅们最大优惠力度，**只需99元就可以加入我们。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCkETPR6LWmyhiccY1ufjKmWB9qia1vPukNHnh2Rg5sHFGobrzX0FS1Zd0Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布**很多高质量的.NET**安全资源，可以说市面上很少见，都是干货。其中主题包括**.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库**等等，后续还会倾力打造**专刊、视频**等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibHErRN3IhgSaicia7Rl5SF0plpcuicd0KG8Cn7vGczlBRtvSJvicWejH7TOro6AGLQ627SvVzxzBnphg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

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