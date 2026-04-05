---
title: X-Perseus AI初窥
url: https://mp.weixin.qq.com/s/Aipz7r6y0SkI3qHiuwgSKg
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:39.603989
---

# X-Perseus AI初窥

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K00EyvEc5HycEvgr3AqAURB90fLmo8icIX9siaffGSBUlMoUwpzVglw6EZIARzlSmzPKBQMUDhApJYXGpiaJdPw5VlOxVATCVT62w/0?wx_fmt=jpeg)

# X-Perseus AI初窥

Tubbs
Tubbs

看雪学苑

![]()

在小说阅读器中沉浸阅读

**说明**

* # 输入一个unidbg trace日志
* codex + gpt5.4 xhigh
* AI发现一个算法或者是一个规律的时候按照之前计算经验引导测试，所有中间脚本都是模型写的，并且没有保存，只有遇到算法的时生成等效python函数
* 分析不完整，缺失很多流程和细节，但是AI处理和分析之后确实可以很快和之前的经验对照上。

##

**目的**

这个文档用于按时间顺序记录`X-Perseus`的逆向过程。

##

**Trace 日志到 DuckDB 的结构说明**

当前分析不是直接对原始 trace 文本逐行做，而是先把执行日志转换进 DuckDB，再围绕统一的`step`号做联查。

这里最重要的三张表是：

| 表名 | 作用 | 关键字段 | 说明 |
| --- | --- | --- | --- |
| `instructions` | 指令主表 | `step` ,`address`,`offset`,`instruction`,`semantic` | 每个`step`对应一条执行指令 |
| `registers` | 寄存器快照表 | `step` ,`reg_name`,`reg_value`,`timing` | 同一`step`下会记录执行前后的寄存器值，`timing`分为`before/after` |
| `memory` | 内存访问表 | `step` ,`mem_addr`,`mem_value`,`mem_type`,`size` | 记录该`step`触发的读写内存行为 |

三张表之间的关系非常简单：

```
instructions.step = registers.step = memory.step
```

所以后文里反复出现的分析方式，本质上都是：

* 先锁定某个关键`step`
* 再同时查看该步对应的指令、寄存器和内存访问
* 必要时再沿`step`向前或向后回溯

读这份文档时，可以把它理解成下面这个映射：

```
一条原始执行日志
-> 归并成一个全局 step
-> 该 step 下拆成：
     指令信息（instructions）
     寄存器快照（registers）
     内存访问（memory）
```

后文如果提到：

* “某一步调用参数是什么”，通常来自`instructions + registers(before)`
* “某一步最终把什么写进了哪里”，通常来自`instructions + registers(after) + memory`
* “重建某块缓冲区内容”，通常来自按地址范围汇总`memory`表里的历史`write`

还有两个查询习惯需要先说明：

* `offset`

  在 SQL 里建议写成`"offset"`，避免和保留字冲突。
* 很多逆向结论都直接依赖`semantic`字段，因为它已经把寄存器/内存结果解析成了可搜索文本。

##

**时间线**

### Step 1：X-Perseus 参数定位

这一节只记录第一次把`X-Perseus`从最终 7 神输出里准确摘出来，并建立首版拷贝链的过程。此时的目标还不是解释算法，而是先把“字符串在哪、从哪搬过来”这两个问题钉死。

#### 关注点

先在最终输出缓冲区里确认`X-Perseus`参数的准确位置，再建立最早一版“它从哪里拷贝过来”的上游链路。

#### 起点

最开始不是从单独的`X-Perseus`字符串入手，而是先重建最终整块参数输出缓冲区：

```
uv run python scripts/query_trace_db.py mem-reconstruct 13501921 0x40642000 0x40642500 --write-limit 0
```

当时直接确认到的基础信息是：

