---
title: Adobe Acrobat Reader Escript.api Use-After-Free Remote Code Execution
url: https://blog.exodusintel.com/2026/06/01/adobe-acrobat-reader-escript-api-use-after-free-remote-code-execution/
source: Exodus Intelligence
date: 2026-06-01
fetch_date: 2026-06-02T06:31:17.103140
---

# Adobe Acrobat Reader Escript.api Use-After-Free Remote Code Execution

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

JUNE 1, 2026
[Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/), [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/), [General Research](https://blog.exodusintel.com/category/general-research/)

# Adobe Acrobat Reader Escript.api Use-After-Free Remote Code Execution

By Michele Campa

## Overview

In this blog post we take a look at a use-after-free vulnerability found in Adobe Acrobat Reader’s Escript.api module in February 2025. This issue was patched on April 2026 and likely assigned `CVE-2026-34621`,  `CVE-2026-34626` , or `CVE-2026-34622`.

***Disclaimer**: Every offset and function name referenced in this blog post refers to Adobe Acrobat Reader 24.005.20399 32-bit version. Since Adobe Acrobat Reader is closed-source software, all function names, data structure names, and field purposes presented in this analysis are inferred through reverse engineering. They represent the author’s best-effort interpretation of the observed behavior and may not reflect the original developer’s naming or intent.*

The vulnerability occurs in the Escript.api module due to improper validation of property accessor definitions on built-in JavaScript objects (similar to prototype pollution). By leveraging the `__defineGetter__()` JavaScript API, it is possible to install a getter on a non-configurable property of a built-in object such as `Collab.toString`.

Each invocation of the getter recurses through native C++ code, where `push_event_scope_and_resolve()` registers an exception handler frame. While the JavaScript call stack does not grow, the exception chain accumulates handler frames with each recursion. This allows the recursion to exhaust the C++ stack without triggering the JavaScript engine’s recursion limit.

The module tracks scoped objects through two independent bookkeeping mechanisms: a reference counting system and an event scope stack. These must be kept in sync, but the exception handler installed by `push_event_scope_and_resolve()` fails to do so. When the C++ stack limit is reached, `push_event_scope_and_resolve()` never reaches its cleanup code that would remove the scoped object from the scope stack. Meanwhile, the reference counter is still decremented to zero through the separate `link_head` chain cleaning phase. The garbage collector then frees the object, but a scope stack entry still holds a pointer to the freed memory — a dangling pointer. Accessing the freed object through the scope stack leads to a use-after-free.

## Background

### Adobe JavaScript \_\_defineGetter\_\_ Method

Certain predefined methods exist for all Javascript objects by default, such as `toString()`, `__defineGetter__()`, `__defineSetter__()`, and so on.

The `__defineGetter__(fieldName, function)` method is used to assign a getter function to an object field, which can be an attribute or a method.

```
obj = {};
field = "name";
obj.__defineGetter__(field,
  function(){

[1]

    console.println("executed");
    return "Value";
  }
);

console.println(obj['name']);
```

The snippet above attaches a getter function to the `name` field of the object `obj`. The snippet produces the following console log.

```
executed
Value
```

When the `name` field is accessed, the function defined at [1] is executed. Notice, that the first argument of the `__defineGetter__()` function must be a string or a variable that can be represented as string.

A more interesting example is the following.

```
obj = {};
anObj = {};

[2]

anObj.toString = function() {console.log("this is the toString method of field object"); return "fieldName";}
obj.__defineGetter__(anObj, function(){console.log("executed"); return "Value";});

console.log(obj['fieldName']);
```

The console log of the above snippet is shown below.

```
this is the toString method of field object
executed
Value
```

The `toString()` method of `anObj` is overwritten, [2]. As the `__defineGetter__()` method expects the first argument to be a string, the new `toString()` method is executed. It returns `fieldName`, which is the field where the getter function is attached to. Then the getter method is executed, returning the field’s value `Value`.

### Adobe JavaScript ReadStream Object

The JavaScript `ReadStream` object is an object which can be created from JavaScript that embeds a string. The string is stored in the NT Heap.

```
var readStreamObj = util.streamFromString("Hello World", "utf-8");
readStreamObj.read(4);
```

The `util.streamFromString()` function expects two strings as parameters and throws a `TypeError` exception when the arguments are not of that type.

The `ReadStream` object is created through the `util.streamFromString()` JavaScript instruction. The string `Hello World` is stored in a new NT Heap chunk, with a size of the string length plus one for the null terminator. It is possible to read the string content from JavaScript by invoking the `read()` method of the `ReadStream` object and passing the number of bytes to read as the argument.

### Adobe Reader Escript – Scoped Objects and the Event Scope Stack

When the `Escript.api` module executes JavaScript it must manage two independent bookkeeping systems that must stay in sync: **scoped objects** and the **event scope stack**. Understanding both – and the relationship between them – is essential to understanding the vulnerability.

**Scoped objects** are runtime-managed objects allocated during JavaScript execution. Each scoped object is tracked through a reference-counted linked list rooted at a global root object. When a scoped object is created, it is optionally linked into the root’s LIFO chain with a state value that determines how it is cleaned up. The cleanup function walks the chain and, depending on the link state, decrements reference counters and frees objects.

**The event scope stack** is a LIFO stack that tracks which `Event` JavaScript object is currently bound to the global `event` property. When a function like `push_event_scope_and_resolve()`creates a new `Event`, it pushes it onto the stack. When the function completes, it pops the entry and rebinds the `event` property to the previously pushed `Event`. This is necessary because JavaScript execution in Escript is re-entrant – recursive calls can nest `Event` bindings, and each must be restored on exit.

The vulnerability arises because these two systems diverge on exception unwind: the scoped object’s reference counter is still decremented through the link chain cleanup, but the event scope stack entry is never popped, leaving a dangling pointer.

### Adobe Reader Escript – Scoped Objects List

Scoped objects are runtime-managed objects allocated during JavaScript execution. Each scoped object is tracked through a reference-counted linked list rooted at a global root object. When created, a scoped object is optionally linked into the root’s LIFO chain with a state value that determines how it is cleaned up.
The `scoped_obj_t` size is 0x48 bytes.

The function responsible for creating such objects is `scoped_obj_init()`.
...