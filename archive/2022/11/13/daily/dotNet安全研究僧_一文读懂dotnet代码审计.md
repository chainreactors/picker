---
title: 一文读懂dotnet代码审计
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487044&idx=2&sn=3dcadf153cbeec499206332bae7c8b83&chksm=fa5aa0a9cd2d29bfbb3b8e97217c431e21c877d77d14fabe72ae81a44d345f8b30cc39563d49&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2022-11-13
fetch_date: 2025-10-03T22:38:26.584470
---

# 一文读懂dotnet代码审计

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF68OVKBpZoW0ibrLer59cic35FiaIrVLM9Ff1P7IkWG1hdPBib3JXw2lnMhg/0?wx_fmt=jpeg)

# 一文读懂dotnet代码审计

dotNet安全矩阵

编者荐语：

dotNet矩阵微信群里的黑仔师傅分享了一篇非常精彩的.NET代码审计文章，内容由浅入深，面面俱到！

以下文章来源于攻防日记
，作者黑仔007

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7wjHchQicrOc1zia1vKaPpSJnvF4torSvZuou8MAh3zCVQ/0)

**攻防日记**
.

十年磨一剑，向攻防进军。分享学习心得，知识秘籍，也可闲聊天下趣事，备好佳肴精酿等你！

## 开发模式

目前，ASP.NET中两种主流的开发方式是：ASP.NET Webform和ASP.NET MVC。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6ELdGlCdBGxunSiaNhbq4vpH6JLupKBP0rgJlJS2KIAs9xthQ0PpUJFQ/640?wx_fmt=jpeg)

WebForm开发模式

WebForm模型：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6EWp9e9sNFDy9gOqicFTmmsU5KHsXzMibMgbz9tP0dpk8oxYMYvPpJOuA/640?wx_fmt=jpeg)

aspx负责显示，服务器端的动作就是在aspx.cs定义的，.cs是类文件，公共类神马的就是这个了，.ashx是一般处理程序，主要用于写web handler,可以理解成不会显示的aspx页面，不过效率更高，dll就是编译之后的cs文件。

.aspx文件作为显示页面，通常代码是一些html代码，第一行文件头会显示具体触发功能代码的位置，就可以通过这个位置进行漏洞跟踪。![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6wI7tNXhxdvlLWFwOeXfibDkPwyyvrq3icBo2ibcgceEudricVFdxibMVYlg/640?wx_fmt=jpeg)

我们先打开一个aspx页面，其中：

1、Labguage 表示当前所使用的语言，为C#。

2、AutoEventWireup 指的是是否页面自动事件回传，自动关联处理函数。

3、Inherits 继承于ChargeLogin, App\_Web\_ozdw0ygm。

### MVC开发模式

MVC模型：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6pcufgcKz1wWZHUyHzAYoZG8vbhrjHMibB1ib1Itr1zXCiaPE6IS2EhnRA/640?wx_fmt=jpeg)

M：Model

> 主要是存储或者是处理数据的组件，Model其实是实现业务逻辑层对实体类相应数据库操作，如：CRUD(C:Create/R:Read/U:Update/D:Delete)。它包括数据、验证规则、数据访问和业务逻辑等应用程序信息。

V：View

> 是用户接口层组件，主要是将Model中的数据展示给用户，ASPX和ASCX文件被用来处理视图的职责。

C：Controller

> 用来处理用户交互，从model中获取数据并将数据传给指定的view。

## 拓展名介绍

### 常见后缀

%windir%\Microsoft.NET\Framework\v2.0.50727\CONFIG\web.config中有详细定义，这里提取部分简单介绍。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6iaOB3ZsnasBlYnkezM3wEaZ5U19ZCXOXdq9ToSmsd9jB0AndGERogZA/640?wx_fmt=jpeg)aspx

> 应用程序根目录或子目录
>
> asp.net的文件后缀名，是微软的在服务器端运行的动态网页文件，包含web控件与其他，它是在服务器端靠服务器编译执行的程序代码，可理解为页面显示文件。

cs

> App\_Code 子目录
>
> 类文件，业务逻辑处理层的代码。

aspx.cs

> web窗体后台程序代码文件。

ascx

> 应用程序根目录或子目录
>
> Web用户控件文件，是作为一种封装了特定功能和行为（这两者要被用在Web应用程序的各种页面上）的Web页面被开发的。一个用户控件包含了HTML、代码和其他Web或者用户控件的组合，并在Web服务器上以自己的文件格式保存，其扩展名是\*.ascx。

asmx

> 应用程序根目录或子目录
>
> 是webservice服务程序的后缀名，ASP.NET 使用.asmx 文件来对Web Services的支持。

