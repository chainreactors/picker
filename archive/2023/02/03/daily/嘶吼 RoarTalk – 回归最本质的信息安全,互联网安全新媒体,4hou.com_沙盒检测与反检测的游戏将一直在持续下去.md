---
title: 沙盒检测与反检测的游戏将一直在持续下去
url: https://www.4hou.com/posts/xjDB
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-03
fetch_date: 2025-10-04T05:33:01.435579
---

# 沙盒检测与反检测的游戏将一直在持续下去

沙盒检测与反检测的游戏将一直在持续下去 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 沙盒检测与反检测的游戏将一直在持续下去

luochicun
[技术](https://www.4hou.com/category/technology)
2023-02-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)167882

收藏

导语：当恶意软件开发者发现自己在沙盒中运行时，会竭尽全力避免恶意行为。目前有很多沙盒检测方法，每种方法都有优缺点。

当恶意软件开发者发现自己在沙盒中运行时，会竭尽全力避免恶意行为。目前有很多沙盒检测方法，每种方法都有优缺点。

至于恶意软件开发者如何检测到沙盒？有很多不同的方法，但总的来说，他们会检查环境的特征，看看它是否看起来像一个目标主机，而不是一个自动化系统。

**逃避沙盒策略**

恶意软件开发者会使用大量技术来检查它们是否运行在“真正的”目标主机上，比如计算浏览器缓存中的cookie数量，或者检查显存是否太小。

**检测仪器或“挂钩”**

逃避沙盒仪器的检测，这绝对是最流行的技术之一。最常见的例子是检查API挂钩，因为这是沙盒和防病毒供应商检测和记录分析中的可执行文件进行的所有API调用的常用方法。这可以像检查常见函数的函数序言一样简单，看看它们是否被挂钩。

在下图中，我们看到了Windows 10中CreateFileA的序言的反汇编是什么样子的，以及如果在沙盒中插入了指令，它可能是什么样子。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372215691662.png "1672372215691662.png")

系统API中函数上的典型沙盒挂钩

如上所示，攻击者很容易察觉到这一点，这就是为什么这是我们所看到的最常见的方法之一。

这种技术的一个有趣的变化是，恶意软件检测并解除现有的挂钩，以便在不记录其活动的情况下偷偷执行。当恶意软件开发者想要通过端点保护而不被目标主机检测到时，就会发生这种情况。

下图显示了GuLoader如何解包ZwProtectVirtualMemory函数序言的字节以恢复原始功能的示例。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372228198679.png "1672372228198679.png")

GuLoader正在解除逃避系统API函数中的检测

**减少逃避沙盒仪器检测的方法**

防止恶意软件作者检测检测仪器的黄金标准就是不要有任何对你正在分析的程序可见的异常内容。越来越多的沙盒将这一想法作为其检测策略的重点。当你在操作系统中的任何地方都不改变一个字节时，你就更容易避免逃避。

与其通过更改代码来检测API，不如使用虚拟化来无形地检测分析中的程序。从来宾VM外部检测恶意软件有很多好处。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372245759648.png "1672372245759648.png")

客户机与基于虚拟机监控程序的挂钩引擎。左：程序分析组件与它执行的恶意软件样本一起存在于来宾VM中。右：分析组件完全存在于来宾VM之外，因此对于被分析的程序来说是不可见的

**检测虚拟环境**

另一个常见的逃避则涉及检测文件正在虚拟机（VM）中执行。这可能涉及指纹资源，如低CPU核心数、系统或视频内存或屏幕分辨率。它还可能涉及特定VM的指纹工件。

在构建沙盒时，供应商有大量的虚拟机解决方案可供选择，如KVM、VirtualBox和Xen。每一个都有各种各样的工件和特性，它们可以被运行在它们下面的vm中的软件检测到。

