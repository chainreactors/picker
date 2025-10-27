---
title: 解密.NET配置文件web.config
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487060&idx=1&sn=bc5f5da6c87f40ca86988d7e17a46962&chksm=fa5aa0b9cd2d29af4902c7260827d23ec9239da47ca6ae894b35ac2e13c1bdfc164e8b112231&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2022-11-15
fetch_date: 2025-10-03T22:46:00.845272
---

# 解密.NET配置文件web.config

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCkLlyU08KZfk1HSUU4WbxNETjgW4zgpq7T6kKTI0sDOZSg9TLsae6p3Q/0?wx_fmt=jpeg)

# 解密.NET配置文件web.config

原创

专攻.NET安全的

dotNet安全矩阵

# 0x01 背景

近期有师傅反馈拿到了.NET web.config文件，发现含有数据库账密连接字符串所在的标签<connectionStrings>被加密了，导致看不到MSSQL账户和密码，如下图

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yicxcy17uPY8micuBh2LKVibBtZVcHcs2yV4sfib4E5LiawIGcnA5VODia43s9ePCGLIzM9AoV724pV8bcg/640?wx_fmt=png)

图上可看出由DataProtectionConfigurationProvider类提供加密保护的，DataProtectionConfigurationProvider 使用windows内置的密码学技术加密的，除此之外.NET还提供了另一种RsaProtectedConfigurationProvider 使用RSA公钥加解密，以下内容将具体介绍基于这两类方式进行加解密。

# 0x02 配置

在.NET中有两种配置数据库连接代码的方式，它们分别是 appSettings 和 connectionStrings 。在使用 appSettings 和 connectionStrings 配置数据库连接代码时，可分别在 <configuration> 下添加如下代码

## 2.1 appSettings

```
<appSettings><add key="conn" value="server=服务器名;database=数据库名;uid=用户名;password=密码;"/></appSettings>
```

## 2.2 connectionStrings

```
<connectionStrings><add name="conn" connectionString="server=服务器名;database=数据库名;uid=用户名;password=密码" providerName="System.Data.SqlClient" /></connectionStrings>
```

# 0x03 DataProtectionProvider

使用.NET FrameWork自带的aspnet\_regiis.exe将配置文件web.config中指定的标签进行加解密，aspnet\_regiis 位于%WinDir%\Microsoft.NET\Framework\<versionNumber>目录下，提供了以下几个常用的参数，因为笔者这里用物理路径表示，所以未用到 -app

```
-pef 指定要加密的配置节，这里是 connectionStrings-app 指定该配置文件所在的虚拟目录-prov 指定要使用的提供程序，这里使用的是 DataProtectionConfigurationProvider
```

加密的命令 aspnet\_regiis.exe -pef "connectionStrings" "D:\WebSite\test" -prov "DataProtectionConfigurationProvider"，解密的命令 aspnet\_regiis.exe -pdf "connectionStrings" "D:\WebSite\test"，解密后的结果如下图所示

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCk3n5ibpAqYHdeHGZzxeLgr8LPFkZAxSrOiaK6qzzeS5ZwHm4Z7eJPlTlw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCkoRdvR6ScrsUDVywicZGzicIltoadxxuj7icyAoK1hmkyLCtib0gVVH1kpA/640?wx_fmt=png)

# 0x04 RSAProtectedProvider

使用 RSAProtectedConfigurationProvider类加解密web.config时，第一步需要创建名称为dotnetKey的RSA密钥容器，命令如下

```
aspnet_regiis -pc "dotnetKey" -exp
```

将创建好的配置项内容粘贴到web.config里，主要是在config文件中加入configProtectedData配置节点，这里注意一下此时的容器创建的name是dotnetProvider，如下图

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCk4OhGIYJGZBqQaSuugpNyPmfS0jGI2DkqShicWpUiarLIJyxNXTysz3Og/640?wx_fmt=png)

加密的命令 aspnet\_regiis -pef "connectionStrings" "D:\WebSite\test" -prov "dotNetProvider"，如图

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCkzxZ26pXduWSqOgsNf4tOlt2yagibib93MIAo5CfJCSq0qcbSMRDNBiaKA/640?wx_fmt=png)

解密的命令 aspnet\_regiis -pdf "connectionStrings" "D:\WebSite\test"。需要注意一点aspnet\_regiis.exe运行所需的权限较高，必须是管理员权限才能调用，像上月底爆出的用友畅捷通的默认权限是足够的，但在通常的iis权限属于Users组，权限不够的，另外因为加密过程中使用了一个基于本机的密钥，这意味着解密过程必须在同一台计算机上完成才可以，所以通过任意下载文件下载web.config回本地是解不开的，如下图在IIS权限下执行解密命令返回空，未能解密，通常需要提权后才能解密。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCkLLGC1YbkTS0W3iaReLLIJia4icEX6OBOuIM4T4ntAsquEK1SicFwEZrThw/640?wx_fmt=png)

# 0x05 结语

.NET 还有很多加解密相关的知识内容，如果对这些技巧感兴趣的话可以多关注我们的博客、[公众号dotNet安全矩阵](https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247485543&idx=1&sn=7296192c848c8158ceca4b82e3e8f151&scene=21#wechat_redirect)以及星球，下一篇将继续分享 .NET相关的安全知识，请大伙继续关注。另外文章涉及的PDF和Demo以及工具已打包发布在星球，欢迎对.NET安全关注和关心的同学加入我们，在这里能遇到有情有义的小伙伴，大家聚在一起做一件有意义的事。

# 星球优惠活动

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。经过运营团队成员商议一致同意给到师傅们最大优惠力度，**只需99元就可以加入我们。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCkETPR6LWmyhiccY1ufjKmWB9qia1vPukNHnh2Rg5sHFGobrzX0FS1Zd0Q/640?wx_fmt=jpeg)

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布**很多高质量的.NET**安全资源，可以说市面上很少见，都是干货。其中主题包括**.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库**等等，后续还会倾力打造**专刊、视频**等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibHErRN3IhgSaicia7Rl5SF0plpcuicd0KG8Cn7vGczlBRtvSJvicWejH7TOro6AGLQ627SvVzxzBnphg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58UeoxTMuRezdHEJu6Hp08Xgm2F49cyBI1zlcj5XqLJK8zedWlUjibYmia3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

dotNet安全矩阵知识星球 — 聚焦于微软.NET安全技术，关注基于.NET衍生出的各种红蓝攻防对抗技术、分享内容不限于 .NET代码审计、 最新的.NET漏洞分析、反序列化漏洞研究、有趣的.NET安全Trick、.NET开源软件分享、. NET生态等热点话题、还可以获得阿里、蚂蚁、字节等大厂内推的机会.

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