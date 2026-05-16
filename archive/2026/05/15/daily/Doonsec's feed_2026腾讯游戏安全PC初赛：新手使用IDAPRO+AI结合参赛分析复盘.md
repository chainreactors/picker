---
title: 2026腾讯游戏安全PC初赛：新手使用IDAPRO+AI结合参赛分析复盘
url: https://mp.weixin.qq.com/s/BNIK4UDQ9GuFm9jIUW8Fkg
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:10:56.843669
---

# 2026腾讯游戏安全PC初赛：新手使用IDAPRO+AI结合参赛分析复盘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3qNInw2Cnt0V5jsX8zpTRvjfiaxMWwmbNWicRDXwrara91PAq3saDKIsQGEonHkDhksmNKN4B8NvtFlTYiaicIicktQhPgK5KcWM4Q/0?wx_fmt=jpeg)

# 2026腾讯游戏安全PC初赛：新手使用IDAPRO+AI结合参赛分析复盘

刘宝
刘宝

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 这篇文章是我对 ShadowGate 题目的完整复盘整理版。和之前的阶段性记录不同，这一版的目标不是只写“我已经做到哪”，而是尽可能把整道题的分析链路整理完整。

不过我想把边界说清楚：

* 文中有一部分内容，是我自己本地逆向、写工具、验证协议后得到的结论；
* 还有一部分，是我当时没有完全做出来，后面参考了吾爱破解上一篇公开 writeup 才补齐的内容；
* 所以这篇文章不是“纯原创完整通关”，而是一篇以我的分析为主、并结合公开 writeup 补全后续步骤的复盘文。

**0****0**

**样本与题目理解**

题目样本主要包括三部分：

* 驱动：ShadowGateSys.sys
* IDA 数据库：ShadowGateSys.sys.i64
* 用户态程序：ShadowGateApp.exe

从题目行为来看，它表面上是一个“迷宫 + 驱动 + 最短路”的组合题，但真正核心并不是迷宫本身，而是：

* 用户态如何与驱动通信；
* 驱动如何把“移动结果”反馈回用户态；
* 这些反馈中，哪些是正常返回，哪些是隐藏泄露通道。

如果把题目拆开，其实就是：

* 加载驱动并正确通信；
* 找出所有隐匿通信方式；
* 还原迷宫地图；
* 求最短路；
* 到达终点并恢复最终 Flag。

##

**0****1**

**我本地首先确认出来的内容**

### 1. 用户态入口：\\.\ShadowGate

这题最先让我锁定方向的，不是驱动，而是用户态控制台程序。

从 ShadowGateApp.exe 的字符串和控制逻辑里，可以直接得到：

* 设备路径：\\.\ShadowGate
* 两个全局事件：

o Global\MazeMoveOK

o Global\MazeMoveWall

对应截图如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3iajOzTWeUx0Tib2yq4encx5homodhzxIYF5RicNNkZXIR9nGhP9BbDpQEzEllzKrBDPnIaia0Kx9M9JlJnbMCLHVFyd89Qib9zfVw/640?wx_fmt=other&from=appmsg)

这一步非常关键，因为它说明：

* 这题并不是完全黑盒；
* 用户态和驱动之间存在一个清晰可复现的通信入口；
* 同时，“移动结果”很可能还通过命名事件额外传回用户态。

### 2. 驱动侧设备对象与初始化框架

回到 ShadowGateSys.sys 之后，我本地确认到：

* DriverEntry 在 0x140008000
* 很快会跳转到实际初始化例程

初始化阶段至少做了这些事情：

* 分配一块大小为 0x1D8 的内存；
* 创建设备对象 \Device\ShadowGate；
* 创建符号链接 \??\ShadowGate；
* 注册分发函数。

驱动侧对应设备路径与用户态完全对上：

* 驱动：\Device\ShadowGate
* 符号链接：\??\ShadowGate
* 用户态：\\.\ShadowGate

这意味着我后续完全可以围绕 CreateFileW + DeviceIoControl 来做实验。

### 3. 主通信路径落在 IRP\_MJ\_DEVICE\_CONTROL

我本地确认到的主要分发表如下：

* IRP\_MJ\_CREATE -> 0x1400014B0
* IRP\_MJ\_CLOSE -> 0x140001410
* IRP\_MJ\_DEVICE\_CONTROL -> 0x140001540
* DriverUnload -> 0x140001840

