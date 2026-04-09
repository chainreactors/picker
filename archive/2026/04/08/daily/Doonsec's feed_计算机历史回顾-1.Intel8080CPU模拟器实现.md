---
title: 计算机历史回顾-1.Intel8080CPU模拟器实现
url: https://mp.weixin.qq.com/s/e8nPTpyzi6wTu-MJYDDBWw
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:26:08.549543
---

# 计算机历史回顾-1.Intel8080CPU模拟器实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4aFFhlhlxThG3x1RupsHL6pLy8KlpWfiaLmWOVmhMyQYHVFvdMGJdVQJB499TcytOxPUYd9mbRmzfGNS1dcttlGR9rWn9y84CwM/0?wx_fmt=jpeg)

# 计算机历史回顾-1.Intel8080CPU模拟器实现

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器中沉浸阅读

一、简介

    Intel 8080是Intel公司于1974年4月发布的8位微处理器。它采用6微米N沟道硅栅MOS工艺制造，集成了约6000个晶体管，主频为2MHz，每秒可执行约29万次操作。更多介绍都可以在百度百科里面搜到，我们从最终目的为制作模拟器的角度学习这块CPU。

  二、CPU基本信息

```
16位地址总线8位数据总线支持64KB内存
```

1.寄存器信息

|  |  |  |
| --- | --- | --- |
| 15 ... 8 | 7 ... 0 | 备注 |
| A(accumulator) | F(flags) | 由PSW指向该寄存器对 |
| B | C | 由B指向该寄存器对 |
| D | E | 由D指向该寄存器对 |
| H | L | 由H指向该寄存器对 |
| SP(stack pointer) | | 栈指针 |
| PC(program counter) | | 程序指针 |

其中标志位寄存器结构表所示：

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| S | Z | 0 | A | 0 | P | 1 | C |

```
S-Sign Flag，符号标志位，最高位为1则置1，最高位为0则置0Z-Zero Flag，零标志位，结果为0则置1，结果为1则置00-不使用，总为0A-Auxiliary Carry Flag，辅助进位标志位，低4位的运算产生进位则置1，不产生进位则置00-不使用，总为0P-Parity Flag，奇偶标志位，结果中1的个数为偶数则置1，为奇数则置01-不使用，总为1C-Carry Flag，进位标志位，结果产生进位则置1，不产生进位则置0
```

2.指令集

    下面是我整理的Intel8080指令集

