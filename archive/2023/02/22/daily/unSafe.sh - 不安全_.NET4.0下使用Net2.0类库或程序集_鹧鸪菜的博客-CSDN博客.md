---
title: .NET4.0下使用Net2.0类库或程序集_鹧鸪菜的博客-CSDN博客
url: https://buaq.net/go-150391.html
source: unSafe.sh - 不安全
date: 2023-02-22
fetch_date: 2025-10-04T07:41:02.702776
---

# .NET4.0下使用Net2.0类库或程序集_鹧鸪菜的博客-CSDN博客

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

.NET4.0下使用Net2.0类库或程序集\_鹧鸪菜的博客-CSDN博客

鹧鸪菜 于 2017-09-14 18:05:47 发布
*2023-2-21 22:31:41
Author: [blog.csdn.net(查看原文)](/jump-150391.htm)
阅读量:20
收藏*

---

![](https://csdnimg.cn/release/blogv2/dist/pc/img/reprint.png)

[鹧鸪菜](https://blog.csdn.net/wlanye "鹧鸪菜")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2017-09-14 18:05:47 发布
![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
1176
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
收藏

**https://msdn.microsoft.com/zh-cn/library/ff602939%28v=vs.110%29.aspx?f=255&MSPPError=-2147217396#Apps**

最近在项目上一直使用.net4.0 framework，使用ffmepeg下的一个dll时，提示只能在2.0下运行,解决方法如下:

app.config中添加一个配置节：startup

![复制代码](http://common.cnblogs.com/images/copycode.gif)

```
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <startup useLegacyV2RuntimeActivationPolicy="true">
    <supportedRuntime version="v2.0"/>
    <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/>
  </startup>
</configuration>
```

![复制代码](http://common.cnblogs.com/images/copycode.gif)

在.NET2.0 framework，.NET3.5 framework的时候，**由于程序运行环境本质还是.NET2.0，**而到了.NET4.0由于整个程序集的版本更新，以前使用.NET2.0所编写的程序集与.NET4.0的程序集互操作的时候就会出现兼容性问题。

通过MSDN，我们可以知道，startup配置节中的useLegacyV2RuntimeActivationPolicy属性是在.NET4.0中新增的，默认是false，表示：使用默认的 .NET Framework 4 激活策略，该激活策略将加载 .NET Framework 4.0,通过使用公共语言运行时 (CLR) 版本 4.0 所创建的程序集，以及 CLR 早期版本通过使用受支持的低于版本 4.0 的最高 CLR 版本所创建的程序集。

现在如果当程序在.NET4.0环境下要使用.NET2.0或.NET3.5及以下的程序集时就必须将useLegacyV2RuntimeActivationPolicy设置为true，同时还要注意**，需要在startup配置节的字节中添加supportedRuntime配置节，并指定为"v4.0"，表示使用.NET4.0运行时来运行程序。**

<supportedRuntime> 元素

指定应用程序支持的公共语言运行时版本。 此元素应由用 .NET Framework 1.1 版或更高版本生成的所有应用程序使用。

<supportedRuntime version="runtime version" sku="sku id"/>

| 特性 | 描述 |
| --- | --- |
| version | 可选特性。  一个字符串值，它指定此应用程序支持的公共语言运行时 (CLR) 版本。 有关version 特性的有效值的信息，请参阅[“运行时版本”值](https://msdn.microsoft.com/zh-cn/library/w4atty68.aspx#version)部分。  | 注意 | | --- | | 通过 .NET Framework 3.5，“运行时版本”值的形式为主版本号.次版本号.内部版本号。 从 .NET Framework 4 开始，仅主版本号和次版本号是必需的（即“v4.0”而不是“v4.0.30319”）。 建议使用较短字符串。 | |
| sku | 可选特性。  一个字符串值，该值指定库存单位 (SKU)，库存单位则指定此应用程序支持的 .NET Framework 版本。  从 .NET Framework 4.0 起，建议使用 sku 特性。  若存在该特性，则它指示应用面向的 .NET Framework 版本。  有关 SKU 特性的有效值的信息，请参阅 [“SKU ID”值](https://msdn.microsoft.com/zh-cn/library/w4atty68.aspx#sku) 部分。 |

如果应用程序配置文件中没有 <supportedRuntime> 元素，则使用用于生成应用程序的运行时版本。

< supportedRuntime> 元素应由使用运行时 1.1 版或更高版本生成的所有应用程序使用。 仅为支持运行时 1.0 版而生成的应用程序必须使用[<requiredRuntime>](https://msdn.microsoft.com/zh-cn/library/a5dzwzc9.aspx) 元素。

对于支持从 .NET Framework 1.1 到 3.5 的运行时版本的应用，支持多个运行时版本时，第一个元素应指定优先级最高的版本，最后一个元素应指定优先级最低的版本。 对于支持 .NET Framework 4.0 或更高版本的应用，version 特性指示普遍适用于 .NET Framework 4 及更高版本的 CLR 版本，而 sku特性指示应用所面向的单个 .NET Framework 版本。

| 注意 |
| --- |
| 如果你的应用程序使用旧式激活路径（如 [CorBindToRuntimeEx 函数](https://msdn.microsoft.com/zh-cn/library/99sz37yh.aspx)），并且你希望这些路径激活 CLR 的版本 4（而不是较早的版本），或者你的应用程序是用 .NET Framework 4 生成的，但在使用较早版本的 .NET Framework 生成的混合模式程序集上有依赖项，则不足以在受支持的运行时列表中指定 .NET Framework 4。 此外，在配置文件的 [<startup> 元素](https://msdn.microsoft.com/zh-cn/library/bbx34a2h.aspx)中，必须将 useLegacyV2RuntimeActivationPolicy 特性设置为 true。 但是，将此特性设置为 true 意味着，用 .NET Framework 早期版本生成的所有组件都使用 .NET Framework 4（而不是生成它们时所用的运行时）运行。 |

建议使用应用程序可在其上运行的所有 .NET Framework 版本来测试这些应用程序。

下表列出了version特性的运行时版本值的有效值。

| .NET Framework 版本 | version 特性 |
| --- | --- |
| 1.0 | "v1.0.3705" |
| 1.1 | "v1.1.4322" |
| 2.0 | "v2.0.50727" |
| 3.0 | "v2.0.50727" |
| 3.5 | "v2.0.50727" |
| 4.0 | "v4.0" |
| 4.5 | "v4.0" |
| 4.5.1 | "v4.0" |
| 4.5.2 | "v4.0" |
| 4.6 | "v4.0" |
| 4.6.1 | "v4.0" |

下表列出 sku 特性支持的 .NET Framework 版本（自 .NET Framework 4 起）。  请注意，自 .NET Framework 4 开始的 sku 特性指示应用面向的 .NET Framework 版本。

| .NET Framework 版本 | sku 特性 |
| --- | --- |
| 4.0 | ".NETFramework,Version=v4.0" |
| 4.0，客户端配置文件 | ".NETFramework,Version=v4.0,Profile=Client" |
| 4.0，平台更新 1 | .NETFramework,Version=v4.0.1 |
| 4.0，客户端配置文件，Update 1 | .NETFramework,Version=v4.0.1,Profile=Client |
| 4.0，平台更新 2 | .NETFramework,Version=v4.0.2 |
| 4.0，客户端配置文件，Update 2 | .NETFramework,Version=v4.0.2,Profile=Client |
| 4.0，平台更新 3 | .NETFramework,Version=v4.0.3 |
| 4.0，客户端配置文件，Update 3 | .NETFramework,Version=v4.0.3,Profile=Client |
| 4.5 | ".NETFramework,Version=v4.5" |
| 4.5.1 | ".NETFramework,Version=v4.5" |
| 4.5.2 | ".NETFramework,Version=v4.5" |
| 4.6 | ".NETFramework,Version=v4.5" |
| 4.6.1 | ".NETFramework,Version=v4.5" |

下表显示对于不同的 sku 特性值，当 version 特性为 v4.0 且 sku 特性标识 .NET Framework 4 或它的一个平台更新 (PU) 时，应用程序将在安装的哪一个 .NET Framework 4 版本上运行。

| sku 特性的值 | 4.0 Client | 4.0 Full | 4.0 Client + PU 1 | 4.0 Full + PU 1 | 4.0 Client + PU 2 | 4.0 Full + PU 2 | 4.0 Client + PU 3 | 4.0 Full + PU 3 | 4.5 和更高版本 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .NETFramework,Version=v4.0,Profile=Client | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 | 是 |
| .NETFramework,Version=v4.0 |  | 是 |  | 是 |  | 是 |  | 是 | 是 |
| .NETFramework,Version=v4.0.1,Profile=Client |  |  | 是 | 是 | 是 | 是 | 是 | 是 | 是 |
| .NETFramework,Version=v4.0.1 |  |  |  | 是 |  | 是 |  | 是 | 是 |
| .NETFramework,Version=v4.0.2,Profile=Client |  |  |  |  | 是 | 是 | 是 | 是 | 是 |
| .NETFramework,Version=v4.0.2 |  |  |  |  |  | 是 |  | 是 | 是 |
| .NETFramework,Version=v4.0.3,Profile=Client |  |  |  |  |  |  | 是 | 是 | 是 |
| .NETFramework,Version=v4.0.3 |  |  |  |  |  |  |  | 是 | 是 |

## 示例

下面的示例演示如何在配置文件中指定支持的运行时版本。 配置文件指示应用面向 .NET Framework 4.6。

```
<configuration> <startup> <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.6" /> </startup> </configuration>
```

转载请保留原地址. http://www.cnblogs.com/lsqandzy

**2.0程序基本都可以在3.5框架下完美运行
 给出错误信息差不多**

文章来源: https://blog.csdn.net/wlanye/article/details/77983602
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)