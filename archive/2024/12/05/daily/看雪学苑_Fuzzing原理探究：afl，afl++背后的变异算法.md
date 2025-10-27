---
title: Fuzzing原理探究：afl，afl++背后的变异算法
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458585303&idx=1&sn=2b6ed7f95723bf3904d7628c295166cf&chksm=b18c385d86fbb14b3a0a3add8407560ee585786f8d3aa69eb08e264a44943f76dd11bc90bc58&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-05
fetch_date: 2025-10-06T19:38:20.229313
---

# Fuzzing原理探究：afl，afl++背后的变异算法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicyF2wh3M58CS4MpxyMWkIqU9SicukRUJ9VPxv2Zw3YuBDWWv2TduKkbQ/0?wx_fmt=jpeg)

# Fuzzing原理探究：afl，afl++背后的变异算法

是气球呀

看雪学苑

对于防御者来说，现有的内存损坏和控制流劫持保护措施提供的保护并不完整。对于软件开发人员来说，手动代码分析无法扩展到大型程序。这些漏洞可能被恶意攻击者利用，导致数据泄露、系统崩溃，甚至是更严重的安全事件。

fuzzing 技术，作为一种无需静态分析、动态调试等手段，却能有效识别和暴露软件程序中的潜在漏洞和安全问题的技术，正广泛应用于安全实践之中。Fuzzing 技术本身也正在快速迭代，但论真正划时代意义的工具，非 AFL 莫属。

作者虽然没有以论文形式发表该成果，但是通过该项目的技术细节文档，可以轻松看懂每部分的逻辑。并且，AFL++整合了 AFL 的各类插件，实现兼容性、性能和变异能力的提升，并改进了遗传算法中变异的自定义方案，方便研究人员进行二次开发。

# 1 Fuzzing 的历史和发展

为了更好地理解fuzzing技术，首先从最原始的fuzzing流程开始：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicjibedQGicpFybMhpRlCXvpC3ribWrHaRrDxlVwaA4z3R7fbmg5KftrRqA/640?wx_fmt=other&from=appmsg)

简单来说就是，使用某种规则来生成测试用例，然后提供给程序进行执行，观察程序是否崩溃，如果发生了崩溃，就报告 bugs，否则直接进入下一轮的循环。流程确实是非常简单，但最难的是，怎么去生成能触发漏洞的测试用例呢？

这就是形成fuzzing算法之间效果差异的地方，这最核心的部分算法的目的是不断地往触发崩溃的方向去制作出新的测试样例。该部分主要有两种派别，分别采用了变异(代表如afl、afl++)/生成（代表如boofuzz）算法。

Fuzzing 技术的发展可以分为以下几个阶段：

## 1.1 早期（1980s）

1989 年，Barton Miller 等人在《An Empirical Study of the Reliability of UNIX Utilities》一文中首次提出 Fuzzing 概念，并通过随机输入发现了多个 UNIX
工具的崩溃问题。这一研究揭示了 Fuzzing 作为漏洞检测工具的潜力。

## 1.2 理论深化与工具开发（1990s）

随着 Fuzzing 概念的传播，研究者们开始深入探讨其理论基础，开发了许多早期 Fuzzing 工具，如 SPIKE 和 Peach。1998 年，Michael Sutton 等人在《Fuzzing: Brute Force Vulnerability Discovery》一书中详细探讨了 Fuzzing 的应用和改进方法。

然而，早期型fuzzing技术采用的盲目随机突变，不太可能达到测试代码中的某些代码路径，从而使一些漏洞完全超出了该技术的范围。

## 1.3 灰盒 Fuzzing 的兴起（2000s）

后来，人们渐渐发现覆盖率引导模糊测试（Coverage-Guided Fuzzing）为最有效的软件漏洞发现方法之一，因为它能够系统地探索未测试的代码路径和边界条件，从而显著提高漏洞发现的效率和成功率。

