---
title: DotRunpeX——揭开野外使用的新型虚拟化.NET注入器的神秘面纱（上）
url: https://www.4hou.com/posts/ZXq6
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-04
fetch_date: 2025-10-04T11:29:40.393335
---

# DotRunpeX——揭开野外使用的新型虚拟化.NET注入器的神秘面纱（上）

DotRunpeX——揭开野外使用的新型虚拟化.NET注入器的神秘面纱（上） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# DotRunpeX——揭开野外使用的新型虚拟化.NET注入器的神秘面纱（上）

luochicun
[技术](https://www.4hou.com/category/technology)
2023-04-03 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)103836

收藏

导语：本研究的主要主题是对两个版本的DotRunpeX注入器进行深入分析，对比它们之间的相似之处，并介绍用于分析新版本的DotRunpeX的PoC技术，因为它是由自定义版本的KoiVM .NET protector.虚拟化传播的。

![微信截图_20230319161953.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218384604208.png "1679218384604208.png")

在过去的几个月里，CPR一直在监测DotRunpeX恶意软件以及它在野外的使用情况。监测显示，这种新型的网络注入器仍在不断发展中。CPR发现了几种不同的传播方法，在发现的所有示例中，DotRunpeX都是第二阶段感染的一部分。这种新的威胁被用来传播许多不同的恶意软件家族，主要与窃取程序、RAT、加载程序和下载程序有关。

与新版DotRunpeX相关的最早示例的日期为2022.10.17。关于这一威胁的首次公开信息发布日期为2022.10.26年。

本研究的主要主题是对两个版本的DotRunpeX注入器进行深入分析，对比它们之间的相似之处，并介绍用于分析新版本的DotRunpeX的PoC技术，因为它是由自定义版本的KoiVM .NET protector.虚拟化传播的。

**主要发现**

Check Point Research（CPR）对DotRunpeX注入器及其与旧版本的关系进行了深入分析；DotRunpeX受到虚拟化（KoiVM的自定义版本）和混淆（ConfuserEx）的保护；

调查显示，DotRunpeX在野外被用来传播许多已知的恶意软件家族；

通常通过网络钓鱼电子邮件作为恶意附件和伪装成常规程序的网站进行传播；

CPR确认并详细说明了恶意使用易受攻击的进程资源管理器驱动程序来禁用反恶意软件服务的功能；

本文会介绍几种PoC技术，这些技术已被批准用于反向工程受保护或虚拟化的dotnet代码；

DotRunpeX是一种使用Process Hollowing技术在.NET中编写的新注入器，用于感染各种已知恶意软件家族的系统。尽管这种注入器是新的，但与旧版本有一些相似之处。此注入器的名称基于其版本信息，在dotRunpeX的两个版本中都是一样的，在CPR分析的所有示例中都是一致的，并且包含ProductName–RunpeX.Stub.Frame。

在CPR监测这一威胁的同时，CPR发现了一些主要由独立研究人员公开共享的信息，这些信息与DotRunpeX的功能有关，但被错误地归因于另一个著名的恶意软件家族。

CPR通过对这一威胁连续进行几个月的监测，CPR获得了足够的信息来区分第一阶段和第二阶段（DotRunpeX）加载程序，但没有迹象表明它们之间存在关系。在各种下载程序和加密货币窃取程序中，CPR发现了这些由dotRunpeX传播的已知恶意软件家族:

```
AgentTesla
ArrowRAT
AsyncRat
AveMaria/WarzoneRAT
BitRAT
Formbook
LgoogLoader
Lokibot
NetWire
PrivateLoader
QuasarRAT
RecordBreaker – Raccoon Stealer 2.0
Redline
Remcos
Rhadamanthys
SnakeKeylogger
Vidar
XWorm
```

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218431632571.png "1679218431632571.png")

DotRunpeX传播的恶意软件家族

从发生的时间顺序来看，基于DotRunpeX示例的编译时间戳，这种新的威胁主要在2022年11月和2023年1月开始流行。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218441169293.png "1679218441169293.png")

DotRunpeX时间轴——编译时间戳

**感染途径**

DotRunpeX注入器通常是原始感染的第二阶段。典型的第一阶段是.NET加载程序/下载程序的非常不同的变体。第一阶段加载程序主要通过钓鱼电子邮件作为恶意附件（通常是“.iso”、“.img”、“.zip”和“.7z”的一部分）或通过伪装成常规程序实用程序的网站进行传播。除了最常见的感染途径外，DotRunpeX的客户还很善于滥用谷歌广告，甚至通过木马恶意软件构建器构建其他潜在的攻击者。

钓鱼邮件“Transaction Advice 502833272391\_RPY - 29/10/2022”将第一阶段加载程序作为恶意“.7z”附件的一部分传播第一阶段加载程序，导致加载DotRunpeX（SHA256:“457cfd6222266941360fdbe36742486ee12419c95f1d7d3502243e795de28200e”）。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218727112503.png "1679218727112503.png")

钓鱼邮件“Transaction Advice 502833272391\_RPY - 29/10/2022”

钓鱼网站会伪装成常规程序实用程序（Galaxy Swapper、OBS Studio、洋葱浏览器、Brave Wallet、LastPass、AnyDesk、MSI Afterburner），并提供第一阶段加载程序，导致dotRunpeX在第二阶段的一部分被感染。

伪装成Galaxy Swapper的网站：https://www.galaxyswapper[.]ru/：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218737170914.png "1679218737170914.png")

