---
title: 2024-10-25 HeptaX - Unauthorized RDP Connections. Nalicious LNK. > Powershell > Bat files Samples
url: https://contagiodump.blogspot.com/2024/10/2024-10-25-heptax-unauthorized-rdp.html
source: contagio
date: 2024-10-30
fetch_date: 2025-10-06T18:55:52.836973
---

# 2024-10-25 HeptaX - Unauthorized RDP Connections. Nalicious LNK. > Powershell > Bat files Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Monday, October 28, 2024

### [2024-10-25 HeptaX - Unauthorized RDP Connections. Nalicious LNK. > Powershell > Bat files Samples](https://contagiodump.blogspot.com/2024/10/2024-10-25-heptax-unauthorized-rdp.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-Ohg1kUL3_h76HZsWkiYgcsRANO_spdYHTLlNW4anzvxRkXTfbJykeKJZ49O85yQWcDa9vjod_suZz5wRteuF5iOgU5AwgP4HcLRIdpfh_BVV8eSkIIdpIPI-OItynOD08-3jiO3EIdSwjcMJqQyUM1SvoRTdekv4R9pNsWAZ_ygkPNXnTCWOFRdzHVM/w245-h244/Discord%202024-10-28%2022.50.38.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-Ohg1kUL3_h76HZsWkiYgcsRANO_spdYHTLlNW4anzvxRkXTfbJykeKJZ49O85yQWcDa9vjod_suZz5wRteuF5iOgU5AwgP4HcLRIdpfh_BVV8eSkIIdpIPI-OItynOD08-3jiO3EIdSwjcMJqQyUM1SvoRTdekv4R9pNsWAZ_ygkPNXnTCWOFRdzHVM/s287/Discord%202024-10-28%2022.50.38.png)

