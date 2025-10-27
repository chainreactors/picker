---
title: 爆火出圈的chatGPT如何在逆向和恶意软件分析中发挥作用
url: https://www.4hou.com/posts/ZXLQ
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-28
fetch_date: 2025-10-04T02:35:11.956049
---

# 爆火出圈的chatGPT如何在逆向和恶意软件分析中发挥作用

爆火出圈的chatGPT如何在逆向和恶意软件分析中发挥作用 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 爆火出圈的chatGPT如何在逆向和恶意软件分析中发挥作用

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-12-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)221316

收藏

导语：让我们看看ChatGPT如何帮助我们解决一些常见的逆向工程和恶意软件分析难题。

ChatGPT是人工智能研究实验室OpenAI新推出的一种人工智能技术驱动的自然语言处理工具，使用了Transformer神经网络架构，也是GPT-3.5架构，这是一种用于处理序列数据的模型，拥有语言理解和文本生成能力，尤其是它会通过连接大量的语料库来训练模型，这些语料库包含了真实世界中的对话，使得ChatGPT具备上知天文下知地理，还能根据聊天的上下文进行互动的能力，做到与真正人类几乎无异的聊天场景进行交流。ChatGPT不单是聊天机器人，还能进行撰写邮件、视频脚本、文案、翻译、代码等任务。

接下来就让我们看看ChatGPT如何帮助我们解决一些常见的逆向工程和恶意软件分析难题。

**1.学习如何更有效地使用逆向工程工具**

软件工具通常带有不同程度的内置帮助，它们所缺少的通常由专门的用户论坛和问答网站（如Stack Overflow、Stack Exchange等）来弥补。ChatGPT为快速获得逆向工程工具的帮助增加了另一条途径。

无论你是使用IDA Pro、Ghidra、Radare2、Hopper、Cutter还是其他一些逆向引擎平台，ChatGPT都能提供帮助。虽然所有这些平台都包含自己的内置帮助功能，但如果ChatGPT的培训模型中已经涵盖了这些问题，那么你可能会发现它能够回答与你自己的用例相关的特定问题，这是一种更快完成任务的方式。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671758909378256.jpeg "1671758909378256.jpeg")

使用ChatGPT作为radare2的交互式帮助助手

**2.自学汇编语言**

ChatGPT擅长传达相关信息。

例如，ChatGPT提供了关于函数调用基础知识和相关堆栈内存管理活动的回答。

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671758920202581.jpeg "1671758920202581.jpeg")

我们可以要求ChatGPT在其输出中或多或少详细一些。例如，在这里，我们希望得到一个堆栈帧的视觉表示。

![3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671758933117591.jpeg "1671758933117591.jpeg")

ChatGPT描述了一个堆栈框架

汇编代码是特定于平台和编译器的。如果向ChatGPT发出的程序集相关问题不包括与编译程序集的平台（即指令集）或更高级别语言相关的特性，ChatGPT将提供相关的免责声明信息，以正确定位答案。

ChatGPT可以帮助攻克汇编难题的另一种方式是将用户熟悉的高级代码转换为汇编代码。这通过将熟悉的概念映射到其内部来促进学习。我们观察到，ChatGPT可以很好地处理各种主题，包括在学习汇编时至关重要的重要概念，例如指针和函数指针调用。ChatGPT的响应通常包括带注释的汇编代码，这进一步提高了学习效果。

![4.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671758947864671.png "1671758947864671.png")

![4.2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671758969293974.jpeg "1671758969293974.jpeg")

ChatGPT将高级代码转换为程序集

**3.了解源代码如何转换为反汇编**

作为恶意软件分析师，我们大部分时间都是从反汇编者的角度来看待恶意软件。编程语言的经验和知识在这里至关重要，但ChatGPT可以帮助我们了解已知源代码在反汇编程序中的样子，以及代码更改如何在反汇编中反映出来。新手可以通过编写自己的源代码来推断一些反汇编代码可能会做什么，并查看它是否与他们正在查看的反汇编类似。这可以帮助经验不足的分析人员加深对恶意代码的理解。

![5.1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671758990240927.jpeg "1671758990240927.jpeg")

![5.2.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759000133037.gif "1671759000133037.gif")

**4.快速编写PoC源代码**

ChatGPT甚至可以帮助我们编写测试理论所需的源代码。例如，我们可以问AI以下问题：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759013255978.png "1671759013255978.png")

然而，有时候ChatGPT需要一点引导。在写完我们请求的函数后，它决定将分解任务委托给我们:

![7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759027598183.jpeg "1671759027598183.jpeg")

首先，我们从前面的答案中复制代码，然后在给出明确的指令后粘贴它。

![8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759039555587.jpeg "1671759039555587.jpeg")

现在，我们得到了我们正在寻找的分解结果。

![9.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759442175582.jpeg "1671759442175582.jpeg")

**5.指令集之间的转换**

鉴于汇编代码是特定于平台的，经验更丰富的逆向工程师可以利用ChatGPT查询不同的指令集，而不是他们已经熟悉的指令集。一种方法是指示ChatGPT将编写在一个指令集中的汇编代码转换为另一个指令集。

![10.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759500111444.jpeg "1671759500111444.jpeg")

ChatGPT将x64汇编代码转换为ARM

这为进一步探索感兴趣的指令集提供了基础，例如，通过查询ChatGPT关于翻译后代码中指令的进一步信息。

![11.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759513105017.jpeg "1671759513105017.jpeg")

ChatGPT解释了blx ARM指令

