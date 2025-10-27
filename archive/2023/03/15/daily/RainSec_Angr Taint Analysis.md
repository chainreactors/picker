---
title: Angr Taint Analysis
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzczOTA3OQ==&mid=2247485835&idx=1&sn=a8344b7ae4ec183b388b0952baa54adc&chksm=cf1f24a3f868adb54faa2fa05d524b3b2d9b8735788da0805521e66684e3f8642db2cefaa7c3&scene=58&subscene=0#rd
source: RainSec
date: 2023-03-15
fetch_date: 2025-10-04T09:36:58.507499
---

# Angr Taint Analysis

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LxlshmzkAkabTx0JNr29iaUG1yXsrK8sNrfibXJVicYyseJ0DibIDVhwdKfJYDYSUeHBhtLibibmEyjxZjQ7JVNHzxZQ/0?wx_fmt=jpeg)

# Angr Taint Analysis

原创

时钟

RainSec

# angr taint analysis

> 本人一直致力于二进制分析和自动化漏洞挖掘领域（Fuzzing and symbolic execution or other），这次算是抛砖引玉，希望可以大家多多指导，欢迎加wx交流，公众号里面发1有我wx

污点分析的基本分类：

1. 1. 动态污点分析
2. 2. 静态污点分析

上述分析方式都有自己的优缺点，对于动态污点分析来说，缺点如下：

1. 1. 分析结果依赖输入。
2. 2. 一些隐式调用难以跟踪。

静态污点分析的缺点如下：

1. 1. 路径爆炸问题。
2. 2. 一些程序特性只有在动态执行的过程中才会展示出来。

angr本身的知识内容多而且杂乱，下面对一些核心的基础知识进行一下讲解。

## angr

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkabTx0JNr29iaUG1yXsrK8sNiaQicriaicfW2h4W25k3umGFPJvbIPz90ATpSEEcAdLdPgOpdiaID6L2S2Q/640?wx_fmt=png)

> https://web.wpi.edu/Pubs/E-project/Available/E-project-101816-114710/unrestricted/echeng\_mqp\_angr.pdf

  angr一般优势在于可以为逆向工程查找函数，生成函数调用图，同时其还具备一个符号执行引擎。上述研究项目为angr研究设置了三个目标：

1. 1. 探索angr的符号执行能力并记录其复杂性。
2. 2. 探索Angr作为二进制分析工具的能力。
3. 3. 为angr创建一个平台，使得逆向工程师更容易接触他们。

从这三个目标来看，这是一个非常适合新手学习angr的项目，展示的都是很基本的功能。

> https://archive.fosdem.org/2017/schedule/event/valgrind\_angr/attachments/slides/1797/export/events/attachments/valgrind\_angr/slides/1797/slides.pdf

这个（应该）是Angr团队的一个演讲，讲的更好一点，可以理解一下Angr的底层实现。

### vex

  angr用VEX作为中间表示用来进行二进制分析，pyVEX就是一个对于VEX的python封包。其实中间语言存在于很多场合，最主要的功能是为了解决二进制分析中面临多种架构的问题，使得一次分析可以运行在多个架构之上。最主要的中间表示如下：

* • Register name，VEX models 存放寄存器在一个单独的内存空间里面，用offset来定位不同的寄存器。
* • Mem access.
* • Mem segmentation.
* • Instruction side-effects. 很多指令具备Side-effects。比如push pop同时还会影响stack pointer, thumb mode on arm很多指令都影响flags。IR可以相应的表示这些影响。

VEX主要存在以下结构，这个非常重要：

* • **Expressions.** IR Expressions represent a calculated or constant value. This includes memory loads, register reads, and results of arithmetic operations.
* • **Operations.** IR Operations describe a modification of IR Expressions. This includes integer arithmetic, floating-point arithmetic, bit operations, and so forth. An IR Operation applied to IR Expressions yields an IR Expression as a result.
* • **Temporary variables.** VEX uses temporary variables as internal registers: IR Expressions are stored in temporary variables between use. The content of a temporary variable can be retrieved using an IR Expression. These temporaries are numbered, starting at `t0`. These temporaries are strongly typed (i.e., "64-bit integer" or "32-bit float").
* • **Statements.** IR Statements model changes in the state of the target machine, such as the effect of memory stores and register writes. IR Statements use IR Expressions for values they may need. For example, a memory store IR Statement uses an IR Expression for the target address of the write, and another IR Expression for the content.
* • **Blocks.** An IR Block is a collection of IR Statements, representing an extended basic block (termed "IR Super Block" or "IRSB") in the target architecture. A block can have several exits. For conditional exits from the middle of a basic block, a special Exit IR Statement is used. An IR Expression is used to represent the target of the unconditional exit at the end of the block.

