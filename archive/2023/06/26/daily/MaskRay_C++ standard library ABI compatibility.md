---
title: C++ standard library ABI compatibility
url: https://maskray.me/blog/2023-06-25-c++-standard-library-abi-compatibility
source: MaskRay
date: 2023-06-26
fetch_date: 2025-10-04T11:45:46.176793
---

# C++ standard library ABI compatibility

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-06-25](/blog/2023-06-25-c%2B%2B-standard-library-abi-compatibility)

# C++ standard library ABI compatibility

Updated in 2023-11.

For a user who only uses one C++ standard library, such as libc++,
there are typically three compatibility goals, each with increasing
compatibility requirements:

* Can the program, built with a specific version of libc++, work with
  an upgraded libc++ shared object (DSO)?
* Can an executable and its DSOs be compiled with different versions
  of libc++ headers?
* Can two relocatable object files, compiled with different versions
  of libc++ headers, be linked into the same executable or DSO?

If we replace "different libc++ versions" with a mixture of libc++
and libstdc++, we encounter additional goals:

* Can the program, built with a specific version of libstdc++, work
  with an upgraded libstdc++ DSO?
* Can an executable, built with libc++, link against DSOs that were
  built with libstdc++?
* Can two relocatable object files, compiled with libc++ and
  libstdc++, or two libstdc++ versions, be linked into the same executable
  or DSO?

Considering static linking raises another interesting question:

If libc++ is statically linked into `b.so`, can it be used
with `a.out` that links against a different version of
libc++? Let's focus on the first three questions, which specifically
pertain to libc++.

## libc++ ABI stability

libc++ is assigned a version number that corresponds to the major and
minor releases of the llvm-project. Additionally, libc++ offers a target
ABI version (`LIBCXX_ABI_VERSION`) as a build-time option,
which currently defaults to 1. `LIBCXX_ABI_VERSION` is used
to choose between the stable ABI and the unstable ABI, as explained in
the official documentation [libc++ ABI
stability](https://libcxx.llvm.org/DesignDocs/ABIVersioning.html).

If we build a program using a specific libc++ version with the stable
ABI and link it against the libc++ DSO, upgrading the libc++ DSO should
not break the program (assuming the program itself doesn't have any
bugs). However, there are rare cases where libc++ might remove symbols
that technically have the potential to cause an ABI break. These cases
usually involve symbols such as debug mode symbols or symbols that only
affect certain C++ 2003 programs, and their impact is limited.

In general, the answer to the first two questions (repeated below) is
yes:

* Can the program, built with a specific version of libc++, work with
  an upgraded libc++ shared object (DSO)? Yes.
* Can an executable and its DSOs be compiled with different versions
  of libc++ headers? Yes, the linked libc++ must be the newest one.

However, certain unusual configurations, like
`_LIBCPP_DISABLE_VISIBILITY_ANNOTATIONS`, need to be
excluded.

Now, let's consider the problem: when does an ABI break occur? An ABI
break can happen when an executable or DSO uses a symbol that undergoes
an ABI change due to a libc++ upgrade. This symbol can be defined in the
libc++ DSO itself or in another DSO that is rebuilt with a new version
of libc++.

For each symbol affected by libc++, there is an intention regarding
whether it should be exported or not. Typically, the goal is to minimize
the number of exported symbols. Let's discuss these symbols
separately.

### Intended exported symbols

The symbols that are intended to be exported include numerous
typeinfo/vtable symbols from `_LIBCPP_TEMPLATE_VIS` classes,
many `_LIBCPP_EXPORTED_FROM_ABI` symbols, a few
`_LIBCPP_CLASS_TEMPLATE_INSTANTIATION_VIS` explicit
instantiation definitions, a few
`_LIBCPP_METHOD_TEMPLATE_IMPLICIT_INSTANTIATION_VIS` and enum
symbols, as well as a few miscellaneous symbols.

libc++ needs to provide ABI compatibility for these symbols within
the stable ABI.

Most classes are marked with `_LIBCPP_TEMPLATE_VIS`, which
allows the instantiated typeinfo symbols to have default visibility even
when using `-fvisibility=hidden` or
`-fvisibility-inlines-hidden`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` % cat typeid.cc #include <string> #include <typeinfo> const char *foo() { return typeid(std::string).name(); } % clang -stdlib=libc++ -c -fvisibility=hidden typeid.cc % readelf -WsC c.o | grep basic_string      5: 0000000000000000    16 OBJECT  WEAK   DEFAULT    9 typeinfo for std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >      7: 0000000000000000    63 OBJECT  WEAK   DEFAULT    7 typeinfo name for std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > ``` |

For exported function symbols (e.g.
`std::__1::thread::~thread()` (when
`LIBCXX_ABI_VERSION=1`)), they are generally defined in
`libcxx/src/**/*.cpp` files.

### Intended non-exported symbols

When our executable or DSO has an undefined symbol that is defined by
the libc++ DSO, problems may arise if a new libc++ DSO defines the
symbol with an ABI break or no longer defines the symbol.

In the case of DSOs, symbol interposition introduces another
consideration: non-local default visibility symbols that are defined. By
default, such symbols are exported to the dynamic symbol table. When the
DSO is used with another DSO, the runtime linker (rtld) binds the
reference from the second DSO to the first DSO or executable that
defines the symbol.

To enable the safe mixing of linked images built with different
versions of libc++, libc++ utilizes the concept of "hiding symbols from
the ABI." Let's explore different categories of symbols and how to hide
them from the ABI.

In short, libc++ provides the macro macro
`_LIBCPP_HIDE_FROM_ABI` for such symbols. The macro consists
of at least
`__attribute__((__visibility__("hidden"))) __attribute__((__exclude_from_explicit_instantiation__))`.

#### Hide defined symbols

The majority of symbols impacted by libc++ are those generated during
the compilation of libc++ headers. Dealing with these symbols is
relatively straightforward. We simply make them hidden using
`__attribute__((__visibility__("hidden")))`.

#### Hide symbols due to explicit instantiation declarations

In the case of explicit instantiation declarations, the compiler
assumes that the definition exists in another translation unit and may
generate undefined symbols. This behavior corresponds to the
`available_externally` linkage in LLVM IR. The presence of
undefined symbols poses a problem because if the definition originates
from a translation unit built with a different version of libc++, there
may be a mismatch in the ABI.

To address this, starting from Clang 8, the attribute [`__attribute__((exclude_from_explicit_instantiation))`](https://reviews.llvm.org/D51789)
is defined. Applying this attribute to a symbol treats it as not being
part of an explicit instantiation declaration. Consequently, the symbol
will exhibit the regular COMDAT behavior (the `linkonce_odr`
or `weak_odr` linkage in LLVM IR), where it is either defined
or optimized out, ensuring that it never results in an undefined
symbol.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` | ``` % cat a.cc #ifndef ATTR #define ATTR #endif template <class T> struct Foo {   ATTR inline void non_static_member_function1();   ATTR void non_static_member_function2();   ATTR static int static_data_member; };  template <class T> inline void Foo<T>::non_static_member_function1() { } template <class T>        void Foo<T>::non_static_member_function2() { } template <class T>        int Foo<T>::static_data_member;  extern template struct Foo<int>;  void use() {   Foo<int> f;   f.non_static_member_function1();   f.non_static_member_function2();   int &odr_use = Foo<int>::static_data_member; } % clang++ -...