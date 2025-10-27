---
title: SilentMoonwalk - PoC Implementation Of A Fully Dynamic Call Stack Spoofer
url: https://buaq.net/go-157793.html
source: unSafe.sh - 不安全
date: 2023-04-10
fetch_date: 2025-10-04T11:29:27.165702
---

# SilentMoonwalk - PoC Implementation Of A Fully Dynamic Call Stack Spoofer

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

![](https://8aqnet.cdn.bcebos.com/9a2a8cb17f80bb2a3e61e9ab6072c5ef.jpg)

SilentMoonwalk - PoC Implementation Of A Fully Dynamic Call Stack Spoofer

PoC Implementation of a fully dynamic call stack spoofer TL;DR SilentMoonwalk is a PoC imp
*2023-4-9 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-157793.htm)
阅读量:35
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhmSfRk3ueboBYs7Ns4as2tc1nPt_hjpY6G69_Z_jEZlF4fgo6ptapaRxxl5sBPzAU0r0wxzs2umTbKbvguUJ0DFS_4ccFbQ7einfQw63uZrYSWjLFfdUp2wTUX3ko51mrKEYGpMBR1PUdN9bh_P5GyRnAiv51GocaQy6hu7YbtbXuZ92fQxU0G7VxPeg=w640-h334)](https://blogger.googleusercontent.com/img/a/AVvXsEhmSfRk3ueboBYs7Ns4as2tc1nPt_hjpY6G69_Z_jEZlF4fgo6ptapaRxxl5sBPzAU0r0wxzs2umTbKbvguUJ0DFS_4ccFbQ7einfQw63uZrYSWjLFfdUp2wTUX3ko51mrKEYGpMBR1PUdN9bh_P5GyRnAiv51GocaQy6hu7YbtbXuZ92fQxU0G7VxPeg)

PoC Implementation of a fully dynamic call stack spoofer

## TL;DR

SilentMoonwalk is a PoC implementation of a fully dynamic call stack spoofer, implementing a technique to remove the original caller from the call stack, using ROP to desynchronize unwinding from control flow.

## Authors

This PoC is the result of a joint research done on the topic of stack spoofing. The authors of the research are:

* [KlezVirus](https://twitter.com/KlezVirus "KlezVirus")
* [Waldo-IRC](https://twitter.com/waldoirc "Waldo-IRC")
* [Trickster0](https://twitter.com/trickster012 "Trickster0")

I want to stress that this work would have been impossible without the work of [Waldo-IRC](https://twitter.com/waldoirc "Waldo-IRC") and [Trickster0](https://twitter.com/trickster012 "Trickster0"), which both contributed to the early stages of the PoC, and to the research behind the PoC.

## Overview

This repository demonstrates a PoC implementation to spoof the call stack when calling arbitrary Windows APIs.

This attempt was inspired by [this Twitter thread](https://twitter.com/_Kudaes_/status/1594753842310434816 "this Twitter thread"), and [this Twitter thread](https://twitter.com/namazso/status/1442314742488567808 "this Twitter thread"), where sensei [namazso](https://twitter.com/namazso "namazso") showed and suggested to extend the stack unwinding approach with a ROP chain to both desynchronize the unwinding from real control flow and restore the original stack afterwards.

This PoC attempts to do something similar to the above, and uses a desync stack to completely hide the original call stack, also removing the EXE image base from it. Upon return, a ROP gadget is invoked to restore the original stack. In the code, this process is repeated 10 times in a loop, using different frames at each iteration, to prove stability.

### Supported Modes

The tool currently supports 2 modes, where one is actually a wrong patch to a non-working pop RBP frame identified, which operates by shifting the current RSP and adding two fake frames to the call stack. As it operates using synthetic frames, I refer to this mode as "SYNTHETIC".

When selecting the frame that unwinds by popping the RBP register from the stack, the tool might select an unsuitable frame, ending up in an abruptly cut call stack, as observable below.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgt64mTK4Wd7s7QLYBGU1EarC8kUNEoBqWxT0e7dR7fRT3yqqDVWySIrmdC7pePnhN7U0VoUiYR9YUWpD_cE0RaX1w0gnRilBt4G5MbRk51b4xQ9u66dHo0FnFQ0K_lvBsAcfNnqWTf4wFZpqSNNy2NpeJ1XACEdbVvfF2wRrapUdlhkb7xTHCeBJTfDw=w640-h308)](https://blogger.googleusercontent.com/img/a/AVvXsEgt64mTK4Wd7s7QLYBGU1EarC8kUNEoBqWxT0e7dR7fRT3yqqDVWySIrmdC7pePnhN7U0VoUiYR9YUWpD_cE0RaX1w0gnRilBt4G5MbRk51b4xQ9u66dHo0FnFQ0K_lvBsAcfNnqWTf4wFZpqSNNy2NpeJ1XACEdbVvfF2wRrapUdlhkb7xTHCeBJTfDw)

### Synthetic Call Stack Mode

A silly solution to the problem would be to create two fake frames and link them back to the cut call stack. This would create a sort of apparently legit call stack, even without a suitable frame which unwinds calling POP RBP, but:

* You would lose the advantage of the desync technique
* The stack would be still unwindable
* The resulting call stack could seem legit just on the first glance, but it would probably not pass a strict check

The result of the \_synthetic spoof can be observed in the image below:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjYXJZU-bj7MCgeMQ0fzznA3UMdP36Wv63MaKHuZ4z1daiFlVn0fLsh4dm1kNsv3pm8r3Q_dmsRvrtOvW4eMyyxHZ9ZXbgv6VyPC2-pUIEB9m3ndOWDAWDooMrf7Vgy0Wm1lEDS_ui5uPiFJNzFxbdTIcTrGHkGBZN1-U5HELCTvKLiBKmgkOObuy1fMg=w640-h284)](https://blogger.googleusercontent.com/img/a/AVvXsEjYXJZU-bj7MCgeMQ0fzznA3UMdP36Wv63MaKHuZ4z1daiFlVn0fLsh4dm1kNsv3pm8r3Q_dmsRvrtOvW4eMyyxHZ9ZXbgv6VyPC2-pUIEB9m3ndOWDAWDooMrf7Vgy0Wm1lEDS_ui5uPiFJNzFxbdTIcTrGHkGBZN1-U5HELCTvKLiBKmgkOObuy1fMg)

*Figure 1: [Windows 10](https://www.kitploit.com/search/label/Windows%2010 "Windows 10") - Apparently Legit, non unwoundable call stack whereby the EXE module was completely removed (calling no parameters function getchar)*

*Note: This operation mode is disabled by default. To enable this mode, change the CALLSTACK\_TYPE to 1*

### Desync Stack Mode

This mode is the right solution to the above problem, whereby the non-suitable frame is simply replaced by another, suitable one.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhmSfRk3ueboBYs7Ns4as2tc1nPt_hjpY6G69_Z_jEZlF4fgo6ptapaRxxl5sBPzAU0r0wxzs2umTbKbvguUJ0DFS_4ccFbQ7einfQw63uZrYSWjLFfdUp2wTUX3ko51mrKEYGpMBR1PUdN9bh_P5GyRnAiv51GocaQy6hu7YbtbXuZ92fQxU0G7VxPeg=w640-h334)](https://blogger.googleusercontent.com/img/a/AVvXsEhmSfRk3ueboBYs7Ns4as2tc1nPt_hjpY6G69_Z_jEZlF4fgo6ptapaRxxl5sBPzAU0r0wxzs2umTbKbvguUJ0DFS_4ccFbQ7einfQw63uZrYSWjLFfdUp2wTUX3ko51mrKEYGpMBR1PUdN9bh_P5GyRnAiv51GocaQy6hu7YbtbXuZ92fQxU0G7VxPeg)

*Figure 2: Windows 10 - Legit, unwoundable call stack whereby the EXE module was completely removed (calling 4 parameters function MessageBoxA)*

## Utility

In the repository, you can find also a little util to inspect runtime functions, which might be useful to analyse runtime function entries.

```
UnwindInspector.exe -h

Unwind Inspector v0.100000

Mandatory args:
```

Sample Output:

```
UnwindInspector.exe -m kernelbase -a 0x7FFAAE12182C
[*] Using function address 0x7ffaae12182c

Runtime Function (0x000000000000182C, 0x00000000000019ED)
  Unwind Info Address: 0x000000000026AA88
    Version: 0
    Ver + Flags: 00000000
    SizeOfProlog: 0x1f
    CountOfCodes: 0xc
    FrameRegister: 0x0
    FrameOffset: 0x0
    UnwindCodes:
    [00h] Frame: 0x741f - 0x04  - UWOP_SAVE_NONVOL     (RDI, 0x001f)
    [01h] Frame: 0x0015 - 0x00  - UWOP_PUSH_NONVOL     (RAX, 0x0015)
    [02h] Frame: 0x641f - 0x04  - UWOP_SAVE_NONVOL     (RSI, 0x001f)
    [03h] Frame: 0x0014 - 0x00  - UWOP_PUSH_NONVOL     (RAX, 0x0014)
    [04h] Frame: 0x341f - 0x04  - UWOP_SAVE_NONVOL     (RBX, 0x001f)
    [05h] Frame: 0x0012 - 0x00  - UWOP_PUSH_NONVOL     (RAX, 0x0012)
    [06h] Frame: 0xb21f - 0x02  - UWOP_ALLOC_SMALL     (R11, 0x001f)
    [07h] Frame: 0xf018 - 0x00  - UWOP_PUSH_NONVOL     (R15, 0x0018)
    [0   8h] Frame: 0xe016 - 0x00  - UWOP_PUSH_NONVOL     (R14, 0x0016)
    [09h] Frame: 0xd014 - 0x00  - UWOP_PUSH_NONVOL     (R13, 0x0014)
    [0ah] Frame: 0xc012 - 0x00  - UWOP_PUSH_NONVOL     (R12, 0x0012)
    [0bh] Frame: 0x5010 - 0x00  - UWOP_PUSH_NONVOL     (RBP, 0x0010)
```

## Build

In order to build the POC and observe a similar behaviour to the one in the picture, ensure to:

* Disable GS (`/GS-`)
* Disable Code Optimisation (`/Od`)
* Disable Whole Program Optimisation (Remove `/GL`)
* Disable size and speed preference (Remove `/Os`, `/Ot`)
* **Enable** intrinsic if not enabled (`/Oi`)

## Previous Work

It's worth mentioning previous work done on this topic, which built t...