---
title: 【Android 原创】某短视频虚拟机分析和还原
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651140757&idx=1&sn=bc87af356202c3dbe2122de83c028fd5&chksm=bd50a2c18a272bd7d0740d009513bfca6b50388937ce72fee2a3a28d1c5c8d6bc62f16ce9bd3&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2024-07-03
fetch_date: 2025-10-06T17:43:29.212197
---

# 【Android 原创】某短视频虚拟机分析和还原

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZINkZb7anSXe3x6WuxjA3B3lfC9KCbDbat7l7xxIfiagHeiaiaqXZV89U6z6ZnKVqPYjwLQMxCxlZc0g/0?wx_fmt=jpeg)

# 【Android 原创】某短视频虚拟机分析和还原

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：金罡**

# 前言

在windows流行的时候，虚拟机保护是多人不敢碰的东西现在依然也是如此，pc的性能比移动端性能要高出不少，虚拟化和变异的代码多到令人发指，因此在加密保护强度上要比移动端要强很多很多，为了移动端App更好的体验(ANR率)移动端加密强度短时间内不会达到pc上的强度，随着移动cpu性能越来越好相信加密强度会逐年加强。

早年兴趣使然分析研究过windows端VMProtect、Safengine Shielden、Themida、VProtect、Enigma Protector等等虚拟机，最近发现国内流行的短视频也有虚拟机加密同时也比较感兴趣，便开始了我的分析之旅。

分析任何虚拟机必须要扣汇编指令级细节。

# 准备

安卓诞生这么多年了至今没有像windows端olldbg、x64dbg那样友好的调试器，IDA PRO虽然自带了安卓调试器总是没有相像中的稳定。lldb作为移动端iOS和android开发的御用调试器，带源码调试在开发环境中还算比较友好，而汇编级调试只能输入命令行了，这是很多用惯了gui调试器的人接受不了的，但是个人发现lldb调试稳定性出奇的好，功能上比IDA Pro的安卓调试器强大太多了。

## 工具 && 参考文档

* 静态分析工具
  IDA Pro
  IDA Pro中的变量和标签命名约定: 1. 无下线为精确的名字，已经非常了解代码的功能和含义，例如："xxx"。2. "\_"单下划线定义为代码的功能和含义比较模糊，例如："\_xxx"。3. 双下划线为分析的代码模糊不清，由于地址不好记忆但需要命名以区分，例如："\_\_xxx"。
* 动态分析工具
  lldb
* ARM参考文档
  《Arm Architecture Reference Manual》
  《ARM Cortex-A Series Programmer's Guide for ARMv8-A》
* 其他工具
  CyberChef

# 虚拟机分析

libEncryptor.so一共包含了三套虚拟机，三套虚拟机各自独立并且代码一模一样，本文重点只分析vm2虚拟机。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZINkZb7anSXe3x6WuxjA3B33ibiavOacibrYB6BY1kL8yEkiaG3KtOyATBJJCDicxADzZiagibT4ibic3qe43A/640?wx_fmt=jpeg&from=appmsg)

虚拟机指令编解码参考借鉴了arm64的一部分规则，并实现了自己的一套规则，在后面的解码分析中会有很多和arm64解码相似的地方。
另外虚拟机并没有像VMProtect那样将一条指令分割成多条"微指令"的方式，此虚拟机没有把当前真实的上下文放到虚拟机上下文去模拟执行，而是运行了一套自己单独的上下文。

1. `vm1`: 0xDA0
   在JNI\_OnLoad中被调用，该虚拟机起始位置在0xDA0，主要作用解密是注册java native所需要的字符串和调用RegisterNatives进行注册。
2. `vm2`: 0x2AC4
   虚拟机起始位置在0x2AC4，是java注册的原生接口com.bytedance.frameworks.encryptor.EncryptorUtil.ttEncrypt(byte[] buff, int size)，用来加密buff字节数组。
3. `vm3`: 0x444
   代码位置在0x444，用于生成aes-128 cbc算法的key和iv。