* 目标地址：`0x40642000`
* 重建 step：`13501921`
* 重建范围：`0x40642000 - 0x40642500`
* 输出性质：不是单独的`X-Perseus`，而是最终拼接好的整块参数输出
* 已见参数头：`X-Argus`、`X-Gorgon`、`X-Helios`、`X-Khronos`、`X-Ladon`、`X-Medusa`、`X-Neptune`、`X-Perseus`
* 重建方法：不能只按“每个起始地址的最新值”恢复，而是要按时间顺序回放覆盖该区间的`write`

当时重建结果里最关键的 hexdump 片段是：

```
40642000  58 2d 41 72 67 75 73 0d 0a 4a 61 57 42 61 51 3d  |X-Argus..JaWBaQ=|
40642010  3d 0d 0a 58 2d 47 6f 72 67 6f 6e 0d 0a 38 34 30  |=..X-Gorgon..840|
...
406421f0  65 70 74 75 6e 65 0d 0a 2d 31 31 7c 35 30 3a 35  |eptune..-11|50:5|
40642200  31 3a 35 39 0d 0a 58 2d 50 65 72 73 65 75 73 0d  |1:59..X-Perseus.|
40642210  0a 4c 70 4c 4c 4c 46 6a 4b 2b 32 4e 6a 63 70 4a  |.LpLLLFjK+2NjcpJ|
```

#### 观察

重建`0x40642000`后，先看到的不是单独一个参数，而是一整块已经拼接好的最终输出，其中包含：

* `X-Argus`
* `X-Gorgon`
* `X-Helios`
* `X-Khronos`
* `X-Ladon`
* `X-Medusa`
* `X-Neptune`
* `X-Perseus`

在这块总输出里，`X-Perseus`的定位结果是：

* 参数头起始地址：`0x40642206`
* 参数值起始地址：`0x40642211`
* 参数值结束地址：`0x406424f4`
* 参数值长度：`740`字节

当时摘出的`X-Perseus`区间 hexdump 开头是：

```
40642200  31 3a 35 39 0d 0a 58 2d 50 65 72 73 65 75 73 0d  |1:59..X-Perseus.|
40642210  0a 4c 70 4c 4c 4c 46 6a 4b 2b 32 4e 6a 63 70 4a  |.LpLLLFjK+2NjcpJ|
40642220  71 4c 4f 53 31 48 6c 49 6f 72 41 75 44 6f 66 57  |qLOS1HlIorAuDofW|
40642230  71 31 61 4c 2f 70 6f 51 53 49 34 73 2b 74 66 2b  |q1aL/poQSI4s+tf+|
```

并且当时已经直接得到完整参数值：

```
LpLLLFjK+2NjcpJqLOS1HlIorAuDofWq1aL/poQSI4s+tf+gq+8Mbb+vUoDRJ3Fs7W5ZQ3aXT9zqBzHC84DhCMkAJn5iCQuiEZvDPZbtlwHPuOPXZBoqAs1jHOfpEMXZ+oC0tJZu6PBrgVonka6qZk5ZL0rmJiHRMmUKNTdXU4898AC5squ6Vscm4QzITlCH1LVRpLZk4NbK+Vkm615gppA3I0Xy0I3joroLsPFXO2ynGAzdUflnSFWgEv5PJTzXbgnHmlI6C5fi8yrdbPOpWxU4ftBXoH8AVx6yIuRWqW7OBR9qq1K2XKbxM0iDMKd0KafUxooDPFm8EcaLzV0WlVSqqA2JqjTRTL08j0bqHRom54563/64EDxopjfE/48sXCuSrFOBAjYLKF5BaoXgLcqQHrrxWCYafdwlY6GgUKSFe3rnD0aOHxN2RY5qD2ZGAs7Kuy1xbNBiJxrI3wRiKugx+m97izex/zlBwVQjtg5/NPtJWY6t0Tu9XG3/Bq+Liz32oKIv9PUOphulUEjbrfYy9Lhlcs1l6Ik91rFnURmhIMuqBvdZDnRCVknREVppeY44lVIlI2ISk/ldrgstpD/1MvhmbNXBXF3p3d7af79f+yq3FXjVI16C3l+D1/nKeRRjmdBdg8ZXayXk9kcreGqP72fGGNcfmxaAgMCsUZgnGgGGgAlBPGI94BXBKeXEIrHny5nHNgD/y7okXwIyCOqSW3H0xfUdsX8=
```

