---
title: Daily Blog #739: USN Versions (2, 3 and 4)
url: https://www.hecfblog.com/2025/02/daily-blog-739-usn-versions-2-3-and-4.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-02-06
fetch_date: 2025-10-06T20:39:46.342761
---

# Daily Blog #739: USN Versions (2, 3 and 4)

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

[usnjrnl](https://www.hecfblog.com/search/label/usnjrnl)

Daily Blog #739: USN Versions (2, 3 and 4)

# Daily Blog #739: USN Versions (2, 3 and 4)

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
February 04, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[usnjrnl](https://www.hecfblog.com/search/label/usnjrnl?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicaEuD1O_A0aqOUdc8Z-Zn7cufTBGbD5_pI-x6YOLiF0-silNNKDm2_v0YFfJNFwAmfwKutkF3Bf8S7cOXuFToW-BxEX9fnWuM08JYlUWilgsskMq-wZWVXYIL6No_ZMR38cZoUkEgY5mBBmnVrF1RCDIm5J25fXd6bnhSZnE8qDUCp_-NxS91v2NlopU/w640-h640/usn.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicaEuD1O_A0aqOUdc8Z-Zn7cufTBGbD5_pI-x6YOLiF0-silNNKDm2_v0YFfJNFwAmfwKutkF3Bf8S7cOXuFToW-BxEX9fnWuM08JYlUWilgsskMq-wZWVXYIL6No_ZMR38cZoUkEgY5mBBmnVrF1RCDIm5J25fXd6bnhSZnE8qDUCp_-NxS91v2NlopU/s1024/usn.webp)

Hello Reader,

Since I first looked at the USN Journal many years ago and Matthew and I released ANJP to parse it along with other data I've known there where multiple USN versions. I thought this post would be a good place to document what the differences are and when to expect to see them.

### **USN Journal v2 – The Vista Era**

* **Introduced:**
  With the arrival of Windows Vista, the USN Journal came into existence.
* **What It Contains:**
  At its core, v2 records fundamental details for every change on an NTFS volume: the unique file reference number, parent file reference, a monotonically increasing USN, timestamp, and a set of reason flags indicating *why* the change occurred.
* **Default Status:**
  On any NTFS volume running Windows Vista or later, v2 is created not at format but after a certain number of changes occur if windows search indexing is turned on. .
* **Documentation**: <https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_record_v2>

### **USN Journal v3 – Refinements in Windows 8**

* **Introduced:**
  Windows 8 ushered in USN Journal v3.
* **What’s New:**
  Building on v2’s foundation, v3 expanded the record structure to capture additional metadata. While the basic fields remain, v3 started to include more nuanced details about certain operations—particularly those around renames and changes to alternate data streams. The idea was simple: as our file operations got more sophisticated, our change records needed to do the same.
* **Default Status:**
  For systems running Windows 8 and later, v3 became the default journal version on NTFS volumes. Again the journal is a subsystem that was meant to assist with drive indexing, backup programs and other utilities that needed to know when things changed and why. If you just format a disk the USN journal will not appear until you have created data that requires tracking.
* **Documentation**: <https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_record_v3>

### **USN Journal v4 – The Windows 10 Evolution**

* **Introduced:**
  With Windows 10 (in a series of updates that refined NTFS’s internal structures), Microsoft rolled out USN Journal v4.
* **What’s New:**
  v4 is less about a radical overhaul and more about fine-tuning. It includes extra fields to provide even more granular information about changes—covering aspects such as improved record consistency, additional flags for security-related modifications, and adjustments for better alignment with newer NTFS features. In short, v4 offers a more complete picture of file system activity while ensuring that the data is as robust and future-proof as possible.
* **Default Status:**
  According to the MSDN documentation V4 records are only read if you Range Tracking is turned on within tghe journal.  .Otherwise my Windows 10 and 11 systems return V3 records.
* **Documentation** : <https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_record_v4>

Also Read:[Arsenal Recon LevelDB Recon](https://www.hecfblog.com/2025/02/daily-blog-738-arsenal-recon-leveldb.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/02/daily-blog-740-usn-v4-data-ranges.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/02/daily-blog-738-arsenal-recon-leveldb.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/7299111377866381354/comments/default)

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

  [Daily Blog #811: Testing AWS Log latency - Modifying User Permissions](https://www.hecfblog.com/2025/04/daily-blog-811...