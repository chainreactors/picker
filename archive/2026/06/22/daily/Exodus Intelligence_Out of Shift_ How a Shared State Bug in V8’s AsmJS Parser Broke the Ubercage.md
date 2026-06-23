---
title: Out of Shift: How a Shared State Bug in V8’s AsmJS Parser Broke the Ubercage
url: https://blog.exodusintel.com/2026/06/22/out-of-shift-how-a-shared-state-bug-in-v8s-asmjs-parser-broke-the-ubercage/
source: Exodus Intelligence
date: 2026-06-22
fetch_date: 2026-06-23T06:06:44.789938
---

# Out of Shift: How a Shared State Bug in V8’s AsmJS Parser Broke the Ubercage

[Skip to content](#content "Skip to content")

[![Exodus Intelligence](https://blog.exodusintel.com/wp-content/uploads/2018/10/exodus-final-logo-1_small.png "Exodus Intelligence")](https://blog.exodusintel.com/ "Exodus Intelligence")

Menu

* [Blog](https://blog.exodusintel.com/)
  + [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/)
  + [News](https://blog.exodusintel.com/category/news/)
  + [Training](https://blog.exodusintel.com/category/training/)
  + [Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/)
  + [Other](https://blog.exodusintel.com/category/other/)
* [Offerings](https://exodusintel.com/index.html)
* [Company](https://exodusintel.com/about.html)
* [Capabilities](https://exodusintel.com/zeroday.html)
* [Training](https://exodusintel.com/training.html)
* [Advisories](https://blog.exodusintel.com/advisories-2/)

# EXODUS BLOG

---

## Out of Shift: How a Shared State Bug in V8’s AsmJS Parser Broke the Ubercage

JUNE 22, 2026
[Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/), [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/), [General Research](https://blog.exodusintel.com/category/general-research/)

By Chanh Pham

## Overview

In this blog post we take a look at a vulnerability patched in a [Chrome release](https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop.html) on 3rd March 2026 and assigned CVE-2026-3542. The vulnerability arose from a flaw in state management when processing an AsmJS module, which results in a corrupted WebAssembly stream when it is fed to the decoder to instantiate the WebAssembly module.

## Preliminaries

This section provides some background on AsmJS and WebAssembly.

### AsmJS

AsmJS[[1]](https://notes.austin.exodusintel.com/FvmNxFhrSYWndxIFMVRVEg?view#fn1) (or `asm.js`) is a strict subset of JavaScript designed for high performance, enabling near-native execution of code compiled from languages like C/C++.

A module is defined using the `"use asm"` directive, which enforces a statically typed model through explicit coercions (e.g., `x|0`, `+x`) and a restricted set of control flow constructs.

To ensure predictability and allow for aggressive optimization, AsmJS excludes many dynamic JavaScript features. It does not support strings, arbitrary objects, closures, dynamic property access, or garbage-collected allocations. Instead, it provides a low-level, C-like environment where values are limited to numeric types and function calls are statically determined. Memory is implemented via a contiguous `ArrayBuffer` accessed through typed arrays, emulating a linear memory model similar to native programs.

The following JavaScript snippet demonstrates the usage of AsmJS modules.

```
function AsmModule(stdlib, foreign, heap) {
  "use asm";

[1]

  var HEAP32 = new stdlib.Int32Array(heap);

[2]

  function f(a) {

[3]

    a = a | 0;

[4]

    a = a + 1;

[5]

    return a | 0;
  }

  return {f:f};
}
var heap = new ArrayBuffer(0x10000);
var m = AsmModule({Int32Array: Int32Array}, {}, heap);
```

An AsmJS module, `AsmModule`, is defined using the `"use asm"` directive. It defines a heap memory `HEAP32`, at [1], and a function `f`, at [2]. In the `f` function, at [3], explicit type coercion `a | 0` is used to declare the parameter `a` as a 32-bit integer. The `a` parameter is then used in an arithmetic expression, result of which is stored back into the parameter `a`, at [4].

Finally, the explicit type coercion `a | 0` is applied again upon the return statement at [5] to guarantee the function’s return value is a 32-bit integer.

V8’s AsmJS parser processes the JavaScript token stream and constructs the corresponding WebAssembly opcode stream, which is later written to a WebAssembly module. This WebAssembly module is processed as a regular module by the WebAssembly engine.

### The WebAssembly Modules

The WebAssembly binary format organizes modules [[2]](https://notes.austin.exodusintel.com/FvmNxFhrSYWndxIFMVRVEg?view#fn2) into a sequence of sections. Each section defines a specific module’s component.
Function definitions are split across the function section (which declares function types) and the code section (which contains function bodies).
Each section is prefixed by a one-byte identifier, followed by a `u32` value indicating the size of the section’s content, and then the actual contents of the section. The section IDs and their corresponding sections are as follows:

* 0: Custom section
* 1: Type section
* 2: Import section
* 3: Function section
* 4: Table section
* 5: Memory section
* 6: Global section
* 7: Export section
* 8: Start section
* 9: Element section
* 10: Code section
* 11: Data section
* 12: Data count section

### The WebAssembly Type Section

The WebAssembly type section, identified as section 1 in the binary encoding of modules, is responsible for defining the function signatures and other custom types used within a module.
The type section provides the list of function types which represents the type of arguments of the function (parameter types) and the types of values returned from the function (result types).

### The WebAssembly Code Section

The WebAssembly Code section, identified by ID 10, contains the actual code for each function defined in the module.
The code for each function must correspond to the function signature declared in the Type section.

The Code section consists of the following:

* The section code number: `0x0a`
* The size of the section in bytes, encoded as a LEB128 integer.
* The number of function entries in the section.
* For each function entry:
  + The size of the function code in bytes, encoded as a LEB128 integer.
  + A list of local variable declarations.
  + A sequence of opcodes representing the function body, terminated by an `end` opcode.

### WebAssembly Opcodes

WebAssembly instructions are encoded as opcodes.[[3]](https://notes.austin.exodusintel.com/FvmNxFhrSYWndxIFMVRVEg?view#fn3) Most opcodes are a single byte, while some are multi-byte sequences that represent extensions to the core instruction set.

Examples of simple opcodes include:

* `0x20`: Local get operation.
* `0x21`: Local set operation.
* `0x23`: Global get operation.
* `0x24`: Global set operation.
* `0xa0`: 64-bit float add operation
* `0xa1`: 64-bit float subtract operation.

Multi-byte opcodes often begin with a prefix byte. For instance, opcodes starting with 0xfb are part of the garbage collection (GC) extension proposal. Some of these include:

* `0xfb 0x01`: New structure operation.
* `0xfb 0x03`: Structure get operation.
* `0xfb 0x06`: Structure set operation.
* `0xfb 0x17`: Array length operation.

Other extensions introduce opcodes for features like reference-typed strings, SIMD (Single Instruction, Multiple Data), and multithreading.
It is important to note that extended opcodes are often experimental WebAssembly features and may not be supported on all platforms.
Their values can also vary between implementations or proposal versions.

Within V8, WebAssembly opcodes are referenced by enumerations. Some example opcodes include:

* `kExprI32Const`: pushing an 32-bit numeric constant onto the stack.
* `kExprI64Const`: pushing an 64-bit numeric constant onto the stack.
* `kExprI32And`: performing bitwise AND between two 32-bit numeric constant, pushing the result onto the stack.
* `kExprI64And`: performing bitwise AND between two 64-bit numeric constant, pushing the result onto the stack.
* `kExprCallFunction`: performing a function call using the function reference on top of the stack.
* `kExprLocalGet`: retrieving the value of an argument/local variable at the specified index.
* `kExprLocalGet`: setting the value at the top of the stack to the argument/local variable at the specified index.

## Vulnerability

When an expression is used to dynamically access values from the heap, the `AsmJsParser::ValidateHeapAccess()`...