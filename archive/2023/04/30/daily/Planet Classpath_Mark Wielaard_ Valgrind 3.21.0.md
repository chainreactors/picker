---
title: Mark Wielaard: Valgrind 3.21.0
url: https://gnu.wildebeest.org/blog/mjw/2023/04/29/valgrind-3-21-0/
source: Planet Classpath
date: 2023-04-30
fetch_date: 2025-10-04T11:32:16.673332
---

# Mark Wielaard: Valgrind 3.21.0

# [Mark J. Wielaard](https://gnu.wildebeest.org/blog/mjw/)

* [Home](https://gnu.wildebeest.org/blog/mjw)
* [About](https://gnu.wildebeest.org/blog/mjw/about/)
* [Subscribe to Feed](https://gnu.wildebeest.org/blog/mjw/feed/ "Mark J. Wielaard RSS Feed")

---

## Valgrind 3.21.0

Posted on April 29, 2023, 03:09.

We are pleased to announce a new release of Valgrind, version 3.21.0, available from <https://valgrind.org/downloads/current.html>.

### Summary of new features

valgrind now provides gdb python commands. These GDB front end commands provide a better integration in the GDB command line interface, so as to use for example GDB auto-completion, command specific help, searching for a command or command help matching a regexp, … For relevant monitor commands, GDB will evaluate arguments to make the use of monitor commands easier.

The `vgdb` utility now supports extended-remote protocol when invoked with `--multi`. In this mode the GDB run command is supported. Which means you don’t need to run gdb and valgrind from different terminals.

The behaviour of realloc with a size of zero can now be changed for tools that intercept malloc with `--realloc-zero-bytes-frees=yes|no`

Make the address space limit on FreeBSD amd64 128Gbytes

When doing a memcheck delta leak\_search, it is now possible to only output the new loss records compared to the previous leak search.

Memcheck now performs checks for the use of realloc with a size of zero. `--show-realloc-size-zero=yes|no`

The helgrind option `--history-backtrace-size=` allows to configure the number of entries to record in the stack traces of “old” accesses.

Cachegrind`--cache-sim=no` is now the default.

`cg_annotate`, `cg_diff`, and `cg_merge` have been rewritten in Python. As a result, they all have more flexible command line argument handling, e.g. supporting `--show-percs` and `--no-show-percs` forms as well as the existing `--show-percs=yes` and `--show-percs=no`.

`cg_annotate` is much faster, e.g. 3-4x on common cases. It now supports diffing (with `--diff`, `--mod-filename`, and `--mod-funcname`) and merging (by passing multiple data files). It now provides more information at the file and function level.

DHAT supports a new user request which allows you to override the 1024 byte limit on access count histograms for blocks of memory.

Full release notes at <https://valgrind.org/docs/manual/dist.news.html>

« [Software Freedom Conservancy 2022 Fundraiser](https://gnu.wildebeest.org/blog/mjw/2022/12/15/software-freedom-conservancy-2022-fundraiser/)

[Sourceware joins Software Freedom Conservancy](https://gnu.wildebeest.org/blog/mjw/2023/05/16/sourceware-joins-software-freedom-conservancy/) »

* Search for:
* ## Recent Posts

  + [classpath.org domain is back!](https://gnu.wildebeest.org/blog/mjw/2025/07/24/classpath-org-domain-is-back/)
  + [Supporting Software Freedom Conservancy in 2025](https://gnu.wildebeest.org/blog/mjw/2025/01/01/supporting-software-freedom-conservancy-in-2025/)
  + [Valgrind 3.23.0-RC1](https://gnu.wildebeest.org/blog/mjw/2024/04/21/valgrind-3-23-0-rc1/)
  + [Software Freedom Conservancy Fundraiser](https://gnu.wildebeest.org/blog/mjw/2024/01/11/software-freedom-conservancy-fundraiser/)
  + [Valgrind 3.22.0](https://gnu.wildebeest.org/blog/mjw/2023/10/31/valgrind-3-22-0/)
* ## Recent Comments

  + Reini Urban on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-472)
  + Jim Klimov on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-463)
  + mike on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-432)
  + kloczek on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-412)
  + [Kevin Kofler](https://www.tigen.org/kevin.kofler/) on [dtrace for linux; Oracle does the right thing](https://gnu.wildebeest.org/blog/mjw/2018/02/14/dtrace-for-linux-oracle-does-the-right-thing/#comment-391)
* ## Archives

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
  + [October 2019](https://gnu.wildebeest.org/blog/mjw/2019/10/)
  + [August 2019](https://gnu.wildebeest.org/blog/mjw/2019/08/)
  + [July 2019](https://gnu.wildebeest.org/blog/mjw/2019/07/)
  + [June 2019](https://gnu.wildebeest.org/blog/mjw/2019/06/)
  + [May 2019](https://gnu.wildebeest.org/blog/mjw/2019/05/)
  + [April 2019](https://gnu.wildebeest.org/blog/mjw/2019/04/)
  + [March 2019](https://gnu.wildebeest.org/blog/mjw/2019/03/)
  + [February 2019](https://gnu.wildebeest.org/blog/mjw/2019/02/)
  + [April 2018](https://gnu.wildebeest.org/blog/mjw/2018/04/)
  + [February 2018](https://gnu.wildebeest.org/blog/mjw/2018/02/)
  + [October 2017](https://gnu.wildebeest.org/blog/mjw/2017/10/)
  + [July 2017](https://gnu.wildebeest.org/blog/mjw/2017/07/)
  + [June 2017](https://gnu.wildebeest.org/blog/mjw/2017/06/)
  + [October 2016](https://gnu.wildebeest.org/blog/mjw/2016/10/)
  + [May 2016](https://gnu.wildebeest.org/blog/mjw/2016/05/)
  + [February 2016](https://gnu.wildebeest.org/blog/mjw/2016/02/)
  + [January 2016](https://gnu.wildebeest.org/blog/mjw/2016/01/)
  + [November 2015](https://gnu.wildebeest.org/blog/mjw/2015/11/)
  + [February 2015](https://gnu.wildebeest.org/blog/mjw/2015/02/)
  + [May 2014](https://gnu.wildebeest.org/blog/mjw/2014/05/)
  + [August 2012](https://gnu.wildebeest.org/blog/mjw/2012/08/)
  + [June 2012](https://gnu.wildebeest.org/blog/mjw/2012/06/)
  + [May 2012](https://gnu.wildebeest.org/blog/mjw/2012/05/)
  + [April 2012](https://gnu.wildebeest.org/blog/mjw/2012/04/)
  + [March 2012](https://gnu.wildebeest.org/blog/mjw/2012/03/)
  + [January 2012](https://gnu.wildebeest.org/blog/mjw/2012/01/)
  + [December 2011](https://gnu.wildebeest.org/blog/mjw/2011/12/)
  + [November 2011](https://gnu.wildebeest.org/blog/mjw/2011/11/)
  + [September 2011](https://gnu.wildebeest.org/blog/mjw/2011/09/)
  + [June 2011](https://gnu.wildebeest.org/blog/mjw/2011/06/)
  + [April 2011](https://gnu.wildebeest.org/blog/mjw/2011/04/)
  + [February 2011](https://gnu.wildebeest.org/blog/mjw/2011/02/)
  + [January 2011](https://gnu.wildebeest.org/blog/mjw/2011/01/)
  + [December 2010](https://gnu.wildebeest.org/blog/mjw/2010/12/)
  + [November 2010](https://gnu.wildebeest.org/blog/mjw/2010/11/)
  + [October 2010](https://gnu.wildebeest.org/blog/mjw/2010/10/)
  + [September 2010](https://gnu.wildebeest.org/blog/mjw/2010/09/)
  + [August 2010](https://gnu.wildebees...