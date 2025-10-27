---
title: Windows10代码还原汇编特征汇总（附NTDLL CreateHeap还原代码）
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589963&idx=1&sn=f44e196a030487673a9ac152b0dad974&chksm=b18c2b8186fba297c4fca88a0a61afb27324557b7e34bd854f0701eb3dabc7f4f34372ce1aac&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-26
fetch_date: 2025-10-06T20:38:06.815257
---

# Windows10代码还原汇编特征汇总（附NTDLL CreateHeap还原代码）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjibt0icp1wibbpMFsbo1nCdiaHW28O4Q4pBkzmVcWs5e8jWDSqGr7vPI0Hlw/0?wx_fmt=jpeg)

# Windows10代码还原汇编特征汇总（附NTDLL CreateHeap还原代码）

TeddyBe4r

看雪学苑

写这篇文章的目的是想帮助刚开始或者准备开始研究windows系统的人员，此篇文章仅作为经验分享，是我在逆向还原windows10堆API`CreateHeap`和`AllocateHeap`以及`AllocateHeapInternal`源代码时总结的一些经验，如有错误请各位前辈斧正。我们仅分享其windows10 ntdll中常见的一些汇编特征优化，如若不涉及的优化请各位自行翻阅资料学习。

## 环境

分析环境: Windows11
工具: Windbg, IDA7.5
分析目标平台: Windows10
分析目标文件: C:\Windows\SysWow64\ntdll.dll（32位）
版本信息：10.0.19041.5007 (WinBuild.160101.0800)
SHA-1:9C3A55D17C022D7B32EE558E8941C4C9938696CA

```
0

常见Release版优化梳理
```

对于常见的Release版编译的优化此篇文章涉及到的有

**CPU流水线优化**

真正的CPU流水线优化有许多概念且十分复杂，但是体现在代码中的我们只需要关注一些会影响我们分析的内容，比如**乱序执行**我们以最经典的三级流水线为例举出例子方便大家简易回顾一下流水线优化。如下三个操作分别由三个不同的CPU组件同步执行。

● 取指令
● 译码
● 执行

在CPU中形如如下流程，但是流水线优化只会优化无相关关联的代码譬如:mov eax, imm32 mov ebx, imm32 等，而如果出现一个指令序列其中的前后代码相关联则会破坏该处的流水线优化，对于3级流水线来讲最好情况是3行代码互相无关。

下面我们给出相关图例辅助理解

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjibj2BBB2y3DWYibEVC1yau2VXFLKeoyJmlNoicfhgs2s8Fy1ECPX9TX28Q/640?wx_fmt=other&from=appmsg)

一旦出现的一组代码(**A组**)可以组成流水线优化则意味着该组代码A的执行顺序与组内其他代码无关，且改组代码也有可能与其他组代码无关，此时编译器有可能将该组代码提前（延后）到某组代码（**B组**）后执行且不会影响程序的逻辑，最简单的情况就是`__cdecl`后的调用方的平栈代码`add esp, imm`在ntdll中如果出现调用函数为`__cdecl`就有可能出现这种优化可能会在后面的代码中穿插一条平栈代码，在还原代码时我们只需要跳过即可。

**加法优化(比例因子优化)**

对于加法通常我们能看到利用`lea`指令进行优化,譬如`eax + eax + 1`在优化版中会出现形如`lea eax, [eax+eax+1]`等优化类型但是在此次还原中出现较少。

```
1

临时变量优化
```

在逆向的过程中我们经常能看到如下片段

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjib9f2ibgVmS1YTB061xB6iaXfhCED2uG1wsMiasRL3KlU6THQbujqRh1xgg/640?wx_fmt=other&from=appmsg)

对于这种情况我们在初次见到时如果发现前面的esi原先为某个变量值但是被赋值覆盖掉了原值，然后中间经过一系列操作运算传入了某个函数或者放入了某个变量，则有可能是编译过程编译器将临时变量优化掉了导致的譬如如下C代码。

```
DWORD add(DWORD a, DWORD b)
{
    DWORD dwRet = a + b;
    return dwRet;
}
```

在这种情况下就有可能将中间代码**dwRet**当作临时变量优化掉变成如下汇编形式

```
mov eax, [ebp + a]
add eax, [ebp + b]
```

当我们出现如下情况时考虑出现了临时变量优化尽量看此寄存器是否用作他用，如果是传参则可以还原为传入参数写表达式，如果是变量赋值则可以写作将表达式赋值为变量。

```
2

0值寄存器传递
```

