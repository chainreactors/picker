---
title: 以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（上）
url: https://www.4hou.com/posts/50xR
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-09
fetch_date: 2025-10-04T11:29:36.028098
---

# 以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（上）

以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（上） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（上）

gejigeji
[技术](https://www.4hou.com/category/technology)
2023-04-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)141971

收藏

导语：以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（上）

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662436231147264.png "1662436231147264.png")

通过在应用程序的安装目录中搜索一些关键字，我们实际上得到了两个结果，它们含有混淆器名称的信息：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662436326168026.png "1662436326168026.png")

NuDetectSDK 二进制文件也使用相同的混淆器，但它似乎没有参与上图所示的早期越狱检测。另一方面，SingPass 是应用程序的主要二进制文件，我们可以观察到与威胁检测相关的字符串：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662436335101617.png "1662436335101617.png")

混淆器的名称已被编辑，但不会影响代码的内容。

不幸的是，二进制文件没有泄漏其他字符串，这些字符串可以帮助识别应用程序检测越狱设备的位置和方式，但幸运的是，应用程序没有崩溃。

如果我们假设混淆器在运行时解密字符串，则可以尝试在显示错误消息时转储 \_\_data 部分的内容。在执行时，用于检测越狱设备的字符串可能已被解码并清楚地存在于内存中。

1.我们运行应用程序并等待越狱消息；

2.我们使用 Frida 附加到 SingPass，并注入一个库：

2.1在内存中解析 SingPass 二进制文件；

2.2转储 \_\_data 部分的内容；

2.3 将转储写入 iPhone 的 /tmp 目录；

一旦数据区被转储，\_\_data部分会发生以下变化：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662436431676585.png "1662436431676585.png")

转储前后的 \_\_data 部分

此外，我们可以观察到以下字符串，它们似乎与混淆器的RASP功能有关：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662436443136317.png "1662436443136317.png")

与 RASP 功能相关的字符串

所有的EVT\_\*字符串都由一个且只有一个我命名为on\_rasp\_detection的函数引用。这个函数是应用程序开发者在触发RASP事件时用来执行操作的威胁检测回调函数。

为了更好地理解这些字符串背后的检查逻辑，让我们从用于检测挂钩函数的 EVT\_CODE\_PROLOGUE 开始。

**EVT\_CODE\_PROLOGUE：挂钩检测**

当通过汇编代码接近 on\_rasp\_detection 的交叉引用时，我们可以多次发现这种模式：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437525131390.png "1662437525131390.png")

为了检测给定函数是否被钩住，混淆器加载函数的第一个字节，并将该字节与值0xFF进行比较。乍一看，0xFF似乎是任意的，但事实并非如此。实际上，常规函数以一个序言开始，该序言在堆栈上分配空间，以保存由调用约定定义的寄存器和函数所需的堆栈变量。在AArch64中，这个分配可以通过两种方式执行：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437535586902.png "1662437535586902.png")

这些指令是不相等的，如果偏移量存在，它们可能会导致相同的结果。在第二种情况下，指令 sub SP、SP、#CST 用以下字节编码：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437543695145.png "1662437543695145.png")

正如我们所看到的，该指令的编码从0xFF开始。如果不是这样，那么该函数要么以不同的堆栈分配序言开始，要么可能以一个挂钩的蹦床开始。由于应用程序的代码是通过混淆器的编译器编译的，因此编译器能够区分这两种情况，并为正确的函数的序言插入正确的检查。

如果函数指令的第一个字节没有通过检查，则跳转到红色基本块。这个基本块的目的是触发一个用户定义的回调，它将根据应用程序的设计和开发人员的选择来处理检测：

打印错误

应用程序崩溃

破坏内部数据

……

从上图中，我们可以观察到检测回调是从位于 #hook\_detect\_cbk\_ptr 的静态变量加载的。调用此检测回调时，混淆器会向回调提供以下信息：

1.检测码：EVT\_CODE\_PROLOGUE 为 0x400；

2.可能导致应用程序崩溃的受攻击指针；

现在让我们仔细看看检测回调的整体设计。

**检测回调**

如上一节所述，当混淆器检测到篡改时，它会通过调用存储在地址的静态变量中的检测回调来做出反应：0x10109D760

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437557169270.png "1662437557169270.png")

通过静态分析 hook\_detect\_cbk，实现似乎破坏了回调参数中提供的指针。另一方面，在运行应用程序时，我们观察到越狱检测消息，而不是应用程序崩溃。

如果我们查看在该地址读取或写入的交叉引用，我们会得到以下指令列表：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437566115057.png "1662437566115057.png")

所以实际上只有一条指令，init\_and\_check\_rasp+01BC，用另一个函数覆盖默认的检测回调：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437574190074.png "1662437574190074.png")

