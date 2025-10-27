---
title: Peach Fuzzer漏洞挖掘实战
url: https://www.4hou.com/posts/kj5x
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-21
fetch_date: 2025-10-04T11:32:36.558266
---

# Peach Fuzzer漏洞挖掘实战

Peach Fuzzer漏洞挖掘实战 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Peach Fuzzer漏洞挖掘实战

盛邦安全
[漏洞](https://www.4hou.com/category/vulnerable)
2023-04-20 17:54:58

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)266081

收藏

导语：Peach Fuzzer漏洞挖掘实战

**概述**

本文主要介绍模糊测试技术，开源模糊测试框架Peach Fuzzer，最后使用Peach Fuzzer对Modbus Slave软件进行漏洞挖掘，并成功挖掘到0DAY漏洞。（文中涉及的漏洞已提交到国家漏洞库，现已修复）

**模糊测试技术**

模糊测试（Fuzz Testing）是一种黑盒测试技术，它通过自动生成一些随机、半随机或者经过分析的数据输入到程序中，来发现潜在的漏洞和错误。具体来说，模糊测试会将大量的随机数据输入到被测程序中，然后观察程序的行为，如果程序崩溃或出现异常，则说明发现了一个漏洞。模糊测试常常应用于网络协议、文件格式、解析器等需要接收输入数据并对其进行处理的软件系统。

在模糊测试中，测试用例通常是自动生成的，并尽量使其包含各种可能性的边界情况，例如最大值、最小值、非法输入、异常字符等。同时，模糊测试还可以根据具体的测试目标进行一些特定的配置，比如设置特定协议数据包的有效负载长度、使用不同的编码方式、调整模糊测试引擎的参数等。

模糊测试可以使用各种工具和框架来实现，例如American Fuzzy Lop（AFL）、Peach Fuzzer、Spike等。这些工具可以自动化生成测试用例并执行测试，同时还能够记录测试过程中产生的信息，帮助开发人员更快地定位问题。在实际应用中，模糊测试通常与其他测试技术（如静态分析、符号执行等）结合使用，以提高软件的质量和安全性。

**Peach Fuzzer框架**

Peach Fuzzer是一款基于模型的模糊测试工具，旨在帮助测试人员发现和利用软件程序中的漏洞和缺陷。它使用一种基于模型的方法，通过分析目标系统的协议、数据格式和行为规则来生成有效的测试用例。

**Peach Fuzzer具有以下特点：**

高度可定制性：

提供了一个高度可定制的框架，可以轻松地扩展和定制测试用例生成和数据分析功能，以满足各种测试需求。

模型驱动的测试：

测试过程是基于目标系统的数据模型进行的。通过对目标系统进行分析和建模，可以自动生成有效的测试用例，以验证系统的行为和规则。

多协议支持：

支持多种协议和数据格式，包括HTTP、FTP、SMTP、XML和JSON等，可以用于测试各种类型的应用程序和系统。

多平台支持：

支持多种操作系统和开发平台，包括Windows、Linux、macOS和Android等。

Peach Fuzzer框架的体系结构可以简化如下：

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973543157600.png "1681973543157600.png")

数据模型：表示输入和输出所需要的数据结构。

变异器：使用不同的变异策略，对数据执行变异。

生成器：生成字符串数据、整型数值等简单类型的数据，还可以生成复杂的分层的二进制数据，甚至是将简单的数据使用生成器拼接起来生成更复杂的数据类型的数据。

状态模型：在每个测试用例中，用户根据状态模型配置初始有限状态机，并进行维护。

代理：与测试引擎进行通信，对被测目标进行状态监视并对其进行执行控制。

测试引擎：使用解析器对pit配置文件进行解析，根据配置文件创建相应的组件并初始化，然后进入执行测试用例的主循环。

**Peach Fuzzer使用方法**

使用Peach Fuzzer进行模糊测试，最关键的是编写Pit配置文件。Pit文件是Peach Fuzzer测试用例生成器的核心配置文件，它是一种XML文件，包含多个元素，这些元素描述了测试用例生成器的数据模型、数据类型、范围、约束和默认值等信息。

Peach Pit文件通常包含以下几个部分：

Peach元素：定义Peach Pit文件的根元素。

DataModel元素：定义测试用例生成器的数据模型。数据模型由多个数据元素组成，每个数据元素表示一个测试用例的输入参数。

数据元素：定义测试用例输入参数的数据类型、范围、约束和默认值。数据元素可以是基本类型，例如整数、字符串和布尔值，也可以是复杂类型，例如结构体、数组和枚举类型。

StateModel元素：定义测试用例生成器的状态机模型。状态机模型描述了测试用例生成器的行为，例如测试用例的生成顺序、条件和转换等。

Action元素：定义测试用例生成器的动作。动作可以是发送网络数据包、写入文件、运行外部程序等。

Agent元素：定义测试用例生成器的代理。代理可以是客户端或服务器端，用于模拟测试用例的执行环境。

一个简单的Pit配置文件如下图所示：

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973611202561.png "1681973611202561.png")

**Peach Fuzzer实战**

