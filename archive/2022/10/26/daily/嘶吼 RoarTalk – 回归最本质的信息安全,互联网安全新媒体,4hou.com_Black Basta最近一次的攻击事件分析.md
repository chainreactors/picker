---
title: Black Basta最近一次的攻击事件分析
url: https://www.4hou.com/posts/YX9O
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-26
fetch_date: 2025-10-03T20:51:28.247301
---

# Black Basta最近一次的攻击事件分析

Black Basta最近一次的攻击事件分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Black Basta最近一次的攻击事件分析

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-10-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)136252

收藏

导语：本文将介绍Black Basta活动的技术细节，以及各种规避和反分析技术。

![微信截图_20221024152448.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596701100095.png "1666596701100095.png")

根据Check Point在2022年上半年的报告，每40个组织中就有1个受到勒索软件攻击的影响，这比去年增加了59%。勒索软件之所以如此猖狂，原因就是获利巨大。随着双重勒索的增加，勒索软件攻击变得更加吸引人：即使受害者拒绝支付，被盗的私人数据可能会在黑市上以相当大的价格出售。

自2022年5月以来，累计有89多起知名组织被Black Basta组织攻击。数据显示，该组织的攻击目标明显位于美国和德国，49%的受害者是美国用户。在某些情况下，赎金甚至超过100万美元。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596709140122.png "1666596709140122.png")

接下来，我将介绍Black Basta活动的技术细节，以及各种规避和反分析技术。

**技术细节**

在攻击开始之前，幕后组织必须将勒索软件传播到受害者的设备。凭借先进的传播技术，滴管有不同的方式将其有效载荷下载到选定的受害者设备，不过也可能会出现不同滴管模块的组合使用（比如QakBot和Cobalt Strike有效载荷的组合），最终导致勒索软件的执行。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596718168681.png "1666596718168681.png")

Black Basta向受害者的设备发送勒索软件的可能方式

我们观察到，滴管可以比技术上简单的勒索软件有效载荷复杂得多。我们将在下面介绍Black Basta勒索软件的最终传播阶段。

**传播阶段**

Black Basta滴管模仿了创建此网站上托管的USB可引导驱动器的应用程序：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596727219215.png "1666596727219215.png")

Black Basta滴管的图标和介绍

应用程序使用与Rufus网站上合法可执行文件相同的证书（由“Akeo Consulting”颁发）进行数字签名：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596735778991.png "1666596735778991.png")

Black Basta滴管和证书颁发者的数字签名

有关如何使用经过验证的数字签名创建恶意应用程序的更多信息，请参阅Check Point研究团队的文章。

**规避和反分析技术**

在Black Basta滴管中实现了很多反调试技巧，下面按类别列出。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596744270128.png "1666596744270128.png")

**Black Basta滴管中的反调试和规避技术**

如果这些技术中的任何一种成功地检测到调试器或仿真环境，则滴管将停止执行并退出，而不启动Black Basta。

**系统标志**

这组反调试技术依赖于进程内结构来检查状态：是否正在调试。

PEB: is debugger present；

PEB: being debugged；

PEB: NtGlobalFlag；

CheckRemoteDebugger；

Check kernel debugger；

**CPU寄存器**

下面分组的技术使用CPU寄存器检查进程是否正在调试。

设置陷阱标志；

检查陷阱标志，同上。标志未设置，只是选中；

检查HW断点（链接中的方法1）；

**CPU指令**

这些技术通过直接调用或包装器使用CPU指令来检查进程是否正在调试。

DebugBreak；

INT 2D；

INT3；

**定时检查**

这些技术执行定时检查，以查看经过调试的进程与没有调试器运行的进程之间的差异。

RDTSC；

QueryPerformanceCounter；

GetTickCount；

**库检查**

这种技术依赖于这样一个假设，即在通常的系统中有一些通用的系统库可以毫无问题地加载，还有一些不常见的库不应该真正出现在典型的系统中。然而，在沙盒环境中，当试图加载一个不常见的库时，在这种情况下可能返回预定义的代码，而不是在非模拟设备中返回的代码。返回代码的差异可以用来检测沙盒。

**必须加载的库**

kernel32.dll；

networkexplorer.dll；

NlsData0000.dll；

**不能加载的库**

NetProjW.dll；

Ghofr.dll；

fg122.dll；

**Windows API检查**

下面的一组技术使用Windows API函数来检测进程是否正在调试。

VirtualAlloc与GetWriteWatch结合使用；

具有错误介绍符的CloseHandle；

OutputDebugString检查最后的系统错误；

**被污染的日志**

这种技术并不是真正的反调试器，但会使日志分析更加困难。重点是随机调用kernel32.beep函数。你可以在这个沙盒分析中看到更多内容。

由于编码错误导致检查失败

这些检查应该使用仿真环境或已调试进程的细节，但由于编码错误而无法正常工作。

FindWindow（类名：▬unAwtFrame）——名称中的第一个符号是错误的，应该是SunAwtFrame；

