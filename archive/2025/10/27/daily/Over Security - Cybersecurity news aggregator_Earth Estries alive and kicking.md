---
title: Earth Estries alive and kicking
url: https://bartblaze.blogspot.com/2025/10/earth-estries-alive-and-kicking.html
source: Over Security - Cybersecurity news aggregator
date: 2025-10-27
fetch_date: 2025-10-28T03:00:12.004916
---

# Earth Estries alive and kicking

# [Blaze's Security Blog](https://bartblaze.blogspot.com/)

Personal blog about internet & malware threats.

## Search this Blog

|  |  |
| --- | --- |
|  |  |

* [Home](https://bartblaze.blogspot.com/)
* [Ransomware Prevention](https://bartblaze.blogspot.com/p/ransomware-prevention.html)
* [The purpose of ransomware](https://bartblaze.blogspot.com/p/the-purpose-of-ransomware.html)
* [About Me & Disclaimer](https://bartblaze.blogspot.com/p/about.html)

## Monday, October 27, 2025

### Earth Estries alive and kicking

Earth Estries, also known as Salt Typhoon and a few other names, is a China-nexus APT actor, and is known to have used multiple implants such as Snappybee (Deed RAT), ShadowPad, and several more.

In their latest campaign, the actor leverages one of the latest WinRAR vulnerabilities that will ultimately lead to running shellcode.

The execution flow is as follows:

![A screenshot of a computer  AI-generated content may be incorrect.](https://blogger.googleusercontent.com/img/a/AVvXsEhl50hr9ggmOl-EQ7YlL-_Sq3iXmSlG7LlfKOYF4MbzTWvFFrTnfsj6o_70f5fq9s6mFNU6vQogrNLaNKTVSK4Fo0V2SlW31LB2HPQbKgZikQBWErFCG_g86DSVgn5TLZSu4IZbO4odawkuFRqArsjSmC5T2UcMlMB8BmoYkFUlORNHz8-y71QRUGhfpo5p)

That is all. Find below indicators of compromise and Yara rules.

|  |  |  |
| --- | --- | --- |
| **Indicator** | **Type** | **Purpose** |
| f8c119bfc057dc027e6c54b966d168ee1ef38c790e581fb44cf965ca0408db1d | SHA256 Hash | CAB file storing ccwkrlib.dll |
| 94aa6619c61d434e96ca8d128731eb7ee81e399a59a17f751a31b564a7f3a722 | SHA256 Hash | Encrypted stub |
| 3c84a5255e0c08e96278dea9021e52c276b4a6c73af9fa81520aefb4a8040a8b | SHA256 Hash | CAB file storing RES.RC |
| 3822207529127eb7bdf2abc41073f6bbe4cd6e9b95d78b6d7dd04f42d643d2c3 | SHA256 Hash | Dropper |
| 64ca55137ba9fc5d005304bea5adf804b045ec10c940f6c633ffde43bc36ff3f | SHA256 Hash | Fake PDF with ADS stream |
| 6c6af015e0bfec69f7867f8c957958aa25a13443df1de26fa88d56a240bdd5ad | SHA256 Hash | Hijacked DLL, bloated |
| 5e062fee5b8ff41b7dd0824f0b93467359ad849ecf47312e62c9501b4096ccda | SHA256 Hash | Hijacked DLL |
| 3b47df790abb4eb3ac570b50bf96bb1943d4b46851430ebf3fc36f645061491b | SHA256 Hash | Downloads CommonSDK.exe |
| ccwkrlib.dll | Filename | Hijacked DLL |
| RES.RC | Filename | Encrypted stub |
| CommonSDK.exe | Filename | Fake PDF with ADS stream |
| doc20250921133625.pdf | Filename | Fake PDF with ADS stream |
| startup.bat | Filename | Downloads CommonSDK.exe |
| WindowsTarys | Filename | Scheduled task |
| 38[.]54[.]105[.]114 | IP Address | Download server |
| mimosa[.]gleeze[.]com | Domain | C2 Server |

**Associated Yara rules are available on my Github:**

[https://github.com/bartblaze/Yara-rules](https://github.com/bartblaze/Yara-rules%20)

Rule names:

* EE\_Loader
* EE\_Dropper
* WinRAR\_ADS\_Traversal

**References / Resources:**

WinRAR CVE:

<https://nvd.nist.gov/vuln/detail/CVE-2025-8088>

<https://www.welivesecurity.com/en/eset-research/update-winrar-tools-now-romcom-and-others-exploiting-zero-day-vulnerability/>

Earth Estries:

https://jsac.jpcert.or.jp/archive/2025/pdf/JSAC2025\_1\_5\_leon-chang\_theo-chen\_en.pdf

https://www.trendmicro.com/en\_us/research/25/j/premier-pass-as-a-service.html

https://malpedia.caad.fkie.fraunhofer.de/actor/earth\_estries

https://malpedia.caad.fkie.fraunhofer.de/actor/ghostemperor

Posted by

[Bart](https://www.blogger.com/profile/18326761248866196755 "author profile")

at
[11:09 PM](https://bartblaze.blogspot.com/2025/10/earth-estries-alive-and-kicking.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/606282676955748155/4134049422110915211 "Email Post")

[Email This](https://www.blogger.com/share-post.g?blogID=606282676955748155&postID=4134049422110915211&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=606282676955748155&postID=4134049422110915211&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=606282676955748155&postID=4134049422110915211&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=606282676955748155&postID=4134049422110915211&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=606282676955748155&postID=4134049422110915211&target=pinterest "Share to Pinterest")

Labels:
[earth estries](https://bartblaze.blogspot.com/search/label/earth%20estries)

#### No comments:

#### Post a Comment

[Older Post](https://bartblaze.blogspot.com/2025/06/steam-phishing-popular-as-ever.html "Older Post")
[Home](https://bartblaze.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://bartblaze.blogspot.com/feeds/4134049422110915211/comments/default)

## Blog Archive

* ▼
  [2025](https://bartblaze.blogspot.com/2025/)
  (2)
  + ▼
    [October](https://bartblaze.blogspot.com/2025/10/)
    (1)
    - [Earth Estries alive and kicking](https://bartblaze.blogspot.com/2025/10/earth-estries-alive-and-kicking.html)
  + ►
    [June](https://bartblaze.blogspot.com/2025/06/)
    (1)

* ►
  [2024](https://bartblaze.blogspot.com/2024/)
  (3)
  + ►
    [August](https://bartblaze.blogspot.com/2024/08/)
    (1)
  + ►
    [June](https://bartblaze.blogspot.com/2024/06/)
    (1)
  + ►
    [March](https://bartblaze.blogspot.com/2024/03/)
    (1)

* ►
  [2023](https://bartblaze.blogspot.com/2023/)
  (1)
  + ►
    [December](https://bartblaze.blogspot.com/2023/12/)
    (1)

* ►
  [2022](https://bartblaze.blogspot.com/2022/)
  (1)
  + ►
    [December](https://bartblaze.blogspot.com/2022/12/)
    (1)

* ►
  [2021](https://bartblaze.blogspot.com/2021/)
  (1)
  + ►
    [June](https://bartblaze.blogspot.com/2021/06/)
    (1)

* ►
  [2020](https://bartblaze.blogspot.com/2020/)
  (2)
  + ►
    [November](https://bartblaze.blogspot.com/2020/11/)
    (1)
  + ►
    [January](https://bartblaze.blogspot.com/2020/01/)
    (1)

* ►
  [2019](https://bartblaze.blogspot.com/2019/)
  (3)
  + ►
    [November](https://bartblaze.blogspot.com/2019/11/)
    (1)
  + ►
    [March](https://bartblaze.blogspot.com/2019/03/)
    (2)

* ►
  [2018](https://bartblaze.blogspot.com/2018/)
  (12)
  + ►
    [August](https://bartblaze.blogspot.com/2018/08/)
    (1)
  + ►
    [June](https://bartblaze.blogspot.com/2018/06/)
    (1)
  + ►
    [May](https://bartblaze.blogspot.com/2018/05/)
    (2)
  + ►
    [April](https://bartblaze.blogspot.com/2018/04/)
    (5)
  + ►
    [February](https://bartblaze.blogspot.com/2018/02/)
    (2)
  + ►
    [January](https://bartblaze.blogspot.com/2018/01/)
    (1)

* ►
  [2017](https://bartblaze.blogspot.com/2017/)
  (16)
  + ►
    [December](https://bartblaze.blogspot.com/2017/12/)
    (2)
  + ►
    [November](https://bartblaze.blogspot.com/2017/11/)
    (1)
  + ►
    [October](https://bartblaze.blogspot.com/2017/10/)
    (3)
  + ►
    [September](https://bartblaze.blogspot.com/2017/09/)
    (1)
  + ►
    [August](https://bartblaze.blogspot.com/2017/08/)
    (1)
  + ►
    [July](https://bartblaze.blogspot.com/2017/07/)
    (1)
  + ►
    [June](https://bartblaze.blogspot.com/2017/06/)
    (1)
  + ►
    [May](https://bartblaze.blogspot.com/2017/05/)
    (2)
  + ►
    [April](https://bartblaze.blogspot.com/2017/04/)
    (1)
  + ►
    [March](https://bartblaze.blogspot.com/2017/03/)
    (2)
  + ►
    [February](https://bartblaze.blogspot.com/2017/02/)
    (1)

* ►
  [2016](https://bartblaze.blogspot.com/2016/)
  (12)
  + ►
    [November](https://bartblaze.blogspot.com/2016/11/)
    (2)
  + ►
    [July](https://bartblaze.blogspot.com/2016/07/)
    (1)
  + ►
    [May](https://bartblaze.blogspot.com/2016/05/)
    (2)
  + ►
    [April](https://bartblaze.blogspot.com/2016/04/)
    (1)
  + ►
    [March](https://bartblaze.blogspot.com/2016/03/)
    (2)
  + ►
    [February](https://bartblaze.blogspot.com/2016/02/)
    (2)
  + ►
    [January](https://bartblaze.blogspot.com/2016/01/)
    (2)

* ►
  [2015](https://bartblaze.blogspot.com/2015/)
  (7)
  + ►
    [November](https://bartblaze.blogspot.com/2...