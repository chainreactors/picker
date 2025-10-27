---
title: Daily Blog #747: What I look for when reviewing external ips
url: https://www.hecfblog.com/2025/02/daily-blog-747-what-i-look-for-when.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-02-14
fetch_date: 2025-10-06T20:37:39.129096
---

# Daily Blog #747: What I look for when reviewing external ips

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

[vps](https://www.hecfblog.com/search/label/vps)

Daily Blog #747: What I look for when reviewing external ips

# Daily Blog #747: What I look for when reviewing external ips

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
February 12, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[ipinfo](https://www.hecfblog.com/search/label/ipinfo?&max-results=8)
[vps](https://www.hecfblog.com/search/label/vps?&max-results=8)
•

Comments :
1

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieipa9gw8raCON1ZWeqlctaXVlaHOZW7ZJW677W_N44gsAfbJ7zlqeXPtjgC0sHWokPwcSKjiFiHV9g5BhfUBFfVTnh5HMoxDkm6b_sVz_lXFhFUyxxKd0zIFjYLe5ZviNLEwG97DQV_Y_Vt0leR39rEw0t2garsSSXbEre4aXNVbHQToqJrMjKgpjzq8/w640-h366/vps.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieipa9gw8raCON1ZWeqlctaXVlaHOZW7ZJW677W_N44gsAfbJ7zlqeXPtjgC0sHWokPwcSKjiFiHV9g5BhfUBFfVTnh5HMoxDkm6b_sVz_lXFhFUyxxKd0zIFjYLe5ZviNLEwG97DQV_Y_Vt0leR39rEw0t2garsSSXbEre4aXNVbHQToqJrMjKgpjzq8/s1792/vps.webp)

Hello Reader,

One question I often receive from clients and new associates is: **What do you look for when reviewing external IP addresses in logs, especially VPN or SAS logs?**

In the past, analysts would typically begin their investigations by searching for suspicious connections originating from foreign countries. However, this approach is less effective today. Many companies operate globally, and even those that don’t often experience noise from automated scanners and brute-force attempts from foreign countries. While scanning for foreign countries sometimes yields results, most threat actors we track don’t actually originate from their native countries as indicated by their IP addresses.

What we’ve observed instead is that many threat actors—ranging from organized crime groups to nation-state actors—have shifted their operations to US-hosted virtual private servers (VPS). My current approach is to collect all unique IPs within a given time frame and enrich them with additional data, such as the datasets available from [ipinfo.io](https://ipinfo.io/). Their API can identify whether an IP is linked to hosting services, proxies, Tor nodes, anonymous IPs, or VPNs.

> **Documentation:** [IP Privacy Detection Database - IPinfo.io](https://ipinfo.io/)

I’ve found it’s very rare for a legitimate company employee to connect from a VPS. Therefore, when we narrow our list down to this subset, it often reliably indicates signs of compromise.

What techniques do you use? Let me know in the comments!

Also Read:[Solving the windows hello challenge part 1](https://www.hecfblog.com/2025/02/daily-blog-745-solving-windows-hello.html)

#### 1 comment :

1. ![](//resources.blogblog.com/img/blank.gif)

   James Dunn[February 12, 2025 at 11:07 PM](https://www.hecfblog.com/2025/02/daily-blog-747-what-i-look-for-when.html?showComment=1739423277650#c2101705966509024513)

   This is a great strategy, but context of the data and descriptiveness of the logs can really help take it to the next level. Incorporation of baseline activity across a time series can help you spot anomalies in things like user agent, byte size, time of day, and device information.

   Reply[Delete](https://www.blogger.com/comment/delete/1466903740262764947/2101705966509024513)

   Replies

   Reply

Add comment

Load more...

[Newer Post](https://www.hecfblog.com/2025/02/daily-blog-748-national-ccdc-2025.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/02/daily-blog-746-solving-windows-hello.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/3338902348396664941/comments/default)

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

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R76fsdeVWnJb-lPNF...