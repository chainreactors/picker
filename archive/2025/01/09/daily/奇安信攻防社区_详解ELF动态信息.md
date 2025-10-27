---
title: 详解ELF动态信息
url: https://forum.butian.net/share/4019
source: 奇安信攻防社区
date: 2025-01-09
fetch_date: 2025-10-06T20:08:17.144822
---

# 详解ELF动态信息

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 详解ELF动态信息

了解ELF动态信息，了解各个表之间的联系，并通过一题CTF题目进行实践。

ELF动态信息
=======
ELF 动态信息是存储在 ELF 文件中的一个段（通常是 `.dynamic` 段），用于描述动态链接器运行时所需的信息。
`.dynamic`段包含了动态链接所需的各种信息，例如：
- 动态链接库的路径 (`DT\_NEEDED`)。
- 动态符号表的位置 (`DT\_SYMTAB`)。
- 字符串表的位置 (`DT\_STRTAB`)。
- 动态重定位表的位置 (`DT\_REL` 或 `DT\_RELA`)。
- `GOT` 表的地址 (`DT\_PLTGOT`)。
- 哈希表信息 (`DT\_HASH` 或 `DT\_GNU\_HASH`)。
每条信息是一个 `Elf32\_Dyn` 或 `Elf64\_Dyn` 结构，包含两个字段：
- `d\_tag`: 类型（例如 `DT\_NEEDED`、`DT\_SYMTAB` 等）。
- `d\_val`: 值，可能是地址、大小或其他信息。
其具体位置可通过010editor解析获取：找`program\_header\_table`中的`Dunamic Segment`。
`VIRTUAL\_ADDRE` 得到地址 `0x41E0`（使用时需加上基地址）
![image-20241211191903072.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-bc159a298ca623a3cab1d1c31607ed5bc93d06e8.png)
其结构一般如下：
![image-20241211190958956.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-de84c3aefa73b8936803c94e3886a9c54a66d7ad.png)
GNU\\_HASH Table
---------------
ELF 文件可以包含 `GNU\_HASH` 表，用于优化符号查找，与传统的 `.hash` 表相比，`GNU\_HASH` 表提供了更高效的符号查找算法。
其组成部分：
- `nbuckets`
- 表示哈希桶（`bucket`）的数量。
- 哈希桶是符号查找的起点，每个桶可以指向符号表中的符号链表。
- 这个值越大，符号分布越均匀，查找效率越高。
- `symbias`
- 符号偏移量，用于定义符号表中实际存储的符号起始位置。
- 所有全局符号的索引在符号表中的起始位置为 `symbias` 的值。也就是说，`symbias` 前的符号通常是局部符号，不被动态链接器处理。
- `bitmask\_nwords`
- 表示 Bloom Filter 中的位图单词数量（每个单词是 64 位）。
- Bloom Filter 是加速符号查找的第一步，用于快速排除符号不可能存在的情况
- `shift`
- 在计算 Bloom Filter 的哈希值时使用的位移量。
- 哈希函数会将符号的哈希值右移 26 位，生成另一部分用于 Bloom Filter 检查。
- `indexes`
- 这是 Bloom Filter 的位图数据，每个值是 64 位（8 字节）。
- 使用哈希函数计算得到的索引在这些位图中查找，如果相关位未被设置，则说明该符号不存在。
- `bucket`
- 每个值表示某个哈希桶中符号链表的起始索引。
- `chain`
- 存储符号的链表哈希值，用于解决哈希冲突。
- 每个值是一个符号的哈希值，如果高位设置为 0，表示链表的结束。
根据上文找到 `GRU\_HASH Table` 的地址：
![image-20241212145510105.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-28178ac50382517137c37ed8ed15e2d21968e190.png)
通过 `GNU\_HASH Table` 的信息，可以找到符号在 `Symbol Table` 中的索引。
其具体算法如下：（用Python代码作为演示）
- `main` 的代码仅为示例，可知 `iusp9aVAyoMI` 为 `Symbol Table` 的第 15 个元素。
```python
class GnuHash:
def \_\_init\_\_(self, nbuckets=0, symbias=0, bitmask\_nwords=0, shift=0, indexes=0, bucket=0, chain=0, ELFCLASS\_BITS=64):
self.nbuckets = nbuckets
self.symbias = symbias
self.bitmask\_nwords = bitmask\_nwords
self.shift = shift
self.indexes = indexes
self.bucket = bucket
self.chain = chain
self.ELFCLASS\_BITS = ELFCLASS\_BITS
def get\_hash(self, name):
h = 5381
for c in name:
h = (h << 5) + h + ord(c)
h &= 0xFFFFFFFF
return h & 0xFFFFFFFF
def check(self, hash\_value):
bit1 = 1 << (hash\_value % self.ELFCLASS\_BITS)
bit2 = 1 << (hash\_value >> self.shift) % self.ELFCLASS\_BITS
mask = self.indexes[hash\_value // self.ELFCLASS\_BITS % self.bitmask\_nwords]
return (mask & bit1) and (mask & bit2)
def get\_idx(self, hash\_value):
idx = self.bucket[hash\_value % self.nbuckets]
while self.chain[idx - self.symbias] & 1 == 0:
if (self.chain[idx - self.symbias] ^ hash\_value) >> 1 == 0:
return idx
idx += 1
return -1
def main():
name = "iusp9aVAyoMI"
gnu\_hash = GnuHash(
nbuckets=4,
symbias=0xB,
bitmask\_nwords=4,
shift=0x1A,
indexes=[
0x204800080000000, 0x800000000400000,
0x10440840201000, 0x30000804040000
],
bucket=[0xB, 0xE, 0x13, 0x14],
chain=[
0xD3AF6B8C, 0xA9CE198C, 0xA9CE198D, 0x7C988538,
0xB9F51094, 0xB9F51094, 0x69E7D2F4, 0x49A386F5,
0xB9F50D9F, 0xD0C97EE2, 0xD0C97EE2, 0x5BBF417A,
0x5BBF417A, 0x8F30E9A2, 0xCA77EE2E, 0xCA77EE2F
]
)
hash\_value = gnu\_hash.get\_hash(name)
print(f"hash: {hash\_value:X}")
if gnu\_hash.check(hash\_value):
idx = gnu\_hash.get\_idx(hash\_value)
print(f"idx: {idx}")
else:
print("Not found")
if \_\_name\_\_ == '\_\_main\_\_':
main()
```
Relocation Table
----------------
重定位表用于描述程序在加载时需要调整的地址信息。
ELF 文件中的重定位表主要有以下两种：
- `.rel` 表：不带附加的值。
- `.rela` 表：包含附加的重定位值。
重定位条目：
- `r\_offset`：重定位目标的内存地址，表示需要修正的地址。
- `r\_info`：由符号表索引和重定位类型编码的值。
- 高 32 位：符号表索引。
- 低 32 位：重定位类型。
- `r\_addend`：附加值，与重定位类型相关。
根据上文找到 `Relocation Table`：
![image-20241212153139763.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a96f0bb6461c12922154982204f9045cf0eb1a8a.png)
- RELA Relocation Table：
- 一个更通用的重定位表，可以包含任何类型的重定位信息。它不仅限于 PLT 或外部函数调用，还可以处理数据引用、内部符号等的重定位。
- JMPREL Relocation Table：
- 包含的是与动态链接相关的重定位条目，特别是那些需要在首次调用外部函数时解析的符号。
部分解释如下：
- `Elf64\_Rela <0x41D0, 0x403, 0xFF0>`
- 重定位类型为 `R\_AARCH64\_RELATIVE`，不涉及符号表，用于修正与基址相关的绝对地址。
- 典型用于静态地址的重定位。
- 将加载基址加上 `0xFF0`，写入 `0x41D0` 处。
- `Elf64\_Rela <0x41D8, 0xE00000101, 0>`
- 重定位类型为 `R\_AARCH64\_ABS64`，符号表相关，用于修正符号的绝对地址。
- `r\_info` 高 32 位为 `0xE`，即加载符号表索引指向的符号地址到 `0x41D8`。
- `Elf64\_Rela <0x43D0, 0x200000402, 0>`
- 重定位类型为 `R\_AARCH64\_JUMP\_SLOT`，动态链接时，为函数调用修正跳转插槽地址。
- 常用于 `.plt` 表。
Global Offset Table (GOT)
-------------------------
GOT 是动态链接中的一个关键表，用于存储每个动态库函数的实际地址，供程序直接调用，以避免多次动态解析。
GOT 表的每个条目都是一个指向函数的指针。
动态链接器在运行时解析符号表，将函数的实际地址填入此条目。
根据上文找到 `GLOBAL\_OFFSET\_TABLE`：
![image-20241212153732982.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1d0831c896a1edf047ad49a1ca74cfd67c2c46dd.png)
String Table
------------
字符串表是 ELF 文件中的一段，用于存储符号名和其他字符串。
- 以 `\x00` 字符分隔字符串。
- 动态符号表和其他部分使用字符串表中的索引来引用符号名。
Symbol Table
------------
符号表存储了程序中的符号信息，例如变量、函数名等。
符号条目内容：
- `st\_name (4 bytes)`： 符号名在 String Table 中的偏移。
- `st\_info (1 byte)`：
- 低 4 位表示符号类型。
- `STT\_NOTYPE`：0
- `STT\_OBJECT`：1
- `STT\_FUNC`：2
- `STT\_SECTION`：3
- 高 4 位表示 `Symbol Binding`。
- `STB\_LOCAL`：0
- `STB\_GLOBAL`：1
- `st\_other (1 byte)`：指定了符号的可见性。
- `STV\_DEFAULT`：0
- `STV\_INTERNAL`：1
- `STV\_HIDDEN`：2
- `STV\_PROTECTED`：3
- `st\_shndx (2 bytes)`：不同的上下文有不同的含义。
- `st\_value (8 bytes)`：符号的地址或值。
- `st\_size (8 bytes)`：符号的大小。
根据上文找到`Symbol Table`：
![image-20241212161544590.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4752d290184ffff9e6952abfb86efdd49d44c192.png)
实践一下
====
通过符号名找共享库中的符号
-------------
1. 根据 `Elf64\_Dyn <0x17, 0x7F0> ; DT\_JMPREL`、`Elf64\_Dyn <2, 0x120> ; DT\_PLTRELSZ` 获取 JMPREL Relocation Table的偏移和大小。
2. 根据 `Elf64\_Dyn <6, 0x288> ; DT\_SYMTAB` 获取 Symbol Table 的偏移。
3. 根据 `Elf64\_Dyn <5, 0x608> ; DT\_STRTAB` 获取 String Table 的偏移。
4. 遍历 JMPREL Relocation Table：
1. 获取表项第 2 项的高 32 位，即其在 Symbol Table 中的索引。
2. 根据索引获取 Symbol Table 的相应的符号信息。
3. 根据符号信息找到符号名在 String Table中的索引。
4. 判断符号名是否为目标符号名：
1. 若相同，则符号地址为 JMPREL Relocation Table 表项的第 1 项。
IDA Python 代码如下：
```python
import idaapi
import idc
def get\_dynamic\_addr():
base = idaapi.get\_imagebase()
program\_header\_offset = idaapi.get\_qword(base + 0x20)
program\_header\_size = idaapi.get\_qword(base + 0x28)
program\_header = base + program\_header\_offset
ph\_itemsize = 0x38
for i in range(program\_header\_size):
ph\_type = idaapi.get\_dword(program\_header + i \* ph\_itemsize)
if ph\_type == 2:
dynamic\_vaddr = idaapi.get\_qword(program\_header + i \* ph\_itemsize + 0x10)
dynamic\_memsz = idaapi.get\_qword(program\_header + i \* ph\_itemsize + 0x20)
break
else:
print("No dynamic segment found")
exit()
return dynamic\_vaddr, dynamic\_memsz
def get\_symtab\_addr():
dynamic\_addr, dynamic\_memsz = get\_dynamic\_addr()
dynamic\_size = dynamic\_memsz // 0x10
symtab = None
for i in range(dynamic\_size):
tag = idaapi.get\_qword(dynamic\_addr + i \* 0x10)
if tag == 6:
symtab = idaapi.get\_qword(dynamic\_addr + i \* 0x10 + 0x8)
break
return symtab
def get\_strtab\_addr():
dynamic\_addr, dynamic\_memsz = get\_dynamic\_addr()
dynamic\_size = dynamic\_memsz // 0x10
strtab, strtab\_size = None, None
for i in range(dynamic\_size):
tag = idaapi.get\_qword(dynamic\_addr + i \* 0x10)
if tag =...