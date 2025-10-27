---
title: .NET内网实战：通过密码喷射遍历域账户
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247498161&idx=1&sn=be37da545ba59c118c2d8331ddebf95e&chksm=fa59575ccd2ede4a649d9a0b0a50098ed73b9a63406c87ad5501b7b911333561666fb79b058a&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-13
fetch_date: 2025-10-06T20:08:55.245853
---

# .NET内网实战：通过密码喷射遍历域账户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8uzUjHD6dMvXQQv5ruZ22d43vFy8IYNEt2oTfqNOGIiaInuGiaicKlwUPZxBU5Y7H5hlpLZMGZmPe4g/0?wx_fmt=jpeg)

# .NET内网实战：通过密码喷射遍历域账户

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过密码喷射技术遍历域账户》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有300+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uzUjHD6dMvXQQv5ruZ22dSvpAV3ia9nSkqDicCJlPwQAv0Jjoa6RS7q2AUueqiaVCbWGGwUe2e2p4Q/640?wx_fmt=png&from=appmsg)

03

原理分析

在内网域渗透测试中，攻击者常常需要评估域环境中的账号密码强度。而密码喷射技术是其中一种高效的方法，通过使用一个已知或猜测的密码，对域内所有用户逐一尝试身份验证，从而快速筛选出使用弱密码的账户。本文介绍的工具基于.NET 实现，通过提供一个已知的密码，能够自动遍历域用户并尝试该密码进行验证，帮助渗透测试人员快速识别域内可能存在的弱密码账户，为后续的横向移动和权限提升打下基础。

## 3.1 NetGetJoinInformation

NetGetJoinInformation 是 Windows 提供的一个 API，用于获取目标计算机的网络加入信息，包括是否加入了域或工作组。该函数在网络管理和开发中非常实用，是许多工具检测计算机网络环境的基础。

```
```
[DllImport("Netapi32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
static extern int NetGetJoinInformation(
    string server,
    out IntPtr domain,
    out NetJoinStatus status
);
```
```

通过 .NET 使用 P/Invoke 调用 NetGetJoinInformation，其中参数 out NetJoinStatus ，输出目标计算机的加入状态.

## 3.2 DirectoryEntry

在 .NET 中 DirectoryEntry 是用于操作 Active Directory 或其他目录服务的类，通常配合 WinNT协议与 域或本地安全账户管理器进行交互，如果要匹配 User，通过调用 SchemaClassName 属性进行判断，具体代码如下所示。

```
```
List<string> userNames = new List<string>();
foreach (DirectoryEntry child in directoryEntry.Children)
{
    if (child.SchemaClassName == "User")
    {
        userNames.Add(child.Name);
    }
}
```
```

## 3.3 LDAP

一般情况下 .NET 可以通过 LDAP:// 常用于用户认证，验证用户名和密码是否在目录服务中有效，具体代码如下所示。

```
```
DirectoryEntry entry = new DirectoryEntry("LDAP://example.com", "username", "password");
bool isAuthenticated = false;
try
{
    object obj = entry.NativeObject; // 触发验证
    isAuthenticated = true;
}
catch (DirectoryServicesCOMException)
{
    isAuthenticated = false;
}
```
```

因此，LDAP:// 是 LDAP 协议访问目录服务的标准 URI 格式，广泛应用于域环境下的用户认证和目录管理。

基于以上知识点，我们使用 .NET 编写一个密码喷射的工具，该工具利用 LDAP 协议在 Windows 域环境中查找用户并尝试使用指定的密码进行身份验证。通过这种方式，可以快速验证域中哪些用户使用了特定的弱密码。

如果域内某些用户的凭据成功验证，工具会在终端中输出对应账户的信息，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8uzUjHD6dMvXQQv5ruZ22d4st3T4SdXAiauVGpYhmbTW8ngXmAnO7icSibEU2oLXISE5LCql3p1NJdg/640?wx_fmt=other&from=appmsg)

综上，本文介绍了一个基于 LDAP 的密码喷射工具，其实现包括域信息获取、用户列举以及身份验证三个核心部分，可以帮助渗透人员快速筛选出域中使用弱密码的用户。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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