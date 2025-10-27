---
title: Wasm core dumps and debugging Rust in Cloudflare Workers
url: https://buaq.net/go-174425.html
source: unSafe.sh - 不安全
date: 2023-08-15
fetch_date: 2025-10-04T11:59:45.404354
---

# Wasm core dumps and debugging Rust in Cloudflare Workers

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/5d7bc637c345823bc91ecbe6da9edac1.jpg)

Wasm core dumps and debugging Rust in Cloudflare Workers

Loading...
*2023-8-14 21:0:33
Author: [blog.cloudflare.com(查看原文)](/jump-174425.htm)
阅读量:24
收藏*

---

Loading...

* [![Sven Sauleau](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/https://blog-cloudflare-com-assets.storage.googleapis.com/2020/09/7cBY6-H7_400x400--1-.jpg)](https://blog.cloudflare.com/author/sven/)
* [![Celso Martinho](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2022/08/Celso-Martinho.png)](https://blog.cloudflare.com/author/celso/)

![Wasm core dumps and debugging Rust in Workers](https://blog.cloudflare.com/content/images/2023/08/image4-5.png)

A clear sign of maturing for any new programming language or environment is how easy and efficient debugging them is. Programming, like any other complex task, involves various challenges and potential pitfalls. Logic errors, off-by-ones, null pointer dereferences, and memory leaks are some examples of things that can make software developers desperate if they can't pinpoint and fix these issues quickly as part of their workflows and tools.

[WebAssembly](https://webassembly.org/) (Wasm) is a binary instruction format designed to be a portable and efficient target for the compilation of high-level languages like [Rust](https://www.rust-lang.org/), C, C++, and others. In recent years, it has gained significant traction for building high-performance applications in web and serverless environments.

Cloudflare Workers has had [first-party support for Rust and Wasm](https://github.com/cloudflare/workers-rs) for quite some time. We've been using this powerful combination to bootstrap and build some of our most recent services, like [D1](https://blog.cloudflare.com/introducing-d1/), [Constellation](https://blog.cloudflare.com/introducing-constellation/), and [Signed Exchanges](https://blog.cloudflare.com/automatic-signed-exchanges/), to name a few.

Using tools like [Wrangler](https://github.com/cloudflare/workers-sdk), our command-line tool for building with Cloudflare developer products, makes streaming real-time logs from our applications running remotely easy. Still, to be honest, debugging Rust and Wasm with Cloudflare Workers involves a lot of the good old time-consuming and nerve-wracking [printf'ing](https://news.ycombinator.com/item?id=26925570) strategy.

What if there’s a better way? This blog is about enabling and using Wasm core dumps and how you can easily debug Rust in Cloudflare Workers.

### What are core dumps?

In computing, a [core dump](https://en.wikipedia.org/wiki/Core_dump) consists of the recorded state of the working memory of a computer program at a specific time, generally when the program has crashed or otherwise terminated abnormally. They also add things like the processor registers, stack pointer, program counter, and other information that may be relevant to fully understanding why the program crashed.

In most cases, depending on the system’s configuration, core dumps are usually initiated by the operating system in response to a program crash. You can then use a debugger like [gdb](https://linux.die.net/man/1/gdb) to examine what happened and hopefully determine the cause of a crash. [gdb](https://linux.die.net/man/1/gdb) allows you to run the executable to try to replicate the crash in a more controlled environment, inspecting the variables, and much more. The Windows' equivalent of a core dump is a [minidump](https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/read-small-memory-dump-file). Other mature languages that are interpreted, like Python, or languages that run inside a virtual machine, like [Java](https://docs.oracle.com/javase/8/docs/technotes/guides/visualvm/coredumps.html), also have their ways of generating core dumps for post-mortem analysis.

Core dumps are particularly useful for post-mortem debugging, determining the conditions that lead to a failure after it has occurred.

### WebAssembly core dumps

WebAssembly has had a [proposal for implementing core dumps](https://github.com/WebAssembly/tool-conventions/blob/main/Coredump.md) in discussion for a while. It's a work-in-progress experimental specification, but it provides basic support for the main ideas of post-mortem debugging, including using the [DWARF](https://yurydelendik.github.io/webassembly-dwarf/) (debugging with attributed record formats) debug format, the same that Linux and gdb use. Some of the most popular Wasm runtimes, like [Wasmtime](https://github.com/bytecodealliance/wasmtime/pull/5868) and [Wasmer](https://github.com/wasmerio/wasmer/pull/3626), have experimental flags that you can enable and start playing with Wasm core dumps today.

If you run Wasmtime or Wasmer with the flag:

```
--coredump-on-trap=/path/to/coredump/file
```

The core dump file will be emitted at that location path if a crash happens. You can then use tools like [wasmgdb](https://github.com/xtuc/wasm-coredump/tree/main/bin/wasmgdb) to inspect the file and debug the crash.

But let's dig into how the core dumps are generated in WebAssembly, and what’s inside them.

### How are Wasm core dumps generated

(and what’s inside them)

When WebAssembly terminates execution due to abnormal behavior, we say that it entered a trap. With Rust, examples of operations that can trap are accessing out-of-bounds addresses or a division by zero arithmetic call. You can read about the [security model of WebAssembly](https://webassembly.org/docs/security/) to learn more about traps.

The core dump specification plugs into the trap workflow. When WebAssembly crashes and enters a trap, core dumping support kicks in and starts unwinding the call [stack](https://webassembly.github.io/spec/core/exec/runtime.html#stack) gathering debugging information. For each frame in the stack, it collects the [function](https://webassembly.github.io/spec/core/syntax/modules.html#syntax-func) parameters and the values stored in locals and in the stack, along with binary offsets that help us map to exact locations in the source code. Finally, it snapshots the [memory](https://webassembly.github.io/spec/core/syntax/modules.html#syntax-mem) and captures information like the [tables](https://webassembly.github.io/spec/core/syntax/modules.html#syntax-table) and the [global variables](https://webassembly.github.io/spec/core/syntax/modules.html#syntax-global).

[DWARF](https://dwarfstd.org/) is used by many mature languages like C, C++, Rust, Java, or Go. By emitting DWARF information into the binary at compile time a debugger can provide information such as the source name and the line number where the exception occurred, function and argument names, and more. Without DWARF, the core dumps would be just pure assembly code without any contextual information or metadata related to the source code that generated it before compilation, and they would be much harder to debug.

WebAssembly [uses a (lighter) version of DWARF](https://webassembly.github.io/spec/core/appendix/custom.html#name-section) that maps functions, or a module and local variables, to their names in the source code (you can read about the [WebAssembly name section](https://webassembly.github.io/spec/core/appendix/custom.html#name-section) for more information), and naturally core dumps use this information.

All this information for debugging is then bundled together and saved to the file, the core dump file.

The [core dump structure](https://github.com/WebAssembly/tool-conventions/blob/main/Coredump.md#coredump-file-f...