所以这题真正要啃的核心函数，其实就是：

* IRP\_MJ\_DEVICE\_CONTROL

也就是说，整道题的协议层本质上就是若干个 IOCTL。

### 4. 三个核心 IOCTL 已经对上

我当时本地最先恢复出来的三个控制码是：

|  |  |  |  |
| --- | --- | --- | --- |
| IOCTL | 功能 | 输入 | 输出 |
| 0x8001200C | 查询迷宫几何信息 | 无 | 24 字节 |
| 0x80012008 | 重置迷宫状态 | 无 | 无 |
| 0x80012004 | 执行移动 | 12 字节 | 0x84 字节 |

其中 0x8001200C 返回六个 DWORD：

* width
* height
* entry\_x
* entry\_y
* exit\_x
* exit\_y

公开 writeup 里对这三个 IOCTL 的识别图如下：
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3U4o4RaHTHIflicibHBR46RZDMrsCRd8wVZ0vxseGA7gAaOiaRdr1icy3QCGkHGyVibyQicmBeeatXkMMOfDxshleUsocibc3JAmdXJI/640?wx_fmt=other&from=appmsg)![]()

这一部分我本地和公开 writeup 是能互相印证的。

### 5. 用户态控制台里的逻辑方向编码

从 ShadowGateApp.exe 的命令跳转表中，我本地能恢复出一套应用层方向语义：

* UP = 0x10
* DOWN = 0x20
* LEFT = 0x30
* RIGHT = 0x40

接受的按键分别是：

* W / I
* S / K
* A / J
* D / L

程序还支持：

* R：重置
* T：查看日志
* H：帮助
* Q / ESC：退出

到这里为止，我已经能比较稳定地还原“控制台程序怎么看待方向”的这一层。

### 6. 我已经明确确认的两类隐藏泄露通道

这是我当时最重视的一部分，因为我觉得这题的本质不在迷宫，而在“反馈机制”。

#### 命名事件

已经明确存在：

* Global\MazeMoveOK
* Global\MazeMoveWall

这组名字几乎已经把用途写脸上了：

* 成功前进 -> MazeMoveOK
* 撞墙失败 -> MazeMoveWall

#### 命名信号量

我本地还恢复出了两组混淆后的名字：