NtQueryInformationProcess, check DebugPort——由于dll名称错误而无法工作；

**模糊转储**

成功躲避检测后，Black Basta滴管又进行了模糊转储。Black Basta有效载荷不是简单地解压缩并在内存中执行的，存在位于勒索软件的PE标头之前的数据是为了防止自动扫描器容易识别恶意有效载荷。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596756765887.png "1666596756765887.png")

位于PE标头之前的数据，以防止自动内存分析

正如预期的那样，WinDbg中的imgscan命令无法显示dropper进程内存中的Black Basta PE模块。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596769409348.png "1666596769409348.png")

WinDbg内存扫描中缺少Black Basta模块

在完成所有这些步骤之后，实际的Black Basta有效载荷被执行。

**Black Basta有效载荷**

在勒索软件开始执行时创建互斥锁，以确保只有一个恶意软件副本处于活动状态：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596778986845.png "1666596778986845.png")

在Black Basta中创建互斥锁

在我们介绍的示例中，互斥锁的名称是“dsajdhas.0”。

然后，恶意软件设置壁纸，并为扩展名为“.basta”的文件指定一个自定义图标。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596789202691.png "1666596789202691.png")

Black Basta释放的图像

这些图像来自Black Basta解压缩它们的TEMP目录。

该勒索软件还试图删除任何卷影副本，如下图所示：

![10.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596809286115.jpeg "1666596809286115.jpeg")

删除卷影副本所执行的命令

**加密**

创建多个线程来进行多线程加密过程：

![11.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596820209573.jpeg "1666596820209573.jpeg")

创建用于执行加密的线程

恶意软件会加密驱动器上找到的所有文件，路径中包含以下字符串的文件除外：

> ```
> $Recycle.Bin
> Windows
> Documents and Settings
> Local Settings
> Application Data
> txt
> Boot
> txt
> jpg
> DAT
> ico
> ```

ChaCha20流密码（其比AES更快）用于加密，每个加密文件随机生成密钥。然后将该密钥传递给带有硬编码公钥的RSA加密，以检索512字节的加密ChaCha20密钥。此密钥附加到加密文件的末尾：

![12.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596830103832.jpeg "1666596830103832.jpeg")

文件末尾的加密密钥开始（左侧）；原始文件（右侧）

在块的末尾，还有加密密钥的长度（0x200）：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596840154446.png "1666596840154446.png")

加密文件末尾的密钥长度

请注意，并不是整个文件都被加密。恶意软件针对每个64字节的第三个块：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596851638360.png "1666596851638360.png")

由Black Basta加密的块（左侧）；原始文件（右侧）

**要处理文件，通常使用kernel32函数**

CreateFile；

ReadFile；

WriteFile；

MoveFile (重命名加密文件)；

作为附带说明，我们需要提到使用了RSA的mini GMP实现。

加密完成后，勒索软件会在桌面上的“readme.txt”文件中释放一条勒索说明。公司ID被硬编码在勒索信中，这是有针对性和有准备的攻击的标志：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596866215538.png "1666596866215538.png")

在示例中硬编码的公司ID

在不知道RSA私钥的情况下，没有明显的方法来解密文件。

**自动分配**

Black Basta具有内置的网络自动传播功能，这是为了预防滴管的功能不足以完成任务。勒索软件尝试在LDAP API的帮助下连接到AD，并使用过滤器字符串（samAccountType=805306369）遍历连接的工作站：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666596881161658.png "1666596881161658.png")

通过连接的工作站启动搜索的函数

获得工作站列表后，勒索软件尝试通过路径\\c$\\Windows\\tmp.exe将自己复制到远程计算机。然后，在COM对象objectIWbemClassObject (CLSID: 4590f812 - 1d3b - 11d0 - 891f - 00aa004b2e24)和IWbemServices->Win32\_Process的帮助下，通过Create方法启动前一阶段复制的可执行文件。

**总结**

勒索软件攻击是受害者可能面临的最严重威胁之一。当代勒索软件攻击有大量成功勒索的记录，并且可以在网络内横向移动，因此在使用双重勒索方案时，可以获得越来越多有保证的回报。

新出现的Black Basta就是一个非常成功的勒索软件组织，它采取了各种预防措施，并执行了实际的数据加密，例如应用的反调试和逃避技术。

如上所述，勒索软件本身的设计不仅能够在最短的时间内造成最大的伤害，而且传播阶段也非常隐蔽、复杂和有效。Black Basta会确保在安全的环境中运行，并且有机会执行加密。

为了降低遭受类似攻击的可能性，组织应采取以下做法：

1.教育员工如何在网络安全领域保持安全；

2.不要打开来自陌生发件人的件；

3.更新并提高网络基础设施的安全性。

4.定期备份敏感数据并将其存储在其他外部驱动器上。

5.保持系统保更新到最新版本。

本文翻译自：https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?UWTNLZ9i)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析]...