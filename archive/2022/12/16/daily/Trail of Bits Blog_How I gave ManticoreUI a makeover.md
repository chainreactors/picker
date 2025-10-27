---
title: How I gave ManticoreUI a makeover
url: https://blog.trailofbits.com/2022/12/15/manitcoreui-symbolic-execution-gui/
source: Trail of Bits Blog
date: 2022-12-16
fetch_date: 2025-10-04T01:39:28.948246
---

# How I gave ManticoreUI a makeover

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# How I gave ManticoreUI a makeover

Calvin Fong

December 15, 2022

[manticore](/categories/manticore/), [symbolic-execution](/categories/symbolic-execution/)

During my internship at Trail of Bits, I explored the effectiveness of symbolic execution for finding vulnerabilities in native applications ranging from CTF challenges to popular open source libraries like image parsers, focusing on finding ways to enhance [ManticoreUI](https://github.com/trailofbits/ManticoreUI). It is a powerful tool that improves accessibility to symbolic execution and vulnerability discovery, but its usability and efficiency leave much room for improvement. By the end, I implemented new ManticoreUI features that reduce analysis time through emulation, improved shared library support, and enabled symbolic state bootstrapping from GDB to side-step complex program initialization. With these new features, I found and reported a vulnerability in the [DICOM Toolkit (DCTMK)](https://dcmtk.org/dcmtk.php.en), which is a widely deployed set of libraries used in medical imaging!

## The current state of ManticoreUI

[Manticore](https://github.com/trailofbits/manticore) is a symbolic execution engine that emulates applications with symbolic data, as opposed to concrete data. This allows Manticore to test all possible execution paths of its targets. ManticoreUI (MUI) is a [graphical user interface plug-in for Binary Ninja](https://blog.trailofbits.com/2021/11/17/mui-visualizing-symbolic-execution-with-manticore-and-binary-ninja/) that exposes the features of Manticore to users in a simpler way with helpful graphical elements. Its design allows users to reap the benefits of symbolic execution without having to worry about the nitty-gritty of the Manticore API.

[![](/img/wpdump/c4174a708ff759967bbce1086219f45c.png)](/img/wpdump/c4174a708ff759967bbce1086219f45c.png)

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

[![](/img/wpdump/ae789c31539f615dc377d0ad77c1d783.png)](/img/wpdump/ae789c31539f615dc377d0ad77c1d783.png)

Functions with function model implementations shown during startup

The **Add Function Model** command allows users to add a custom hook at the function address to use the function model instead of native code.

[![](/img/wpdump/6ae533b32f0e91dddfb86029dcfb0f7b.png)](/img/wpdump/6ae533b32f0e91dddfb86029dcfb0f7b.png)

Function model selection pop-up

### Global Hooks

Global hooks are another less obvious functionality. These are custom hooks that are triggered for every instruction that gets executed. They can be useful for implementing user-defined tracing functionality, like tracing every syscall that occurs (similar to strace). Alternatively, they can help with performing checks not bound to specific instructions (e.g., a global hook that ends the Manticore run when the RAX register has the value `0xdeadbeef`). They can be added using the **Add/Edit Global Hook** command.

[![](/img/wpdump/5733c197ce78a6461fa52ee27a9135ff.png)](/img/wpdump/5733c197ce78a6461fa52ee27a9135ff.png)

Global hook management pop-up

## Improving the workflow for bug discovery

To address the second and third improvement areas, I implemented new MUI features that facilitate the bug discovery process. The `emulate_until` feature increases the performance of MUI, while shared library support and gdb state dumping improved MUI’s usability in complex targets. These features are described in greater depth below.

### emulate\_until

The `emulate_until` feature is an additional MUI solve option. Setting this value to an address will make Manticore use the Unicorn emulator to concretely emulate your target binary until it reaches the address specified. The Unicorn emulator is far faster than Manticore’s own emulated CPU, which greatly improves execution speed.

[![](/img/wpdump/9d838a0cbf801b31c72df1c9f65e51fc.png)](/img/wpdump/9d838a0cbf801b31c72df1c9f65e51fc.png)

Emulate\_until field in the Manticore run options

I noticed this feature was very useful for C++ binaries, which execute more instructions during initialization. When we symbolically executed a simple benchmark with a `hello world` C++ binary on an Ubuntu 20.04 machine, we observed the following run times:

|  |  |  |
| --- | --- | --- |
|  | Default | `emulate_until` to main |
| Total Duration /s | 311 seconds | 12 seconds |

Evidently, using Unicorn emulation with the `emulate_until` option causes significant performance benefits for even the simplest C++ binaries.

### Shared library support

In vulnerability discovery, we commonly test underlying libraries of an application rather than a full application itself. Such workflows usually involve a simple harness binary that loads the library and calls library functions to be tested. Since MUI supported loading and setting hooks in only a single binary, the use of a harness binary with the shared library was a troublesome workflow for MUI.

With this new feature, users can separately load the shared library in MUI and set up all necessary hooks. Then, they can load the harness binary in MUI and link the Binary Ninja project file of the shared library. During execution, all hooks set in the shared library’s project will be resolved and added to the runtime accordingly.

While not yet implemented, this feature would be well suited for the Ghidra MUI Plugin. Binary Ninja projects contain only single binaries, while Ghidra projects can contain multiple binaries. This feature would enable a more convenient workflow for vulnerability discovery in Ghidra.

### GDB state dumping

I ran into various issues while testing MUI with different targets, including unsupported system calls, unimplemented instructions, and applications that were too complicated to interact with through MUI/Manticore. I also frequently encountered situations where testing the entire application symbolically would lead to state explosion (i.e., too many forked states).

This led me to begin exploring the idea of limiting the use of Manticore’s execution engine. For example, rather than trying to symbolically execute from the start of the application, what about starting execu...