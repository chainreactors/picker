---
title: Function multi-versioning
url: https://maskray.me/blog/2023-02-05-function-multi-versioning
source: MaskRay
date: 2023-02-06
fetch_date: 2025-10-04T05:47:20.292176
---

# Function multi-versioning

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-02-05](/blog/2023-02-05-function-multi-versioning)

# Function multi-versioning

Updated in 2023-12.

GCC supports some function attributes for function multi-versioning:
a way for a function to have multiple implementations, each using a
different set of ISA extensions. A function attribute specifies
different requirements of ISA extensions. The generated program decodes
the CPU model and features at run-time, and picks the most restrictive
implementation that is satisfied by the CPU, assuming that the most
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
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` extern int flags;  static __attribute__((target("default"))) int foo_default(int a) { return a & a-1; } static __attribute__((target("arch=x86-64-v2"))) int foo_v2(int a) { return a & a-1; } static __attribute__((target("arch=x86-64-v3"))) int foo_v3(int a) { return a & a-1; }  int foo(int a) {   if (flags & 2) return foo_v3(a);   if (flags & 1) return foo_v2(a);   return foo_default(a); } ``` |

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

In C mode, GCC reports `error: redefinition of âfooâ`.
Clang emits two symbols `foo` and
`foo.see4.2`.

With more than one declaration, the compiler merges the attributes.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` int foo(void); __attribute__((target("avx2"))) int foo(void) { return 0; }  //---  __attribute__((target("avx2"))) int foo(void); int foo(void) { return 0; } ``` |

riscv-c-api-doc [defined
the `target` attribute](https://github.com/riscv-non-isa/riscv-c-api-doc/pull/35) in 2023-11.

## `__attribute__((target_clones(...)))`

GCC [added this
attribute](3b1661a9b93fe8000faa6ab4b721a96ffb48d525) to convenient function multi-versioning. Since GCC 6, we
can just define one function with the attribute specifying all supported
targets. GCC 12 [implements](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=101696)
`arch=x86-64`, `arch=x86-64-v2`,
`arch=x86-64-v3`, and `arch=x86-64-v4` for
micro-architecture levels. Clang implemented `target_clones`
in 2021. I [added support for
x86 micro-architecture levels for Clang 18](https://reviews.llvm.org/D158329).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` // b.c __attribute__((target_clones("default","arch=x86-64-v2","arch=x86-64-v3")))  int foo(int a) { return a & a-1; }  int foo_plus_1(int a) { return foo(a) + 1; } ``` |

See the GCC doc (Common Function Attributes) and [Attributes
in Clang#target\_clones](https://clang.llvm.org/docs/AttributeReference.html#target_clones).

For the above function, GCC emits three implementations:
`foo.default`, `foo.arch_x86_64_v2`, and
`foo.arch_x86_64_v3`. `foo` is a dispatch function
that selects one of the implementations. This is implemented as a [GNU indirect function](/blog/2021-01-18-gnu-indirect-function)
(ifunc). The ifunc resolver is called once by rtld at the relocation
resolving phase. The resolver calls `__cpu_indicator_init`
and inspects features bits from `__cpu_model` and/or
`__cpu_features2`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ```         .section        .text.foo.resolver,"axG",@progbits,foo.resolver,comdat         .p2align 4         .weak   foo.resolver         .type   foo.resolver, @function foo.resolver:         subq    $8, %rsp         call    __cpu_indicator_init@PLT         movq    __cpu_features2@GOTPCREL(%rip), %rax         movl    8(%rax), %eax         testb   $2, %al         je      .L8         leaq    foo.arch_x86_64_v3(%rip), %rax .L7:         addq    $8, %rsp         ret .L8:         testb   $1, %al         leaq    foo.arch_x86_64_v2(%rip), %rdx         leaq    foo.default(%rip), %rax         cmovne  %rdx, %rax         jmp     .L7         .size   foo.resolver, .-foo.resolver         .globl  foo         .type   foo, @gnu_indirect_function         .set    foo,foo.resolver ``` |

The `target_clones` applies to non-definition
declarations. `foo.default`, `foo.arch_x86_64_v2`,
and `foo.arch_x86_64_v3` are undefined symbols while (GCC:
`foo`, Clang: `foo.ifunc`) and
`foo.resolver` remain as definitions.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` // a.c __attribute__((target_clones("default","arch=x86-64-v2","arch=x86-64-v3")))  int foo(int a); int main(void) { foo(0); } ``` |

### Drawbacks

Compilers largely don't know the semantics of ifunc and are very
conservative. Ifunc defeats most interprocedural optimizations ([feature
request](https://github.com/llvm/llvm-project/issues/71714) to enable more). We can see that the
`target_clones` function `foo` is not inlined into
`foo_plus_1`. Fortunately, functions called by a
`target_clones` function are still inlinable.

An ifunc call needs a PLT entry, regardless of whether it is
preemptive or not. On the contrary, a non-preemptive function does not
need a PLT entry.

### x86

`libgcc.a(cpuinfo.o)` defines `__cpu_model` and
`__cpu_features2`. `__cpu_indicator_init` executes
`cpuid`, extracts information about the x86 family model and
available CPU features, and stores them into `__cpu_model`
and `__cpu_features2`. The resolver decodes the information
and selects the best implementation.

In `libgcc.a` and `libclang_rt.builtins.a`,
`__cpu_model` and `__cpu_features2` have the
hidden visibility, therefore a process may have multiple copies from the
main executable and loaded shared objects.

In llvm-project, `compiler-rt/lib/builtins/cpu_model.c`
provides an alternative implementation.

### AArch64

The support is missing/incomplete as of GCC 12 and Clang 16.0. When
implemented, `+` separated features can be specified.

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
doesn't support the two attributes. They fe...