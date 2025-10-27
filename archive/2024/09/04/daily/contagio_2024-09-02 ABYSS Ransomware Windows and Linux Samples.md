---
title: 2024-09-02 ABYSS Ransomware Windows and Linux Samples
url: https://contagiodump.blogspot.com/2024/09/2024-09-02-abyss-ransomware-windows-and.html
source: contagio
date: 2024-09-04
fetch_date: 2025-10-06T18:42:52.175730
---

# 2024-09-02 ABYSS Ransomware Windows and Linux Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Tuesday, September 3, 2024

### [2024-09-02 ABYSS Ransomware Windows and Linux Samples](https://contagiodump.blogspot.com/2024/09/2024-09-02-abyss-ransomware-windows-and.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjf5cwfmW4-Mbw7MJwxQCN9u8BPRi-PDwM7XtNEdM5LOt7YdT9BCEX6YWURPxeERy-mmYetd42yAS8COStKG0WaSH82H-0X_24AWEsF7Bu8jQVC0LB5__CE9NmYavuoEISuRH9uQjKnq89ge72RzGbgO_RSbYVqO8wZ-hC7T5wvnQdQM-EyeDutvO-oB_4/s320/Google%20Chrome%202024-09-03%2012.51.56.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjf5cwfmW4-Mbw7MJwxQCN9u8BPRi-PDwM7XtNEdM5LOt7YdT9BCEX6YWURPxeERy-mmYetd42yAS8COStKG0WaSH82H-0X_24AWEsF7Bu8jQVC0LB5__CE9NmYavuoEISuRH9uQjKnq89ge72RzGbgO_RSbYVqO8wZ-hC7T5wvnQdQM-EyeDutvO-oB_4/s999/Google%20Chrome%202024-09-03%2012.51.56.png)

