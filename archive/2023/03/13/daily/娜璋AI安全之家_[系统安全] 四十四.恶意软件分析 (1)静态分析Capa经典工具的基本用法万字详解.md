---
title: [系统安全] 四十四.恶意软件分析 (1)静态分析Capa经典工具的基本用法万字详解
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247497871&idx=1&sn=449e986f0c95b0b37fe758635de4aef9&chksm=cfcf4842f8b8c1540032a0e14a04c940f03af6f1a963c8b5241ef1987c1c770f3bacbb40de4d&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2023-03-13
fetch_date: 2025-10-04T09:25:39.528390
---

# [系统安全] 四十四.恶意软件分析 (1)静态分析Capa经典工具的基本用法万字详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06jTVDbPLtYsMR0qZ3gIbnC2rvIaxKN9Hc8fXYllMWMzgad4eNP4fvPA/0?wx_fmt=jpeg)

# [系统安全] 四十四.恶意软件分析 (1)静态分析Capa经典工具的基本用法万字详解

原创

eastmount

娜璋AI安全之家

最近真的太忙了，天天打仗一样，感谢大家的支持和关注。继续加油！该系列文章将系统整理和深入学习系统安全、逆向分析和恶意代码检测，文章会更加聚焦，更加系统，更加深入，也是作者的慢慢成长史。漫漫长征路，偏向虎山行。享受过程，一起加油~

**前文详细介绍恶意代码同源分析和BinDiff软件基础用法，包括恶意代码同源分析原理、BinDiff工具的原理知识和安装过程、BinDiff软件基础用法和Diaphora开源工具。这篇文章将详细讲解恶意代码静态分析经典工具Capa的基础用法，它是FireEye团队开源的工具，旨在自动化提取样本的高级静态特征，快速挖掘样本的恶意行为，同时支持IDA插件操作，方便安全人员快速定位恶意代码，且能与ATT&CK框架和MBC映射。基础性文章，希望对您有帮助，如果存在错误或不足之处，还请海涵。且看且珍惜。**

**作者作为网络安全的小白，分享一些自学基础教程给大家，希望你们喜欢。同时，这些大佬是真的值得我们去学习，献上小弟的膝盖~fighting！**

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE064LFcuH1OqMNNb5pTg0Qv6OjjicTjU7RNwZTJrcibDmTDbKicRUAuuHgiaA/640?wx_fmt=png)

希望这些基础原理能更好地帮助大家做好防御和保护，基础性文章，希望对您有所帮助。作者作为网络安全的小白，分享一些自学基础教程给大家，主要是在线笔记，希望您们喜欢。同时，更希望您能与我一起操作和进步，后续将深入学习网络安全和系统安全知识并分享相关实验。总之，希望该系列文章对博友有所帮助，写文不易，大神们不喜勿喷，谢谢！如果文章对您有帮助，将是我创作的最大动力，点赞、评论、私聊均可，一起加油喔！

文章目录：

* **一.恶意软件分析**

* 1.静态特征
* 2.动态特征

* ****二.Capa简介****

* 1.基础知识
* 2.CAPA原理详解

* **三.Capa基本用法**

+ 1.静态特征提取
+ 2.特征分析

* ****四.Capa文件存储及ATT&CK映射****

+ 1.特征提取
+ 2.文件存储

* ****五.批量提取PE文件静态特征****
* ****六.总结****

作者的github资源：

* 逆向分析：

* https://github.com/eastmountyxz/

  SystemSecurity-ReverseAnalysis

* 网络安全：

+ https://github.com/eastmountyxz/

  NetworkSecuritySelf-study

作者作为网络安全的小白，分享一些自学基础教程给大家，主要是关于安全工具和实践操作的在线笔记，希望您们喜欢。同时，更希望您能与我一起操作和进步，后续将深入学习网络安全和系统安全知识并分享相关实验。总之，希望该系列文章对博友有所帮助，写文不易，大神们不喜勿喷，谢谢！如果文章对您有帮助，将是我创作的最大动力，点赞、评论、私聊均可，一起加油喔！