在谷歌搜索Galaxy Swapper得到的结果“https://www.galaxyswapper[.]ru/”

下载重定向到https://gitlab[.]com/forhost1232/galaxyv19.11.14/-/raw/main/galaxyv19.11.14.zip。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218747899565.png "1679218747899565.png")

“https://www.galaxyswapper[.]ru/”上的下载按钮重定向到一个木马程序

伪装成LastPass密码管理器的网站：http://lastpass[.]shop/en/

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218793163837.png "1679218793163837.png")

网站“http://lastpass[.]shop/en/”伪装成LastPass密码管理器

LastPass密码管理器的假冒网站在调查时已经关闭。尽管如此，CPR可以确认该假冒软件是从“最终URL”https://gitlab[.]com/forhost1232/lastpassinstaller/-/raw/main/LastPassInstaller.zip下载的。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218816169754.png "1679218816169754.png")

 “http://lastpass[.]shop/en/” 上的下载按钮重定向到一个木马程序

GitLab页面https://gitlab[.]com/forhost1232包含数十个被DotRunpeX恶意软件木马化的程序。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218831999690.png "1679218831999690.png")

GitLab存储库“https://gitlab[.]com/forhost1232”上的数十个木马程序

在前面提到的GitLab页面上，所有的木马程序都包含了主.NET应用程序，并通过覆盖层进行了放大，以避免使用沙盒进行扫描。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218856209009.png "1679218856209009.png")

由GitLab存储库" https://gitlab[.]com/forhost1232 "提供的木马程序示例

上面提到的带有覆盖的.NET应用程序是典型的第一阶段，其行为就像带有简单混淆的dotnet加载程序。这些不同的加载程序变体在第二阶段使用反射来加载DotRunpeX注入器。其中有些非常简单，有些则更高级。

简单的第一阶段加载程序（System.Reflection.Assembly.Load()方法）：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218899134501.png "1679218899134501.png")

简单的第一阶段加载程序

下面可以看到更高级的第一阶段加载程序的示例（使用AMSI Bypass和DynamicMethod通过反射加载和执行第二阶段加载程序）。这种高级加载程序的优点是没有直接引用System.Reflection.Assembly.Load()方法，因此它可以避免检测依赖于.NET元数据静态解析的引擎。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218919183470.png "1679218919183470.png")

使用AMSI绕过和DynamicMethod的更高级的第一阶段加载程序

后一种的去混淆形式如下图所示：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218933842183.png "1679218933842183.png")

更高级的第一阶段加载程序的去混淆形式

从这些类型的加载程序中提取第二阶段（DotRunpeX阶段）的编程方式可以简单地使用AsmResolver和反射来实现，如下所示。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218947200710.png "1679218947200710.png")

使用AsmResolver和反射从第一阶段加载程序提取DotRunpeX

值得注意的是，那些指向GitLab页面的钓鱼网站的示例只与一个活动有关，在这个活动中，DotRunpeX注入器总是负责注入带有C2–77.73.134.2的Redline恶意软件。

除了前面提到的最常见的感染途径外，CPR还观察到了一个非常有趣的感染途径示例，在这个示例中，DotRunpeX的一位客户可能已经厌倦了以普通受害者为目标，并决定以其他潜在的攻击者为目标。Redline构建器Redline\_20\_2\_crack.rar (SHA256: “0e40e504c05c30a7987785996e2542c332100ae7ecf9f67ebe3c24ad2468527c”)被下载程序木马化，该下载程序使用反射来加载dotRunpeX作为构建器的隐藏“添加功能”。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218958174082.png "1679218958174082.png")

木马化的Redline构建器的文件夹结构

事实证明，在Redline的构建过程中，根据需求进行配置，使用者还将获得另一个Redline示例。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218978481396.png "1679218978481396.png")

使用反射来加载DotRunpeX的下载程序，该下载程序传播另一个Redline恶意软件

旧版本的DotRunpeX：

使用自定义混淆：仅对名称进行混淆；

配置有限（有效负载注入目标、提升+UAC绕过、有效负载解密的XOR密钥）；

只有一种UAC绕过技术；

使用简单的XOR对要注入的主要有效负载进行解密；

使用D/Invoke类似的技术来调用本机代码（基于使用GetDelegateForFunctionPointer()），但使用诱饵系统调用例程；

使用D/Invoke重新映射" ntdll.dll "

新版本的DotRunpeX：

由自定义版本的KoiVM虚拟程序保护；

高度可配置(禁用反恶意软件服务，反虚拟程序，反沙盒，持久性设置，有效负载解密密钥，UAC绕过方法)；

更多的UAC绕过技术；

使用简单的XOR来解密要注入的主要有效负载(在最新开发的版本中省略了)；

滥用procexp驱动程序(Sysinternals)阻止受保护进程(反恶意软件服务)；

基于俄罗斯procexp驱动程序的标志名称 Иисус.sys 翻译过来就是“jesus.sys”；

两个版本的相似之处：

用.NET编写的64位可执行文件“.exe”；

用于注入几个不同的恶意软件家族；

使用简单的XOR对要注入的主要有效负载进行解密；

可能使用相同的UAC绕过技术（新版DotRunpeX提供了更多技术）；

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230319/1679218991539393.png "1679218991539393.png")

UAC绕过技术

使用相同的版本信息；

![17.png](https://img.4hou.com/uploads/uedi...