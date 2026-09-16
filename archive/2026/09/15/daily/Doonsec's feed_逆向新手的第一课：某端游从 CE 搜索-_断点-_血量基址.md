---
title: 逆向新手的第一课：某端游从 CE 搜索->断点->血量基址
url: https://mp.weixin.qq.com/s/80L2T7CO1TV38ltQccD_7A
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:02:11.065275
---

# 逆向新手的第一课：某端游从 CE 搜索->断点->血量基址

# 逆向新手的第一课：某端游从 CE 搜索->断点->血量基址

切尔曼提察
切尔曼提察

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

文章作者：切尔曼提察

文章来源：https://xz.aliyun.com/news/92788

01

0x1 逆向新手的第一课：某端游从 CE 搜索->断点->血量基址

# 基础数据逆向（一）：从 CE 搜索到血量基址

面向逆向新手的第一篇实战。目标：从一个游戏数据（人物血量）出发，用 CE 锁定它的内存地址，再用 x32dbg 沿汇编逐层回溯，最终得到「基址 + 偏移」的指针公式。

* 目标程序：《笑傲江湖》32 位客户端（xajh.exe）
* 目标数据：人物血量
* 使用工具：Cheat Engine（CE）、x32dbg（32 位程序用 x32dbg；x64dbg 是其 64 位版本，操作基本一致）

## 本文流程速览

1. **CE 搜索** → 锁定血量所在的内存地址
2. **下内存访问断点** → 找到“读取血量”的汇编指令
3. **逐层向上回溯寄存器来源** → 直到收敛到游戏基址
4. **汇总指针公式**

## 1. 工具与整体思路

### 1.1 两类工具，各司其职

* **Cheat Engine（CE）**：负责**搜数值**——把“血量”这个数值定位到某个具体的内存地址。
* **x32dbg**：负责**看代码**——拿到地址后，用它来观察哪条指令在读/写这块内存，并逐层向上找基址。

  ![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUVRaVCXfRUnyyz7Rqc7mRXrm9Te2s9pexia3cA8ZYmJR3wqsUGStoxzd61ESp9HQt15LrzwLdsSZfP8qXiaItlic6PTwog3xBeIs/640?wx_fmt=png&from=appmsg)

CE 与调试器的各种具体操作（附加、搜索、单步、下断），在练习中不断熟悉即可，遇到不会的功能随时查。

### 1.2 整体思路：记住这条主线

**数据地址 → 访问断点找到读写指令 → 看“对象地址”从哪来 → 一路向上 → 回到模块基址**

这是所有“找基址”类逆向的通用套路。下面整篇文章都在反复执行这一条主线。

### 1.3 会用到的调试器操作速查

| **操作** | **作用** |
| --- | --- |
| 附加进程 | 让调试器接管目标进程 |
| Ctrl+G | 数据 / 代码窗口跳转到指定地址 |
| 内存访问断点 | 目标内存被读 / 写时中断 |
| Ctrl+F9 | 执行到返回（配合 F8 单步，可快速“回到上一层”） |
| F8 | 单步执行 |
| 条件断点 | 满足指定条件才中断（本文用它“识破”假来源） |

## 2. 用 CE 锁定血量地址

### 2.1 附加进程

先在游戏里确认当前血量：43348

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV8Tfwe7lniaHZFibW916zja01IfRczVXapKialzd2w1aFys8jwsNfiaHsM7YsiaGxKuATyTAQGvk4NibYqhPej7ygdJnzH52B7ttSVo/640?wx_fmt=png&from=appmsg)

打开 CE，附加到目标进程（xajh.exe）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWVyfNnq3ffeWKYoccuiccxE7NInTp88N9X7TUEpQmlVWznaeEQxxNTBoKEVUjf7dkHC4jpmTqSXWyeVpLD0sQqIAwyhhKjOgtk/640?wx_fmt=png&from=appmsg)

进程列表里可能不止一个候选，选中你游戏对应的那个进程即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXCV5xBMQR8Ip1RqWFWAu5W0LA46Iht1VOAMtjJrcrnfS4eicmGB4IcjJXnUyhJg5CDZzwYlxWhB9eppfVQyD3BsILdEbneHiaibc/640?wx_fmt=png&from=appmsg)

### 2.2 首轮扫描与二次筛选

以当前血量作为初值进行一次扫描，结果往往很多，这很正常。关键在于**改变数值后二次筛选**：

使用血量道具，让血量从 43348 变成 44278。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUnvGQjxGNlGEWzPpsTJibVyXRia3wo75XYdwzf9gbNWw6hUOO60RFCoaAqfwqPY4IfNlANSw7gJGzBkm8tDJThOcT72Tbn7yOL8/640?wx_fmt=png&from=appmsg)