Pit文件的编写至关重要，更多使用方法可以参考官方文档。现在，从编写简单Pit文件开始，以实际应用程序作为测试目标，熟悉和理解Pit文件的基本结构和参数配置，最后挖掘到0DAY漏洞。

首先，准备如下程序：

Peach Fuzzer程序：可从公开的源代码编译Peach Fuzzer，为简单起见，这里直接使用其他人编译后的Windows系统可执行程序Peach-3.1.124-win-x86-release。

目标程序：ModbusSlaveSetup32Bit.exe，Windows系统modbus工控协议从站模拟程序，曾被发现过漏洞。

调试器：使用Windows系统的Windbg调试程序，用于捕获模糊测试过程中的异常。

接下来安装并运行目标程序，Modbus Slave版本为7.5.1，如下图所示：

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973626205750.png "1681973626205750.png")

简单使用Modbus Slave程序，寻找可以模糊测试的功能点。在“File”菜单下的“Open”功能可以打开mbs后缀的文件。所以此次以mbs文件作为模糊测试的输入，编写Pit文件进行漏洞挖掘。

由于目前还不知道mbs文件的文件格式，所以在编写Pit文件定义数据模型时（DataModel）时，将其整个文件的内容作为模糊测时的变异数据。

定义数据模型的代码如下图所示：

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973639188542.png "1681973639188542.png")

其中Blob 元素常常用于代表缺少类型定义或格式的数据，hex表示内容为十六进制，value为空。

接下来定义状态模型，如下图所示：

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973648207803.png "1681973648207803.png")

其中Action元素中的filename的值是测试用例文件sample.mbs，这是一个空文件，需要在Peach.exe同目录下建立，StartModbusSlave是定义的调用方法。

然后再定义代理，如下图所示：

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973657311641.png "1681973657311641.png")

其中Monitor元素的class类型为WindowsDebugger，紧接着在参数WinDbgPath的Value中指定Windbg的目录（注意是文件夹），然后在CommandLine参数中指定运行目标程序打开变异后的测试用例的方法，最后在StartOnCall参数中指定调用StartModbusSlave方法。

最后定义Test元素，启动模糊测试，如下图所示：

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973669156550.png "1681973669156550.png")

其中状态模型（StateModel）元素的ref内容是之前定义的状态模型名称，Publisher元素的FileName内容是每次数据变异后保存的文件名，Logger元素的Path参数是配置的日志文件保存目录。

到此，一个针对mbs文件的模糊测试pit文件就完成了。最后执行命令Peach.exe  C:\fuzz\mbslave\_mbs\_pit.xml，启动模糊测试，如下图所示：

![图片8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973680132044.png "1681973680132044.png")

从模糊测试启动成功后，偶尔显示“File version error. Please upgrade to a newer version of Modbus Slave”对话框，如下图所示：

![图片9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973687457518.png "1681973687457518.png")

说明Modbus Slave软件在打开mbs后缀的文件时会检测文件版本，也就是说变异后的mbs文件版本不符合标准的mbs文件格式，导致模糊测试过程提前结束。

那么需要找到正确的文件版本，再调整数据模型（DataModel）的定义。使用反编译工具IDA打开mbslave.exe，根据字符串“File version error. Please upgrade to a newer version of Modbus Slave”找到对应的检查代码，如下图所示：

![图片10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973695699208.png "1681973695699208.png")

可以看到，确实检查了文件版本。经逆向分析，版本数据在mbs文件的前4个字节。此处选用最小的版本0xFA0进行测试，修改数据模型（DataModel）的配置，让其前4个字节固定为“A0 0F 00 00”，不参与数据变异，这样就可以通过版本检查代码。修改后的数据模型配置，如下图所示：

![图片11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973702315688.png "1681973702315688.png")

然后将sample.mbs的前4个字节也修改为“A0 0F 00 00”，如下图所示：

![640 (1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973782173021.png "1681973782173021.png")

最后执行命令Peach.exe  C:\fuzz\mbslave\_mbs\_pit.xml，启动模糊测试，很快就捕获到了多个异常，如下图所示：

![图片12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973796191422.png "1681973796191422.png")

进入logs目录，找到EXPLOITABLE相关的文件夹，其下存放的1.Initial.Action.bin的文件就是漏洞触发的mbs文件，如下图所示：

![图片13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973805111905.png "1681973805111905.png")

![图片14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973812121409.png "1681973812121409.png")

根据调试器的日志文件，可以看到EIP寄存器已被定义为0x994a4f1d，这是一个不存在的地址，导致了异常，如下图所示：

![图片15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230420/1681973821104170.png "1681973821104170.png")

至此，成功挖掘到一个0day漏洞。后经逆向分析，这是一个缓冲区溢出漏洞，感兴趣的读者可以自行调试。

**项目地址**

https://github.com/webraybtl/PeachFuzzer

**概述**

https://bbs.kanxue.com/thread-270106-1.htm

https://github.com/TideSec/Peach\_Fuzzing

https://www.freebuf.com/articles/ics-articles/219996.html

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6V5HSQ31)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* ...