* Global\{B8E2C3D0
* Global\{A7F3B2C1

结合驱动中出现的：

* ObReferenceObjectByName
* KeReleaseSemaphore
* ObfDereferenceObject

我能比较有把握地说：

* 除了事件以外，驱动还会通过命名信号量额外传递状态。

### 7. 我已经写了用户态工具继续推进

为了不让分析停留在“静态猜测”，我本地还写了一个工具：

* tools/shadowgate\_tool.py

它现在已经能做：

* 打开 \\.\ShadowGate
* 调 query / reset / move
* 监控命名事件
* 监控命名信号量
* 统计耗时
* 读取返回缓冲区关键字段
* 可选监控用户态内存变化

也就是说，我当时虽然还没完整把题做完，但已经把后续实验框架搭起来了。

**0****2**

**当时没完全做出来，后面参考公开 writeup 补上的部分**

这一节的内容，严格来说不属于“我当时已经独立做出来的结果”，而是我后面参考了吾爱破解那篇文章之后，重新整理并补进来的。我会尽量用自己的表达去写，但要明确说明来源。

参考文章：

* 52pojie《2026腾讯游戏安全PC初赛Writeup》
* 链接：https://www.52pojie.cn/thread-2102723-1-1.html

### 1. 驱动里那块 0x1D8 全局对象，确实可以看成迷宫状态结构体

公开 writeup 给出的一个非常重要的信息是：

* 初始化时分配的那块 0x1D8 内存，tag = Maze
* 全局指针通常记作 P

同时它还给出了一份候选结构体：

```
struct Maze{    UCHAR maze[172];    struct Pos Position;    UCHAR OtherState[8];    UINT32 MoveCount;    UCHAR StatusFlag;    UCHAR Reserved1[255];    UINT64 SpinLock;    UINT64 ProcessId;    UINT64 ThreadId;};
```

结合文中的偏移说明，可以大致理解成：

* 结构体前部是一块连续的迷宫网格区；
* 中间是当前位置和若干状态字段；
* 后部包含移动计数、锁和 PID/TID。

公开文章中还把迷宫网格解释为：

* 13 x 13
* 0 表示可通行
* 1 表示墙

这里我自己的看法是：

* 这份结构体可以当作“工作近似模型”；
* 不一定每个字节边界都已经完全精准；
* 但它至少很有力地说明：

o 这块 0x1D8 全局对象确实就是迷宫核心状态。

### 2. 移动输入并不是单个方向值，而是 12 字节三元组

这是我觉得公开 writeup 对我帮助最大的一个点。

当时我本地已经知道：

· 0x80012004 是移动 IOCTL；

· 它的输入大小是 12 字节；

· 但我还没有彻底把这 12 字节的意义闭环。

公开文章给出的补全思路是：

```
struct input {    int x;    int y;    int z;};
```

并满足校验关系：

x ^ y ^ 0xDEAD1337 == z

对应截图如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2ic9hgLEuBSiacGQlmib5QKJte36hHfAf0FHZP6nkyJ0DZJ0c1sLZxc0m8TZNp8dj7mXFthjxVqjffMp6j5WW1viaL2xISJVe4S8M/640?wx_fmt=other&from=appmsg)![]()

这就把“为什么输入是 12 字节”这件事解释清楚了：

· 驱动不是只吃一个方向枚举；

· 它还要校验这组输入是否满足特定关系。

### 3. 方向值其实分成两层：控制台逻辑值和真正送进驱动的编码值

这也是我后面觉得特别值得记下来的地方。

我自己当时已经能从控制台逻辑里恢复出：

· 0x10 / 0x20 / 0x30 / 0x40

但公开 writeup 通过调试 DeviceIoControl 输入缓冲区，又给出了一组“真正送入驱动”的值：

· UP -> 0x52

· DOWN -> 0xD3

· LEFT -> 0x53

· RIGHT -> 0xD0

对应截图如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0rgzlWQjC6l1HMFcNIiaiblEXFqibpiajVINGwoetiasMoSj6gHHRBLWWIFKQOKc9sQQqn4JIktyYqZgmSbDlfrRYSVMrlRRickmicCc/640?wx_fmt=other&from=appmsg)![]()

这个结论非常自然地解释了一个问题：

· 为什么只看控制台代码，和只看输入缓冲区，会得到两套不同的方向编码。

更合理的理解是：

1. 控制台内部先把按键映射成逻辑方向值；

2. 然后再经过一层变换，生成真正写入输入缓冲区的 x / y / z。

也就是说，两边都没错，只是观察的层次不同。

### 4. 从这套协议出发，就可以直接做地图探索和最短路求解

公开 writeup 在完成协议恢复后，后面的思路其实就很顺了：

1. 先通过 query 拿到迷宫边界、入口和出口；

2. 再通过 reset 保持每次实验从同一起点开始；

3. 用 move 驱动一步步探索；

4. 通过事件、信号量或其他泄露通道判断每一步是“前进成功”还是“撞墙”；

5. 把整张迷宫图恢复出来后，再跑最短路算法。

从方法论上说，这一步并没有什么魔法，核心前提只有一个：

· 你必须能稳定判定“这一脚有没有走通”。

一旦这个前提成立：

· 地图恢复就是标准图搜索问题；

· 最短路径就是标准 BFS / 最短路问题。

### 5. 输出缓冲区本身也可能参与了终点判定和最终凭证恢复

公开文章还补充了一点：

· 移动返回缓冲区长度是 0x84

· 用户态程序会检查：

o output[0x3C:0x40] == "WIN!"

o 偏移 0x80 处的 DWORD

o 0x40 之后的数据区

这说明一个关键事实：

· 驱动并不是只有“事件 / 信号量”这种旁路反馈；

· 主返回缓冲区里也可能在终点附近携带额外状态，甚至和最终凭证恢复直接相关。

也就是说，这题最后阶段很可能不是单纯“走到终点就结束”，而是：

· 先到达终点；

· 再从输出缓冲区里拿到额外信息；

· 再进入最后的解密 / Flag 恢复逻辑。

**0****3**

**回头看，这题真正卡我的地方在哪里**

