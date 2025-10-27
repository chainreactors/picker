---
title: Daily Blog #709: Sunday Funday 1/5/25 Entra ID and Bloodhound
url: https://www.hecfblog.com/2025/01/daily-blog-709-sunday-funday-1525-entra.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-06
fetch_date: 2025-10-06T20:20:19.198788
---

# Daily Blog #709: Sunday Funday 1/5/25 Entra ID and Bloodhound

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

[sunday funday](https://www.hecfblog.com/search/label/sunday%20funday)

Daily Blog #709: Sunday Funday 1/5/25 Entra ID and Bloodhound

# Daily Blog #709: Sunday Funday 1/5/25 Entra ID and Bloodhound

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 05, 2025
•

[azure](https://www.hecfblog.com/search/label/azure?&max-results=8)
[azure ad](https://www.hecfblog.com/search/label/azure%20ad?&max-results=8)
[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[entraid](https://www.hecfblog.com/search/label/entraid?&max-results=8)
[sunday funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvKwflCB2hae67iDBWDkwF38Fk-QtZXj9vXnjxsz7dDBGz7Y_D3cblTHrUC900aSv-HxQy7hPsfCF29tqW4K7EN9052cOu8o2SKSgbzx5rfEtvFqGAbDtDt0_szx7wg-uZpAej4XAu4HuUeUmAfUyRooPQsvFZqtLWTxlqWLCesJ4qBKsdaxdRkNzoeA/w640-h360/aws.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvKwflCB2hae67iDBWDkwF38Fk-QtZXj9vXnjxsz7dDBGz7Y_D3cblTHrUC900aSv-HxQy7hPsfCF29tqW4K7EN9052cOu8o2SKSgbzx5rfEtvFqGAbDtDt0_szx7wg-uZpAej4XAu4HuUeUmAfUyRooPQsvFZqtLWTxlqWLCesJ4qBKsdaxdRkNzoeA/s1244/aws.png)

Hello Reader,

Welcome back to Sunday Funday! This week we are going straight in to topics I see as current research blind spots. We are going to be focusing on Entra ID aka Azure AD and what evidence you can find when people run tools like Bloodhound/Sharphound. I look forward to your thorough responses as we work as a community to overcome lack of knowledge.

**The Prize:**

$100 Amazon Giftcard
An apperance on the following week's Forensic Lunch!

**The Rules:**

1. You must post your answer before Friday 1/10/25 7PM CST (GMT -5)
2. The most complete answer wins
3. You are allowed to edit your answer after posting
4. If two answers are too similar for one to win, the one with the earlier posting time wins
5. Be specific and be thoughtful
6. Anonymous entries are allowed, please email them to dlcowen@gmail.com. Please state in your email if you would like to be anonymous or not if you win.
7. In order for an anonymous winner to receive a prize they must give their name to me, but i will not release it in a blog post

**The Challenge:**

What evidence is left behind in Azure when an attacker runs Bloodhound or any derivative like Sharphound. You should document at least two scenarios:

1. Default logging

2. Turning on any optional logging you want to test.

Your response can be a link to your own blog, an email, a document etc.. Bonus points if you point out specific indicators that can be searched for or alerted off of.

Also Read: [Zeltser Challenge Spotlight - Oleg Skulkin](https://www.hecfblog.com/2025/01/daily-blog-708-zeltser-challenge.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/01/daily-blog-710-developing-aws.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/01/daily-blog-708-zeltser-challenge.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/8344273886425520678/comments/default)

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
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72JbkCoEID0IEVH-rls7Q1LRd_0awNugK97uT7EDxugHyuXvFM/s72-c/forgive.png)...