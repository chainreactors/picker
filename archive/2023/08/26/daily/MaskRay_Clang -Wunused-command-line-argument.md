---
title: Clang -Wunused-command-line-argument
url: https://maskray.me/blog/2023-08-25-clang-wunused-command-line-argument
source: MaskRay
date: 2023-08-26
fetch_date: 2025-10-04T11:59:27.308889
---

# Clang -Wunused-command-line-argument

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-08-25](/blog/2023-08-25-clang-wunused-command-line-argument)

# Clang -Wunused-command-line-argument

clangDriver is the library implementing the compiler driver for
Clang. It utilitizes LLVMOption to process command line options. As
options are processed when required, as opposed to [use a large
switch](/blog/2020-10-03-llvm-command-line-processing), Clang gets the ability to detect unused options
straightforwardly.

When an option is checked with APIs such as `hasArg` and
`getLastArg`, its "claimed" bit is set.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` template<typename ...OptSpecifiers> Arg *getLastArg(OptSpecifiers ...Ids) const {   Arg *Res = nullptr;   for (Arg *A : filtered(Ids...)) {     Res = A;     Res->claim();   }   return Res; } ``` |

After all options are processed, Clang reports a
`-Wunused-command-line-argument` diagnostic for each
unclaimed option. There are multiple possible messages, but
`argument unused during compilation` is the most common one.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` % clang -c a.c -la clang: warning: -la: 'linker' input unused [-Wunused-command-line-argument] % clang -c -Werror a.c -la clang: error: -la: 'linker' input unused [-Werror,-Wunused-command-line-argument] % clang -c -Werror=unused-command-line-argument a.c -la clang: error: -la: 'linker' input unused [-Werror,-Wunused-command-line-argument] ``` |

There are many heuristics to enhance the desirability of
`-Wunused-command-line-argument`, which can be rather
subjective. For instance, options that are relevant only during
compilation do not result in `-Wunused-command-line-argument`
diagnostics when linking is performed. This is necessary to support
linking actions that utilitize `CFLAGS` or
`CXXFLAGS`.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` % clang -faddrsig -fpic -march=generic a.o ``` |

## Where options are claimed

In clangDriver, there are many job actions, e.g. preprocess,
precompile, compile, backend, assemble, link. For most actions
(preprocess/precompile/compile/backend/etc),
`clang::driver::tools::Clang` is selected.
`Clang::ConstructJob` is where most compilation only options
are handled. Target-specific options are handled by `Clang`'s
member function `RenderTargetOptions`.

For assembly files that do not need preprocessing (e.g.
`.s` (`clang::driver::types::TY_PP_Asm`)), the
driver selects `clang::driver::tools::ClangAs` to use the
integrated assembler. `ClangAs::ConstructJob` claims very few
options.

For a link job, oftentimes
`clang::driver::tools::gcc::Linker` is selected. Its
`ConstructJob` forwards `Link_Group` and
`LinkOption` options to the linker, and processes
`-Wa,` options.

## Assembly files

Assembling a `.s` file uses `ClangAs`. As
mentions, it claims very few options and we can get many
`-Wunused-command-line-argument` diagnostics.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` % gcc -S -fpic -mfpmath=sse a.c % gcc -c -fpic -mfpmath=sse a.s % clang -c -fpic -mfpmath=sse a.s clang: warning: argument unused during compilation: '-mfpmath=sse' [-Wunused-command-line-argument] ``` |

Preprocessing and assembling a `.S` file selects
`Clang`. We will get behaviors similar to compiling a
`.c` file: compilation only options do not lead to
diagnostics.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` % clang -c -fpic -mfpmath=sse a.S ``` |

## Default options

There is a tension between
`-Wunused-command-line-argument` and default options. Let's
consider a scenario where we specify
`--rtlib=compiler-rt --unwindlib=libunwind` in
`CFLAGS` and `CXXFLAGS` to utilize compiler-rt and
LLVM libunwind. ClangDriver claims `--rtlib` and
`--unwindlib` in the following code snippet:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` if (!Args.hasArg(options::OPT_nostdlib, options::OPT_r)) {   if (!Args.hasArg(options::OPT_nodefaultlibs)) {     // Handle --rtlib and --unwindlib.   }   if (!Args.hasArg(options::OPT_nostartfiles)) {     // Handle --rtlib. Append clang_rt.crtend.o or GCC style crtend{,S,T}.o   } } ``` |