对于0值寄存器传递是我在逆向CreateHeap API的时候发现的，

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjibhPVkib1IGROICicAldhRk0RjbxucG2CnaPtMgbHfrcibOEMQU28Edt3Dw/640?wx_fmt=other&from=appmsg)

这里的EBX寄存器在整个函数中都被当作0值进行赋值操作,譬如在返回失败空值的时候对返回值esi的赋0处理。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjibVASFVwfwlOTFYYJ3mClrNwIP4Aic4LjUWBXwbMKsWdDib9Qd8ldhDMHQ/640?wx_fmt=other&from=appmsg)

###

```
3

函数调用约定优化
```

###

对于这个应该也属于是常见优化里面的但是笔者还是提出来单独分析一下，对于大家习惯用的ida如果F5之后发现函数参数不对多半就是因为编译器将原本的`__stdcall`优化为`__fastcall`譬如

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjibtRxdttbgcn0iaRYlPJJnbQG5rInAK8CR6oyftHYxhUPibhrd94SzKAyg/640?wx_fmt=other&from=appmsg)

对于见到在调用前给EDX和ECX等赋值的行为我们需要进入其调用的函数中查看

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjib8tONNXz3IB6vVfny5ncQp14q3ViaoVFh6w8W7rvBcepetey5wf9pDHQ/640?wx_fmt=other&from=appmsg)

如果被调用的函数中直接使用了EDX或者ECX寄存器则考虑将该函数翻译为`__stdcall`或者照例翻译为`__fastcall`具体情况应该视可读性和可维护性而定。

```
4

if特征与平坦化优化(if反转)
```

在讨论这个汇编特征之前我们先看一下VS2019对if语句的优化如下

```
; if (a >= 0)
; {
;		printf("hello world");
;	}
mov edx, [a]
test edx, edx
jns xxxx ; 这里会取反
  ; 这里则是语句块中的代码
  push str_xxx ;HelloWorld
  call subxxxxx;printf
  add esp, 8; 平栈
xxxx:
  ;这里一般为后面的代码
```

图示

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjib2Z3J8FibV2QBjClLNyWfvicNY8icIvYj5fDXUtf1BooF53ibBBFGAFYRoA/640?wx_fmt=other&from=appmsg)

**在正常的VS2019编译器中Release将会把汇编优化为取反跳的形式**但是在ntdll中如果出现了跳转分支在平坦流片段中的情况则需要翻译为**条件不取反**如果跳转后的平坦流片段中紧接判断还可以考虑将其整合翻译为**条件表达式 + if语句的形式**。

在还原过程中还有一种情况就是条件表达式融合到平坦流中，在这种情况下同样需要翻译为**条件不去反**然后将平坦流中的代码翻译到条件语句块中，一般这种情况会经历两次跳转，一次是跳入另一次是在平坦流跳出，如果有else语句则有可能跳出到出口前面。

我们来看下面的例子，首先是外层

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjibFX06X70d0bBMpcwc4FPibZLsjtwLnVY0YSmia9JcuhOU6ibtMPupODJVA/640?wx_fmt=other&from=appmsg)

然后是内层

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjibFJ6LTwgib5xMCibaoL95zAG0bSZpAW6nojwnB2oO4zEqGu0lC26SEjZA/640?wx_fmt=other&from=appmsg)

在ntdll中我们会遇到大量这种形式的代码，唯独在较为短小的条件判断语句中能看到正常取反跳的优化身影，我们需要多往后看看比对跳转的汇编标签是否和平坦流内部的跳转相同，辅以上下文依据可读性进行判断。

```
5

push pop寄存器赋
```

对于这种情况多半是寄存器不够用了，这种情况后面多半会接一个call或者较为复杂的比较逻辑，如下示例。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHaA5QYiahAFzeeMWicRcbjibdwpiajbYMEquIpImW3wtdvPqLexbEvr0BT4icbqVlupq6Wa4Mqia3T0fw/640?wx_fmt=other&from=appmsg)

###

### 总结

> 对于windows的逆向需要熟悉其内部编译器的汇编代码优化特征才能更好的进行还原，我仅PO出我逆向还原的CreateHeap API代码，而AllocateHeap等其他API代码就不发了。**注意：此代码仅作学习用途，且由于是项目原因，所以我给出粗糙版的代码，某些结构体就不发出来了（偏移还在），如果各位感兴趣可以自己进行逆向 还原**