回到 CE，在已有结果上对“改变后的数值（44278）”再次扫描，此时就只剩两条结果了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUkIoibcF1XicxLmMuzbib125sO8dWia6wLsaWJ8oZVIuiauHKuXRU2RGoSCZQOvzaMfOhc1rxrff9lBoSCubWElu07Txib2iaFxsEqQQ/640?wx_fmt=png&from=appmsg)

提示：真实项目里通常要经过好几轮“改值 → 再扫”才能把结果筛干净，一轮扫不干净很正常，多点耐心。

### 2.3 如何辨认干扰数据

筛选中如果看到**以 00 开头**的数据，或者**长得几乎一模一样的一大批**地址，大概率不是我们要找的目标：

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWsjmj518YK7l6opLicTRBmGiabibbATa14zTN9xOGib6dUpwgdDrP4unsLjlXauTwHCtGocV1AnSmyJ4XuZ0cbj0DSliaJAtTt23GY/640?wx_fmt=png&from=appmsg)

### 2.4 把候选地址加入列表

本例运气不错，只剩两条。把结果双击加入下方的地址列表，两条都可以试——这里我们用 45B1A58C 这条继续演示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUtKCRA4qQTcNfWIgxCHkIHWakXsjR5JQoSibC563b0Bq7pcElfXRO2icXdqAXtIEab1YibDicFNwdFTlwT3AW13FVFKOa2X3IEAq8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV0VuF2QOgLJMEGiboqUZWdmf15oouCG54goLj2Lk6OMap8TErjn5JQqrMZNUouXNTuoOwN8ibOcktTQHOl3ceyuHbHGiaIpA3uSU/640?wx_fmt=png&from=appmsg)

### 1.5 切到调试器，确认数值

CE 负责“找到它”，接下来交给调试器来“看代码”。把进程交给 x32dbg（附加，或以调试方式打开游戏）。在数据窗口用 Ctrl+G 跳转到 0x45B1A58C：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXur9Hviav9VfJ2qm66q4gibQDI554p1EJkx7vcoFGx6LU3HQTD7Xpttm20J4RpgqYlWjKdvCrdyJknpypZYKWHR9ZNb68OsIxqI/640?wx_fmt=png&from=appmsg)

直接看时显示的数值可能不对，把该位置的显示类型切换为**无符号整型（Unsigned）**，就能正确读出当前血量：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXS3icW4uPhdJrdIkmcTMEiawicHSDOV4Pw0bheaDdeiaic6ds6PBYaOktv0V5kFAibhDiaXDpCqc2yj5v6Rlpt431lPZnickHx4Jia9bzQ/640?wx_fmt=png&from=appmsg)

## 3. 内存访问断点：找到“读血量”的代码

### 3.1 下断点

确认 0x45B1A58C 上保存的正是血量后，对它下一个**内存访问断点（长度 4 字节）**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV3aOE0nWeSfN7ayvSsiaMicqAsIrYVPk4gOKQ2NicHKjnFgAGqDHCnrsthvDzLoAAfel03rnZzickPicFZxzXa5X3G4lMjNa5rwN7U/640?wx_fmt=png&from=appmsg)

断点就绪后，让游戏去读这块内存——例如再扣/加一次血、刷新血条——访问发生时立刻断下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXuVlO800l6Jk3HjBib131deXvvLjBaT2hliaibzel1A2pFpnNLwJ4c5UKHDwp8nUHibQWzPnYnhlCXQhibcpPb5VndjdL9WkIv7LRc/640?wx_fmt=png&from=appmsg)

### 3.2 命中的指令

断下后停住的这条指令，就是“正在读取血量”的地方：

```
mov edi, dword ptr ds:[esi+0x1C]        ; esi = 0x45B1A570
```

也就是说：**血量 = esi + 0x1C** 0x45B1A570 是血量所在的对象，血量字段偏移是 +0x1C——这是我们要记录的第一层。

### 3.3 记录完先收尾，再继续

记完这层信息后，**立刻取消刚才的断点再继续运行**，否则之后随便操作都会再次断下：

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWdJIbv6ibTsj4F4F8hsZmfHKnFpwOknBLRBbR8nkkwyJ4QHibKzbc3iaWmtSE8XSPiaeBAT84DVbuShyGevopiaN1hq5oI00IWIypQ/640?wx_fmt=png&from=appmsg)

如果取消断点后游戏仍卡住不动，在上方**线程窗口**里右键“恢复所有线程”，再点运行即可。

## 4. 逐层回溯：把对象地址一路追到基址

### 4.1 回溯心法

现在的问题是：血量对象 `0x45B1A570` 是从哪来的？反复执行下面四步，直到追到模块基址：

1. 在当前函数里向上找“谁给持有该值的寄存器（esi/ecx 等）赋了值”；
2. 如果来源不在当前函数（例如往上遇到 `int 3`、或找不到赋值），就在函数头部下断，用 `Ctrl+F9` + `F8`**返回到上一层**继续找；
3. **每一步先确认寄存器里的数据正确**，再继续向上（怎么确认见 3.2）；
4. 一直追到 EBX/ECX 等寄存器的注释显示它来自 `xajh.exe` 模块基址为止。

