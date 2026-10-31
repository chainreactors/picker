---
title: Beatrice.py 源码解读
url: https://mp.weixin.qq.com/s/isHszbx8pQqfrYoxj-jE9Q
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:42:43.687207
---

# Beatrice.py 源码解读

# Beatrice.py 源码解读

原创

mimi3389
mimi3389

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 仓库地址：https://github.com/raskolnikov90/Beatrice.py
> 分析对象：main 分支 12 次提交，末次 2026-09-11（给 Adaptix 补了一条手工补丁），beatrice.py 单文件 722 行
> 说明：全文结论来自静态阅读源码与 README，未实际对样本打补丁

免杀改二进制的常见路数是加壳、加密 loader、混淆字符串，Beatrice.py 选了条更朴素的路：**文件长度一字节不变，程序功能理论上不变，只把指令替换成编码不同但语义等价的其他指令**，让 YARA 规则和杀软的静态字节签名对不上号。工具 2026 年开源，Python 单文件，依赖只有三个：Capstone 反汇编、Keystone 汇编、pefile 解析 PE。作者用它配合字符串混淆跑通过 Defender 对 Mimikatz 的检测，README 里逐个列了对 Metasploit、Havoc、Sliver、CobaltStrike、Donut 等 payload 的实测结果。

本文是源码级解读，阅读对象是写 YARA 规则的检测工程师和关注免杀技术演进的红队工具维护者。先给一句话结论：**核心思路干净利落——等长、等价、可批量；实现是典型的红队快反原型，性能意识超出同体量脚本的平均水准，但代码卫生粗糙，而且有几处“等价”替换在边界条件下并不等价**。对防御方真正的价值在于：这个工具的输出自带可建模的统计指纹，公开的补丁表等于把规避字典双手奉上。

## 1. 原理总览：三段式流水线

整个工具就是一条流水线，三个引擎各管一段：

```
读取二进制 → ① Capstone 反汇编，采集目标里实际出现的指令和相邻指令对
           → ② Keystone 把模式 × 寄存器全排列编码成机器码，生成 (旧字节 → 新字节) 补丁表
           → ③ Trie 树对整个文件做等长字节替换，共两遍
```

贯穿全程的硬约束是 **新旧编码等长**：新编码更长的补丁一律丢弃，更短的用 NOP 补齐。等长意味着不用重定位、不动 PE 结构、不改变文件布局，这是它能“保功能”的前提，也是它区别于加壳方案的地方——熵值、导入表、文件大小基本原样，变的只有指令字节本身。

## 2. 第一段：反汇编采集，只扫可执行节

入口用两字节魔数 `MZ` 判断 PE，不做更多校验。PE 文件只遍历 `Characteristics` 带 `IMAGE_SCN_MEM_EXECUTE`（0x20000000）标志的节，从 `ImageBase + VirtualAddress` 起做线性扫描；非 PE 一律当作 raw shellcode，基址固定 0x1000。

每条指令过两道筛选。`is_complex()`（`beatrice.py:19`）用关键字过滤单条指令：内存操作数（`ptr`）、SSE 指令（`xmm`）、带立即数的 mov / jcc / add / sub，命中收进候选列表。`find_twoins()`（`beatrice.py:54`）把相邻两条指令拼成字符串，识别三类指令对存进全局列表，供后面专门处理：`mov reg,[mem]` 后跟 `add`、`mov reg, reg` 后跟带立即数指令、`xor reg, reg` 后跟带立即数指令。

这里有个覆盖率缺口值得注意：Capstone 的 `disasm` 生成器遇到解不出的字节会**静默停止**，所以可执行节里嵌了数据的地方，之后的指令全部漏采。对正确性无影响（采集只决定“生成哪些补丁”），但意味着工具对目标的理解是不完整的。

## 3. 第二段：等价替换的批量生成

