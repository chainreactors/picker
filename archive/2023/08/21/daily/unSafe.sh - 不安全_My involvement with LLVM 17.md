---
title: My involvement with LLVM 17
url: https://buaq.net/go-174861.html
source: unSafe.sh - 不安全
date: 2023-08-21
fetch_date: 2025-10-04T11:58:47.401550
---

# My involvement with LLVM 17

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

My involvement with LLVM 17

LLVM 17 will soon be re
*2023-8-20 15:0:0
Author: [maskray.me(查看原文)](/jump-174861.htm)
阅读量:23
收藏*

---

LLVM 17 will soon be relased. This post provides a summary of my
contributions in this release cycle to record my learning progress.

* Ported `-fsanitize=function` to non-x86 architectures and
  the C language.
* lld maintenance. See [lld 17 ELF changes](https://maskray.me/blog/2023-07-30-lld-17-elf-changes)
* Helped features `-fexperimental-sanitize-metadata=`
* LLVM binary utility maintenance, e.g.
  + [adopted llvm-readobj
    style ObjectFile specific dumpers](https://reviews.llvm.org/D155045)
  + [`[llvm-objdump][X86] Add @plt symbols for .plt.got`](https://reviews.llvm.org/D149817)
* compiler-rt maintenance, e.g.
  + changed lsan to work with high-entropy ASLR for x86-64 Linux
  + [removed crypt and crypt\_r
    interceptors](https://reviews.llvm.org/D149403) to work with glibc
* Fixed ~20 places where the iteration order of `MapVector`
  or `SetVector` was relied on. Proposed more
  `LLVM_ENABLE_REVERSE_ITERATION=on` coverage
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

## MC

* Removed many obsoleted workarounds from the integrated
  assembler
* Fixed placement of function entry comments
* Re-architectured a substantial part of the integrated assembler that
  is used by RISC-V linker relaxation. Fixed some longstanding bugs. See
  [The
  dark side of RISC-V linker relaxation](https://maskray.me/blog/2021-03-14-the-dark-side-of-riscv-linker-relaxation) for detail.

## clangDriver

* Made output files more meaningful when combining compilation and
  linking phases for certain options: `-gsplit-dwarf`,
  `-ftime-trace`, `--coverage`. See [Compiler output files](https://maskray.me/blog/2023-04-25-compiler-output-files)
  for detail
* made target-specific option report an error when used with a
  different target. Previously Clang merely issued warnings like
  `warning: argument unused during compilation: '-msse' [-Wunused-command-line-argument]`
* `-fdebug-prefix-map=`: made the last win when multiple
  prefixes match
* [added
  `-mllvm=`](https://reviews.llvm.org/D143325) as an alias for `-mllvm`

## Code review

At the present, LLVM uses a self-hosted Phabricator for code review.
I did a SQL query to find the numbers of accepted/rejected patches by
Phabricator username between the two tags [`llvmorg-17-init`](https://github.com/llvm/llvm-project/tree/llvmorg-17-init)
and [`llvmorg-18-init`](https://github.com/llvm/llvm-project/tree/llvmorg-18-init)
(181 days), which roughly corresponds to the LLVM 17.x release
cycle.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` select u.username, count(distinct r.lastActionDIffPHID) from differential_reviewer r join phabricator_user.user u where r.reviewerStatus in ('accepted','rejected') and 1674629847<=r.dateCreated and r.dateCreated<1674634847 and r.reviewerPHID=u.phid group by r.reviewerPHID; ``` |

I have accepted or rejected 381 Phabricator Differentials
(patches).

In June 2023, a [full
disk issue](https://discourse.llvm.org/t/phabricator-unhandled-exception-aphrontqueryexception/71570) occurred with the server, which led to the rejection of
new patch uploads. To address this problem, I expanded the database disk
size from 500GB to 600GB, helping to mitigate the issue.

Phabricator is gradually winding down. Maintaining a website with
over 600K lines of PHP code is not sustainable. As a result, our
community is in need of a suitable replacement. Ultimately, the
individuals investing their efforts will have a significant say in
determining the replacement. GitHub's pull request system have been
selected as the alternative. I belong to the group that shares concerns
regarding the quality of GitHub's pull request system. My primary
worries include:

* Efficient subscription: how do contributors effectively [subscribe to
  patches](https://github.com/llvm/llvm-project/issues/56638) they are interested in?
* Review time for less prepared patches: will these patches consume
  more time from established reviewers?
* Rubber stamping: will we witness an increase in rubber stamping, or
  will many patches be approved that would have otherwise been rejected by
  experienced reviewers for valid technical reasons?

Moreover, the GitHub Pull Request system utilizes a model that some
consider flawed. It represents a patch as a difference between commits,
rather than using plus/minus hunks. Unfortunately, this flaw has caused
workflow friction, leading to concerns like the belief that "force
pushing on the patch branch" should be avoided.

[**Older**

lld 17 ELF changes](https://maskray.me/blog/2023-07-30-lld-17-elf-changes)

文章来源: https://maskray.me/blog/2023-08-20-my-involvement-with-llvm-17
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)