However, if a build target employs `-nostdlib` or
`-nodefaultlibs`, options such as `--rtlib`,
`--unwindlib`, and many other linker options (e.g.
`-static-libstdc++` and `-pthread`) will not be
claimed, resulting in unused argument diagnostics:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` % clang --rtlib=compiler-rt --unwindlib=libunwind -stdlib=libstdc++ -static-libstdc++ -pthread -nostdlib a.o clang: warning: argument unused during compilation: '--rtlib=compiler-rt' [-Wunused-command-line-argument] clang: warning: argument unused during compilation: '--unwindlib=libunwind' [-Wunused-command-line-argument] clang: warning: argument unused during compilation: '-static-libstdc++' [-Wunused-command-line-argument] clang: warning: argument unused during compilation: '-pthread' [-Wunused-command-line-argument] ``` |

While some options like `-stdlib=` do not trigger a
diagnostic, this seems more like a happenstance rather than a deliberate
design choice.

To suppress the diagnostics, we can utilitize [`--start-no-unused-arguments`
and `--end-no-unused-arguments`](https://reviews.llvm.org/D116503) (Clang 14) like the
following:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` % clang --start-no-unused-arguments --rtlib=compiler-rt --unwindlib=libunwind -stdlib=libstdc++ -static-libstdc++ -pthread --end-no-unused-arguments -nostdlib a.o ``` |

There is also a heavy hammer `-Qunused-arguments` to
suppress `-Wunused-command-line-argument` diagnostics
regardless of options' positions:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` % clang -Qunused-arguments --rtlib=compiler-rt --unwindlib=libunwind -stdlib=libstdc++ -static-libstdc++ -pthread -nostdlib a.o ``` |

`-Qunused-arguments` is similar to
`-Wno-unused-command-line-argument`.

Conveniently, options specified in a Clang configuration file are
automatically claimed.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` cat >a.cfg <<e -stdlib=libstdc++ --rtlib=libgcc --unwindlib=libgcc e clang --config=./a.cfg a.c            # no diagnostic mkdir bin lib ln -s /usr/bin/clang bin/ cp a.cfg bin/clang.cfg ln -s /usr/lib/clang lib/ bin/clang -no-canonical-prefixes a.c  # no diagnostic ``` |

In the last command, I specify `-no-canonical-prefixes` so
that clang will find `dirname(clang)/clang.cfg`, otherwise
Clang would try to find
`dirname(realname(clang))/clang.cfg`.

## Target-specific options

GCC has [machine-dependent
options](https://gcc.gnu.org/onlinedocs/gcc/Submodel-Options.html) that usually begin with `-m`. These options are
often referred to as "machine-specific" or sometimes as
"target-specific". I am not certain whether there are any distinctions
in these terms within the context of GCC. In Clang, we prefer the term
"target-specific".

For instance, certain targets implement `-mtls-dialect=`.
This is achieved through files like
`gcc/config/aarch64/aarch64.opt`. If we use such options on
unsupported targets, we will encounter an error:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` % aarch64-linux-gnu-gcc -c -mtls-dialect=desc a.c % powerpc64le-linux-gnu-gcc -c -mtls-dialect=desc a.c powerpc64le-linux-gnu-gcc: error: unrecognized command-line option â-mtls-dialect=descâ ``` |

However, Clang employs a unified table named
`clang/include/clang/Driver/Options.td` for all options,
thereby eliminating the need for maintaining target-specific lists.
Historically, an unsupported option [merely issued a
warning](https://github.com/llvm/llvm-project/issues/64632) (unless `-Werror` is used):

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` % clang-16 -c --target=aarch64 -mavx a.c clang-16: warning: argument unused during compilation: '-mavx' [-Wunused-command-line-argument] ``` |

For Cl...