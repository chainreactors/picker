---
title: 2024-08-29 UNDERGROUND Ransomware Samples
url: https://contagiodump.blogspot.com/2024/09/2024-08-29-underground-ransomware.html
source: contagio
date: 2024-09-03
fetch_date: 2025-10-06T18:39:11.605862
---

# 2024-08-29 UNDERGROUND Ransomware Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Monday, September 2, 2024

### [2024-08-29 UNDERGROUND Ransomware Samples](https://contagiodump.blogspot.com/2024/09/2024-08-29-underground-ransomware.html)

[**2024-08-29 Fortinet Ransomware Roundup - Underground**](https://www.fortinet.com/blog/threat-research/ransomware-roundup-underground)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBzHSsJvdd93FoFBLqiUFUZp0NpFfgDetC_EE7baB95Rxql3e1jmjZjKUoBOvk2nVoNyZaPd_yKetzbVeoC0XwpdApeK2bhQstg9tDldPvIeFwzTrmvIUlDtKa7Yx3o967qFKdQQvbc_7IXYXONUV2fUuUA9O5QlFCAzHzNrSURhVhtnyQiN1DYV-SYNM/w289-h248/Google%20Chrome%202024-09-02%2013.01.33.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBzHSsJvdd93FoFBLqiUFUZp0NpFfgDetC_EE7baB95Rxql3e1jmjZjKUoBOvk2nVoNyZaPd_yKetzbVeoC0XwpdApeK2bhQstg9tDldPvIeFwzTrmvIUlDtKa7Yx3o967qFKdQQvbc_7IXYXONUV2fUuUA9O5QlFCAzHzNrSURhVhtnyQiN1DYV-SYNM/s874/Google%20Chrome%202024-09-02%2013.01.33.png)

The Underground ransomware is likely spread by the RomCom group (also known as Storm-0978). The group exploits the Microsoft Office and Windows HTML RCE vulnerability (CVE-2023-36884). Other methods, such as phishing emails and access via Initial Access Brokers (IABs), may also be used.

* + **Shadow Copies Deletion:** It removes all shadow copies to prevent file recovery:
  + bash
  + Copy code
  + vssadmin.exe delete shadows /all /quiet
  + **RDP Session Limits:** Sets a 14-day limit on Remote Desktop sessions to maintain persistence:
  + bash
  + Copy code
  + reg.exe add HKLM\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services / v MaxDisconnectionTime / t REG\_DWORD / d 1209600000 / f
  + **SQL Server Service Stop:** Halts the MS SQL Server service to disrupt operations:
  + bash
  + Copy code
  + net.exe stop MSSQLSERVER /f /m
  + **Ransom Note Deployment:** Drops a ransom note named “!!readme!!!.txt” in directories containing encrypted files.
* **File Encryption:** The ransomware encrypts files without altering their extensions, making it harder to visually identify encrypted files. It avoids encrypting critical system files (e.g., .sys, .exe, .dll) to maintain system functionality.
* **Log and File Deletion:** It creates and runs a script (temp.cmd) to delete the original ransomware file and clear Windows Event logs, complicating forensic analysis.
* **Data Leak Site:** The ransomware group maintains a site where they post stolen data from their victims, spanning industries such as construction, pharmaceuticals, and manufacturing. As of July 2024, they have listed 16 victims.
* **Telegram Channel:** The group also uses a Telegram channel to distribute stolen data, with links to files hosted on Mega, a cloud storage service.

**Download**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/Ransomware/2024-09_UNDERGROUND_Win_ransomware.zip)

File Information

├── 9d41b2f7c07110fb855c62b5e7e330a597860916599e73dd3505694fd1bbe163 enc getswin x64 exe

├── 9f702b94a86558df87de316611d9f1bfe99a6d8da9fa9b3d7bb125a12f9ad11f exe

├── cc80c74a3592374341324d607d877dcf564d326a1354f3f2a4af58030e716813 exe

├── d4a847fa9c4c7130a852a2e197b205493170a8b44426d9ec481fc4b285a92666 exe

└── eb8ed3b94fa978b27a02754d4f41ffc95ed95b9e62afb492015d0eb25f89956f exe

Posted by
Mila

at
[1:05 PM](https://contagiodump.blogspot.com/2024/09/2024-08-29-underground-ransomware.html "permanent link")

Tags:
[ransomware](https://contagiodump.blogspot.com/search/label/ransomware)

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=7670597244435446046&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-08-29-asyncrat-samples.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-08-23-angry-stealer-rage-stealer.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/7670597244435446046/comments/default)

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
    - [2024-09-10 KIMSUKY (North Korean APT) Sample (Saka...](https://contagiodump.blogspot.com/2024/09/2024-09-10-kimsuky-north-k...