#### 猜测

在完成最终输出定位后，最早的直觉是：

* `0x40642000只是最后的总输出缓冲区。`
* `X-Perseus很可能先在某个中间缓冲区里生成，再被拼接/拷贝进总输出。`
* `0x40642206这个偏移很关键，因为它正好是X-Perseus在最终大缓冲区中的起始位置。`

基于这个偏移，最早建立的链路猜测是：

* 整块输出来自`0x408be000`
* `X-Perseus`

  子区间来自`0x40625800`
* 更前面还会有一个与算法主体相关的源块`0x40624400`

#### 验证

随后沿着`0x40642000`逆着 trace 看调用参数和内存流向，做了三类验证。

第一类是整块最终拷贝：

* `step 13501708`
* 调用参数：`x0 = 0x40642000`，`x1 = 0x408be000`，`x2 = 0x4f7`
* 说明整块最终参数输出是从`0x408be000`拷贝到`0x40642000`

第二类是子区间偏移验证：

* `step 13501424`
* 调用参数：`x0 = 0x408be206`，`x1 = 0x40625800`，`x2 = 0x2f1`
* 因为`0x206`正好等于`X-Perseus`在最终大缓冲区中的起始偏移，所以最早就把`0x40625800 -> 0x408be206`识别成`X-Perseus`子区间搬运链

第三类是前缀源块验证：

* `step 13501392`
* 调用参数：`x0 = 0x408be000`，`x1 = 0x40624400`，`x2 = 0x206`
* 这一步把`0x40624400`和最终拼接缓冲区的前缀区联系起来

同时又用`mem-trace`做了交叉验证：

* `0x40642000 <- 0x408be000`
* `0x40642210 <- 0x408be210`
* `0x406424e7 <- 0x408be4e7`

当时按 trace 得到的最早版拷贝链证据是：

```
step 13501708:
  x0 = 0x40642000
  x1 = 0x408be000
  x2 = 0x4f7

step 13501392:
  x0 = 0x408be000
  x1 = 0x40624400
  x2 = 0x206

step 13501424:
  x0 = 0x408be206
  x1 = 0x40625800
  x2 = 0x2f1
```

这里`0x206`很关键，因为：

* `0x40642000 + 0x206 = 0x40642206`
* `0x408be000 + 0x206 = 0x408be206`

也就是说，最开始就是用这个偏移把`X-Perseus`在最终输出里的位置，和`0x408be206`这段子区间连起来的。

#### 结果

到这一步，最早稳定下来的定位结果有两部分。

第一部分是参数定位本身：

* 已确认`X-Perseus`在最终总输出缓冲区中的准确范围
* 已确认它不是独立缓冲区，而是整块参数输出中的一个子区间

第二部分是最初版本的上游链路：

```
0x40624400 --(0x206 bytes)--> 0x408be000
0x40625800 --(0x2f1 bytes)--> 0x408be206
0x408be000 --(0x4f7 bytes)--> 0x40642000
```

这一步虽然还没进入算法细节，但已经完成了两个关键工作：

* 把`X-Perseus`从整块输出里准确摘出来
* 给后续逆向明确了最早的追踪方向

#### 修正

这一步后面有一个重要修正。

最初我们一度把`0x40625800`看得太“靠前”了，像是在把它当作`X-Perseus`的主要上游结果区。

但后续用户补充并确认：

* 真正更早的成品字符串区是`0x40624c00`

这带来两个修正：

* 前面建立的`0x40642000 <- 0x408be000 <- 0x40625800`这条链并没有错，但它只是**后段搬运/拼接链**，不是最早的成品生成链。
* `0x40625800、0x408be206、0x408be000更像中间缓冲区；真正应该优先继续追的是：`

