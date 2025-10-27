---
title: 2024-09-03 LUXY Ransomware / Stealer Sample
url: https://contagiodump.blogspot.com/2024/09/2024-09-03-luxy-ransomware-stealer.html
source: contagio
date: 2024-09-12
fetch_date: 2025-10-06T18:42:06.513285
---

# 2024-09-03 LUXY Ransomware / Stealer Sample

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Tuesday, September 10, 2024

### [2024-09-03 LUXY Ransomware / Stealer Sample](https://contagiodump.blogspot.com/2024/09/2024-09-03-luxy-ransomware-stealer.html)

[2024-09-03 K7 Security Labs: Luxy: A Stealer and a Ransomware in one](https://labs.k7computing.com/index.php/luxy-a-stealer-and-a-ransomware-in-one/)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdnSgwGY_enjDokwDmro85ns8s3wRJsG7_xWIoc0MR8bHNlq8mqkJHH7DMTT0osBYWf3oeE83H9gss9JN4WosAM7KrYhEGXauEj2dEbNBOvb_Sc7_Mrky6aHFnnhmjznEm09OaSMsvib8VPn4M_Of6gx32nGkqZftl9Ox_pwY-irC6NfbjKEq25X9Y71c/w289-h272/Google%20Chrome%202024-09-10%2020.12.14.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdnSgwGY_enjDokwDmro85ns8s3wRJsG7_xWIoc0MR8bHNlq8mqkJHH7DMTT0osBYWf3oeE83H9gss9JN4WosAM7KrYhEGXauEj2dEbNBOvb_Sc7_Mrky6aHFnnhmjznEm09OaSMsvib8VPn4M_Of6gx32nGkqZftl9Ox_pwY-irC6NfbjKEq25X9Y71c/s383/Google%20Chrome%202024-09-10%2020.12.14.png)

* The sample is a .NET 32-bit executable, enforcing single-instance execution via a mutex and ensuring network connectivity before proceeding. It also implements anti-VM checks using System UUIDs, process names, and other system identifiers to evade sandbox environments.
* Browser Data Extraction: Utilizes methods like GETENCRYPTIONKEY to extract and decrypt stored passwords and cookies from various browsers.
* Cryptocurrency Wallet Theft: Targets wallets such as Zcash, Ethereum, and others, copying wallet files to a text file for exfiltration.
* Session File Theft: Extracts Minecraft session files, logging them in a source.txt file, potentially compromising user authentication.
* Roblox Cookie Theft: Steals cookies from the registry and browsers using PowerShell commands.
* File Encryption: Deploys AES256 encryption on all files in the malware execution path, renaming files post-encryption. The encryption method uses a 128-bit key and IV, padding the plaintext to meet AES block size requirements.
* Ransom Note: After encryption, a ransom note is dropped, informing the victim of the encryption and providing instructions to obtain the decryption key.

The Ransom note reads:

> > ATTENTION!
>
> > Don't worry, you can return all your files!
>
> > All your files like pictures, databases, documents and other important are encrypted with strongest encryption and unique key.
>
> > The only method of recovering files is to purchase decrypt tool and unique key for you.
>
> > This software will decrypt all your encrypted files.
>
> > Price of private key and decrypt software is $980.
>
> > Discount 50% available if you contact us first 72 hours, that's price for you is $490.
>
> > Please note that you'll never restore your data without payment.
>
> > To get this software and key you need join our server discord:
>
> > discord.gg/
>
> > Personal ID:

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/Ransomware/2024-09-03_LUXY_Ransomware.zip)

**File Information**

a2bc9b467f331a26b33cfd70f7bf12c9e2e6b3ebc8d3749c12a7eedf507e9323
09b5f5200e59d3a4623d739661ce9832

**Malware Repo Links**

Over the past 15 years, as the blog has been around, many hosting providers have dropped support due to stricter no-malware policies. This has led to broken links, especially in older posts. If you find a broken link on contagiodump.blogspot.com (or contagiominidump.blogspot.com), just note the file name from the URL and search for it in the [Contagio Malware Storage](https://s3.amazonaws.com/contagiomobile.deependresearch.org/categories.html).

Posted by
Mila

at
[8:14 PM](https://contagiodump.blogspot.com/2024/09/2024-09-03-luxy-ransomware-stealer.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=6213166242391332299&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-09-10-kimsuky-north-korean-apt.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-09-05-shrinklocker-bitlocker.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/6213166242391332299/comments/default)

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
    - [2023-11-23 BEAVERTAI...