```
# Data Transfer数据传输指令'MOV': self._exec_mov,#MOV dst, src, 将src寄存器的值移动到dst寄存器，指令大小为1个字节'MVI': self._exec_mvi,#MVI dst, imm8, 将立即数imm8移动到dst寄存器，指令大小为2个字节'LXI': self._exec_lxi,#LXI reg, imm16, 将立即数imm16移动到reg寄存器对，指令大小为3个字节'LDA': self._exec_lda,#LDA addr, 将addr地址的值移动到A寄存器，指令大小为3个字节'STA': self._exec_sta,#STA addr, 将A寄存器的值写入addr地址，指令大小为3个字节'LHLD': self._exec_lhld,#LHLD addr, 将addr地址的值移动到HL寄存器，指令大小为3个字节'SHLD': self._exec_shld,#SHLD addr, 将HL寄存器的值写入addr地址，指令大小为3个字节'LDAX': self._exec_ldax,#LDAX rp, 将rp寄存器对的值所指向的内存地址的值移动到A寄存器，指令大小为1个字节'STAX': self._exec_stax,#STAX rp, 将A寄存器的值写入rp寄存器对所指向的内存地址，指令大小为1个字节'XCHG': self._exec_xchg,#XCHG, 交换DE寄存器对和HL寄存器对，指令大小为1个字节# Arithmetic'ADD': self._exec_add,#ADD reg, 将reg寄存器的值加到A寄存器，指令大小为1个字节，更新全部标志位'ADC': self._exec_adc,#ADC reg, 将reg寄存器的值加标志位carry的值然后再加到A寄存器，指令大小为1个字节，更新全部标志位'SUB': self._exec_sub,#SUB reg, 将A寄存器的值减去reg寄存器的值，指令大小为1个字节，更新全部标志位'SBB': self._exec_sbb,#SBB reg, 将A寄存器的值减去reg寄存器的值再减去标志位carry的值，指令大小为1个字节，更新全部标志位'INR': self._exec_inr,#INR reg, 将reg寄存器的值加1，指令大小为1个字节，更新标志位（除了carry标志位）'DCR': self._exec_dcr,#DCR reg, 将reg寄存器的值减1，指令大小为1个字节，更新标志位（除了carry标志位）'INX': self._exec_inx,#INX rp, 将rp寄存器对的值加1，指令大小为1个字节，不影响标志位'DCX': self._exec_dcx,#DCX rp, 将rp寄存器对的值减1，指令大小为1个字节，不影响标志位'DAD': self._exec_dad,#DAD rp, 将rp寄存器对的值加到HL寄存器对，指令大小为1个字节，只更新carry标志位'DAA': self._exec_daa,#DAA, 调整A寄存器适应BCD编码，指令大小为1个字节，更新标志位'ADI': self._exec_adi,#ADI imm8, 将立即数imm8加到A寄存器，指令大小为2个字节，更新全部标志位'ACI': self._exec_aci,#ACI imm8, 将立即数imm8加标志位carry的值然后再加到A寄存器，指令大小为2个字节，更新全部标志位'SUI': self._exec_sui,#SUI imm8, 将A寄存器的值减去立即数imm8的值，指令大小为2个字节，更新全部标志位'SBI': self._exec_sbi,#SBI imm8, 将A寄存器的值减去立即数imm8再减去标志位carry的值，指令大小为2个字节，更新全部标志位# Logical'ANA': self._exec_ana,#ANA reg, 将A寄存器的值与reg寄存器的值进行AND操作，指令大小为1个字节，更新全部标志位'XRA': self._exec_xra,#XRA reg, 将A寄存器的值与reg寄存器的值进行XOR操作，指令大小为1个字节，更新全部标志位'ORA': self._exec_ora,#ORA reg, 将A寄存器的值与reg寄存器的值进行OR操作，指令大小为1个字节，更新全部标志位'CMP': self._exec_cmp,#CMP reg, 将A寄存器的值减去reg寄存器的值，指令大小为1个字节，更新全部标志位'RLC': self._exec_rlc,#RLC, 将A寄存器的值左移1位，最高位移至最低位，且carry标志位为A寄存器的最高位，指令大小为1个字节'RRC': self._exec_rrc,#RRC, 将A寄存器的值右移1位，最低位移至最高位，且carry标志位为A寄存器的最低位，指令大小为1个字节'RAL': self._exec_ral,#RAL, 将A寄存器的值左移1位，A寄存器的最低位为carry标志位的值，然后carry标志位为A寄存器移位前的最高位，指令大小为1个字节'RAR': self._exec_rar,#RAR, 将A寄存器的值右移1位，A寄存器的最高位为carry标志位的值，然后carry标志位为A寄存器移位前的最低位，指令大小为1个字节'CMA': self._exec_cma,#CMA, 对A寄存器的值取反，指令大小为1个字节，不更新标志位'CMC': self._exec_cmc,#CMC, 对carry标志位取反，指令大小为1个字节，不更新标志位（除了carry标志位）'STC': self._exec_stc,#STC, 将carry标志位设为1，指令大小为1个字节，不更新标志位'ANI': self._exec_ani,#ANI imm8, 将立即数imm8与A寄存器的值进行AND操作，指令大小为2个字节，更新全部标志位'XRI': self._exec_xri,#XRI imm8, 将立即数imm8与A寄存器的值进行XOR操作，指令大小为2个字节，更新全部标志位'ORI': self._exec_ori,#ORI imm8, 将立即数imm8与A寄存器的值进行OR操作，指令大小为2个字节，更新全部标志位'CPI': self._exec_cpi,#CPI reg, 将A寄存器的值与立即数imm8进行比较，指令大小为2个字节，更新全部标志位# Branch'JMP': self._exec_jmp,#JMP addr, 将PC设置为addr，指令大小为3个字节'JNZ': self._exec_jnz,#JNZ addr, 如果zero标志位为0，将PC设置为addr，指令大小为3个字节'JZ': self._exec_jz,#JZ addr, 如果zero标志位为1，将PC设置为addr，指令大小为3个字节'JNC': self._exec_jnc,#JNC addr, 如果carry标志位为0，将PC设置为addr，指令大小为3个字节'JC': self._exec_jc,#JC addr, 如果carry标志位为1，将PC设置为addr，指令大小为3个字节'JPO': self._exec_jpo,#JPO addr, 如果parity标志位为0，将PC设置为addr，指令大小为3个字节'JPE': self._exec_jpe,#JPE addr, 如果parity标志位为1，将PC设置为addr，指令大小为3个字节'JP': self._exec_jp,#JP addr, 如果sign标志位为0，将PC设置为addr，指令大小为3个字节'JM': self._exec_jm,#JM addr, 如果sign标志位为1，将PC设置为addr，指令大小为3个字节'CALL': self._exec_call,#CALL addr, 将下一条指令地址压入栈，将PC设置为addr，指令大小为3个字节'CNZ': self._exec_cnz,#CNZ addr, 如果zero标志位为0，将下一条指令地址压入栈，将PC设置为addr，指令大小为3个字节'CZ': self._exec_cz,#CZ addr, 如果zero标志位为1，将下一条指令地址压入栈，将PC设置为addr，指令大小为3个字节'CNC': self._exec_cnc,#CNC addr, 如果carry标志位为0，将下一条指令地址压入栈，将PC设置为addr，指令大小为3个字节'CC': self._exec_cc,#CC addr, 如果carry标志位为1，将下一条指令地址压入栈，将PC设置为addr，指令大小为3个字节'CPO': self._exec_cpo,#CPO addr, 如果parity标志位为0，将下一条指令地址压入栈，将PC设置为addr，指令大小为3个字节'CPE': self._exec_cpe,#CPE addr, 如果parity标志位为1，将下一条指令地址压入栈，将PC设置为addr，指令大小为3个字节'CP': self._exec_cp,#CP addr, 如果sign标志位为0，将下一条指令地址压入栈，将PC设置为addr，指令大小为3个字节'CM': self._exec_cm,#CM addr, 如果sign标志位为1，将下一条指令地址压入栈，将PC设置为addr，指令大小为3个字节'RET': self._exec_ret,#RET, 从栈中弹出PC值，指令大小为1个字节'RNZ': self._exec_rnz,#RNZ, 如果zero标志位为0，从栈中弹出PC值，指令大小为1个字节'RZ': self._exec_rz,#RZ, 如果zero标志位为1，从栈中弹出PC值，指令大小为1个字节'RNC': self._exec_rnc,#RNC, 如果carry标志位为0，从栈中弹出PC值，指令大小为1个字节'RC': self._exec_rc,#RC, 如果carry标志位为1，从栈中弹出PC值，指令大小为1个字节'RPO': self._exec_rpo,#RPO, 如果parity标志位为0，从栈中弹出PC值，指令大小为1个字节'RPE': self._exec_rpe,#RPE, 如果parity标志位为1，从栈中弹出PC值，指令大小为1个字节'RP': self._exec_rp,#RP, 如果sign标志位为0，从栈中弹出PC值，指令大小为1个字节'RM': self._exec_rm,#RM, 如果sign标志位为1，从栈中弹出PC值，指令大小为1个字节'RST': self._exec_rst,#RST n, 将下一条指令地址压入栈，然后设置PC为向量表地址，指令大小为1个字节'PCHL': self._exec_pchl,#PCHL, PC寄存器指向HL寄存器的值，指令大小为1个字节# Stack'PUSH': self._exec_push,#PUSH rp, 将rp寄存器对的值压入栈，指令大小为1个字节'POP': self._exec_pop,#POP rp, 从栈中弹出一个值，将其赋值给rp寄存器对，指令大小为1个字节'XTHL': self._exec_xthl,#XTHL, 交换HL寄存器对指向的值和SP寄存器对指向的值，指令大小为1个字节'SPHL': self._exec_sphl,#SPHL, 将HL寄存器对的值写入SP寄存器对，指令大小为1个字节# I/O'IN': self._exec_in,#IN port, 从端口读取一个字节，指令大小为1个字节'OUT': self._exec_out,#OUT port, 将A寄存器的值写入端口，指令大小为1个字节# Control'EI': self._exec_ei,#EI, 启用中断，指令大小为1个字节'DI': self._exec_di,#DI, 禁用中断，指令大小为1个字节'HLT': self._exec_hlt,#HLT, 挂起当前指令，指令大小为1个字节'NOP': self._exec_nop,#NOP, 无操作，指令大小为1个字节
```