为了提高 Fuzzing 的效率和有效性，研究者引入了灰盒 Fuzzing 技术，通过插桩和反馈机制来优化输入生成策略。2007 年，Zalewski 发布了 AFL（American Fuzzy Lop），这是一种采用灰盒 Fuzzing 技术的工具，大大提高了Fuzzing 的覆盖率（Coverage）和漏洞发现率。

## 1.4 现代 Fuzzing（2010s 至今）

现代 Fuzzing 工具结合了先进的变异算法、分布式计算和云服务等，实现了高效的大规模漏洞检测。工具如 libFuzzer和 Honggfuzz在 Google 和其他大型科技公司中广泛应用，为软件安全性提供了强有力的保障。

AFL、AFL++主要是采用变异策略来生成测试样例，它们效果为什么这么好？AFL++为什么相较于AFL改进如此巨大？接下来的部分将试图弄清其中的来龙去脉。

# 2 AFL：遗传算法与确定性变异策略

## 2.1 AFL-Fuzz简介

American fuzzy lop (AFL) 是一个开源的模糊测试工具，采用遗传算法以有效地提高测试用例的代码覆盖率。目前为止，它帮助检测了数十个主要软件项目中的重大程序错误，包括X.Org Server、PHP、OpenSSL、pngcrush、bash、Firefox、BIND、Qt和SQLite等。

其执行流程大致如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicEccbF55vNH2MzuPhBR7Hb5Lz0PAia9yVyKicNLmkQ4PPLan7wDqZzdzg/640?wx_fmt=other&from=appmsg)

①在从源码编译程序时进行插桩，以记录代码覆盖率（Code Coverage）。
②选择一些输入文件作为初始测试集，加入输入队列（queue）。
③对队列中的文件按一定策略进行“突变”。
④如果变异文件扩展了覆盖范围，则将其保留并添加到队列中。
⑤上述过程循环进行，期间触发 crash 的文件会被记录下来。

其核心主函数为fuzz\_one()，示例图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47Hic6qGtQLCAPNehiapZLTfhibZWTiaMVtUglagIOJoA9Pb7X4AC2nUMplYIA/640?wx_fmt=other&from=appmsg)

fuzz\_one(queue\_entry \*q):获取测试用例并喂给目标程序，根据优胜者机制按概率跳过。调用trim\_case剪枝，calculate\_score打分，然后进行变异（如bitflip、arithmetic inc/dec等），变异后调用common\_fuzz\_stuff处理结果。这是主要函数。

以下是值得关注的函数，如何对数据进行剪枝，如何评估测试用例并优选种子，等等
trim\_case():对当前测试用例进行剪枝，以减少无效数据。

calculate\_score():计算测试用例得分。根据执行时间、覆盖率、新路径和深度对测试用例评分，确保高潜力的测试用例在变异过程中获得更多机会。

save\_if\_interesting():保存有趣的测试用例。检查执行结果是否有趣，即，调用has\_new\_bits(virgin\_bits)来判断是否产生了新的路径元组，若是则保存或加入队列。trace\_bits指向由全体进程共享的内存区域，其中包含每次样本执行的覆盖率，其实是之后提到的覆盖次数桶的压缩存储。

## 2.2 插桩技术

既然要进行覆盖率的引导来辅助遗传算法的进化过程，就必须统计覆盖率，而如果想要记录这一数值，就需要用到插桩技术，插桩一共有三种模式：llvm mode，汇编层面插桩，qemu-mode动态插桩。

### 2.2.1静态插桩

有两种静态插桩方式：llvm mode，汇编层面插桩。

