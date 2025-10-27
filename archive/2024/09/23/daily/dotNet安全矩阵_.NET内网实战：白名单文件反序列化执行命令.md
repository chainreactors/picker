---
title: .NET内网实战：白名单文件反序列化执行命令
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495443&idx=1&sn=800a2199213b472937733ba58c1b1a2b&chksm=fa5941fecd2ec8e828d2defdfa0ff28920bb54b67698386488437c031f98b2770ad132ccff64&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-09-23
fetch_date: 2025-10-06T18:24:36.335486
---

# .NET内网实战：白名单文件反序列化执行命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8P8gy09FzIjLrrsDjBHVoF7vQ3WdgOBdibmVnRMBZNCszGrADE2ia4YD0beowZo7KicuDWs2g1UXzWw/0?wx_fmt=jpeg)

# .NET内网实战：白名单文件反序列化执行命令

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 白名单文件通过反序列化执行命令》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有200+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8P8gy09FzIjLrrsDjBHVoFaFB83WuRtBomOsyeXX7JWDYuYq9alqdBoJ4jzEw75jpFNicMvATCl7w/640?wx_fmt=png&from=appmsg)

03

原理分析

VisualUiaVerifyNative是一款具备微软白名单的可执行文件，用于基于Microsoft UI Automation框架进行应用测试。然而，通过对其配置文件的精心操作，攻击者可以非法使用其功能来触发反序列化漏洞，执行任意代码。VisualUiaVerifyNative.exe通常依赖于以下两个重要的动态链接库。

## 3.1 UIAComWrapper.dll

UIAComWrapper.dll，该 DLL 文件封装了 UI Automation COM 接口，用于简化与 UI Automation 元素的交互。

## 3.2 WUIATestLibrary.dll

另外，WUIATestLibrary.dll 提供了一些专门用于 UI 自动化测试的库函数，主要支持自动化测试中的通用任务，例如自动化 UI 控件的查找、状态验证和操作。

这些依赖库的主要作用是为 VisualUIAVerifyNative.exe 提供接口和功能支持，使其能够与 Windows 应用程序的 UI 自动化框架进行通信，并通过自动化的方式验证和测试界面元素。

## 3.3 反编译

使用dnspy打开VisualUiaVerifyNative文件的入口方法Main，发现调用了MainWindow类，MainWindow类的初始化方法中，有一个至关重要的函数ApplicationStateDeserialize负责反序列化配置文件中的数据。如下图所示

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8P8gy09FzIjLrrsDjBHVoFsFWbnZJQfJC2L2S2xbciaK0Jm7PyekANGEdLomKrPicrrJWpAchzH8wQ/640?wx_fmt=other&from=appmsg)

进入此方法内部，发现打开读取了一个名为uiverify.config的文件，位于用户的AppData目录中，代码如下所示

```
```
private void ApplicationStateDeserialize()
{
    this._configFile = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + "uiverify.config";
    if (File.Exists(this._configFile))
    {
        Stream stream = File.Open(this._configFile, FileMode.Open);
        BinaryFormatter binaryFormatter = new BinaryFormatter();
        this._applicationState = (ApplicationState)binaryFormatter.Deserialize(stream);
        stream.Close();
    }
}
```
```

最核心的是调用了BinaryFormatter类反序列化内容，攻击者可以通过精心构造的payload欺骗反序列化过程，加载恶意代码

04

实战利用

使用ysoserial.exe工具生成一个恶意的序列化payload，这会生成一个二进制格式的恶意payload，并将其保存为Roaminguiverify.config文件，内容如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8P8gy09FzIjLrrsDjBHVoFgl5KAVShkkuWMzoN9xIsYyvicqww8XqeEc3ribb6DGCsESQsRoBFDHOw/640?wx_fmt=other&from=appmsg)

将生成的Roaminguiverify.config文件写入到当前用户目录，比如C:\Users\Administrator\AppData\Roaminguiverify.config。这个配置文件是VisualUiaVerifyNative在启动时会自动读取的文件，触发命令执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8P8gy09FzIjLrrsDjBHVoFriaUVbEWFiab86pgxn5fqyT9o17wxOdjIGxsFlUP40jXgicAFbjV2uJ7A/640?wx_fmt=other&from=appmsg)

综上，在日常的红队行动中，利用微软签名的白名单文件来绕过防护措施是一种常见的行为，有些场景下红队通过利用系统白名单文件加载反序列化漏洞的方式执行恶意指令。想要了解完整或者更多的内网安全防御绕过方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

05

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

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8g70WSk5ibViagFgQ8Sj8tUmOzzGX6ic8Cs2icOPBHibOcQLqsC73tF9H9cl8JkU0DIOYj6hXicXyCfoeg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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