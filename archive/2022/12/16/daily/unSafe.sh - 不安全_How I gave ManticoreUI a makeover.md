---
title: How I gave ManticoreUI a makeover
url: https://buaq.net/go-140166.html
source: unSafe.sh - 不安全
date: 2022-12-16
fetch_date: 2025-10-04T01:39:02.167972
---

# How I gave ManticoreUI a makeover

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

![](https://8aqnet.cdn.bcebos.com/448a16a001f96f4b9eabe72608c6a521.jpg)

How I gave ManticoreUI a makeover

By Calvin FongDuring my internship at Trail of Bits, I explored the effectivenes
*2022-12-15 21:0:23
Author: [blog.trailofbits.com(查看原文)](/jump-140166.htm)
阅读量:25
收藏*

---

***By Calvin Fong***

During my internship at Trail of Bits, I explored the effectiveness of symbolic execution for finding vulnerabilities in native applications ranging from CTF challenges to popular open source libraries like image parsers, focusing on finding ways to enhance [ManticoreUI](https://github.com/trailofbits/ManticoreUI). It is a powerful tool that improves accessibility to symbolic execution and vulnerability discovery, but its usability and efficiency leave much room for improvement. By the end, I implemented new ManticoreUI features that reduce analysis time through emulation, improved shared library support, and enabled symbolic state bootstrapping from GDB to side-step complex program initialization. With these new features, I found and reported a vulnerability in the [DICOM Toolkit (DCTMK)](https://dcmtk.org/dcmtk.php.en), which is a widely deployed set of libraries used in medical imaging!

## The current state of ManticoreUI

[Manticore](https://github.com/trailofbits/manticore) is a symbolic execution engine that emulates applications with symbolic data, as opposed to concrete data. This allows Manticore to test all possible execution paths of its targets. ManticoreUI (MUI) is a [graphical user interface plug-in for Binary Ninja](https://blog.trailofbits.com/2021/11/17/mui-visualizing-symbolic-execution-with-manticore-and-binary-ninja/) that exposes the features of Manticore to users in a simpler way with helpful graphical elements. Its design allows users to reap the benefits of symbolic execution without having to worry about the nitty-gritty of the Manticore API.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/Screenshot-2022-12-13-at-2.31.43-PM.png?resize=690%2C600&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/Screenshot-2022-12-13-at-2.31.43-PM.png?ssl=1)

An example of the GUI.

One of my goals was to improve MUI’s user experience for finding vulnerabilities. I spent some time using MUI in CTF challenges, on artificially created vulnerable code samples, and on some small real-world targets. From this, I determined three general directions for improvement:

* I realized that many non-default features were not obvious to new or inexperienced Manticore users. These features were sometimes implemented in code but not covered in the documentation.
* I also noticed that real-world software targets were significantly more challenging to approach than smaller samples like CTF challenges. CTF challenges tend to be small command-line applications that typically receive input from standard input. However, there are many application types in the real world, including network services, daemons, and libraries. And the MUI user experience was very different for each type.
* Lastly, when testing software that processes large inputs, like format parsers with big iterating loops or complex C++ binaries, MUI’s emulation was obviously much slower than the execution speed of a real CPU.

## Exposing useful features through ManticoreUI

To address the first improvement area, I made two of MUI’s useful features—function models and global hooks—more obvious to users.

### Function models

Function models are Python re-implementations of common library functions with awareness of Manticore’s symbolic execution engine. These models override actual library functions during symbolic execution. This improves performance because Manticore does not have to emulate each native instruction individually.

ManticoreUI now prompts when there are library functions that could be substituted with an existing function model implementation, as shown below:

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/function_model.png?resize=555%2C153&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/function_model.png?ssl=1)

Functions with function model implementations shown during startup

The **Add Function Model** command allows users to add a custom hook at the function address to use the function model instead of native code.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/function_pop_up.png?resize=420%2C271&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/function_pop_up.png?ssl=1)

Function model selection pop-up

### Global Hooks

Global hooks are another less obvious functionality. These are custom hooks that are triggered for every instruction that gets executed. They can be useful for implementing user-defined tracing functionality, like tracing every syscall that occurs (similar to strace). Alternatively, they can help with performing checks not bound to specific instructions (e.g., a global hook that ends the Manticore run when the RAX register has the value `0xdeadbeef`). They can be added using the **Add/Edit Global Hook** command.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/Global_hooks.png?resize=420%2C279&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/Global_hooks.png?ssl=1)

Global hook management pop-up

## Improving the workflow for bug discovery

To address the second and third improvement areas, I implemented new MUI features that facilitate the bug discovery process. The `emulate_until` feature increases the performance of MUI, while shared library support and gdb state dumping improved MUI’s usability in complex targets. These features are described in greater depth below.

### emulate\_until

The `emulate_until` feature is an additional MUI solve option. Setting this value to an address will make Manticore use the Unicorn emulator to concretely emulate your target binary until it reaches the address specified. The Unicorn emulator is far faster than Manticore’s own emulated CPU, which greatly improves execution speed.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/Emulate_until.png?resize=620%2C531&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2022/12/Emulate_until.png?ssl=1)

Emulate\_until field in the Manticore run options

I noticed this feature was very useful for C++ binaries, which execute more instructions during initialization. When we symbolically executed a simple benchmark with a `hello world` C++ binary on an Ubuntu 20.04 machine, we observed the following run times:

|  |  |  |
| --- | --- | --- |
|  | Default | `emulate_until` to main |
| Total Duration /s | 311 seconds | 12 seconds |

Evidently, using Unicorn emulation with the `emulate_until` option causes significant performance benefits for even the simplest C++ binaries.

### Shared library support

In vulnerability discovery, we commonly test underlying libraries of an application rather than a full application itself. Such workflows usually involve a simple harness binary that loads the library and calls library functions to be tested. Since MUI supported loading and setting hooks in only a single binary, the use of a harness binary with the shared library was a troublesome workflow for MUI.

With this new feature, users can separately load the shared library in MUI and set up all necessary hooks. Then, they can load the harness binary in MUI and link the Binary Ninja project file of the shared library. During execution, all hooks set in the shared library’s project will be resolved and added to the runtim...