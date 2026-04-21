---
title: Mark Wielaard: Anticipating Valgrind 3.27.0
url: https://gnu.wildebeest.org/blog/mjw/2026/04/20/anticipating-valgrind-3-27-0/
source: Planet Classpath
date: 2026-04-20
fetch_date: 2026-04-21T04:43:26.297040
---

# Mark Wielaard: Anticipating Valgrind 3.27.0

# [Mark J. Wielaard](https://gnu.wildebeest.org/blog/mjw/)

* [Home](https://gnu.wildebeest.org/blog/mjw)
* [About](https://gnu.wildebeest.org/blog/mjw/about/)
* [Subscribe to Feed](https://gnu.wildebeest.org/blog/mjw/feed/ "Mark J. Wielaard RSS Feed")

---

## Anticipating Valgrind 3.27.0

Posted on April 20, 2026, 18:10.

We’ll release [Valgrind](https://valgrind.org) 3.27.0 later today. While making sure the NEWS file was up to date [I wrote about all the contributions](https://mastodon.nl/%40mjw/tagged/valgrind) made this release.

Thanks all, and apologies if I missed something or someone.

Aaron Merey added two new options to helgrind.

To control helgrind tracing of internal synchronization, threading and memory events use –show-events=1|2|3.

Use –track-destroy=no|yes|all to checks for missing pthread\_mutex\_destroy and pthread\_rwlock\_destroy calls. With yes, helgrind warns when pthread\_mutex\_init or pthread\_rwlock\_init is called on the address of a live (undestroyed) lock. With all, Helgrind also reports undestroyed locks at process exit.

Valgrind has separate VEX IR translators for AMD64 and x86 (32 bit) code. While the AMD64 translator has seen support for new encodings and instruction sets, the x86 translator has not.

Alexandra Hájková decided to port the SSE4.1 instruction set from the AMD64 translator to the x86 translator and add backend support. This is ongoing work, see the [bug dependency tree](https://bugs.kde.org/showdependencytree.cgi?id=518222).

But many more 32bit programs using SSE4.1 should now run under Valgrind.

Andreas Arnez and Florian Krohm did a lot of work on the s390x support.

Andreas added support for new s390x z/Architecture features from the 15th edition. This enables running binaries compiled with -march=arch15 or -march=z17 and exploiting the new MSA extensions 10-13.

Florian Krohm integrated binutils objdump for s390x disassembly in VEX. And did a lot of s390x code and facilities cleanups.
s390x machine models older than z196 are no longer supported.

Andreas also showed there are still meaningful optimizations to be made on how memcheck tracks undefinedness bits as outlined in the original “[Using Valgrind to detect undefined value errors with bit-precision](https://valgrind.org/docs/memcheck2005.pdf)” paper.

His optimization of memcheck instrumenting a bitwise AND/OR with a constant is [clever and simplifies the generated code](https://sourceware.org/cgit/valgrind/commit/?id=8514763a215f863bc52400991eba332df115eaea).

Martin Cermak maintains the Linux Test Program (LTP) valgrind integration, which checks our syscall wrappers work correctly. And he makes sure newer linux syscalls are wrapped. Valgrind 3.27.0 adds support for file\_getattr, file\_setattr, lsm\_get\_self\_attr, lsm\_set\_self\_attr, lsm\_list\_modules. And corrects various syscall and ioctl corner cases.

Martin also added Valgrind address space manager support for tracking linux kernel lightweight guard pages, created through madvise (MADV\_GUARD\_INSTALL).

These guard pages are very low overhead for the kernel because they aren’t tracked as separate VMAs and don’t show up in the process proc maps. But Valgrind does still need to know whether the addresses are accessible. A new –max-guard-pages option controls the memory Valgrind reserves for tracking these pages.

Paul Floyd had more commits than all others combined for this release. Paul takes care of the alternative toolchains, Solaris/illumos, FreeBSD and Darwin/MacOS ports.

Tested Oracle Solaris 11.4, OpenIndiana Hipster and OmniOS.
FreeBSD works on both amd64 and arm64, support for 16.0-CURRENT has been added.

Supported MacOS versions, 10.13 (bug fixes), 10.14, 10.15, 11.0 (Intel only), 12.0 (Intel only), 13.0 (Intel only, preliminary). No arm64 support yet.

A lot of code in valgrind 3.27.0 to support MacOS was previously maintained by Louis Brunner [out of tree](https://github.com/LouisBrunner/valgrind-macos).

There are two new [client requests](https://valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.clientreq) (macros defined in valgrind.h)

* VALGRIND\_REPLACES\_MALLOC Returns 1 if the tool replaces malloc (e.g., memcheck). Returns 0 if the tool does not replace malloc (e.g., cachegrind and callgrind) or if the executable is not running under Valgrind.
* VALGRIND\_GET\_TOOLNAME Get the running tool name as a string. Takes two arguments, an input buffer pointer and the length of that buffer.

[Comment](#respond) ([RSS](https://gnu.wildebeest.org/blog/mjw/2026/04/20/anticipating-valgrind-3-27-0/feed/))  |  [Trackback](https://gnu.wildebeest.org/blog/mjw/2026/04/20/anticipating-valgrind-3-27-0/trackback/%20)

### Leave a Reply

[Click here to cancel reply.](/blog/mjw/2026/04/20/anticipating-valgrind-3-27-0/#respond)

Name (required)

Mail (will not be published) (required)

Website

« [classpath.org domain is back!](https://gnu.wildebeest.org/blog/mjw/2025/07/24/classpath-org-domain-is-back/)

* Search for:
* ## Recent Posts

  + [Anticipating Valgrind 3.27.0](https://gnu.wildebeest.org/blog/mjw/2026/04/20/anticipating-valgrind-3-27-0/)
  + [classpath.org domain is back!](https://gnu.wildebeest.org/blog/mjw/2025/07/24/classpath-org-domain-is-back/)
  + [Supporting Software Freedom Conservancy in 2025](https://gnu.wildebeest.org/blog/mjw/2025/01/01/supporting-software-freedom-conservancy-in-2025/)
  + [Valgrind 3.23.0-RC1](https://gnu.wildebeest.org/blog/mjw/2024/04/21/valgrind-3-23-0-rc1/)
  + [Software Freedom Conservancy Fundraiser](https://gnu.wildebeest.org/blog/mjw/2024/01/11/software-freedom-conservancy-fundraiser/)
* ## Recent Comments

  + Reini Urban on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-472)
  + Jim Klimov on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-463)
  + mike on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-432)
  + kloczek on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-412)
  + [Kevin Kofler](https://www.tigen.org/kevin.kofler/) on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-391)
* ## Archives

  + [April 2026](https://gnu.wildebeest.org/blog/mjw/2026/04/)
  + [July 2025](https://gnu.wildebeest.org/blog/mjw/2025/07/)
  + [January 2025](https://gnu.wildebeest.org/blog/mjw/2025/01/)
  + [April 2024](https://gnu.wildebeest.org/blog/mjw/2024/04/)
  + [January 2024](https://gnu.wildebeest.org/blog/mjw/2024/01/)
  + [October 2023](https://gnu.wildebeest.org/blog/mjw/2023/10/)
  + [August 2023](https://gnu.wildebeest.org/blog/mjw/2023/08/)
  + [July 2023](https://gnu.wildebeest.org/blog/mjw/2023/07/)
  + [May 2023](https://gnu.wildebeest.org/blog/mjw/2023/05/)
  + [April 2023](https://gnu.wildebeest.org/blog/mjw/2023/04/)
  + [December 2022](https://gnu.wildebeest.org/blog/mjw/2022/12/)
  + [November 2022](https://gnu.wildebeest.org/blog/mjw/2022/11/)
  + [October 2022](https://gnu.wildebeest.org/blog/mjw/2022/10/)
  + [September 2022](https://gnu.wildebeest.org/blog/mjw/2022/09/)
  + [July 2022](https://gnu.wildebeest.org/blog/mjw/2022/07/)
  + [June 2022](https://gnu.wildebeest.org/blog/mjw/2022/06/)
  + [November 2021](https://gnu.wildebeest.org/blog/mjw/2021/11/)
  + [April 2021](https://gnu.wildebeest.org/blog/mjw/2021/04/)
  + [March 2021](https://gnu.wildebeest.org/blog/mjw/2021/03/)
  + [February 2020](https://gnu.wildebeest.org/blog/mjw/2020/02/)
  + [January 2020](https://gnu.wildebeest.org/blog/mjw/2020/01/)
  + [December 2019](https://gnu.wildebeest.org/blog/mjw/2019/12/)
  + [October 2019](https://gnu.wildebee...