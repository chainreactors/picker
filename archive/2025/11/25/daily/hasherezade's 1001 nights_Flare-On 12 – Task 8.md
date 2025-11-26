---
title: Flare-On 12 – Task 8
url: https://hshrzd.wordpress.com/2025/11/25/flare-on-12-task-8/
source: hasherezade's 1001 nights
date: 2025-11-25
fetch_date: 2025-11-26T03:15:41.283392
---

# Flare-On 12 – Task 8

[hasherezade's 1001 nights](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

projects and tasks that I do in my free time

[![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/an-electronic-vault-with-a-keypad-containing-only-digits-1.png?w=940&h=198&crop=1)](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

[Skip to content](#content "Skip to content")

* [Home](https://hshrzd.wordpress.com)
* [Projects](https://hshrzd.wordpress.com/mycode/)
  + [PE-sieve](https://hshrzd.wordpress.com/pe-sieve/)
  + [PE\_unmapper](https://hshrzd.wordpress.com/pe_unmapper/)
  + [IAT Patcher](https://hshrzd.wordpress.com/iat-patcher/)
  + [PE-bear](https://hshrzd.wordpress.com/pe-bear/)
  + [ViDi](https://hshrzd.wordpress.com/vidi-visual-disassembler/)
  + [DMA Unlocker](https://hshrzd.wordpress.com/mycode/dma-unlocker/)
* [How to start RE/malware analysis?](https://hshrzd.wordpress.com/how-to-start/)

[← Flare-On 12 – Task 9](https://hshrzd.wordpress.com/2025/11/20/flare-on-12-task-9/)

## [Flare-On 12 – Task 8](https://hshrzd.wordpress.com/2025/11/25/flare-on-12-task-8/)

Posted on [November 25, 2025](https://hshrzd.wordpress.com/2025/11/25/flare-on-12-task-8/ "4:01 am") by [hasherezade](https://hshrzd.wordpress.com/author/hshrzd/ "View all posts by hasherezade")

*In this mini-series I describe the solutions of my favorite tasks from this year’s [Flare-On competition](https://flare-on12.ctfd.io/scoreboard). To those of you who are not familiar, [Flare-On](https://flare-on.com/) is a marathon of reverse engineering. This year it ran for 4 weeks, and consisted of 9 tasks of increasing difficulty. Collection of my sourcecodes created in the process of solving can be found in my Github repository [flareon\_2025](https://github.com/hasherezade/flareon2025).*

This post covers Task 8 – *FlareAuthenticator*, which is an obfuscated Windows binary.

# Overview

Task 8 is a GUI application written in C++/Qt 6. We are instructed to launch it via a batch script that sets the path to the appropriate DLLs.

```
@echo off
set QT_QPA_PLATFORM_PLUGIN_PATH=%~dp0
start %~dp0\FlareAuthenticator.exe
```

For convenience, I simply added this directory to the system `PATH`.

When we run the application, we see the following window:

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/flare_auth.png?w=246)

At this point, the goal of the task becomes clear: by pressing the on-screen buttons, we are supposed to enter a code that will be verified by the authenticator. If we manage to type the correct value, we will obtain the flag. Otherwise the “Wrong Password” popup shows:

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/wrong_pass.png?w=290)

It is worth noticing that button “DEL” activates only when there is an input filled, and the button “OK” – only if the input is of expected size (25 characters).

# IDA

Looking inside the application in IDA, we can see that the code is obfuscated. The patterns suggest that some [OLLVM](https://github.com/obfuscator-llvm/obfuscator?tab=readme-ov-file)-style (LLVM-based) obfuscator was used.

In most functions, attempts to decompile the code do not give us the full result. Only a small fragment is decompiled, and the basic block ends with a jump whose target is calculated on-the-fly.

Below is the first attempt at decompiling the `main` function:

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t8_main_fragment.png?w=1024)

This is how the calculation of the next block looks at the assembly level:

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t8_calculated_jump.png?w=526)

Similarly, calls to other functions are obfuscated: instead of direct calls, the targets are dynamically computed at runtime.

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t9_calc_call_address.png?w=508)

On top of this, the executable is relatively large, relies on asynchronous GUI-driven actions, and calls into various Qt libraries. All of this makes the control flow very hard to follow.

## TinyTracer

In order to grasp this complexity more quickly, I decided to trace the binary’s execution. For this purpose I used my tool **[TinyTracer](https://github.com/hasherezade/tiny_tracer/)** ([v3.2](https://github.com/hasherezade/tiny_tracer/releases/tag/3.2)). As my understanding improved, I kept tweaking its settings.

The goal at this stage was to pinpoint how the input is collected and processed, and what exact condition decides whether the code is considered correct.

### Reducing noise

The executable calls many functions from the Qt DLLs. Most of them are related to setting up the GUI and handling event loops, and are irrelevant to the main objective. A preview of [the first trace log](http://github.com/hasherezade/flareon2025/blob/main/task8/tracelogs/0_default/FlareAuthenticator.exe.tag) looks as follows:

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/t8_initial_tracelog.png?w=672)

The only interesting record in this log is the one where a `QMessageBox` displaying **“Wrong Password”** is shown.

```
8e030;qt6widgets.?warning@QMessageBox@@SA?AW4StandardButton@1@PEAVQWidget@@AEBVQString@@1V?$QFlags@W4StandardButton@QMessageBox@@@@W421@@Z
```

The rest is dominated by cyclical GUI repaint events, which are not really of interest here.

TinyTracer allows us to reduce this noise by [setting exclusions](https://github.com/hasherezade/tiny_tracer/wiki/Exclusions-from-tracing). The latest version can filter out not only individual functions, but also entire libraries, which is especially helpful in this case, where many different APIs are called from the same Qt modules. I set the following list in `excluded.txt`:

```
qt6gui
qt6widgets
qt6core
```

After applying these exclusions, the trace log becomes much cleaner and easier to analyze (example [here](https://github.com/hasherezade/flareon2025/blob/main/task8/tracelogs/1_filtered/FlareAuthenticator.exe.tag)).

### Finding the input collection

While observing the trace log in real time (using **[baretail](https://www.baremetalsoft.com/baretail/)**), I noticed that each button click caused multiple calls to `memcpy` and `strlen` to be appended. I suspected that this behavior must be related to the input collection.

A relevant fragment of the trace log looks like this:

```
[...]
8e280;vcruntime140.memcpy
8e450;ucrtbase.strlen
8e290;vcruntime140.memmove
8e450;ucrtbase.strlen
[...]
```

TinyTracer allows us to [observe both the input and output of selected functions](https://github.com/hasherezade/tiny_tracer/wiki/Tracing-function-input-and-output). To configure which functions we want to watch, we add them to `params.txt` in the tracer’s installation directory. For this step, I filled it with the following definitions:

```
ucrtbase;strlen;1
vcruntime140;memmove;3
```

By default, only the input parameters are watched. If we want to watch the output as well, it can be enabled by editing [TinyTracer.ini](https://github.com/hasherezade/tiny_tracer/wiki/The-INI-file) (details on how to do it are extensively [documented on Wiki](https://github.com/hasherezade/tiny_tracer/wiki/Tracing-function-input-and-output#watching-arguments-modified-by-the-function)). Monitoring the log in real time confirms that those calls are used to copy the input content into some storage buffer.

![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/taking_input.png?w=749)

(Full tracelog from this session available [here](https://github.com/hasherezade/flareon2025/blob/main/task8/tracelogs/2_filtered_args/FlareAuthenticator.exe.tag)).

We can seek via IDA how those interesting APIs were referenced. It leads to two functions that IDA recognizes as `"`append\_to\_string” (`append_to_string_0`, `append_to_string1`):

[![](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/memmove_reft-1.png?w=1024)](https://hshrzd.wordpress.com/wp-content/uploads/2025/11/memmove_reft-1.png)

However, IDA can’t follow statically where exactly those functions are ca...