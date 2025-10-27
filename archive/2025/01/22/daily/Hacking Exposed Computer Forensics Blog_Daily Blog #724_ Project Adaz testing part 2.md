---
title: Daily Blog #724: Project Adaz testing part 2
url: https://www.hecfblog.com/2025/01/daily-blog-724-project-adaz-testing.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-22
fetch_date: 2025-10-06T20:24:32.162159
---

# Daily Blog #724: Project Adaz testing part 2

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

[project adaz](https://www.hecfblog.com/search/label/project%20adaz)

Daily Blog #724: Project Adaz testing part 2

# Daily Blog #724: Project Adaz testing part 2

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 20, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[project adaz](https://www.hecfblog.com/search/label/project%20adaz?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO_dHVwhi52m9GqaxgLilWS9Oc1hWI1KEjYphrwN13xgHXNV3uet6xYqojZhihEJwlammcokAzNfp36A5dQdZRkTcEtWB3GS00mAyQce1UJKdQBFHvLsRyxGVoseapRghwoeL_CTPJ6FyYRZEdrEKhUF0oAb8IjxVRsd_rbWmupsHY_vMDuBXcD10lIKA/w640-h366/adaz2.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO_dHVwhi52m9GqaxgLilWS9Oc1hWI1KEjYphrwN13xgHXNV3uet6xYqojZhihEJwlammcokAzNfp36A5dQdZRkTcEtWB3GS00mAyQce1UJKdQBFHvLsRyxGVoseapRghwoeL_CTPJ6FyYRZEdrEKhUF0oAb8IjxVRsd_rbWmupsHY_vMDuBXcD10lIKA/s1792/adaz2.webp)

Hello Reader,

When we last left off I got project adaz to run on my Windows 11 system, but once I launched terraform I got an error.

###

> ### *Error running command '/bin/bash -c 'source venv/bin/activate && ANSIBLE\_HOST\_KEY\_CHECKING=false ansible-playbook │ elasticsearch-kibana.yml -v'': exit status 1. Output: The system cannot find the path specified.*

Now this does not mean that terraform didn't create any systems, it absolutely did.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimHuODR-_iQE07aBZVuDefVqwFNhsM_GTB7mNe5Wt4kscepOk-vbBu7k2H2phVFXY-UUkiMUQjMejFIeRaq2PWZbTNJ47eGYjRgzZoWgmPYHJzSlEPvmm9t-0ITnT0hq_bSUGjTju47PwdlxA_feACjlwctNNe-zBEe7XXcbFNIca0XTnV7fOabF2jRPI/w640-h200/adazmachines.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimHuODR-_iQE07aBZVuDefVqwFNhsM_GTB7mNe5Wt4kscepOk-vbBu7k2H2phVFXY-UUkiMUQjMejFIeRaq2PWZbTNJ47eGYjRgzZoWgmPYHJzSlEPvmm9t-0ITnT0hq_bSUGjTju47PwdlxA_feACjlwctNNe-zBEe7XXcbFNIca0XTnV7fOabF2jRPI/s1136/adazmachines.jpg)

  What it does mean is that Ansible was not able to configure them, which is 1/2 of the solution. I'm running this from the windows command line (yes I could do this in linux or on a mac but the point is many of you are running on windows) so I need to modify what Ansible is calling out to so this will work.

I've been looking up solutions that are portable (make a PR back to adaz when I'm done) but so far the quick help from google and chat gpt 4o haven't seen my newly defined windows variables carry over. So I'm going to try again tomrrow with o1 and see if we can figure it out!

Also Read:

[Project Adaz testing part 1](https://www.hecfblog.com/2025/01/daily-blog-719-installing-project-adaz.html)

[Project Adaz testing part 3](https://www.hecfblog.com/2025/01/daily-blog-725-project-adaz-testing.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/01/daily-blog-725-project-adaz-testing.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/01/daily-blog-723-sunday-funday-11925.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/5160698651673866381/comments/default)

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
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72JbkCoEID0IEVH-rls7Q1LRd_0awNugK97uT7EDxugHyuXvFM/s72-c/forg...