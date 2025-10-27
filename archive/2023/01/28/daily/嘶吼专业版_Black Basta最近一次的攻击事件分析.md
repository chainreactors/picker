---
title: Black Basta最近一次的攻击事件分析
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247556797&idx=2&sn=c721885066dab480c4fcd1b53c35ef77&chksm=e915ce87de624791151180aeeecb19d6a27b55b7717f0cc21cccaa52a1d84c9d0615df5d88ee&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-01-28
fetch_date: 2025-10-04T05:04:30.230991
---

# Black Basta最近一次的攻击事件分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1GBgWCaIPRA5UfFTF6bf0D2M5rDGSzqTD9mfQV2nEONKkVX1rJYicwuw/0?wx_fmt=jpeg)

# Black Basta最近一次的攻击事件分析

xiaohui

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1NDic9R4X3hOOWg9AAjI3P6Riaib2SApwbnTJbUn3uwib8kKsG90bdm1icEA/640?wx_fmt=png)

根据Check Point在2022年上半年的报告，每40个组织中就有1个受到勒索软件攻击的影响，这比去年增加了59%。勒索软件之所以如此猖狂，原因就是获利巨大。随着双重勒索的增加，勒索软件攻击变得更加吸引人：即使受害者拒绝支付，被盗的私人数据可能会在黑市上以相当大的价格出售。

自2022年5月以来，累计有89多起知名组织被Black Basta组织攻击。数据显示，该组织的攻击目标明显位于美国和德国，49%的受害者是美国用户。在某些情况下，赎金甚至超过100万美元。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1N4blZu29ZSwYBiaxavmNCcgHO1NKj77m0xZpXQZ2U1amZLESLGUefjA/640?wx_fmt=png)

接下来，我将介绍Black Basta活动的技术细节，以及各种规避和反分析技术。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)技术细节

在攻击开始之前，幕后组织必须将勒索软件传播到受害者的设备。凭借先进的传播技术，滴管有不同的方式将其有效载荷下载到选定的受害者设备，不过也可能会出现不同滴管模块的组合使用（比如QakBot和Cobalt Strike有效载荷的组合），最终导致勒索软件的执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd18aTlicd0R6MoFXibQ1FQDxAw5icOxed7HCibnD3YxvJCkQbyt17E340GicA/640?wx_fmt=png)

Black Basta向受害者的设备发送勒索软件的可能方式

我们观察到，滴管可以比技术上简单的勒索软件有效载荷复杂得多。我们将在下面介绍Black Basta勒索软件的最终传播阶段。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)传播阶段

Black Basta滴管模仿了创建此网站上托管的USB可引导驱动器的应用程序：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd15ZUibIMZt4DeTTsje25AIzicZOyUxJlicKwhL6eEberxhIPNNGEhsE7vA/640?wx_fmt=png)

Black Basta滴管的图标和介绍

应用程序使用与Rufus网站上合法可执行文件相同的证书（由“Akeo Consulting”颁发）进行数字签名：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1t0P3qPg5CrrMYA1a7zkZ7PRqrgAQVllQibFTLia8Zhb8N6BlT3yBoJbA/640?wx_fmt=png)

Black Basta滴管和证书颁发者的数字签名

有关如何使用经过验证的数字签名创建恶意应用程序的更多信息，请参阅Check Point研究团队的文章。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)规避和反分析技术

在Black Basta滴管中实现了很多反调试技巧，下面按类别列出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1ibqibueQ82WyIOaH785afsnfMe4TzW02oNXibluicibHBKrgAISibvodBGkw/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)Black Basta滴管中的反调试和规避技术

如果这些技术中的任何一种成功地检测到调试器或仿真环境，则滴管将停止执行并退出，而不启动Black Basta。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)系统标志

这组反调试技术依赖于进程内结构来检查状态：是否正在调试。

PEB: is debugger present；

PEB: being debugged；

PEB: NtGlobalFlag；

CheckRemoteDebugger；

Check kernel debugger；

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)CPU寄存器

下面分组的技术使用CPU寄存器检查进程是否正在调试。

设置陷阱标志；

检查陷阱标志，同上。标志未设置，只是选中；

检查HW断点（链接中的方法1）；

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)CPU指令

这些技术通过直接调用或包装器使用CPU指令来检查进程是否正在调试。

DebugBreak；

INT 2D；

INT3；

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)定时检查

这些技术执行定时检查，以查看经过调试的进程与没有调试器运行的进程之间的差异。

RDTSC；

QueryPerformanceCounter；

GetTickCount；

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)库检查

这种技术依赖于这样一个假设，即在通常的系统中有一些通用的系统库可以毫无问题地加载，还有一些不常见的库不应该真正出现在典型的系统中。然而，在沙盒环境中，当试图加载一个不常见的库时，在这种情况下可能返回预定义的代码，而不是在非模拟设备中返回的代码。返回代码的差异可以用来检测沙盒。

**必须加载的库**

kernel32.dll；

networkexplorer.dll；

NlsData0000.dll；

**不能加载的库**

NetProjW.dll；

Ghofr.dll；

fg122.dll；

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)Windows API检查

