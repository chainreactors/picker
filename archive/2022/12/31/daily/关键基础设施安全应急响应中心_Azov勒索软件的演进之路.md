---
title: Azov勒索软件的演进之路
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247533634&idx=2&sn=f78b1867cfbef858b51ca68eeaaea77b&chksm=c1e9c813f69e4105818964a0c830d8b90d39df9e235604d13919662477e61e5887938a606f2c&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-12-31
fetch_date: 2025-10-04T02:48:13.094096
---

# Azov勒索软件的演进之路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogu0Z7V8QibUtzmyhy5231WkIhdqeJwJ14oEZuFlT8w7ro9F8e1Zdk0WXxtUILKMGwMbG9Y79vZacww/0?wx_fmt=jpeg)

# Azov勒索软件的演进之路

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogu0Z7V8QibUtzmyhy5231WkIvliarrF8NxLRscQEStw89yPuNLzJhznSeogAElgIvalt94oD8CPEGhA/640?wx_fmt=png)

Check Point Research（CPR）对臭名昭著的Azov勒索软件进行了分析，分析表明，Azov能够修改某些64位可执行文件以执行自己的代码。在过去的几周里，CPR在其社交媒体以及Bleeping Computer上分享了对Azov勒索软件的初步调查结果。接下来，我们将介绍Azov勒索软件的内部工作原理及其技术特点。

# **主要发现**

Azov最初是作为SmokeLoader僵尸网络的有效负载而引起注意的，该僵尸网络通常存在于假冒盗版软件和破解网站中。

Azov与普通勒索软件不同的是它对某些64位可执行文件的修改以执行自己的代码。在现代互联网出现之前，这种行为曾经是恶意软件泛滥的必经之路。可执行文件的修改是使用多态代码来完成的，这样就不会被静态签名潜在地破坏，并且也适用于64位可执行文件。

这种对受害者可执行文件的攻击性多态感染导致了大量感染Azov的公开可用文件。每天都有数百个与Azov相关的新样本提交给VirusTotal，截至2022年11月，该样本已超过17000个。使用手工制作的查询，可以只搜索正确的Azov样本，而不使用木马化的二进制文件。

VirusTotal查询以搜索与Azov相关的样本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObGjJNxzUZbqiayZQUspZXr73VjiaRyibrkqYicN7Wetv2Ojgu5o3AGNFdMA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZOb4dQ6ia3a4NFm3qTn5BouGahagmvaIxeYwQQ2YDhwoq3L6T3IWibwia15g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

VirusTotal查询——Azov相关样本

VirusTotal查询仅搜索正确的Azov样本，而不搜索木马化二进制文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObEXxIx9RmzwSJMjCBibslicIpYSyOtxSR7YTV1gicdib2HaHC0kZDcMm8qg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

VirusTotal查询——仅原始Azov样本

丰富的样本使我们能够区分Azov的两个不同版本，一个更老，一个稍新。这两个版本共享它们的大部分功能，但较新版本使用了不同的勒索通知，以及销毁文件的不同文件扩展名（.azov）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObicbl9vu9o2jrhr31G1sULEcGEskEresWuEsjTdaicLTvlsC5ibN4fK7QA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

新版本的Azov的赎金通知

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObGXT2QicLSHU1TQEAMCAvbz3iacYLUpicCmVpKB2n5LgjzBXFEJLN5ickhg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

旧版本的Azov的赎金通知

# **技术分析**

使用FASM在程序集中手动制作；

使用反分析和代码混淆技术；

原始数据内容的多线程间歇性覆盖（循环666字节）；

在受损系统中后门64位“.exe”文件的多态方式；

“逻辑炸弹”设定在特定时间引爆。下面分析的样本被设置为在UTC时间2022年10月27日上午10:14:30引爆；

没有网络活动，没有数据泄露；

利用SmokeLoader僵尸网络和木马程序进行传播；

有效、快速且不幸无法恢复的数据清除器；

研究人员专注于新Azov版本的原始样本（SHA256:650f0d694c0928d88aeeed649cf629fc8a7bec604563bca716b1688227e0cc7e-如上所述，与旧版本相比，功能上没有重大差异）。这是一个64位的可移植可执行文件，已用FASM（平面汇编程序）组装，只有1段.code (r+x)，并且没有任何导入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObm3FaH0nibVL1wtBuICjMjWZWFhXErGyAf1G2dop6ywyGPYj7Qdfc86g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

FASM编译器的检测

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObI9sqo06sVbw7OtA2VGxicmZHJE2zL87t58sIcSHuic67NsYbgKRzZJfA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

只有一个“.code”部分，没有导入

code字段分为三个部分，通过查看其熵最容易看出。首先，有一个高熵部分包含加密的shell代码。之后是实现解包程序的纯代码，然后是熵非常低的最后一部分，似乎由用于构造勒索信的纯字符串组成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObxaiba6k6PbTs6DntHUAQB4RRRPYyWbl4ysibmVZQeEMUsU5675G8gbkA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

“.code”部分的熵

# **打开程序**

由于Azov的整个代码都是手工编写的，因此有必要执行一些IDA魔术和清理工作，以将代码塑造成可以反编译和理解的状态。完成此操作后，过程start\_0()就可见了。这段代码将shellcode解包到新分配的内存中，然后将执行传递给它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZOb18Ek1glRGbicap2q1fjIicWlkiahv91dZCnvEPg4PtV4UaeRDdF25HPxw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

输入函数start\_0

函数AllocAndDecryptShellcode()中的解包程序被故意创建得看起来比实际更复杂。但实际上，它是一个简单的种子解密算法，使用xor和rol的组合，其中key = 0x15C13。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZOb668jiaibDmO2j3XNp8DmXJuLAwpZkFOicCqIlAUGDZghRYXXEjpkicrhLQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