上面可以了解angr的一些基本概念。详细例子可以参考下面：

> https://github.com/angr/pyvex
>
> 这些语言描述是很难的，建议还是根据官方例子调试一下，就知道每个IR对应的意思了。

  下图在angr团队的演讲里面展示的，正是对应的上述的VEX结构。因此可以看出pyvex可以很好的把机器码转换为中间语言来方便进行二进制分析。对于所有的vex struct都对应的有python class和enums，这些都以字符串的形式表示，总的来说就是整个的中间表示能力都可以用python完成。

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkabTx0JNr29iaUG1yXsrK8sNmWicIaE4icSWmibJQyEJTU9I1QKiaJfGwbAPQnKy8AJvibNNuoHPk1tatrw/640?wx_fmt=png)

在Angr里面还存在SimuVEX，这是为了符号执行，它本身是作为VEX IR（IRSBs）的符号执行引擎：

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkabTx0JNr29iaUG1yXsrK8sN5gjnqywzxFAyuHOTRwiaWuwZ0S0zMlBQhznkkiaN7QknX7riaFhjkJN9g/640?wx_fmt=png)

符号执行的一个核心在于执行环境的实现，因此SimuVEX必须实现：

1. 1. 内存和寄存器建模。
2. 2. syscalls
3. 3. Files and other data sources from outside the program
4. 4. Providing symbolic summaries (SimProcedures) of common library functions

这里面比较难以理解的就是symbolic summaries了，先看下angr官方的例子：

```
>>> from angr import Project, SimProcedure
>>> project = Project('examples/fauxware/fauxware')

>>> class BugFree(SimProcedure):
...    def run(self, argc, argv):
...        print('Program running with argc=%s and argv=%s' % (argc, argv))
...        return 0

# this assumes we have symbols for the binary
>>> project.hook_symbol('main', BugFree())

# Run a quick execution!
>>> simgr = project.factory.simulation_manager()
>>> simgr.run()  # step until no more active states
Program running with argc=<SAO <BV64 0x0>> and argv=<SAO <BV64 0x7fffffffffeffa0>>
<SimulationManager with 1 deadended>
```

  可以看出SimProcedures的一个核心作用就是hook，这里main函数不再执行，而是执行我们定义的SimProcedures，这意味着可以定义程序的运行。因此上述的4应该就是提供对于库函数的替代，这样的一个好处也在于提升了符号执行的性能。如果想对SimuVEX有一个更好的了解可以参考下面的文章，来从源代码进行理解：

> https://sites.google.com/site/bletchleypark2/malware-analysis/angr/simuvex
>
> 如果打算做符号执行的话，还是深入读一下，这一块是对执行过程state的很核心的代码。

### claripy

> 这个玩意挺难，挺复杂的。
>
> https://docs.angr.io/advanced-topics/claripy#solvers

claripy是Angr的一个约束求解引擎，主要的设计思想如下：

* • Claripy ASTs 提供一个统一的方式和符号化的或者具体化的表达式交互。

  在claripy里面实现了bitvectors，这使得我们可以在变量上构建表达式符号树，对它们的值添加约束然后求解它们具体的值，这个操作依赖z3。Claripy ASTs抽象了claripy支持的不同数学结构之间的差异，实现了很多处理操作，同时还实现了求解器。求解器可以说是Claripy最主要的功能，Solvers暴露api和ASTs以不同的方式进行交互并且返回可用的值，同时其具备不同的求解器类型以满足不同的要求。通过Claripy Backends可以构建自定义求解器，但是这将非常硬核。

### symbolic execution example

  符号执行的一个特色就是状态复制，这也是路径爆炸问题的一个根本来源，状态复制指的是在符号执行的过程中如果state A遇到一个if else分支结构，那么就会复制出来两个状态对应不同的分支。

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkabTx0JNr29iaUG1yXsrK8sN3DzmJxqiaOmWVxnxwA9m1tPTpVxkCIIeZZu8Ctyicnc0RicwnuDJ0JF1g/640?wx_fmt=png)