在函数中调用虚拟机时会传入一个指针数组类型参数变量，这是传入到虚拟机入口的唯一参数。

```
void vm_entry(*int args)
```

c伪代码来表示函数调用虚拟机入口

```
void ttEncrypt(char* buff, int buff_size) {
    int dst_size = size ＋0x76;
    char* pDstBuff = malloc(size ＋0x76);
    vm_entry(buff, size, pDstBuff, &dst_size);
}
```

反汇编版本：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZINkZb7anSXe3x6WuxjA3B3IXDl1ZibwWCu0S89hzDQy8gxUWAq8SXhxH8cP8uibjzUGzjtIwcmfpjQ/640?wx_fmt=jpeg&from=appmsg)

## 入口

IDA Pro查看入口的cfg图，复杂程序看似很难其实一点都不简单，话说回来cfg看起来和ollvm的混淆平坦化非常相似，其实和ollvm混淆关系不大，只不过一部分的switch被拉平了，在了解调度逻辑后分析也不算复杂。
在代码中依然能看到两个ollvm swtich var变量，其作用没有详细分析，但整个cfg图确定与ollvm关系不是很大，猜测开启ollvm后性能会大幅下降影响app启动速度了。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZINkZb7anSXe3x6WuxjA3B3wq5kCicEbjAkbmzL5Zh5jbwm7vE1HsgibrHRH8E3hr4FkLAw0V6AwpEg/640?wx_fmt=jpeg&from=appmsg)

在进入虚拟机运行时前，在入口需要准备虚拟机所需的内存和参数。对虚拟机内存布局情况必须了解如指掌，这样在动态和静态分析时才不会迷失方向。

* 分配空间
  入口首先会分配堆栈空间，真实堆栈空间中包含了参数占用、虚拟机运行时的上下文(context)和虚拟机堆栈的所使用的空间，
  从上图代码中看出虚拟机堆栈起始位置位于sp+0x38，结束位置sp+0x4D8，大小4D8-0x38=4A0，虚拟机所有可用真实内存为0x4A0，其中上下文(context)使用0x150，剩余分配给虚拟机堆栈4A0-150=2C0。
  vm\_entry调用vm2\_run时的堆栈内存布局情况:

| SP | 类型 | 变量名 | 注释 |
| --- | --- | --- | --- |
| 0x0 |  |  | 未使用 |
| 0x8 | char \* | pSrcBuffer |  |
| 0x10 | int | srcSize |  |
| 0x18 | char \* | pDstBuffer |  |
| 0x20 | int \* | pDstBufferSize |  |
| 0x28 | void \* | pCall\_register\_trampoline |  |
| 0x30 | void \* | pVMMemoryEnd | 偏移0x510 |
| 0x38 | vmMemoryStart | 虚拟机运行时专用内存起始位置 |  |
| ... |  |  |  |
| 0x510 |  | vmMemoryEnd | 虚拟机运行时内存结束位置 |
| 0x518 |  |  |  |
| 0x520 | x28 |  |  |
| 0x528 | x19 |  |  |
| 0x530 | x29 | 上一个栈桢地址 |  |
| 0x538 | x30 |  |  |

* 参数
  在进入虚拟机正式执行前，vm2\_entry在进入虚拟机运行时前会对5个参数进行初始化。
  `pOpcode`：opcode指针指向虚拟机要执行的代码
  `pArgs`：传入虚拟机的参数
  `pReserve`：未使用，用途暂时未知
  `pExternalFunc`：调用虚拟机外的函数列表，此列表是加密的。
  `pVmData`：一个结构体指针，结构体存储了两指针分别是函数跳板地址另一个是虚拟机内存结束地址，{0x0: pCallRegisterTrampoline, 0x8: pVMMemoryEnd}

  ```
  vm2_run(void* pOpcode,  void* pArgs,  void* pReserve,  void* pExternalFunc， void* pVmData);
  ```
* opcode
  vm2的opcode起始地址在0xB090，共占用0x2D8字节，每个opcode占用四个字节。
