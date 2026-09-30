---
title: Debugger Conditional Breakpoints and the Expression Parser That Backs Them
url: https://binary.ninja/2026/09/29/debugger-conditional-breakpoint.html
source: Binary Ninja
date: 2026-09-29
fetch_date: 2026-09-30T07:42:10.973687
---

# Debugger Conditional Breakpoints and the Expression Parser That Backs Them

[Skip to main content](#main-content)

[![Binary Ninja](/images/binary-ninja-wordmark-light-2tone.svg)](/)

Features

[Features Overview](/features/)
[Enterprise](/enterprise/)

[Sidekick](https://sidekick.binary.ninja)
[Portal](https://portal.binary.ninja/dashboard)
[Training](/training/)

Support

[Support Overview](/support/)
[Extended Support](/support/extended.html)
[Documentation](/support/#documentation)
[License/Installer Recovery](/recover/)
[Renew Current License](/renew/)
[Slack Signup](https://slack.binary.ninja/)
[FAQ](/faq/)
[Sponsorship Information](/sponsorship/)
[Contact Us](/support/)

[Blog](/blog/)
[Gear](https://shop.binary.ninja)

[Try For Free](/free)
[Purchase](/purchase)

Not a bird, a plane, it's [Binary Ninja 6.0](/2026/09/03/binary-ninja-6.0-krypton.html)! A
super-powered release with more improvements than ever. Massive performance gains, binary similarity, TMS320C6x, MCP, and much more.

[Binary Ninja Blog](/blog/)

# Debugger Conditional Breakpoints and the Expression Parser That Backs Them

By [Xusheng Li](https://github.com/xusheng6)
 2026-09-29

In Binary Ninjaâs debugger, when you set a breakpoint and add a condition like `rax == 0x1234`, it just works. Letâs take a look into how that works and what sorts of conditions you can use.

This post tells the story of the [conditional breakpoint](https://docs.binary.ninja/guide/debugger/index.html#conditional-breakpoints) with a side-quest to explore Binary Ninjaâs [expression parser](https://api.binary.ninja/binaryninja.binaryview-module.html#binaryninja.binaryview.BinaryView.parse_expression) which is the feature that makes it possible.

## It Started with Navigation

If youâve used Binary Ninja, youâve probably pressed `G` to open the navigation dialog and typed in a function name. But did you know that dialog is powered by a full expression parser? This means you can type `main + 0x10` to navigate 16 bytes past the start of `main`, or `.text + 0x100` to jump to an offset within a section, or even `[.data + 0x20]` to dereference a pointer.

The expression parser can do a lot more than you would probably guess. Hereâs some examples:

### Expression Parser Capabilities

| Feature | Example | Description |
| --- | --- | --- |
| Arithmetic | `main + 0x10` | Navigate 16 bytes after main |
| Sections | `.text + 0x100` | Offset into a section |
| Symbols | `data_00005000` | Unnamed data variables |
| Dereference | `[.data + 0x20]` | Read pointer at address |
| Size suffix | `[.data + 0x20].q` | Read 8 bytes (quadword) |
| Special values | `$here`, `$start`, `$end` | Current address, file boundaries |

The supported operators include arithmetic (`+`, `-`, `*`, `/`, `%`), bitwise operations (`&`, `|`, `^`, `~`), comparisons (`==`, `!=`, `>`, `<`, `>=`, `<=`), and grouping with parentheses.

For memory dereferences, you can specify the size: `[expr].b` for a byte, `[expr].w` for a word, `[expr].d` for a dword, and `[expr].q` for a quadword. Without a suffix, it reads an address-sized value.

Numbers default to hexadecimal, but you can use `0n10` for decimal or `010` for octal when needed.

For the complete specification, see the [parse\_expression API documentation](https://api.binary.ninja/binaryninja.binaryview-module.html#binaryninja.binaryview.BinaryView.parse_expression).

## Making It Dynamic: Magic Values

The expression parser becomes even more powerful during debugging thanks to âmagic valuesâ which are name-value pairs that can be registered at runtime.

When youâre in a debug session, the debugger automatically registers all CPU registers (`rax`, `rbx`, `rsp`, `rbp`, `rip`, etc.) and module bases (`kernel32`, `ntdll`, `libc`, etc.) into the expression parser. This enables some useful workflows:

* Type `rbp - 0x20` to navigate directly to a stack variable â no manual calculation needed
* Type `kernel32 + 0x1000` to navigate into a loaded module, even with ASLR
* Type `rsp` to jump straight to the stack pointer

![Navigate dialog with register expression](/blog/images/conditional-breakpoint/1.png)

*A quick note: historically, register names required a `$` prefix (e.g., `$rax`). Register names can now be used directly, as in `rax`.*

Plugin authors can take advantage of this system too. The [add\_expression\_parser\_magic\_value](https://api.binary.ninja/binaryninja.binaryview-module.html#binaryninja.binaryview.BinaryView.add_expression_parser_magic_value) API lets you register custom values. Imagine registering heap chunk addresses or TLS slots that users can then reference directly in expressions.

## The 500-Line Feature

Conditional breakpoint support landed in December 2025, thanks to a PR from community contributor [3rdit](https://github.com/3rdit). The entire feature (condition evaluation, UI, and API) took about 500 lines of code.

How is it possible to implement such a major feature in just 500 lines? The secret is that the condition evaluation uses the expression parser we just discussed. Hereâs a simplified version of [how it works](https://github.com/Vector35/debugger/blob/2e0c5f6d031bf4a2e30c0333715fbafbfd714115/core/debuggercontroller.cpp#L2559-L2577):

```
bool DebuggerController::EvaluateBreakpointCondition(uint64_t address)
{
    const std::string condition = m_state->GetBreakpoints()->GetConditionAbsolute(address);
    if (condition.empty())
        return true;  // No condition means always stop

    // Use the expression parser to evaluate the condition
    uint64_t result = 0;
    std::string error;
    if (!BinaryView::ParseExpression(GetData(), condition, result, address, error))
        return true;  // Parse error, stop to be safe

    return result != 0;  // Non-zero means condition is true
}
```

The debugger simply calls `ParseExpression` on the condition string. If the result is non-zero, the condition is true and the debugger stops. Thatâs it. All the heavy lifting including parsing the expression, reading register values, performing arithmetic and comparisons is handled by the expression parser.

Because the condition is evaluated at the debugger core level rather than the adapter level, the same expression syntax is available across supported debugger adapters. The register and module names in an expression still depend on the target.

## But Wait â Comparison Operators?

You might be wondering: how does the expression parser handle conditions like `rax == 0x1234`? After all, it was originally a navigation feature. What does a comparison even mean in that context?

Back in December 2022, while I was adding the magic value support for register values, I also added comparison operators to the expression parser: `==`, `!=`, `>`, `<`, `>=`, `<=`. These operators return `1` if the condition is true, `0` otherwise.

I was already thinking ahead for conditional breakpoints. The expression parser already knew how to read register values and dereference memory locations making it a perfect match for evaluating breakpoint conditions. Adding comparison operators made it ready to use.

Then in December 2025, [3rdit](https://github.com/3rdit) reached out asking about adding conditional breakpoint support. I was excited â the foundation Iâd laid three years earlier was finally going to be used. I told him that the expression parser was already there to support it so it shouldnât be hard. He came back with [PR #941](https://github.com/Vector35/debugger/pull/941), which was merged with little modification.

Thanks to 3rdit for the contribution!

## How to Use Conditional Breakpoints

Hereâs how to add a condition to a breakpoint.

### Setting a Condition

1. Add a breakpoint at the desired location
2. Right-click the breakpoint in the Breakpoints widget
3. Select âEdit Conditionâ¦â
4. Enter your condition expression
5. Click OK

![Edit condition dialog](/blog/images/conditional-breakpoint/2.png)

You can also view and edit conditions in the âConditionâ column of the Breakpoints widget.

![Breakpoint condition ...