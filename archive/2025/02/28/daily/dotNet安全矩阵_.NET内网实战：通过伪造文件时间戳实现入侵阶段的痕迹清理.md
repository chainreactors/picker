---
title: .NET内网实战：通过伪造文件时间戳实现入侵阶段的痕迹清理
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247499017&idx=2&sn=121df4bae602a09c7584447b778948d6&chksm=fa5953e4cd2edaf2c82f63e9ae6590e0c96abf05b7bfa471754ca1632322a6820fd0e9daf797&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-28
fetch_date: 2025-10-06T20:38:25.394109
---

# .NET内网实战：通过伪造文件时间戳实现入侵阶段的痕迹清理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9JnlUI4jslmCDOJtPib7lWRrR5ChCm8DqUaw3LIXRKInUDgXJXy7HecCZYrkdwxdx2XxHJFdQgmwQ/0?wx_fmt=jpeg)

# .NET内网实战：通过伪造文件时间戳实现入侵阶段的痕迹清理

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过伪造文件时间戳实现痕迹清理》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有300+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

03

原理分析

Sysnative 路径是Windows操作系统中一个非常有用的特性，解决了32位应用程序在64位系统中访问系统目录时的路径重定向问题。通过利用这一特性，红队渗透时可以实现一些新的功能和绕过防御，如启动64位CMD等。

## 3.1 基本介绍

CreateFile 函数通常用于在 Windows 系统中创建或打开文件、设备或管道。该函数从 kernel32.dll 库中导入.NET，具体函数的声明如下所示。

```
```
[DllImport("kernel32.dll", SetLastError = true)]
public static extern IntPtr CreateFile(
    string lpFileName,          // 文件路径
    int dwDesiredAccess,        // 访问权限
    int dwShareMode,            // 共享模式
    IntPtr securityAttrs,       // 安全属性
    int dwCreationDisposition,  // 创建方式
    int dwFlagsAndAttributes,   // 文件属性
    IntPtr hTemplateFile        // 模板文件句柄
);
```
```

在 Windows API 中，CreateFile 函数不仅用于创建文件，也可以用于打开现有文件并返回文件句柄，以便后续进行读写操作。具体的例子如下，通过使用 CreateFile 函数打开一个已存在的文件，并获取文件句柄。

```
```
class Program
{
    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern IntPtr CreateFile(
        string lpFileName,
        int dwDesiredAccess,
        int dwShareMode,
        IntPtr securityAttrs,
        int dwCreationDisposition,
        int dwFlagsAndAttributes,
        IntPtr hTemplateFile);
    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern bool CloseHandle(IntPtr hObject);
    static void Main()
    {
        string filePath = "C:\\example.txt";
        if (!File.Exists(filePath))
        {
            File.WriteAllText(filePath, "这是一个测试文件。");
        }
        IntPtr hFile = CreateFile(
            filePath,               // 文件路径
            GENERIC_READ,           // 只读权限
            FILE_SHARE_READ,
            IntPtr.Zero,
            OPEN_EXISTING,
            FILE_ATTRIBUTE_NORMAL,
            IntPtr.Zero
        );
        if (hFile  IntPtr.Zero || hFile  new IntPtr(-1))
        {
            int errorCode = Marshal.GetLastWin32Error();
            Console.WriteLine($"打开文件失败，错误码：{errorCode}");
        }
        else
        {
            Console.WriteLine("文件句柄已成功获取！");
            CloseHandle(hFile);
            Console.WriteLine("文件句柄已关闭。");
        }
    }
}
```
```

## 3.2 SetFileTime

SetFileTime 函数是 Windows API 中用于修改文件时间戳的函数。它允许你设置文件的创建时间、最后访问时间和最后写入时间。通过修改这些时间戳，可以改变文件在系统中的时间标记。该函数在.NET里的调用方式如下所示。

```
```
[DllImport("kernel32.dll", SetLastError = true)]
public static extern bool SetFileTime(
    IntPtr hFile,                // 文件句柄
    ref long lpCreationTime,     // 文件创建时间
    ref long lpLastAccessTime,   // 最后访问时间
    ref long lpLastWriteTime     // 最后写入时间
);
```
```