其中一些特性是特定系统特有的，比如检查VMware的后门接口，或者检查提供给操作系统的硬件是否与QEMU提供的虚拟硬件匹配。其他方法可以简单地检测一般的管理程序。例如，Mark Lim在一篇文章中讨论了管理程序的一般逃避，该文章利用了许多管理程序错误地模拟trap标志行为这一事实。

恶意软件确定其是否在VMware虚拟机内运行的最早和最广泛使用的机制之一是使用VMware的后门接口来查看VMware虚拟机管理程序是否有任何有效响应。这种检查的示例如下图所示。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372260134728.png "1672372260134728.png")

恶意软件检查它是否在VMware虚拟机内运行

恶意软件家族还可以使用Windows Management Instrumentation（WMI）查询来查询计算机制造商或型号信息。这允许他们获取有关系统的信息，并将其与已知的沙盒或管理程序字符串进行比较。

下图显示了如何使用它对VMware、Xen、VirtualBox和QEMU进行查询。同样的技术也可以在Al-Khaser中找到，这是一个包含许多反沙盒技术的开源工具。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372277198921.png "1672372277198921.png")

用于查询计算机信息的WMI查询

下图显示了恶意软件可能与之交互的软件组件，以显示它是否在虚拟环境中执行。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372293800002.png "1672372293800002.png")

进程可以与之交互以评估它们是否在VM内部

此外，在来宾虚拟机周围经常会散布大量信息，这些信息可以很容易地提供有关来宾操作系统在其下运行的虚拟机平台的线索。具体信息取决于所使用的VM基础架构（例如，VMware、KVM或QEMU）。

以下只是恶意软件作者可以检查的几个示例：

显示VM特定硬件、驱动程序或服务的注册表项路径；

VM特定驱动程序或其他服务的文件系统路径；

特定于某些VM基础结构的MAC地址；

虚拟硬件(例如，如果查询报告你的网卡是多年未生产的Intel e1000，它可以推断你可能正在使用Qemu硬件模型运行)；

运行显示虚拟机平台特定服务以支持准虚拟化的流程，或为用户提供方便的系统（如VMware工具）；

CPUID指令，在许多情况下，有助于通知VM平台的客户端软件；

**缓解虚拟机逃避**

大多数缓解措施的主要问题是，主流虚拟化平台替代方案为恶意软件开发者所熟知。为了便于实现，大多数沙盒都基于KVM、Xen或QEMU等系统，这使得这类逃避特别难以缓解。

每一个主流虚拟机平台都被沙盒逃避所针对。问题是，除了编写自己的自定义管理程序来支持恶意软件分析之外，没有什么能有效地解决这类逃避问题。

**缺乏人机互动**

这一类别包括需要特定人机互动的逃避。例如，恶意软件开发者希望看到鼠标点击或其他事件发生在“真实”用户驱动的系统上，但这在典型的自动分析平台中是不存在的。恶意软件家族通常会检查人员交互，如果看起来没有用户驱动系统，则停止执行，因为用户活动正在模拟中。

以下是我们在人机交互检查中观察到的一般主题：

提示用户进行交互。例如，应该点击沙盒可能不知道的对话框或虚假eula以确保引爆。

检查鼠标点击，鼠标移动和按键。甚至可以分析鼠标事件的位置或击键的时间，以确定它们看起来是“自然的”还是通过编程生成的。

在文档中放置宏以检查是否存在诸如滚动、单击电子表格中的单元格或检查其他工作表选项卡等人机交互的证据。

让我们看一个具体的示例（如下图所示），说明恶意软件如何获取自上次用户输入（GetLastUserInput）和自系统启动（GetTickCount）以来的时间。然后，它可以比较自按下最后一个键以来经过了多长时间，以检测系统上是否有任何活动。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372309309050.png "1672372309309050.png")

攻击开始所需的用户交互

**减少人际互动逃避**

在实现沙盒时，我们可以控制虚拟键盘、鼠标和显示器。如果由于某种原因，分析的可执行文件需要任何输入键，我们可以向分析发送按键，或者确保点击正确的按钮以继续执行可执行文件。

