---
title: http.sys — UlpParseNextRequest 中连接数组容量整数溢出（CWE-190）导致内核池溢出
url: https://mp.weixin.qq.com/s/wZoarN6LLHU_s8U9vGZk-w
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:44:14.189826
---

# http.sys — UlpParseNextRequest 中连接数组容量整数溢出（CWE-190）导致内核池溢出

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSia6drhjkOt9oN5HtccDq0LrbAdeLPUkiak64gaueM0oDEjBT75CXoWyOlbLyIib3e3LygqSG0jzehVWdJ3wj2L5wRWgyFrM9VZw8/0?wx_fmt=jpeg)

# http.sys — UlpParseNextRequest 中连接数组容量整数溢出（CWE-190）导致内核池溢出

The Drift Corpus
The Drift Corpus

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原文链接:

* "https://byteray-ai.github.io/drift-corpus/item/http\_a10f1434-http-report-20260629-001610.html"

## 1. 概述

| 项目 | 值 |
| --- | --- |
| 未修补二进制 | `http_unpatched.sys` |
| 已修补二进制 | `http_patched.sys` |
| 整体相似度 | 0.9896 |
| 匹配函数 | 3205 |
| 变更函数 | 6 |
| 相同函数 | 3199 |
| 未匹配 (未修补 → 已修补) | 0 / 0 |

**结论：**一个微小但关键的补丁，围绕每个TCP连接 HTTP 请求追踪数组的 capacity 字段引入了 16 位溢出检查，封堵了 `http.sys`中一个可远程触达的内核池溢出。

在 6 个变更函数中，只有 1 个 (`UlpParseNextRequest (sub_1c000e4a0)`→ `UlpParseNextRequest (sub_1c000e550)`) 与安全相关。其余是重定位到新地址的相同函数（寄存器/偏移漂移）或启发式误配对，外加无害的配置管道（新增 `MaxHeadersCount`注册表参数）。实际修复集中在请求处理循环中：已修补版本调用标准安全整数库例程 `RtlUShortAdd (sub_1c001c6e4)`执行 `capacity + 5`并带溢出检测，且此检查路径由 KIR 特性标志 `UxKirRefBufferOverflowCheck (data_1c0078d80)`选择。当该标志关闭时，已修补版本仍运行原始未检查的 `add cx, 5`路径，因此该修复是一个 KIR 门控的安全路径，而非无条件替换。

---

## 2. 漏洞摘要

### 严重 — 整数溢出 (CWE-190) → 内核池缓冲区溢出 (CWE-122)

**受影响函数：**`UlpParseNextRequest (sub_1c000e4a0)`（未修补）、`UlpParseNextRequest (sub_1c000e550)`（已修补）—— HTTP 请求处理主循环。

**根因：**

该函数为每个连接维护一个动态的 HTTP 请求/区间 (range) 对象数组。数组在连接对象上追踪三个小字段：

* `+0x630`

  — `WORD`capacity（容量）
* `+0x632`

  — `WORD`count（计数）
* `+0x638`

  — `PVOID`buffer 指针（位于 `NonPagedPoolNx`）

每当 `count >= capacity`时，代码扩张数组：分配一块大小为 `(capacity * 8) + 0x28`的新池缓冲区，复制旧条目，释放旧缓冲区，然后用\*\* 16 位加 5 \*\*写入新容量：

```
*(conn + 0x630) = capacity + 5;     // 16 位加法，无溢出检查
```

`capacity`是一个 `WORD`。一旦它达到 `0xFFFB..0xFFFF`，加 5 会回绕到 `0x0000..0x0004`。在\*\* 下一次 \*\*扩张事件时，分配大小由这个微小的回绕后容量计算（例如 `1*8 + 0x28 = 0x30`字节），但 *count*仍从其先前值（约 `0xFFFC`+）继续攀升。紧接着的下一条条目写入

```
mov qword [rax + rcx*8], rsi   ; rcx = count (很大), rax = 微小缓冲区
```

便会以 8 字节指针的步长走出新池分配的末端——一个大型的、由攻击者驱动的、内核池溢出。

**为何可被利用：**索引 (`count`) 和步长 (8 字节) 完全由攻击者控制，攻击者只需在长连接上发送更多 HTTP 请求/区间，即可控制数组的增长节奏。缓冲区位于 `NonPagedPoolNx`，其相邻分配常包含其他连接对象、头部或池元数据。

