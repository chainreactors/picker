---
title: c-ares TCP Use-After-Free 漏洞深度解析：从 DNS 响应序列到本地 Calculator 代码执行 PoC
url: https://mp.weixin.qq.com/s/fyubodc5SwWNAtvElTdovA
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:06:59.277161
---

# c-ares TCP Use-After-Free 漏洞深度解析：从 DNS 响应序列到本地 Calculator 代码执行 PoC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0EDIyXRvKxKnIaxDcahHMg9LWqOQjPwvt46rgrnFccjosdMPaKQicNeJQQaWleAqKRrzxe1VMFjZeia9lsgibNVvSzSFaoxe9XINk/0?wx_fmt=jpeg)

# c-ares TCP Use-After-Free 漏洞深度解析：从 DNS 响应序列到本地 Calculator 代码执行 PoC

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

今天我们来深入剖析一个近期公开的 c-ares 库中的 TCP Use-After-Free（UAF）漏洞，并一步步讲解作者提供的本地 Calculator Proof-of-Concept（Po C）。

这个 PoC 不仅能触发漏洞，还能实现受控的代码执行（虽然是 benign 的本地 calculator 作为 payload 演示）。

文章会非常详细，从基础知识到漏洞成因、PoC 运行原理、构建步骤、影响范围，再到缓解措施，一一拆解。即使你是初学者，也能跟得上。

一、什么是 c-ares？

c-ares 是一个用 C 语言编写的异步 DNS 解析器库。它被广泛用于需要高性能、非阻塞 DNS 查询的场景，比如：

* curl / libcurl（异步后端之一）
* Node.js（历史 vendored）
* gRPC（默认 DNS resolver）
* Envoy Proxy
* Wireshark
* 各种 Python/Rust/C++ 项目中的异步 DNS 组件

它支持 UDP 和 TCP 传输、EDNS 等高级特性，专注于安全和跨平台。为什么重要？ 许多大型系统和应用都直接或间接依赖它。一旦出现内存安全漏洞（如 UAF），潜在影响面很广。

二、Use-After-Free（UAF）漏洞基础

Use-After-Free 是内存腐败漏洞的一种：

1. 程序分配一块内存（heap 对象）。
2. 代码逻辑错误导致这块内存被提前释放（free）。
3. 后续代码仍然持有指向这块已释放内存的指针，并继续使用它（use）。
4. 攻击者如果能控制已释放内存的内容（heap shaping / spray），就能劫持指针指向的数据（如函数指针），实现任意代码执行或崩溃。

在这个 PoC 中，UAF 发生在 TCP DNS 查询处理路径 的 ares\_getaddrinfo() 中，具体与 EDNS 重试和连接重置相关。

三、漏洞触发路径详解

PoC 重现的精确路径如下（非常关键）：

* API：ares\_getaddrinfo()
* 传输：DNS over TCP（ARES\_FLAG\_USEVC）
* Channel 配置：ARES\_FLAG\_EDNS + DNS-only lookups（opts.lookups = "b"）
* 服务器行为（PoC 自带 loopback DNS-over-TCP server）

1. 接收 TCP DNS 查询。
2. 在一次 read 中返回两个响应（相同 query id）：

   第一个：FORMERR（格式错误），无 OPT 数据 → 触发 EDNS 重试逻辑。

   第二个：成功的空响应（same query id）。
3. 接受重试的 write。
4. 重置 TCP 连接（在下一次 internal lookup write 之前）。

核心问题：连接重置后，某些查询相关的状态（ares\_query\_t 中的 node\_queries\_by\_timeout 等）变成了 stale（过时）指针。在后续的 query cleanup 过程中（如 read\_answers() → ares\_process()），这些 stale 状态被使用，导致 UAF。

通过公共的 ares\_library\_init\_mem() allocator hook，PoC 可以精确塑造 heap 布局，让 stale 指针指向精心构造的 skip-list node。最终控制流：

```
ares_slist_node_destroy(node) → node->parent->destruct(node->data) → proof_marker() // 攻击者控制的函数
```

GDB 证据显示调用链清晰：proof\_marker() ← ares\_slist\_node\_destroy() ← ... ← ares\_process() ← main()。

这不是简单崩溃，而是受控间接调用，证明了代码执行潜力。

四、PoC 结构与文件说明

https://github.com/bikini/exploitarium/tree/main/c-ares-tcp-uaf-calc-poc

仓库目录：c-ares-tcp-uaf-calc-poc

* poc/cares\_tcp\_uaf\_calc\_poc.c：核心 PoC 代码（standalone C 程序 + benign payload）。
* scripts/build\_from\_checkout.sh：从指定 c-ares checkout 构建静态库并链接 PoC。
* scripts/run\_until\_hit.sh：因 heap 布局概率性，自动重试直到命中。
* evidence/：GDB 栈 trace、验证日志等证据。
* README.md：完整文档（本文主要基于此）。

