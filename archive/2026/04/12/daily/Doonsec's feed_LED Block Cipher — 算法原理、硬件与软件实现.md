---
title: LED Block Cipher — 算法原理、硬件与软件实现
url: https://mp.weixin.qq.com/s/ibC5C0up0NNBUwaoXHEoiw
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:55:07.137650
---

# LED Block Cipher — 算法原理、硬件与软件实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CvoBUu8TBhuYVUf2dQaFD7OgtQfdI0usggBsAz2A5HeH6hVmHDibAEDvgqUvEqGFPTN4LmKibI9DFhJPZHAsZyx1DkFXjyERKr8Qfia4S22cQA/0?wx_fmt=jpeg)

# LED Block Cipher — 算法原理、硬件与软件实现

原创

喜吾安璇
喜吾安璇

攻防SRC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# LED Block Cipher — 算法原理、硬件与软件实现

**原著：** Jian Guo, Thomas Peyrin, Axel Poschmann, Matt Robshaw（CHES 2011）
**本项目：** LED-64 / LED-80 / LED-128 的 Verilog HDL 实现与 Python 参考实现，含完整加解密验证。

代码链接：https://github.com/inwpu/LED-Block-Cipher/

## 一、背景与算法参数

随着 RFID 标签、无线传感器和嵌入式控制器的大规模普及，如何在极端受限的硬件资源下提供密码保护成为一个现实工程问题。这类设备的可用门电路往往不足 2000 GE，而传统 AES 的最小实现已需要约 3400 GE，其密钥扩展算法本身就占去相当比例。

LED（Light Encryption Device）的核心设计取舍是：**完全取消密钥扩展算法**，让原始密钥以周期性复用的方式直接参与每一步的密钥异或。这不仅将硬件面积压缩到 966 GE（LED-64），更带来了关键的安全分析优势——由于轮函数结构高度规整，可以在单密钥和相关密钥两种攻击模型下都推导出精确的安全界。

轮函数的设计延续 AES 的 SPN（置换-替换网络）框架，以 PRESENT 密码中经过广泛验证的 S 盒作为非线性层，并采用专为串行硬件实现优化的 **MixColumnsSerial** 结构。

下表列出三个变种的参数对比。"步"（step）是 LED 特有的结构单元，每步包含 4 轮内部变换和 1 次密钥注入，是安全性证明的基本分析单位。密钥注入次数 = 步数 + 1，因为加密开始前有一次初始注入，每步结束后有一次注入。

| 版本 | 块大小 | 密钥长度 | 步数 | 总轮数 | 密钥注入次数 | 运算域 | 硬件面积（可变密钥） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LED-64 | 64 bit | 64 bit | 8 | 32 | 9 |  | 966 GE |
| LED-80 | 64 bit | 80 bit | 12 | 48 | 13 |  | 1,040 GE（估算） |
| LED-128 | 64 bit | 128 bit | 12 | 48 | 13 |  | 1,265 GE |

> 面积数据来自原论文 Table 2（Flexible Keys 列，UMC 0.18 μm 工艺）。LED-80 标注估算值（\*）。LED-64 若使用硬连线密钥可降至 688 GE，LED-128 可降至 700 GE。

**本项目**基于官方规范（ePrint 2012/600）及 Jian Guo 于 2014 年公开的字节级参考实现 `led-bytes.c`，完成了：

* **Verilog HDL**：LED-64、LED-80、LED-128 各提供时序逻辑（每时钟周期完成一轮）和组合逻辑（单周期）两种架构，均支持加解密；
* **Python**：`led.py` 单文件实现三个变种的完整加解密，90 项测试全部通过；
* **交叉验证**：所有实现的输出均与官方 C 参考逐字节比对一致。

## 二、算法结构与轮操作

### 2.1 状态矩阵

LED 将 64 位数据块解释为一个 **4 行 × 4 列的 nibble 矩阵**，每个格子存储一个  元素（4 比特）。与 AES 按列优先填充不同，LED 按**行优先、高位优先**的顺序将明文字节填入，这是面向硬件串行实现的设计选择——串行电路每次只处理一个 nibble，行优先与高位先出的比特流顺序一致。

