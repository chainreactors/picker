---
title: Mark Wielaard: Checking usage of realloc with Valgrind
url: https://gnu.wildebeest.org/blog/mjw/2023/07/26/checking-usage-of-realloc-with-valgrind/
source: Planet Classpath
date: 2023-07-27
fetch_date: 2025-10-04T11:53:37.895713
---

# Mark Wielaard: Checking usage of realloc with Valgrind

# [Mark J. Wielaard](https://gnu.wildebeest.org/blog/mjw/)

* [Home](https://gnu.wildebeest.org/blog/mjw)
* [About](https://gnu.wildebeest.org/blog/mjw/about/)
* [Subscribe to Feed](https://gnu.wildebeest.org/blog/mjw/feed/ "Mark J. Wielaard RSS Feed")

---

## Checking usage of realloc with Valgrind

Posted on July 26, 2023, 16:22.

**Full article**: [Checking usage of realloc with Valgrind](https://developers.redhat.com/articles/2023/05/31/checking-usage-realloc-valgrind)

**Summary**: realloc has a surprising number of tricky corner cases to watch out for. Valgrind Memcheck will help you find various issues like using it with bad arguments, pointers that might have become invalid, and leaks of blocks that have been resized.

Also, don’t forget to use GCC with -fanalyzer, -Wuse-after-free, and -Wfree-nonheap-object to catch some of these issues early.

Finally, there is the almost philosophical question of what it means to have a zero-sized memory block. Since different implementations of (and standards describing) realloc answer that question differently, it is best to avoid ever calling realloc with size zero.

If you do then Valgrind 3.21.0 has two options to help:

* --show-realloc-size-zero=no|yes. Warn for size zero realloc calls.
* --realloc-zero-bytes-frees=yes|no. Whether size zero returns NULL or not.

Both options were implemented by Paul Floyd.

« [Sourceware joins the fediverse](https://gnu.wildebeest.org/blog/mjw/2023/05/30/sourceware-joins-the-fediverse/)

[Sourceware 25 Roadmap](https://gnu.wildebeest.org/blog/mjw/2023/08/07/sourceware-25-roadmap/) »

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
  + [August 2010](https://gnu.wildebeest.org/blog/mjw/2010/08/)
  + [July 2010](https://gnu.wildebeest.org/blog/mjw/2010/07/)
  + [April 2010](https://gnu.wildebeest.org/blog/mjw/2010/04/)
  + [March 2010](https://gnu.wildebeest.org/blog/mjw/2010/03/)
  + [January 2010](https://gnu.wildebeest.org/blog/mjw/2010/01/)
  + [December 2009](https://gnu.wildebeest.org/blog/mjw/2009/12/)
  + [November 2009](https://gnu.wildebeest.org/blog/mjw/2009/11/)
  + [October 2009](https://gnu.wildebeest.org/blog/mjw/2009/10/)
  + [September 2009](https://gnu.wildebeest.org/blog/mjw/2009/09/)
  + [August 2009](https://gnu.wildebeest.org/blog/mjw/2009/08/)
  + [March 2009](https://gnu.wildebeest.org/blog/mjw/2009/03/)
  + [February 2009](https://gnu.wildebeest.org/blog/mjw/2009/02/)
  + [January 2009](https://gnu.wildebeest.org/blog/mjw/2009/01/)
  + [November 2008](https://gnu.wildebeest.org/blog/mjw/2008/11/)
  + [September 2008](https://gnu.wildebeest.org/blog/mjw/2008/09/)
  + [August 2008](https://gnu.wildebeest.org/blog/mjw/2008/08/)
  + [July 2008](https://gnu.wildebeest.org/blog/mjw/2008/07/)
  + [May 2008](https://gnu.wildebeest.org/b...