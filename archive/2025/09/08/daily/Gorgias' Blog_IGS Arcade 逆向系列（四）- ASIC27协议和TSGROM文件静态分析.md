---
title: IGS Arcade 逆向系列（四）- ASIC27协议和TSGROM文件静态分析
url: https://gorgias.me/posts/igs_arcade_re_4/
source: Gorgias' Blog
date: 2025-09-08
fetch_date: 2025-10-02T19:48:44.967763
---

# IGS Arcade 逆向系列（四）- ASIC27协议和TSGROM文件静态分析

[Gorgias' Blog](/)

[Categories](/categories/)[Tags](/tags/)[About](/about)[Links](/links)

# IGS Arcade 逆向系列（四）- ASIC27协议和TSGROM文件静态分析

Monday, September 8, 2025

# 嵌入式架构分析

IGS的反盗版技术上不难，但是非常诡异，可能是代码写的太烂了。

IGS E2000 本质上，是 PC + 游戏基板 的组合（研华设计）。既要考虑到 Anti-Copy （反盗版），又需要考虑到软件工程上的复用。ASIC相当于一个完全黑盒的计算模块，将游戏关键逻辑放在里面，既能提升性能，也可以防止破解。

![diagram](diagram.png)

## 主程序流程分析

游戏主程序会开辟一段 0x200034的栈空间，其中缓冲区占0x200000，而且这个栈开辟出来后不会恢复，这会导致IDA Pro无法反编译，不知道是不是故意的。

![main](main.png)

首先需要patch这个缓冲区大小，减小函数的栈帧，然后将函数 undefine，最后重新识别，就可以成功反编译。

![edit_func](edit_func.png)

1. Kernel mount\_root 时，以及游戏程序启动时 会校验 BIOS 版本信息，开发者却说是获取CRC结果，结果我愣是找遍了所有CRC的位置，也没找到任何反盗版有关的CRC计算逻辑；
2. BIOS 信息校验失败就校验PCI的驱动信息，如果失败，好像也没有任何操作，但其他地方也插入了许多一样的校验桩，校验失败就会阻止运行；
3. 系统初始化：屏幕、音频、图形、文字、语言、ASIC、Timer、PLXPCI、游戏、音乐、控制器、摄像机、台账、控制、投币、混合器等等；
4. 刷新4次ASIC，why???；
5. 加载基础 action 文件（TSGROM格式），每次加载都刷新一次ASIC；
6. 游戏版本校验，显示第一屏，加载字体，加载声音；
7. 加载读卡器；
8. 游戏Loop，4种状态(Game, Test, Setting, Demo)，可通过ASIC控制

![main_loop](main_loop.png)

游戏使用了SDL 1.2.7开发，SDL（Simple DirectMedia Layer）是一个跨平台的多媒体开发库，主要用于提供对音频、输入设备（键盘/鼠标/游戏手柄）和图形硬件的底层访问‌。但是这个性能比较低，只适合2D游戏。Percussion Master 2008 是2D游戏。Speed Driver 2 是 3D游戏，两者的差别可能很大。

开发者在游戏主程序每一处与 ASIC 交互的位置，都插了代码桩，暂时把他称作 `RealTimeEvent`，应该是统一事件处理程序，每次逻辑的变化、动画的变化，都需要刷新事件。用来实现各种复杂的控制功能，也附带了一些反盗版功能。不得不吐槽，这个代码质量真糟糕，每次都要做大量的计算，性能很差，和用纯 js + html 开发单页面应用一样。

状态检查桩的逻辑

1. 更新时钟
2. 计时器检查
3. Action处理
4. 音乐处理
5. 音频处理
6. 按键状态以及控制输入
7. 台账
8. 游戏币处理
9. PLX PCI 状态处理
10. SDL 事件处理
11. 绘制动态五边形动画
12. PCI 控制写入
13. ASIC 27 命令写入
14. PCI 数据读取
15. 图形刷新

### 区域初始化

percussion master 2008 支持7个地区，3种语言；简体中文、繁体中文、英文。

![location_table](location_table.png)

## ROIO BIOS 信息校验

内核会运行一个驱动 /dev/roio, 游戏程序通过此驱动对比内置的版本信息表，实现校验功能。内核本身和游戏程序均内置了表格，原理应该是开发者通过某些工具解析了BIOS信息，然后将物理偏移硬编码到程序和内核里面。

![bios_table](bios_table.png)

内核和主程序的 BIOS 信息表结构有些区别，Kernel的4字节对齐，但使用原理都是一样的。

Game BIOS table

```
struct bios_item {
    unsigned int index;  // index
    unsigned char table_cmp_max_count;
    unsigned int value_addr; // base addr 0xC0000000
    unsigned char char_cmp_max_count;
    unsigned int name_addr;
}
```

Kernel BIOS table

```
struct bios_item {
    unsigned int index;  // index
    unsigned int table_cmp_max_count;
    unsigned int value_addr; // base addr 0xC0000000
    unsigned int char_cmp_max_count;
    unsigned int name_addr;
}
```

对比的逻辑也很简单，

第一步通过遍历程序内置的 BIOS Table，获取版本字符串地址、目标字符串物理地址、遍历轮数等。
第二步，通过 IOCTL Call /dev/roio， 对比System ROM 区域指定偏移和程序内置的对应字符串，只要有一个字符相等就通过，太蠢了。

该内核只允许运行在4种主板，但是游戏允许运行在更多的设备，因此需要校验主程序、内核、主板是否匹配。这是反盗版的机制，直接patch掉就行了。

经过统计，地址和版本字符串如下，所有地址都是0x0f0000起始。

```
# Kernel + Game
0x0F086E   i852-W83627HF
0x0FEC7C   i852-W83627HF
0x0FEC8A   6A69YILTC-00
0x0FECDE   Ph6A69YILT

# Game
0x0FE0C1   L4S5MG3
0x0FEC84   6A6IXE19C-00
0x0FECDF   I6A6IXE19
0x0FE0C1   L4S5MG/651+
0x0F006D   nVidia-nForce
0x0FECDE   Ph6A61BPA9
0x0FEC8A   6A61B_00C-00
0x0FECDE   Ph6A61B_00
```

接下来分析ROIO驱动，大部分代码都插了 Anti-Copy 暗桩，使用XOR，对性能影响最小，可以防止游戏A程序放到游戏B的系统运行。

* 输入参数 mask 0x1FB8408E
* 返回值 mask 0xC2E83AB8

![ioctl_0xfc](roio_0xfc.png)

ROIO 的 Magic Number 有三种：

* 0xfc 获取目标地址的32位数值，小端
* 0xfd 获取目标地址的32位数值，大端
* 0xfe 获取目标地址的8位数值

最后再 xor 0xC2E83AB8

![roio_ioctl_dispatcher](roio_ioctl_dispatcher.png)

这里的data作为偏移，基址是0xc0000000，然后加上BIOS信息的值，是因为x86打开了paging，因此CPU访问内存需要走虚拟地址。Linux i386 对于虚拟地址偏移的设定如下

```
#define __PAGE_OFFSET (0xC0000000)
#define __pa(x)			((unsigned long) (x) - PAGE_OFFSET)
#define __va(x)			((void *)((unsigned long) (x) + PAGE_OFFSET))
```

通过IOMEM的map，也可以看到BIOS信息的地址位于 System ROM

```
# cat /proc/iomem
00000000-0009fbff : System RAM
0009fc00-0009ffff : reserved
000a0000-000bffff : Video RAM area
000c0000-000c7fff : Video ROM
000f0000-000fffff : System ROM
00100000-1feeffff : System RAM
  00100000-0050aab5 : Kernel code
  0050aab6-006f8f27 : Kernel data
1fef0000-1fefffff : reserved
1ff00000-1ff003ff : Intel Corp. 82801DB Ultra ATA Storage Controller
d0000000-dfffffff : PCI Bus #01
  d0000000-dfffffff : PCI device 10de:0221 (nVidia Corporation)
e0000000-e7ffffff : Intel Corp. 82852/855GM Host Bridge
e8000000-eaffffff : PCI Bus #01
  e8000000-e8ffffff : PCI device 10de:0221 (nVidia Corporation)
    e8000000-e8ffffff : nvidia
  e9000000-e9ffffff : PCI device 10de:0221 (nVidia Corporation)
eb000000-eb01ffff : PLX Technology, Inc. PCI <-> IOBus Bridge Hot Swap
eb020000-eb02007f : PLX Technology, Inc. PCI <-> IOBus Bridge Hot Swap
eb021000-eb0213ff : PLX Technology, Inc. PCI <-> IOBus Bridge Hot Swap
eb022000-eb022fff : Intel Corp. 82801BD PRO/100 VE (CNR) Ethernet Controller
  eb022000-eb022fff : e100
eb100000-eb1003ff : Intel Corp. 82801DB USB2
  eb100000-eb1003ff : ehci_hcd
eb101000-eb1011ff : Intel Corp. 82801DB AC'97 Audio Controller
  eb101000-eb1011ff : Intel 82801DB-ICH4
eb102000-eb1020ff : Intel Corp. 82801DB AC'97 Audio Controller
  eb102000-eb1020ff : Intel 82801DB-ICH4
fec00000-ffffffff : reserved
```

BIOS芯片封装是PLCC 32，使用RT809H成功dump。

![PLCC32_BIOS](PLCC32_BIOS.jpg)

使用系统启动后，BIOS ROM的一些数据被解析到了内存里，不是1:1 copy，偏移地址是 0xF0000，。

![bios_version](bios_version.png)

## PCCard 随机数校验

我实在不理解这个代码的目的是什么，驱动代码里有SPY的关键词，可能是反嗅探用的暗桩？在启动程序、初始化游戏和print日志会触发，如果上面的BIOS Check 失败了，也会触发此校验。通过ioctl来请求`/dev/pccard0`，获取结果或者不获取结果。

![pccard_random_value_check1](pccard_random_value_check1.png)

request 0 列表，用于对比结果。列表有4个成员，对应相关偏移。从四个里随机选一个，并带上随机数，随机值区间 [17, 768]，本地计算后，发到驱动执行一下，然后发回来，实际上PCI没有真正参与。

```
0x64 基址：0xC8000000 设置 SPY_FLAG spy_fixec_func
0x6e 基址：0xD0000000 设置 SPY_FLAG spy_quit_func
0x96 基址：0xA8000000 设置 SPY_FLAG
0xa0 基址：0xB0000000 设置 SPY_FLAG
```

request 1 列表，长度17

```
0xfe,0xc8,0xfd,0xa0,0x96,0x6e,0x64,0xdd,0xde,0xdf,0xe0,0xe1,0xe2,0xe3,0xe4,0xe5,0xe6
```

看[1,255]的值是否能命中列表的值，尝试5-30次，如果命中，尝试次数-1，然后再来一次。如果没命中，就通过ioctl来请求随机值对应的偏移（参数[17,768]），幻数就是命中的那个值。我感觉可能是用来初始化驱动的，实在想不到其他作用了。为什么写的那么复杂？

![pccard_random_value_check](pccard_random_value_check.png)

在游戏主程序的某处，发现了残留的代码，异或的内容是 0xD4AA268A，在 percussion master 2008 未发现触发逻辑，应该是另一个游戏的暗桩。可以更确定，这个功能就是为了反盗版的。（虽然设计的很烂）

![pccard_random_value_check2](pccard_random_value_check2.png)

## ASIC 27 协议

### A27 初始化

游戏主程序与I/O板的通信，经过 PLX PCI 9030 芯片，以共享内存的方式，进行数据交换。

游戏启动后，ASIC 27 初始化之前，会先加载PCI 9030驱动，并开辟一段缓冲区，专门用来存放 ASIC Buffer，里面有各种数据状态。开发者称作 CommandPort。

![pci9030_init](pci9030_init.png)

接下来初始化 ASIC 27，首先更新Checksum，将位于buffer的按键灵敏度、按键输入、灯光状态、system mode、buffersize累加得到数值checksum，然后放在buffer的两个位置。后续的每次ASIC 27 请求，都会重新计算 checksum。

首先写入0x2024字节到ASIC 27，cmd: 0xfe，也就是直接拷贝缓冲区数据到到共享内存。
然后ASIC处理后，刷新的共享内存，并且会将sm从0x1c改为其他值，代表处理结束。

ASIC会将游戏的配置信息，同步OS用于更新游戏配置，将会更新以下目录

```
./pm2_data/storename.dat
./pm2_data/soundset.bin
./pm2_data/gameset.bin
```

将sm设为0，同时再更新一次 checksum，发送到A27

### System Mode

经过分析，以下模式

* 0x0: 默认模式
* 0x1: ASIC测试数据读取
* 0x2: 按键测试
* 0x3: 蜂鸣器测试
* 0x4: 灯光板测试
* 0x5: 投币测试
* 0x6: Trackball 测试
* 0x7: SelMode，IGS Logo
* 0x8: Teammark
* 0xc: Coin Page
* 0xf: option
* 0x14: Photo
* 0x10: Song Play
* 0x1a: CCD
* 0x1d: 调整音量

### A27 System Mode Write 状态机

发送数据到ASIC之前的预处理，当 sm 为以下值，无处理逻辑，返回1

```
0x0,0x2,0x3,0x6,0x9,0xa,0xb,0x11,0x12,0x15,0x16,0x17,0x18,0x19,0x1b,0x1c,0x1e
```

* 0x1: 测试数据写入
* 0x4: 灯光测试
* 0x5: 投币测试
* 0x7: SelMode
* 0x8: Teammark
* 0xc: 代码已删除
* 0xe: 代码已删除
* 0xf: 代码已删除
* 0x10: Song
* 0x13: 代码已删除
* 0x14: 代码已删除
* 0x1a: 摄像机测试
* 0x1d: 调整音量

其他值则触发 Assert

### A27 System Mode Analysis 状态机

ASIC 返回的数据，由游戏主程序处理，当 sm 为以下值，无处理逻辑，返回1

```
0x0,0x6,0x9,0xa,0xa,0xb,0x11,0x12,0x15,0x16,0x17,0x18,0x19,0x1b,0x1c,0x1d,0x1e
```

System Mode 对应的处理

* 0x1: ASIC测试数据读取
* 0x2: 进入按键测试
* 0x3: 进入蜂鸣器测试
* 0x4: 进入灯光板测试
* 0x5: 投币测试
* 0x7: 加载 IGS LOGO
* 0x8: 加载 Teammark 数据
* 0xC: 代码已删除
* 0xE: 代码已删除
* 0xF: 代码已删除
* 0x10: Song
* 0x13: 代码已删除
* 0x14: 代码已删除
* 0x1a: CCD 信息

其他值则触发 Assert

### 按键状态机

```
                press
        ┌──────────────────────┐
        │                      │
   ┌────▼─────┐  release    ┌──┴─────┐
   │   Idle   │────────────►│Released│
   │   (0)    │             │   (3)  │
   └────▲─────┘             └──▲─────┘
        │                      │
        │ press                │ release
        │                      │
   ┌────┴─────┐ long press  ┌──┴─────┐
   │ Pressed  │────────────►│Holding │
   │   (1...