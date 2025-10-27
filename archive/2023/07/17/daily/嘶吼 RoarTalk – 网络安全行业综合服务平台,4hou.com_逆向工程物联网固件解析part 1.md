---
title: 逆向工程物联网固件解析part 1
url: https://www.4hou.com/posts/gDQr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-17
fetch_date: 2025-10-04T11:51:20.519955
---

# 逆向工程物联网固件解析part 1

逆向工程物联网固件解析part 1 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 逆向工程物联网固件解析part 1

walker
[技术](https://www.4hou.com/category/technology)
2023-07-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)117494

收藏

导语：物联网 (IoT) 设备已经成为我们日常生活、工作环境、医院、政府设施和车队的重要组成部分。

物联网 (IoT) 设备已经成为我们日常生活、工作环境、医院、政府设施和车队的重要组成部分。比如：Wi-Fi打印机、智能门锁、报警系统等等。2020 年，美国居民平均拥有十多个联网设备。但出于实用性而选择物联网设备的用户还需要确保这些设备的安全。

由于物联网设备通常连接到内部家庭或公司网络，因此破坏此类设备可以为犯罪分子提供对整个系统的访问权限。2021 年前六个月，智能设备遭受了约 15 亿次攻击，攻击者试图窃取数据、挖掘加密货币或构建僵尸网络。

确保物联网设备良好安全性的一种方法是执行逆向工程活动，这将帮助您更好地了解特定设备的构建方式，并允许您对设备及其固件进行进一步分析。

在本文中，我们展示了智能空气净化器逆向工程固件的实际示例，强调了研究其架构的重要性。本文对于致力于网络安全项目、想要了解逆向工程物联网设备的细微差别和步骤的开发团队很有帮助。

**研究固件架构的重要性**

逆向工程物联网固件的过程因所研究的设备而异。

物联网设备发展得非常快，市场的主导架构一直在变化。不到十年前，最流行的选择主要是 x86 或 ARM，不太可能是 MIPS 或 PowerPC。但现在，您需要了解多种微控制器架构来对嵌入式设备进行逆向工程：Tricore、rh850、i8051、PowerPC VLE等。

深入学习单一架构不足以在物联网逆向工程中取得成功。如果开发人员有必要尽快开始逆向工程，他们应该从学习固件架构和结构的基础知识开始。

这正是我们想要在本文中描述的：逆向工程师研究他们以前从未见过的新架构和固件格式的方式。

在本文中，我们使用了小米空气净化器 3H 的固件转储。我们选择它是因为它是 ESP32 CPU（即Tensilica Xtensa 架构）的固件转储。这是一种相当奇特的架构选择，但在需要 Wi-Fi 通信的物联网设备中很常见。您可以在此 GitHub 页面上找到我们将作为本文示例进行逆向工程的固件 (ESP-32FW.bin) 。

这种情况的挑战是，没有针对固件架构的现有反编译器，并且反汇编器几乎不支持它。然而，这是逆向工程师当今面临的一个非常准确的例子。

物联网固件逆向工程过程由以下五个阶段组成：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721952112785.png "1688720794211744.png")

**1.确定架构**

在对物联网设备进行逆向工程之前要问的第一个问题是如何了解逆向工程所需的固件的架构。

最直接的找出方法是阅读 CPU 的数据表并从中了解答案。但在某些情况下，您所拥有的只是固件本身。在这种情况下，您可以使用以下两个选项之一：

1. 字符串搜索可能允许您找到一些剩余的编译字符串，其中包含有关编译器名称和体系结构的信息。

2. 二进制模式搜索要求您了解不同类型的微控制器架构中经常使用的指令。您可以在固件中搜索特定架构常见的二进制模式，然后尝试将固件加载到支持此类架构的反汇编程序中以验证您的猜测。

一旦确定了架构类型，您就可以开始选择用于进一步逆向的工具集。对于 ESP-32FW.bin，我们已经知道它将是 Tensilica Xtensa 架构，因此我们需要选择要用于研究的反汇编程序。

**2.选择反汇编工具**

在研究了可以支持 Xtensa 的适当反汇编程序后，我们最终得到了三个选项：IDA、Ghidra和Radare。

我们决定首先尝试使用 Ghidra 和 IDA，因为我们已经拥有将这些工具成功应用于不同逆向工程项目的丰富经验。由于 IDA 没有用于 Xtensa 的反编译器，只有用于反汇编器的 CPU 模块，因此我们决定首先尝试使用 Ghidra（我们使用的是 10.0 版本）。

Ghidra 默认不支持 Xtensa，因此我们需要先为 Ghidra 安装 Tensilica Xtensa 模块。

Xtensa 的反汇编程序可以工作，但反编译程序存在一些问题，如下面的屏幕截图所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721954113201.png "1688720849197569.png")

屏幕截图 1. 有关 Ghidra 反编译器中未实现指令的警告

经过一段时间的反汇编，我们意识到 Xtensa 的 Ghidra 处理器模块在多种情况下难以确定指令长度。因此，我们放弃了 Ghidra，转而使用 IDA（我们使用的是 7.7 版本）。

起初在处理器模块列表中找到 Xtensa 很困难，但最终我们在这里找到了它：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721955158512.png "1688720878102550.png")

屏幕截图 2. IDA 处理器模块列表中的 Xtensa

IDA 中的处理器模块看起来足够稳定，因此我们决定坚持使用 IDA。

**3. 加载固件**