```
typedef struct _SYSTEM_BASIC_INFORMATION {
    ULONG Reserved;                     // 保留字段，通常为 0
    ULONG TimerResolution;              // 系统定时器的分辨率（以微秒为单位）
    ULONG PageSize;                     // 页面大小（以字节为单位）
    ULONG NumberOfPhysicalPages;        // 物理页面的数量
    ULONG LowestPhysicalPageNumber;     // 物理页面的最低编号
    ULONG HighestPhysicalPageNumber;    // 物理页面的最高编号
    ULONG AllocationGranularity;        // 内存分配粒度
    ULONG MinimumUserModeAddress;       // 用户模式下的最小地址
    ULONG MaximumUserModeAddress;       // 用户模式下的最大地址
    ULONG ActiveProcessorsAffinityMask; // 活动处理器的亲和性掩码
    UCHAR NumberOfProcessors;           // 处理器的数量
} SYSTEM_BASIC_INFORMATION;

/*
* Flags : 指定堆的可选属性的标志。
这些选项会影响通过调用堆函数（RtlAllocateHeap和RtlFreeHeap）对新堆的后续访问。
    一共有3个值
    1. HEAP_GENERATE_EXCEPTIONS 指定系统引发异常而不是通过返回空值即异常堆
    2. HEAP_GROWABLE 可增长堆如果HeapBase为空必须指定
    3. HEAP_NO_SERIALIZE 指定当堆函数从此堆分配和释放内存时不使用互斥。
                        当未指定 HEAP_NO_SERIALIZE 时，默认是序列化对堆的访问。
                        序列化堆访问允许两个或多个线程同时从同一堆分配和释放内存。
* HeapBase: 非空情况下就是将指定分配的地址，如果空的情况下则会在进程空间随机分配
* ReserveSize:
*
*
*/

ULONG g_initVar1ByInitalizeProccess = 0;
ULONG g_initVar2ByAvrfLoadDll = 0;
typedef  int(__thiscall* PFN_4B3A32F4)(DWORD, DWORD, DWORD, DWORD, DWORD, PVOID);

PFN_4B3A32F4 g_4B3A32F4;

PVOID
RtlCreateHeap(
    [in]           ULONG                Flags,
    [in, optional] PVOID                HeapBase,
    [in, optional] SIZE_T               ReserveSize,
    [in, optional] SIZE_T               CommitSize,
    [in, optional] PVOID                Lock,
    [in, optional] PRTL_HEAP_PARAMETERS Parameters
)
{
    DWORD var_12C;
    DWORD var_120;
    DWORD var_110[10];
    PVOID pLock = Lock;
    ULONG ulFlags = Flags;
    PVOID pBase = HeapBase;
    PVOID pBase2 = HeapBase;
    SIZE_T stReserver = ReserveSize;
    DWORD var_BC;
    SIZE_T stCommit = CommitSize;
    PVOID pLock2 = Lock;
    DWORD var_CC;
    DWORD CriticalSectionFlag;
    DWORD var_D8;
    DWORD BaseAddress;
    BOOL ntGlobalFlag = ((PPEB)__readfsdword(0x30))->NtGlobalFlag;
    ULONG ulUnknow1 = 0;
    DWORD dwRegionSize = 0;
    ULONG ulUnknow2 = 0;
    ULONG ulUnknow3 = 0;
    DWORD pHeapHandle2;
    BYTE var_A8[0x30];
    DWORD dwCommiteSize;

    SYSTEM_BASIC_INFORMATION SystemInformation;
    DWORD var_58;
    CPPEH_RECORD ms_exc;
    // 模拟组
    DWORD eax = 0;
    DWORD ecx = 0;
    DWORD edx = (DWORD)Flags;
    DWORD ebx = 0;
    DWORD esi = 0;
    DWORD edi = (DWORD)Parameters;

    // 进程默认堆
    if (g_initVar1ByInitalizeProccess != NULL
        && pBase == NULL
        && pLock == NULL)
    {
        // 不允许应用程序更改策略
        RtlpHpAppCompatDontChangePolicy();
        // 如果用户设置了Commit指针则通过Commit指针来获取堆结果
        esi = g_4B3A32F4(ulFlags, 0, stReserver, stCommit, 0, Parameters);
        if (esi != 0)
        {
            goto RELEASE_SRC;
        }
        if (edi != 0xFFFFFFFF)
        {
            edi = (DWORD)pBase;
            esi = 0;
            goto RELEASE_SRC;
        }
    }
    else
    {
        if (g_initVar2ByAvrfLoadDll != 0
            && (DWORD)Parameters == 1)
        {
            /*
            mov     eax, edx
            and     eax, 100h       ; if ((eax & 100h) != 0)
                                    ; eax = 100h
                                    ; if ((eax & 100h) == 0)
                                    ; eax = 0
            ne...