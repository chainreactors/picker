---
title: Leave Only Footprints: When Prevention Fails
url: https://www.ericconrad.com/2023/06/leave-only-footprints-when-prevention.html
source: Eric Conrad
date: 2023-06-12
fetch_date: 2025-10-04T11:46:52.631512
---

# Leave Only Footprints: When Prevention Fails

# [Eric Conrad](https://www.ericconrad.com/)

Author, SANS Faculty Fellow, and CTO of Backshore Communications

## Sunday, June 11, 2023

### Leave Only Footprints: When Prevention Fails

Here are links and EVTX files from my SANS Blue Team Summit keynote Leave Only Footprints: When Prevention Fails.

* Here are [my slides](https://www.dropbox.com/s/195q5mrcm0e9py0/Leave%20Only%20Footprints.pdf?dl=0)
* Here are the [EVTX files](https://www.dropbox.com/s/m1qj0b66rb9jm3j/Leave%20Only%20Footprints.zip?dl=0)
* [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
* [The Rise of C2 Frameworks](https://www.thec2matrix.com/matrix)
* [Most Popular C2 Frameworks – May 2023](https://twitter.com/teamcymru_S2/status/1662103798050066432)
* [Busting the Ghost in the Logs](https://www.youtube.com/watch?v=bTU5xTIXoI4) - Randy Pargman & Jean-Francois Maes
* [Tracking Malware with Import Hashing](https://www.mandiant.com/resources/blog/tracking-malware-import-hashing)
* [Impacket](https://github.com/fortra/impacket)
* [Hydra](https://github.com/vanhauser-thc/thc-hydra)
* [Metasploit](https://www.metasploit.com/)
* [Sliver](https://github.com/BishopFox/sliver)
* [Enabling logging of failed logons on Windows](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-auditing-faq)

Here are a few Powershell commands to parse the logs (also check out [DeepBlueCLI](https://github.com/sans-blue-team/DeepBlueCLI)):

* Any command referencing **ADMIN$**:

+ **Get-WinEvent @{Path="metasploit-sysmon.evtx";id=1} | Where {$\_.Message -like "\*ADMIN$\*"} | fl**

* Any command referencing both **cmd.exe** and **wmiprvse.exe**:

+ **Get-WinEvent @{Path="**metasploit-sysmon**.evtx";id=1} | Where {$\_.Message -like "\*cmd.exe\*" –and $\_.Message -like "\*wmiprvse\*"} | fl**

* Create Remote Thread (Hashdump and process migration):

+ **Get-WinEvent @{Path="**metasploit-sysmon.**evtx";id=8} | fl**

Posted by

[Eric Conrad](https://www.blogger.com/profile/04946059331360224891 "author profile")

at
[3:38 PM](https://www.ericconrad.com/2023/06/leave-only-footprints-when-prevention.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=8710533&postID=2597952996286868986&from=pencil "Edit Post")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/8710533/2597952996286868986)

[Newer Post](https://www.ericconrad.com/2023/06/introducing-deepbluecli-v3.html "Newer Post")

[Older Post](https://www.ericconrad.com/2023/01/blind-data-exfiltration-using-dns-and.html "Older Post")
[Home](https://www.ericconrad.com/)

Subscribe to:
[Post Comments (Atom)](https://www.ericconrad.com/feeds/2597952996286868986/comments/default)

## About Me

[Eric Conrad](https://www.blogger.com/profile/04946059331360224891)
:   Peaks Island, ME, United States
:   CTO, [Backshore Communications](http://www.backshore.net)

    I am a [SANS Faculty Fellow](http://www.sans.org/security-training/instructors/Eric-Conrad), co-author of [SANS Security 511](https://www.sans.org/course/continuous-monitoring-security-operations), [MGT 414](https://www.sans.org/course/sans-plus-s-training-program-cissp-certification-exam), and [Security 542](https://www.sans.org/course/web-app-penetration-testing-ethical-hacking).

    I am [GIAC GSE](http://www.giac.org/certification/security-expert-gse) #13.

    I am a graduate of the [SANS Technology Institute](http://www.sans.edu), with a [Master of Science in Information Security Engineering (MSISE)](http://www.sans.edu/academics/curricula/msise)

    My [Amazon author page](http://www.amazon.com/Eric-Conrad/e/B003GX931K)

    Email me: blogger7@backshore.net

    Bluesky: [@ericconrad.com](https://bsky.app/profile/ericconrad.com)

[View my complete profile](https://www.blogger.com/profile/04946059331360224891)

## My videos and podcasts

* [Cyber Security Interviews - You need to be interested beyond 9-5](https://cybersecurityinterviews.com/038-eric-conrad-need-interested-beyond-9-5/)
* [DerbyCon 2017: Introducing DeepBlueCLI v2 now available in PowerShell and Python](https://www.youtube.com/watch?v=2E2p03_Et-M)
* [Paul's Security Weekly #519](https://www.youtube.com/watch?v=73a8HZ0fGHE)
* [How to become a SANS instructor](https://www.youtube.com/watch?v=jOf2Q9lRJKo)
* [DerbyCon 2016: Introducing DeepBlueCLI a PowerShell module for hunt teaming via Windows event logs](https://www.youtube.com/watch?v=hoDSv5KpEJk&t=33s)
* [Security Onion Con 2016: C2 Phone Home](https://www.youtube.com/watch?v=ViR405l-ggg)
* [Long tail analysis](https://www.youtube.com/watch?v=KgVmNicfHxo&t=8s)

## CISSP® Study Guide

[![](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_vxZwJkHiRRzK-yNdSr7plGHvNJBNiYVaBWxrkYJ6K8mFEBjMd0GiPnI8_43VR3xuh6-0Us06eSNcEEROTkc6o8HlvLxd5YoWN4fEoYf8FRTOFBH9lC73bOzLsyDnWt-gt8SYOWsS7wLxkfxn5I=s0-d)](http://www.amazon.com/CISSP-Study-Guide-Third-Conrad/dp/0128024372)

## Twitter

[Follow @eric\_conrad](https://twitter.com/eric_conrad)

## LinkedIn

[![View Eric Conrad's profile on LinkedIn](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_t4wjVJSr0ex1sRaEIXnVlCFKdmYivzXd9UJMj2yeTLgSc0D8aYbN8FFLagTP0SoFEWxz_2kRkk-XsXZx-_xTkqnqGAZJUBUKYar5026llrQhMn7eNCjcv1034rsN8=s0-d)](http://www.linkedin.com/in/ericconrad)

## My Books

* [CISSP Study Guide 3E](http://www.amazon.com/CISSP-Study-Guide-Third-Conrad/dp/0128024372)
* [Eleventh Hour CISSP 2E](http://www.amazon.com/Eleventh-Hour-CISSP-Second-Edition/dp/0124171427)

## Join My Lists

* [CISSP](http://groups.google.com/group/ericconrad-cissp)
* [Sec511 Alumni](http://groups.google.com/d/forum/sec511)

## Upcoming Conferences

* <http://www.sans.org/instructors/eric-conrad>

## My Infosec Papers and Links

* [Waking Sleeping Dogs: Information Security Ethics](http://www.sans.edu/research/management-laboratory/article/conrad-mgt421)
* [MGT 414 Images](http://files.ericconrad.com/CISSP-Images.zip)
* [CISSP Study Guide Errata](https://docs.google.com/spreadsheets/d/15B9DexdmTXb3XKKnuHgcaTpNJxVOSZ2aiSxKlCDI2Kc)

## SANS GIAC Certifications and Gold Research

* [My SANS GIAC certifications](http://www.giac.org/certified-professional/eric-conrad/106237)
* [Detecting Spam with Genetic Regular Expressions](http://www.sans.org/reading_room/whitepapers/email/detecting-spam-genetic-regular-expressions_2006)
* [A Heap o’ Trouble / Heap-based flag insertion buffer overflow in CVS](http://pen-testing.sans.org/resources/papers/gcih/heap-o-trouble-heap-based-flag-insertion-buffer-overflow-cvs-106237)

## Blog Archive

* ►
  [2024](https://www.ericconrad.com/2024/)
  (2)
  + ►
    [April](https://www.ericconrad.com/2024/04/)
    (2)

* ▼
  [2023](https://www.ericconrad.com/2023/)
  (3)
  + ▼
    [June](https://www.ericconrad.com/2023/06/)
    (2)
    - [Introducing DeepBlueCLI v3](https://www.ericconrad.com/2023/06/introducing-deepbluecli-v3.html)
    - [Leave Only Footprints: When Prevention Fails](https://www.ericconrad.com/2023/06/leave-only-footprints-when-prevention.html)
  + ►
    [January](https://www.ericconrad.com/2023/01/)
    (1)

* ►
  [2022](https://www.ericconrad.com/2022/)
  (1)
  + ►
    [April](https://www.ericconrad.com/2022/04/)
    (1)

* ►
  [2020](https://www.ericconrad.com/2020/)
  (5)
  + ►
    [August](https://www.ericconrad.com/2020/08/)
    (1)
  + ►
    [June](https://www.ericconrad.com/2020/06/)
    (2)
  + ►
    [May](https://www.ericconrad.com/2020/05/)
    (1)
  + ►
    [January](https://www.ericconrad.com/2020/01/)
    (1)

* ►
  [2019](https://www.ericconrad.com/2019/)
  (3)
  + ►
    [November](https://www.ericconrad.com/2019/11/)
    (1)
  + ►
    [May](https://www.ericconrad.com/2019/05/)
    (1)
  + ►
    [April](https://www.ericconrad.com/2019/04/)
    (1)

* ►
  [2018](https://www.ericconrad.com/2018/)
  (4)
  + ►
    [December](https://www.ericconrad.com/2018/12/)
    (2)
  + ►
    [April](https://www.ericconrad.com/2018/04/)
    (2)

* ►
 ...