* 跳板函数
  跳板函数是衔接适配虚拟机和外部函数以及参数的桥梁，它包含来自虚拟机传递的两个参数, 参数1：x0是调用跳转的一个外部函数地址，参数2：x1是外部函数需要使用的参数指针。

  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZINkZb7anSXe3x6WuxjA3B3qfznU7iaBJUgd3repAYJvC50FnLPs80eqbSBjlmHUMFEgUTV0lv8n8w/640?wx_fmt=jpeg&from=appmsg)
* 外部函数
  外部地址函数目标地址是被简单加密过的，在虚拟机指令中使用加法解密这8个地址，例如：0xDDD2D0(加密地址数据) + FF225870(key) = 0x2B40(目标地址)。
  截图中IDA Pro以默认0基址的地址，在调试时看到的地址数据是被代码手动重定位后的数据。

  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZINkZb7anSXe3x6WuxjA3B3eaVZjfuibteM4j1dlgGPA6KkkqGibnkbr44a0Wq9ics0dGEZXRR9dqGoQ/640?wx_fmt=jpeg&from=appmsg)

## 初始化

vm2\_run仅仅只分配了保存被调用者寄存器的堆栈内存空间，并没有分配空闲的堆栈内存，在虚拟机真实开始之前会将传递进来的5个参数即0x-x4对虚拟机中的虚拟寄存器和真实专用寄存器进行初始化。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZINkZb7anSXe3x6WuxjA3B35zAicYnKGXSQgCtYicdUOicahx1c1iaibNaibPvfhxpQYjSz4KxrgEOFFnqw/640?wx_fmt=jpeg&from=appmsg)

vm\_run还初始化了解码opcode的switch表，在初始化时发现一共初始化了6张switch表，当然在handler中还存在其他switch表，这么多表是如何来的？猜测编写时只有1-2张表，在编译器优化后表就被分割成多块了。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZINkZb7anSXe3x6WuxjA3B3IDA9HcMksBUbdp2A1TOPBooAcs2s3BTsaSgtdCYQtRWlj51UYfn6hA/640?wx_fmt=jpeg&from=appmsg)

* | 虚拟寄存器初始化 vm2\_run初始化时会将传递的5个参数赋值给虚拟寄存器，其中包括PC和SP的值。 | 虚拟寄存器 | 参数 | 注释 |
  | --- | --- | --- | --- |
  | x0 |  | x0始终为0，XZR寄存器? |  |
  | x4 | arg2: pArgs |  |  |
  | x5 | arg3: pReserve |  |  |
  | x6 | arg4: pExternalFunc |  |  |
  | x7 | arg4: pVmData->pCallRegisterTrampolineFunction |  |  |
  | x29(SP) | arg5: pVmData->pVmMemoryLimit - 0x150 | SP的初始值 |  |
  | x31(LR) | 初始值为0，寄存器名不确定，vm退出时保存退出代码编号 |  |  |
  | PC | arg1: pOpcode |  |  |
