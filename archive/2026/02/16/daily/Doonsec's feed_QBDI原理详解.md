---
title: QBDI原理详解
url: https://mp.weixin.qq.com/s/cLlRY38yjhwEXhCbc-MNeA
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:14:54.102949
---

# QBDI原理详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3spRNsE9StbneXgyp38WOxGmWxZUM82icnfpKncsfUIbANG8e72icW57ghRqNLUfZtNNQdyyrG11fvUJ11JAKbibefNpqQAAqntg/0?wx_fmt=jpeg)

# QBDI原理详解

飞翔的猫咪
飞翔的猫咪

看雪学苑

![]()

在小说阅读器中沉浸阅读

QBDI的代码位于:  https://github.com/QBDI/QBDI

QBDI的含义为: A Dynamic Binary Instrumentation framework based on LLVM。

它对标的是像Frida Stalker这样的工具,但是QBDI没有像frida那样提供了代码注入的功能,需要自己实现注入代码并且启动QBDI。

其他相似的工具有:

* valgrind: 一款用于内存调试、内存泄漏检测以及性能分析的软件开发工具,只支持linux平台,使用起来比较复杂。
* DynamoRIO: 开源多平台的应用程序动态instrumentation框架

以下内容没有特别说明都是针对arm64平台。

**一. 交叉编译在安卓上运行的目标**

从github下载代码以后,修改cmake/config/config-android-aarch64.sh文件加入以下行 :

```
-DCMAKE_BUILD_TYPE=Debug \
-DQBDI_EXAMPLES=true \
-DQBDI_LOG_DEBUG=true \
-DCMAKE_EXPORT_COMPILE_COMMANDS=1 \
```

编译:

```
$ export NDK_PATH=/your_ndk_dir/android-ndk-r28b-linux/android-ndk-r28b
$ mkdir build
$ cd build
$ ../cmake/config/config-android-aarch64.sh
$ ninja
```

运行示例程序:

```
$ adb push libQBDI.so /data/local/tmp
$ adb push examples/cpp/fibonacci_cpp /data/local/tmp
$ adb shell
$ cd /data/local/tmp
$ LD_LIBRARY_PATH=. ./fibonacci_cpp
```

调试:将ndk的lldb-server push到手机中

在手机端执行:

```
 $ ./lldb-server platform --listen "*:10086" --server
```

在PC端执行:

```
$ adb forward tcp:10086 tcp:10086
$ lldb
$ platform select remote-android
$ platform connect connect://[adb devices返回的id]:10086
$ file fibonacci_cpp
$ env LD_LIBRARY_PATH=/data/local/tmp
$ b main
```

可以看到在这个示例的代码(examples/cpp/fibonacci.cpp)中,需要自己调用被trace的函数并且传递需要的参数:

```
res = vm.call(&retvalue, reinterpret_cast<QBDI::rword>(fibonacci),{static_cast<QBDI::rword>(n)});
```

其实我们可以利用frida的inline hook功能拦截原始函数的参数并且转交给qbdi让它trace,就不需要我们自己准备参数了。

**二. qbdi的基本原理**

qbdi本质上是一个VM,监视程序的运行指令流并跟随该流实时的patch代码。

所以会有qbdi context和guest context并有上下文切换的操作。

遇到不在指定trace范围的代码经由ExecBroker将控制权递交出去并监控返回点,返回以后再接管控制。

执行流程:

* 从被trace的代码开始位置处调用llvm库反编译,并对其中的代码patch(修复pc相关指令)直到遇到改动pc指令为止
* 对上面得到的基本块调用instrument函数对每条指令插入trace相关指令,并且执行寄存器分配与保存相关工作
* 创建ExecBlock,它由连续的两页组成: Code Block和Data Block, 这样安排的好处是Code Block只需要pc相对指令就可以访问到Data Block的内容,无需引入额外的寄存器, 引入额外的寄存器会破坏guest寄存器需额外保存. 而Data Block则存放着host上下文数据. 因为ExecBlock的空间有限，空间不够存放的时候必须创建新的ExecBlock
* 执行当前ExecBlock,根据回调返回值做相应的处理
* 执行完基本块以后获取新的pc地址,跳到步骤1继续循环直到函数执行完毕

**三、API**

知道了大概原理以后来看一下trace相关API

**操纵trace范围的api:**