hFile (IntPtr)：文件句柄，表示要修改时间戳的文件。通常通过调用 CreateFile 函数获取该句柄。lpCreationTime、lpLastAccessTime、lpLastWriteTime 分别代表文件的创建时间和 文件最后的访问时间、以及 文件的最后写入时间，这三个时间戳都是传入同样的 64 位时间戳。

## 3.3 编码实现

攻击者可以通过 CreateFile 打开文件，获取文件句柄，然后使用 SetFileTime 来修改文件的时间戳，从而达到隐藏和清理入侵的痕迹，具体代码如下所示。

```
```
        long num5 = Date.ToFileTime();  // 将指定的时间（Date）转换为文件时间戳
        long num6 = 0L;  // 默认值为零，表示不修改某些时间戳
        // 如果没有指定需要修改的时间戳，则设置所有时间戳为相同的时间
        if (!CreateTime && !AccessTime && !WriteTime)
        {
            result = Mace.SetFileTime(intPtr, ref num5, ref num5, ref num5);  // 修改所有时间戳为指定时间
        }
        else
        {

            if (CreateTime && !AccessTime && !WriteTime)
            {
                result = Mace.SetFileTime(intPtr, ref num5, ref num6, ref num6);

            }
            if (CreateTime && AccessTime && !WriteTime)
            {
                result = Mace.SetFileTime(intPtr, ref num5, ref num5, ref num6);

            }
            if (CreateTime && !AccessTime && WriteTime)
            {
                result = Mace.SetFileTime(intPtr, ref num5, ref num6, ref num5);

            }
            if (!CreateTime && AccessTime && !WriteTime)
            {
                result = Mace.SetFileTime(intPtr, ref num6, ref num5, ref num6);

            }
            if (!CreateTime && AccessTime && WriteTime)
            {
                result = Mace.SetFileTime(intPtr, ref num6, ref num5, ref num5);
            }
            if (!CreateTime && !AccessTime && WriteTime)
            {
                result = Mace.SetFileTime(intPtr, ref num6, ref num6, ref num5);

            }
```
```

比如执行命令 Sharp4ModifyTime.exe -s 23.txt -t "2019-02-19 01:01:01"

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9JnlUI4jslmCDOJtPib7lWRSBjib9icRsnZKB2L90xVhl7k5N6xMKDgZFJAyyiaRFpADvRdTWK0lPRfQ/640?wx_fmt=other&from=appmsg)

可以将文件23.txt 时间戳全部伪造成 2019-02-19 01:01:01，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9JnlUI4jslmCDOJtPib7lWR2iawHOXqFffqFqzqk1rLrvHKeqODZVh20P4vaKibDgOuN4FCrpRsB4iag/640?wx_fmt=other&from=appmsg)

综上，伪造文件时间戳是一个非常强大的攻击技术，尤其是在攻击者需要掩盖入侵痕迹时。通过巧妙地修改文件的创建时间、最后访问时间和最后写入时间，攻击者能够有效规避安全监测和日志审计。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

04

**欢迎加入.NET 电子报刊**

我们的小报童电子报刊【.NET内网安全攻防】也开始运营，引入小报童也是为了弥补知识星球对于轻量级阅读支持的不足，为用户读者提供更佳的阅读体验。如果您对阅读体验的需求比较高，那么可以订阅这个专栏。

本次电子报刊《.NET 内网安全攻防》专栏，内容主要有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，可细分为以下8个方向。

```
1） .NET 安全防御绕过
2） .NET 本地权限提升
3） .NET 内网信息收集
4） .NET 内网代理通道
5） .NET 内网横向移动
6） .NET 目标权限维持
7） .NET 数据传输外发
8） .NET 目标痕迹清理
```

原价899，现在限时只需59元，永久买断！目前已有280+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibXibiaRyFPI439dFybReKxQoa5OnhetdDKdnd36lG844cFIWNaib1adpRCXOJbRb6mVicfic8tLqXl9Pw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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