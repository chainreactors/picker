---
title: 2024-09-10 KIMSUKY (North Korean APT) Sample (Sakai @sakaijjan - Terms and Conditions.msc)
url: https://contagiodump.blogspot.com/2024/09/2024-09-10-kimsuky-north-korean-apt.html
source: contagio
date: 2024-09-12
fetch_date: 2025-10-06T18:42:04.474233
---

# 2024-09-10 KIMSUKY (North Korean APT) Sample (Sakai @sakaijjan - Terms and Conditions.msc)

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Tuesday, September 10, 2024

### [2024-09-10 KIMSUKY (North Korean APT) Sample (Sakai @sakaijjan - Terms and Conditions.msc)](https://contagiodump.blogspot.com/2024/09/2024-09-10-kimsuky-north-korean-apt.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdTktkUStFFLLA1J14aCCW07O1j99VyVm-37vaTmGP3Orp3VJoazqEEE0-hzr8lZ4LEROs0paiN0srvSIctsRLL4g9iLQUnJk2ltOsMrufspHhgfUQpS1uslFyGg8gdwJRu5uEQ3StJKxCPeO3DPdFZ6eMVO_H6fS1nYHLFb9PTZjuGC5Tel4rJHL6Gck/w277-h269/Google%20Chrome%202024-09-10%2020.47.53.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdTktkUStFFLLA1J14aCCW07O1j99VyVm-37vaTmGP3Orp3VJoazqEEE0-hzr8lZ4LEROs0paiN0srvSIctsRLL4g9iLQUnJk2ltOsMrufspHhgfUQpS1uslFyGg8gdwJRu5uEQ3StJKxCPeO3DPdFZ6eMVO_H6fS1nYHLFb9PTZjuGC5Tel4rJHL6Gck/s486/Google%20Chrome%202024-09-10%2020.47.53.png)

 [2024-09-10 Sakai @sakaijjang 김수키(Kimsuky) 에서 만든 악성코드-Terms and conditions(이용 약관).msc(2024.9.6)](https://wezard4u.tistory.com/429275)   - Kimsuky (North Korea) - Terms and Conditions.msc

by<https://x.com/sakaijjang?lang=en>

[Article translation in English](https://s3.amazonaws.com/contagio.deependresearch.org/read/2024-09-10_sakaijjang_Kimsuky_TermsandConditions.pdf)

More about Kimsuky: 2020-10-27 CISA North Korean Advanced Persistent Threat Focus

* The malware is delivered as a file named "Terms and conditions.msc," containing embedded PowerShell commands.
* The PowerShell script is executed in a hidden window (-WindowStyle Hidden), preventing user awareness.
* The script uses Invoke-Expression (iex) to execute code and Invoke-WebRequest (iwr) to download a malicious script from hxxps://0x0(.)st/Xyl7(.)txt.
* The downloaded data, encoded in hexadecimal, is decoded into a byte array.
* The decoded data is initially saved as an MP3 file (e.g., vBqz.mp3) in the system’s public documents folder.
* The MP3 file is then renamed to an executable file (e.g., vBqz.exe), disguising the payload as a media file.
* The executable is run using conhost.exe in the background with the -NoNewWindow option, ensuring it remains hidden.
* File Camouflage: The use of the MP3 extension initially disguises the executable file.
* Stealthy Execution: Utilizing system utilities like conhost.exe and executing commands in hidden windows help evade user detection and security software.
* Command-and-Control (C2) Infrastructure: The malware’s reliance on a public site for payload distribution suggests a flexible and easily reconfigurable C2 mechanism.
* Hexadecimal Encoding: The use of encoded data indicates potential obfuscation techniques; decoding this data can reveal more about the malware.
* Potential Variants: Different versions of this malware may exist, with variations in the payload or C2 URLs. Monitoring and updating detection rules, such as YARA, would be beneficial.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/APT/NorthKorea/2024-09-10_KIMSUKY_Sample.zip)

**File Information**

Name: Terms and conditions.msc

Size: 141 KB

MD5: 81d224649328a61c899be9403d1de92d

SHA-1: f4895809cb38fa1f225340e99c05e477a5017111

SHA-256: cea22277e0d7fe38a3755bdb8baa9fe203bd54ad4d79c7068116f15a50711b09

**Malware Repo Links**

Over the past 15 years, as the blog has been around, many hosting providers have dropped support due to stricter no-malware policies. This has led to broken links, especially in older posts. If you find a broken link on contagiodump.blogspot.com (or contagiominidump.blogspot.com), just note the file name from the URL and search for it in the [Contagio Malware Storage](https://s3.amazonaws.com/contagiomobile.deependresearch.org/categories.html).

Posted by
Mila

at
[8:59 PM](https://contagiodump.blogspot.com/2024/09/2024-09-10-kimsuky-north-korean-apt.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=6700209502405408293&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2023-11-23-beavertail-and.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-09-03-luxy-ransomware-stealer.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/6700209502405408293/comments/default)

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
    - [2024-09-19 X-WORM RAT (Phishing) S...