**6. 比较语言或特定于平台的约定**

有经验的逆向工程师还可以从使用ChatGPT查询编程语言和平台的内存管理技术的差异中受益，例如调用约定。

![12.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759528563440.jpeg "1671759528563440.jpeg")

ChatGPT比较调用约定

在撰写本文时，ChatGPT正在使用2021年之前的训练数据进行训练。因此，如果某些平台或高级语言的特性在某个时间点之后发生了变化，ChatGPT不会提供当前信息。调用约定更改的一个例子是在Golang语言中从基于堆栈的调用约定转换为基于寄存器的调用约定。

有经验的逆向工程师，特别是恶意软件分析师，可以利用ChatGPT来熟悉日益流行的编程语言的高级结构，以及这些结构是如何在汇编中表示的。例如，内存安全的Golang和Rust越来越多地被恶意软件开发人员采用。

![13.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759542646771.jpeg "1671759542646771.jpeg")

**7.分析恶意软件样本中的代码段**

ChatGPT能够解释和分析与逆向工程相关的代码，包括伪代码和汇编代码。这使得ChatGPT在分析恶意软件可执行文件的代码段(如函数)时非常有用，主要是因为ChatGPT可以提供代码执行活动的摘要。

这可以显著提高恶意软件逆向工程师的效率。Gepetto IDA Pro插件在IDA Pro中集成了ChatGPT，并查询语言模型以提供由Hex-Rays反汇编程序反编译的函数的含义。

解释代码的能力还可以对代码进行比较，使恶意软件分析人员能够了解不同恶意软件样本实现之间的差异。

为了在分析人员通常需要的描述性级别上总结代码的功能，ChatGPT可能缺少所需的关于分析中的可执行文件的更广泛的上下文，而分析人员可能拥有这些上下文。

假设分析师很少或没有向ChatGPT提供上下文，如果所分析的代码与其目的相关，那么该模型将提供最大的即时价值。在实践中，这通常意味着代码不会调用以ChatGPT未知的方式扩展代码功能的用户定义函数，但如果它调用函数，则它们是已知的、公开记录的库函数。由于ChatGPT是基于公开可用的数据进行训练的，因此语言模型此时可以准确地解释在用户提供的代码中使用这些函数的情况。

例如，如果提供给ChatGPT的伪代码引用了公开记录的库函数，则ChatGPT对代码用途的解释将围绕这些函数的功能展开。

![14.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759558171583.jpeg "1671759558171583.jpeg")

ChatGPT通过解释十六进制射线伪代码来讨论函数的用途

为了从ChatGPT中获得更好的代码分析输出，用户仍然需要:

制定实质性的ChatGPT查询，以便提供所需的上下文;

与ChatGPT进行对话，在对话期间提供上下文，并完善ChatGPT的答案;

尝试在回答的末尾使用“重新生成响应”选项，这似乎是对ChatGPT的一种“再努力一点”的指示。

向ChatGPT添加更多上下文可以包括用户定义函数的功能，这些功能是分析师所了解的。上下文信息可以以编程的方式提供，以减少人工分析人员的工作量，例如，通过为此目的开发的反汇编程序插件。

这同样适用于从非技术角度改进ChatGPT的输出。例如，ida\_gpt(一个通过查询ChatGPT来协助程序集代码分析的IDA Pro插件)分别为分析和重构程序集代码制定了下面的查询。

下面是ida\_gpt ChatGPT查询的几个示例:

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759570510635.png "1671759570510635.png")

**8.识别代码中的恶意活动**

恶意软件分析师可以使用ChatGPT来识别某个功能可能实现的潜在恶意活动的指示器。这对于将恶意软件可执行文件中的功能映射到特定的恶意功能非常重要，类似于capa IDA Pro插件的功能。

在这种情况下，我们观察到ChatGPT能够对函数中恶意活动的所有指标的强度进行优先级排序。因此，恶意软件分析师可以确定与ChatGPT的交互范围，以更详细地讨论最强指标。

例如，OpenGPT将vssadmin.exe的执行确定为下面伪代码中恶意活动的最强指标。

![16.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759587168147.jpeg "1671759587168147.jpeg")

![16.2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759598164486.jpeg "1671759598164486.jpeg")

![16.3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759614281653.jpeg "1671759614281653.jpeg")

ChatGPT评估恶意活动的指标

**9.推测功能目的和目标**

除了识别恶意活动指标外，恶意软件分析师还可以进一步与ChatGPT对话，以推测并更好地了解恶意软件如何使用特定平台或软件结构以及达到何种目的。即使在分析师没有提供全面背景的情况下，这也可能是有效的。

例如，下面的勒索软件伪代码代码使用Microsoft Cryptographic API（CAPI），也称为CryptographicAPI：下一代（CNG）加密架构，用于加密数据。

![17.1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759633632401.jpeg "1671759633632401.jpeg")

![17.2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759643867550.jpeg "1671759643867550.jpeg")

![17.3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221223/1671759653903217.jpeg "1671759653903217.jpeg")

ChatGPT讨论了恶意软件对CAPI的使用

**10. 了解漏洞并利用代码**

了解漏洞是如何工作的，恶意软件开发者如何利用它们，以及我们如何识别和检测它们在代码中的使用是一项极具挑战性的任务。ChatGPT在这方面也可以帮助我们。

让我们以CVE-2022-468889为例，看看ChatGPT是否可以帮助我们理解代码的工作原理。

![18.jpg](https://img.4hou.com/uploads/ueditor/php/upl...