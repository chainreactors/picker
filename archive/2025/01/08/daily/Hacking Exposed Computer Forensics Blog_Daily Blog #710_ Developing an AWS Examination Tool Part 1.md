---
title: Daily Blog #710: Developing an AWS Examination Tool Part 1
url: https://www.hecfblog.com/2025/01/daily-blog-710-developing-aws.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-08
fetch_date: 2025-10-06T20:26:42.555580
---

# Daily Blog #710: Developing an AWS Examination Tool Part 1

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

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog)

Daily Blog #710: Developing an AWS Examination Tool Part 1

# Daily Blog #710: Developing an AWS Examination Tool Part 1

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 06, 2025
•

[ai programming](https://www.hecfblog.com/search/label/ai%20programming?&max-results=8)
[aws](https://www.hecfblog.com/search/label/aws?&max-results=8)
[cursor](https://www.hecfblog.com/search/label/cursor?&max-results=8)
[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdE90_F5zWqZao4l3u2Pg77cYzhGI6V5pXiPw_ZE2aGjPh-ma9eqDiJ6p4gFWLBLHdlWi78ABOJJ2NHI9xO2NSgpPDGIOc2qgyf4lk3S5TOOuN9JgEyb5IvqoS93bv2KneBxBYyRquxqh6s89R3hXeNKLY9wWuDjDAVcRrpANGoIJGT7j1dXtD-KRFNHs/w640-h640/awsenum.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdE90_F5zWqZao4l3u2Pg77cYzhGI6V5pXiPw_ZE2aGjPh-ma9eqDiJ6p4gFWLBLHdlWi78ABOJJ2NHI9xO2NSgpPDGIOc2qgyf4lk3S5TOOuN9JgEyb5IvqoS93bv2KneBxBYyRquxqh6s89R3hXeNKLY9wWuDjDAVcRrpANGoIJGT7j1dXtD-KRFNHs/s1024/awsenum.webp)

Hello Reader,

I've been really enjoying creating forensic tools with cursor (an AI extended version of Visual Studio Code). While I'm not ready to show my main pet project, an open source clone of FTK Imager, I thought it would be fun to start a series of making a smaller tool with a much more well known API. I've found that the more well known the API is and the more example code the model has ingested the better the results are. That's not to say that less known APIs won't work well, I have it working with dfvfs, but more that it does take more work to get it to find the right examples to work with.

For this example I've installed cursor and given it a small series of prompts:

"We are going to create a tool to assist forensic examiners and incident responders with investigating AWS accounts. You will create a tool that when provided with AWS credentials will enumerated all of the regions and the resources within them. The code should be written in python"

This created the first part of the script.

The next prompt

"Add on a QT GUI written in Pyside6, the top left pane should be a list of regions and when one is selected it displays the resources within it in the top right pane. The bottom pane should be a log of actions taken. There should be a region labeled ALL that allows all regions to be selected and displayed at once."

And now I have a working tool that is enumerating some AWS resources:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmXrw3ksSiL9vLLov3IimbcAgcOz5uAeYQAR8qwBMOUOcWTo0N6g6D1CXfL6aw0IDk5U9E_N5Yk55nmynPdReRgKU0G3q7fxrMsV3krIJrPGhA7aROL6sfOgrHZCAx4_cnDqWgj7cm75nhGr2_3x8b7f7Tra0P85BkyJYdVIJeCVx035ZjWL5dq7_g2Yw/w640-h396/awsenum1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmXrw3ksSiL9vLLov3IimbcAgcOz5uAeYQAR8qwBMOUOcWTo0N6g6D1CXfL6aw0IDk5U9E_N5Yk55nmynPdReRgKU0G3q7fxrMsV3krIJrPGhA7aROL6sfOgrHZCAx4_cnDqWgj7cm75nhGr2_3x8b7f7Tra0P85BkyJYdVIJeCVx035ZjWL5dq7_g2Yw/s992/awsenum1.jpg)

You can view the code here: <https://github.com/dlcowen/AWSEnumerator>

In the next series of posts I'm going to extend the functionality:

1. Selecting what credentials to use, this is defaulting to my default AWS profile for FOR509

2. Include more AWS services

3. Add in support for global views

4. Exporting out the inventory

5. Extracting cloudwatch logs

6. Extracting cloudtrail logs

7. Exporting snapshots

8. Creating snapshots

9. Exporting lambda functions

10. Enumerating organizations

11. Exporting flows

**Also Read:**

[**Developing an AWS Examination Tool Part 2**](https://www.hecfblog.com/2025/01/daily-blog-711-developing-aws.html)

[**Developing an AWS Examination Tool Part 3**](https://www.hecfblog.com/2025/01/daily-blog-712-developing-aws.html)

[**Developing an AWS Examination Tool Part 4**](https://www.hecfblog.com/2025/01/daily-blog-713-developing-aws.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/01/daily-blog-711-developing-aws.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/01/daily-blog-709-sunday-funday-1525-entra.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/7628787860889612329/comments/default)

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

Powe...