asax

> 应用程序根目录
>
> 通常是Global.asax。

**Global.asax**

> Global.asax是 ASP.NET 应用程序的中心点，提供全局可用的代码，从HttpApplication基类派生的类，响应的是应用程序级别会话级别事件，通常ASP.NET的全局过滤代码就是在这里面。

config

> 应用程序根目录或子目录
>
> 通常是web.config，Web.config 文件向它们所在的目录和所有子目录提供配置信息。

**web.config**

> web.config是基于XML的文件，可以保存到Web应用程序中的任何目录中，用来储存数据库连接字符、身份安全验证等。
>
> 加载方式：当前目录搜索 -> 上一级到根目录 -> %windir%/Microsoft.NET/Framework/v2.0.50727/CONFIG/web.config -> %windir%/Microsoft.NET/Framework/v2.0.50727/CONFIG/machine.config -> 都不存在返回null。

ashx

> 应用程序根目录或子目录
>
> 一般处理程序，该文件包含实现 IHttpHandler 接口以处理所有传入请求的代码。

soap

> 应用程序根目录或子目录
>
> soap拓展文件，基于XML简单协议。

### ASPX和ASP的区别

asp

> Active Server Pages，是MicroSoft公司开发的服务器端脚本环境，可用来创建动态交互式网页并建立强大的web应用程序，即为动态服务器页面。

.asp是asp的文件后缀名

.aspx是asp.net的文件后缀名

asp.net又叫 asp+ 是动态网络编程的一种设计语言

**ASPX的webshell权限为什么比asp的大？**大概分两个阶段去回答这个问题

阶段一：在IIS6.0 - IIS7.5

> .NET默认的账户是aspnet，隶属于Users，而此时的ASP基于IUSER账户，隶属于Guest组，对于组来说Users组的权限 > Guest组，所以能执行或者读取的资源更多。

阶段二：IIS7.5以后到现在IIS10

> .NET默认的账户是iis apppool\defaultapppool，默认身份为 ApplicationPoolIdentity，而此账户继承了Users组和IIS\_IUSRS组的成员，而ASP同样也是继承于apppool\defaultapppool，返回用户组也和.NET一致。

结论：在老版本的IIS里的确ASPX的webshell权限 > ASP Webshell；新版本的IIS里只要开启了ASP的话，两者的权限一样的，但新版的IIS默认已经关闭了ASP。

## 审计工具

### 反编译

如果遇到的asp.net cms源码包是没有编译成dll的话，那么就方便很多了，可以直接拖入Visual Studioont查看，而更多的是会遇到编译成了dll，这样相对地说就麻烦很多了，不过也有方法。

一、Reflector

可以将dotnet程序集中的中间语言反编译成C#或者Visual Basic代码，除了能将IL转换为C#或Visual Basic以外，Reflector还能够提供程序集中类及其成员的概要信息、提供查看程序集中IL的能力以及提供对第三方插件的支持，比如reflexil。

二、ILSpy、DnSpy

自reflector就开始转收费软件，ILSpy也就应运而生了，它反编译出的代码和reflector差不多。

ILSpy、https://github.com/icsharpcode/ILSpy

DnSpy、https://github.com/dnSpy/dnSpy

找到后端代码，直接将对应的DLL文件拖进来即可。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6LJhHAFeC4TPzSha913v8wibrB1sjzcuMkINyJm6zI09DicaGIiaIt6jiag/640?wx_fmt=jpeg)

**预编译的原理：**

简单的来说，就是在网站发布时将aspx文件进行编译，转换成dll文件。因为.NET程序在运行时会优先加载bin目录下的程序集。

即index.aspx -> /bin/index.dll

在用户访问index.aspx时，则直接由index.dll进行处理。而不是index.aspx。一旦进行预编译后，相关程序会被转换为dll存储在bin目录下。这时候，程序的访问路径和相关逻辑，都被封装成了dll。无论根目录下是否存在index.aspx，都可以正常处理特定路由下的功能。

可参考畅捷通T+任意文件上传(CNVD-2022-60632 )漏洞来理解。

### 小玩意

ListFile、https://github.com/He1za1/ListFile

填写文件后缀和文件路径，筛选出项目里面对应后缀的文件路径，并把结果保存到工具根目录下的result.txt中。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6yy9DcfDujiceaP6df1guGPoSbUobGC83Vor2Xr5q4wRKbBbvsHlYAOA/640?wx_fmt=jpeg)

用命令也可以实现，dir /s /b \*.aspx。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF60AxicJrfDib7miaTeb2kz92zsZgbtMTwsgXvnicQ0uJ15Lkuhqf0FHWbBw/640?wx_fmt=jpeg)