[2024-10-25 Cyble:](https://cyble.com/blog/heptax-unauthorized-rdp-connections-for-cyberespionage-operations/)

[HeptaX: Unauthorized RDP Connections for Cyberespionage Operations](https://cyble.com/blog/heptax-unauthorized-rdp-connections-for-cyberespionage-operations/)

Summary:

* The attack starts with a malicious LNK file delivered within a ZIP file, likely distributed through phishing emails, and seems to target the healthcare industry.
* Upon execution, the LNK file initiates a PowerShell command that downloads multiple scripts and batch files from a remote server to establish persistence and control over the victim’s system.

1. * The LNK file, once opened, triggers PowerShell commands that download additional payloads from `hxxp://157.173.104[.]153`.
   * These scripts enable the attacker to create a new user account with administrative privileges and alter RDP settings, reducing authentication requirements for easier unauthorized access.
2. * A persistent shortcut (LNK) file is created in the Windows Startup folder to maintain access.
   * The primary PowerShell script communicates with the C2 server, constructing URLs with a unique identifier (UID) for the compromised machine to fetch commands or additional payloads.
   * If UAC is detected as weak or disabled, the attack proceeds with further stages that lower the system's security configurations.
3. * A secondary payload, "ChromePass," is introduced, targeting Chromium-based browsers to harvest stored credentials, escalating the risk of compromised accounts.
   * Scripts configure the system to facilitate remote desktop access, enabling actions such as data exfiltration, monitoring, and installation of further malware.
4. * Subsequent batch files (e.g., `k1.bat`, `scheduler-once.bat`) execute commands that hide traces, remove logs, and schedule tasks disguised as system operations to maintain persistence and evade detection.
   * The final stages involve the execution of a PowerShell script that performs reconnaissance, collects extensive system data, and sends it encoded to the C2 server.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.us-east-1.amazonaws.com/contagio.deependresearch.org/APT/tbd/2024-10-25%2BHeptaX%2BPs%2BBat.zip)

**File Information**

* ├── 18e75bababa1176ca1b25f727c0362e4bb31ffc19c17e2cabb6519e6ef9d2fe5 Google Chrome.lnk
* ├── 1d82927ab19db7e9f418fe6b83cf61187d19830b9a7f58072eedfd9bdf628dab bb.ps1
* ├── 4b127e7b83148bfbe56bd83e4b95b2a4fdb69e1c9fa4e0c021a3bfb7b02d8a16 ChromePass.exe
* ├── 5ff89db10969cba73d1f539b12dad42c60314e580ce43d7b57b46a1f915a6a2b 202409 Resident Care Quality Improvement Strategies for Nursing Homes Enhancing Patient Satisfaction and Health Outcomes.pdf.lnk
* ├── 6605178dbc4d84e789e435915e86a01c5735f34b7d18d626b2d8810456c4bc72.zip
* ├── 999f521ac605427945035a6d0cd0a0847f4a79413a4a7b738309795fd21d3432 k1.bat
* └── a8d577bf773f753dfb6b95a3ef307f8b4d9ae17bf86b95dcbb6b2fb638a629b9 b.ps1

**Malware Repo Links**

Over the past 15 years, as the blog has been around, many hosting providers have dropped support due to stricter no-malware policies. This has led to broken links, especially in older posts. If you find a broken link on contagiodump.blogspot.com (or contagiominidump.blogspot.com), just note the file name from the URL and search for it in the [Contagio Malware Storage](https://s3.amazonaws.com/contagiomobile.deependresearch.org/categories.html).

Posted by
Mila

at
[10:55 PM](https://contagiodump.blogspot.com/2024/10/2024-10-25-heptax-unauthorized-rdp.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=471790487352760219&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/10/2024-10-23-warmcookiebadspace-apt-ta866.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/10/2024-10-03-amnesia-stealer-samples.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/471790487352760219/comments/default)

[Home](http://contagiodump.blogspot.com/)

## Shared by

[Mila](https://www.blogger.com/profile/09472209631979859691)

[View my complete profile](https://www.blogger.com/profile/09472209631979859691)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQQ9CtYxjXxYmJEJrS45nRw7TUYzsz2hcu6zvZnjwA2rbA_BZoSLQsPHHlGrZG1ArdPgFtHEOhNDHhH6A2lTR32GNPWlZWBTDFfkRgOB33dXbRM3nTCTay0WRmQ6kJdKzXE-JNPHC6qqQ/s1600/%25D0%2596%25D0%25AE%25D0%259723_filtered+%2528Custom%2529.jpg)

## About contagio

Contagio is a collection of the historic malware samples, threats, observations, and analyses.

![No Putler](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieKJB9iR6r5eAoodbA436bn8bvNdqGGqtMdUxeCz8BQ2OUkOqMPPjigFgbuG9J0Q4VTraqwm4uT-fZ--Fcbswum1s2H7F6-lmZN2oqT51VHA6NziTxCaIfNCaXBAQQ80BvDJT1zNHONhsTaKRI_AjnYg6kORfoAlunUylRHoWiapLkUxBSeoa-rTzY/s618/NoPutler.png)

Malware samples are available for download by any responsible whitehat researcher.

By downloading the samples, anyone waives all rights to claim punitive, incidental and consequential damages resulting from mishandling or self--infection

If you see errors, typos, etc, please let me know.

## About Contagio Mobile

[Contagio mobile mini-dump](http://contagiominidump.blogspot.com/) is a part of contagiodump.blogspot.com.

[Twitter](http://twitter.com/snowfl0w)
[LinkedIn](https://www.linkedin.com/in/milaparkour/)

## Blog Archive

* ▼
  [2024](https://contagiodump.blogspot.com/2024/)
  (27)
  + ►
    [November](https://contagiodump.blogspot.com/2024/11/)
    (2)
  + ▼
    [October](https://contagiodump.blogspot.com/2024/10/)
    (3)
    - [2024-10-23 WarmCookie/BadSpace - APT TA866 - Samples](https://contagiodump.blogspot.com/2024/10/2024-10-23-warmcookiebadspace-apt-ta866.html)
    - [2024-10-25 HeptaX - Unauthorized RDP Connections. ...](https://contagiodump.blogspot.com/2024/10/2024-10-25-heptax-unauthorized-rdp.html)
    - [2024-10-03 Amnesia Stealer Samples](https://contagiodump.blogspot.com/2024/10/2024-10-03-amnesia-stealer-samples.html)
  + ►
    [September](https://contagiodump.blogspot.com/2024/09/)
    (22)

* ►
  [2023](https://contagiodump.blogspot.c...