[2024-09-02 SocRadar: Dark Web Profile: Abyss Ransomware](https://socradar.io/dark-web-profile-abyss-ransomware/)

Abyss Ransomware, first identified in 2023, is a sophisticated ransomware strain targeting both Windows and Linux systems, with a specific focus on VMware ESXi environments. It employs advanced encryption techniques, multi-extortion tactics, and strategic network infiltration to disrupt operations across various sectors, including finance, healthcare, and technology.

Key Characteristics:

Target Platforms: Windows, Linux (particularly VMware ESXi)

Encryption: Utilizes the Salsa20 encryption algorithm; appends .abyss or .crypt extensions.

Initial Access Vectors: Phishing emails, weak SSH configurations, and exploiting known vulnerabilities in exposed servers.

Multi-Extortion Tactics: Encrypts files and exfiltrates data, threatening public exposure on a TOR-based leak site if ransom demands are not met.

Windows Variant:

Service Termination: Disables critical services (e.g., MSSQL, Exchange) to ensure encryption success.

Persistence: Alters boot configuration to disable recovery options.

File Encryption: Employs Salsa20; ransom note WhatHappened.txt is dropped in each directory.

Obfuscation: Written in C++, using techniques to evade detection and hinder forensic analysis.

Linux Variant:

VMware ESXi Targeting: Leverages esxcli to manage and shut down virtual machines for encryption.

Selective Encryption: Avoids critical system directories to maintain partial system functionality.

Persistence: Establishes daemon processes to ensure the ransomware remains active post-reboot.

**Download**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)[Download (Email me if you need the password scheme)](https://s3.amazonaws.com/contagio.deependresearch.org/Ransomware/2024-09_ABYSS_Win_Ransomware.zip)

**File Information**

**├── ├── Abyss\_Linux**

│   ├── 6f9046f4bc6517d47150caa3d6ddbc327cced5eecd86e8699d105beef388c3c0  elf\_

│   └── 72310e31280b7e90ebc9a32cb33674060a3587663c0334daef76c2ae2cc2a462  elf\_

**└── Abyss\_Windows**

├── 0079fb42859d04096cf9d6aaaaf6a463bd723b1fb7625d4137cc88b890dbec51  exe\_

├── 00fb27c489126cb61a2908f0ce15961c4af4681985e233cdac4f021fb3735ad0  exe\_

├── 03f9dccb15e19b5af71d1c831f963e834c41a42777b270bd1d60230f88fe6a95  exe\_

├── 056220ff4204783d8cc8e596b3fc463a2e6b130db08ec923f17c9a78aa2032da  exe\_

├── 07532f7b226afb8e4a931d9e51da41a6c163c4b59b7472682999ce795fd48ca1  exe\_

├── 0763e887924f6c7afad58e7675ecfe34ab615f4bd8f569759b1c33f0b6d08c64  exe\_

├── 0d2c958ee0a7a8667b93d0f9aaa265a32fbd44f3af0aaca9dfe93bfd0253d035  exe\_

├── 10eddba5af7b55a8bd815fd98184cb703583bee61812fcf3e12f8b220bf3a7c7  exe\_

├── 112a76c7fb220e0e44f96d833da260cfadb051e64a9311e19f34448eb856341f  exe\_

├── 1189c8aa073b9630958a1d8fdb81b8a1f6b538962e7b39c1de9071ab25007a23  exe\_

├── 13158c90fe1a73a8bfec9205dbfe65a5346632a637d92d8aa671737af804e61d  exe\_

├── 1a31b8e23ccc7933c442d88523210c89cebd2c199d9ebb88b3d16eacbefe4120  exe\_

├── 1d04d9a8eeed0e1371afed06dcc7300c7b8ca341fe2d4d777191a26dabac3596  exe\_

├── 25ce2fec4cd164a93dee5d00ab547ebe47a4b713cced567ab9aca4a7080afcb7  exe\_

├── 2cc6aeea99c5c45d16a4d84bf9c87c1fac3c3a390214179331d7049457ee7621  exe\_

├── 2e42b9ded573e97c095e45dad0bdd2a2d6a0a99e4f7242695054217e2bba6829  exe\_

├── 362a16c5e86f13700bdf2d58f6c0ab26e289b6a5c10ad2769f3412ec0b2da711  exe\_

├── 3b2687884f2cc8710fabcfa39264a6fa2056d5178b1a9aba027a74abdf273ed6  exe\_

├── 3fd080ef4cc5fbf8bf0e8736af00af973d5e41c105b4cd69522a0a3c34c96b6d  exe\_

├── 505934035dfcff6afabc9c29c10e1aa30187207f7c805ea10d24621d09db9277  exe\_

├── 62069d85d187ffc78dc0c8b108098016b7631b5cc7501e30be3d1515eddd781a  exe\_

├── 68cbeaccb231459ceb604934f9b4cb6fc3b51901293db9d8464074e350f11bc2  exe\_

├── 822c77cc025d12b267cf598a3bdff207b1ba278e96126590ac60d88701cd840a  exe\_

├── 877c8a1c391e21727b2cdb2f87c7b0b37fb7be1d8dd2d941f5c20b30eb65ee97  exe\_

├── 88f16d251a88b9429ca9a99d4fb3083081ff55fb7cedfb32213b4bca011e9ce7  exe\_

├── 9243bdcbe30fbd430a841a623e9e1bcc894e4fdc136d46e702a94dad4b10dfdc  exe\_

├── 94fa7d8eefce262cb2386b8fff2e1f35c8f35d570cecef54515207b9df40d97d  exe\_

├── b524773160f3cb3bfb96e7704ef31a986a179395d40a578edce8257862cafe5f  exe\_

├── ba7c611f8c14a5651b33405a521e189ad17210b36633972700540ba2056564a0  exe\_

├── d58c756206dcf233d853ddf3c7c7cfd7b2052637211f442b10b93995e969f0d7  exe\_

├── dced334f3d9739ef157ead80133d584af782e22e87d227a5ed83bf968f17d367  exe\_

├── dee2af08e1f5bb89e7bad79fae5c39c71ff089083d65da1c03c7a4c051fabae0  exe\_

├── e331eac881cbd0c473dfc63de47e9cead852625658ab7e602f9ed5128b65c6a4  exe\_

├── e5417c7a24aa6f952170e9dfcfdf044c2a7259a03a7683c3ddb72512ad0cd5c7  exe\_

├── e63420bc4a633d9e44e146ceeee17584e752b3e6fd9700137373746461d7b378  exe\_

├── e6537d30d66727c5a306dc291f02ceb9d2b48bffe89dd5eff7aa2d22e28b6d7c  exe\_

└── f88f90760aa5f3bfa3977b5f388db814b767878dc6b9d45929c1ee94d7f5c57d  exe\_

Posted by
Mila

at
[1:32 PM](https://contagiodump.blogspot.com/2024/09/2024-09-02-abyss-ransomware-windows-and.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=2784997319557447269&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-08-30-cicada-esxi-ransomware-sample.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2022-2024-north-korea-citrine-sleet.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/2784997319557447269/comments/default)

[Home](http://contagiodump.blogspot.com/)

## Shared by

[Mila](https://www.blogger.com/profile/09472209631979859691)

[View my complete profile](https://www.blogger.com/profile/09472209631979859691)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQQ9CtYxjXxYmJEJrS45nRw7TUYzsz2hcu6zvZnjwA2rbA_BZoSLQsPHHlGrZG1ArdPgFtHEOhNDHhH6A2lTR32GNPWlZWBTDFfkRgOB33dXbRM3nTCTay0WRmQ6kJdKzXE-JNPHC6qqQ/s1600/%25D0%2596%25D0%25AE%25D0%259723_filtered+%2528Custom%2529.jpg)

## About contagio

Contagio is a collection of the historic malware samples, threats, observations, and analyses.

![No Putler](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieKJB9iR6r5eAoodbA436bn8bvNdqGGqtMdUxeCz8BQ2OUkOqMPPjigFgbuG9J0Q4VTraqwm4uT-fZ--Fcbswum...