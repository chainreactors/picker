---
title: .NET内网实战：通过命令行解密Web.config
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247495187&idx=2&sn=63bad28593263dea2da29d9d85373ebb&chksm=fa5940fecd2ec9e89421ffdb3bb804f49e10b183219b162ed4e195ff03749311cfeef67a265b&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-09-11
fetch_date: 2025-10-06T18:29:09.656060
---

# .NET内网实战：通过命令行解密Web.config

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibsLjwvQpNLiaEqdiaaXwjuJUmVGY6VpsyyAcibQYrQQtSLUEpbvC4DqibOL8LXQj308oibKBRQxp2qBvQ/0?wx_fmt=jpeg)

# .NET内网实战：通过命令行解密Web.config

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所节选自小报童《.NET 内网实战攻防》专栏，主要内容有.NET在各个内网渗透阶段与Windows系统交互的方式和技巧，对内网和后渗透感兴趣的朋友们可以订阅该电子报刊，解锁更多的报刊内容。

02

基本介绍

本文内容部分节选自小报童《.NET 通过命令行解密Web.config配置》，完整的文章内容请加入小报童后订阅查看。现在限时只需59元，永久买断！目前已有200+位朋友抢先预定，我们会长期更新，对.NET内网安全的朋友们请尽快订阅该报刊！

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9bfMNaqibVEP7KnYc1PEZoXhHPzFbzL5Ark0eEDur6M0T6lZDJL35bVreUItS1lIlu7QmosLbPcjw/640?wx_fmt=png&from=appmsg)

03

编码实现

在.NET应用系统中，保护数据库连接字符串的安全性至关重要。.NET 提供了一种通过 DataProtectionConfigurationProvider 加密连接字符串的方法，以防止敏感数据泄露。然而，在内网信息收集阶段，攻击者只需在目标主机上运行aspnet\_regiis.exe这个命令行工具即可完成解密，获取数据库连接的明文字符串。

## 3.1 aspnet\_regiis是什么

aspnet\_regiis.exe 是一个命令行工具，用于配置和管理 .NET 应用程序在 IIS 中的注册和设置。该工具通常与 .NET 版本一起安装，用于执行各种与 ASP.NET 配置相关的任务。

使用 aspnet\_regiis 工具将特定版本的 ASP.NET 注册到 IIS 上，确保 .NET 应用程序可以在该版本上运行，注册命令如下所示：

```
aspnet_regiis -i
```

## 3.2 .NET加解密提供器

DataProtectionConfigurationProvider 是 .NET Framework 2.0 引入的默认加密提供程序之一，主要用于在单台服务器上加密和解密配置文件数据。原理上使用 Windows Data Protection API (DPAPI) 进行加密，这意味着加密数据与操作系统的用户或机器密钥绑定。只有加密时使用的同一用户帐户或同一台机器才能解密数据。假设在 web.config 中有一个连接字符串如下所示。

```
<connectionStrings>
  <add name="MyDb" connectionString="Data Source=myServer;Initial Catalog=myDb;User ID=myUser;Password=myPass;" providerName="System.Data.SqlClient" />
</connectionStrings>
```

使用aspnet\_regiis.exe进行加密数据库连接字符串的命令如下所示。

```
aspnet_regiis -pef "connectionStrings" "C:\path\to\your\project" -prov "DataProtectionConfigurationProvider"
```

加密后，内容将被替换成如下所示。

```
<connectionStrings configProtectionProvider="DataProtectionConfigurationProvider">
  <EncryptedData>
    <CipherData>
        <CipherValue>AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAnu1l5eTFekKy...</CipherValue>
    </CipherData>
  </EncryptedData>
</connectionStrings>
```

解密连接字符串的命令如下所示。因此，这种加密方式适用于单台服务器环境下的配置文件保护，不适合在多个服务器之间共享加密的数据。密钥由 Windows 操作系统管理，不需要额外的密钥管理。

```
aspnet_regiis -pdf "connectionStrings" "C:\path\to\your\project"
```

## 3.3 技术实现

该工具首先会将站点根目录下的 web.config 文件复制到一个新创建的 dotNetMatrix 目录中，以防止直接操作原始配置文件导致意外损坏，具体代码如下所示。

```
string webConfigPath = Path.Combine(exeDirectory, "web.config");
string targetDirectory = Path.Combine(exeDirectory, "dotNetMatrix");
string targetWebConfigPath = Path.Combine(targetDirectory, "web.config");
if (File.Exists(webConfigPath))
{
    Directory.CreateDirectory(targetDirectory);
    File.Copy(webConfigPath, targetWebConfigPath, true);
    Console.WriteLine($"web.config 已复制到 {targetWebConfigPath}");
}
```

通过 File.Exists 判断 web.config 文件是否存在，然后创建 dotNetMatrix 目录，并将 web.config 文件复制到该目录下。随后，使用 ProcessStartInfo 配置解密命令行参数，并启动 aspnet\_regiis.exe 进程执行解密操作。

```
ProcessStartInfo psi = new ProcessStartInfo
{
    FileName = aspnetRegiisPath,
    Arguments = decryptCommand,
    UseShellExecute = false,
    RedirectStandardOutput = true,
    CreateNoWindow = true
};
using (Process process = Process.Start(psi))
{
    string result = process.StandardOutput.ReadToEnd();
    Console.WriteLine(result);
    process.WaitForExit();
}
```

最后，打开dotNetMatrix文件夹查看解密后的web.config内容，可以发现数据库连接字符串已经成功解密。如下图所示

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9bfMNaqibVEP7KnYc1PEZoX0oMsiawkFGpauAWzauMfTgadFhfibCWhTkPzibPOrXicXHwtzpGnARBcNA/640?wx_fmt=other&from=appmsg)

综上，使用DataProtectionConfigurationProvider 加密器可以提高攻击者获取明文密码的难度，但在获取目标webshell权限后，通过自动化攻击就可以完成加密连接字符串的解密操作。

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

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8g70WSk5ibViagFgQ8Sj8tUmOzzGX6ic8Cs2icOPBHibOcQLqsC73tF9H9cl8JkU0DIOYj6hXicXyCfoeg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

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