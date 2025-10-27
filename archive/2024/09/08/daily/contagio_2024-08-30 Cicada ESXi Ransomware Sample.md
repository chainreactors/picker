---
title: 2024-08-30 Cicada ESXi Ransomware Sample
url: https://contagiodump.blogspot.com/2024/09/2024-08-30-cicada-esxi-ransomware-sample.html
source: contagio
date: 2024-09-08
fetch_date: 2025-10-06T18:25:53.495484
---

# 2024-08-30 Cicada ESXi Ransomware Sample

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Saturday, September 7, 2024

### [2024-08-30 Cicada ESXi Ransomware Sample](https://contagiodump.blogspot.com/2024/09/2024-08-30-cicada-esxi-ransomware-sample.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmZffOuHsqP4QYiZBQqam9o2k_CpvzOVm52Hl67YqkW6_fS1xHUWdgi6qK_Hb8kXQ8U_vNothiUdMzuHFGzm43Maa30FoOOKW2V5kaWC0vDyddUuSsk61-4e0gnvw49TyKh7v6Rh94wjg4gLfpiewXh2oDbymNUo0gSJGSSsG7J8LoEigeQY9US9ESsZ4/w256-h270/Google%20Chrome%202024-09-07%2017.21.52.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmZffOuHsqP4QYiZBQqam9o2k_CpvzOVm52Hl67YqkW6_fS1xHUWdgi6qK_Hb8kXQ8U_vNothiUdMzuHFGzm43Maa30FoOOKW2V5kaWC0vDyddUuSsk61-4e0gnvw49TyKh7v6Rh94wjg4gLfpiewXh2oDbymNUo0gSJGSSsG7J8LoEigeQY9US9ESsZ4/s473/Google%20Chrome%202024-09-07%2017.21.52.png)

[2024-08-30 Truesec: Dissecting the Cicada (Ransomware)](https://www.truesec.com/hub/blog/dissecting-the-cicada)  ESXi Ransomware

Cicada3301, a ransomware group first detected in June 2024, appears to be either a rebranded or derivative version of the ALPHV ransomware group, employing a ransomware-as-a-service (RaaS) model. The ransomware, written in Rust, targets both Windows and Linux/ESXi environments, utilizing ChaCha20 for encryption. Technical analysis reveals several key similarities with ALPHV: both use nearly identical command structures for shutting down VMs and removing snapshots, and share a similar file-naming convention. The ransomware's binary is an ELF file, with its Rust origin confirmed through string references and investigation of the .comment section.

Key parameters include **sleep**, which delays the ransomware's execution, and **ui**, which displays the encryption progress on the screen. The **key** parameter is crucial for decryption; if it's not provided or incorrect, the ransomware will stop running. The main function, **linux\_enc**, starts the encryption process by generating a random key using **OsRng**. Files larger than 100 MB are encrypted in parts, while smaller files are encrypted entirely using ChaCha20. The **ChaCha20 key** is then secured with an RSA public key and added, along with a specific file extension, to the end of the encrypted file.

Initial access appears to be facilitated by the Brutus botnet, with threat actors using stolen or brute-forced credentials to gain entry via ScreenConnect. The IP address associated with this attack is tied to the Brutus botnet, raising the possibility of a direct connection between the botnet operators and Cicada3301. The ransomware also features a decryption check routine, where an encoded and encrypted ransomware note stored within the binary is decrypted using the provided key, validating the correct decryption.

**Download**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)[Download. (Email me if you need the password scheme)](https://s3.amazonaws.com/contagio.deependresearch.org/Ransomware/2024-06-25_CICADA%2BRansomware_esxi.zip)

**File Information**

63e0d4e861048f581c9e5c64b28a053eb0023d58eebf2b943868d5f68a67a8b7 esxi

The article didn't include any hashes, only the YARA rule. While this sample doesn't trigger a match with the rule, I believe it's the same malware

Posted by
Mila

at
[5:31 PM](https://contagiodump.blogspot.com/2024/09/2024-08-30-cicada-esxi-ransomware-sample.html "permanent link")

Tags:
[ransomware](https://contagiodump.blogspot.com/search/label/ransomware)

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=8664823011317138208&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-09-05-shrinklocker-bitlocker.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-09-02-abyss-ransomware-windows-and.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/8664823011317138208/comments/default)

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
    - [2024-09-03 LUXY Ransomware / Stealer Sample](https://contagiodump.blogspot.com/2024/09/2024...