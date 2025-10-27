---
title: Function multi-versioning
url: https://buaq.net/go-148042.html
source: unSafe.sh - 不安全
date: 2023-02-06
fetch_date: 2025-10-04T05:47:06.245906
---

# Function multi-versioning

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

![]()

Function multi-versioning

UNDER CONSTRUCTIONGCC
*2023-2-5 16:0:0
Author: [maskray.me(查看原文)](/jump-148042.htm)
阅读量:24
收藏*

---

UNDER CONSTRUCTION

GCC supports some function attributes for function multi-versioning:
a way for a function to have multiple implementations, each using a
different set of ISA extensions. A function attribute specifies
different requirements of ISA extensions. The generated program decodes
the CPU model and features at run-time, and picks the most restrictive
implementation which is satisfied by the CPU, assuming that the most
restrictive implementation has the best performance.

## `__attribute__((target(...)))`

`__attribute__((target(...)))` has been available for a
long time, even before attributes for function multi-versioning were
introduced. Here are some links to relevant documentation.

* <https://gcc.gnu.org/onlinedocs/gcc/Common-Function-Attributes.html#:~:text=target%20(>
* [Attributes
  in Clang#target](https://clang.llvm.org/docs/AttributeReference.html#target)
* <https://gcc.gnu.org/onlinedocs/gcc/AArch64-Function-Attributes.html>
* <https://gcc.gnu.org/onlinedocs/gcc/x86-Function-Attributes.html>

Usually we use different function names for different implementations
and define a dispatch function. This approach is like a manual ifunc.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` extern int flags;  static __attribute__((target("default"))) int foo_default(int a) { return a & a-1; } static __attribute__((target("arch=x86-64-v2"))) int foo_v2(int a) { return a & a-1; } static __attribute__((target("arch=x86-64-v3"))) int foo_v3(int a) { return a & a-1; }  int foo(int a) {   if (flags & 2) return foo_v3(a);   if (flags & 1) return foo_v2(a);   return foo_default(a); } ``` |

The function bodies are duplicated. We can define a
`[[gnu::always_inline]]` function shared by the different
implementations.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` __attribute__((always_inline)) static inline foo_impl(int a) { return a & a-1; } static __attribute__((target("default"))) int foo_default(int a) { return foo(a); } static __attribute__((target("arch=x86-64-v2"))) int foo_v2(int a) { return foo(a); } static __attribute__((target("arch=x86-64-v3"))) int foo_v3(int a) { return foo(a); } ``` |

Let's check the behavior of an external linkage. In C++ mode, GCC and
Clang emit two symbols `_Z3foov` and
`_Z3foov.sse4.2` for the following program:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` __attribute__((target("default"))) int foo(void) { return 0; } __attribute__((target("sse4.2"))) int foo(void) { return 1; } ``` |

In C mode, GCC reports `error: redefinition of ‘foo’`.
Clang emits two symbols `foo` and
`foo.see4.2`.

TODO forward declaring

## `__attribute__((target_clones(...)))`

GCC 6 introduced `__attribute__((target_clones(...)))`. We
can just define one function with the attribute specifying all supported
targets.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ```  __attribute__((target_clones("default","arch=x86-64-v2","arch=x86-64-v3")))  int foo(int a) { return a & a-1; }  int foo_plus_1(int a) { return foo(a) + 1; } ``` |

See the GCC doc (Common Function Attributes) and [Attributes
in Clang#target\_clones](https://clang.llvm.org/docs/AttributeReference.html#target_clones). Clang only supports some basic forms, not
`arch=`.

For the above function, GCC emits three implementations
`foo.default`, `foo.arch_x86_64_v2`, and
`foo.arch_x86_64_v3`. `foo` is a dispatch function
which selects one of the implementations. This is implemented as a GNU
indirect function (ifunc). The ifunc resolver is called once by rtld at
the relocation resolving phase. The resolver references a function and a
variable defined in the runtime (libgcc).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ```         .section        .text.foo.resolver,"axG",@progbits,foo.resolver,comdat         .p2align 4         .weak   foo.resolver         .type   foo.resolver, @function foo.resolver:         subq    $8, %rsp         call    [email protected]         movq    [email protected](%rip), %rax         movl    8(%rax), %eax         testb   $2, %al         je      .L8         leaq    foo.arch_x86_64_v3(%rip), %rax .L7:         addq    $8, %rsp         ret .L8:         testb   $1, %al         leaq    foo.arch_x86_64_v2(%rip), %rdx         leaq    foo.default(%rip), %rax         cmovne  %rdx, %rax         jmp     .L7         .size   foo.resolver, .-foo.resolver         .globl  foo         .type   foo, @gnu_indirect_function         .set    foo,foo.resolver ``` |

As an ifunc, `foo` defeats interprocedural optimizations.
We can see that `foo_plus_1` does not inline
`foo`.

The attribute can apply to a non-definition declaration.
`foo.default`, `foo.arch_x86_64_v2`, and
`foo.arch_x86_64_v3` are undefined symbols while (GCC:
`foo`, Clang: `foo.ifunc`) and
`foo.resolver` remain as definitions.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ```  __attribute__((target_clones("default","arch=x86-64-v2","arch=x86-64-v3")))  int foo(int a); int main(void) { foo(0); } ``` |

In llvm-project, compiler-rt provides an alternative
implementation.

### x86

The runtime executes `cpuid`, extracts information about
the x86 family model and available CPU features, and stores them into
`__cpu_model` and `__cpu_features2`. The resolver
decodes the information and selects the best implementation.

### AArch64

The support is missing/incomplete as of GCC 12 and Clang 16.0.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` __attribute__((target_clones("sha2+memtag2", "fcma+sve2-pmull128"))) void foo() {} ``` |

(`compiler-rt/lib/builtins/cpu_model.c` defines some
symbols like `__aarch64_have_lse_atomics`. [GCC
commit](https://gcc.gnu.org/git/?p=gcc.git;h=33befddcb849235353dc263db1c7d07dc15c9faa))

## `__attribute__((cpu_dispatch(...)))` and `__attribute__((cpu_specific(...)))`

* [Attributes
  in Clang#cpu\_dispatch](https://clang.llvm.org/docs/AttributeReference.html#cpu-dispatch)

Supported by Intel C++ Compiler and later ported to Clang. GCC
doesn't support the two attributes.

The declaration and definition can be in different translation
units.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` echo '__attribute__((cpu_dispatch(ivybridge, atom, sandybridge))) void foo(void); int main(void) { foo(); }' > a.c echo '__attribute__((cpu_specific(ivybridge, atom, sandybridge))) void foo(void) {}' > b.c clang a.c b.c -o a ``` |

## `__attribute__((target_version(...)))`

Arm C Language Extensions introduced a new GNU attribute
`target_version`. Clang 17

* <https://github.com/ARM-software/acle/blob/main/main/acle.md#function-multi-versioning>
* [Attributes
  in Clang#target\_version](https://clang.llvm.org/docs/AttributeReference.html#target_version)

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` int __attribute__((target_version("default"))) tv(void) { return 0; } int __attribute__((target_version("fp16+simd"))) tv(void) { return 1; } ``` |

[**Older**

All about UndefinedBehaviorSanitizer](https://maskray.me/blog/2023-01-29-all-about-undefined-behavior-sanitizer)

文章来源: https://maskray.me/blog/2023-02-05-function-multi-versioning
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)