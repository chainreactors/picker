---
title: 2024-08-29 ASYNCRAT Samples
url: https://contagiodump.blogspot.com/2024/09/2024-08-29-asyncrat-samples.html
source: contagio
date: 2024-09-03
fetch_date: 2025-10-06T18:39:10.109770
---

# 2024-08-29 ASYNCRAT Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Monday, September 2, 2024

### [2024-08-29 ASYNCRAT Samples](https://contagiodump.blogspot.com/2024/09/2024-08-29-asyncrat-samples.html)

2024-08-29 Esentire: [Exploring AsyncRAT and Infostealer Plugin Delivery Through Phishing Emails](https://www.esentire.com/blog/exploring-asyncrat-and-infostealer-plugin-delivery-through-phishing-emails)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3AbpvnN-DomjYpBtVpC6y55xEW3VfP4rrVU2x-ZwdnXSVoOFYo3N5bttc1LbToMMCMpEODiLPDJ6l5wRMJ1lq92US7rp3jFHD-ZE3unyjQp9PQpgSzvVU2PAH4scIMrUBlrwzDduuvQB0QqefE0iIMPe7knK90ggiaKOu3Ak2q6lqTFd9hSIYB_R9ae8/w263-h268/Google%20Chrome%202024-09-02%2013.23.16.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3AbpvnN-DomjYpBtVpC6y55xEW3VfP4rrVU2x-ZwdnXSVoOFYo3N5bttc1LbToMMCMpEODiLPDJ6l5wRMJ1lq92US7rp3jFHD-ZE3unyjQp9PQpgSzvVU2PAH4scIMrUBlrwzDduuvQB0QqefE0iIMPe7knK90ggiaKOu3Ak2q6lqTFd9hSIYB_R9ae8/s343/Google%20Chrome%202024-09-02%2013.23.16.png)eSentire's Threat Response Unit (TRU) discovered an AsyncRAT infection that was delivered through a Windows Script File (.wsf) via email. The malicious `.wsf` file, named “SummaryForm\_,” downloaded a VBScript from a remote server, which then fetched a fake image file.

This file was actually a ZIP archive that, once extracted, ran additional scripts to establish persistence on the system. The scripts created a scheduled task to execute the AsyncRAT payload repeatedly, making it difficult to detect and remove. The payload was injected into the `RegAsm.exe` process using a DLL to further evade detection.

Additionally, this version of AsyncRAT included an infostealer plugin designed to exfiltrate data from popular web browsers like Chrome and Firefox, as well as cryptocurrency wallet extensions such as MetaMask and Coinbase. The attack highlights the use of multiple stages and obfuscation techniques to maintain persistence and steal sensitive information from the infected system.

**Download**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/crime/2024-08-29_Win_AsyncRat.zip)

**File Information**

├── 29b4af288f1bb75da4df5cbf00033c68df1fee656433cb99726f16de8c2b55f1 uzopuzbkrpcziwca txt

├── 5768a2bfeaa935af64b66bec24cc4d35c7919e1317daa072f8902a7354f3bf8d WJVIQQFZMZLSZTJJ bat

├── 5b1b7bd1fadfc3d2abcd8ea8f863fe96233e1dac8b994311c6a331179243b5cd NewPE2 dll

├── 7d91feeb19c895927012f56d9502ba8a9345ff955adc7d20f2e3a660a029769e SummaryForm  wsf

├── 82dcc44da4b3454291a1d846414efde776b51bf2d30406cb9aa5bac020b0c4c5 AsyncRAT

├── ab2bef5c63ac65904386a02f4c7d9bbceaafa3763aceef24fd7981ca993006a4 CEIULUDEZFCEVSMM bat

├── b8631fd49a327589f97232eefc14bec144ef6fdd43d3d79ce9fab3adf8067221 IRUAHCKDFAFDCHUV vbs

├── c351fafa32e9c2e91a514c10fa8097da0f837c2a4bfcbac0e899f5780fd8b69a YXRPNPSMGCOBEURV ps1

└── d381eeba306533d765ae541fcb737f408abbeeed2f15ae1b1c678adde3960d31 lAOdPuUqwXLVFvqT jpg

Posted by
Mila

at
[1:27 PM](https://contagiodump.blogspot.com/2024/09/2024-08-29-asyncrat-samples.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=5256913899659729528&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-08-28-corona-mirai-botnet-spreads.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-08-29-underground-ransomware.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/5256913899659729528/comments/default)

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
    - [2024-08-30 Cicada ESXi Ransomware Sample](https://contagiodump.blogspot.com/2024/09/2024-08-30-cicada-esxi-r...