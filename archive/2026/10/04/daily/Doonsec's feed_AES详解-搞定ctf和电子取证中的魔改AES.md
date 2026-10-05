---
title: AES详解-搞定ctf和电子取证中的魔改AES
url: https://mp.weixin.qq.com/s/9DHQgZFsTKt82oxrC2zvWg
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:53:12.221750
---

# AES详解-搞定ctf和电子取证中的魔改AES

# AES详解-搞定ctf和电子取证中的魔改AES

原创

李逍遥
李逍遥

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

GZH WORKBENCH

AES详解

第0章.：从一个异或到AES

01

1 要解决的问题

PROBLEM

Alice 想把一段秘密消息发给 Bob，但通信信道被 Eve 窃听。Alice 和 Bob 事先共享一个秘密K（密钥）。目标：Alice 用 K 把明文 P 变成密文 C 发出去；Eve 即使拿到 C，也推不出 P；Bob 用 K 能把 C 还原成 P。

这就是**对称密码**（加解密用同一把密钥）的核心问题。AES（Advanced Encryption Standard，高级加密标准）是当今世界上使用最广泛的对称分组密码：128 位的数据块，128/192/256 位密钥。2001 年由美国国家标准与技术研究院（NIST）在全球公开竞赛中选出（Rijndael 算法胜出）。

02

2 AES概览

AES

AES 看起来很复杂：S 盒、行移位、列混合、轮密钥加、密钥扩展……但其实它是一条**"发现问题—解决问题—再发现问题—再解决"** 的过程。

CODE

异或加密

   │  问题1：密钥复用会被破解；短密钥可被频率分析破解

   ▼

+ 字节代换 SubBytes    ← 引入"非线性"，打散统计规律

   │  问题2：替换是逐字节的，字母频率/位置结构仍然保留

   ▼

+ 行移位 ShiftRows     ← 把一个位置的字节扩散到整行整列

   │  问题3：行移位只管"行"，列内 4 个字节之间没有混合

   ▼

+ 列混合 MixColumns    ← 让每一列的 4 个字节互相混合

   │  问题4：以上全是"固定运算"，密钥从未参与每轮变换

   ▼

+ 轮密钥加 AddRoundKey ← 每一轮都注入密钥材料

   │  问题5：只做一轮的话，攻击者用两个已知明文就能解出密钥

   ▼

× 10 轮迭代              ← 多轮复合，让差分和线性痕迹彻底湮灭

   │

   ▼

AES-128

第1章：数学基础

AES 的全部运算只发生在一个 8 位字节的世界里。这一章我们把这个8位字节世界构造出来。

03

1 异或 XOR：在 GF(2) 上做加法

XOR

一位二进制数组成的集合 {0, 1} 上定义两种运算：

运算 · 规则 · 说明

运算加法 ⊕

规则0⊕0=0，0⊕1=1，1⊕0=1，1⊕1=0

说明\*\*就是异或\*\*；1+1=0（进位被丢弃）

运算乘法 ·

规则0·0=0·1=1·0=0，1·1=1

说明就是普通与

这个两元素的集合配上这两种运算，构成一个**域**（field，能加减乘除的代数系统），记作 GF(2)（Galois Field，伽罗瓦域，纪念法国数学家 Évariste Galois）。

把 8 个这样的位打包成一个字节，逐位做 ⊕，就得到字节的加法：

CODE

0x57 ⊕ 0x83：

01010111

⊕ 10000011

= 11010100 = 0xD4

**关键性质**：在 GF(2) 上，**加法和减法是同一个运算**（因为 1⊕1=0，任何数加自己都归零：a⊕a=0，所以 -a = a）。这一条贯穿 AES 始终——解密时"减密钥"就是"加密钥"，"逆变换"全部由"正变换的逆元"构成。

04

2 把字节看成多项式

SECTION

一个字节b₇b₆…b₁b₀ 可以写成 GF(2) 上的多项式：

CODE

b₇x⁷ + b₆x⁶ + … + b₁x + b₀

例如 0x57 = 0101 0111 对应多项式**x⁶ + x⁴ + x² + x + 1**。

两个多项式相加 = 对应系数相加（系数相加就是 ⊕），所以**多项式加法就是字节异或**。麻烦的是乘法：两个 7 次多项式相乘会得到最高 14 次的多项式，不再是"一个字节"。

05

3 有限域 GF(2⁸)：模一个不可约多项式

