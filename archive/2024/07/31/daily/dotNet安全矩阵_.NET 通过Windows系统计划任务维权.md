---
title: .NET 通过Windows系统计划任务维权
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493717&idx=3&sn=a366c9b6c90a11ffda25715fe803e36d&chksm=fa5946b8cd2ecfae198da4db4a43e6e2a3f54b4ac2237ccb9f0666a3d17fd8e17af5d79c56d2&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-07-31
fetch_date: 2025-10-06T17:44:05.176136
---

# .NET 通过Windows系统计划任务维权

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibjDoJXgdgG8lsrfjTNicZicEfhffjXud1K8beJXkzsHKaP2g6a6ibWicY1oplkpUNZlOu4iav2y3L5qfA/0?wx_fmt=jpeg)

# .NET 通过Windows系统计划任务维权

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过Windows系统计划实现权限维持》，完整的文章内容请加入小报童后订阅查看。现在限时只需49元，永久买断！目前已有100+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibjDoJXgdgG8lsrfjTNicZicEJ9ibQibsI8mzfusKPubibGdxaibBkuvfgScvBRfFzyCibiatwmzTx3RqickkA/640?wx_fmt=png&from=appmsg)

03

编码实现

在渗透测试或恶意软件开发中，攻击者经常需要在目标系统上维持持久的访问权限，Windows计划任务是实现这一目标的有效工具之一，因为它允许攻击者在特定时间或事件触发时执行预定义的命令或脚本。下面，我们将详细介绍如何通过Windows计划任务来维持权限。

## 3.1 连接任务管理器

Windows 任务计划程序 (Task Scheduler) 的 CLSID标识符是 0F87369F-A4E5-4CFC-BD3E-73E6154572DD，这串CLSID可以在taskschd.h文件中找到，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibjDoJXgdgG8lsrfjTNicZicErkImbHgQPFAvC0XQzLP3giaaesZER2t4PODczYOdc6iarZyoJ47kRiaibQ/640?wx_fmt=other&from=appmsg)

在.NET中使用 new Guid("0F87369F-A4E5-4CFC-BD3E-73E6154572DD") 创建该 CLSID 的 GUID 对象，接着通过 Activator.CreateInstance 方法创建该 Type 的对象，具体代码如下所示。

```
TaskScheduler taskScheduler = (TaskScheduler)Activator.CreateInstance(Type.GetTypeFromCLSID(new Guid("0F87369F-A4E5-4CFC-BD3E-73E6154572DD")));
try
{
    taskScheduler.Connect(Type.Missing, Type.Missing, Type.Missing, Type.Missing);
}
```

然后尝试通过 taskScheduler.Connect 方法连接Windows系统任务调度管理器。

## 3.2 配置系统计划任务

首先调用taskScheduler.NewTask 方法创建一个新的计划任务定义接口 ITaskDefinition，代码如下所示。

```
ITaskDefinition taskDefinition = taskScheduler.NewTask(0U);
taskDefinition.RegistrationInfo.Author = author;
taskDefinition.RegistrationInfo.Description = description;
taskDefinition.Settings.RunOnlyIfIdle = false;
```

高级部分涉及配置计划任务触发器、任务执行等，触发器是任务计划的重要组成部分，决定了任务在什么时间和条件下被触发，比如定义每小时触发器 (hourly)，具体如下所示

```
if (triggertype.ToLower() == "hourly")
{
    string interval = string.Format("PT{0}H", rep);
    ITimeTrigger timeTrigger = (ITimeTrigger)taskDefinition.Triggers.Create(_TASK_TRIGGER_TYPE2.TASK_TRIGGER_TIME);
    timeTrigger.Id = "TimeTrigger";
    timeTrigger.Repetition.Interval = interval;
    timeTrigger.StartBoundary = startBoundary;
}
```

## 3.3 执行系统计划任务

计划任务被触发后会执行一系列动作，这也是任务计划中的关键部分，通过 ITaskDefinition.Actions 属性的Create方法创建一个指定的动作类型，execAction.Path 设置要执行的.exe文件完整路径，Arguments 设置传递给程序的命令行参数。最后通过 folder.RegisterTaskDefinition 完成自定义计划任务在Windows系统的注册，核心代码如下所示。

```
IExecAction execAction = (IExecAction)taskDefinition.Actions.Create(_TASK_ACTION_TYPE.TASK_ACTION_EXEC);
execAction.Id = "ExecAction";
execAction.Path = path;
execAction.Arguments = arguments;
```

利用Windows计划任务是一种常见且有效的方法。通过创建和配置计划任务，攻击者可以在特定时间或事件触发时自动执行预定义的命令或脚本，从而实现持久化。想要了解更多内网权限维持的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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

原价899，现在限时只需49元，永久买断！目前已有100+位朋友抢先预定，我们会长期更新，初步计划保持每周更新1-2篇新内容，对.NET内网安全的朋友们请尽快订阅该报刊！![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibeicvDNVldcXTgRnFUFTwOqfTleogJThU7kCaZJuuU2BLVLYluu6CFV7BX458AxBcd93ickZ0rmOqQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

每增加五十人涨价10元，抓紧订阅，超值！订阅后请关注公众号：dotNet安全矩阵，发送订单截图和您的微信号，邀请您加入专属交流群。感兴趣的朋友，可以点击链接：https://xiaobot.net/p/dotNetAttack，或者扫描下方海报微信二维码加入即可，订阅后小报童定时会将最新内容通过微信推送给您。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8MlqPfO4GcwJSzf4KqIychkMYp15fE5lQT6B6SibSFztMNaz2Wc9qolUQQe4N76V0wiapfLkGMWbsg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

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