### 4.2 第一跳：从“血量对象”到它的来源

在命中指令所在的函数里向上找“给 esi 赋值”的位置：

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXjWS8HImbZ90nibZYKibiasCJOYic5t9tkKibGyzAhSgm5YsCITvHJic8ryzM1pv4Hxdiaq0ACjsjEKlmAv7Bx692y2tH5KNa7E4Qict8/640?wx_fmt=png&from=appmsg)

发现 esi 来自 ecx：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUvwpKT4f4TdXN9PO5j9Uia5Ajn0wSQJbdianbGVQNBiaQc4h3l9kricJAV1PGDZT8oTiaYWazDicPdl1SWY4PxGfRY1vVkFYZlxF4vI/640?wx_fmt=png&from=appmsg)

**关键技巧——如何确认自己找对了？**新手最常担心的是“我追的这个对象到底对不对”。方法很简单：在怀疑的位置下个断点，断下后把**调试器里寄存器/内存显示的值**和**游戏里的真实数据**对比。一致就继续，不一致就说明方向错了。

本例寄存器位置对应的数据确实正确。但继续往上翻，发现再往上是 int 3（没有有效代码），那就需要返回到上一层去找。做法：在**当前函数头部下断点**，用 Ctrl+F9 执行到返回，再 F8 单步，回到上一层函数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QU8jQbgc2AQgl8FdRKusTTWwsia4qAnqXr3ibg1CRxhah1DibF1XKQlWg9PXfTpyayjQ2n0fTO9v2n8Sib4Bu2nIaQMrOL5lFTkiccI/640?wx_fmt=png&from=appmsg)

返回上一层后，找到了真正给这个对象赋值的那一行：

```
lea ecx, dword ptr ds:[esi+0x2A0]        ; esi = 0x45B1A2D0 → ecx = 0x45B1A570
```

也就是说：**血量对象（0x45B1A570） = 上层对象（0x45B1A2D0） + 0x2A0**。偏移 +0x2A0 记下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVgnahnAKoXibvmgnm9GJYdIS0TZoIXUaGboKrTcftCS7iah60a4bY9aIwkoxf0FeeScNDWxicjlBLpsCFNbR20ptt7yzD4URKAs4/640?wx_fmt=png&from=appmsg)

继续向上寻找 0x45B1A2D0 的来源。又是老一套：esi 来自上一层的 ecx → 头部下断返回上一层 → 返回后发现 ecx 又来自 esi → esi 又来自 ecx，再次返回上一层去追：

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUx1jm4CM87ialFNzSe8USiaMVAjibZJ3PKHGBdIpImBJhwLyTKPYsqrbeqicOviaPpZHibyN6Z2szUMvAuoo160uOE3NibnQdpoc1Gic8/640?wx_fmt=png&from=appmsg)

### 4.3 一大段循环：小心“看起来的来源”

返回上一层后，看到上面有一大串循环。**这里是新手最容易犯错的地方。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWMsiasicxsBOvcxcqwXymtLv75E9sdAAmpSYjbqZfQ9MZRI7kXBtx4QFYaRxALliadHuicvgvtdTEiaRQ6kDR4T8FExoxd0IgffYrY/640?wx_fmt=png&from=appmsg)

很多人抬头看到不远处的一句：

```
mov ecx, dword ptr ss:[esp+28]
```

便理所当然地认为 ecx 来自 [esp+28]，顺着去追——但其实是错的。

**识破方法：条件断点。**在怀疑的位置下条件断点，让它在“你判断的某个值”时才断下。本例中断点确实停下来了，但停下来的数据跟你的断点条件完全对不上——说明它根本不在这条路径上。至于“为什么值不满足却还是断了”，涉及 x32dbg 断点触发原理，这里先不展开。

实际上 ecx 并不来自这部分，而是来自更上面的分支。利用反汇编窗口的**跳转提示（从哪条跳转过来的）**，跳到真正的来源处：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVmTHwu9JDbv5DdfFSVjbMxfEjVg1KPW6zcYUWIQRkyzAMo9swW8UNFsVOPt5QZc6BAzsJ96ZVpogzKALkGaicL1tric0cITAIdo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXLeRdSR8aPs8iaZLVASKvORC7kN3E4Y7SkjfCDy6Ab74J66HFweWgPJ3IZDWNuRSkJcAonPzwSUHsYrvY7l9oX4iappm2EfmuG0/640?wx_fmt=png&from=appmsg)

跳过去之后发现：ecx 还是来自 esi，并且此时数据确实正确：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV94xaibVT7uotlaNIj8n4icL2jARfdzZKXSySeQ1x1c9ibEuLBSF1LqAjW5jEib6At6epX0HweRzfJStG2yXXp2lSsyN7Qk1akrn4/640?wx_fmt=png&from=appmsg)

继续...