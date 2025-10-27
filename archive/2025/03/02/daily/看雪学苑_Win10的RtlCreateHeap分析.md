---
title: Win10的RtlCreateHeap分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458590214&idx=1&sn=ea56d3846fc017aa6e90556182d855eb&chksm=b18c2c8c86fba59af2bd135d742305a171ef98a7d88d9aab89a32713b89e51ced7398024e77f&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-03-02
fetch_date: 2025-10-06T21:57:22.871297
---

# Win10的RtlCreateHeap分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9icbbWsWC9jkXydNhEsnodsVQNdmpPiaEu8vowbcK8oyMAIUYasNbPHNw/0?wx_fmt=jpeg)

# Win10的RtlCreateHeap分析

xichang13

看雪学苑

# RtlCreateHeap

◆RtlCreateHeap 源码

```
NTSYSAPI PVOID RtlCreateHeap(
  [in]           ULONG                Flags,
  [in, optional] PVOID                HeapBase,
  [in, optional] SIZE_T               ReserveSize,
  [in, optional] SIZE_T               CommitSize,
  [in, optional] PVOID                Lock,
  [in, optional] PRTL_HEAP_PARAMETERS Parameters
);
```

![RtlCreateHeap](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB90cvA80JhnzWXicdQice4kJ4CibeOtzeRm45cmwnKhL2hbBpiaLuJKddrRA/640?wx_fmt=other&from=appmsg)

![系统堆](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9FmINDYABh5rbiccCTpzlgVf5nrjcmTibzWib2xFgzdbgEODmDhDoNduJg/640?wx_fmt=other&from=appmsg)

**系统堆**

判断是否是系统堆，如果是，则在判断系统兼容性(RtlpHpAppCompatDontChangePolicy())后创建段堆(Segment Heap)。

![堆段](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9LlpnleuzdicTMa47ciaD6fZ1BZZvYrC40w01Zmty8gHfzNxZEHIXQlOw/640?wx_fmt=other&from=appmsg)

**段堆**

如果不是系统堆则判断HEAP\_CREATE\_SEGMENT\_HEAP(0x100)标志，如果是则调用(\_RtlpHpEnvGetEnvHandleFromParams)获取上下文后调用(\_RtlpHpHeapCreate())创建段堆，否则创建普通堆。

**普通堆**

![日志](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9icmDXSp0iadL59yQS1LSPcJ7YHPzMcMSZ2sTK9IDJ2ERZBQrcxoUgz5w/640?wx_fmt=other&from=appmsg)

1. 在创建普通堆之前会打印日志。

![堆信息](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9hWBDtuup5SkvlGYnVZDNz9ZnIibtco6a5TNVC0wuMwxAfapJ1Q1icjFg/640?wx_fmt=other&from=appmsg)

2.申请堆创建信息空间，判断我们是否传入Parameters参数。如果传入则使用传入的参数，否则使用默认参数，这里默认参数为进程堆信息。

3.有Parameters堆信息后，获取堆基址。

![调试堆](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB91uTGnQapvY4kfHmTH5IJ6HgMe8glWW8x0tiaSj3GDaC7UeUKtxR2RsA/640?wx_fmt=other&from=appmsg)

在获取堆基址之后会判断是否为调式堆。

![随机堆](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9S5AT7TEjkS14l32cM31lZsyPr7tzMwfWqFVf46T7Lribfmr5kndwBbQ/640?wx_fmt=other&from=appmsg)

4.调用(\_RtlpHeapGenerateRandomValue)获取随机数创建随机堆。

![申请堆地址](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB99iaG8ZAibV5JQWbNXywQo8hibquvfvnadUQWHe1icWviazqne62ibkum7LKQ/640?wx_fmt=other&from=appmsg)
![Encoding](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9koRibqXANdER2zDibaqtNfvPXr2nBb21RqntBQvDpSAERkRuibNt2acsg/640?wx_fmt=other&from=appmsg)
![初始化堆段](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB91Q6GRnia36YUnGxz3iby2fe1FWHGNKbTYvTW8wS6Rpor2jeRTicFe6MdA/640?wx_fmt=other&from=appmsg)

5.申请堆空间，并将堆信息写入堆空间。

![填入堆信息](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9RCV49KnyEEibASOFrBgmXkvaK3pAxX233bSn4yQTs2cy5pWvQmwd8Cw/640?wx_fmt=other&from=appmsg)

6.将堆基址加入堆链表。
![填入堆链表](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5rRvjzb0Dk6WcBJvsoaB9EyAkiaibGzLfN2soiazdgnJTscYp6SEwgfWIvgl9GexSc5c5NGia0CR7lQ/640?wx_fmt=other&from=appmsg)

#

# RtlAllocateHeap

```
PVOID RtlAllocateHeap(
    [in]           PVOID  HeapHandle,
    [in, optional] ULONG  Flags,
    [in]           SIZE_T Size
) {
    if (HeapHandle == NULL) {
        /*
        // 记录错误日志
        RtlpLogHeapFailure(0x13,0,0,0,0,0);
        */
    }

    if (*((DWORD*)HeapHandle + 2) == 0xDDEEDDEE) {
        /*
        // 分配内存与异常处理
        return RtlpHpAllocWithExceptionProtection(HeapHandle,Size,Flags);
        */
    }

    if (_RtlpHpHeapFeatures & 2 != 0) {
        /*
        // 分配内存
        RtlpHpTagAllocateHeap(HeapHandle,Size,Flags);
        */
    }
    // 分配内存
    return RtlpAllocateHeapInternal(HeapHandle, Size, Flags, 0);
}
```

#

# RtlFreeHeap

