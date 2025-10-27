---
title: Daily Blog #746: Solving the windows hello challenge part 2
url: https://www.hecfblog.com/2025/02/daily-blog-746-solving-windows-hello.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-02-13
fetch_date: 2025-10-06T20:36:52.052842
---

# Daily Blog #746: Solving the windows hello challenge part 2

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

[windows hello](https://www.hecfblog.com/search/label/windows%20hello)

Daily Blog #746: Solving the windows hello challenge part 2

# Daily Blog #746: Solving the windows hello challenge part 2

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
February 11, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[pin](https://www.hecfblog.com/search/label/pin?&max-results=8)
[windows hello](https://www.hecfblog.com/search/label/windows%20hello?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK3kW6VY-8DuzdI5_qF5GRYPH6LdyNR4iNSJ7b59mknit1x04Sq2VGVgCr3rKFq9Rv_A5PwOxlaw2NOS3attdEvfIFOUVvKY0MKrBelapDlGbI0ZhN66hhYU18IMdAtCocCNCrkaIQ6jrKe9m6WtI95MWcCiPzl0HIZt8C3gS5NtKlMyCkXY7IstzIjFc/w640-h640/hello2.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK3kW6VY-8DuzdI5_qF5GRYPH6LdyNR4iNSJ7b59mknit1x04Sq2VGVgCr3rKFq9Rv_A5PwOxlaw2NOS3attdEvfIFOUVvKY0MKrBelapDlGbI0ZhN66hhYU18IMdAtCocCNCrkaIQ6jrKe9m6WtI95MWcCiPzl0HIZt8C3gS5NtKlMyCkXY7IstzIjFc/s1024/hello2.webp)

Hello Reader,

Continuing from yesterday’s entry—where we explored the logs for biometric face-scanning authentication in Windows Hello—today we’re taking a closer look at PIN-based authentication. With a PIN, you can sign in using a simple number sequence instead of a full password.

To test this out, I ensured my PIN was already set up, locked my workstation, and then unlocked it using the PIN. Here’s what I observed in the security logs:

* **Event ID 4624:** I found two entries related to my sign-in. One of these events is marked as type 11, which indicates:

  > **CachedInteractive:** A user logged on to this computer with network credentials that were stored locally on the computer. The domain controller wasn't contacted to verify the credentials.
* **The other was a Type 7:** Which indicated that my workstation was unlocked.

Additionally, the logon process is recorded as “Negotiat,” and the authentication package is listed as “Negotiate” as well.

Interestingly, I didn’t come across any specific logs that would clearly indicate a PIN was used. I was hoping to find entries in either the Windows Hello for Business or User Device Registration logs—similar to what we see with biometric logins—but neither those logs nor the biometric logs provided any details related to the PIN-based login.

Next on my list is testing a Windows Hello–approved fingerprint scanner. Stay tuned for more updates on that front!

Also Read:

[Windows hello challenge part 4](https://www.hecfblog.com/2025/02/daily-blog-753-windows-hello-challenge.html)

[Windows hello challenge part 3](https://www.hecfblog.com/2025/02/daily-blog-752-windows-hello-challenge.html)

[Windows hello challenge part 1](https://www.hecfblog.com/2025/02/daily-blog-745-solving-windows-hello.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/02/daily-blog-747-what-i-look-for-when.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/02/daily-blog-745-solving-windows-hello.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/5428898901377921189/comments/default)

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
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72...