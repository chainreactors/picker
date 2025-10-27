---
title: 2024-09-19 X-WORM RAT (Phishing) Samples
url: https://contagiodump.blogspot.com/2024/09/2024-09-19-x-worm-phishing-samples.html
source: contagio
date: 2024-09-14
fetch_date: 2025-10-06T18:30:17.622001
---

# 2024-09-19 X-WORM RAT (Phishing) Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Thursday, September 12, 2024

### [2024-09-19 X-WORM RAT (Phishing) Samples](https://contagiodump.blogspot.com/2024/09/2024-09-19-x-worm-phishing-samples.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1R5t2gfkcXaRAT7sAtqMTQ1hNsI_2BsBTSIan95zdE3YlhkTIynhLOowZlNyVRdZgw2RHUTUoC613_dc4HDEP7i4b-MdkdmHVy2LIwajLyDhOgT5WXiRYVxW0lrJfs-jp1h4gYnyr3nNp4KZJ_lnkGFmqvDnG9bWnrHKsiEY_l2WP3WcbgBiK6Kzlw6g/w273-h273/dumpstercity.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1R5t2gfkcXaRAT7sAtqMTQ1hNsI_2BsBTSIan95zdE3YlhkTIynhLOowZlNyVRdZgw2RHUTUoC613_dc4HDEP7i4b-MdkdmHVy2LIwajLyDhOgT5WXiRYVxW0lrJfs-jp1h4gYnyr3nNp4KZJ_lnkGFmqvDnG9bWnrHKsiEY_l2WP3WcbgBiK6Kzlw6g/s2048/dumpstercity.png)

[2024-09-12 0day in {REA\_TEAM}: The X-Worm malware is being spread through a phishing email](https://kienmanowar.wordpress.com/2024/09/12/quicknote-the-xworm-malware-is-being-spread-through-a-phishing-email/)
*by m4n0w4r*

More about X-Worm: [Malpedia: X-Worm Malware with wide range of capabilities ranging from RAT to ransomware.](https://malpedia.caad.fkie.fraunhofer.de/details/win.xworm)
> * Phishing Tactics: An attacker sent an email with a shortened link that, when clicked, triggered the download of a file named Itinerary.doc\_.zip.
> * The downloaded .zip file contained a shortcut file (.lnk).
> * This .lnk file was used to download and run a malicious batch script (output4.bat), which employed bitsadmin to download a harmful payload, disguised as svchost.com, into the %temp% folder.
> * The svchost.com file was analyzed using tools like DiE and ExeInfo, revealing it to be part of the XWorm malware family, protected by .NET Reactor.
> * The malware's code was heavily obfuscated but was partially deobfuscated using the NETReactorSlayer tool.
> * MD5 hashing, AES encryption in ECB mode, and Base64 decoding to decrypt strings.
> * The malware’s configuration included a host (cyberdon1[.]duckdns[.]org), port (1500), and other parameters like a Telegram token and chat ID.
> * XWorm Version: The analyzed version of XWorm was 5.6.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/crime/2024-09-12%2BXWORM%2BRAT%2Bphishing.zip)

**File Information**

├── 1893afc228afedb18b743176cbd3f0e4adb31fee7982252a4dc6180a6fb83451 ZBWWHQNZII.exe

├── ec7351c49098d55c332f9c5b0b4c51ffe804dd5780fc954006efcf2aeef91b7f HPFQJGRKIS.exe

├── ec7e0bf7036f03786789b6cb58d01c84733fc3a865974c79edf68cba25ff9891.Itinerary.doc.zip.exe

└── ec7e0bf7036f03786789b6cb58d01c84733fc3a865974c79edf68cba25ff9891 ZBWWHQNZII.exe

**Malware Repo Links**

Over the past 15 years, as the blog has been around, many hosting providers have dropped support due to stricter no-malware policies. This has led to broken links, especially in older posts. If you find a broken link on contagiodump.blogspot.com (or contagiominidump.blogspot.com), just note the file name from the URL and search for it in the [Contagio Malware Storage](https://s3.amazonaws.com/contagiomobile.deependresearch.org/categories.html).

Posted by
Mila

at
[8:33 PM](https://contagiodump.blogspot.com/2024/09/2024-09-19-x-worm-phishing-samples.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=664564916379467785&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-09-12-supershell-2023-03-13.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2023-11-23-beavertail-and.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/664564916379467785/comments/default)

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
    - [2024-09-05 SHRINKLOCKER (Bitlocker) Ransomware Sam...](https://contagiodump.blogspot.com/...