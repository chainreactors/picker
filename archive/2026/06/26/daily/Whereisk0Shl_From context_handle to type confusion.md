---
title: From context_handle to type confusion
url: https://whereisk0shl.top/post/From%20context_handle%20to%20type%20confusion/
source: Whereisk0Shl
date: 2026-06-26
fetch_date: 2026-06-27T05:50:38.655050
---

# From context_handle to type confusion

# [Whereisk0Shl](/)

k0shl

一只在二进制漏洞路上不断努力的菜鸡

[Home](/)
[Archive](/archive/)
[RSS](/feed.xml)
[GitHub](https://github.com/k0keoyo)

There is
[k0shl](https://whereisk0shl.top)

# From context\_handle to type confusion

2026-06-26

# A Type Confusion Vulnerability Pattern in Windows RPC Servers

In this blog post, I will share a common type-confusion vulnerability scenario that exists in many RPC servers. I’ll walk through some of my thoughts while discovering and studying this class of issues, as well as certain technical details. These problems generally arise due to insufficient constraints in IDL definitions and the lack of proper validation inside RPC interfaces.

The story begins in early 2025 when I was researching the attack surface of Windows HTTP Services. During the review of various Windows HTTP components, I found that **ssdpsrv** hosts not only an HTTP service but also an RPC server. In the following research, I started auditing this RPC server and noticed that it exposed several different context-handle types, such as `CONTEXT_HANDLE_TYPE` and `SYNC_HANDLE_TYPE`, each managed by different RPC interfaces.

```
_SSDPOpenRpc
_SSDPCloseRpc

_InitializeSyncHandle
_RemoveSyncHandle
```

Context handles are extremely common in RPC. Conceptually, they work like indices. In rpcrt4, a context handle maps to a specific memory region that usually stores an object. This mechanism is similar to how object references are represented inside the Windows operating system.

When I examined this RPC service, one idea immediately came to mind: since a context handle is merely an index that represents a memory region, what would happen if I passed a `CONTEXT_HANDLE_TYPE` object into an interface that expects a `SYNC_HANDLE_TYPE`?

---

## CVE-2025-48815

Inside `ssdpsrv!_RemoveSyncHandle`, the `SYNC_HANDLE` refers to a specific handle value that is opened by the `InitializeSyncHandle` interface. The interface creates a semaphore object:

```
__int64 __fastcall InitializeSyncHandle(_QWORD *a1)
{
  [...]
  Semaphore = CreateSemaphoreExW(0i64, 0, 0x7FFFFFFF, 0i64, 0, 0x1F0003u);
  [...]
  *a1 = v4;
  return 0i64;
}
```

`_RemoveSyncHandle` then simply calls `CloseHandle` on this value:

```
BOOL __fastcall RemoveSyncHandle(void **a1)
{
  [...]
    result = CloseHandle(v1);
    *a1 = 0i64;
  [...]
}
```

However, if I pass a context handle returned by `_SSDPOpenRpc` into `RemoveSyncHandle`, the call still succeeds—even though the context points to a `CONTEXT_HANDLE` object instead of a sync handle. This is a straightforward type-confusion case. Interestingly, the handle returned by `_SSDPOpenRpc` actually points to the global variable `g_lSsdpRef`, which tracks a reference count:

```
__int64 __fastcall SSDPOpenRpc(_QWORD *a1)
{
  [...]
      ++g_lSsdpRef;
      *a1 = &g_lSsdpRef;
  [...]
}
```

This means that by repeatedly calling `_SSDPOpenRpc`, I can cause the returned context handle to point to a reference-count value that matches any small integer handle value — e.g., `0x1C4`, `0x200`. When this value is passed to `_RemoveSyncHandle`, `ssdpsrv` ends up closing an **arbitrary handle** accessible in the process context.

---

## FC\_SUPPLEMENT and FC\_BINDING\_CONTEXT

Once I understood this behavior, I realized that many Windows RPC servers likely have similar setups — multiple context-handle types within the same interface. I quickly found other RPC servers with comparable patterns, but when testing them, RPC threw exception `0x6` (`invalid_handle`). This confused me: why does `ssdpsrv` allow cross-type usage while others reject it?

To investigate, I began reverse-engineering the RPC runtime.

A useful trick: exceptions inside RPC servers generally don’t break into the debugger by default. To capture exception `0x6`, use:

```
sxe 00000006
```

This allows breaking at the exact moment the exception is thrown. By walking the call stack, I found the function `NDRSContextUnmarshall2`.

Reverse-engineering RPCRT4 is a massive task, so instead of analyzing every call in detail, I used a shortcut: I set a breakpoint on the same function inside `ssdpsrv` and compared the behavior against the other target RPC server.

Surprisingly, the breakpoint never triggered in `ssdpsrv`.

This meant the root cause was not inside that function. So I moved outward, comparing the surrounding logic, and eventually found the key difference: in the IDL of `ssdpsrv`, the context-handle descriptor begins with `0x70`, while in the other RPC server, the value is `0x75`:

```
.rdata:000000018003AE04   db 70h
.rdata:000000018003AE05   db 0EDh

.rdata:0000000140017850   db 75h
.rdata:0000000140017851   db 70h
```

---

This may indicate that different types exist among context handles. So I searched online for the type definitions of context handles, and in my colleague victorv’s blog (https://v-v.space/2023/09/06/rpc\_readme/), I found some inspiration regarding these definitions. This blog also explains in detail how to identify parameter types in RPC, and I highly recommend interested readers to go through it.

In that post, victorv listed parameter types. Among them, **0x75 represents SUPPLEMENT**, and **0x70 represents BIND\_CONTEXT**:

```
FC64_BIND_CONTEXT = 112 0x70
FC64_SUPPLEMENT = 117 0x75
```

With these structure types in mind, I noticed during reversing that when the incoming context handle is of type SUPPLEMENT, rpcrt4 will validate whether the context ID matches during unmarshalling. If it does not match, it throws an exception with error code **0x6**. However, when the context handle is of type BIND\_CONTEXT, rpcrt4 directly indexes the corresponding object and passes it into the RPC interface.

### From binding\_context to type confusion

At this point, things become much simpler. You only need to find an RPC server that has multiple context handles under the same interface, and this will give you a set of potential attack surfaces. During this process, I used James Forshaw’s tool **NtObjectManager** (https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools/tree/main/NtObjectManager). NtObjectManager can parse the RPC server’s IDL and clearly distinguish between **FC\_BINDING\_CONTEXT** and **FC\_SUPPLEMENT**, so I only needed to filter RPC servers whose interfaces contain multiple occurrences of `"[out] /* FC_BINDING_CONTEXT */"`.

## CVE-2025-53143

Crash Dump:

```
0:034> r
rax=00000283529a8f50 rbx=00000283529a8f50 rcx=00007ffe440edb60
rdx=0000000000000001 rsi=00007ffe440eba28 rdi=0000000000000001
rip=00007ffe44027373 rsp=000000a4c2c7e9d0 rbp=0000000000000011
 r8=7ffffffffffffffc  r9=000000a4c1bb1000 r10=0000000000000000
r11=000000a4c2c7e830 r12=0000000000000001 r13=000000000000000e
r14=000000a4c2c7ee90 r15=0000000000000000
iopl=0         nv up ei pl nz na pe nc
cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010202
MQQM!CTransaction::StartPrepareRequest+0x5b:
00007ffe`44027373 834b1420        or      dword ptr [rbx+14h],20h ds:00000283`529a8f64=????????
```

Stack Trace:

```
0:034> k
 # Child-SP          RetAddr               Call Site
00 000000a4`c2c7e9d0 00007ffe`440265e6     MQQM!CTransaction::StartPrepareRequest+0x5b
01 000000a4`c2c7ea10 00007ffe`44037e01     MQQM!CTransaction::InternalCommit+0x62
02 000000a4`c2c7ea40 00007ffe`43ff81ab     MQQM!QMDoCommitTransaction+0xcd
03 000000a4`c2c7ea70 00007ffe`43fc5685     MQQM!qmcomm_v1_0_S_QMCommitTransaction+0xb
04 000000a4`c2c7eaa0 00007ffe`68113882     RPCRT4!Ndr64StubWorker+0x862
05 000000a4`c2c7ead0 00007ffe`680c599c     RPCRT4!NdrServerCallAll+0x3c
...
```

## CVE-2025-54104

Crash Dump:

```
0:013> r
rax=0000000000000000 rbx=0000000002000200 rcx=00007fffe5104ad8
rdx=00000080007fe188 rsi=00000080007fe188 rdi=0000008001ff9b10
rip=00007fffe50c3943 rsp=00000080007fe120 rbp=00000080007fe1f0
 r8=00000080007fe088  r9=0000000000000000 r10=0000000000000000
r11=0000000000000246 r12=0000000000000000 r13=0000008001ff9c78
r14=00007fffe5104000 r15=0000008001ff9c60
iopl=0         nv up...