```
/*
限制:
    范围只能在函数级别或者库级别,不支持只指定函数内的部分指令
    ExecBroker不支持异常机制: 如setjmp/longjmp
*/
//添加删除跟踪范围
void VM::addInstrumentedRange(rword start, rword end);
void VM::removeInstrumentedRange(rword start, rword end);

//添加删除跟踪模块
bool VM::addInstrumentedModule(const std::string &name);
bool VM::removeInstrumentedModule(const std::string &name);

//通过模块内的一个地址添加删除跟踪模块
bool VM::addInstrumentedModuleFromAddr(rword addr);
bool VM::removeInstrumentedModuleFromAddr(rword addr);

//跟踪所有的可执行映射
bool VM::instrumentAllExecutableMaps();
//删除所有的跟踪范围
void VM::removeAllInstrumentedRanges()
```

**跟踪指令执行:**

```
//PREINST执行前,POSTINST执行后
QBDI_EXPORT uint32_t addCodeCB(InstPosition pos, InstCallback cbk, void *data,
int priority = PRIORITY_DEFAULT);
```

VM事件API:

```
/*
BASIC_BLOCK_NEW -> 解析目标代码遇到一个新的bb时事件
BASIC_BLOCK_ENTRY -> bb开始执行时事件
BASIC_BLOCK_EXIT -> bb执行完毕时事件
SEQUENCE_ENTRY -> 序列开头时事件
SEQUENCE_EXIT -> 序列退出时事件
EXEC_TRANSFER_CALL -> 当遇到不在trace范围内的指令跳转到ExecBroker执行时事件
EXEC_TRANSFER_RETURN -> ExecBroker返回以后事件
*/
uint32_t addVMEventCB(VMEvent mask, VMCallback cbk, void *data);
```

内存访问API:

```
//注册内存访问回调
VM.addMemAccessCB(MemoryAccessType type, InstCallback cbk,void *data,int priority);

//下面两个回调其实是qbdi帮我们做了范围过滤的操作
//注册指定地址范围内的内存访问回调
VM.addMemRangeCB(rword start, rword end,MemoryAccessType type, InstCallback cbk,void *data);

//注册指定地址的内存访问回调
VM.addMemAddrCB(rword address, MemoryAccessType type, const InstCbLambda &cbk);
```

**四. 更进一步观察细节**

dbi意味着需要修改原始指令添加instrument代码，那么就需要创建新的内存空间容纳这些代码并且重定向，由于不可能事先处理整个二进制代码，因此需要运行时监视程序指令流，只处理真正需要执行的代码块。

因此就引入了qbdi上下文和guest(我这里用虚拟化中的术语称之为guest)上下文，这有点类似于qemu tcg中的用x86指令模拟arm指令运行时的上下文切换与指令处理技术，两者有些相通性，只不过qbdi运行在和guest一样的用户进程中，也因此带来了一些缺陷: trace框架本身用到的非重入性库函数可能会导致死锁，而且qbdi对目标程序属于弱控制，不像qemu或者java虚拟机可以完全控制目标的执行流。

由于目标trace代码可能有pc相关指令因此需要重定向修复操作，这个步骤称为patch，而且需要加入跟踪指令，这个步骤称为instrument，还需要进一步组装加入上下文切换相关代码，因此整个执行过程如下: 反汇编 -> patch -> instrument -> 组装 -> 执行 -> 反汇编

**上下文切换:**

guest上下文主要由GPRState和FPRState结构组成，GPRState包括了体系结构的所有通用寄存器(也包括条件码)，FPRState则包括了所有浮点寄存器。它们都作为Engine类的成员变量。

```
typedef struct QBDI_ALIGNED(8) {
rword x0;
rword x1;
rword x2;
rword x3;
rword x4;
rword x5;
rword x6;
rword x7;
rword x8;
rword x9;
rword x10;
rword x11;
rword x12;
rword x13;
rword x14;
rword x15;
rword x16;
rword x17;
rword x18;
rword x19;
rword x20;
rword x21;
rword x22;
rword x23;
rword x24;
rword x25;
rword x26;
rword x27;
rword x28;
rword x29; // FP (x29)
rword lr;  // LR (x30)
rword sp;
rword nzcv;
rword pc;
  // ? rword daif; ?
  /* Internal CPU state
   * Local monitor state for exclusive load/store instruction
   */
struct {
rword addr;
rword enable; /* 0=>disable, 1=>exclusive state, use a rword to not break
                     align */
} localMonitor;
} GPRState;

typedef struct QBDI_ALIGNED(8) {
__uint128_t v0;
__uint128_t v1;
__uint128_t v2;
__uint128_t v3;

__uint128_t v4;
__uint128_t v5;
__uint128_t v6;
__uint128_t v7;

__uint128_t v8;
__uint128_t v9;
__uint128_t v10;
__uint128_t v11;

__uint128_t v12;
__uint128_t v13;
__uint128_t v14;
__uint128_t v15;

__uint128_t v16;
__uint128_t v17;
__uint128_t v18;
__uint128_t v19;

__uint128_t v20;
__uint128_t v21;
__uint128_t v22;
__uint128_t v23;

__uint128_t v24;
__uint128_t v25;
__uint128_t v26;
__uint128_t v27;

__uint128_t v28;
__uint128_t v29;
__uint128_t v30;
__uint128_t v31;

rword fpcr;
rword fpsr;
} FPRState;
```