与默认回调相比：hook\_detect\_cbk（被覆盖的函数）相比，hook\_detect\_cbk\_user\_def不会损坏一个会导致应用程序崩溃的指针。相反，它调用on\_rasp\_detection函数，该函数引用上图中列出的所有字符串EVT\_CODE\_TRACING、EVT\_CODE\_SYSTEM\_LIB等。

通过整体查看init\_and\_check\_rasp函数，我们可以注意到X23寄存器也用于初始化其他静态变量：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437585203603.png "1662437585203603.png")

X23写入指令

这些内存写入意味着回调 hook\_detect\_cbk\_user\_def 用于初始化其他静态变量。特别是，这些其他静态变量很可能用于其他 RASP 检查。通过查看这些静态变量#EVT\_CODE\_TRACING\_cbk\_ptr、#EVT\_ENV\_JAILBREAK\_cbk\_ptr 等的交叉引用，我们可以找到执行其他 RASP 检查的位置以及触发它们的条件。

**EVT\_CODE\_SYSTEM\_LIB**

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437599105344.png "1662437599105344.png")

EVT\_ENV\_DEBUGGER

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437610279501.png "1662437610279501.png")

EVT\_ENV\_JAILBREAK

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437620153058.png "1662437620153058.png")

多亏了#EVT\_\*交叉引用，我们可以静态地通过使用这些#EVT\_\*变量的所有基本块，并突出显示可能触发RASP回调的底层检查。在详细检查之前，需要注意以下几点：

1.虽然应用程序使用了一个商业混淆器，除了RASP之外，还提供了本地代码混淆，但代码是轻度混淆的，这使得静态汇编代码分析非常容易。

2.应用程序为所有 RASP 事件设置相同的回调。因此，它简化了 RASP 绕过和应用程序的动态分析。

**反调试**

SingPass 使用的混淆器版本实现了两种调试检查。首先，它检查父进程 id (ppid) 是否与 /sbin/launchd 相同，后者应该为 1。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437634214459.png "1662437634214459.png")

getppid 通过函数或系统调用调用。

如果不是这种情况，它会触发 EVT\_ENV\_DEBUGGER 事件。第二个检查基于用于访问 extern\_proc.p\_flag 值的 sysctl。如果此标志包含 P\_TRACED 值，则 RASP 例程会触发 EVT\_ENV\_DEBUGGER 事件。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437643253249.png "1662437643253249.png")

在 SingPass 二进制中，我们可以在以下地址范围内找到这两个检查的实例：

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437652161255.png "1662437652161255.png")

**越狱检测**

对于大多数越狱检测，混淆器会通过检查设备上是否存在（或不存在）某些文件来尝试检测设备是否已越狱。

借助以下帮助程序，可以使用系统调用或常规函数检查文件或目录：

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437662208069.png "1662437662208069.png")

如上所述，我提到 \_\_data 部分的转储显示与越狱检测相关的字符串，但转储并未显示混淆器使用的所有字符串。

通过仔细研究字符串编码机制，可以发现有些字符串是在临时变量中即时解码的。我将在本文的第二部分解释字符串编码机制，这样，我们可以通过在fopen、utimes等函数上设置钩子，并在这些调用之后立即转储\_\_data部分来揭示字符串。然后，我们可以遍历不同的转储，查看是否出现了新的字符串。

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437673209480.png "1662437673209480.png")

最后，该方法无法对所有字符串进行解码，但可以实现良好的覆盖。用于检测越狱的文件列表在附件中给出。

还有一个检测 unc0ver 越狱的特殊检查，包括尝试卸载 /.installed\_unc0ver：

```
0x100E4D814: _unmount("/.installed_unc0ver")
```

**环境**

混淆器还会检查触发 EVT\_ENV\_JAILBREAK 事件的环境变量。其中一些检查似乎与代码提升检测有关，但仍会触发 EVT\_ENV\_JAILBREAK 事件。

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437683120432.png "1662437683120432.png")

**startswith()**

从逆向工程的角度来看，startswith()实际上是作为一个“or-ed”的xor序列来实现的，以得到一个布尔值。这可能是编译器优化的结果。你可以在位于地址0x100015684的基本块中观察这个模式。

**高级检测**

除了常规检查之外，混淆器还执行高级检查，比如验证SIP(系统完整性保护)的当前状态，更准确地说，是KEXTS代码签名状态。

根据我在iOS越狱方面的经验，我认为没有越狱会禁用CSR\_ALLOW\_UNTRUSTED\_KEXTS标志。相反，我猜它是用来检测应用程序是否在允许这种停用的 Apple M1 上运行。

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437694548211.png "1662437694548211.png")

```
 Assembly range: 0x100004640 – 0x1000046B8
```

混淆器还使用 Sandbox API 来验证是否存在某些路径：

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662437704907595.png "1662437704907595.png")

通过这个 API 检查的路径是 OSX 相关的目录，所以我猜它也被用来验证当前代码没有在 Apple Silicon 上被解除。例如，下面是使用 Sandbox API 检查的目录列表：

![25.pn...