![](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDROZ0FiaQhr7u82U6dJibrM3VO0dUcD3EMLylohBICfH8ibt9D8T7r2jcvDCAFuf4VR5IhcypN5mvCSVg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

> 声明：本人坚决反对利用教学方法进行犯罪的行为，一切犯罪行为必将受到严惩，绿色网络需要我们共同维护，更推荐大家了解它们背后的原理，更好地进行防护。（参考文献见后）

---

# 一.恶意软件分析

恶意软件或恶意代码分析通常包括静态分析和动态分析。特征种类如果按照恶意代码是否在用户环境或仿真环境中运行，可以划分为静态特征和动态特征。

那么，如何提取恶意软件的静态特征或动态特征呢？ 因此，第一部分将简要介绍静态特征和动态特征。

## 1.静态特征

没有真实运行的特征，通常包括：

* 字节码

  ：二进制代码转换成了字节码，比较原始的一种特征，没有进行任何处理
* IAT表

  ：PE结构中比较重要的部分，声明了一些函数及所在位置，便于程序执行时导入，表和功能比较相关
* Android权限表

  ：如果你的APP声明了一些功能用不到的权限，可能存在恶意目的，如手机信息
* 可打印字符

  ：将二进制代码转换为ASCII码，进行相关统计
* IDA反汇编跳转块

  ：IDA工具调试时的跳转块，对其进行处理作为序列数据或图数据
* 常用API函数
* 恶意软件图像化

静态特征提取方式：

* CAPA
  – https://github.com/mandiant/capa
* IDA Pro
* 安全厂商沙箱

---

## 2.动态特征

相当于静态特征更耗时，它要真正去执行代码。通常包括：
– API调用关系：比较明显的特征，调用了哪些API，表述对应的功能
– 控制流图：软件工程中比较常用，机器学习将其表示成向量，从而进行分类
– 数据流图：软件工程中比较常用，机器学习将其表示成向量，从而进行分类

动态特征提取方式：

* Cuckoo
  – https://github.com/cuckoosandbox/cuckoo
* CAPE
  – https://github.com/kevoreilly/CAPEv2
* 安全厂商沙箱

---

# 二.Capa简介

## 1.基础知识

Capa是FireEye（Mandiant）公司开源的静态分析工具，旨在检测和识别恶意软件的高级静态行为，同时支持IDA插件操作和安装服务及HTTP通信，方便安全人员快速定位恶意代码，且能与ATT&CK框架和MBC映射。

通常能分析的样本格式：

* PE文件
* ELF文
* .NET模块
* ShellCode文件

下载地址：

* https://github.com/mandiant/capa
* https://github.com/fireeye/capa

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06GcvSQibIPnbCgOEJBW6uNB8XNLVdjaOF9T1hLAQicIaU27ObMUlTr6wA/640?wx_fmt=png)

该工具运行结果如下所示，它能有效反映恶意软件在ATT&CK框架中的技战术特点，比如：DEFENSE EVASION、DISCOVERY、EXECUTION、EXFILTRATION、PERSISTENCE等。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06ZutiaV5fpDjIqb8P0bcdaZmYw5IYD7yFLTJaT19Cqia9USmNS0nMUkGg/640?wx_fmt=png)

`（1）安装方式一`
安装过程主要是从Github中下载文件，该文件夹中报告Capa规则，即capa-rules子项目路径下包含了所有类型的检测规则。下载好后，使用命令安装：

* pip install -e [path\_to\_capa]

CAPA规则读者可以尝试编写自适应规则，也可以参考开源大佬们的分享，如下图所示（参考systemino老师）。

> CAPA规则的编写格式如下，第一个红框meta用于描述该规则的描述信息，第二个红框features就是用于匹配的逻辑规则，类似于yara，支持的类型有：api、string、bytes、mnemonic等。
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE067WPXKUuw4Crr8jeIr6iaicJUrnvFjN9Qv45CnGEyCjEZ2aragly8chbg/640?wx_fmt=png)
> 识别结果如下图所示，比如识别出Lazarus组织的Dtrack后门。
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06hiaWwdptvR1TrJOWiau9f6ZwKQcLIw00gibo4txFxQuQMYLoFTRA46taQ/640?wx_fmt=png)