核心是一张模式表（`beatrice.py:495`），每条模式是“原指令序列 → 等价指令序列”，占位符 `{a}{b}{c}{d}` 用 `itertools.permutations` 对 16 个 x64 通用寄存器做全排列——两个变量 240 种组合，三个变量 3360 种，四个变量 43680 种。每种组合都经 Keystone 编码一次，逐条生成补丁：

| 原指令 | 替换 | 等价性 |
| --- | --- | --- |
| `xor a,a` | `sub a,a` | 置零，编码不同 |
| `mov a,b` | `push b; pop a` | 借栈搬运寄存器 |
| `mov a,b; mov c,d` | `mov a,b; push d; pop c` | 第二条走栈 |
| `lea a,[b+c]` | `lea a,[c+b]` | 操作数交换，SIB 字节不同 |
| `test a,a` | `or a,a` | ZF/SF 一致 |
| `xor a,a; dec a` | `or a,-1` | 置 -1 |
| `cmp a,0` | `test a,a` | 标志位等价 |
| `add a,imm` | `sub a,-imm` | 立即数按 64 位补码取负 |
| `mov r,[rbp-0x10]; add r,rcx` | `mov r,rcx; add r,[rbp-0x10]` | 加法交换律换序 |
| SSE `movdqu` | AVX `vmovdqu` | VEX 前缀，同长度 |

长度对齐的逻辑在 `beatrice.py:314`：新旧编码长度差为奇数补 `0x90`（NOP），偶数补成对 `87 FF`——`xchg edi,edi`，寄存器自交换、无副作用的 2 字节空指令。补完再验等长，不等长（新编码更长）就丢弃。所以 `cmp rax,0` 实际被替换成 `test rax,rax; nop`，4 字节对 4 字节。

另有几组针对采集结果的专门变换：带立即数的 add/sub 互换正负；相邻两条指令中 `mov reg,reg` 换成 `push/pop` 组合并补 NOP、`xor reg,reg` 换成 `sub reg,reg`；内存操作数 `[rbx+rax*1+0x1]` 交换基址与变址寄存器改变 SIB 编码。这些处理全部用字符串切片和下标硬拆操作数（`b[6]`、`b[7]` 定位立即数），是全工具最脆的部分。

性能上倒是做足了：Keystone 编码带全局缓存，寄存器排列按 20 万一组切块丢进 `ProcessPoolExecutor` 多进程并行，还局部绑定了 `append`。单文件脚本里能主动做这些的不多见。

## 4. 关键落差：应用阶段是全文件字节扫描

这是全文最重要的一处实现事实。README 声称“strictly match machine code to avoid breaking binaries”，但看 `patch_binary()`（`beatrice.py:140`）：所有补丁的旧字节建成一棵 Trie，对**整个文件的字节流**逐偏移做贪心左最长匹配替换——不区分节属性，不校验命中位置是否为指令边界。

反汇编在整条链路里的作用只有“决定生成哪些补丁”：目标里出现过 `mov rax,rcx`，就去生成 `mov rax,rcx` 的替换。到了应用阶段，这些字节模式同样会命中数据节、字符串、以及未对齐的指令内部字节。这就是“某些二进制会坏”的根因，也是 `-s` 安全模式存在的原因——安全模式砍掉全部激进变换，只保留 10 条基础模式，还加了一条启发式：编码十六进制里字符 `0` 超过 6 个的补丁直接跳过（太“空”的模式容易大面积误伤数据）。

## 5. 替代编码：同一条 mov 的两副面孔

第二遍处理玩的是编码层面的花样。x86 的 `mov r64, r/m64`（操作码 8B）和 `mov r/m64, r64`（操作码 89）语义相同，编码却不同：操作码一换，ModRM 的 reg 与 r/m 字段对调，REX 前缀里 R/B 两个扩展位的归属也跟着对调。工具预生成全部 16×16 寄存器对的双向编码（`beatrice.py:272`），然后把 `mov`、`xor`、`push/pop`、`div`、`inc` 这些指令的标准编码作为锚点，与方向编码拼接出更多可匹配的字节组合——本质上是：**当一条方向翻转的 mov 恰好出现在另一条已知编码旁边时，把它翻回去**，字节变了，语义没动。

第二遍跑完如果一个补丁都没打上，工具会把全部方向编码对调（`beatrice.py:707`）再生成一遍——8B 转 89 换成 89 转 8B。这个小兜底说明作者意识到两遍补丁之间可能互相抵消。

## 6. 手工补丁表：对已知工具签名的定点爆破

模式之外还有一组硬编码补丁（`beatrice.py:659`），注释直接写明目标：donut、CobaltStrike、Adaptix、Mimikatz。这些就是从公开 YARA 规则里抠出来的签名字节，逐条换成等长变体，代表性几条如下：

| 目标 | 原字节 | 新字节 | 说明 |
| --- | --- | --- | --- |
| Donut | `33 C0 EB 08` | `29 C0 EB 08` | `xor eax,eax` 换 `sub eax,eax`，等价，后两字节为锚 |
| CobaltStrike | `48 89 C2 83 E2 03` | `50 5A 90 83 E2 03` | `mov rdx,rax` 换 `push rax; pop rdx; nop`，等价，末三字节为锚 |
| Mimikatz | `01 00 00 C0 48 85 C9` | `01 00 00 C0 48 09 C9` | `test rcx,rcx` 换 `or rcx,rcx`，标志位等价 |
| Mimikatz | `F3 0F 6F 6C 24 30` | `C5 FA 6F 6C 24 30` | `movdqu` 换 `vmovdqu`，**要求 CPU 支持 AVX** |
| Adaptix | `0F B6 55 12 88 10` | `0F BE 55 12 88 10` | `movzx` 换 `movsx`，**符号扩展，并不等价** |
| Adaptix | `8B 45 FC 01 C2` | `90 03 55 FC 90` | 拆成 `nop; add edx,[rbp-4]; nop`，**丢弃了对 eax 的写入** |

表里加粗的三条引出本节真正的问题——**有几处替换在边界条件下会改变程序行为**：

* `movzx`

  换 `movsx`：零扩展变符号扩展，源操作数高位为 1 时结果直接不同。生成的模式补丁里同样有这条（`beatrice.py:621` 对全部 `movzx word` 生效），命中即改，不看取值范围。
* `mov eax,[rbp-4]; add edx,eax`

  整体换成 `nop; add edx,[rbp-4]; nop`：加法照做，但对 eax 的写入被丢掉了，eax 后续被读时结果直接不同。
* SSE 换 AVX：`vmovdqu` 在 2011 年前的 CPU 上直接 #UD 异常。
* `push a; jmp b`

  换 `push a; push b; ret`：用 ret 实现跳转，控制流等价，但在开启 CET 影子栈（Intel Control-Flow Enforcement Technology）的进程里会因返回地址不匹配直接崩溃。
* 最悬的是两条 Mimikatz 补丁。`24 02 0F 84 00 00 → 24 02 0F 84 00 01` 动的是 `jz rel32` 位移的第二个字节，跳转目标后移 0x100 字节，除非目标处恰好能容忍，否则必然破坏控制流；`05 02 0F 0D 09 → 2D FE F0 F2 F6` 把 `add eax,0x090F0D02` 换成 `sub eax,0xF6F2F0FE`，而 0x090F0D02 的 64 位补码应是 0xF6F0F2FE——**替换立即数中间两个字节写反了**，数学上不等价。这两条大概率命中的是数据区的签名字节（作者对特定二进制手调过、不破坏执行），也再次印证上一节：手工补丁的匹配完全不做代码/数据区分。

## 7. 代码里的 bug 与工程评价

静态阅读能确认的问题不少：

* `beatrice.py:49`

  一处运算符优先级 bug：`if "r" and "d" in op_lower:` 实际等价于 `if "d" in op_lower:`，`"r"` 是恒真常量，过滤条件与字面意图不符。
* `beatrice.py:586`

  一段死代码：新编码比原编码长时，想补 `87 FF` 的循环用 `range(0, 负数)` 起步，循环体永远不执行；即便执行，方向也是反的（往更长的编码上追加）。碰巧无害——后面的等长校验会把这种补丁整个丢弃。
* `beatrice.py:490`

  一句 `complexops[1:]` 无差别丢掉统计出的最高频指令，疑似调试残留。
* 全局可变状态遍布各处，`sys.argv` 在深层函数里被反复扫描（`patch_binary` 里查 `-v`，工作进程里查 `-s`），进程池子进程与命令行耦合。
* 操作数解析全靠字符串下标和前缀比较（`prev.op_str[0:4] == insn.op_str[0:4]` 当作操作数匹配），寄存器名稍长或格式稍变即错位。

总评：**思路是好的，实现是一次性的**。等长约束、Trie 匹配、多进程生成这三个骨架选得都对；但“语义等价”这个立身之本，在实现里既没有指令边界校验兜底，也混进了几条真不等价的替换。README 自己也承认“despite working most of the time some binaries may still break”，`-s` 模式和每次运行必留的 `.bak` 备份，本质上是作者对这些风险的书面承认。

## 8. 防御视角：它的输出自带指纹

这个工具对抗的是纯字节级静态签名，而它自己的输出恰恰布满可建模的特征：

* **统计异常**

  ：正常编译器几乎不会用 `push r; pop r` 搬运寄存器、用 `sub r,r` 置零、成对出现 `87 FF` 填充、用 `or r,-1` 置全 1。对一个二进制做指令分布统计，这几类习语密度异常就是强信号——工具的替换表是公开的，这些习语本身就是新 YARA 规则的素材。
* **成对翻转**

  ：第二遍的方向编码翻转只在已知编码附近生效，产物里会留下“mov 密度高、编码方向成对交替”的局部模式。
* **取证工件**

  ：工具每次运行都在目标旁边留一个 `文件名.bak`，对应急响应是现成的证据——两个文件等长、指令差异集中在已知模式上，直接坐实。
* **它改变不了的东西**

  ：导入表、字符串、熵值、行为。README 对 CobaltStrike“绕过了检测字节但仍然被字符串命中”的记录是诚实的——字符串、IAT 和行为检测都不在这个工具的射程内，字符串和 IAT 混淆被划给了付费 Pro 版。

## 9. 使用方式与边界

```
python3 beatrice.py <binary>
-v  逐条输出补丁偏移与新旧字节
-s  安全模式，只保留 10 条基础模式（手工补丁和替代编码两遍仍会执行）
```

运行后原文件被就地打补丁，旁边生成 `.bak` 备份。README 的实测结论可以概括为：对 Mimikatz（需配合字符串混淆）、Havoc、Donut、Metasploit shellcode 等样本能过 Defender 或 Elastic YARA 规则；Sliver 因 Garble 混淆和符号字符串仍有检出；Garble 混淆的 Golang 二进制可能直接被弄坏。已知问题之外，Pro 版（付费）补齐字符串混淆、IAT 混淆和 .NET 支持——免费版与付费版的分界线，恰好就是本文指出的“这个工具改变不了的东西”。

## 参考资源

* Beatrice.py 仓库：https://github.com/raskolnikov90/Beatrice.py
* 作者修改 Mimikatz 过 Defender 的记录：https://medium.com/@luisgerardomoret\_69654/modifying-mimikatz-to-evade-defender-2026-dc701000289d
* Elastic protections-artifacts：https://github.com/elastic/protections-artifacts
* DefenderYara：https://github.com/roadwy/DefenderYara
* defender2yara：https://github.com/t-tani/defender2yara

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqVN9b7iadOceI5KLl2wzhO4kpqdNoRRMEHV7SbRic7yRUz6yNs73iafib3CAXdnJ9TtiaMOIcGIlFzY3KxFNu5Z8ES7ibkHecxWU5Afk/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过