dirscan、https://github.com/safe6Sec/dirScan

图形化的目录扫描工具之一，可结合ListFile的筛选结果进行目录爆破，从而快速的找出可未授权访问的页面。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6nJdxf2dEt5sko12OE7icsbnXhFTRJxtfD9XPvS8wCcvEC3fTWT7S73g/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6qwUW5Nstsn804qs1g4bSqAd7kODruKls9RfgIezFm6YCibKoicZoWiciaQ/640?wx_fmt=jpeg)

sublime、http://www.sublimetext.com/

如果不想下visual studio，可以用这个，一款轻量级的代码编辑器。将反编译后的源码直接拖入进去即可。

### 反混淆

de4dot、https://github.com/de4dot/de4dot

反混淆的工具有很多，其中de4dot是目前最主流的反混淆工具。

检测混淆器类型

> de4dot.exe -d f:\bin\h1z1.dll

批量反混淆

> de4dot.exe -r c:\input -ru -ro c:\output

## 漏洞案例

### 任意文件上传

WebForm，通过class定位到后端业务处理处进行审计。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF64R5FKjCJlibZv1NL5S1YsEZkxnyDjfbh1mJcQnpcsiatcMjIMCXyKTMg/640?wx_fmt=jpeg)

无后缀校验，经典的路径+时间+文件名拼接。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6LJhHAFeC4TPzSha913v8wibrB1sjzcuMkINyJm6zI09DicaGIiaIt6jiag/640?wx_fmt=jpeg)

漏洞验证。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6psta3hoRk18YFMk7mlOQpsJsAiaeBIMbOnTqSPUXah3xsGibvYchHibeg/640?wx_fmt=jpeg)

代码审计关注点：

```
saveas()
```

### 任意文件下载

MVC，发现存在下载函数。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6iaRUroHqwLOh4bCq7XDbzu9Yk5WYKLkqOwAqkSXlBYaURtctSSYpuMg/640?wx_fmt=jpeg)

跟进，文件路径拼接处未做过滤，可造成任意下载。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6O38jxMWlH9uSgibhWsrZZlwC90ZcnTftK2A1ZiaFt5dFQrINDhibNKlkA/640?wx_fmt=jpeg)

漏洞验证。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6GNcbeullO1jDzF7Cq87NuzLY4pWq73lNTKXf7hYRUyjsy6koiaf5zNw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6eoQcjNl2Cw5pVdQbkLQScP9cMKibia1yjYnvfabhzm4SZr0Rot5EHDbQ/640?wx_fmt=jpeg)

代码审计关注点：

```
1. File对象的 OpenText和OpenRead方法
2. FileStream对象的FileMode.Open和FileMode.Read
3. Response.WriteFile 常用于文件下载
```

### SQL注入漏洞

MVC，发现存在数据交互。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6Ov767vhU73geMMvicvQ70JMfGibU8NU1zJYkQyOFasVox0X7UIdGlib9w/640?wx_fmt=jpeg)

跟进，存在SQL语句拼接，且不存在预编译SQL parameter和其他过滤，可造成SQL注入漏洞。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6lMJyGuiaPU6rPibKahbH47iaVPmkedJXMj6JyFaGPXULIN4sNPpODNbPA/640?wx_fmt=jpeg)

漏洞验证。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibyhXPNOCerMoj2Ub2Y7hChxkMVVwLeF6ibfvmtpFVOw1Q9l44t63rnibJCSnDQRzOeadaD6ZhaptXzAjKwuianiauw/640?wx_fmt=jpeg)

代码审计关注点：

SQL语句拼接处。

### XSS

在asp.net中我们插入XSS代码经常会遇到一个错误`A potentially dangerous Request.Form`这是因为在`aspx`文件头一般会定义一句`<%@ Page validateRequest="true" %>` 。

```
<%@ Page Language="C#" ValidateRequest="true" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication13.WebForm1" %>
```

当然也可以在`web.config`中定义，值得注意的是`validateRequest`的值默认为`true` ,所以通常情况下asp.net很少存在`XSS`的,除非程序员把他的值改变。

```
<system.web>
    <pages validateRequest="true"></pages>
    <httpRuntime requestValidationMode="2.0"/>
</stytem.web>
```

### 未授权访问

AuthorizeAttribute

一、AuthorizeAttribute是asp.net MVC的几大过滤器之一，俗称认证和授权过滤器，也就是判断登录与否，授权与否。当为某一个Controller或Action附加该特性时，没有登录或授权的账户是不能访问这些Controller或...