不同的state会添加不同的约束，然后最后求解的时候就是对这些约束进行求解。

### CLE

> https://www.anquanke.com/post/id/231591https://www.anquanke.com/post/id/231591
>
> （上面的好像关了。。。）
>
> https://github.com/angr/cle

  CLE主要表现为一个binary loader，但是其非常复杂，通过其可以将可执行文件和libraries文件载入到可用的地址空间，其复杂性来源于为不同平台，不同架构设计了统一的加载接口。这个里面最重要的其实就是VEX IR，VEX IR利用中间语言的方式抽象了机器代码的表示形式，同时消除不同体系结构之间的差异：

1. 1. 寄存器名称。
2. 2. 内存访问
3. 3. 内存分段
4. 4. 具有副作用的指令，比如push pop

### analyses

  这是angr的核心分析模块，它将所有的抽象结合在一起形成一个统一的控制接口Project，这将实现非常便利的访问符号执行，CFG恢复，data-flow分析等等。但是这需要大量的基础知识来帮助完成理解。

在对于Angr的CFG进行理解的时候也不能完全按照ida的模式去理解:

> https://docs.angr.io/introductory-errata/faq#why-is-angrs-cfg-different-from-idas

  id不会再function call的地方拆分block，但是angr会，所以angr每次的step可能会因为function call进入下一个基本块。IDA侧重于提供更好的分析体验，而angr则侧重于自动化分析，在自动化分析过程中一般不需要超图，因为自动化分析一般想要的是更细致的内容。如果一个类似jump的跳转返回到基本块中间，ida一般会拆分，但是angr不会，因为很多静态分析一般不需要，但是可以通过生成cfg的过程中传递`normalize=True` 参数来开启拆分功能。

### Simulation Managers

> https://github.com/angr/angr-doc/blob/master/docs/pathgroups.md#simulation-managers

  angr分析模块里面最重要的control interface就是SimulationManager了，它可以同时控制状态组的符号执行，执行不同的搜索策略来探索程序的state空间。在符号执行的过程中，States会被组织成stashes，这使得分析人员可以step forward, filter, merge, and move around as you wish，甚至同时以不同的方式指向两种不同的stash集合并对其进行合并，默认操作的的stash是active。之前已经了解到angr可能存在很多states在stash里面，这些state可以通过move切换，move存在三个参数from\_stash, to\_stash, and filter\_func用来对states进行filter和移动。

```
>>> simgr.move(from_stash='deadended', to_stash='authenticated', filter_func=lambda s: b'Welcome' in s.posix.dumps(1))
>>> simgr
<SimulationManager with 2 authenticated, 1 deadended>
```

  通过上述操作我们创建一个新的stash。同时必须记得，state其实就是一个list，可以通过索引访问或者迭代等其它方法访问，比如利用`one_` 或者 `mp_`前缀，但是mp前缀返回给你的是一个 mulpyplexed version of the stash.对于stash也存在一些特殊类型，如下：

1. 1. active和deadended。这两个比较容易理解，一个是当前使用的stash一个是里面包含的已经没办法继续执行的state。
2. 2. pruned, state可以通过Options进行调整，每一个state存在一个state.options，它们控制着angr 执行引擎的行为，当options中添加LAZY\_SOLVES的时候，states在运行的时候不会检查满意度（satisfiability 指的是solver在求解前的测试，看看约束或者其他信息能否满足求解需要，如果返回true，接下来进行求解），除非非常必要的情况下才会进行检查，当该state unsat的时候， 遍历所有的state层级去识别历史上什么时候最初变得unsat，所有的继承于最初unsat点的state都将被放入pruned 集合。
3. 3. save\_unconstrained option如果被指定，所有被确定为无法约束的状态都会被放入这里。
4. 4. Unsat，如果save\_unsat option被指定，那么所有的unsatisfiable state都被放在这个集合，大多数的原因可能是具备相互矛盾的约束。
5. 5. errored，如果state在执行过程中遇到raise error，该state被打包进入ErrorRecord object，这其中还包括raised error，然后放入errord集合.

1. 1. You can get at the state as it was at the beginning of the execution tick that caused the error with `record.state`, you can see the error that wa...