Payload 行为：

* 写入 /tmp/cares\_rce\_proof\_latest 标记文件。
* 尝试启动计算器（优先 WSL Windows calc → Linux 常见计算器）。
* 成功输出类似 CARES\_RCE\_PAYLOAD\_TRIGGERED。

五、如何构建和运行（超详细步骤）

环境要求（Linux 或 WSL）：

* gcc、cmake、git
* POSIX sockets + pthreads

步骤 1：准备 c-ares 源码

```
# 构建 upstream maingit clone --depth 1 https://github.com/c-ares/c-ares.git /tmp/c-ares-main# 或指定 release（v1.34.6）git clone --depth 1 --branch v1.34.6 https://github.com/c-ares/c-ares.git /tmp/c-ares-v1.34.6
```

步骤 2：构建 PoC

```
cd /path/to/exploitarium/c-ares-tcp-uaf-calc-poc./scripts/build_from_checkout.sh /tmp/c-ares-main /tmp/c-ares-main-build ./cares_tcp_uaf_calc_poc
```

（类似地构建 v1.34.6）

步骤 3：运行

```
chmod +x ./cares_tcp_uaf_calc_poc./scripts/run_until_hit.sh ./cares_tcp_uaf_calc_poc
```

成功标志：

* 看到 CARES\_RCE\_PAYLOAD\_TRIGGERED
* 计算器弹出
* /tmp/cares\_rce\_proof\_latest 文件生成

可靠性：heap-layout 敏感，但本地验证经常 run=1 即命中。多次运行也很稳定。

六、已验证目标

* c-ares upstream main（commit c93e50f...）：命中
* v1.34.6（最新官方 release at PoC 时间）：命中

注意：这是本地 harness，不是通用远程 exploit。它证明在特定路径 + allocator shaping + cleanup 条件下可达代码执行。实际应用 exploitability 取决于很多因素（见下文 Limits）。

七、影响范围

c-ares 被大量项目使用。需要检查的具体产品包括：

* Node.js（bundled cares）
* gRPC（默认 resolver ）
* Envoy Proxy（默认 DNS）
* curl（可选异步 backend）
* Wireshark、Python async 库（pycares、aiodns）、Rust crates 等

八、为什么这是代码执行而非单纯崩溃？

PoC 没有停留在“写坏指针导致 segfault”，而是通过 allocator hook 塑造 skip-list node，让 destruct 函数指针指向 proof\_marker()。GDB 确认 IP 控制在 marker 函数，且下方栈帧全是 c-ares 代码。这为真实 RCE 提供了强证据（在支持 heap shaping 的场景下）。

九、限制与实际利用难度

* 需要应用使用受影响的 ares\_getaddrinfo() + TCP + EDNS 路径。
* 需要 attacker 可控的 DNS 服务器（或中间人）发送特定响应序列。
* 高度依赖目标进程的 heap 布局和 allocator 行为。
* 沙箱、mitigations（如 ASLR、heap hardening）、重启模型都会影响成败。
* 不是 drop-in exploit，仅为研究证明。

十、缓解措施

首选：等待上游 c-ares 官方修复，升级到 patched 版本，所有静态链接应用必须重新构建。

短期绕过：

* 避免对不可信 resolver 强制 DNS over TCP。
* 沙箱化 DNS 相关进程。
* 监控 DNS 服务异常崩溃。
* 清点所有静态 bundled c-ares 副本。

动态链接用户更新系统库 + 重启即可；静态链接必须产品级更新。

十一、总结与思考

这个 PoC 再次提醒我们：即使是成熟的底层库，也可能在复杂的状态机（TCP 重试、EDNS、cleanup）中隐藏 UAF。DNS 解析作为互联网基础，安全风险被低估时，后果可能波及整个生态。

研究者通过 loopback server + allocator hook + 精确响应序列，优雅地证明了从 UAF 到控制流劫持的路径，值得学习。责任使用声明：仅在本地研究环境、自己拥有的系统或明确授权的 lab 中运行 PoC。切勿用于非法目的。想复现的同学，建议先在干净的 Linux/WSL 环境中按步骤操作，并用 GDB 观察调用链，会收获更多。

参考仓库：https://github.com/bikini/exploitarium/tree/main/c-ares-tcp-uaf-calc-poc欢迎留言讨论 DNS 安全、内存漏洞利用技巧，或其他类似 PoC 分析。如果你有特定应用想检查是否受影响，也可以提供更多细节一起探讨。

（本文基于公开 GitHub PoC 整理，所有技术细节均来自公开来源。如有更新，请以官方 c-ares 发布为准。）

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FXqSyPb7qZOuQ5fxUlic0p6tZVZJPG2vKXav2UPicnd2xOupiby9TcKZ46dmFxSHg0icaWskKA1yuSGfZ8HC7ndnu8ZtUKDUWOGmU/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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