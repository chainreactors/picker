---
title: 深入MD5：逆向工程师如何识别和还原标准与魔改算法
url: https://mp.weixin.qq.com/s/GP-apKySR-ciZ6fmNTVKjA
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:53:46.797986
---

# 深入MD5：逆向工程师如何识别和还原标准与魔改算法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fJBlDTU8pLGaQQJ5K8lIp34XHRzcaQYAvwworABeDrtnyDdBfqlPFReT3HUX8ZrnlcPx7lwRBWN8gms8VAWMb6bZ6uTzn31qnsCWyHC7XibI/0?wx_fmt=jpeg)

# 深入MD5：逆向工程师如何识别和还原标准与魔改算法

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

推荐文章

以下文章来源于泡泡以安
，作者泡泡以安

![](http://wx.qlogo.cn/mmhead/yYI4pIsF7XGF3kCvrfFU6YnUxQy1x9TyAF1vWHO9LUbp5N0d30MhTyhKCrRb5aRGxeJ9It2Lzac/0)

**泡泡以安**
.

聚焦爬虫、安全、逆向、人工智能。技术致知，实战致用。

> 本文从安卓逆向工程师的视角出发，全面剖析 MD5 算法的原理、实现步骤、代码实现（Java/C/ARM 汇编）、在安卓中的应用场景，以及在逆向分析中如何识别标准与魔改的 MD5 算法并进行还原。

---

## 目录

1. MD5 算法概述
2. MD5 算法原理详解
3. MD5 的代码实现
4. MD5 在安卓中的应用场景
5. 安卓逆向中识别 MD5 算法
6. 标准 MD5 的还原
7. 魔改 MD5 的识别与还原
8. 实战案例分析
9. 工具与资源
10. 总结

---

## 1. MD5 算法概述

### 1.1 什么是 MD5

MD5（Message-Digest Algorithm 5，消息摘要算法第五版）是由 Ronald Linn Rivest 于 1991 年设计并公开的一种密码散列函数（RFC 1321），用以取代此前的 MD4 算法。它能够将**任意长度**的输入数据映射为固定 **128 位（16 字节）** 的哈希值，通常以 **32 个十六进制字符**表示。

MD5 的核心价值在于为数据生成一枚唯一的「指纹」。例如在文件传输场景中，接收方可以计算收到文件的 MD5 值，与发送方提供的原始 MD5 进行比对——若两者一致，即可认为文件在传输过程中未被篡改。

### 1.2 基本特征

| 特征 | 说明 |
| --- | --- |
| 输出长度 | 128 bit（32 hex chars） |
| 分组长度 | 512 bit（64 bytes） |
| 轮数 | 4 轮，每轮 16 步，共 64 步 |
| 设计者 | Ronald Linn Rivest |
| 发布年份 | 1991（RFC 1321） |
| 安全性 | 已被证明存在碰撞攻击，不建议用于安全场景 |

### 1.3 MD5 在哈希家族中的位置 ![](https://mmbiz.qpic.cn/mmbiz_png/fJBlDTU8pLGRgvKK6WZ3FibuW1WJtfDYMjViap3T3iaiaWicztSMRv4qKSibPA5XribW1Yed4m9icjj6ufNZ0wdehyb8j3voMTaJaV8JGrMrHZlxBgw/640?wx_fmt=png&from=appmsg) 哈希算法家族演进

MD5 属于 MD 家族（Message-Digest）的第五代算法。上图展示了从 MD2 到 SHA-3 的演进路径。需要注意的几个关键时间节点：

* **2004 年**：王小云教授团队发表了针对 MD5 的碰撞攻击论文，证明可以在合理时间内找到两个不同的输入产生相同的 MD5 值
* **2017 年**：Google 公布了首个 SHA-1 碰撞实例（SHAttered），标志着 SHA-1 也不再安全
* **目前主流**：SHA-256（SHA-2 家族）和 SHA-3（Keccak）是当前推荐使用的哈希算法

尽管 MD5 在密码学意义上已不安全，但在安卓应用中仍被大量使用——特别是在签名校验、数据完整性检查、接口参数签名等场景中。这使得 MD5 成为安卓逆向工程师**必须深入理解**的算法之一。

> **逆向工程师须知**：碰撞攻击意味着攻击者能伪造出与原文件 MD5 值相同的恶意文件。因此在实际项目中若发现应用使用 MD5 作为安全签名机制，应建议开发者升级至 SHA-256 或 HMAC-SHA256。

---

## 2. MD5 算法原理详解

### 2.1 算法总体流程

MD5 算法的处理流程可以分为五个阶段：

![](https://mmbiz.qpic.cn/mmbiz_png/fJBlDTU8pLHIC8MGb1BDGuUiaFvcMU4iafsxq87ribUWlwrqghJDsIrCW7sIHXoOE4mTttdDnkHibWgDGXDbGVM19ibjxO7ujicamNrwM8t4kAwvU/640?wx_fmt=png&from=appmsg)

MD5 算法总体流程

整个过程遵循经典的 **Merkle-Damgård 结构**：先对消息进行填充和分组，然后通过迭代压缩函数逐块处理，最终输出固定长度的摘要。这一结构也是后续识别 MD5（包括魔改版本）的核心依据——即使参数被修改，「分组→迭代压缩→累加输出」的骨架通常不会改变。

### 2.2 步骤一：消息填充（Padding）

MD5 是按分块进行处理的，分块长度为 `512 bit`。大多数情况下，数据的长度不会恰好是 512 的整数倍，因此需要进行填充。

**填充规则**：

1. 在消息末尾先添加一个 `1` 比特（即字节 `0x80`）
2. 然后添加若干个 `0` 比特，直到消息长度 ≡ 448 (mod 512)
3. **即使原始消息长度已满足 L % 512 = 448**，也必须继续填充 `100...0`，此时会跨越到下一个 512 位区块来完成填充过程
4. 填充长度范围：最少 1 比特，最多 512 比特

```
原始消息:  [M0, M1, M2, ..., Mn]
填充后:    [M0, M1, ..., Mn, 1, 0, 0, ...., 0]
                            ↑              ↑
                          必须有1        填充至 ≡448(mod512)
```

### 2.3 步骤二：附加长度

在填充后的消息末尾追加一个 **64 位（8 字节）** 的值，表示原始消息的**位长度**（小端序）。这样最终消息的总长度恰好是 512 的整数倍。

```
填充后消息 (≡448 mod 512 bits) + 64位原始长度 = N × 512 bits
```

![](https://mmbiz.qpic.cn/mmbiz_png/fJBlDTU8pLEZdYQjdxTb5qLicylbVnK89RC1JEThfic8nm4p7EfibFAKibOibnEib352ZbmOM30MNzIHzpfLzKibKDpBXrSyxaL0j1LfVAHBHKyHvU/640?wx_fmt=png&from=appmsg)

MD5 数据填充与分组结构

这也意味着 MD5 算法最多可以处理位长度小于等于 `2^64 bit` 的数据。

> **逆向关键点**：**小端序（Little-Endian）** 是识别 MD5 的一个关键特征。MD5 全程采用小端序存储，而 SHA 系列算法采用大端序（Big-Endian）。在分析二进制代码时，如果发现哈希相关的数据以小端序组织，且输出 128 位，极大概率为 MD5。

数据填充后的结构示意：

![](https://mmbiz.qpic.cn/mmbiz_png/fJBlDTU8pLEPNXWAfvTTfiabxlVhdDibghtNsRk4JXmopibLbialtOtQpv3qicia1HaCsRFqtKzGWsITXNpZFkGLMG7OgQH05NQKtzwLPzYJfBCVE/640?wx_fmt=png&from=appmsg)

数据填充结构

### 2.4 步骤三：初始化链变量（IV / 缓冲区）

MD5 使用四个 32 位寄存器作为初始链变量（也称为初始化向量 IV），用于后续的分组计算。每个数据占 32 bit，由 8 个十六进制数字组合构成：

```
A: 01 23 45 67 （16进制，小端序表示）
B: 89 AB CD EF
C: FE DC BA 98
D: 76 54 32 10
```

由于计算机中字节存储顺序为**小端序**（低字节在前），当从右向左获取字节数据时，实际在程序中初始化为：

```
// 小端序转换后的实际赋值
A = 0x67452301
B = 0xEFCDAB89
C = 0x98BADCFE
D = 0x10325476
```

以 A 为例说明小端序转换过程：

```
A 的字节表示: 01 23 45 67
A 的二进制:   00000001 00100011 01000101 01100111

// 小端序: 低字节在前, 从右向左读取字节
// 即 67 45 23 01 -> 0x67452301
```

> **逆向关键点**：这四个魔数 `0x67452301`、`0xEFCDAB89`、`0x98BADCFE`、`0x10325476` 是识别标准 MD5 **最直接的特征**。在二进制文件中搜索这些常量是定位 MD5 实现的第一步。由于小端序存储，在内存中实际看到的字节序为：
>
> ```
> A: 01 23 45 67
> B: 89 AB CD EF
> C: FE DC BA 98
> D: 76 54 32 10
> ```

### 2.5 步骤四：分组压缩（核心）

这是 MD5 算法**最核心**的部分。输入消息被分成 512 bit 的块，每个块被分成 16 个 32 位的子块（M0, M1, ..., M15）。算法内部的 4 个 32 位寄存器 A、B、C、D 存储当前的哈希状态，经过多轮迭代处理后更新。

MD5 核心压缩结构示意图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fJBlDTU8pLH1oUuuXtHhVNNmvy8uPqs6SKzbZQWRFoJLxBshAliapsDJLLx62DwAXKWpV0ib9Al4QRqxIM3mK2iaHn1Ac4c5SP0yTgselNlebM/640?wx_fmt=png&from=appmsg)

MD5 核心结构

#### 2.5.1 四个非线性函数

MD5 定义了四个非线性布尔函数，分别用于四轮运算。每个函数接收三个 32 位输入，输出一个 32 位结果：

```
// 第1轮: F - 选择函数
// 逻辑: 若 B=1 则取 C 对应位, 否则取 D 对应位
F(B, C, D) = (B & C) | (~B & D)

// 第2轮: G - 选择函数变体
// 逻辑: 若 D=1 则取 B 对应位, 否则取 C 对应位
G(B, C, D) = (B & D) | (C & ~D)

// 第3轮: H - 奇偶函数
// 逻辑: 三个输入的逐位异或, 产生最大的扩散效果
H(B, C, D) = B ^ C ^ D

// 第4轮: I - 逆选择函数
// 逻辑: 比较复杂的非线性组合
I(B, C, D) = C ^ (B | ~D)
```

各函数在逆向分析中的识别特征：

| 函数 | 名称 | 逻辑特点 | 逆向识别特征（汇编指令组合） |
| --- | --- | --- | --- |
| F | 选择函数 | 若 B=1 取 C 否则取 D | `AND` , `NOT`(`BIC`), `OR` 组合 |
| G | 选择函数变体 | 若 D=1 取 B 否则取 C | 与 F 类似但操作数位置不同 |
| H | 奇偶函数 | 三输入异或 | 连续两个 `EOR`(XOR) 指令 |
| I | 逆选择 | 复杂非线性 | `NOT` (`MVN`), `OR`, `EOR` 组合 |

#### 2.5.2 单步运算详解

每一步运算的公式可以表达为：

```
temp = A + func(B, C, D) + M[k] + T[i]
A = D
D = C
C = B
B = B + ROTL(temp, s)
```

其中：

* `func` 是当前轮对应的非线性函数（F/G/H/I）
* `M[k]` 是当前消息分组中的第 k 个 32 位子块
* `T[i]` 是预计算的常量（来源于正弦函数）
* `s` 是循环左移的位数
* 所有加法运算均为 **模 2^32 加法**（即结果超过 32 位时截断高位）

![](https://mmbiz.qpic.cn/mmbiz_png/fJBlDTU8pLHeic11RXxHyokWwvib8keRATI8VLiblWMXvAbzMhflHvzsA32xD3icksYiaJ6R77quW4waIPBqYORxiaWjKH7XWhJ5pz6LofzPEP3FI/640?wx_fmt=png&from=appmsg)

MD5 单步运算

整体可描述为 FF、GG、HH、II 这 4 个运算公式：

```
// <<< 为循环左移
FF(a, b, c, d, Mj, s, ki) 操作为 a = b + ((a + F(b,c,d) + Mj + ki) <<< s)
GG(a, b, c, d, Mj, s, ki) 操作为 a = b + ((a + G(b,c,d) + Mj + ki) <<< s)
HH(a, b, c, d, Mj, s, ki) 操作为 a = b + ((a + H(b,c,d) + Mj + ki) <<< s)
II(a, b, c, d, Mj, s, ki) 操作为 a = b + ((a + I(b,c,d) + Mj + ki) <<< s)
```

#### 2.5.3 T 常量表（正弦表）

T 常量表包含 64 个 32 位整数，由以下公式生成：

```
T[i] = floor(2^32 × |sin(i)|)，其中 i 从 1 到 64
```

完整的 T 常量表值如下：

```
T[1]  = 0xD76AA478    T[2]  = 0xE8C7B756    T[3]  = 0x242070DB    T[4]  = 0xC1BDCEEE
T[5]  = 0xF57C0FAF    T[6]  = 0x4787C62A    T[7]  = 0xA8304613    T[8]  = 0xFD469501
T[9]  = 0x698098D8    T[10] = 0x8B44F7AF    T[11] = 0xFFFF5BB1    T[12] = 0x895CD7BE
T[13] = 0x6B901122    T[14] = 0xFD987193    T[15] = 0xA679438E    T[16] = 0x49B40821
T[17] = 0xF61E2562    T[18] = 0xC040B340    T[19] = 0x265E5A51    T[20] = 0xE9B6C7AA
T[21] = 0xD62F105D    T[22] = 0x02441453    T[23] = 0xD8A1E681    T[24] = 0xE7D3FBC8
T[25] = 0x21E1CDE6    T[26] = 0xC33707D6    T[27] = 0xF4D50D87    T[28] = 0x455A14ED
T[29] = 0xA9E3E905    T[30] = 0xFCEFA3F8    T[31] = 0x676F02D9    T[32] = 0x8D2A4C8A
T[33] = 0xFFFA3942    T[34] = 0x8771F681    T[35] = 0x6D9D6122    T[36] = 0xFDE5380C
T[37] = 0xA4BEEA44    T[38] = 0x4BDECFA9    T[39] = 0xF6BB4B60    T[40] = 0xBEBFBC70
T[41] = 0x289B7EC6    T[42] = 0xEAA127FA    T[43] = 0xD4EF3085    T[44] = 0x04881D05
T[45] = 0xD9D4D039    T[46] = 0xE6DB99E5    T[47] = 0x1FA27CF8    T[48] = 0xC4AC5665
T[49] = 0xF4292244    T[50] = 0x432AFF97    T[51] = 0xAB9423A7    T[52] = 0xFC93A039
T[53] = 0x655B59C3    T[54] = 0x8F0CCC92    T[55] = 0xFFEFF47D    T[56] = 0x85845DD1
T[57] = 0x6FA87E4F    T[58] = 0xFE2CE6E0    T[59] = 0xA3014314    T[60] = 0x4E0811A1
T[61] = 0xF7537E82    T[62] = 0xBD3AF235    T[63] = 0x2AD7D2BB    T[64] = 0xEB86D391
```

> **逆向关键点**：这些 T 常量值是在二进制中搜索和识别 MD5 的**核心特征**。搜索 `0xD76AA478` 或 `0xE8C7B756` 等值，几乎可以 100% 确认存在 MD5 实现。即使 IV 被魔改，T 表通常保持不变，因此 T 表是比 IV 更可靠的识别依据。

#### 2.5.4 消息子块选取顺序与移位量

四轮中消息子块的选取索引 k 和移位量 s 如下：

**第 1 轮（F 函数）** — 消息块顺序取用，移位量 s = 7, 12, 17, 22 循环：

| 步骤 | k（消息块索引） | s（移位量） |
| --- | --- | --- |
| 0-3 | 0, 1, 2, 3 | 7, 12, 17, 22 |
| 4-7 | 4, 5, 6, 7 | 7, 12, 17, 22 |
| 8-11 | 8, 9, 10, 11 | 7, 12, 17, 22 |
| 12-15 | 12, 13, 14, 15 | 7, 12, 17, 22 |

**第 2 轮（G 函数）** — k = (1 + 5i) mod 16...