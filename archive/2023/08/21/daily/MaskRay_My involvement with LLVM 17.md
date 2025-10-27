---
title: My involvement with LLVM 17
url: https://maskray.me/blog/2023-08-20-my-involvement-with-llvm-17
source: MaskRay
date: 2023-08-21
fetch_date: 2025-10-04T11:59:02.399081
---

# My involvement with LLVM 17

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2023-08-20](/blog/2023-08-20-my-involvement-with-llvm-17)

# My involvement with LLVM 17

LLVM 17 will soon be relased. This post provides a summary of my
contributions in this release cycle to record my learning progress.

* Ported [`-fsanitize=function`](/blog/2022-12-18-control-flow-integrity#fsanitizefunction)
  to non-x86 architectures and the C language.
* lld maintenance. See [lld 17 ELF changes](/blog/2023-07-30-lld-17-elf-changes)
* LLVM binary utility maintenance, e.g.
  + [adopted llvm-readobj
    style ObjectFile specific dumpers](https://reviews.llvm.org/D155045)
  + [`[llvm-objdump][X86] Add @plt symbols for .plt.got`](https://reviews.llvm.org/D149817)
  + [`[llvm-readobj] Print <null> for relocation target with an empty name`](https://reviews.llvm.org/D155353)
* compiler-rt maintenance, e.g.
  + changed lsan to work with high-entropy ASLR for x86-64 Linux
  + [removed crypt and crypt\_r
    interceptors](https://reviews.llvm.org/D149403) to work with glibc
  + [implemented
    interceptors](https://reviews.llvm.org/D158943) for glibc 2.38 `__isoc23_strtol` and
    `__isoc23_scanf` family functions
* Fixed ~20 places where the iteration order of `MapVector`
  or `SetVector` was relied on. [Proposed](https://discourse.llvm.org/t/reverse-iteration-bots/72224)
  more `LLVM_ENABLE_REVERSE_ITERATION=on` coverage
* Fixed longstanding brittle assembler support for RISC-V linker
  relaxation
* adapted a simplified 64-bit xxh3 from [Cyan4973/xxHash](https://github.com/Cyan4973/xxHash)
  + as efficient as the reference implementation for lld's purpose
  + migrated various xxhash64 uses in the repository
* XRay maintenance, e.g.
  + Implemented
    `__xray_customevent`/`__xray_typedevent` for
    AArch64
  + Changed codegen to work with Mach-O. Though the runtime part
    requires some CMake (which I lack) expertise to move more progress
  + Fixed semantics of some obscure driver options
* gcov maintenance
* Helped improving featuress like
  `-fexperimental-sanitize-metadata=`,
  `-fpseudo-probe-for-profiling`, and [`-fsanitize=kcfi`](https://reviews.llvm.org/D154125)

## MC

* Removed many obsoleted workarounds from the integrated
  assembler
* Fixed placement of function entry comments
* Re-architectured a substantial part of the integrated assembler that
  is used by RISC-V linker relaxation, fixing some longstanding bugs. See
  [The
  dark side of RISC-V linker relaxation](/blog/2021-03-14-the-dark-side-of-riscv-linker-relaxation) for detail.

## Clang

Driver

* Made output files more meaningful when combining compilation and
  linking phases for certain options: `-gsplit-dwarf`,
  `-ftime-trace`, `--coverage`. See [Compiler output files](/blog/2023-04-25-compiler-output-files)
  for detail
* made [target-specific
  option](/blog/2023-08-25-clang-wunused-command-line-argument#target-specific-options) report an error when used with a different target. Previously
  Clang [merely
  issued warnings](https://github.com/llvm/llvm-project/issues/64632) like
  `warning: argument unused during compilation: '-msse' [-Wunused-command-line-argument]`
* `-fdebug-prefix-map=`: made the last win when multiple
  prefixes match
* [added
  `-mllvm=`](https://reviews.llvm.org/D143325) as an alias for `-mllvm`
* Downgraded `riscv*-` triples to
  `-fdebug-default-version=4` due to [linker-relaxation
  complexity](https://reviews.llvm.org/D157663)

Others:

* [[CodeGen] Support bitcode
  input containing multiple modules](https://reviews.llvm.org/D154923)

## Learning plan

I shall learn more about instrumentation related technologies and
code generation.

## Code review

At the present, LLVM uses a self-hosted Phabricator for code review.
I have accepted or rejected 381 Phabricator Differentials revisions
(patches) during the 181 days. (I will mention how I get this number
later.) I hope that the number is fabulous, considering so many other
tasks I have to do at work for bread and butter. Here is an incomplete
list:

* [unified LTO](https://reviews.llvm.org/D123804)
  (`clang -funified-lto`)
* [fat LTO](https://reviews.llvm.org/D146777)
  (`clang -ffat-lto-objects`) (pulled out from the 17.x release
  to avoid an incomplete state)
* [many lld
  features](/blog/2023-07-30-lld-17-elf-changes)
* revamp of sanitizer interceptors
* [`-gsplit-dwarf` for
  Windows](https://reviews.llvm.org/D152785)
* [RISC-V
  `-fsanitize=kcfi`](https://reviews.llvm.org/D148385).
* RISC-V patches related to assembler, linker, and psABI
* [`llvm-objdump -d` for
  BPF](https://reviews.llvm.org/D149058)
* LLVMSupport patches
* Mips and LoongArch patches

## Future of LLVM code review process

In June 2023, a [full
disk issue](https://discourse.llvm.org/t/phabricator-unhandled-exception-aphrontqueryexception/71570) occurred with the server, which led to the rejection of
new patch uploads. To address this problem, I expanded the database disk
size from 500GB to 600GB, helping to mitigate the issue.

Phabricator is [winding
down](https://admin.phacility.com/phame/post/view/11/phacility_is_winding_down_operations/). Maintaining a website with over 600K lines of PHP code is not
sustainable. As a result, our community is in need of a suitable
replacement and GitHub's pull request system have been selected as the
replacement. I belong to the group that shares concerns regarding the
quality of GitHub's pull request system, as it utilizes a model that
some consider flawed.

GitHub's pull request system tightly couples a pull request with a
branch and has a poor commit tracking ability. In short, the system [shoehorns
into less flexible and less desired workflows](https://gregoryszorc.com/blog/2020/01/07/problems-with-pull-requests-and-how-to-fix-them/).

> If commits are reordered or added or removed in the middle of an
> existing series, the tool can get confused quite easily.
>
> [...]
>
> I have to think will my rewriting history here make re-review harder?
> [...] This is a textbook example of tooling deficiencies dictating a
> sub-optimal workflow and outcome: because pull requests don't track
> commits explicitly, I'm forced to adopt a non-ideal workflow or
> sacrifice something like commit quality in order to minimize risks that
> the review tool won't get confused.

That said, ultimately, the individuals investing their efforts will
have a significant say in determining the replacement. We that are
concerned of GitHub pull will aceept the result, but I hope that the
level of harm caused by the less-capable system is deemed acceptable. My
primary worries include:

* Efficient subscription: how do contributors effectively [subscribe to
  patches](https://github.com/llvm/llvm-project/issues/56638) they are interested in?
* Review time: will we witness an increase in less prepared patches?
  Will they consume more time from established reviewers? Or will they be
  rubber stamped more frequently?
* Will we have dirty commit messages such as "Fix typo", "Add test",
  "Resolve XXX's comments"? We can force "Squash and merge" (forbid
  "Create a merge commit" and "Rebase and merge"), but it is difficult to
  ensure clean commit messages, if contributors have to think of
  implications of rewriting history.

### Appendix

I did a SQL query to find the numbers of accepted/rejected patches by
Phabricator username between the two tags [`llvmorg-17-init`](https://github.com/llvm/llvm-project/tree/llvmorg-17-init)
and [`llvmorg-18-init`](https://github.com/llvm/llvm-project/tree/llvmorg-18-init)
(181 days), which roughly corresponds to the LLVM 17.x release
cycle.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` select u.username, count(distinct r.lastActionDIffPHID) from differential_reviewer r join phabricator_user.user u where r....