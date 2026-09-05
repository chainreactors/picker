---
title: 2026年“中国（广西）—东盟人工智能安全攻防决赛（赛道一）
url: https://mp.weixin.qq.com/s/Hvv-GRkxxCke2G-CdMtlPg
source: Doonsec's feed
date: 2026-09-04
fetch_date: 2026-09-05T06:27:40.060159
---

# 2026年“中国（广西）—东盟人工智能安全攻防决赛（赛道一）

# 2026年“中国（广西）—东盟人工智能安全攻防决赛（赛道一）

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于0xNyx
，作者識.

![](https://wx.qlogo.cn/mmhead/OUicWJdJoz3GibGSccEEagSTlcv35unKiad08sI2kibx9mvFvNzzVpD6SFma3ykic6VTjQugKv6aRc4U/0)

**0xNyx**

Neuro Token VM

*Writeup: reverse the drifting token routing table an*

*d recover the one-token input*

题目给出的附件只有一个 `neuro\_token\_vm.exe`。程序运行后会显示 `Neuro Token VM`、`loading tiny-bpe.q4 checkpoint...` 和 `prompt token> `，表面上像是一个简单的 token 校验器，但实际更像是一个被包装成“神经网络 checkpoint”的小型虚拟机。最终目标并不是猜一个普通字符串，而是恢复唯一能让程序进入 `accepted: logits aligned` 分支的输入。

**一、样本概览**

我先做了静态检查：这是一个 64 位 PE，导入表很干净，没有明显壳或者运行时自解密痕迹。可见字符串直接暴露了题目语境，尤其是 `flag{`、`accepted: logits aligned` 和 `rejected: token drift detected` 这几句，说明它已经把成功/失败分支写死在程序内部。

|  |  |
| --- | --- |
| **项** | **内容** |
| 文件 | neuro\_token\_vm.exe |
| 架构 | x64 PE |
| 核心提示 | Neuro Token VM / tiny-bpe.q4 / prompt token |
| 结果分支 | accepted: logits aligned / rejected: token drift detected |

**二、关键字符串与入口**

在 `.rdata` 中可以直接看到几个关键字符串，程序的流程也很清楚：先打印标题，再打印 checkpoint 加载信息，然后提示输入一个 token。反汇编里入口附近的字符串引用分别落在 0x140002a04、0x140002a10、0x140002a1c 这一段。

l 0x140004000: `Neuro Token VM`

l 0x140004010: `loading tiny-bpe.q4 checkpoint...`

l 0x140004032: `prompt token> `

l 0x14000404a: `accepted: logits aligned`

l 0x140004068: `rejected: token drift detected`

输入读取之后，程序会先检查长度是否为 0x2a，也就是 42 字符。紧接着它又检查前缀 `flag{` 和结尾 `}`，因此输入外壳已经被固定成标准 UUID 格式：`flag{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}`。也就是说，真正需要恢复的是中间 36 个字符。

**三、主校验逻辑**

核心校验从 0x140002aa4 之后开始。程序先对输入中的每个字符做分类：数字 `0-9`、小写 `a-f`、以及 4 个连字符位置都被纳入约束。这里最关键的一步是下面这条映射：

`v = ((13 \* i - 0x59) & 0xff) ^ table[i]`

这条式子会把 `.rdata` 中的一张 256 字节表映射成一串 opcode。整个表里最有意义的三种值是 `0x10`、`0x20`、`0x30`，它们分别驱动三种状态分支。换句话说，这不是“查表比对”，而是把输入拆成若干个 4-bit 片段后，塞进一个自定义的状态机里跑。

|  |  |
| --- | --- |
| **地址 / 现象** | **含义** |
| 0x140002a72 | 输入长度必须等于 42 |
| 0x140002a7c | 前缀必须是 `flag{` |
| 0x140002a99 | 最后一个字符必须是 `}` |
| 0x140002ab0 | 进入 opcode 状态机 |

**四、状态机拆解**

我把 0x140002ab0 到 0x140002c54 这一段按控制流拆开后，可以把它理解成“每 5 个输入字符处理一轮”的循环。每轮会先读一个索引位，再读 4 个十六进制字符，拼成一个 16 位值，最后和前一轮状态一起参与模运算。

这里有两个特别重要的点：

l 遇到 `0x10` 时，程序在检查一个字符是否为 `-`。

l 遇到 `0x20` 时，它会把字符映射成 0-15 的十六进制 nibble。

l 遇到 `0x30` 时，它会拼接两个 nibble，并和一个 16 位状态值比较。

这个结构非常像“routing table drift”题面的说法：表面是 token routing，实际是在按固定规则把字符路由成状态。只要把 opcode 序列还原出来，输入就能被一段段解开。

**五、表数据与方程**

我从 `.rdata` 中提取出了 256 字节的路由表，并对每个位置计算 `v = ((13\*i - 0x59) & 0xff) ^ table[i]`。这样就能得到每个索引对应的 opcode。之后把每一轮中出现的 4 个十六进制字符记为 `a1, a2, a3, a4`，把轮间状态记为 `prev`，就可以写出

`a2 \* s ≡ W - a4 \* prev - a3 - a1 \* idx (mod 65521)`

其中 `W` 是那一轮拼出来的 16 位比较值，`idx` 是前导索引 nibble，`s` 是该轮最终状态。因为模数 65521 是素数，大多数轮次都能直接求逆并解出状态。

|  |  |  |  |
| --- | --- | --- | --- |
| **轮次** | **idx** | **W** | **解出的状态** |
| 0 | 0 | 0x2eae | 15 |
| 1 | 1 | 0xdeec | 5 |
| 2 | 2 | 0x3cad | 8 |
| 3 | 3 | 0xe3e7 | 5 |

完整跑完 36 轮以后，36 个 nibble 序列会稳定落到一个标准 UUID。把连字符补回去之后，得到的中间串是：

`f585dc57-9657-4591-9bbb-14b05ffd868e`

**六、验证**

我把最终输入回喂给程序，程序返回了 `accepted: logits aligned`，说明解出来的 token 是正确的。完整 flag 为：

`flag{f585dc57-9657-4591-9bbb-14b05ffd868e}`

Route

|  |  |
| --- | --- |
| **题目** | A company got an ONNX model |
| **目标** | 从 ONNX 模型中恢复隐藏的 UUID flag |
| **模型输入** | session\_vector: int64[42] |
| **最终状态** | 已通过 ONNX ReferenceEvaluator 验证 |

|  |
| --- |
| **最终 Flag**flag{beda4910-1e3f-446a-92be-472c5dbda8ab} |

# **1. 题目与目标**

题目给出一个 challenge.onnx 文件。模型表面上接收一个长度为 42 的整数向量，并输出一个名为 audit\_score 的浮点数。目标不是训练模型，而是逆向其计算图，构造能够使检查逻辑通过的输入，并从中恢复隐藏的 UUID flag。

模型文件位于题目目录中的 challenge.onnx。分析时使用 ONNX 的图结构、initializer 常量以及 ReferenceEvaluator 进行最终复核。

# **2. 初步分析：输入格式被直接编码**

读取 graph.input、graph.output 和 initializer 后，可以看到模型包含 42 个输入字节以及多组命名为 q00 到 q21 的常量。最先有价值的是 q04 和 q05：

q04 = [0, 1, 2, 3, 4, 13, 18, 23, 28, 41]

q05 = [102, 108, 97, 103, 123, 45, 45, 45, 45, 125]

把 q05 转成 ASCII 后正好是 f、l、a、g、{、-、-、-、-、}。因此输入向量的固定位置为：

v[0:5] = b"flag{";  v[13] = v[18] = v[23] = v[28] = ord('-');  v[41] = ord('}')

q03 则列出剩余 32 个位置：[5..12]、[14..17]、[19..22]、[24..27]、[29..40]。这些位置正好对应 UUID 中的 32 个十六进制字符。

l 固定位置负责识别 flag{...} 的外层格式。

l 非固定位置必须是 ASCII 数字 0-9 或小写字母 a-f。

l 经过 Where 节点后，ASCII 十六进制字符被转换成 0 到 15 的 nibble。

# **3. 找到正确的约束行**

图中首先对固定位置做 Equal 检查，然后将结果与 q06、q07 组合，经过模 251、求和，再对 q02=7 取模。该值是后续 7 组候选约束的行选择器。使用 q05 对应的固定字节计算后，选择结果为 row = 6。

row = sum(((q05 \* q06 + q07) % 251)) % 7 = 6

q08、q09、q10、q11、q12、q13、q14 都是按行组织的常量：q08 的形状为 (7, 96, 4)，q09/q10 的形状为 (7, 96, 11)，q11-q14 的形状为 (7, 96)。因此只需要取第 6 行的 96 条约束。

# **4. 还原非线性模约束**

对于第 j 条约束，先定义四个变量索引：

ids = q08[6][j] % 32

系数和目标值分别为：

d[j] = (q09[6][j] - q10[6][j]) % 251

t[j] = (q11[6][j] + q12[6][j] \* q13[6][j] + q14[6][j]) % 251

结合图中 Gather、Mul、Add 节点，可以将约束写成如下形式。令 x0...x31 为 32 个 nibble，每个变量范围为 0 到 15：

s\_j = d0\*x0 + d1\*x1 + d2\*x2 + d3\*x3
    + d4\*x0\*x1 + d5\*x1\*x2 + d6\*x2\*x3
    + d7\*x0^2 + d8\*x3^2 + d9\*x0\*x2 + d10
s\_j mod 251 = t\_j

这里的 x0、x1、x2、x3 表示由 ids 选出的变量，而不是固定的前四个变量。特别要注意：Gather\_17 对 d[j][10] 的结果是直接 Add 到表达式中的，因此第 11 个系数是常数项，不应误写成 d10\*x3。

# **5. 使用 CP-SAT 求解**

这是一个带有二次项和模约束的有限域搜索问题。为避免手工处理 32 个十六进制变量，使用 OR-Tools CP-SAT 建模。每个乘积项建立一个辅助变量，并用 AddMultiplicationEquality 连接；模运算改写成整数等式：

expr\_j - t\_j = 251 \* k\_j

k\_j 是整数商变量。第一次尝试时将 k\_j 的范围设置得过小，求解器会错误地报告 infeasible，这也是得到错误答案的根因。修正为足够宽的范围后，96 条约束可以同时满足。

1. 建立 x[0..31]，每个变量域为 [0, 15]。

2. 根据 row=6 读取 q08 和 d/t 数组。

3. 为所有出现的二次项建立乘积辅助变量。

4. 将每条模 251 约束改写为 expr - target = 251\*k。

5. 读取求解器返回的 32 个 nibble，并按十六进制输出。

hex\_string = beda49101e3f446a92be472c5dbda8ab

# **6. 构造完整输入并验证**

将求出的十六进制字符串重新编码为 ASCII，并填入 q03 指定的 32 个位置；其余位置按 q04/q05 填入固定字节。输入向量满足格式：

flag{beda4910-1e3f-446a-92be-472c5dbda8ab

最后使用 onnx.reference.ReferenceEvaluator 执行原始模型，而不是只验证独立的约束脚本。模型输出为：

|  |
| --- |
|  |

|  |
| --- |
|  |

# **7****. 最终答案**

|  |
| --- |
|  |

|  |
| --- |
|  |

|  |
| --- |
| **Flag**flag{beda4910-1e3f-446a-92be-472c5dbda8ab} |

**Noisy Digits**

|  |
| --- |
|  |

|  |
| --- |
|  |

|  |  |
| --- | --- |
| **容器地址** | nc 60.205.220.63 22536 |
| **附件** | check.py、modelofmnist.pth、mnist\_label\_1\_noisy.png |
| **最终结果** | flag{fc493ea5-82a5-4736-9f14-9027687e1e3f} |

# **1. 题目概述**

本题给出一个 MNIST 手写数字识别模型，以及一张在传输过程中被加入盐椒噪声的攻击目标图。服务端要求提交一张 base64 编码的 PNG 图片：它需要与服务端保存的原始数字 1 图片保持足够高的 SSIM 相似度，同时让模型以较高置信度把它分类为数字 9。

l 相似度约束：SSIM >= 0.65。

l 分类约束：softmax 最大置信度 > 0.75。

l 目标类别：max\_indices == 9。

# **2. 附件分析**

|  |
| --- |
|  |

|  |
| --- |
|  |

|  |  |
| --- | --- |
| **check.py** | 服务端判题逻辑，包含模型结构、输入处理、SSIM 判断和 flag 输出条件。 |
| **modelofmnist.pth** | 卷积神经网络权重，结构为两层卷积 + 池化 + 两层全连接。 |
| **mnist\_label\_1\_noisy.png** | 28x28 灰度图，原始数字为 1，但第 13 行和第 25 行被明显白色噪声污染。 |

|  |
| --- |
|  |

|  |
| --- |
|  |

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

# **3. 判题逻辑还原**

核心判题逻辑可以概括为：先将提交的 base64 解码成图片，再计算其与原始图片的 SSIM，最后用 MNIST 模型分类。只有同时满足三项条件才读取 flag。

|  |
| --- |
|  |

|  |
| --- |
| ssimvalue = ssim(ten\_attack, ten\_image) output = torch.softmax(model(input\_batch), dim=1) max\_probs, max\_indices = torch.max(output, dim=1)  if ssimvalue >= 0.65 and max\_probs.item() > 0.75 and max\_indices.item() == 9:     print(flag) |

# **4. 解题思路**

噪声图本身会被模型预测为 8，而去掉两条全白噪声行后会被预测为 1。由于题目要求目标类别为 9，直接提交修复图无法过关，需要构造目标对抗样本。

6. 先读取 28x28 噪声图，观察像素矩阵，确认全白行属于盐椒噪声。

7. 将第 13 行、第 25 行置零，得到一个更接近原始数字 1 的参考图。

8. 加载本地模型权重，复现服务端 CNN 的前向推理流程。

9. 以修复图为起点，使用目标攻击优化图片，使 cross entropy 指向类别 9。

10. 在损失函数中加入 SSIM 约束，避免图片偏离原始数字 1 太远。

11. 把最终 PNG 转为 base64，发送到 nc 服务。

# **5. 对抗样本生成**

实际使用的优化目标如下：分类损失推动模型输出 9，相似度项限制图像不要远离参考图。最终候选样本在本地模型上预测为 9，目标类别概率约为 0.996，并且与修复参考图的 SSIM 约为 0.779。

|  |
| --- |
|  |

|  |
| --- |
|  |

|  |
| --- |
| var = start.clone().detach().requires\_grad\_(True) opt = torch.optim.Adam([var], lr=0.02)  for i in range(2600):     opt.zero\_grad()     x = var.clamp(0, 1)     logits = model(x)     ce = F.cross\_entropy(logits, torch.tensor([9]))     sim = ssim(x, reference)     l2 = (x - reference).pow(2).mean()     loss = ce + 10.0 \* F.relu(torch.tensor(0.76) - sim).pow(2) + 1.2 \* l2     loss.backward()     opt.step()     var.data.clamp\_(0, 1) |

# **6. 提交与结果**

生成 PNG 后，将其转为 base64 并直接发送到服务端。服务端执行 check.py 后返回 flag

|  |...