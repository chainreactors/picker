---
title: Daily Blog #720: The new hardest question to answer in an incident
url: https://www.hecfblog.com/2025/01/daily-blog-720-new-hardest-question-to.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-19
fetch_date: 2025-10-06T20:11:21.089495
---

# Daily Blog #720: The new hardest question to answer in an incident

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

[sso](https://www.hecfblog.com/search/label/sso)

Daily Blog #721: The new hardest question to answer in an incident

# Daily Blog #721: The new hardest question to answer in an incident

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 17, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[ir](https://www.hecfblog.com/search/label/ir?&max-results=8)
[sso](https://www.hecfblog.com/search/label/sso?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVMedlqsRDxbrf407ssicE65PjEgCsMrA8xokJGTI6SN70e3J1HQ1FW5VAtfgR9HOk9nEhdDg7J_NJ1gfEfxJVNaPVLFA8oXZbPXs-RJZfqocpF3rhFFGZaje1RyjMQfJGkCarxWst8Njr3SGrHT01yDWMh_q6aBG0oIOYwkBubOnWLWOW1X_C-bs-N2M/w640-h640/ssodetective.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVMedlqsRDxbrf407ssicE65PjEgCsMrA8xokJGTI6SN70e3J1HQ1FW5VAtfgR9HOk9nEhdDg7J_NJ1gfEfxJVNaPVLFA8oXZbPXs-RJZfqocpF3rhFFGZaje1RyjMQfJGkCarxWst8Njr3SGrHT01yDWMh_q6aBG0oIOYwkBubOnWLWOW1X_C-bs-N2M/s1024/ssodetective.webp)

Hello Reader,

When an attacker compromises a single user’s credentials, the immediate concern is no longer limited to that user’s inbox or workstation. Instead, it can quickly expand to the entire ecosystem of externally hosted services and apps connected to that account. This challenge poses several unique problems:

1. **Identification of All Linked Services**

Many organizations lack a centralized, real-time inventory of the external services each login has access to. As a result, the incident response team must quickly piece together which third-party platforms are integrated with the compromised account—an often gargantuan task.

2. **Visibility Gaps**

Even when SSO or identity management systems are in place, visibility might be limited. Some SaaS vendors offer only basic logs, making it difficult to determine if the attacker accessed or manipulated data within those services. Some offer no logs at all!

3. **Third-Party Risk Management**

Security posture assessments and vendor questionnaires help, but they don’t always guarantee robust incident response capabilities from each third-party. If data was accessed or stolen, companies must coordinate with multiple external providers to understand the breach’s scope, which can slow down containment efforts. Sometimes just knowing who to contact at the individual vendor in the event of an incident can take days.

4. **Regulatory and Compliance Overlaps**

Access to third-party systems often means multiple compliance regimes could be in play (e.g., HIPAA, GDPR, PCI DSS). Failing to account for these can lead to significant fines, reputational damage, and legal complications.

So if you are trying to determine where you should focus your teams attention to be prepared for the next incident, start the long journey to building the catalog, knowledge and contacts to be able to answer this question on demand.

Also Read:[Spotlight on zeltser challenge participant - Chris Eng](https://www.hecfblog.com/2025/01/daily-blog-720-spotlight-on-zeltser.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/01/daily-blog-721-solution-saturday-11825.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/01/daily-blog-720-spotlight-on-zeltser.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/5808660286694527944/comments/default)

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

  [Daily Blog #814: Sunday Funday 4/20/25](https://www.hecfblog.com/2025/04/daily-blog-81...