下面的一组技术使用Windows API函数来检测进程是否正在调试。

VirtualAlloc与GetWriteWatch结合使用；

具有错误介绍符的CloseHandle；

OutputDebugString检查最后的系统错误；

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)被污染的日志

这种技术并不是真正的反调试器，但会使日志分析更加困难。重点是随机调用kernel32.beep函数。你可以在这个沙盒分析中看到更多内容。

由于编码错误导致检查失败

这些检查应该使用仿真环境或已调试进程的细节，但由于编码错误而无法正常工作。

FindWindow（类名：▬unAwtFrame）——名称中的第一个符号是错误的，应该是SunAwtFrame；

NtQueryInformationProcess, check DebugPort——由于dll名称错误而无法工作；

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)模糊转储

成功躲避检测后，Black Basta滴管又进行了模糊转储。Black Basta有效载荷不是简单地解压缩并在内存中执行的，存在位于勒索软件的PE标头之前的数据是为了防止自动扫描器容易识别恶意有效载荷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1XVVOlwA9cRWibvKUsd0ibzchaAn1EfZKj27OP0cLd9cXRvffeBTBbFsg/640?wx_fmt=png)

位于PE标头之前的数据，以防止自动内存分析

正如预期的那样，WinDbg中的imgscan命令无法显示dropper进程内存中的Black Basta PE模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1RUmPUqJEDx7hIlFuAK67adoAxLReqYNz3KEDbsjicabvKbaRqJMhhag/640?wx_fmt=png)

WinDbg内存扫描中缺少Black Basta模块

在完成所有这些步骤之后，实际的Black Basta有效载荷被执行。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)Black Basta有效载荷

在勒索软件开始执行时创建互斥锁，以确保只有一个恶意软件副本处于活动状态：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1T6w9HOlDkHjAK1SKzyCek4JZdOe64dm4TBQGpIzibdRagib5NemRDDPg/640?wx_fmt=png)

在Black Basta中创建互斥锁

在我们介绍的示例中，互斥锁的名称是“dsajdhas.0”。

然后，恶意软件设置壁纸，并为扩展名为“.basta”的文件指定一个自定义图标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd13ItJiab7CpTAsnPbiaDvibAxveicdV8f71IRoQPBmXQFic9QwmAJpAeSEOw/640?wx_fmt=png)

Black Basta释放的图像

这些图像来自Black Basta解压缩它们的TEMP目录。

该勒索软件还试图删除任何卷影副本，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1EdljfBICdqSCPWPDuFgDhJjviaEyLrLp4QOHfqgw1B6GQyHJTmnHw4g/640?wx_fmt=jpeg)

删除卷影副本所执行的命令

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)加密

创建多个线程来进行多线程加密过程：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd10g7eOL5qUvt82y47y5VibjRD1hTeZic0lXWl2fwibRykibYab4WTfyqa7w/640?wx_fmt=jpeg)

创建用于执行加密的线程

恶意软件会加密驱动器上找到的所有文件，路径中包含以下字符串的文件除外：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1bgsbEdibkMDHaY2IycxuEK2GcVCR95Db8mpC80xjzV2Lfu9Wca9Lt8w/640?wx_fmt=png)

ChaCha20流密码（其比AES更快）用于加密，每个加密文件随机生成密钥。然后将该密钥传递给带有硬编码公钥的RSA加密，以检索512字节的加密ChaCha20密钥。此密钥附加到加密文件的末尾：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1ciczF0nDXsnv98C63fC3T7BUoog9JRMFQRNibBe4Otc7OywlJ6dVL7fg/640?wx_fmt=jpeg)

文件末尾的加密密钥开始（左侧）；原始文件（右侧）

在块的末尾，还有加密密钥的长度（0x200）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1DcB5HrsxYjgLQ8SEJP8tTR0RVD1xrvVDMhfIkDCx9hx4yny3yUCRAQ/640?wx_fmt=png)

加密文件末尾的密钥长度

请注意，并不是整个文件都被加密。恶意软件针对每个64字节的第三个块：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd14tpLpsz6hib3EoNYUPZVvDJ4M2caSTfA6gialxW7PvP55RbTcJ5TpnicQ/640?wx_fmt=png)

由Black Basta加密的块（左侧）；原始文件（右侧）

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1wwlmO86duQukuy9c3DqvL7GRG9jN8g76o1V1WeVDr5gHRzQc8G2d0Q/640?wx_fmt=png)要处理文件，通常使用kernel32函数

CreateFile；

ReadFile；

WriteFile；

MoveFile (重命名加密文件)；

作为附带说明，我们需要提到使用了RSA的mini GMP实现。

加密完成后，勒索软件会在桌面上的“readme.txt”文件中释放一条勒索说明。公司ID被硬编码在勒索信中，这是有针对性和有准备的攻击的标志：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iciaWY0EjxaZ0OslmOIQCrd1y8ypT6fxjPSYIIfoXUc2N7iapj4hg3bF7hwEokCQwSC7iaYorqoS3gaQ/640?wx_fmt=png)

在示例中硬编码的公司ID

在不知道RSA私钥的情况下，没有明显的方法来解密文件。

# ![](https://mm...