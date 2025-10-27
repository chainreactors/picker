---
title: Debug Visualizations
url: https://binary.ninja/2024/07/15/debug-visualizations.html
source: Binary Ninja
date: 2024-07-16
fetch_date: 2025-10-06T17:42:49.583030
---

# Debug Visualizations

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Debug Visualizations

* [Glenn Smith](https://github.com/CouleeApps)
* 2024-07-15
* [reversing](/tag/reversing), [decompiler](/tag/decompiler)

Decompilation is an incredibly complicated process with a huge number of optimizations, analyses, and transformations happening behind the scenes. Luckily, Binary Ninja has many advanced features that expose access to this internal information. Whether itâs across the ILs, analysis, or the type system, there are tools built in to help display how things work. Not only do we use them internally, but you can leverage them as well to save time and gain understanding! Read on to learn about some of the features that exist for exactly this purpose.

## High Level IL Debug Report

Binary Ninja has a built-in visualization tool for inspecting the steps in the creation of High Level IL (HLIL), and it has been instrumental in helping us build and maintain our decompiler. Check out how the various stages work together to produce the final output:

[

](/blog/images/debug-viz/debug-report-hlil.webm)

You can view the High Level IL Debug Report on your own binaries using the Python command, `current_function.request_debug_report("hlil")`. If you find yourself opening it often, you can use the Snippets plugin to register it as a UI Action with a hotkey. In fact, itâs one of the example scripts included with the plugin, and can be downloaded by running the `update snippets` script.

## Low Level IL: Show Stack Pointer Value

Sometimes analysis runs into problems when branches have diverging Stack Pointer offset values. Either due to anti-analysis obfuscations or incorrectly predicted function call stack adjustments, having a mismatched Stack Pointer leads to incorrect lifting and confusing output. Binary Ninja has a visualization mode built into Low Level IL which is designed to help resolve these errors. For example, here is a function intentionally causing the Stack Pointer to change in a branch that is never taken:

![Function using a technique to break Stack Pointer analysis](/blog/images/debug-viz/llil-sp-ex1.png)

In the disassembly, you can see a â?â tag placed on the continuation block, indicating that Stack Pointer analysis could not resolve the diverging offsets. If we switch to Low Level IL, we can enable Show Stack Pointer Value (from the View Options menu > Advanced sub-menu). This will add annotations to every instruction that modifies the Stack Pointer value, allowing you to observe where the values diverge:

![Enabling Show Stack Pointer Value in Low Level IL](/blog/images/debug-viz/llil-sp-ex2.png)

You can observe how the incoming edges to the block at `20 @ 00004f0d` have `esp` values of both `StackFrameOffset: -0x54` and `StackFrameOffset: -0x50` due to the rogue `esp = esp + 4` anti-analysis feature. Using this information, you can use the âPatch > Convert to NOPâ action on that instruction, allowing Stack Pointer analysis to succeed at this location and propagate further:

![After patching the rogue instruction, the Stack Pointer value no longer diverges in the following Basic Block](/blog/images/debug-viz/llil-sp-ex3.png)

Note that sometimes this will occur within loops, and the incoming Stack Pointer values will both be `UndeterminedValue`. When this happens, itâs often helpful to look for the âUnresolved Stack Pointer Valueâ tags created on any blocks where the incoming Stack Pointer offsets diverged, even if the final result was undetermined. There is also another feature you can use in complicated situationsâ¦

## Stack Adjustment Graph Debug Report

Sometimes, when functions make calls, Binary Ninja cannot automatically determine if the Stack Pointer is adjusted or preserved during the call. In these cases, you can get access to the Stack Adjustment Graph Debug Report and inspect the many steps taken to attempt to resolve the problem. Note that this is actually different from the Unresolved Stack Display, which is the view you can access from the warning message to manually fix up the calls. Observe how Binary Ninja still shows an Unresolved Stack Usage warning for that function. Clicking âView graph of stack usageâ will open the Unresolved Stack Display, where you can find and correct the unresolved call:

![This call has an unresolved stack offset which can be entered manually via the Set Stack Adjustment menu action](/blog/images/debug-viz/unresolved-stack-graph.png)

However, before doing this, you can use the Python command `current_function.request_debug_report("stack_adjust_graph")` to get a thorough breakdown of exactly how Binary Ninja tried (and failed) to follow the Stack Pointer offset through the function:

[

](/blog/images/debug-viz/debug-report-stack.webm)

This display may be helpful for you in determining which calls caused Stack Pointer analysis to fail, since you can see the analysis details over time and pinpoint which places may have caused a problem.

## Lifted IL: Show IL Flag Usage

When writing a lifter, one of the many features you will have to handle is flag usage. Unlike many other disassemblers, Binary Ninja uses a system known as Semantic Flags. In this system, [architectures specify instructions that set and use flags](https://binary.ninja/2021/12/09/guide-to-architecture-plugins-part2.html), but do not calculate their values directly. As a result of this, you may want more insight into how these flags are used in analysis. If you switch to the Lifted IL view (under the IL Type menu > Advanced sub-menu) and enable the Show IL Flag Usage option (under the View Options menu > Advanced sub-menu), additional annotations are added showing flag usage:

![Enabling Show IL Flag Usage adds annotations showing when flags are set and used](/blog/images/debug-viz/il-flag-usage.png)

Notice how each block now has an annotation showing which instruction(s) set each of the flags. Instructions that use these flags, like if-statements, now have annotations showing which instruction set the flags they use. Flag uses are also annotated with their semantic flag groups and the location where those flags were set.

## All ILs: Show IL Opcodes

When writing scripts that interact with the ILs, you usually have to check for the operation of IL instructions youâre processing, but since these operation names are not normally displayed in the UI, it may be difficult to debug the input your script will be getting. To help with this, Binary Ninja has a built-in option in the UI to render the operation of every IL instruction. When the âShow IL Opcodesâ option is enabled (under the View Options menu > Advanced sub-menu), all instructions will be rendered with their operation name and surrounded by parentheses. This rendering mode is available in all levels of ILs, including SSA forms and Pseudo-C. Though the resulting display is verbose, it is very useful for writing scripts using the ILs:

![Enabling Show IL Opcodes lets you see exactly which IL instructions are used](/blog/images/debug-viz/show-il-opcodes.png)

## Medium/High Level IL: Show All Expression Types

When working with Medium Level or High Level ILs, you will often have types applied to expressions in differ...