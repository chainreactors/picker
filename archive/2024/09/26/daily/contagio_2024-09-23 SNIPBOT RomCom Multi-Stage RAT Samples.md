---
title: 2024-09-23 SNIPBOT RomCom Multi-Stage RAT Samples
url: https://contagiodump.blogspot.com/2024/09/2024-09-23-snipbot-romcom-multi-stage.html
source: contagio
date: 2024-09-26
fetch_date: 2025-10-06T18:34:41.575925
---

# 2024-09-23 SNIPBOT RomCom Multi-Stage RAT Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Wednesday, September 25, 2024

### [2024-09-23 SNIPBOT RomCom Multi-Stage RAT Samples](https://contagiodump.blogspot.com/2024/09/2024-09-23-snipbot-romcom-multi-stage.html)

|  |
| --- |
| [![Image courtesy of Palo Alto](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCM-k5MhrtPJZS1sogFXxdZ7WDYOBhgLUkO38NqFHItGZrJ3fF0jrTLKoTFgZu8mvSruu2pJM6NAHxpc_cF7WOdjTW3EpTxfSg8go1-oqSUhiRl23L1HF1XIUrd65jeZtM8_R9URRNWDSNLqtgky-JStkcyJr9KdlvaCOFqxQ_N-OK0C5AeuMx813GvPQ/w320-h285/Firefox%202024-09-25%2019.34.23.png "Image courtesy of Palo Alto")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCM-k5MhrtPJZS1sogFXxdZ7WDYOBhgLUkO38NqFHItGZrJ3fF0jrTLKoTFgZu8mvSruu2pJM6NAHxpc_cF7WOdjTW3EpTxfSg8go1-oqSUhiRl23L1HF1XIUrd65jeZtM8_R9URRNWDSNLqtgky-JStkcyJr9KdlvaCOFqxQ_N-OK0C5AeuMx813GvPQ/s1166/Firefox%202024-09-25%2019.34.23.png) |
| Image courtesy of Palo Alto |

[2024-09-23 Palo Alto Unit42: Inside SnipBot: The Latest RomCom Malware Variant](https://unit42.paloaltonetworks.com/snipbot-romcom-malware-variant/)

This latest version integrates novel obfuscation techniques and exhibits distinct post-infection activities not seen in previous variants (RomCom 3.0 and PEAPOD/RomCom 4.0).

**Key Points:**

* **Capabilities:** SnipBot allows attackers to execute commands and download additional modules onto the victim's system. It deploys an initial signed executable downloader, followed by unsigned EXEs or DLLs.
* **Infection Vector:** Delivered via email containing links that redirect to the SnipBot downloader. The downloader uses anti-sandbox tricks, including checking the file’s original name and verifying at least 100 entries in the `RecentDocs` registry key. It also employs window message-based control flow obfuscation.
* **Post-Infection Activity:**
  + Downloads additional DLL payloads, injecting them into `explorer.exe` using COM hijacking. Specifically, it registers the malicious DLL (`keyprov.dll`) as a thumbnail cache library in the registry (`HKCU\SOFTWARE\Classes\CLSID`).
  + The primary payload, `single.dll`, listens on port 1342 for commands such as deleting registry keys, executing stored DLL payloads, and initiating further updates.
  + Creates and manages registry keys (`HKCU\SOFTWARE\AppDataSoft\Software`) to store encrypted payloads and keep track of updates.
* **Command & Control:** Contacts its C2 domains (e.g., `xeontime[.]com`) to download payloads. Encrypts strings, including the C2 domain and API function names, to evade detection.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/crime/2024-09-23%2BSNIPBOT%2BRomCom.zip)

**File Information**

* ├── 0be3116a3edc063283f3693591c388eec67801cdd140a90c4270679e01677501 atch scan052224 CV.exe
* ├── 2c327087b063e89c376fd84d48af7b855e686936765876da2433485d496cb3a4.exe
* ├── 5390ba094cf556f9d7bbb00f90c9ca9e04044847c3293d6e468cb0aaeb688129 Attachment CV June2024.exe
* ├── 57e59b156a3ff2a3333075baef684f49c63069d296b3b036ced9ed781fd42312 Attachment Medical report.exe
* ├── 5b30a5b71ef795e07c91b7a43b3c1113894a82ddffc212a2fa71eebc078f5118  CV for a job.exe
* ├── 5c71601717bed14da74980ad554ad35d751691b2510653223c699e1f006195b8  Atch Data Breach Evidence.pdf                                                                                          Open with Adobe Acrobat.exe
* ├── a2f2e88a5e2a3d81f4b130a2f93fb60b3de34550a7332895a084099d99a3d436  atch List of Available Documents.exe
* ├── b9677c50b20a1ed951962edcb593cce5f1ed9c742bc7bff827a6fc420202b045  webtime-e.exe
* ├── cfb1e3cc05d575b86db6c85267a52d8f1e6785b106797319a72dd6d19b4dc317.exe
* └── f74ebf0506dc3aebc9ba6ca1e7460d9d84543d7dadb5e9912b86b843e8a5b671 резюме.pdf

**Malware Repo Links**

Over the past 15 years, as the blog has been around, many hosting providers have dropped support due to stricter no-malware policies. This has led to broken links, especially in older posts. If you find a broken link on contagiodump.blogspot.com (or contagiominidump.blogspot.com), just note the file name from the URL and search for it in the [Contagio Malware Storage](https://s3.amazonaws.com/contagiomobile.deependresearch.org/categories.html).

Posted by
Mila

at
[7:38 PM](https://contagiodump.blogspot.com/2024/09/2024-09-23-snipbot-romcom-multi-stage.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=1054278828715779902&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-09-24-linux-malware-cryptocurrency.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-09-19-unc1860-iran-apt-temple-of.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/1054278828715779902/comments/default)

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
  + ►
    [October](https://contagiodump.blogspot.com/2024/10/)
    (3)
  + ▼
    [September](https://contagiodump.blogspot.com/2024/09/)
    (22)
    - [2024-09-24 Linux Malware Cryptocurrency Miners, DO...](https://contagiodump.blogspot.com/2024/09/2024-09-24-linux-malware-cryptocurrency.html)
    - [2024-09-23 SNIPBOT RomCom Multi-Stage RAT Samples](https://contagiodump.blogspot.com/2024/09/2024-09-23-snipbot-romcom-multi-stage.html)
    - [2024-09-19 UNC1860 Iran APT - Temple of Oats ( OA...](https://contagiodump.blogspot.com/2024/09/2024-09-19-unc1860-iran-apt-temple-of.html)
    - [2024-09-18 SAMBASPY Java RAT Samples](https://contagiodump.blogspot.com/2024/09/2...