---
title: 2024-08-18 RAPTOR TRAIN NOSEDIVE - Mirai-type IoT Botnet Samples
url: https://contagiodump.blogspot.com/2024/09/2024-08-18-raptor-train-nosedive-mirai.html
source: contagio
date: 2024-09-20
fetch_date: 2025-10-06T18:30:41.534647
---

# 2024-08-18 RAPTOR TRAIN NOSEDIVE - Mirai-type IoT Botnet Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Wednesday, September 18, 2024

### [2024-08-18 RAPTOR TRAIN NOSEDIVE - Mirai-type IoT Botnet Samples](https://contagiodump.blogspot.com/2024/09/2024-08-18-raptor-train-nosedive-mirai.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9kWO6sIfAqBxRrkfFmIrRWHs_r5L_SyRVpcK8LAHziqMKuqSoO1yS3JLYDgQlmGhVEYxBM74RR_sPa-o51Itw9ueu9_6gogIJaWuHPMj_9jk_7EaQ7bMH8YTf-QCg_Uwsc8HcYz1_D2vHSOCFfRkaN8kwOCu3mCZYjTQIiGNjoT5gGEjk_ip2QXQusls/w248-h272/Google%20Chrome%202024-09-18%2022.09.57.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9kWO6sIfAqBxRrkfFmIrRWHs_r5L_SyRVpcK8LAHziqMKuqSoO1yS3JLYDgQlmGhVEYxBM74RR_sPa-o51Itw9ueu9_6gogIJaWuHPMj_9jk_7EaQ7bMH8YTf-QCg_Uwsc8HcYz1_D2vHSOCFfRkaN8kwOCu3mCZYjTQIiGNjoT5gGEjk_ip2QXQusls/s315/Google%20Chrome%202024-09-18%2022.09.57.png)

[2024-09-18 Lumen: Derailing the Raptor Train Black Lotus Labs](https://assets.lumen.com/is/content/Lumen/raptor-train-handbook-copy?Creativeid=17b819e2-06d1-4f29-a43f-a4e01b4a4fba)

The Raptor Train botnet, discovered in 2023, is a large, multi-tiered network primarily composed of compromised SOHO routers, IP cameras, NAS servers, and NVR/DVR devices. The botnet's primary implant, named "Nosedive," is a customized variant of the Mirai malware, designed to infect various IoT architectures like MIPS, ARM, PowerPC, and others. Nosedive implants are delivered via multi-stage droppers using encoded URL schemes, making detection challenging. Once deployed, the malware operates entirely in-memory, allowing for file uploads, downloads, command execution, and DDoS attacks. This memory-resident nature, combined with anti-forensics techniques such as obfuscated processes and multi-stage infections, complicates detection and analysis.

The botnet operates across three tiers: Tier 1 devices (bots), Tier 2 C2 servers, and Tier 3 management nodes. Tier 1 devices are compromised using 0-day and n-day vulnerabilities, with a lifespan of about 17 days. Tier 2 C2 nodes facilitate communication between bots and are managed from Tier 3 nodes using a custom Electron-based tool called "Sparrow." Sparrow enables operators to control C2 servers, deploy payloads, manage bots, and conduct exploitation activities.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/crime/2024-09-17%2BRAPTOR%2BTRAIN%2BNOSEDIVE%2BMirai%2BIOT%2Bbotnet.zip)

**File Information**

* ├── 2022 Finch NOSEDIVE
* │   ├── a8ca358dcd9c16eaf33d1ca583dd0f95d18ef6ce29595df55e25d09b0fca64ac elf\_
* │   └── ba2c26e641a34b1683add59e7481a22934d62ca9814e4ee0f1c71766f37dfd6d elf\_
* ├── 2023 NOSEDIVE
* │   ├── 9119babb36c94a47b5034a76fc4d56b927eae9511c86bcc7c02a4afe3fe1c0f8 elf\_
* │   ├── fcfac7831cbe120b6cf6792c3527135d84b0b97ed78fe773833f5b5f26d7a0d9 elf\_
* │   └── fe088f3553e09f62cc89f40d931be1b29491607c8f813ab17a7d664443a8e244 elf\_
* └── 2024 NOSEDIVE (2024 Yara matches for NOSEDIVE)
* ├── 88e0e0be0805fa3fb5ac0a4e29a3c7a206a63b20eaa8661a1a865061601b7f3f elf\_
* ├── 9591b845695d8fc5d99aaf8571c21d5526ab2777c64c2c6fa5ae5d491e592fc8 elf\_
* ├── b0355fe61ae232620d8f446ab8487b9b74307ff956f4e5222fc5dded53fea765 elf\_
* └── f23b9b9f09b4875f2c2f78cf50222c309cc312b0bdb01c0d3a6056bcea8eaec5 elf\_

**Malware Repo Links**

Over the past 15 years, as the blog has been around, many hosting providers have dropped support due to stricter no-malware policies. This has led to broken links, especially in older posts. If you find a broken link on contagiodump.blogspot.com (or contagiominidump.blogspot.com), just note the file name from the URL and search for it in the [Contagio Malware Storage](https://s3.amazonaws.com/contagiomobile.deependresearch.org/categories.html).

Posted by
Mila

at
[10:40 PM](https://contagiodump.blogspot.com/2024/09/2024-08-18-raptor-train-nosedive-mirai.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=566437544102749870&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-09-18-earth-baxia-apt-ripcoy.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-09-12-supershell-2023-03-13.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/566437544102749870/comments/default)

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
    - [2024-09-18 SAMBASPY Java RAT Samples](https://contagiodump.blogspot.com/2024/09/2024-09-18-sambaspy-java-rat-samples.html)
    - [2024-09-18 Earth Baxia APT - RIPCOY + SWORDLDR Sam...](https://contagiodump.blogspot.com/2024/09/2024-09-18-earth-baxia-apt-ripcoy.html)
    - [2024-08-18 RAPTOR TRAIN NOSEDIVE - Mirai-type IoT ...](https://contagiodump.blogspot.com/2024/09/2024-08-18-raptor-train-nosedive-mirai.html)
    - [2024-09-12 SUPERSHELL + 2023-03-13 SHELLBOT Target...](https://contagiodump.blogspot.com/2024/09/2024-09-12-supershell-2023-03-13.html)
...