`（2）安装方式二`
另一方面可以下载可执行程序，直接运行。下载地址如下：

* https://github.com/mandiant/capa/releases

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE063rdyJhBEtiaa2UYkOBz9qZebSTFmEjsUib1tDjT15gR4puu2FK0goTrw/640?wx_fmt=png)

下载成功之后如下图所示，直接在CMD或PowerShell中运行即可。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE069hy24lIqLoS8EibeGT0t8KClu2DukibEvWLTdWrULuGniaLSbKKElCaicw/640?wx_fmt=png)

`（3）安装方式三`
在IDA中通过插件的方式使用（支持IDA7.2及以上版本），IDA打开样本后，点击File->Script File加载ida\_capa\_explorer.py脚本。该部分建议从事恶意软件分析的童鞋或技术人员深入研究。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06OmUpv0PldSLRd8bjddTRaiaiao8okFpJUicMLGTJ70QticVibg1w1jHEEOA/640?wx_fmt=png)

---

## 2.CAPA原理详解

CAPA原理知识推荐大家学习FireEye的相关原文介绍。地址如下：

* capa: Automatically Identify Malware Capabilities

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06ZHkz3ka16ypjyicibh9JWhWib9EbiaeafeyqliakHxwXfJDIkqnticbFYMLA/640?wx_fmt=png)

（1）提出问题
在分析程序是否恶意、它们在攻击期间所扮演的角色、潜在功能和攻击作者的意图时，通常需要经验丰富的逆向工程师来完成。恶意软件专家可以快速对未知二进制文件进行分类，以获取初步见解并知道后续分析。然后，经验不足的分析师较难区分正常和恶意样本，并且字符串、FLOSS或PE查看器等常用工具显示的细节级别较低，较难分析恶意软件的行为特点。

（2）恶意软件分类
以某个恶意软件为例，下图展示文件的字符串和导入表信息。通过这些信息，逆向工程师可以利用字符串和导入API函数猜测程序的功能，但仅限于此。

* 该程序可能会创建互斥锁、启动进程、网络通信（可能与IP地址127.26.152.13通信）。
* Winsock（WS2\_32）导入会联想到网络功能，但此处没有名称，可能是按照序号导入。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06WWeAW0QjXkMTofrLXt0icmTKYSKXyx7vuzsgG4E6FcU7f2jMd4hOE2g/640?wx_fmt=png)

动态分析可以进一步挖掘该程序的其它功能。然而，沙盒报告或动态分析工具仅限于从执行代码路径中捕获行为，譬如连接命令和控制（C2）服务器后触发的功能，通常不建议使用实时互联网连接来分析恶意软件。因此，我们需要对它进行逆向分析，如下图所示，利用IDA Pro对程序的主要功能进行反编译。尽管我们使用反编译而不是反汇编来简化描述过程，但这两种表示具有相似的概念。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06NFE8icbf07xC9PHyXoeibUuc1jBCB0I97TMBW65NYZjqJmJdKLRicOq7g/640?wx_fmt=png)

了解编程和Windows API后，我们可以发现恶意软件具备如下功能：

* 创建互斥锁以确保只有一个实例在运行
* 创建一个 TCP 套接字，由常量 2 = AF\_INET、1 = SOCK\_STREAM 和 6 = IPPROTO\_TCP 表示
* 连接IP地址 26.152.13.80，端口为127
* 发送和接收数据
* 将接收到的数据与字符串睡眠和可执行文件进行比较
* 创建新流程

尽管并非每个代码路径都可以在每次运行时执行，但可以说该恶意软件具有执行这些行为的能力。此外，通过结合各个结论，可以推断该恶意软件是一个后门，可以运行由硬编码的 C2 服务器指定的任意程序。这一高级别结论使我们能够确定调查范围并决定如何应对威胁。

（3）自动识别能力
当然，恶意软件分析很少这么简单。意图识别需要通过包含数百或数千个函数的二进制文件进行传播。此外，逆向工程具有相当陡峭的学习曲线，需要对许多低级概念（如汇编语言和操作系统内部）有扎实的理解。