该图是在互联网上找到的Intel8080CPU寄存器和指令集一览图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YCFhd4xMLn11ibLfL6YGWj16r6aNOcyriaDcz94NF4KKy11wuKL8X9S5s4hr6e9fqmgvxRpUh4XRnmS6MA9YaK1tr0yEA4F2MGo/640?wx_fmt=png&from=appmsg)

三.模拟器实现

    接下来使用python实现一个简单的Intel8080CPU模拟器，使用64KB内存，模块如下：

```
1.Intel8080CPU模块2.RAM-64KB内存模块
```

1.Intel8080CPU模块

```
package name：intel8080
```

    该包下主要包含两个py文件，分别是i8080.py和instructions.py，其中i8080.py主要定义intel8080CPU的寄存器值以及状态行为，而instructions.py主要定义操作指令属性，辅助i8080.py解码并执行。

    首先instructions.py的导入依赖如下：

```
from enum import Enum, autofrom dataclasses import dataclassfrom typing import Optional
```

该py文件主要包含的类如下：

（1）OperandType类：对应指令的操作数类别

```
class OperandType(Enum):  """  指令的操作数类别  """  NONE = auto()  REGISTER = auto()  # 8-bit 寄存器 (B, C, D, E, H, L, A)  REGISTER_PAIR = auto()  # 16-bit 寄存器对 (BC, DE, HL, SP)  IMMEDIATE_8 = auto()  # 8-bit 立即数  IMMEDIATE_16 = auto()  # 16-bit 立即数 (address or data)  MEMORY = auto()  # Memory reference (M，也就是HL寄存器对指向的内存中的数据)  CONDITION = auto()  # 条件跳转标志 (NZ, Z, NC, C, PO, PE, P, M)
```

（2）Register类：对应的寄存器标识

```
class Register(Enum):  """  8-bit 寄存器  """  B = 0  C = 1  D = 2  E = 3  H = 4  L = 5  A = 7  M = 6  # Memory (HL)
```

(3)RegisterPair类：对应的寄存器对标识

```
class RegisterPair(Enum):  """  16-bit 寄存器对  """  BC = 0  DE = 1  HL = 2  SP = 3  # Stack Pointer  PSW = 3  # Program Status Word (A + Flags)
```

（4）Condition类：对应的条件跳转标识

```
classCondition(Enum):    """跳转条件"""    NZ=0  # Not Zero    Z=1   # Zero    NC=2  # No Carry    C=3   # Carry    PO=4  # Parity Odd    PE=5  # Parity Even    P=6   # Plus (正数)    M=7   # Minus (负数)
```

（5）Flag类：对应的标志位标识

```
classFlag(Enum):    """Status flags"""    CARRY=0      # Carry flag    PARITY=2     # Parity flag    AUX_CARRY...