```
0x40624c00 ->0x40625800 / 0x408be206 / 0x40642000
```

这个修正当时依赖的关键事实是：

* 用户确认的更前一步地址：`0x40624c00`
* 在`step 13433848`重建`0x40624c00`可以直接得到完整`X-Perseus`字符串
* `step 13500742调用时，已经把x1 = 0x40624c00传给外部函数，参数为：`

```
step 13500742:
  x0 = 0x4062540b
  x1 = 0x40624c00
  x2 = 0x2e4
  target = 0x40281600 -> br x17 ->0x4046c300
```

也正是因为这一段外部函数体没有被当前 trace 展开，所以当时出现了一个重要方法论修正：

* 不能把`0x40625800`当成最早成品区
* 遇到`bl -> 跳板 -> br x17`这类外部路径时，不能只靠内存溯源结果本身，必须同时分析调用前参数

#### 补充：成品字符串区也应归入这一步定位

在把`0x40625800`修正为“中间缓冲区”之后，Step 1 实际上还多完成了一件事：确认了**真正的成品字符串区**是`0x40624c00`。

这仍然属于“参数定位”而不是“算法拆解”，因为这里解决的问题依然是：

* 完整`X-Perseus`字符串最早稳定落在哪块内存
* 后续拼接链里看到的几个地址，谁是成品，谁只是搬运中转

当时支撑这个判断的直接证据有三组。

第一组证据是重建结果本身：

```
uv run python scripts/query_trace_db.py mem-reconstruct 13433848 0x40624c00 0x40624ee5
```

在这个 step 重建`0x40624c00`后，可以直接得到完整`X-Perseus`字符串，而不是某种二进制中间态。这一点和`0x40624400`那种主体输入块的形态完全不同。

第二组证据是调用参数：

```
step 13500742:
  x0 = 0x4062540b
  x1 = 0x40624c00
  x2 = 0x2e4
  target = 0x40281600 -> br x17 ->0x4046c300
```

这说明在后续外部函数调用前，`0x40624c00`已经作为源地址放进`x1`，长度`0x2e4`也与成品字符串长度一致。换句话说，这一步看到的不是“正在生成字符串”，而是“已经拿着成品字符串去做下一步处理”。

第三组证据是生成方式：

* `0x40624c00不是通过一次性整块 memcpy 得到`
* 当前 trace 中能看到它主要由`strb w10, [x8, x9]`逐字节写入
* 主要写入点落在`offset 0x1e865c`和`offset 0x1f9d10`
* 写入前还能看到`ldrb`从自定义字符表地址取单字节字符

这带来一个当时很重要的定位结论：

```
0x40624c00
  = 已经完成字符映射后的成品字符串区

0x40625800 / 0x408be206 / 0x408be000
  = 后续搬运、拼接、封装过程中的中间缓冲区
```

也就是说，Step 1 最终不只是把`X-Perseus`在最终大缓冲区中的位置找出来，还把“最早可确认的成品字符串落点”一起钉死了。

#### Python 表达

Step 1 本身不是算法分析，而是“定位 + 切片 + 首版链路建立”。因此这里给出的 Python 更偏向于把最终输出里`X-Perseus`摘出来，并把首版拷贝链表达成结构化数据：

```
from dataclasses import dataclass

@dataclass(frozen=True)
class PerseusSlice:
    header_addr: int
    value_addr: int
    value_end: int
    value: bytes

def locate_x_perseus_from_final_output(
    full_output: bytes,
    base_addr: int = 0x40642000,
) -> PerseusSlice:
    marker = b"X-Perseus\r\n"
    header_off = full_output.index(marker)
    value_off = header_off + len(marker)
    value_end_off = full_output.index(b"\r\n", value_off)
return PerseusSlice(
        header_addr=base_addr + header_off,
        value_addr=base_addr + value_off,
        value_end=base_addr + value_end...