![图 1　状态矩阵布局（64 位明文 → 4×4 nibble 矩阵）](https://mmbiz.qpic.cn/mmbiz_png/CvoBUu8TBhvc7ibJv7Ks75zbVic15QicUOnlBJd5COMBW6RROzryEBcoNYWLBfdgqN35VMIOfxon7yaibv8tnx2SMQuubqpib5zXnzNicudsbVjuU/640?wx_fmt=png&from=appmsg)

图 1　状态矩阵布局（64 位明文 → 4×4 nibble 矩阵）

格子  对应 64 位字的位域：

例如  取最高 4 位（bits[63:60]）， 取最低 4 位（bits[3:0]）。子密钥  以完全相同的  格式组织，其格位  的值由密钥 nibble 公式  确定（详见第三章）。

### 2.2 加密整体架构

加密过程由  个**步（step）**串联而成，每步开始前先对状态 XOR 一个子密钥，随后执行 4 轮内部变换；所有步结束后再做最后一次密钥注入（收尾 XOR）。图 2 展示了这一"密钥—步—密钥—步—…—密钥"的交替结构。

![图 2　LED 加密整体架构](https://mmbiz.qpic.cn/sz_mmbiz_png/CvoBUu8TBhu9rqtKhyWEQtiabxib8ScqGEdholdIf8MhPPnib51vm3TZ5npeKe7ANqIQxqZVk3mr4Hop2bBwJiatmcn8jeDCiaVWdM1vo1FrsS1k/640?wx_fmt=png&from=appmsg)

图 2　LED 加密整体架构

图中每个  节点表示一次子密钥 XOR（AddRoundKey）。 注入 **step 0 之前**， 注入 **step 0 之后（step 1 之前）**，以此类推； 是最后一次注入（step  之后），也称"output whitening"。没有这次最终 XOR，最后一个 MixColumnsSerial 的输出就直接暴露，攻击者可以跳过最后一轮分析整个结构，因此收尾 XOR 是构造完整性的必要组成。

每步（step）由 4 轮（round）顺序执行，每轮依次完成以下 4 个操作（图 3）：

![图 3　一轮（round）的内部操作顺序（每步重复 4 轮，轮编号 r 递增）](https://mmbiz.qpic.cn/sz_mmbiz_png/CvoBUu8TBhvaia2QSaYM11n6XDic8PPteG4ucUAsRHCKsg9KRWnJIeKde42TQ3SFvWFVeVywUULecsp3DtFeKCn7RB3rXgdibg6SibrEeavabE4/640?wx_fmt=png&from=appmsg)

图 3　一轮（round）的内部操作顺序（每步重复 4 轮，轮编号 r 递增）

四个操作的排列顺序遵循 SPN 设计原则：AddConstants 在 SubCells 之前注入，避免 S 盒输入具有可预测的对称性；SubCells 提供非线性（混淆）；ShiftRows + MixColumnsSerial 共同提供扩散（雪崩）。理论上，经过 4 轮（一步）之后，每个输出 nibble 依赖所有 16 个输入 nibble（全扩散），这是 LED 步结构作为安全分析基本单元的原因。

### 2.3 AddConstants — 轮常数注入

每轮注入的作用有两个：一是在每轮引入轮差异打破状态的对称性，防止出现固定点或滑动攻击；二是将密钥长度信息编码进状态，使 LED-64 / LED-80 / LED-128 三个变种即使面对相同的明文和密钥也产生完全不同的密文（抵御跨变种的通用攻击）。

每轮使用一个 6 位常数 ，由 6 位仿射 LFSR 生成，递推规则为：

即寄存器左移一位，新的最低位由旧 、 和常数 1 异或得到。LFSR 从全零初始化，每轮使用前更新一次，故 。序列前 8 项验证如下：

```
初始：000001 = 0x01
步1：新b0 = 0⊕0⊕1=1 → 000011 = 0x03  ✓
步2：新b0 = 0⊕0⊕1=1 → 000111 = 0x07  ✓
步3：新b0 = 0⊕0⊕1=1 → 001111 = 0x0F  ✓
步4：新b0 = 0⊕0⊕1=1 → 011111 = 0x1F  ✓
步5：新b0 = 0⊕1⊕1=0 → 111110 = 0x3E  ✓
步6：新b0 = 1⊕1⊕1=1 → 111101 = 0x3D  ✓
步7：新b0 = 1⊕1⊕1=1 → 111011 = 0x3B  ✓
```

全部 48 个 RC 值（LED-80 / LED-128 使用全部 48 个，LED-64 使用前 32 个）：

```
RC[0..47] = {
  01 03 07 0F 1F 3E 3D 3B 37 2F 1E 3C 39 33 27 0E
  1D 3A 35 2B 16 2C 18 30 21 02 05 0B 17 2E 1C 38
  31 23 06 0D 1B 36 2D 1A 34 29 12 24 08 11 22 04
}
```

注入只作用于状态矩阵的**第 0 列和第 1 列**，第 2、3 列完全不变。Col 0 注入"行索引与密钥长度编码的组合"固定常数（所有轮相同），Col 1 注入  的高 3 位和低 3 位（每轮不同）：

* **Col 0**：设 `ks_hi = (key_bits >> 4) & 0xF`，`ks_lo = key_bits & 0xF`，则行  注入 （）或 （）。该值在同一 LED 变种内的所有轮中固定不变，在不同变种间取值不同，以此让三个变种产生不同的常数域。
* **Col 1**：`RC_hi = (RC[r] >> 3) & 0x7`（RC 的高 3 位）注入偶数行（行 0、行 2）；`RC_lo = RC[r] & 0x7`（RC 的低 3 位）注入奇数行（行 1、行 3）。每轮  不同，确保每轮的注入图案唯一。

![图 4　AddConstants 注入位置与值（ 表示将该值异或叠加到格子的现有值上）](https://mmbiz.qpic.cn/sz_mmbiz_png/CvoBUu8TBhtEPHaSK70ss75Cuq8IYVQn6vhnbMJBKZTqWMD9foib4bflnrZ9jDdDlUYOrGZ3uXoOfAMibsx8iaKJ5AWic2PPAvSlUx8yEg4Ln4A/640?wx_fmt=png&from=appmsg)

图 4　AddConstants 注入位置与值（ 表示将该值异或叠加到格子的现有值上）

三个变种在 Col 0 注入的固定值如下表。注意  和  对所有变种均为 2 和 3：这是因为 64、80、128 这三个数值的低 4 位（）均为 0，导致 、。

| 格位 (row, col) | LED-64 () | LED-80 () | LED-128 () |
| --- | --- | --- | --- |
| (0, 0) |  |  |  |
| (1, 0) |  |  |  |
| (2, 0) |  |  |  |
| (3, 0) |  |  |  |

### 2.4 SubCells — 非线性替换

SubCells 对状态矩阵中的全部 16 个 nibble **独立并行**地做 S 盒查表替换，是整个轮函数中唯一的非线性操作（混淆层）。LED 复用了 PRESENT 密码的 S 盒，该 S 盒基于  上的仿射变换构造，最大差分概率为 ，最大线性近似概率为 （均为 4 位 S 盒的理论最优值之一）。

正向 S 盒（加密用，）：

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | C | 5 | 6 | B | 9 | 0 | A | D | 3 | E | F | 8 | 4 | 7 | 1 | 2 |

逆向  盒（解密用，查逆映射）：

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 5 | E | F | 8 | C | 1 | 2 | D | B | 4 | 6 | 3 | 0 | 7 | 9 | A |

可以验证 ，例如 ， ✓；， ✓。SubCells 在解密时直接替换为查  盒，操作结构完全对称，硬件实现可共用查表逻辑。

### 2.5 ShiftRows — 行移位

ShiftRows 将第  行向左**循环移动  个 nibble**（），第 0 行不动。该操作本身不增加混淆，其目的是为后续的 MixColumnsSerial 准备跨行的扩散条件：ShiftRows 之后，同一列中来自不同原始行的 nibble 被重新排布，MixColumnsSerial 对列做矩阵乘法时就能将多个行的信息混合，实现全状态的雪崩效应。

![图 5　ShiftRows 变换：每行逐一展示移位前后的 nibble 排列](https://mmbiz.qpic.cn/mmbiz_png/CvoBUu8TBhtwQN8AHVuPpgXWrXydIQNTX0LN6DXhXLVTCCW19a3vkW5fT4cC4zZIXvFIZZAacHqUS2ib2RFsduUafCwZlqM2Mj5p3FfJWlGs/640?wx_fmt=png&from=appmsg)

图 5　ShiftRows 变换：每行逐一展示移位前后的 nibble 排列

ShiftRows 的等价公式为：

（行左移位）

解密逆操作 InvShiftRows：

（行右移位）

以 Row 1 为例：原来位于  的元素  左移 1 位后落到列位置 3，即 。MixColumnsSerial 作用于列 3 时，会将来自行 0、行 1（移位后）、行 2（移位后）、行 3（移位后）的四个元素全部混合，这正是跨行扩散的机制。

### 2.6 MixColumnsSerial 与  域运算

MixColumnsSerial 对状态矩阵的每一列**独立**执行一次  矩阵乘法：将该列的 4 个 nibble 视为  上的列向量，乘以 MDS 矩阵 ，结果写回该列。图 6 展示了这一过程。

![图 6　MixColumnsSerial 矩阵乘法（对每列  独立执行）](https://mmbiz.qpic.cn/mmbiz_jpg/CvoBUu8TBhuurFsOtXaf4y0FV1EAVUkjWThDGIiaZtOA3WAicTGYFl44ic7bHvgUAEO3zQeQibgMjVHWFgFXbITGNlYu8B9nV7XeQIZhQ19AktI/640?wx_fmt=webp&from=appmsg)

图 6　MixColumnsSerial 矩阵乘法（对每列  独立执行）

矩阵  与串行步骤矩阵  的关系（原论文式 ）：

（所有元素均在  中，以十六进制表示）

矩阵  对应单次串行移位混合步骤——硬件上每拍将当前列向量  更新为 ，连续执行 4 拍即完成 ，这是 **MixColumnsSerial** 命名的由来，也使其在逐 nibble 串行硬件中极易实现。展开后的矩阵方程为：

 是一个 **MDS（最大距离可分）矩阵**，分支数（Branch Number）。分支数的含义：对于任意非零输入差分向量，输入与输出中被激活（非零差分）的 nibble 数之和至少为 5。换言之，若输入只有 1 个 nibble 发生变化，输出中至少 4 个 nibble 会发生变化，实现强扩散。

**域运算**：矩阵系数的乘法运算在有限域  中进行，该域由不可约多项式  定义。 加法即按位异或（），乘法是多项式乘法后模  归约，因此 。实现上采用"移位-累加"循环：

```
gf4_mul(a, b):
    r ← 0
    重复 4 次：
        若 b[0] = 1 ：r ← r ⊕ a           ← 当前最低位为 1 时累加
        b ← b >> 1
        若 a[3] = 1 ：a ← (a << 1) ⊕ 0x3  ← 溢出：x⁴ ≡ x+1，XOR 归约多项式余项 (x+1) = 0x3
        否则        ：a ← a << 1
    返回 r（取低4位）
```

`0x3` 对应多项式 ，即  去掉最高次  后的余项。每次  溢出（），左移后产生 ，按  替换，相当于 XOR `0x3` 并丢弃溢出位。

## 三、密钥方案与解密

### 3.1 统一密钥取用公式

LED 没有独立的密钥扩展算法。第  步的子密钥  的格位  处的 nibble，直接按下式从原始密钥取出：

其中  是原始密钥按高位优先展开的 nibble 数组（共  个元素）。 给出了第  步的"起始偏移"，三种密钥长度对应不同的取用规律：

| 变种 | key nibbles | 偏移公式 | 规律 |
| --- | --- | --- | --- |
| LED-64 | 16 |  | 所有步偏移为 0，子密钥永远等于原始密钥 |
| LED-80 | 20 |  | 每 5 步一周期，窗口在 20 个 nibble 上循环滑动 |
| LED-128 | 32 |  | 0 与 16 严格交替，对应高/低 64 位两个子密钥 |

### 3.2 LED-64 密钥方案

密钥共 16 个 nibble。步偏移  对所有步恒成立，因此全部 9 个子密钥（）均等于原始密钥  本身。

![图 7　LED-64 密钥方案：单一密钥重复注入 9 次](https://mmbiz.qpic.cn/mmbiz_jpg/CvoBUu8TBhsStbeF7B6WibRcibN...