如果拥有受测试程序的源代码，可以使用静态插桩技术来实现覆盖率的记录和增强，这一功能被AFL项目命名为llvm mode，具体实现方式是借助LLVM的Pass来更改中间代码表示IR(Intermediate Representation)，从而在编译过程中实现插桩。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicHF9bNfvvZOvicz9l5OhIbicQMgicAXffc1U6qasswibkFHea9fJmpHCD7g/640?wx_fmt=other&from=appmsg)
在有源代码的情况下，可以使用 AFL 自带的 afl-gcc 或 afl-clang 插桩方式，这些工具通过修改 GCC 或 Clang 编译器，在编译过程中插入覆盖率收集代码，性能介于 QEMU 动态插桩和 LLVM 静态插桩之间。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicIYXWgpN5mZIJB6ia96GhVNr5zDdXE0GUayA27GY86vrJLxCFBetrJaA/640?wx_fmt=other&from=appmsg)
接下来详细叙述怎么进行汇编层面插桩。实际的插桩工作发生在汇编为机器语言的环节。查看该项目的afl-as.h头文件，可以看到，以下这段内容是AFL插入到每个代码块结束处的汇编代码，其调用(call指令)\_\_afl\_maybe\_log，这个正是探测点（Probe Points）相关汇编代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47Hicuwok1zEpSutXIXfic5kOznU1tyANYh3vXreibjR8dM7ef4iaxEFthkLFg/640?wx_fmt=other&from=appmsg)

从控制流的角度来看，代码块（code block）是一个或多个语句的集合，这些语句按照程序的逻辑顺序一起执行。代码块的基本功能是将一系列操作组织在一起，以实现特定的功能或操作。代码块的控制流主要涉及语句的顺序执行、条件分支和循环。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicIAYP6z5ZsFJqdRcAMkAqOwaNTnmCGAIytBM2bYxsv5hLL65lxazibgQ/640?wx_fmt=other&from=appmsg)

该源代码插桩方式正是将所有代码块的开始部分进行插入，因为插入点位于基本块的开始处，可以准确记录程序执行到这个代码块的次数和路径。

而对于分支(如)和函数调用的插桩，AFL会把所有函数调用都进行插桩，但分支的数量往往比较巨大，为了让用户能够按需进行性能和插桩完整程度的权衡，AFL提供了一个值inst\_ratio\_str ,这个值用于控制对分支的插桩比例，R(100)是0-100随机值，如果>inst\_ratio\_str则不进行插桩，这就完成了按概率来进行对分支的插桩。其代码逻辑如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47Hic18uuxtaIZMMbib0o1w8E6tic1iaPzZamzCDID5zcfARk8HZt2H4yGNeTQ/640?wx_fmt=other&from=appmsg)

此外，对于LLVM插桩，跟随afl-llvm-rt.o.c查看LLVM Pass层次的实现代码，实际上可以发现，很多内容都是用c来表示的，但功能和先前的汇编差不多，比如插桩比例的控制：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicveXzNF0PpZaTcEiaOYmeibsmxOwq0b9WsiaWWHp7zZfh77rXlJxfGTq0Q/640?wx_fmt=other&from=appmsg)

又比如forkserver与父进程的等待和通信，这些内容将会在接下来进行详细叙述。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicfQKpo3mib7KLHagpJGxUQ5tE3VkXhIbDVvJobuCM75Fdb05SUqia5O1g/640?wx_fmt=other&from=appmsg)

###

### 2.2.2动态插桩

在没有源代码的情况下进行插桩，被称为唯二进制插桩 (Binary-only instrumentation)。AFL 的作者对 QEMU（一种跨架构软件执行环境工具，也可称为”跨架构二进制翻译器”）进行了二次开发，使其具备二进制插桩的能力。具体而言，是对QEMU 使用基础块（basic blocks）作为翻译单元。直接查看其二开的QEMU不太方便，查看technical\_details.txt说的概念：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HictN03ibAukwCicbs31uoL9W8PgibXsdB5yFfjzcyrXKH6PaBWSL6kQs6TQ/640?wx_fmt=other&from=appmsg)

if (block\_address > elf\_text\_start && block\_address < elf\_text\_end) 这一判断是为了确保当前基础块的地址在可执行代码段（.text 段）内，以过滤掉不相关的地址。

紧接着，cur\_location = (block\_address >> 4) ^ (block\_address << 8); 通过移位和异或运算计算当前基础块的位置。这种计算方式生成一个相对唯一的标识符，用于标识当前基础块。