SECTION

多项式乘法的解决办法和"时钟算术"（mod 12）一样：**取模**。GF(2⁸) 的构造：

找一个 8 次**不可约多项式**（irreducible polynomial）m(x)，所有多项式都对它取模。这样任何乘积都会被压回"次数 < 8"的范围，即一个字节。且每个非零元素都有乘法逆元——域的除法得以成立。

找一个不可约多项式是因为需要保证每个非零元素都有唯一的乘法逆元，即满足x\*x<sup>-1</sup>对m(x)取模为1，这里x<sup>-1</sup>是唯一的，这样可以解密的时候直接使用逆元进行运算即可。

AES 选定的模数（FIPS-197 规定）：

CODE

m(x) = x⁸ + x⁴ + x³ + x + 1        （二进制 100011011，记作 0x11B）

它不可约——不能被任何次数 ≤ 4 的 GF(2) 不可约多项式整除。8 次不可约多项式在 GF(2) 上一共有 30 个，AES 选择了二进制重量较轻（1 0001 1011）的那个，这样模运算的电路实现最便宜——**AES 的每个选择都是"安全性 × 实现成本"的权衡**。

以AES选定的模数为例：

PYTHON

x·(x⁷+x³+x²+1) + 1 = x⁸ + x⁴ + x³ + x + 1

所以x的逆元就是x⁷+x³+x²+1

06

4 快速乘法：xtime 与"移位—条件异或"

XTIME

乘以 x（即 0x02）有一个极快的算法。设字节 a 的多项式最高次为 x⁷，则 a·x 次数可能是 8，需要取模：由 m(x)=0 得 x⁸ ≡ x⁴+x³+x+1（mod m），也就是**溢出位补回 0x1B**：

CODE

xtime(a):                     // a · 0x02，即 a · x

a <<= 1// 整体左移一位（多项式乘 x）

if 原 a 的最高位是 1:      // 发生了 x⁸ 溢出

a ⊕= 0x1B// 模掉 m(x)

示例：xtime(0x57) = 0xAE（0101 0111 → 1010 1110，无溢出）；xtime(0xD4) = 0xB3（1101 0100 左移得 1 1010 1000，溢出则 ⊕0x1B → 1011 0011）。

任意乘法用"二进制展开 + xtime 链"完成，例如官方文档的经典例子：

CODE

0x57 · 0x83：      0x83 = 10000011 = x⁷ + x + 1

  0x57·x⁰ = 0x57

  0x57·x¹ = 0xAE

  0x57·x⁷ = 0x38      （连续 7 次 xtime：AE→47→8E→07→0E→1C→38）

  相加：0x57 ⊕ 0xAE ⊕ 0x38 = 0xC1

∴ 0x57 · 0x83 = 0xC1

07

5 乘法逆元与扩展欧几里得算法

SECTION

域里每个非零元 a 都有唯一逆元 a⁻¹ 使 a·a⁻¹ = 1。求法：扩展欧几里得算法（对多项式版本）。AES 的 S 盒第一步就是查逆元，这里看一个简单例子——求0x02（即 x）的逆：

CODE

m(x) = x·(x⁷+x³+x²+1) + 1

     └────商 q(x)────┘ 余 1

⇒ 1 = m(x) − x·q(x) ≡ (−q(x))·x  (modm)

⇒ x⁻¹ = q(x) = x⁷+x³+x²+1 = 0x8D

验证：xtime(0x8D) = 00011010 ⊕ 00011011 = 0x01 ✓

**为什么要逆元？**  密码算法的可逆性（能解密）要求每个变换都有逆。加法的逆是自己；乘法的逆靠这个域。S 盒的"逆映射"天然是 GF(2⁸) 里的求逆运算。  求解逆元可以根据费马小定理计算：x⁻¹=x²⁵⁴（费马小定理），也就是做254次xtime

08

6 📝 练习

SECTION

POINT 1**A1** 计算：0xD4 ⊕ 0xBF = ?

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4b9ZDNwnsAu8ZdKMP7qVicU5BzWq9kDwofricvfLXzpoDib4pCSfpE805KNrDNf2iccicIEoENJX8VnL3wpqTscu5qfcU5BjBheFAk0/640?wx_fmt=jpeg&from=appmsg)

