---
title: FPGA中的有符号数表示与高速加法器实现 - potatso
url: https://www.cnblogs.com/potatso/p/18926720
source: 博客园 - potatso
date: 2025-06-14
fetch_date: 2025-10-06T22:47:49.269029
---

# FPGA中的有符号数表示与高速加法器实现 - potatso

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [FPGA中的有符号数表示与高速加法器实现](https://www.cnblogs.com/potatso/p/18926720 "发布于 2025-06-13 11:37")

# 1. 有符号整数的表示：补码（Two's Complement）

在数字系统中，表示有符号整数是一个核心问题。常见的方法包括原码（Sign-Magnitude）、反码（One's Complement）和补码（Two's Complement）。其中，补码因其在硬件实现上的优越性而成为主流。

## 1.1 原码与反码的局限性

原码： 最高位为符号位（0代表正，1代表负），其余位表示数值的绝对值。
问题： 存在正零（0000）和负零（1000）两种表示；加减法运算规则复杂，需要根据操作数符号额外判断。
反码： 正数与原码相同；负数对其绝对值的所有位取反。
问题： 依然存在正零（0000）和负零（1111）两种表示；加法运算中，若最高位产生进位，需进行“末位进位加一”的操作，增加了硬件复杂性。

## 1.2 补码的定义与优势

补码通过一个巧妙的定义，解决了原码和反码的所有问题：

* 正数： 补码与其原码相同。
* 负数： 负数 X 的补码，等于其绝对值 ∣X∣ 的反码加1。
  补码的核心优势在于其与**模运算（Modular Arithmetic）**的紧密关联。在一个 N 位的二进制系统中，其模数是 2^N。负数 −X 的补码 Comp
  2
  ​
  (−X) 实际上就是 X 在模 2
  N
  意义下的补数，即 Comp
  2
  ​
  (−X)=2
  N
  −X。
* 带来的硬件优势：

零的唯一表示： 只有 0000...0 唯一表示零。反码中的负零 1111...1，经过加1操作后，会变成 (1)0000...0，其溢出的最高位被丢弃，结果正是唯一的正零。
加减法运算的统一： 这是最重要的优势。无论操作数是正数还是负数，它们的加法和减法（通过加负数的补码实现）都可以直接使用同一个标准二进制加法器来完成。加法器只需执行简单的二进制加法，而无需额外的符号位判断和处理逻辑。若运算结果产生最高位的进位（溢出），该进位可直接丢弃（对于 N 位运算，只保留 N 位结果）。

# 2. 高速加法器实现：超越串行进位

在计算机的算术逻辑单元（ALU）中，加法器的速度是关键性能指标。

## 2.1 行波进位加法器（Ripple-Carry Adder, RCA）

原理： RCA 由 N 个全加器串联组成。每个全加器处理一位数的加法，并将产生的进位（Carry Out）传递给下一位（高位）的进位输入（Carry In）。进位信号像水波一样，从最低位逐级向最高位传播。

FPGA 实现特点：
Verilog 描述： 通常通过实例化单个全加器模块并进行串行连接来描述，或直接通过循环生成逻辑。
综合与映射： 现代 FPGA 架构（如 Xilinx、Intel）内部包含专用的高速进位链（Carry Chain）硬件。综合器在识别 RCA 结构时，会将其优化映射到这些专用链上，利用其极低的物理传播延迟。
性能： 由于专用进位链的优化，RCA 在 FPGA 上的实际性能远优于理论上的通用逻辑门串行传播延迟，对于大多数中等位宽的加法任务而言，其性能和资源效率均可接受。

## 2.2 超前进位加法器（Carry-Lookahead Adder, CLA）

CLA 旨在克服 RCA 的进位串行传播瓶颈，通过并行计算所有进位信号来提高速度。

核心思想：进位逻辑的“展开”与并行计算
CLA 的本质是对传统全加器中进位信号的逻辑依赖关系进行“展开”。它并非将整个加法操作转化为查表，而是将进位计算中原本的串行依赖转化为纯组合逻辑的并行计算。这利用了数字电路天生具备的并行特性。

```
module addr(
    input[2:0] a,
    input[2:0] b,
    output[2:0] Sum,
    output carry
    );

    wire [2:0] G; // 每位独立的进位产生信号 (Generate)
    wire [2:0] P; // 每位独立的进位传播信号 (Propagate)
    // C[i] 对应公式中的 C_{i+1}，表示从第 i 位传递给第 i+1 位的进位
    wire [2:0] C;

    // --- 1. 计算每位的 G 和 P 信号 ---
    // G[i] = A[i] & B[i]: 表示当前位 (A[i], B[i]) 自身相加是否产生进位
    // 因为如果A[i]和B[i]都是1，那么当前位就会产生进位。
    assign G[0] = a[0] & b[0];
    assign G[1] = a[1] & b[1];
    assign G[2] = a[2] & b[2];

    // P[i] = A[i] ^ B[i]: 表示当前位 (A[i], B[i]) 是否能将低位的进位传播到高位
    // 如果A[i]与B[i] 不同，那么再加上低位的进位，就会产生进位。否则，即使低位产生进位，也不会传播到高位。
    assign P[0] = a[0] ^ b[0];
    assign P[1] = a[1] ^ b[1];
    assign P[2] = a[2] ^ b[2];

    // --- 2. 并行计算所有中间进位信号 (C1, C2, C3) ---
    // C_{i+1} = G_i | (P_i & C_i)
    // （这里假设最开始的输入进位 C0 = 0）

    // C[0] 对应公式中的 C1 (从0位传给1位的进位)
    // C1 = G0 | (P0 & C0)
    // 若 C0=0，则 C1 = G0
    assign C[0] = G[0];

    // C[1] 对应公式中的 C2 (从1位传给2位的进位)
    // C2 = G1 | (P1 & C1)
    // 此处 C1 已被展开为 G0，所以 C2 = G1 | (P1 & G0)
    // 含义：进位到第2位，要么是第1位自己产生(G1)
    // 要么是在两位与上一位进位相加的过程中产生的进位。
    assign C[1] = G[1] | (P[1] & C[0]); // C[0]在此处代表C1

    // C[2] 对应公式中的 C3 (从2位传给3位的进位，即最终进位)
    // C3 = G2 | (P2 & C2)
    // 此处 C2 已被展开，所以 C3 = G2 | (P2 & (G1 | (P1 & G0)))
    // 含义：进位到第3位，要么是第2位自己产生(G2)，要么是第2位将C2传播过来(P2 & C2)。
    assign C[2] = G[2] | (P[2] & C[1]); // C[1]在此处代表C2

    // --- 3. 计算最终的和 (Sum) ---
    // S_i = P_i ^ C_i
    // S0 = P0 ^ C0 (若 C0=0，则 S0=P0)
    assign Sum[0] = P[0];

    // S1 = P1 ^ C1
    assign Sum[1] = P[1] ^ C[0]; // C[0]在此处代表C1

    // S2 = P2 ^ C2
    assign Sum[2] = P[2] ^ C[1]; // C[1]在此处代表C2

    // --- 4. 计算最终的输出进位 (Carry Out) ---
    // 最终进位就是最高位产生的进位 C3
    assign carry = C[2]; // C[2]在此处代表C3

endmodule
```

“展开”与“查表”的区别：
值得注意的是，这种“展开”是将逻辑函数转化为更深更广的组合逻辑门网络（例如，通过更多的与门和或门来直接计算结果），以牺牲面积换取速度。这不同于查表运算（Look-up Table, LUT-based operation）。查表运算是指将所有可能的输入组合及其对应输出预先存储在一个查找表中，然后通过输入地址来直接读取输出。虽然 FPGA 的基本逻辑单元 LUT 本身就是小型的查找表，但 CLA 的设计理念并非将整个加法器视为一个大查表，而是通过门级逻辑的并行化实现加速。

延迟特性： 所有进位 C
i
​
的计算可以并行进行。总延迟不再是与位数 N 成正比（O(N)），而是主要取决于实现这些复杂组合逻辑的门级深度，通常为对数级 O(logN)。

FPGA 实现特点：

Verilog 描述： 通常直接使用 assign 语句实现上述展开的逻辑表达式，即进行门级描述。
综合与映射： 综合器会将这些复杂的与或非表达式映射到 FPGA 的通用**查找表（LUT）**中，可能需要多个 LUT 级联来完成。
性能与资源权衡：
优势： 理论上能打破进位串行瓶颈，适用于 ASIC 中对速度有极致要求的场景。
劣势： 手写 CLA 结构在 FPGA 上通常会消耗更多的通用 LUT 资源。由于 LUT 级联的延迟和通用布线延迟，一个大型的手写 CLA 在 FPGA 上不一定能比利用了专用进位链的 RCA 更快。在某些特定 FPGA 架构中，且经过精心设计和优化，才能体现出其速度优势。

# 3. 实际 FPGA 设计实践中的加法器选择

在实际的 FPGA 设计中，对于加法器这样的基本算术单元，最推荐和高效的方法是：

利用 Verilog/SystemVerilog 的内置运算符 (+)：

```
assign {Cout, Sum} = A + B + Cin;
```

这是最佳实践。综合工具（如 Vivado）会智能地识别此运算符，并根据目标 FPGA 架构和设计约束，自动选择最优化、最高效的底层硬件实现方式。这包括：

优先映射到 FPGA 内部的硬核 DSP 块（如果加法器是其功能的一部分）。
利用 FPGA 内部的专用进位链和优化的 LUT 结构。
根据时序要求，自动选择合适的加法器架构（如行波进位、查找表级联、甚至内部优化后的超前进位变体），以平衡性能和资源。
实例化厂商提供的 IP 核：
对于关键路径上的加法器或需要特定功能的加法器（如可配置延迟、带溢出标志等），可以直接使用 FPGA 厂商（如 Xilinx 或 Intel）提供的预优化加法器 IP 核。这些 IP 核是针对特定 FPGA 架构高度定制和优化的，能够确保最佳的性能、面积和功耗。

总结：

补码作为有符号数的统一表示方法，为计算机的加减法运算奠定了基础。而加法器的实现则在追求速度的道路上不断演进。从简单的行波进位到复杂的超前进位，核心都在于如何高效地处理进位信号。在 FPGA 设计中，理解这些底层原理固然重要，但掌握如何利用EDA工具的智能优化能力，通过简洁的Verilog运算符实现高效加法器，是更具实践意义的技能。

posted @
2025-06-13 11:37
[potatso](https://www.cnblogs.com/potatso)
阅读(119)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025