shared\_mem[cur\_location ^ prev\_location]++;使用当前块的位置与前一个块的位置进行异或运算，更新共享内存中的覆盖率信息。shared\_mem 是一个共享内存区域，用于记录不同路径的执行次数。

prev\_location = cur\_location >> 1;更新前一个块的位置，以便在下一个基础块执行时进行正确的覆盖率计算。其实现的正是QEMU下的覆盖率引导计算，相关内容在后面还会详细说明。

本身的二进制翻译器如 QEMU、DynamoRIO 和 PIN 启动较慢，为了弥补这一点，AFL 在 QEMU 模式下使用了 fork server和管道机制，前面已作详细说明。经过这些优化，QEMU 模式下的 AFL 开销是白盒模式(有源代码插桩fuzzing)的 2-5 倍，而使用 PIN 的开销则高达 100 倍以上。

## 2.3 eff\_map对变异的影响

这里还要引入一个eff\_map的概念，此项记录了每个字节是否引起了新路径元组的出现，用以评估其对整个执行路径元组的影响。如果 byte 尝试所有改变都没有出现新路径，AFL开发者认为这种字节很有可能只是单纯的非元数据，AFL后续会参考eff\_map 进行选择性的跳过。接下来每次变异都会检查eff\_map中的对应项 ，如果当前字节对应的项为 0 ，则检查变异以后路径是否有新元组产生，如果是则置为 1。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicHqfYSoicXUdYLroMGAB0Efaz8tGcbyibMYKwxwFGbGTzuz3kcCg1IN2Q/640?wx_fmt=other&from=appmsg)

而且，eff\_map会将输入测试用例文件小于128字节的情况，认为每个字节都是有效的，而如果一个测试用例，90%的字节都能触发新路径元组，那么AFL会直接把剩余的10%也认为是有效的。

这种做法改善了变异的方向性，使其能够避免过多的无效变异，从而更加专注于有效的变异。

## 2.4 输入队列变异

在完成上述步骤以后，AFL会对测试样例进行变异操作。

这部分的内容更像是经验主义的产物，没有什么比较有意思的细节，但被实践证明是高效率的，因而被采纳。主要的代码逻辑仍位于afl-fuzz.c。

### 2.4.1 简单位翻转(simple bitflip)变异

首先是简单的位翻转(Simple Bitflip)，该操作是之后一系列变异方式的基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicmcEXVX1OASbYkoc6xJNRlkx4QibBSBP29IHODAIMcGInNL1BFnGZyuA/640?wx_fmt=other&from=appmsg)

该定义宏实现了指定位翻转的功能，\_ar传入需要进行位翻转操作的字节数组指针，\_b则是要翻转的位置。实际上该定义宏常见于各项目，不再赘述。

由简单翻转衍生出的变异模式有：

bitflip 1/1：步长为 1 bit，每次翻转 1 bit。
bitflip 2/1：步长为 1 bit，每次翻转相邻的 2 bit。
bitflip 4/1：步长为 1 bit，每次翻转相邻的 4 bit。
bitflip 8/8：步长为 1 byte，每次翻转 1 byte，并检查效应图（eff\_map）。
bitflip 16/8：步长为 1 byte，每次翻转相邻的 2 byte。
bitflip 32/8：步长为 1 byte，每次翻转相邻的 4 byte。

此处以bitflip 4/1为例：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47Hic5yu3KicXFRTuNUNciaAqicIHdHmdEFLmoE4ygWj5cJP3picFjBPe0ibH1Wg/640?wx_fmt=other&from=appmsg)

实现的就是步长总长度1byte，每次翻转这1byte里面连续的4bits。实际上其它的位翻转变异实现功能上是大同小异的，细节可能稍微有点不一样。

common\_fuzz\_stuff实际上正如其名，是在检测fuzz是否成功触发新路径，如果是，那么就记录该路径并放弃继续变异，这次变异的结果也会被保存。

该操作的剩余部分的作用将在字典变异里提及，此处按下不表。

### 2.4.2 加减法变异

加减法变异，就是对测试用例做加减法方面的变异；为了避免无意义的重复变异，...