POINT 1**A2** 用 xtime 计算：xtime(0x9A) = ?（提示：0x9A 最高位为 1）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4Zt7tvdSiauQuSQeGfEcoWbxuYicyIJyTCicb4y2cyoqMjCgeJe2fzPpGV6uUBjhEXRekULbTaANu4MhtTR0ggJibvXfKxn3n8yHsM/640?wx_fmt=jpeg&from=appmsg)

POINT 1**A3** 用 1.4 节的方法计算：0x13 · 0xA5 = ?

![](https://mmbiz.qpic.cn/mmbiz_jpg/6nhGiavBDP4YxQBtRWR6WziaRuTPPMt0XtpicPKhPWxfIbHPfBUPFibwCmdqpULz9oatFOMS5FQ1OEgeGFLpmvsS5EbGU7tAd3ibX36KiahonYl3U/640?wx_fmt=jpeg&from=appmsg)

第2章：异或加密

在引入任何复杂模块之前，我们先建立**最小的加密原语**：把密钥和明文逐字节异或。它是现代流密码的祖先，也是 AES 内部"轮密钥加"的原型。

09

1 异或密码

SECTION

CODE

加密：C = P ⊕ K

解密：P = C ⊕ K        （因为 (P⊕K)⊕K = P⊕(K⊕K) = P⊕0 = P）

异或的三个代数性质是整个密码学的基石：

1**自逆性**：a⊕a = 0 ⇒ 解密和加密是同一个操作；

2**可交换可结合**：(a⊕b)⊕c = a⊕(b⊕c)，乱序合并不影响结果；

3**对位独立**：每一位互不影响，没有任何"进位"把信息从一个位带到另一个位。

性质 3 是双刃剑：它让实现极其简单，也让**统计规律原封不动地从明文传递到密文**——只不过套上了一层"逐位遮盖"。遮盖是否可靠，完全取决于密钥 K。

10

2 理论上无敌的情形：一次性密码本

SECTION

如果密钥满足三个苛刻条件：

1与明文**等长**；

2**真正随机**；

3**只用一次**；

则 OTP 被信息论证明**绝对安全**（Shannon, 1949）：无论攻击者算力多强，密文都不泄露明文的任何信息（所有明文先验等可能）。每个密文字节 C = P⊕K，当 K 均匀随机时，C 也均匀随机，与 P 统计独立。

11

3 攻击一：密钥复用——两次密码本攻击（Two-Time Pad）

TWO-TIME PAD

**场景**：Alice 用同一段密钥 K 加密了两条消息。

CODE

C₁ = P₁ ⊕ K

C₂ = P₂ ⊕ K

Eve 拿到 C₁、C₂，做一件小事：

CODE

C₁ ⊕ C₂ = P₁ ⊕ P₂ ⊕ (K⊕K) = P₁ ⊕ P₂     ← 密钥消失了！

P₁⊕P₂ 是两条明文的"差"。两条有意义的消息（比如都是英文），它们的异或绝非随机：在两者相同的位置结果是 0（会暴露出成片的 0x00），在字母相同处结果偏小……**明文的一切统计结构都渗进了这个差里**。攻击者随后用 **crib dragging（猜测词滑动）** ：把一个猜测的单词（crib）摆在某个偏移上，与 P₁⊕P₂ 异或，看翻出来的另一段明文是否像人话。像，就说明猜测和位置都对；不像，就换词或换偏移。几轮下来两条明文全部被还原。

**实战演示**：

CODE

P₁ = "attack the bridge at midnight tonight"

P₂ = "attack the bridge with heavy weapons!!"

K  = 3fa10759c2 8e44bb12 6d90e5 2af783 4c01de68b5 3a97 0d52afc976 1be8a430 9b 5ed387f2

密文与它们的异或：

CODE

C₁     = 5ed57338a1e564cf7a08b087589ee72b64fe09c11afa6436c1a011739c8444f430bae09a

C₂     = 5ed57338a1e564cf7a08b087589ee72b64fe1fdc4eff2d3acaa80062c8d355fa2ebce981

C₁⊕C₂ = 000000000000000000000000000000000000161d5405490c0b0811115457110e1e06091b55

         └────────── 前 18 字节全 0 ────────┘

前 18 字节全是 0——因为两条明文都以 attack the bridge  开头。**密钥复用瞬间暴露**。然后对剩余部分做 crib dragging：在偏移 23 处试词 heavy：

CODE

C₁⊕C₂[23..27] ⊕ "heavy" = "dnigh"    ← 很像 "midnight" 的尾巴！

顺着这个猜想，把 midnight摆在偏移 21 再试：

CODE

C₁⊕C₂[21..28] ⊕ "midnight" = "h heavy "    ← P₂ 果然是 "...with heavy ..."

12

4 攻击二：短密钥反复使用——退化为多表代换

USAGE

**场景**：密钥比明文短，就循环重复使用：

CODE

C[i] = P[i] ⊕ K[imodL]        （L = 密钥长度）

这等价于 L 个独立的单字节异或（每个密钥字节对应明文的一个"列"）。每个单字节异或都是**单表代换**：明文字母 a 在该列永远变成 a⊕k。于是退化为维吉尼亚密码：单看一列，字母频率表被"平移"了，但形状还在。破解两步走：

1**确定密钥长度 L**：密文两个副本错开 t 位异或，若 t 恰是 L 的倍数，则结果是两个"同列明文"的异或，0 的比例显著偏高（卡斯基检验 / 汉明距离法）。

2**逐列频率分析**：每一列里频次最高的密文字节，大概率对应明文里频次最高的字符（空格或 e）。用 k = 空格 ⊕ 最高频字节 恢复该列密钥字节。

13

5 异或密码的问题

PROBLEM

病根 · 表现 · 需要的解药

病根线性：输出是输入的线性函数（异或是 GF(2) 上的加法）

表现已知明文 P 立刻给出 K = P⊕C

需要的解药注入\*\*非线性\*\*变换 → SubBytes

病根逐字节独立：一个字节的明文只影响同位置的字节

表现频率结构按位置保留，可被逐列分析

需要的解药让字节之间\*\*互相混合\*\* → ShiftRows + MixColumns

病根密钥只加一次

表现密钥与密文之间结构简单

需要的解药每一轮注入不同密钥材料 → AddRoundKey + 密钥扩展

病根轮数太少

表现1 轮的复合仍可被代数/统计攻击拆开

需要的解药多轮迭代 → 10 轮

14

6 混淆与扩散

SECTION

1949 年 Shannon 在《保密系统的通信理论》中给出对称密码的两条设计原则，AES 是它们的教科书级实现：

POINT 1**混淆（Confusion）** ：让密文与密钥之间的关系尽可能复杂，使攻击者无法从密文统计中剥离出密钥。→ 由**非线性**的 S 盒提供。

POINT 2**扩散（Diffusion）** ：让明文每一位的影响迅速蔓延到密文的许多位，抹平统计规律。→ 由**线性置换层**（行移位+列混合）提供。

第3章：AES 四大模块逐一剖析

15

0 状态矩阵 State：16 字节摆成 4×4 方阵

STATE

AES 不是对"一维字节串"运算，而是把 16 字节明文填进一个 4 行 4 列的方阵（**列主序**：按列依次填入）：

CODE

明文字节序列：in₀ in₁ in₂ … in₁₅

state[r][c] = in[r + 4c]        （r 行号 0..3，c 列号 0..3）

例：明文 3243f6a888 5a30 8d313198a2e0370734 摆成

c0c1c2c3

r0328831e0

r143   5a3137

r2f6309807

r3a8   8da234

（读法：第 0 列的 4 个字节 32 43 f6 a8 就是明文的前 4 个字节。）

**为什么这样排？**  因为 AES 需要两个作用方向正交的操作——列内的混合（列混合）与列间的扩散（行移位）——而方阵是让它们共存的最简数据结构。加密结束后按同样的列主序把 state 展平回 16 字节即密文。

PYTHON

defprint\_state(state):

forrowinstate:

display\_row = [hex(r) forrinrow]

print(display\_row)

deftranslate\_to\_state(plain\_bytes):

state = [[0for\_inrange(4)] for\_inrange(4)]

forrowinrange(4):

forcolinrange(4):

state[row][col] = plain\_bytes[row + col\*4]

returnstate

plain\_bytes = [0x32,0x43,0xf6,0xa8,0x88,0x5a,0x30,0x8d,0x31,0x31,0x98,0xa2,0xe0,0x37,0x07,0x34]

state = translate\_to\_state(plain\_bytes)

print\_state(state)

输出：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Y9InHOPRxMsxeGMTWsZLcaicYcwZUKibFiacc6m1tmJoLxheVaS0oP6xyfOh306CzoHzvFnax5UtvrkKz6ZiauwQw0KSBVryqxNyc/640?wx...