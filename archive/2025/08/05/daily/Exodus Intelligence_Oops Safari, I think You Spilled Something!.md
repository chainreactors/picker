---
title: Oops Safari, I think You Spilled Something!
url: https://blog.exodusintel.com/2025/08/04/oops-safari-i-think-you-spilled-something/
source: Exodus Intelligence
date: 2025-08-05
fetch_date: 2025-10-07T00:17:51.520557
---

# Oops Safari, I think You Spilled Something!

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
* [Advisories](https://blog.exodusintel.com/advisories/)

[Exodus Blog](https://blog.exodusintel.com)

# Oops Safari, I think You Spilled Something!

* [August 4, 2025](https://blog.exodusintel.com/2025/08/04/)
* [Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/), [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/), [General Research](https://blog.exodusintel.com/category/general-research/)

## Overview

In February 2023, researchers at Exodus Intelligence discovered a bug in the Data Flow Graph (DFG) compiler of WebKit, the browser engine used by Safari. This bug, CVE-2024-44308, was patched by Apple in November 2024. While it was alive, its exploit was chained with PAC and APRR bypasses on Apple Silicon to yield renderer remote code execution capabilities on macOS and iOS. Such capabilities, and many others including LPEs and RCEs on Windows and Linux, are available to Exodus’ customers.

In this blog post, we examine the technical details of the DFG vulnerability and walk through exploiting it. We cover some concepts pertinent to this bug, go over both the DFG source and generated assembly to show the root cause, and demonstrate how to reliably control the stack layout and register state in order to achieve stable object corruption and ultimately gain arbitrary read/write.

## Introduction

The bug we are exploring in this post is a use-of-uninitialized-variable vulnerability found in the DFG compiler. Specifically, it exists in the code responsible for storing data to an index in a TypedArray. The next section will cover much of the important information needed to understand this bug, but we would highly recommend reading through our previous post on a Safari [integer overflow](https://blog.exodusintel.com/2023/07/20/shifting-boundaries-exploiting-an-integer-overflow-in-apple-safari/) vulnerability, which goes over many more topics, such as the JavaScriptCore (JSC) optimization pipeline.

##

## Background

Browser engines are constantly seeking to improve user experience by increasing the responsiveness of web pages, with one of the biggest bottlenecks being JavaScript execution. The solution to this problem has been to switch from always interpreting the code, which is much too slow for modern web applications, to compiling the JavaScript with various optimizations. When JavaScript code is executed repeatedly, such as in a loop, it stops being interpreted and is instead just-in-time (JIT) compiled. The JavaScript engine in WebKit, JavaScriptCore, contains several compilers, each of which takes increasingly longer to compile and produce optimized code. As JavaScript code executes increasingly more times (i.e, the code gets “hotter”) it is fed into a higher tier compiler for better optimization.

### DFG Compiler

The DFG is a mid-tier compiler that runs between the Baseline and the Faster Than Light (FTL) compilers, and is meant to generate machine code quickly with optimizations that are cheap in terms of computation time. It is the first tier in the optimization pipeline to use a separate intermediate representation (IR) instead of simply operating on bytecode. DFG IR consists of instructions or operations, which are also called nodes. DFG nodes are simultaneously nodes in a data flow graph and instructions in a control flow graph. Some examples of nodes are `PutByVal`, `GetArrayLength`, `NewFunction`, `ArithMul`.

#### Speculation

JSC relies heavily on [speculation](https://webkit.org/blog/10308/speculation-in-javascriptcore/) to be able to increase performance with optimizations meant for strongly typed languages. While the code is executing, JSC records information about the types that it has seen in order to apply optimizations specific to certain types. This makes sense since a function is likely to often see the same input type. For example, the compiler can generate very different code for the following function depending on whether it is always called with integers or strings.

```

					function add(a, b) {
    return a + b;
}

```

If whenever `add()` is called `a` and `b` are always integers, then this is extremely straightforward and can easily by compiled to just a few machine code instructions. This is much better than the generic version that the interpreter can handle in which the arguments may be integers, strings, objects, etc. This system can greatly increase the overall speed of the code being run given that the type information remains consistent.

### On-stack replacement (OSR) Exit

But now the obvious question is “what happens when the compiler’s speculation is wrong?” Along with every piece of code optimized to deal with a specific type, the compiler must include some check to ensure that the runtime type matches the one it has prepared for and, if there is a mismatch, return to a lower-tier executor which can handle the more general case for the operation. This process is often called “deoptimization” or in WebKit “OSR exit.” Every DFG node contains the corresponding bytecode to jump to a lower-tier in case of a broken assumption at runtime.

#### What Exactly is On-Stack Replacement?

On-Stack Replacement (OSR) is a method that allows code execution to transfer to a different version of the code at runtime. The execution stack is not entirely destroyed, but instead the state is altered to allow different versions of the code to continue executing on the same stack. As the compiler switches between different compilation tiers it must be careful to preserve the state of the stack and registers so that the JavaScript values being operated on do not get confused.

### Object Shapes in JavaScriptCore

The concept of an object shape, generically speaking in JavaScript terms, depends on its properties. For example, the following two objects would be considered to have the same shape:

```

					obj1 = { x: 1, y: 2 };
obj2 = { x: 2, y: 3 };

```

In JavaScriptCore object shapes are referred to as Structures. Structures help JavaScriptCore optimize code by allowing it to make assumptions about the memory layout and property access patterns of objects with the same structure.

Each structure in JavaScriptCore maintains an internal table that maps property names to their respective offsets within the memory layout of the object. When JavaScriptCore accesses a property on an object, it first checks the object’s structure to determine the property’s offset, and then it reads or writes the value at that offset in the object’s memory.

Consider the two objects `obj1` and `obj2` defined above. The structure for these objects might have the following property offsets:

```

					x: 0
y: 1

```

This means that the “x” property is located at offset 0, and the “y” property is located at offset 1. When JavaScriptCore needs to access the “x” property of `obj1`, it looks up the offset of “x” in the structure (0) and then reads the value at that offset in `obj1`‘s memory.

### Shape Guards

Shape guards play an essential role in JavaScriptCore’s optimization strategy. They allow the JIT compiler to speculate about an object’s structure, enabling it ...