```
BOOL RtlFreeHeap(
[in]           PVOID                 HeapHandle,
[in, optional] ULONG                 Flags,
_Frees_ptr_opt_ PVOID BaseAddress
) {
    if (!BaseAddress)
        return 1;
    if (!HeapHandle)
        /*
        // 记录错误日志
        RtlpLogHeapFailure(HeapHandle,0,0,0,0,0);
        */
    if (*(DWORD*)((DWORD)HeapHandle + 8) == 0xDDEEDDEE)
        /*
        // 在异常保护中释放内存
        return RtlpHpFreeWithExceptionProtection(HeapHandle,BaseAddress,Flags);
        */
    if ((RtlpHpHeapFeatures & 2) != 0)
        /*
        // LFH 快速堆分配的释放
            return RtlpHpTagFreeHeap(HeapHandle, BaseAddress,Flags);
        */
    /*
    // 释放内存
    return RtlpFreeHeapInternal(HeapHandle, BaseAddress, Flags, 0, 0);
    */
    return FALSE;
}
```

#

# RtlCreateHeap 源码

```
DWORD dword_4B3A32DC = 0;
DWORD dword_4B3A32F4 = 0; // 函数?
DWORD dword_4B3A32E4 = 0;
// 堆特性
DWORD RtlpHpHeapFeatures = 0;
// 堆的错误处理行为
DWORD RtlpHeapErrorHandlerThreshold = 0;
DWORD dwAllocationGranularity = 0;
DWORD _RtlHeapKey = 0;
DWORD RtlpDisableHeapLookaside = 0;
DWORD _RtlpDisableHeapLookaside = 0;
DWORD _RtlpProcessHeapsListLock = 0;

PVOID RtlCreateHeap(
    ULONG                Flags,
    PVOID                HeapBase,
    SIZE_T               ReserveSize,
    SIZE_T               CommitSize,
    PVOID                Lock,
    PRTL_HEAP_PARAMETERS Parameters
) {
    DWORD SizeOfHeap;
    DWORD var_C0 = CommitSize;
    DWORD RandValue;
    _PEB32* peb = (_PEB32*)NtCurrentTeb()->ProcessEnvironmentBlock;
    DWORD NtGlobalFlag = peb->NtGlobalFlag;
    DWORD var_E4 = 0;
    _HEAP* pHeapBase = 0;
    DWORD var_D0 = 0;
    DWORD var_4C;
    DWORD var_DC;
    DWORD var_D8;
    DWORD var_E0;
    DWORD var_CC;

    DWORD edi = (DWORD)Parameters;
    DWORD esi = 0;
    DWORD eax = 0;

    if (dword_4B3A32DC != 0) { // 是否是系统堆
        if (HeapBase == 0 && Lock == 0) {
            /*
            RtlpHpAppCompatDontChangePolicy() // 不允许应用程序更改兼容性策略
            DWORD Result = dword_4B3A32F4(Flags, 0, ReserveSize, CommitSize, 0, edi);
            if(Result != 0)
                return Result;
            if(edi != 0xFFFFFFFF)
                return NULL;
            */
            edi = 0;
        }
    }
    else {
        if (dword_4B3A32E4 != 0) {
            if (edi == 1) {
                if ((Flags & 0x100) != 0)
                    edi = 0;
            }
        }
    }

    Flags &= 0xF1FFFFFF;
    if ((Flags & 0x100) != 0) { //HEAP_CREATE_SEGMENT_HEAP        0x00000100
        if (Flags & 0x2 == 0 || HeapBase != 0 || ReserveSize != 0
            || CommitSize != 0 || Lock != 0)
            return NULL;
        if (edi == 0xFFFFFFFF && dword_4B3A32E4 != 0) {
            edi = 0;
        }
        if (edi == 0) {
            esi = (DWORD)&var_4C;
        }
        else {
            esi = edi;
            /*
            // 检查参数是否合法
            if(!RtlpHpParametersVerify(edi))
                return NULL;
            */
        }
    }
    else if (RtlpHpHeapFeatures & 1 != 0) {
        if (Flags & 0x2 != 0 && HeapBase == 0) {
            if (edi != 0) {
                /*
                // 检查参数是否合法
                if(!RtlpHpParametersVerify(edi))
                    goto return53;
                */
            }
            eax = 2;
            if (Lock == 0)
                esi = (DWORD)&var_4C;
        }
    }
return53:
    eax = 2;
return52:
    if (esi != 0) {
        // 创建一个有异常保护的堆
        // return RtlpHpCreateHeap;
    }

    if (Flags & 0x10000000 == 0) {
        if (RtlpHeapErrorHandlerThreshold >= eax) {
            // 打印日志
        }
        if (Flags & 0xFFF80C00 != 0) {
            Flags &= 0x7F3FF;
        }
    }
    RTL_HEAP_PARAMETERS stParameters = { 0 };
    DWORD var_4;
    if (Parameters != 0) {
        var_4 = 0;
        if (Parameters->Length == 48) {
            memcpy(&stParameters, Parameters, 12);
        }
        var_4 = 0xFFFFFFFE;
    }

    // 修改flag
    if (NtGlobalFlag & 0x10 != 0) {
        Flags |= 0x20;
    }
    if (NtGlobalFlag & 0x20 != 0) {
        Flags |= 0x40;
    }
    if (NtGlobalFlag & 0x200000 != 0) {
        Flags |= 0x80;
    }
    if (NtGlobalFlag & 0x40 != 0) {
        Flags |= 0x40000000;
    }
    if (NtGlobalFlag & 0x80 != 0) {
        Flags |= 0x20000000;
    }
    if (NtGlobalFlag & 0x1000 != 0) {
        Flags |=...