* | 真实专用寄存器 虚拟机运行时使用了真实虚拟器，其中包括临时寄存器和专用寄存器，临时寄存器保存多种类型的值，而专用寄存器在虚拟机从开始到退出只保存一种指定类型数据或恒定不变。 opcode位域伪代码： w12保存了4位32字节的opcode，在opcode首次解码时，位域中的变量会放到真实寄存器。 位域伪代码示例： `w12[26]`: 取第26位到放到入目标的26位 `w12[26->0]`: 取第26位并放入到目标的指定位 `w12[27-26->1-0]`: 取27位和26位放入到目标第1位和第0位 ` | `: 按位或 | 真实寄存器 | 注释 |
  | --- | --- | --- | --- |
  | x0 | temp/pcode |  |  |
  | x1 | temp,保存[x19-0x20]的值某种流程控制 |  |  |
  | x2 | temp |  |  |
  | x3 | temp |  |  |
  | x4 | 虚拟寄存x4，初始化时保存pBufferInfo(x1)，虚拟机中保存跳板函数地址 |  |  |
  | x5 | 虚拟寄存x5，初始化时保存数值为0，虚拟机运行时跳板函数的参数指针 |  |  |
  | x6 | ollvm混淆switch\_var，初始值:0x400000b，这个应该是llvm混淆的switch var |  |  |
  | w7 | ollvm混淆switch\_var，初始值:0x200fff，这个应该是llvm混淆的switch var |  |  |
  | w8 | w12[20-16]   operand1 Xt/Xm,det register index? |  |  |
  | w9 | w12[25-21]   operand2 Xn,src register index? |  |  |
  | w10 | w12[15->4] |  w12[14->3] | w12[13->2] | w12[12->1] | w12[31->0],5个位合并到低5位 |  |  |
  | w11 | w12[30->4] | w12[29->3] | w12[28->2] | w12[27-26->0-1],组成的低5位 |  |  |
  | w12 | 32位的opcode |  |  |
  | w13 | w12[31] |  |  |
  | w14 | w12[30] |  |  |
  | w15 | w12[29] |  |  |
  | w16 | w12[28] |  |  |
  | w17 | w12[27] |  |  |
  | w18 | w12[26] |  |  |
  | x19 | 虚拟机下文负偏移指针指向可使用内存最高上限的地址与vmMemoryLimit值相同，使用负偏移对上下文进行访问。 |  |  |
  | x20 | call\_register\_trampoline 跳板地址 |  |  |
  | x21 | Context，上下文指针 |  |  |
  | x22 | switch\_table7 |  |  |
  | x23 | switch\_table6 |  |  |
  | w24 | 默认为1 |  |  |
  | x25 | switch\_table5 |  |  |
  | x26 | switch\_table3 |  |  |
  | x27 | switch\_table\_main |  |  |
  | x28 | switch\_table2 |  |  |
  | x29(fp) | 未使用 |  |  |
  | x30(lr) | switch\_table\_4(3A) |  |  |
* | 虚拟机context 虚拟机中也有专用寄存器，在调用外部函数时，其中`x4`虚拟机中保存外部函数地址，`x5`虚拟机中保存参数指针，`x25`虚拟机中调用外部函数时的跳板地址。另外虚拟寄存器和aarch64中的寄存器并不是一一对应的，在这里只是对每个虚拟寄存器启了一个相应的名字方便理解和记忆。 | 负偏移 | 虚拟寄存器 | 注释 |
  | --- | --- | --- | --- |
  | -0x150 |  | 虚拟机堆栈SP初始位置 |  |
  | -0x148 |  |  |  |
  | -0x140 |  |  |  |
  | -0x138 | pc | pc指针，真实寄存器x21中的值指向此地址，handler使用 |  |
  | -0x130 | x0 | 初始化值:0,虚拟机中开始到结束始终为0，XZR寄存器? |  |
  | -0x128 | x1 |  |  |
  | -0x120 | x2 |  |  |
  | -0x118 | x3 |  |  |
  | -0x110 | x4 | 初始化值：pBufferInfo，专用寄存器：虚拟机中调用外部函数时保存外部函数地址 |  |
  | -0x108 | x5 | 初始化值: 0，专用寄存器：虚拟机中调用外部函数时保存参数指针 |  |
  | -0x100 | x6 | 初始化值: vm2\_external\_func\_list |  |
  | -0xF8 | x7 | 初始化值: call\_register\_trampoline\_function |  |
  | -0xF0 | x8 |  |  |
  | -0xE8 | x9 |  |  |
  | -0xE0 | x10 |  |  |
  | -0xD8 | x11 |  |  |
  | -0xD0 | x12 |  |  |
  | -0xC8 | x13 |  |  |
  | -0xC0 | x14 |  |  |
  | -0xB8 | x15 |  |  |
  | -0xB0 | x16 |  |  |
  | -0xA8 | x17 |  |  |
  | -0xA0 | x18 |  |  |
  | -0x98 | x19 |  |  |
  | -0x90 | x20 |  |  |
  | -0x88 | x21...