切换到guest执行需要恢复GPRState和FPRState，而切回qbdi则需要保存GPRState和FPRState。在执行guest时宗旨是不能修改guest状态，包括栈和寄存器，因为被trace的代码可能各种各样，不能假设trace代码如何使用栈和寄存器，最好的方式就是原样维持否则将会引发与原有程序执行不一致的问题。

而对原始指令进行pc重定位和添加instrument代码可能会不可避免的引入寄存器的修改。设想有一个需要trace的代码片段，它使用了所有的通用寄存器进行某种计算，在里边添加的instrument指令是某种函数调用，调用到qbdi提供的指令跟踪函数(处于qbdi上下文)，那么这些instrument指令如何实现? 如果是近端可以使用pc相对寻址，如果是远端则需要借助于ADRP/LDR这样的指令，这样就引入了对某个guest寄存器的修改，就需要保存该寄存器，执行完指令以后再恢复。

那么保存到哪里又成了问题，像普通的函数调用是有调用约定，caller保存一些可能被callee修改的寄存器在栈上，调用完之后从栈中恢复。但对qbdi来说它不能保存在guest的栈上(会破坏原代码环境)，那么就需要保存到qbdi上下文的内存中，这段内存需要事先配置好让guest上下文中的代码可以相对寻址访问到，这个方案类似于arm中的常量池(Literal Pool), qbdi对应的则为ExecBlock。

借用官方文档里边的图:

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0iaWV2AfDfFv4nMPrjkiceLeibXcn6ib8TpJoiaTaUAX04DMnpm1R9ybNcw1YlYUsnLib9DEEYL4BwncVjQ4xpRjnYsvemrqslQ321I/640?wx_fmt=other&from=appmsg)

每一段需要执行的代码都被放置在了一个ExecBlock对象当中,它由两个4096大小的页组成:

```
llvm::sys::MemoryBlock codeBlock;
llvm::sys::MemoryBlock dataBlock;
```

这样在codeBlock当中的代码就可以使用相对寻址方式访问到dataBlock中的数据，在qbdi所支持的体系结构中，都支持相对寻址至少4096字节。

如果需要执行的代码多于4096字节那么会有多个ExecBlock,每一条需要执行的指令经过重定位并添加instrument片段以后都放置在codeBlock中，伴随着的还有prologue和epilogue代码用于上下文切换以及控制管理，而dataBlock中的GPRState和FPRState用于保存guest上下文, Host Context则保存qbdi一侧所需的上下文信息，因此这个方案会有一些内存冗余。

Shadows区域则保存着和patch、instrument相关的shadow数据如常量等:

```
shadows = reinterpret_cast<rword *>(
reinterpret_cast<rword>(dataBlock.base()) + sizeof(Context));
```

**结构图(引用自官方):**

**![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K24iczxfzBJjAVsjJgUR5sJ7DcnJNTG4mHWaFV5byNDT1CCPnjVD0PjPTKfS64vBDibbNTRY8ibH4UlWNAeOMhgK0PJn9yoCBA13I/640?wx_fmt=other&from=appmsg)![]()**

用户代码通过QBDI::VM暴露出来的api来和Engine对象进行交互,Engine负责总管整个控制流并且利用PatchDSL来对目标指令重定位、instrument和组装，PatchDSL是QBDI自己提出的概念，它用一个中间层让重新组装目标代码变的简单，如果是RET或者BR指令，以下的代码就可以实现重定位:

```
 /* Rule #1: Simulate RET and BR
   * Target:  RET REG64 Xn
   * Patch:   DataBlock[Offset(PC)] := Xn
   */
rules.emplace_back(
    Or::unique(conv_unique<PatchCondition>(OpIs::unique(llvm::AArch64::RET),
    OpIs::unique(llvm::AArch64::BR))),
    conv_unique<PatchGenerator>(GetOperand::unique(Temp(0), Operand(0)),
    WriteTemp::unique(Temp(0), Offset(Reg(REG_PC))),
    SaveX28IfSet::unique()));
```

ExecBlockManager顾名思义管理各个ExecBlock，最终执行的是ExecBlock中的Code Block代码。

**LLVM:**

qbdi使用LLVM的MC功能来反编译以及生成目标指令,比如反编译我们可以执行: echo "0x76 0x02 0x40 0xf9" | llvm-mc --disassemble -triple=aarch64

qbdi使用CMake的FetchContent\_Populate函数将https://github.com/llv...