AllocAndDecryptShellcode函数中的解包程序

我们在下面提供了简化程序逻辑的Python实现：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZOb4YKGqxoxfnJAyHic1HZpvcjTHrpk8Km82BDGOeVGxETPOicIH07qVm8g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

下一阶段分为两个主要程序：一个负责清除文件，另一个负责为可执行文件设置后门。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZOblzUWEGZvicHs9dcPzqvZbMGL57D3S8vWjVPH7FxqHaGboiaOjWCDribEA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

将执行转移到清除和后门逻辑

# **清除程序**

清除程序首先创建一个互斥锁（Local\\\\azov），以验证恶意软件的两个实例没有同时运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObYOic5fwyAdZqmzoNmuv7ZzgFDw9D9mENNHMvClEbTgRXG97dpA6KM1Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

清除程序——互斥锁创建

如果成功获得互斥锁句柄，Azov会通过木马(类似于后门程序)64位Windows系统二进制文件msiexec.exe或perfmon.exe并将其保存为rdpclient.exe来创建持久性。在SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run上创建一个注册表项，指向新创建的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObhvWcwfjLBmo96DrXOVdHMHczu7AWjzpje2A4FiawUu3r4WvXiarplhnw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

持久性创建

清除程序使用触发时间——有一个循环，被分析的样本检查系统时间，如果不等于或大于触发时间，则休眠10秒，然后再次循环。样本触发时间为2022年10月27日。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObfWpjHjTh6vHHykQaYbgnH4y51Zwj53xczGf7pa9XGLRbsrN7TDMicgQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

样本触发时间为2022年10月27日

一旦这个逻辑炸弹被触发，清除器逻辑就会遍历所有设备目录，并对每个目录执行清除程序，从而避免某些硬编码的系统路径和文件扩展名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObFC0UMgFicnKwlHWA3SzXx7UuTtYqlsUbqy1jcTyuetDp2hyte5icWCuQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

系统路径和文件扩展名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObn3FQ6fJsDNnWWLJFXb7J7PMLqRVF6q0kjoDzajSqF6PJolFL2KgM5Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

清除时省略的文件扩展名

每个文件都被“间歇性”清除，这意味着666字节的块被随机噪声覆盖，然后一个大小相同的块保持完整，然后一块再次被覆盖，依此类推，直到达到4GB的硬限制，此时所有其他数据都保持完整。作为随机源，样本使用未初始化的局部变量（例如，char buffer[666]），这实际上意味着随机堆栈内存内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObHQ0xibbBABmJJicicdRPuLuCHTqYY5WF9mw8Nuy5NoIWNDKKrJPeBIqJg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

间歇性数据清除

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObwiaQiatdhWR7ewXdl1icI6HArMriaOjf5LjVOjBnON57Xqib0l1JBdz1egQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

数据清除程序的示例跟踪

清除完成后，新的文件扩展名.azov将添加到原始文件名中。清除文件的典型文件结构如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObBkuVRXMaZCgnX22ic50snSYuGSjL6hCTpHLbfpibSnt1Zqib17I7PbhPA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

清除文件的示例结构

# **后门程序**

在遍历文件系统以搜索要进入后门的文件之前，创建一个名为Local\\\\Kasimir\_%c的互斥锁，其中%c替换为正在处理的驱动器的字母。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObQZe5SEov9eibic0wZpFWN1sUQHY7BhQnAlQcNznL32xjv3ZXIGoZMs0g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

后门程序——互斥锁创建

TryToBackdoorExeFile()函数负责解密满足特定条件的64位“.exe”文件进行后门。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObspaaYr2tSyAY5QJGRyJmdD2WVamvYf57qicro1S7XHlLcxiasqmNl1Kw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

通过预处理条件的文件进入TryToBackdoorExeFile函数

这些具体条件可简化如下：

预处理条件：

它不是文件系统位置清除列表的一部分；

文件扩展名为“.exe”；

文件大小小于20MB；

处理条件：

该文件是64位可执行文件；

包含入口点的PE部分有足够的空间用于注入shellcode植入程序，以保留PE的原始入口点（shellcode起始地址将放在原始入口点的地址）；

File size == PE size（PE大小是手动计算的）；

处理条件都在TryToBackdoorExeFile()函数中检查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObxjo6bxib3PrModCYCGXJoNtrjiboY90icAwDZqMGIZeb3DJPvCTopFvqw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

TryToBackdoorExeFile函数

一旦文件满足所有预处理和处理条件，它就被认为适合适合进行后门操作，并将其推入BackdoorExeFile()函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObLR0qcjdibGSLPLaMiaYV9zXmjtNqlzDiaGz13uwuiaIG5GTEPPAbFY0LIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

函数TryToBackdoorExeFile的邻近图

函数BackdoorExeFile()负责可执行文件的多态后门。它首先获取原始代码段(通常是.text段)的地址，然后在几个位置随机修改其内容。在将shellcode的主要blob注入到修改的代码部分之前，某些常量值将被更改，整个shellcode将使用与前面描述的恶意软件解包期间使用的相同的加密算法和密钥重新加密。后门文件写回磁盘后，三个编码的数据结构被追加到它的末尾，这是勒索软件运行所需的有效资源(例如，一种模糊形式的勒索通知)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObLR0qcjdibGSLPLaMiaYV9zXmjtNqlzDiaGz13uwuiaIG5GTEPPAbFY0LIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

函数BackdoorExeFile的邻近图

尽管存在多态后门，但解包和后门过程中使用的加密/解密算法是一致的，可用于Azov检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jLicYe6UtAoqdPuMjP2ZObsEe85C7ib10dAS6RAovnIPWxIsh3mBguCGnnNjERD1luibCxMUBsDqsw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&...