与VM检测问题的所有其他领域一样，我们需要对恶意软件家族正在寻找的内容保持警惕，并不断改进缓解逃避策略。最近的一个例子涉及需要在Excel电子表格中的多个单元格上单独点击鼠标的恶意软件。

**时间和计算资源逃避**

早期，沙盒中最常见的逃避方式之一是在做任何攻击之前只需要睡眠一个小时。这样，它将保证恶意软件将远远超出几乎所有沙盒使用的最短分析时间窗口，因为运行每个样本超过几分钟是不可行的。

沙盒开发者对此的反应是将长时间睡眠缩短为短时间睡眠。下图显示了一种使用Windows计时器和Windows消息的逃避技术。其思想是安装一个每秒钟触发一次的计时器，然后在执行计时器的回调时增加一个内部变量。

一旦变量达到特定的阈值，它将发送另一条Windows消息通知示例开始执行恶意软件。这种规避的问题是，沙盒不能简单地将计时器的超时时间减少到一个较低的数字，因为它可能会中断其他软件的执行，但它仍然必须以某种方式执行。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372334123893.png "1672372334123893.png")

使用定时器和Windows消息的睡眠示例

另一个示例如下图所示，其中恶意可执行文件只需在循环中调用时间戳计数器指令。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372355136444.png "1672372355136444.png")

使用时间戳计数器指令的休眠循环

**缓解利用时间逃避的方法**

老实说，利用时间逃避很难缓解。如前所述，我们总是可以调整睡眠参数和计时器，但这并不能完全解决问题。

我们发现另一个有用的策略是，因为我们控制管理程序，所以我们可以使用技术来控制所有硬件和软件，从而使来宾VM中的时间过得更快。甚至不需要更改参数或安装任何挂钩就可以做到这一点。我们可以在几分钟内实时运行一个小时的可执行文件，这使我们能够更快地获取恶意代码。

垃圾指令循环或虚拟机退出循环可能是最难对付的情况。如果恶意软件开发者执行了几百万条CPUID指令，在管理程序下面执行这些指令的时间就会呈指数级增长，那么我们的代码就是在VM中运行的。

**Pocket Litter检查**

“Pocket Litter”一词来自间谍活动领域，其目的是用于恶意软件开发者检查环境是否显示出真实的目标主机的证据。

在沙盒环境中，检查“Pocket Litter”通常包括查找合理的系统正常运行时间、My Documents文件夹中的足够数量的文件或系统浏览器缓存中的大量页面。这些都有助于证实该系统是“真实的”，而不是沙盒环境。与其他类别一样，变化的数量似乎是无限的。

下图显示了另一个示例，其中恶意软件检查是否有两个以上的可用处理器以及是否有足够的可用内存。通常，沙盒环境的可用内存没有普通PC那么多，这项检查是测试目标系统是否可能是台式PC或在沙盒环境中运行。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372373135979.png "1672372373135979.png")

检查所需的最小处理器数量和运行所需的内存

在下图中，还有另一个示例，如果卷磁盘序列号与已知防病毒供应商使用的模拟器的序列号匹配，则AutoIt可执行文件将退出。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221230/1672372393334193.png "1672372393334193.png")

检查卷序列号

**Pocket Litter检查缓解措施**

目前没有一种特定的方法可以用于缓解这种逃避，只能具体问题具体解决。

例如，当我们看到对特定位置的特定类型文件进行检查时(如果它看起来是对VM映像的无害更改)，我们将它们添加到任何相关示例中以查看。这种Pocket Litter的方法感觉像是猫捉老鼠的游戏。

**总结**

沙盒逃避的方法太多，没有哪一种方法可以有效地解决所有问题，因此必须具体问题具体分析解决。

本文翻译自：https://securelist.com/bluenoroff-methods-bypass-motw/108383/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?SUwXyAhJ)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/07/6cfb327dad8fe371f6fa.jpg)

# [luochicun](https://www.4hou.com/member/aOZG)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器...