---
title: 以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（下）
url: https://www.4hou.com/posts/6Vy9
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-12
fetch_date: 2025-10-04T11:30:33.228730
---

# 以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（下）

以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（下）

gejigeji
[技术](https://www.4hou.com/category/technology)
2023-04-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)124759

收藏

导语：以 SingPass 应用为例分析 iOS RASP 应用自保护的实现以及绕过方法（下）

**线程检查**

之前的 Frida stalker 检查的替代方法是通过以下调用访问当前线程状态：

![43.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438677106897.png "1662438677106897.png")

然后，由于以下比较，它检查 state->ts\_64.\_\_pc 是否在 libsystem\_kernel.dylib 中：

![44.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438691238306.png "1662438691238306.png")

换句话说，如果 state->ts\_64.\_\_pc 与 &mach\_msg 的距离小于 0x4000，则认为它在 libsystem\_kernel.dylib 中。

乍一看，对这个 RASP 检查可能不是很熟悉，但由于之前与 EVT\_CODE\_TRACING 相关的检查旨在检测 Frida Stalker，因此该检查也可能旨在检测 Frida Stalker。

为了证实这个假设，我开发了一个小测试用例，在一个独立的二进制文件中重现了这个检查，我们可以根据它是否通过 Frida stalker 来观察差异：

![45.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438702144066.png "1662438702144066.png")

Stalker 测试用例的输出

![46.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438712148171.png "1662438712148171.png")

没有 Stalker 的测试用例的输出

通过使用函数 gum\_stalker\_exclude 从跟踪者中排除库 libsystem\_kernel.dylib ，从而轻松绕过此检查：

![47.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438723367986.png "1662438723367986.png")

可以看到，state->ts\_64.\_\_pc 位于 libsystem\_kernel.dylib 中：

![48.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438732328307.png "1662438732328307.png")

排除内存范围的测试用例的输出

**应用加载的库**

RASP 事件 EVT\_APP\_LOADED\_LIBRARIES 旨在检查 Mach-O 依赖项的完整性。换句话说，它检查 Mach-O 导入的库是否被修改。

```
Assembly ranges: 0x100E4CDF8 – 0x100e4d39c
```

由于 dladdr 函数，与此检查相关的代码首先访问 Mach-O 标头：

![49.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438743985266.png "1662438743985266.png")

dl\_info 包含库的基地址，其中包含第一个参数中提供的地址，因此，一个Mach-O二进制文件会连同它的标头文件Dl\_info一起加载。Dli\_fbase实际上指向mach\_header\_64。

然后该函数遍历类似 LC\_ID\_DYLIB 的命令以访问依赖项的名称：

![50.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438753114133.png "1662438753114133.png")

此名称包含依赖项的路径。例如，我们可以按如下方式访问此列表：

![51.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438763201341.png "1662438763201341.png")

依赖项的名称用于填充哈希表，其中哈希值以 32 位编码：

![52.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438772209903.png "1662438772209903.png")

在后面的代码中，这个计算表将与另一个哈希表(代码中硬编码的)进行比较，如下所示：

![53.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438781243913.png "1662438781243913.png")

**哈希示例**

如果某些库已被修改为注入，例如 FridaGadget.dylib，那么动态计算的哈希将与代码中硬编码的哈希不匹配。

虽然这种检查的执行是相当“标准”的，但有几点值得一提：

首先，哈希函数似乎是一个派生的MurmurHash。

其次，哈希是32位编码的，但是图4中的代码引用了64位的X11/X12寄存器。这实际上是一个限制内存访问次数的编译器优化。

最后，在每个检查实例中，硬编码的哈希值在二进制文件中重复。在 SingPass 中，此 RASP 检查出现两次，因此我们在以下位置找到这些值：0x100E4CF38、0x100E55678。这种重复可能用于防止易于修复的单点位置（ single spot location）。

**代码系统库**

此检查与事件 EVT\_CODE\_SYSTEM\_LIB 相关联，该事件包括验证内存系统库及其在 dyld 共享缓存（磁盘上）中的内容的完整性。

```
Assembly ranges: 0x100ED5BF8 – 0x100ED5D6C and 0x100ED5E0C – 0x100ED62D4
```

此检查通常以以下模式开始：

![54.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438791126347.png "1662438791126347.png")

如果带有给定 check\_region\_cbk 回调的 iterate\_system\_region 的结果不为 0，它会触发 EVT\_CODE\_SYSTEM\_LIB 事件：

![55.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438801441637.png "1662438801441637.png")

要理解这个检查背后的逻辑，我们需要了解 iterate\_system\_region 函数的用途以及它与回调 check\_region\_cbk 的关系。

**iterate\_system\_region**

