---
title: Precompiled headers
url: https://maskray.me/blog/2023-07-16-precompiled-headers
source: MaskRay
date: 2023-07-17
fetch_date: 2025-10-04T11:51:58.168890
---

# Precompiled headers

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-07-16](/blog/2023-07-16-precompiled-headers)

# Precompiled headers

C/C++ projects can benefit from using precompiled headers to improve
compile time. GCC [added
support for precompiled headers](https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=17211ab55314d76370a68036f2d057b1effd687f) in 2003 ([version 3.4](https://gcc.gnu.org/gcc-3.4/changes.html)), and
the current documentation can be found at <https://gcc.gnu.org/onlinedocs/gcc/Precompiled-Headers.html>.

Even with the emergence of C++ modules, precompiled headers remain
relevant for several reasons:

* Precompiled headers share implementation aspects with modules (e.g.,
  AST serialization in Clang).
* Many C++ projects rely on the traditional compilation model and are
  not converted to C++ modules.
* Modules may possibly use some preamble-like technology to accelerate
  IDE-centric operations.
* C doesn't have C++ modules.

This article focuses on Clang precompiled headers (PCH). Let's begin
with an example.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` cat > a1.cc <<'eof' #include "b.hh" int fa1() { return fb(); } eof cat > a.cc <<'eof' #include "b.hh" int fa1(); int main() { return fa1() + fb(); } eof cat > b.hh <<'eof' #ifndef B_HH #define B_HH inline int fb() { return 42; } #endif eof  clang -c b.hh -o b.hh.pch            # cc1 action is -emit-pch clang -c -include-pch b.hh.pch a.cc  # or -include b.hh clang -c -include-pch b.hh.pch a1.cc clang++ a.o a1.o -o a ``` |

We compile `b.hh` using `-c`, just like we
would compile a non-header file. Clang parses the file, performs
semantic analysis, and writes the precompiled header (as a serialized
AST file) into `b.hh.pch`.

When compiling `a.cc`, we use `-include-pch` as
a prefix header. This means that the translation unit will get two
`b.hh` copies: one from `b.hh.pch` and one from
the textual `b.hh`. The same applies to `a1.cc`.
To avoid a `redefinition of 'fb'` error, `b.hh`
should have a header guard or use `#pragma once`.

Now, let's examine the steps in detail.

## PCH generation

Given a header file as input, Clang determines the input type as
either `c-header` (`.h`) or
`c++-header`
(`.hh`/`.hpp`/`.hxx`) based on the file
extension.

For compilation actions, either `clang` or
`clang++` can be used. If we treat `.h` as a C++
header, we need to specify `-xc++-header` (e.g.,
`clang -c -xc++-header b.h -o b.h.pch`). (It's worth noting
that the behavior of `clang++ -c a.h` is deprecated. Other
than that, the only significant difference between `clang`
and `clang++` is the linking process, specifically whether
the C++ standard library is linked.)

When the input type is `c-header` or
`c++-header`, Clang Driver selects the `-emit-pch`
frontend action. (Note:
`c++-user-header`/`c++-system-header` are used for
C++ modules and have different functionality.)

Conventionally, the extension used for Clang precompiled headers is
`.pch` (similar to MSVC). However, to match GCC, when the
`-o` option is omitted, the default output file for older
Clang versions is `input_file + ".gch"` (see
`Driver::GetNamedOutputPath`). For example, when the input
file is `d/b.hh`, the output is `d/b.hh.gch`. This
is different from `d/b.cc` that will go to
`b.o`.

The frontend parses the file, performs semantic analysis, and writes
the precompiled header (as a serialized AST file) (see
`PCHGenerator`). For the serialized format, refer to [Precompiled Header
and Modules Internals](https://clang.llvm.org/docs/PCHInternals.html).

## Using PCH

`-include-pch b.hh.pch`
(`PreprocessorOptions::ImplicitPCHInclude`) loads the
precompiled header `b.hh.pch` as a prefix header.

We can also write `-include b.hh`, and Clang will probe
`b.hh.pch`/`b.hh.gch` and use the file if present.
This is a behavior ported from GCC.

`-include` and `-include-pch` may specify a
directory. Clang will search for a suitable precompiled header in the
directory (see `ASTReader::isAcceptableASTFile`). The
directory may contain precompiled headers for different compiler
options. This is another behavior ported from GCC.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` echo 'extern int X;' > d.hh echo 'int use() { return X; }' > e.cc mkdir d.hh.pch clang++ -c -DX=x d.hh -o d.hh.pch/x.pch clang++ -c -DX=y d.hh -o d.hh.pch/y.pch clang++ -c -DX=x -include-pch d.hh.pch e.cc  # use d.hh.pch/x.pch clang++ -c -DX=x -include d.hh e.cc          # use d.hh.pch/x.pch ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` % clang++ -c -DX=z -include d.hh e.cc error: no suitable precompiled header file found in directory 'd.hh.pch' 1 error generated. % clang++ -c -include d.hh e.cc  # clang>=15.0 error: no suitable precompiled header file found in directory 'd.hh.pch' 1 error generated. ``` |

## PCH validation

When we generate and use a precompiled header with different compiler
options, the behavior will be a combination of those options.
Consequently, the behavior of `-include b.hh` may differ
depending on the presence of
`b.hh.pch`/`b.hh.gch`.

To identify this common pitfall, Clang performs PCH validation (see
`PCHValidator`) to check for inconsistent options, similar to
how MSVC handles it. The validated options include those that can affect
AST generation, such as language options (driver `-std=`,
`-fPIC`, `-fPIE`), target options (driver
`--target`), file system options, header search options, and
preprocessor options.

Modules employ the same validation mechanism, but PCH validation is
stricter (`!AllowCompatibleConfigurationMismatch`). This
means that
`COMPATIBLE_LANGOPT`/`COMPATIBLE_ENUM_LANGOPT`/`COMPATIBLE_VALUE_LANGOPT`
options (e.g., whether the built-in macro `__OPTIMIZE__` is
defined) must match as well.

If one side of the precompiled header and the user code are compiled
with the `-D` option, the other side should either use the
same `-D` option or omit it entirely.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` clang -c b.hh -o b.hh.pch -DB=1  # tolerable clang -c -include-pch b.hh.pch a.cc  # definition of macro 'B' differs between the precompiled header ('1') and the command line ('2') clang -c -include-pch b.hh.pch a.cc -DB=2  # error: macro 'B' was defined in the precompiled header but undef'd on the command line clang -c -include-pch b.hh.pch a.cc -UB ``` |

As an escape hatch, `-Xclang -fno-validate-pch` disables
PCH validation.

## Performance optimization

In order to achieve better performance, it is possible to make
certain compromises on properties such as language standard
conformance.

### `-fpch-instantiate-templates`

[`-fpch-instantiate-templates`](https://reviews.llvm.org/D69585)
allows pending template instantiations to be performed in the PCH file.
This means that these instantiations do not need to be repeated in every
translation unit that includes the PCH file. This optimization can
significantly improve the speed of certain projects. However, the option
changes the point of instantiation for certain function templates, which
is non-conforming. Nevertheless, the altered behavior is generally
harmless in most cases.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` #ifndef HEADER #define HEADER template<typename T> void f(); struct X; void g() { f<X>(); } // delayed instantiation  template<typename T> void f() { T t; }; #else struct X {}; #endif ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` % clang++ -c -xc++-header a.cc -o a.pch % clang++ -c -include-pch a.pch a.cc % clang++ -c -xc++-header a.cc -o a.pch -fpch-instantiate-templates d.cc:5:35: error: variable has incomplete type 'X'     5 | template<typename T> void f() { T t; };       |                                   ^ ... ``` |

`-fpch-instantiate-templa...