**补丁的作用：**已修补循环调用标准 RTL 安全加法库例程 `RtlUShortAdd (sub_1c001c6e4)`，它在 32 位算术中执行 `capacity + 5`，将截断后的 16 位结果与输入比较，并用 `cmp ax, cx; jb`检测回绕。回绕时钳制为 `0xFFFF`并返回 `STATUS_INTEGER_OVERFLOW (0xC0000095)`；调用方在负状态值时退出，因此溢出的容量永远不会抵达 `ExAllocatePoolWithTagPriority`。此检查路径在运行时由 KIR 特性标志 `UxKirRefBufferOverflowCheck (data_1c0078d80)`选择（来自 WIL 特性分级查询）。当标志禁用时，已修补版本回退到原始未检查的 `add cx, 5`路径 (0x1c000ea02)，该路径与被漏洞利用的代码逐字节相同。未修补版本只有那条未检查路径，且没有对 `RtlUShortAdd`的调用。

**攻击者可达的入口点：**任何经由 `http.sys`的 HTTP 监听器（IIS、HTTP API v2、WinRM、Print Spooler 的 HTTP API 等）。

**调用链：**

1. 远程客户端向目标 HTTP 端点打开 TCP 连接。
2. `TDI/WSK`

   接收将字节交给 `http.sys`。
3. `http.sys`

   的 IRP 分发将请求路由进请求处理主循环。
4. 调用方 `UlpAuthenticateRequestCompletion (sub_1c01176a0)`→ `UlResumeParsing (sub_1c000a940)`→ `UlpHandleRequest (sub_1c000e1a0)`→ `UlBeginOpaqueMode (sub_1c002dc84)`→ **`UlpParseNextRequest (sub_1c000e4a0)`**（脆弱循环）。
5. 循环内部，`ExAllocatePoolWithTagPriority`以回绕后的欠尺寸容量被调用。
6. 在 `mov qword [rax+rcx*8], rsi`(0x1c000e8d7) 处的下一条条目写入破坏了相邻的 `NonPagedPoolNx`内存。

---

## 3. 伪代码 Diff

```
// === 未修补: UlpParseNextRequest (sub_1c000e4a0) ===========================================
void process_request(conn_t *conn, request_t *req) {
    uint16_t count    = *(uint16_t *)(conn + 0x632);
    uint16_t capacity = *(uint16_t *)(conn + 0x630);

    if (count >= capacity) {
        size_t   new_size = (size_t)capacity * 8 + 0x28;   // 使用当前 capacity
        void    *new_buf  = ExAllocatePoolWithTagPriority(..., new_size, ...);
        if (!new_buf) return;

        memcpy(new_buf, conn->buf, capacity * 8);
        ExFreePoolWithTag(conn->buf);
        conn->buf = new_buf;

        // *** BUG: 16 位加法, 无溢出检查 ***
        *(uint16_t *)(conn + 0x630) = capacity + 5;        // 超过 0xFFFF 后回绕!
    }

    // 以 *单调递增* 的 count 为索引
    conn->buf[count] = req;                                // 若 capacity 已回绕则为 OOB 写入
    *(uint16_t *)(conn + 0x632) = count + 1;
}

// === 已修补: UlpParseNextRequest (sub_1c000e550) =============================================
// RtlUShortAdd 是标准 RTL 安全整数库例程, 非 http.sys 自定义辅助函数.
NTSTATUS RtlUShortAdd(uint16_t cur, uint16_t addend, uint16_t *out) {  // sub_1c001c6e4
    uint32_t sum = (uint32_t)cur + addend;                // 32 位加法
    if ((uint16_t)sum < cur) {                            // cmp ax,cx ; jb
        *out = 0xFFFF;                                    // 钳制
        return STATUS_INTEGER_OVERFLOW;                   // 0xC0000095
    }
    *out = (uint16_t)sum;
    return STATUS_SUCCESS;
}

void process_request(conn_t *conn, request_t *req) {
    uint16_t count    = *(uint16_t *)(conn + 0x632);
    uint16_t capacity = *(uint16_t *)(conn + 0x630);

    if (count >= capacity) {
        if (UxKirRefBufferOverflowCheck) {                 // 新增 KIR 门控安全路径
            uint16_t new_cap;
            if (RtlUShortAdd(capacity, 5, &new_cap) < 0)   // 新增带溢出检查的加法
                goto fail_request;                         // 新增回绕时退出
            size_t new_size = (size_t)new_cap * 8;         // 使用已校验的 capacity
            void  *new_buf  = ExAllocatePoolWithTagPriority(..., new_size, ...);
            if (!new_buf) goto fail_request;
            memcpy(new_buf, conn->buf, count * 8);
            if (capacity > 1) ExFreePoolWithTag(conn->buf);
            *(uint16_t *)(conn + 0x630) = new_cap;         // 安全, 已校验
            conn->buf = new_buf;
        } else {                                           // KIR 标志关闭: 原始未检查路径
            size_t new_size = (size_t)capacity * 8 + 0x28;
            void  *new_buf  = ExAllocatePoolWithTagPriority(..., new_size, ...);
            if (new_buf) {
                memcpy(new_buf, conn->buf, count * 8);
                if (capacity > 1) ExFreePoolWithTag(conn->buf);
                *(uint16_t *)(conn + 0x630) = capacity + 5;  // 仍会 16 位回绕!
                conn->buf = new_buf;
            }
        }
    }

    conn->buf[count] = req;
    *(uint16_t *)(conn + 0x632) = count + 1;
}
```

