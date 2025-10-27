---
title: Daily Blog #740: USN V4 Data Ranges
url: https://www.hecfblog.com/2025/02/daily-blog-740-usn-v4-data-ranges.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-02-07
fetch_date: 2025-10-06T20:47:03.022958
---

# Daily Blog #740: USN V4 Data Ranges

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[v4](https://www.hecfblog.com/search/label/v4)

Daily Blog #740: USN V4 Data Ranges

# Daily Blog #740: USN V4 Data Ranges

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
February 05, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[usnjrnl](https://www.hecfblog.com/search/label/usnjrnl?&max-results=8)
[v4](https://www.hecfblog.com/search/label/v4?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmsf8-Nd2ikmZAdCkC46hmWv-abobFMFNysaibEboDTL93GC5al1ZjVjGZcUQF9TetjRvdcqJly8EGq_eFWdWwQOo_W47D6uJTLvmIwB_5DNmsYSAhi7CJ5gbm2M3SOYWfo9Dw8oa3-pwAanfNTt0911IKXlkDqV0RgTdY2wgs4fpERurrQNiBwdF1vVo/w640-h640/usndata.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmsf8-Nd2ikmZAdCkC46hmWv-abobFMFNysaibEboDTL93GC5al1ZjVjGZcUQF9TetjRvdcqJly8EGq_eFWdWwQOo_W47D6uJTLvmIwB_5DNmsYSAhi7CJ5gbm2M3SOYWfo9Dw8oa3-pwAanfNTt0911IKXlkDqV0RgTdY2wgs4fpERurrQNiBwdF1vVo/s1024/usndata.webp)

Hello Reader,

In the prior post we talked aboutt the differences between USN v2, v3 and v4. I thought it would be good to a bit more into v4 and why it may be creating evcen more useful data for you. v4 stores 'data ranges' which means that it tells you what sectors on the disk where involved in a change.

What does that mean for you?

1. If a file was deleted you have the data ranges it previously existed in, even if it was fragmented

2. If a file was changed you can see what blocks may have nay previous partial contents

What gets more interesting is that in the testing done it also appears that in some cases its not just the ranges of data that is being written to the USN Journal but some of the contents of those sectors as well. I'm going to be doing some testing to see if this limited to just resident files or if like EXT4 it will record the contents of all blocks changed!

Also Read: [USN Versions (2, 3 and 4)](https://www.hecfblog.com/2025/02/daily-blog-739-usn-versions-2-3-and-4.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/02/daily-blog-741-ai-powered-honeypots.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/02/daily-blog-739-usn-versions-2-3-and-4.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/2018951862040933252/comments/default)

## Top Posts/Right Now

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R76fsdeVWnJb-lPNFnJnif0HpOq-5yuADLWqHUQjQG4zpbLb46P0PM-dvHaM9rsb-D39qs/s72-c/sundayfunday.png)](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)

  [Daily Blog #814: Sunday Funday 4/20/25](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72JbkCoEID0IEVH-rls7Q1LRd_0awNugK97uT7EDxugHyuXvFM/s72-c/forgive.png)](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)

  [Daily Blog #815: I missed a day](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi60iLy5WiSNWWSyeIoM9JsOK9Xwv5L7GT5g4NxBmdQwyQNbbHzgWoiG4FbwefVVrqg1yDaz0ripRAlyXSWNX4xJ3tACOcH7a0_YyoPVT2XMPnI2-0aE3gKc9hJWhMWYqDWlTUDM2XM3DEHiJB5Z1iSrtjQeP0qG5xKxmt4RewUfbqA0FR7cw1DXPwxYNM/s72-c/solutionsaturday.png)](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)

  [Daily Blog #813: Solution Saturday 4/19/25](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhK3OAgdGTujkTy5X-nM4364yuWc8TJa-ct4GGE-Phw3vdXX9DApDT_kRhIvjELWVYLvnTPIrJTGFuz2hhkhVoklmY6bixe4fypY1X1A8RuJgAoPUUK597HYTBKVrOgLMn11x2g6b0azfhNnVv7CE6p-ZZRcfmAnaIIB-RNEBL_rIakVyr80MUyDhMQGgI/s72-c/removefromgroup.png)](https://www.hecfblog.com/2025/04/daily-blog-812-testing-aws-log-latency.html)

  [Daily Blog #812: Testing AWS Log latency - Removing Users from Groups](https://www.hecfblog.com/2025/04/daily-blog-812-testing-aws-log-latency.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitgwVMjukTzCuo_bdlGs6epwr95Xl8x8_1MJt_djP4ZVpHlyf15v6pNOYVIhyphenhyphenEO0Tplcb2BMczNRo7gwcMaWeS0T64eGqUHQuini6o_dnTYA9dLg8oWfo4tJQD8i2ba_PZh3jQG6k_fgY_n86V6LkpQq2FQx4RO44Mvptg6TjE3V7-fs21BSiYgNXb2xk/s72-c/addusertogrou%5Bp.png)](https://www.hecfblog.com/2025/04/daily-blog-811-testing-aws-log-latency.html)

  [Daily Blog #811: Testing AWS Log latency - Modifying User Permissions](https://www.hecfblog.com/2025/04/daily-blog-811-testing-aws-log-latency.html)

Powered by [Blogger](https://www.blogger.com).

## About

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)

A Blog on computer and digital forensic research, DFIR programming, the forensic lunch and more wirrten by Hacking Exposed Computer Forensic author David Cowen

## Follow us

## Popular Posts

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R76fsdeVWnJb-lPNFnJnif0HpOq-5yuADLWqHUQjQG4zpbLb46P0PM-dvHaM9rsb-D39qs/s72-c/sundayfunday.png)](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)

  [Daily Blog #814: Sunday Funday 4/20/25](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72JbkCoEID0IEVH-rls7Q1LRd_0awNugK97uT7EDxugHyuXvFM/s72-c/forgive.png)](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)

  [Daily Blog #815: I missed a day](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi60iLy5WiSNWWSyeIoM9JsOK9Xwv5L7GT5g4NxBmdQwyQNbbHzgWoiG4FbwefVVrqg1yDaz0ripRAlyXSWNX4xJ3tACOcH7a0_YyoPVT2XMPnI2-0aE3gKc9hJWhMWYqDWlTUDM2XM3DEHiJB5Z1iSrtjQeP0qG5xKxmt4RewUfbqA0FR7cw1DXPwxYNM/s72-c/solutionsaturday.png)](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)

  [Daily Blog #813: Solution Saturday 4/19/25](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhK3OAgdGTujkTy5X-nM4364yuWc8TJa-ct4GGE-Phw3vdXX9DApDT_kRhI...