如果现在复盘，我觉得我当时没做出来，不是因为“不会最短路”，而是因为这几个关键环节没有完全闭合：

### 1. 我没有彻底吃透输入构包

我知道有方向； 我知道有 12 字节输入； 但我当时没有把“控制台逻辑值 -> 真正输入缓冲区三元组”这一层完整抠清楚。

而这一层一旦没闭环，后面自己写工具直连驱动就会不稳。

### 2. 我知道有侧信道，但没有把所有侧信道调度关系画清楚

我当时已经明确意识到题目里不止一条反馈面：

· 事件

· 信号量

· 时序

· DeviceIoControl 返回值

· 输出缓冲区

· 用户态内存副作用

但我还没有把它们之间的关系画到足够细：

· 哪些是主反馈；

· 哪些是冗余反馈；

· 哪些只在特殊状态出现。

### 3. 我已经有了实验工具，但还没有把它推进到“自动探索收敛”

我已经搭好了工具框架，这一点其实很重要。

说明我不是完全停在静态分析，而是已经具备继续推进的工程基础。

但当时的问题在于：

· 工具已经能发命令、能采样；

· 可还没有把“观测结果 -> 稳定状态判断 -> 地图恢复”整个流程打成一个闭环。

**0****4**

**现在如果再做这题，我会怎么推进**

如果按现在的理解重新做一次，我会严格按下面这个顺序来：

1. 彻底确认移动输入三元组的构造逻辑；

2. 对每种侧信道分别做最小实验，判断其稳定性；

3. 选出一条最稳定的“移动结果判定通道”作为主通道；

4. 在这个基础上自动恢复整张迷宫图；

5. 用 BFS 求出最短路；

6. 在终点附近重点分析 0x84 输出缓冲区和最终凭证恢复逻辑。

如果这样推进，整道题就会从“混合了很多要素的难题”变成一个清晰的流水线：

· 协议恢复

· 结果判定

· 地图探索

· 最短路

· 终点凭证恢复

**0****5**

**结语**

ShadowGate 这题让我印象最深的地方，是它并不是一道纯粹的“驱动题”，也不是一道单纯的“迷宫题”。

它真正的核心在于：

· 驱动如何和用户态说话；

· 又如何在“明面通信”之外，通过事件、信号量、时序和缓冲区这些方式偷偷把结果传回来。

从这个角度说，迷宫只是壳，真正值得啃的是那套隐藏反馈机制。

对我来说，这次复盘最有价值的地方，也不是“我已经完全通关”，而是我终于能比较清楚地说明：

· 我到底已经做到了哪一步；

· 我当时卡在哪；

· 以及借助公开 writeup，我能把缺失的那几步补到什么程度。

如果以后我再继续把终点逻辑和最终 Flag 也彻底跑通，这篇文章大概还能再补一个“完整版后记”。

**06**

**参考**

## 本地样本：

* ShadowGateSys.sys
* ShadowGateSys.sys.i64
* ShadowGateApp.exe

公开参考文章：

* https://www.52pojie.cn/thread-2102723-1-1.html

说明：

* 本文前半部分以我自己的实际分析为主；
* 后半部分关于输入构包、真实方向编码、地图恢复思路和终点阶段的内容，参考了公开 writeup 后补完；
* 这些补充内容我已经按自己的理解重新组织，但并不把它们伪装成我当时已经独立做出的完整结果。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0Lrzak7QXB3ZdVn1teB5adRWm9ToOYwcCibSlGBCpKPCa0ok8X6OQFV4JvU5icCeeRznj1k1qRlr8sbFDWARvLEgKb4W2k5IMls/640?wx_fmt=jpeg&from=appmsg)

看雪ID：刘宝

https://bbs.kanxue.com/user-home-994967.htm

\*本文为看雪论坛优秀文章，由 刘宝 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0NTcVRFDyUWtET22ia094tpMTFWhg50P4ia0ibnVdJapbQXZM7TRta653sX48YW54A2SZem2fdXp5ZRJbFg0CuuJ6hKklEM2WhtU/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458611117&idx=1&sn=f063788f8971edf449fd09571d515ba7&scene=21#wechat_redirect)

第十届安全开发者峰会【议题征集】-欢迎投稿

# 往期推荐

[安卓逆向基础知识之frida Hook](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612348&id...