**关键要点：**

* 未修补版本中危险的一行是未设防的 `capacity + 5`。
* 检查路径在 `RtlUShortAdd (sub_1c001c6e4)`返回成功前绝不信任加法结果，并将校验后的值用于分配大小、存储容量和条目写入。
* 已修补版本保留了原始未检查的 `add cx, 5`路径作为回退（当 `UxKirRefBufferOverflowCheck (data_1c0078d80)`禁用时采用），因此该修复依赖于该 KIR 标志被启用。

---

## 4. 汇编分析

### 未修补 — 脆弱的分配块

```
; --- 读取两个 16 位字段 ---
0x1c000e82f | movzx   eax, word [rdi+0x632]      ; eax = count
0x1c000e836 | movzx   ecx, word [rdi+0x630]      ; ecx = capacity
0x1c000e83d | cmp     ax, cx
0x1c000e840 | jb      0x1c000e8cd                 ; 若 count < capacity, 跳过增长
                                                  ; (这是路径中唯一的尺寸检查)

; --- 使用当前 capacity 计算新分配大小 ---
0x1c000e846 | lea     rdx, [rcx*8 + 0x28]         ; rdx = capacity*8 + 0x28   <-- 盲目信任
0x1c000e85c | call    qword [rel 0x1c0086c50]     ; ExAllocatePoolWithTagPriority
0x1c000e86b | test    rax, rax
0x1c000e86e | je      0x1c000e8e9                 ; 分配失败 -> 退出

; --- (通过 memmove 复制旧数据, 释放旧缓冲区) ---
; ... (为清晰省略) ...

; --- BUG: capacity 更新是 16 位加法, 无溢出检测 ---
0x1c000e8ad | movzx   ecx, word [rdi+0x630]       ; 重新加载 capacity
0x1c000e8bb | add     cx, 5                        ; 16 位加法; 若 cx >= 0xFFFB 则回绕
0x1c000e8bf | mov     [rdi+0x630], cx              ; 存储回绕后的 capacity, 无检查

; --- 条目写入: count 是索引, capacity 已不再相关 ---
0x1c000e8cd | movzx   ecx, ax                     ; ecx = count (上方已设, 仍很大)
0x1c000e8d0 | mov     rax, qword [rdi+0x638]      ; rax = 当前缓冲区指针
0x1c000e8d7 | mov     qword [rax+rcx*8], rsi      ; *** OOB 写入 ***
                                                  ; rsi = 条目指针, rcx*8 = 索引
0x1c000e8db | inc     word [rdi+0x632]            ; count++
```

注解：

* `0x1c000e83d`

  –`0x1c000e840`：路径中唯一的比较。它告诉函数 *是否*增长；它**不**验证增长算术。
* `0x1c000e846`

  ：`lea rdx, [rcx*8 + 0x28]`信任回绕后的 capacity。
* `0x1c000e8d7`

  ：破坏性的写入。一旦 `capacity`已回绕并进行了一次新的微小分配，`rcx`(count) 约为 `0xFFFC`，因此 `rcx*8 ≈ 0x7FFE0`字节，远超新缓冲区末端。

### 已修补 — 安全路径与 RTL 安全加法例程 `RtlUShortAdd (sub_1c001c6e4)`

在 `UlpParseNextRequest`中，增长判定后跟随一个 KIR 标志测试来选择检查路径：

```
0x1c000e8ec | movzx   ...