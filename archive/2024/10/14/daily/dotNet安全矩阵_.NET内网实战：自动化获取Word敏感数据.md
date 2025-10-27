---
title: .NET内网实战：自动化获取Word敏感数据
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495959&idx=1&sn=11d922eb661e8aaa47dc8b40beaf6aae&chksm=fa595ffacd2ed6ecaec64ea45c979114cc7df43a5f45ba6a12f52e0fe980f3ad42a892017864&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-10-14
fetch_date: 2025-10-06T18:47:36.147270
---

# .NET内网实战：自动化获取Word敏感数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8De2ujr3AvrgZIkWAc9xpA1c79COPyYic3CTKLSgdm2mfxK4vXIiajuTVnW29XV7VhEYJaAyUjnh1A/0?wx_fmt=jpeg)

# .NET内网实战：自动化获取Word敏感数据

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过第三方库批量读取Word敏感数据》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有220+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8De2ujr3AvrgZIkWAc9xpAyHWpiaUGP7Kyqa8hYWR3t1qOrmvHMiaFSecXyJrYb63ClQIkpVicNcnpw/640?wx_fmt=png&from=appmsg)

03

原理分析

在 Windows 操作系统中，借助 Microsoft.Office.Interop.Word 和 Marshal.GetActiveObject，红队可以自动化地读取 Microsoft Word 文档内容，使红队能够快速批量提取信息，迅速识别文档中的敏感数据。

## 3.1 Microsoft.Office.Interop.Word

Microsoft.Office.Interop.Word 是一个用于与 Microsoft Word 进行交互的 .NET 开源的第三方库，我们可以通过代码控制 Word 应用程序，比如读取文档内容、处理表格、插入图片等。打开文档读取内容具体实现代码如下所示。

```
```
doc = wordApp.Documents.Open(@"C:\document.docx");
string text = doc.Content.Text;
Console.WriteLine(text);
```
```

## 3.2 Marshal.GetActiveObject

Marshal.GetActiveObject 方法属于 System.Runtime.InteropServices 命名空间。用于获取当前运行的 COM 对象的实例，特别是在与 Office 应用程序（如 Word、Excel 等）进行交互时非常有用。下面是一个简单的示例，展示如何使用 Marshal.GetActiveObject 获取当前运行的 Word 应用程序实例

```
```
try
{
   wordApp = (Application)Marshal.GetActiveObject("Word.Application");
   Console.WriteLine("running.");
}
```
```

## 3.3 批量读取Word敏感数据

首先，判断当前系统中Word 应用程序的状态，如果正在运行就使用Marshal.GetActiveObject("Word.Application") 获取当前活动的 Word 对象，具体代码如下所示。

```
```
bool isWordRunning = IsProcessRunning("winword");
bool isWordOpen = false;
bool isDocOpen = false;
bool isPWprotected = false;
if (isWordRunning)
{
    wordApp = (Application)Marshal.GetActiveObject("Word.Application");
    if (wordApp == null)
    {
        throw new Exception("Failed");
    }
    wordApp.DisplayAlerts = WdAlertLevel.wdAlertsNone;
    isWordOpen = true;
}
```
```

随后，检查指定的 Word 文档是否已经在 Word 应用程序中打开，如果未打开，则将其以只读模式打开并读取文档内容。以只读模式打开文档，并将 Visible 参数设置为 false， 这样Word 应用程序不会在用户界面上显示。然后，通过doc.Content.Text;获取文档的全部文本内容，并存储在 content 变量中。

```
```
string content = doc.Content.Text;
DateTime date = DateTime.Now;
Console.WriteLine("\n" + date + ": " + "Reading Document: " + docName + "\n\n");
Console.WriteLine("File Content:");
Console.WriteLine(content);
```
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8De2ujr3AvrgZIkWAc9xpAGVQStULgdoaF0z9PgXjxqa0HbJlppMyZSp2ylBXfMyQV3soYu8Tubg/640?wx_fmt=other&from=appmsg)

综上，这种实现方式非常适合在红队活动或信息收集任务中使用，能够有效地批量读取和处理 Word 文档，而不干扰用户界面或引起安全警觉。想要了解完整或者更多的内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

原价899，现在限时只需59元，永久买断！目前已有200+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibTRic7PgrT4472YFHDrrOLlcTgKtwgm9cngTJDUib6AO9siaC7WXl6f8Jk1QZbYcib76QcIOBTicMDRhQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

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