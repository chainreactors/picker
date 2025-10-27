---
title: 2024-08-14 OSX BANSHEE infostealer Samples
url: https://contagiodump.blogspot.com/2024/09/2024-08-14-osx-banshee-infostealer.html
source: contagio
date: 2024-09-03
fetch_date: 2025-10-06T18:39:15.247517
---

# 2024-08-14 OSX BANSHEE infostealer Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Monday, September 2, 2024

### [2024-08-14 OSX BANSHEE infostealer Samples](https://contagiodump.blogspot.com/2024/09/2024-08-14-osx-banshee-infostealer.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh73L95T8Tuv11a89wP0urvUsKWNlKz0eeFUHtueWZlDvB02NDlwactbkOb51ArwmLbE8plOk5wLMv1alKsnkf3d-CfM7tbCpOFPUhyrLB0pMAdBt_qaH60raOq-p0D8BPVAJbO8Up_es5DDuiv3Xv8vIQLTA_DfyeU2HEHu4o519qGCu4x9bqul3ZHCHg/s320/Affinity%20Designer%202024-09-02%2012.38.51.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh73L95T8Tuv11a89wP0urvUsKWNlKz0eeFUHtueWZlDvB02NDlwactbkOb51ArwmLbE8plOk5wLMv1alKsnkf3d-CfM7tbCpOFPUhyrLB0pMAdBt_qaH60raOq-p0D8BPVAJbO8Up_es5DDuiv3Xv8vIQLTA_DfyeU2HEHu4o519qGCu4x9bqul3ZHCHg/s442/Affinity%20Designer%202024-09-02%2012.38.51.png)

[2024-08-14 Elastic: Beyond the wail: deconstructing the BANSHEE infostealer](https://www.elastic.co/security-labs/beyond-the-wail)

 This analysis of BANSHEE Stealer reveals a sophisticated macOS-based malware (sold for $3,000) developed by Russian threat actors, targeting both x86\_64 and ARM64 architectures. BANSHEE Stealer is designed to collect a wide range of data from infected systems, including browser history, cookies, logins, cryptocurrency wallets, and around 100 browser extensions. The malware employs basic anti-analysis techniques, such as debugging and virtualization detection using the sysctl API and system profiling commands, and avoids infecting systems set to the Russian language.

It uses AppleScripts for tasks like muting system sound, phishing for user passwords, and copying keychain data. The stolen data is then compressed, XOR-encrypted, Base64-encoded, and exfiltrated to a remote server.

BANSHEE Stealer targets nine browsers for browser data collection—Chrome, Firefox, Brave, Edge, Vivaldi, Yandex, Opera, OperaGX, and Safari - extracting history, cookies, and login credentials. Interestingly, it focuses on Safari cookies using an AppleScript script, while other browsers have a broader range of data collected. The malware also scans for around 100 browser plugins, saving the data in a specified temporary directory.

BANSHEE Stealer targets wallets like Exodus, Electrum, Coinomi, Guarda, Wasabi, Atomic, and Ledger. It copies wallet-related files to a temporary directory for later exfiltration. The malware's functionality is structured in several C++ files, including Controller. cpp, which manages core tasks like anti-debugging measures using the sysctl API, language checks via CFLocaleCopyPreferredLanguages, and exfiltration processes.

The malware's exfiltration method involves compressing the collected data into a ZIP file using the ditto command, followed by XOR encryption and Base64 encoding. The resulting file is then exfiltrated via an HTTP POST request to a command-and-control server using the cURL command.

**Download**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)[Download. (Email me if you need the password)](https://s3.amazonaws.com/contagio.deependresearch.org/crime/2024-08-14_OSX_Banshee_Stealer.zip)

d556042c8a77ba52d39e211f208a27fe52f587047140d9666bbeca6032eae604 localfile~ x64

**File Information**

├── 11aa6eeca2547fcf807129787bec0d576de1a29b56945c5a8fb16ed8bf68f782 localfile~ x64

└── Variants

├── 7a6c0b683961869fc159bf8da1b4c86bc190ee07b0ad5eb09f99deaac4db5c69 localfile~ x64

└──

Posted by
Mila

at
[12:42 PM](https://contagiodump.blogspot.com/2024/09/2024-08-14-osx-banshee-infostealer.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=6429876448303229306&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-08-23-angry-stealer-rage-stealer.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-08-22-peaklight-stealthy-memory.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/6429876448303229306/comments/default)

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
    -...