第一步是将固件加载到正确的映像基地址，以便将所有全局变量指针解析为有效地址。为此，有必要了解代码在二进制文件中的位置。

我们首先在基地址加载固件0，并尝试标记尽可能多的代码。为了能够在 IDA 中正确标记代码，我们需要学习 Xtensa 固件常见的典型指令序列。为了找出在函数序言中使用哪些指令，我们从GitHub 中获取了一个示例：esp8266/Arduino：适用于 Arduino 的 ESP8266 核心。

编译器似乎使用了以下指令：entry a1, XX

该指令根据参数的值转换为字节序列，例如 36 41 00 / 36 61 00 / 36 81 00 XX。

通过实现一个简单的 IDA 脚本来搜索此类模式，可以标记大约 90% 的代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721957385884.png "1688721010108474.png")

屏幕截图 3. 在 IDA 中标记代码的结果

一旦我们找到了代码，就该探索并看看它看起来是否正确。

看看下面的截图，很明显有问题。字符串资源被正确引用，但call8指令指向字符串，而不是代码。并且有些call8指令指向不存在的地址。通常这意味着映像基址错误，固件必须加载到其他基址，而不是0.

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721958883970.png "1688720922914358.png")

屏幕截图 4. 发现 call8 指令指向字符串和不存在的地址

确定基地址的常见方法是：

1.选择一个字符串。

2.使用该字符串地址的低位部分查找引用它的代码。

3.找出真实的字符串地址和我们在代码中看到的地址之间的差异。因此，我们可以理解如何移动代码的地址以匹配字符串的当前地址。

在这种情况下，我们发现基地址一定是0x3F3F0000，但即使使用它，call8指令仍然无效。这可能意味着二进制数据被分段，并且闪存中的代码被分段映射到 RAM。因此，有必要将固件分割成多个片段，并将这些片段加载到 IDA 的适当段中。

我们查看了固件中的字符串，发现它确实是分段的：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721959117641.png "1688720974555618.png")

屏幕截图 5. 固件分段证明

经过进一步研究，我们发现了ESP IDF 框架。由于我们的目标固件包含该框架的某些版本，因此我们可以尝试使用其源代码来了解固件结构。

我们在 ESP IDF 内的 bootloader\_utility.c 源代码文件中发现了一个有趣的bootloader\_utility\_load\_partition\_table()函数，这意味着固件必须包含分区表。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721960414923.png "1688721028333578.png")

屏幕截图 6. bootloader\_utility\_load\_partition\_table() 函数显示固件必须包含分区表

为了识别分区表，我们继续探索源代码，最终找到了 esp\_partition\_table\_verify ()函数，该函数由bootloader\_utility\_load\_partition\_table()函数调用：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721962135064.png "1688721045193592.png")

屏幕截图 7. 发现 esp\_partition\_table\_verify() 函数

所以一定有ESP\_PARTITION\_MAGIC和ESP\_PARTITION\_MAGIC\_MD5：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721962158533.png "1688721069599903.png")

二分搜索AA 50给了我们很好的结果：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721963998570.png "1688721083137102.png")

屏幕截图 8. AA 50 的二分搜索成功结果

两者ESP\_PARTITION\_MAGIC都ESP\_PARTITION\_MAGIC\_MD5可以在附近看到。最有可能的 sub\_3F3F4848 是esp\_partition\_table\_verify()。

由于我们已经知道esp\_partition\_table\_verify函数在哪里，因此我们能够找到bootloader\_utility\_load\_partition\_table函数和 ESP\_PARTITION\_TABLE\_OFFSET 文件偏移量：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721964103134.png "1688721127148109.png")

屏幕截图 9. 查找 bootloader\_utility\_load\_partition\_table 和 ESP\_PARTITION\_TABLE\_OFFSET

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721965838481.png "1688721142162103.png")

屏幕截图 10. 查找偏移值

ESP\_PARTITION\_TABLE\_OFFSET 是 ESP32-FW.bin 文件中的文件偏移量。现在我们只需要知道分区表条目的结构。ESP IDF框架的源代码再次帮助了我们：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721966200029.png "1688721161206130.png")

我们已将这些结构导入 IDA 并将其应用到分区表数据中：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721967749070.png "1688721193200104.png")

屏幕截图 11. 将结构导入 IDA 并将其应用到分区表数据

如您所见，esp\_partition\_pos\_t.offset 是每个分区的文件偏移量，我们现在可以将 ESP32-FW.bin 拆分为分区。

但是我们如何才能将每个分区加载到适当的地址呢？似乎有一个image\_load()函数负责将固件分区映射到地址空间：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721968126817.png "1688721207130024.png")

屏幕截图 12. 将固件分区映射到地址空间

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721969686376.png "1688721223115544.png")

接下来，每个分区被分成段。在标题之后，您可以看到一个结构，后面是实际数据：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721970646058.png "1688721256149097.png")

这里，esp\_image\_segment\_header\_t.load\_addr是 CPU 地址空间中段数据的虚拟地址。

分区内的段如下所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230707/1688721970190872.png "1688721258113901.png")

现在，有了有关段的完整信息，我们可以将分区拆分为段并将它们加载到 IDA 中的适当地址。我们可以手动完成此提取工作，也可以尝试通过 IDA 加载器插件将其自动化。

尽管如此，Ghidra 似乎已经实现了这样的加载器。

本文翻译自：https://www.apriorit.com/dev-blog/reverse-reverse-engineer-iot-firmware如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou...