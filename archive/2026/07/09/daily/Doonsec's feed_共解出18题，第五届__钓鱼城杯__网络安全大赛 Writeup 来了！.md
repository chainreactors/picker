---
title: 共解出18题，第五届\"钓鱼城杯\"网络安全大赛 Writeup 来了！
url: https://mp.weixin.qq.com/s/8OmAy_OZoBNnUnr52OFSBw
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:56:35.108306
---

# 共解出18题，第五届\"钓鱼城杯\"网络安全大赛 Writeup 来了！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JRw8ba1QkAwykmlHoCzIMlgMQ0VT7IEagY6wnHeDKWwKNgJ1jaO5xFpsg2qLxQ9CxqQyzpxrpDG5yIeHUdbeorAweG2zNibdVBibylexEB23g/0?wx_fmt=jpeg)

# 共解出18题，第五届"钓鱼城杯"网络安全大赛 Writeup 来了！

00后反骨崽
00后反骨崽

00后反骨崽

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 从Crypto的数学迷雾到Pwn的栈上刀锋，从Reverse的层层混淆到Misc的天马行空——我们全方向出击，满载而归！

# 📋 赛事总览

第五届"钓鱼城杯"网络安全技能大赛已圆满落幕！本次比赛中，我们战队lanyangyang共确认解出18道题目，覆盖五大方向：

| 方向 | 解题数 | 题目 |
| --- | --- | --- |
| 🔐 Crypto（密码学） | 5 | ntru\_ghost、quadratic\_vine、rational\_echo、syndrome\_shadow、torsion\_weave |
| 🧩 Misc（杂项/取证） | 4 | 八卦、合川斜影、寻找白塔、雀神 |
| 🔧 Reverse（逆向工程） | 4 | MazeRunner、OblivionGate、PolyLock、SpiralVM |
| 💥 Pwn（程序漏洞） | 4 | firm\_sync、FlightAnnouncer、NeonDB、shadow\_auction |
| 🌐 Web（网站漏洞） | 1 | Webhook回调链 |

下面按方向逐一分享解题思路，干货满满，建议收藏！👇

# 🔐 Crypto：数学不会骗你，但出题人会

Crypto方向5题全部拿下，涉及格密码、有限域、离散对数、编码理论等多个硬核领域。

## 1. ntru\_ghost —— 环上求逆，秒杀！

核心思路：把负循环卷积建模为 F₆₅₅₃₇[x]/(x⁷⁰+1) 上的乘法。

题目给出的 a 是随机向量，几乎总是可逆的，所以根本不需要枚举 14¹⁰ 的路径，直接在环上求逆就能恢复稀疏秘密向量 s：

将 u、v 转成多项式

在 x⁷⁰+1 模下求 a 的逆元

计算 s = v · a⁻¹

每7个系数一组，找唯一非零项，还原位置和符号

> 💡 **心得**：看到"负循环卷积"不要怕，换到多项式环的视角，问题瞬间降维。

Flag：flag{888a66cd-0ee8-4f01-a26b-12c4d4019cf6}

## 2. quadratic\_vine —— RANSAC 也能打CTF？

核心思路：65维单项式向量 + 模线性方程组 + RANSAC 过滤脏数据。

服务端给出 78 条正确方程 + 4 条脏方程，还有 box = seal(x)。解题关键是：

随机抽 65 条方程做模高斯消元

如果恰好全抽到正确方程，就能恢复真实解

用全部 82 条验证，只有恰好 78 条通过的才是真解

取前 10 个分量得到 x，逆向 seal(x) 解出 flag

这就是经典的RANSAC 思路——坏方程只有 4 条，随机抽样跑几千次很快就能撞到全对样本。

> 💡 **心得**：RANSAC 不只属于计算机视觉，在带噪声的代数问题里同样好使。

Flag：flag{afd9d0d7-77e1-4dbf-9581-64b26452e4bc}

## 3. rational\_echo —— 有理函数版 Berlekamp-Welch

核心思路：带错误点的有理函数采样恢复。

题目给了分子 13 次、分母 12 次的有理函数，68 个正确点 + 30 个噪声点。

设 U(x) 为分子、D(x) 为分母、E(x) 为错误定位多项式（≤30次），构造：

Q(x) = U(x)·E(x)，次数 ≤ 43

R(x) = D(x)·E(x)，次数 ≤ 42

对所有采样点都有 Q(xᵢ) = yᵢ·R(xᵢ)，直接变成线性方程组求解！

解出 Q、R 后求 gcd 得到 E，约掉公因子恢复 U、D，最终解 box 拿 flag。

> 💡 **心得**：Berlekamp-Welch 不只是 Reed-Solomon 的专利，有理函数一样能玩。

Flag：flag{31a290cc-be88-4f23-ab2f-33ec3c0be5f6}

## 4. syndrome\_shadow —— 哈希约束 + MITM 搜索

核心思路：先定位每组的 goodmark，再用 Meet-in-the-Middle 做异或匹配。

140 列、72 行二进制矩阵，7 组各选 2 列，目标是 14 列异或后的 shadow。

第一层：对每组枚举 C(20,2)=190 个列对，计算 goodmark 和完整的 6 元 bag，递归搜索使 bag 与题目 noise 完全匹配，将候选从 190 压缩到个位数。

第二层：7 组拆成 3+4 做 MITM——左边 3 组枚举异或结果存哈希表，右边 4 组查找 need = target ^ right\_xor，命中即得完整 14 列路径。

> 💡 **心得**：两层剪枝是关键——先靠哈希约束缩小范围，再用 MITM 暴力匹配，思路清晰就不难。

Flag：flag{c052d754-85c7-4171-8763-cd871007875c}

## 5. torsion\_weave —— 离散对数 + CRT 组合拳

核心思路：每条通道独立枚举离散对数，再组合 CRT 还原 x。

18 条通道中有 9 条真通道满足 b = a^(x mod w) mod m，模数 w 只有 5 万级，可以直接暴力枚举。

解题步骤：

对每条通道暴力枚举指数 e（w ≈ 5万，很轻松）

枚举 C(18,9) = 48620 个子集，对每个子集做增量 CRT

用候选 x 解 box，检查明文是否为 flag{...} 格式

只要子集正好命中 9 条真通道，解出来的明文就会变成合法 flag。

> 💡 **心得**：不需要先区分真假通道，直接穷举组合 + CRT + 验证，暴力美学！

Flag：flag{dac00856-f156-4d23-bf1d-0e37fe5c91d0}

# 🔧 Reverse：看不见的才是最危险的

## 6. MazeRunner —— 迷宫里的逆向

题目要求对迷宫路径进行逆向分析，通过静态分析和动态调试相结合，还原出正确的行走路径。

Flag：已确认提交 ✅

## 7. OblivionGate —— 遗忘之门

复杂的程序逻辑需要逐层剥离，通过IDA反编译和动态调试，找到关键的验证逻辑并还原算法。

Flag：已确认提交 ✅

## 8. PolyLock —— 多态锁

多层变换和保护机制，需要耐心逐层拆解，每层都有独特的混淆手法。

Flag：已确认提交 ✅

## 9. SpiralVM —— 螺旋虚拟机

虚拟机保护的逆向分析，需要理解自定义指令集和执行引擎，还原虚拟指令到真实逻辑。

Flag：已确认提交 ✅

# 💥 Pwn：栈上刀锋，毫厘之间

Pwn 方向 4 题全部拿下！从 shellcode 注入到 tcache poisoning，从格式化字符串到 FSOP，每种利用手法都是经典中的经典。

## 10. firm\_sync —— 协议解析里的栈溢出

核心漏洞：长度检查只比较低 8 位，但 memcpy 用完整 16 位长度！

cmp [rbp+var\_1], 0x60 ← 只检查低8位

call \_memcpy ← 用的是完整长度

当 len = 0x100/0x200 且 len & 0xff <= 0x60 时，就能稳定覆盖 RIP。

利用链：

tag=7 泄露返回地址 → 恢复 PIE 基址

第二次 tag=7 泄露 puts 地址 → 恢复 libc 基址

tag=1 写入 /flag 到 .data 段

tag=3 触发栈溢出 → ORW：openat → read → write

> 💡 **心得**：`cmp` 只比低 8 位这种低级错误，在嵌入式/固件场景里真的很常见。

Flag：flag{493ab9a3-4bb1-4139-8a82-8d698e9a4a6d}

## 11. FlightAnnouncer —— 格式化字符串 + 两段式栈迁移

核心思路：先格式化字符串泄露全套地址，再栈溢出做两段式栈迁移到 .bss 执行 ORW。

关键发现：

%23$p

→ 当前 rbp（直接算出缓冲区精确地址）

%25$p

→ main 返回地址（恢复 PIE）

%29$p

→ canary

%35$p

→ libc 基址

seccomp 白名单只放行 openat/read/write，方向锁死为 ORW。

由于栈空间不够放完整链，采用两段式：

第一次 leave;ret 迁移到溢出的 v2，只做 read(0, .bss, 0x400)

第二次 leave;ret 迁移到 .bss，执行完整 ORW

> 💡 **心得**：小栈溢出不够放完整链？别硬塞！先 read 一段更大的第二阶段到可写段，再迁移过去执行。

Flag：flag{82dc0721-0229-47e8-a290-8a89aae113ac}

## 12. NeonDB —— UAF + tcache poisoning 的艺术

核心漏洞：过期页只 free 不清空指针，读写接口不检查活跃标志 → 稳定 UAF read/write。

利用链：

从页尾 footer 泄露控制页地址、回调函数地址、PIE 基址

两个同尺寸 free chunk 绕过 safe-link，完成 tcache poisoning

分配重定向到控制页，伪造 callback（指向现成的 openat/read/write 函数）、path = "/flag"、校验值

触发结算逻辑 → 命中隐藏回调 → flag 输出

> 💡 **心得**：free 不清指针 = 白送利用原语。这题的 footer 主动泄露地址更是贴心到家。

Flag：flag{13e051ef-2d9e-4627-88a3-22a8598916b3}

## 13. shadow\_auction —— 格式化字符串 + %hn 精准写入

核心思路：格式化字符串模板和 8 个审计参数均可控，同时完成地址泄露和 halfword 任意写。

利用链：

模板泄露返回地址 → PIE 基址

%1$.8s

读取堆对象指针 → 结算对象地址

重算合法 checksum（rol64 + fnv1a）

用 8 个 %m$hn 一次性改写：回调指针 → 隐藏读文件函数、路径 → "/flag"、校验值 → 新合法值

触发结算 → 命中隐藏 openat/read/write 回调

> 💡 **心得**：`%hn` 半字写比 `%n` 全字写更精准可控，配合 checksum 重算绕过完整性保护。

Flag：flag{4b0fda81-c693-4610-93c0-949bff790a51}

# 🌐 Web：信息收集是门手艺活

## 14. Webhook回调链

Web 方向虽然只解出 1 题，但含金量十足。通过深入的信息收集和 Webhook 回调链分析，找到关键突破口。

Flag：已确认提交 ✅

# 🧩 Misc：万物皆可取证

## 15. 八卦 —— 六十四卦的 Base64

核心思路：8×8 卦象矩阵 → 爻线识别 → Base64 解码。

将图片按 8×8 网格切出 64 个卦象，识别每格六条爻线（实线=1，断线=0），自下而上读取组成 6-bit 值，64 个值正好映射到 Base64 字母表。

> 💡 **心得**：看到卦象就想到二进制，看到 64 就想到 Base64，CTF 的直觉很重要！

Flag：flag{Y1Jing\_8x8\_WHT\_64\_Gua\_GF2\_Hadamard\_Misc\_CT}

## 16. 合川斜影 —— 地理定位挑战

从桥梁外观和城市环境入手，锁定合川嘉陵江南屏大桥，在 Google Earth 坐标体系下收敛到斜拉结构中心对称点。

Flag：flag{2958591061653}

## 17. 寻找白塔

通过图片分析和地理信息定位，找到目标建筑的精确位置。

Flag：已确认提交 ✅

## 18. 雀神 —— 麻将里的密码学

将麻将规则与密码学结合，需要理解牌面编码和验证逻辑。

Flag：已确认提交 ✅

# 📊 赛后总结

## 技术栈全景

本次比赛涉及的核心技术点：

| 类别 | 技术点 |
| --- | --- |
| 数学 | 环上多项式求逆、Coppersmith 小根攻击、Wiener 攻击、CRT、Berlekamp-Welch、RANSAC |
| 逆向 | Android 签名验证、PE 文件修复、虚拟机逆向、驱动 IOCTL 分析 |
| Pwn | Shellcode 注入、格式化字符串、UAF、tcache poisoning、FSOP、栈迁移、ORW、safe-link 绕过 |
| 取证 | RAID5 降级恢复、DNS 流量分析、NTFS 模板填充、词向量类比、地理定位 |
| Web | 信息收集、Webhook 回调链 |

## 经验与感悟

Crypto 靠数学直觉

：很多题看似复杂，但换一个数学视角就能降维打击

Pwn 靠细节把控

：1 字节的长度检查漏洞、free 后不清指针，都是经典突破口

Reverse 靠耐心

：层层混淆不要慌，从入口开始一步步剥洋葱

Misc 靠脑洞

：卦象→二进制→Base64、阿拉伯语→GBK乱码→词向量，跨领域联想是王道

Web 靠信息收集

：很多时候突破口就藏在不起眼的注释和文档里

从一无所知到长城杯线下，从 babygame 到 解出18 题——这条路走得很值。

需要完整wp的可以进Q群自取或者私信我

我们下一场比赛再见！🚀

本文由 lanyangyang 赛后整理

懒羊羊大王出品

QQ群：1051436928

![](https://mmbiz.qpic.cn/mmbiz_png/JRw8ba1QkAyWTwS7zAgLORpqDEF0ezVgNFWJZZzHvIaA9GhTwfqiawSudRQNn4R5J5aeaicaYicQKvFQWextk3BzF6uZDFqKo7ZDUWibbxJ7xNo/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JRw8ba1QkAyLaO7jbGn1micB35COoXcRibmHnX88t5OF2rgjK2lGzoyQLUiao99b5CNQ8n639PFAGicoBia82RXK4ZZaZUaJAJg2fWiayktHaF7Gg/0?wx_fmt=png)

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