---
title: Daily Blog #745: Solving the windows hello challenge part 1
url: https://www.hecfblog.com/2025/02/daily-blog-745-solving-windows-hello.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-02-12
fetch_date: 2025-10-06T20:37:53.374207
---

# Daily Blog #745: Solving the windows hello challenge part 1

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

Daily Blog #745: Solving the windows hello challenge part 1

# Daily Blog #745: Solving the windows hello challenge part 1

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
February 10, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[windows hello](https://www.hecfblog.com/search/label/windows%20hello?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhTOL4wHTw-CKa17lmJveTZNXTQ1q7oNz4QNrcqYvsyF3-n0Q7woo-pihRpweLM7NHx6xgxm3YKJReHR_8z49HmHhWRAzF5G0HrrAoVLhkDgcPGFM_FUePC43WCLI7MgplO47VcbtAC7ssOXSIdpMj07c5J0Q8vbTBxUfFZ2Di_QhKNZ-G-XtTNAS0TOQ/w640-h366/hello.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhTOL4wHTw-CKa17lmJveTZNXTQ1q7oNz4QNrcqYvsyF3-n0Q7woo-pihRpweLM7NHx6xgxm3YKJReHR_8z49HmHhWRAzF5G0HrrAoVLhkDgcPGFM_FUePC43WCLI7MgplO47VcbtAC7ssOXSIdpMj07c5J0Q8vbTBxUfFZ2Di_QhKNZ-G-XtTNAS0TOQ/s1792/hello.webp)

Hello Readers,

Last week’s Sunday Funday challenge had me asking you all to test Windows Hello and discover what traces it leaves behind after authentication. Since the community couldn’t pinpoint the answer, I decided to dive in and do the testing myself.

**Part 1: Facial Recognition**

I started by focusing on the aspect that interests me most—facial recognition. Why facial recognition because it would indicate whose face was being presented and in theory who is actually at the keyboard. I purchased a Windows Hello-capable webcam that uses a facial scan for authentication. After installing it, I rebooted my computer, logged in using the facial scan, and then locked and unlocked the computer with Windows Hello.

**Digging Into the Event Logs**

First, I checked the Security Event Log. As expected, I found several Event ID 4624 entries. However, these only showed “Type 11 (cached credentials)”—there was no mention of Windows Hello or the facial scan being used for authentication.

After some research, I discovered a custom Microsoft log called **Microsoft-Windows-Biometrics/Operational**. There, I found **Event ID 1605**, which read:

> "The Windows Biometric Service secure component successfully authorized user (domain)<user>"

This confirmed that biometric authentication had taken place, but it didn’t specify which method was used. Looking two events earlier, I found **Event ID 1019**, which provided the missing details:

> "The Windows Biometric Service completed a privileged vendor-specific operation for sensor: Facial Recognition (Windows Hello) Software Device (ROOT\WINDOWSHELLOFACESOFTWAREDRIVER\0000).
> The command was directed to the biometric unit's 'Sensor Adapter' component."

This closed the loop for me. I now know exactly which biometric device was used, which user was authenticated, and that the login was successful—all thanks to facial recognition.

Stay tuned for the next part, where I’ll explore PIN-based logins and what they leave behind!

Also Read:

[Windows hello challenge part 4](https://www.hecfblog.com/2025/02/daily-blog-753-windows-hello-challenge.html)

[Windows hello challenge part 3](https://www.hecfblog.com/2025/02/daily-blog-752-windows-hello-challenge.html)

[Windows hello challenge part 2](https://www.hecfblog.com/2025/02/daily-blog-746-solving-windows-hello.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/02/daily-blog-746-solving-windows-hello.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/02/daily-blog-744-sunday-funday-2925.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/5125317130153866104/comments/default)

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

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R...