---
title: 2024-09-05 SHRINKLOCKER (Bitlocker) Ransomware Samples
url: https://contagiodump.blogspot.com/2024/09/2024-09-05-shrinklocker-bitlocker.html
source: contagio
date: 2024-09-08
fetch_date: 2025-10-06T18:25:50.620443
---

# 2024-09-05 SHRINKLOCKER (Bitlocker) Ransomware Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Saturday, September 7, 2024

### [2024-09-05 SHRINKLOCKER (Bitlocker) Ransomware Samples](https://contagiodump.blogspot.com/2024/09/2024-09-05-shrinklocker-bitlocker.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9T_6qg_HUo5fCI6I8oT3dmhrGI48wzuinH1tigDjdZIbMsiDYztvKWoCsQCFBMJjVGleJ3r9FGooZjjtHHagQfiTbENyaXpAL5_TKCmk4zY5hxWTgPHkmgplKjhp-aeFfknYhfBJ4p6sXwn2bmw2mGDn_3sUScsPs6KeYpVkhLmYejE8F7p3zuGTnYh4/w256-h266/Google%20Chrome%202024-09-07%2017.37.16.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9T_6qg_HUo5fCI6I8oT3dmhrGI48wzuinH1tigDjdZIbMsiDYztvKWoCsQCFBMJjVGleJ3r9FGooZjjtHHagQfiTbENyaXpAL5_TKCmk4zY5hxWTgPHkmgplKjhp-aeFfknYhfBJ4p6sXwn2bmw2mGDn_3sUScsPs6KeYpVkhLmYejE8F7p3zuGTnYh4/s375/Google%20Chrome%202024-09-07%2017.37.16.png)

2024-09-05 Splunk: ShrinkLocker Malware: Abusing BitLocker to Lock Your Data

ShrinkLocker is a newly discovered ransomware strain that exploits BitLocker, a legitimate Windows feature, to encrypt data by locking users out of their systems. Unlike traditional ransomware, ShrinkLocker leverages BitLocker's secure boot partition to make decryption extremely challenging. The malware initiates its attack by identifying the operating system and determining whether it’s a suitable target. It modifies key system registry settings, particularly those related to Remote Desktop Protocol (RDP) and Trusted Platform Module (TPM), to suit its objectives. After disabling BitLocker key protectors, ShrinkLocker shrinks non-boot partitions by 100MB, formats these partitions, and reconfigures boot files to destabilize the system, potentially rendering it irreparable. The malware also exfiltrates data to a command-and-control server and attempts to erase traces of its activity by deleting logs, firewall rules, and scheduled tasks.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/Ransomware/2024-09-07_SHRINKLOCKER%2BRansomware.zip)

**File Information**

d4f2c5b21e96cfef0fc4e5acb6bde30113d1c8c7522f35d99102de886ed337b3 disk.vbs\_

32f31b35179bbff9ca9dd21b43bfc3e585baafedde523bd3e4869400ab0362cb Dim oShell.txt  (vba)

7662aeae889c350bdabdcc89ccc4c117e0fffdc06933dd7058946fa74a0842bb run.vbs

**Malware Repo Links**

Over the past 15 years, as the blog has been around, many hosting providers have dropped support due to stricter no-malware policies. This has led to broken links, especially in older posts. If you find a broken link on contagiodump.blogspot.com (or contagiominidump.blogspot.com), just note the file name from the URL and search for it in the [Contagio Malware Storage](https://s3.amazonaws.com/contagiomobile.deependresearch.org/categories.html).

Posted by
Mila

at
[5:39 PM](https://contagiodump.blogspot.com/2024/09/2024-09-05-shrinklocker-bitlocker.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=9139770928154406357&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-09-03-luxy-ransomware-stealer.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-08-30-cicada-esxi-ransomware-sample.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/9139770928154406357/comments/default)

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
    - [2024-09-19 X-WORM RAT (Phishing) Samples](https://contagiodump.blogspot.com/2024/09/2024-09-19-x-worm-phishing-samples.html)
    - [2023-11-23 BEAVERTAIL and INVISIBLE\_FERRET Lazarus...](https://contagiodump.blogspot.com/2024/09/2023-11-23-beavertail-and.html)
    - [2024-09-10 KIMSUKY (North Korean APT) Sample (Saka...](https://contagiodump.blogspot.com/2024/09/2024-09-10-kimsuky-north-korean-apt.html)
    - [2024-09-03 LUXY Ransomware / Stealer Sample](https://contagiodump.blogspot.com/2024/09/2024-09-03-luxy-ransomware-stealer.html)
    - [2024-09-05 SHRINKLOCKER (Bitlocker) Ransomware Sam...](https://contagiodump.blogspot.com/2024/09/2024-09-05-shrinklocker-bitlocker.html)
    - [2024-08-30 Cicada ESXi Ransomware Sample](https://contagiodump.blogspot.com/2024/09/2024-08-30-cicada-esxi-ransomware-sample.html)
    - [2024-09-02 ABYSS Ransomware Windows and Linux Samples](https://contagiodump.blogspot.com/2024/09/2024-09-02-abyss-ransomware-windows-and.html)
    - [2...