该函数旨在调用系统函数 vm\_region\_recurse\_64，然后根据可能触发第一个参数check\_region\_cbk中给出的回调的条件过滤它的输出。

iterate\_system\_region首先通过SYS\_shared\_region\_check\_np系统调用访问dyld共享缓存的基址。这个地址用于读取和记忆dyld\_cache\_header结构中的一些属性：

1.共享缓存标头；

2.共享缓存结束地址；

3.与共享缓存相关的其他限制；

计算过程如下：

![56.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438809533297.png "1662438809533297.png")

从逆向工程的角度来看，用于记忆这些信息的堆栈变量与稍后调用的 vm\_region\_recurse\_64 的参数信息别名。我不知道这种混叠是否是故意的，但它使结构的逆向工程变得更加复杂。

在vm\_region\_recurse\_64上有一个循环，它查询vm\_region\_submap\_info\_64信息，查找dyld共享缓存范围内的这些地址。由于mach\_msg\_type\_number\_t \*infoCnt参数被设为19，我们可以确定查询的类型(vm\_region\_submap\_info\_64)：

![57.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438819171507.png "1662438819171507.png")

此循环在某些条件下中断，并且在其他条件下触发回调。正如稍后解释的那样，回调验证 dyld 共享缓存中存在的库的内存完整性。

这个循环在某些条件下中断，而在其他条件下触发回调。回调会验证dyld共享缓存中存在的库在内存中的完整性。

基本上，如果发生以下情况，就会触发对共享缓存进行深度检测的回调：

![58.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438829142079.png "1662438829142079.png")

**check\_region\_cbk**

当条件满足时，iterate\_system\_region调用check\_region\_cbk，第一个参数中带有可疑地址：

![59.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438839118847.png "1662438839118847.png")

在分析 SingPass 时，只有一个回调函数与iterate\_system\_region一起使用，它的代码并没有特别混淆(字符串除外)。一旦我们知道这些检查与dyld共享缓存有关，我们就可以很容易地弄清楚这个函数中涉及的结构。这个回调位于0x100ed5e0c地址，并重命名为check\_region\_cbk。

它首先访问有关地址的信息：

![60.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438848202652.png "1662438848202652.png")

此信息用于读取与地址参数关联的\_\_TEXT 段的内容。

![61.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438857106062.png "1662438857106062.png")

  \_\_TEXT 字符串以及共享缓存的不同路径（如 /System/Library/Caches/com.apple.dyld/dyld\_shared\_cache\_arm64e 和标头的魔法值：0x01010b9126：dyld\_v1 arm64e 或 0x01010b9116：dyld\_v1 arm64）都被编码。

另一方面，该函数打开 dyld\_shared\_cache 并查找包含与地址参数关联的库的共享缓存部分：

![62.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438867740211.png "1662438867740211.png")

第二次调用mmap()的目的是加载包含库代码的共享缓存部分。然后，该函数检查\_\_TEXT段的内容是否与内存中的内容相匹配。执行此比较的循环位于0x100ED6C58 - 0x100ED6C70。

我们可以从这个RASP检查的描述中观察到，开发者花了很多精力来避免性能问题和内存消耗。另一方面，在我的测试中从来没有调用过回调check\_region\_cbk（即使我挂钩了系统函数）。我不知道是不是因为我误解了条件，但最后，我必须手动强制条件。

**RASP 的设计弱点**

由于保存函数指针的不同 #EVT\_\* 静态变量，混淆器能够为支持的 RASP 事件提供专用回调。尽管如此，应用程序开发人员定义的函数 init\_and\_check\_rasp 将所有这些指针设置为同一个回调：hook\_detect\_cbk\_user\_def。在这样的设计中，所有 RASP 事件最终都在一个函数中，这削弱了不同 RASP 检查的强度。

这意味着我们只需要针对这个函数来禁用或绕过 RASP 检查。

![63.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220906/1662438876209401.png "1662438876209401.png")

由于这个缺点，我可以防止应用程序一启动就显示错误消息。

它存在另外两个 RASP 检查：EVT\_APP\_MACHO 和 EVT\_APP\_SIGNATURE，由于开发人员未启用它们，因此在 SingPass 中不存在。

**总结**

一方面商业解决方案实现了强大而先进的 RASP 功能，例如，内联系统调用分布在应用程序的不同位置。另一方面，应用程序的开发人员通过为所有事件设置相同的回调来削弱 RASP 功能。此外，该应用程序似乎没有使用商业解决方案提供的本机代码混淆，这使得 RASP 检查不受静态代码分析的保护。无论用户提供什么配置，对这些检查强制执行代码混淆都是值得的。

本文翻译自：https://www.romainthomas.fr/post/22-08-singpass-rasp-analysis/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会...