但是，通过足够的练习，我们可以简单地从 API 调用、字符串、常量和其他功能的重复模式中识别程序中的功能。CAPA证明了一些关键分析结论实际上是可以自动识别的。该工具提供了一种通用而灵活的方法来编纂专业知识并将其提供给整个安全社区。当您运行CAPA时，它会将特征和模式识别为人类的力量，从而产生可以推动后续调查步骤的高级结论。例如，当CAPA识别出未加密的HTTP通信功能时，这可能是您需要到代理日志或其他网络实施跟踪的提示。

下图是CAPA的功能介绍，该表格显示此示例中所有已识别的功能。

* 左侧的每个条目都描述一个功能
* 右侧的关联命名空间有助于对相关功能进行分组

CAPA可以非常出色地描述先前讨论的所有程序功能。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06kBNNlgjuKStslJe4icp6iaNmmA6QtmGFjcBia046cHmP8CBUfv9INXEdw/640?wx_fmt=png)

通过实验发现，CAPA经常能够提供令人惊讶的好结果，这也是FireEye希望CAPA能够识别恶意软件功能的追求。下图显示CAPA对“创建TCP套接字”结论的具体输出。由图可知，我们可以通过CAPA检查二进制文件并发现相关特征的确切位置。此外，我们可以利用语法规则推测它们低级功能的逻辑树组成。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06Kp3ia9HNP9Gl4pniaKUD0zUDI4j638GCeQ7j0LI6ZMyFSIKtqwDkN3Tg/640?wx_fmt=png)

（4）CAPA原理
CAPA由两个主要组件组成，这些主要组件通过算法对未知程序进行分类。

* 首先，代码分析引擎从文件中提取功能。 如字符串、反汇编和控制流。
* 其次，逻辑引擎查找以通用规则格式表示的特征组合。 当逻辑引擎找到匹配项时，CAPA会报告规则描述的功能。

代码分析引擎从程序中提取低级功能。所有特征都与人类可能识别的内容一致（如字符串或数字），并使CAPA能够解释其工作。这些功能通常分为两大类：

* `文件特征`：文件特征是从原始文件数据及其结构中提取的，例如 PE 文件头。这是滚动整个文件时可能会注意到的信息。除了上面讨论的字符串和导入的 API 之外，还包括导出的函数和节名称。
* `反汇编特征`：反汇编特征是从文件的高级静态分析中提取的，这意味着反汇编和重建控制流。下图显示了选定的反汇编功能，包括API调用、指令助记符、数字和字符串引用。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06bLDmPNjiaibCAZhHv8Mh6IC0KeCt3ic20oltQYT0bScSc7Ulx3QSMk33A/640?wx_fmt=png)

由于高级分析可以区分程序中的函数和其他范围，因此CAPA可以在适当的详细级别应用其逻辑。例如，当不相关的API用于不同的函数时，它不会混淆，因为CAPA规则可以指定它们应该与每个函数独立匹配。

在设计CAPA 时考虑了灵活且可扩展的特征提取。可以轻松集成其他代码分析后端。目前，CAPA独立版本依赖于分析框架。如果您使用的是IDA Pro，您还可以使用 IDA Python 后端运行CAPA。请注意，有时代码分析引擎之间的差异可能会导致不同的功能集，从而导致不同的结果。幸运的是，这在实践中通常不是一个严重的问题。

（5）CAPA规则
CAPA规则使用结构化的功能组合来描述可以在程序中实现的功能。如果所有必需的功能都存在，CAPA会得出程序包含的功能。

* CAPA规则是包含元数据和语句树以表达其逻辑的YAML文档。除此之外，规则语言还支持逻辑运算符和计数。

在下图所示，“创建 TCP 套接字”规则表示，数字 6、1 和 2以及对API函数套接字或WSA Socket的调用必须存在于单个基本块的范围内。基本块在非常低的级别对汇编代码进行分组，使其成为匹配紧密相关的代码段的理想场所。除了在基本块中，CAPA还支持函数和文件级别的匹配。函数作用域将反汇编函数中的所有功能绑定在一起，而文件作用域包含整个文件中的所有功能。

* 基本块匹配
* 函数匹配
* 文件级别匹配

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMsURJwujJ6SUtmAy43VE06RKnXESLSvaThOrib250crerWV8...