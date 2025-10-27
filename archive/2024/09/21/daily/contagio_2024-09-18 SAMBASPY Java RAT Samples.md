---
title: 2024-09-18 SAMBASPY Java RAT Samples
url: https://contagiodump.blogspot.com/2024/09/2024-09-18-sambaspy-java-rat-samples.html
source: contagio
date: 2024-09-21
fetch_date: 2025-10-06T18:31:41.737447
---

# 2024-09-18 SAMBASPY Java RAT Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Thursday, September 19, 2024

### [2024-09-18 SAMBASPY Java RAT Samples](https://contagiodump.blogspot.com/2024/09/2024-09-18-sambaspy-java-rat-samples.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQZs6zX4boYVqCQxP361E9LDSDAqKiURBk9JTm-Fr_vf0bYIGOD7eB8bEh5P6yOtahGsOg0qCk19oVO9IQUybcHlfxwRUqeM37R2UuWKRjZKkYmek6bmMRrcl9dTbb_iA-M05z4Y81CU5ILOgqVTdBTOR7AT0Pa0Gg_OBUiFe5VIASAVqogpOijpND4Hs/w247-h237/Discord%202024-09-19%2021.58.33.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQZs6zX4boYVqCQxP361E9LDSDAqKiURBk9JTm-Fr_vf0bYIGOD7eB8bEh5P6yOtahGsOg0qCk19oVO9IQUybcHlfxwRUqeM37R2UuWKRjZKkYmek6bmMRrcl9dTbb_iA-M05z4Y81CU5ILOgqVTdBTOR7AT0Pa0Gg_OBUiFe5VIASAVqogpOijpND4Hs/s388/Discord%202024-09-19%2021.58.33.png)

[**2024-09-19 Kaspersky: Exotic SambaSpy is now dancing with Italian users**](https://securelist.com/sambaspy-rat-targets-italian-users/113851/)

SambaSpy  is a highly obfuscated Java-based RAT, protected by the Zelix KlassMaster protector. It supports a range of malicious activities, including:

* **File system and process management**
* **Keystroke logging** using the JNativeHook library, sending keystrokes to the C2 upon key release
* **Clipboard content control** through Java Abstract Window native libraries
* **Webcam access and remote desktop control** using the Java Robot and GraphicsDevice classes
* **Browser credential theft**, targeting Chrome, Edge, Brave, Opera, and others
* **Remote shell access** and the ability to load additional plugins dynamically via URLClassLoader, using `addURL()` to invoke downloaded plugins.

SambaSpy exhibits heavy obfuscation to evade detection, with encrypted strings and obfuscated class names and methods. The malware performs detailed environment checks to avoid execution in virtualized or sandbox environments, exiting immediately if the language is not set to Italian. It also encrypts its communications with the C2, complicating analysis.

Some malicious websites contain comments in Brazilian Portuguese, hinting at a possible connection to Brazil. The attackers repeatedly use second-level domains with new subdomains, allowing them to maintain control while shifting operations to evade detection.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/crime/2024-09-19%2BSAMBASPY%2BJava%2BRAT%2BSamples.zip)

**File Information**

* ├── 43f86b6d3300050f8cc0fa83948fbc92fc69af546f1f215313bad2e2a040c0fa DOCUMENTO pdf
* ├── 49bbfac69ca7633414172ec07e996d0dabd3f7811f134eecafe89acb8d55b93a jar Dropper
* ├── 9948b75391069f635189c5c5e24c7fafd88490901b204bcd4075f72ece5ec265 jpg jar Sambaspy
* ├── SAMBASPY - additional samples
* │   ├── 23fcf754156e84559d5640c0fc5f24d536332c3be516202086223528e2b45956  fMBFwZaxLTVpj
* │   ├── 6e059b017198c588cc5a39e608ca0034438dab953772ed7cd196a1aab1415b63  file jar
* │   ├── 8025e6b88d96cf77672bb0eed783808778b52074d686fe1f51076ffadae44749 jar
* │   ├── 8a4fce944f129b1f7bd36ba0076af5a37cd54c45644b155073cbd8a27b6430e8 FACTURE jar
* │   ├── 8e0c5271cc354d6a9f81f1d09472d8b88209b7afca85358e2c7e034ce0bbec37 daisynuke jar
* │   ├── 9530d49197932cc7f169dae3f953e00dc9cf3625eb74e0e335701d3e3fd8c8d4 Prodotto png
* │   ├── 9d7fc389f5c0793a5282da241999069c6e8b09a30efcaace36e76416556c3bbb jar
* │   ├── b1a61e5a54a61e8dc5feac75023120c29541c1597d82ea689d6246163cd98d75 ElxoxoYytt11893183509316623887 tmp
* │   ├── bc7d491a4a88b7c214c679433647c92bc5001741672bcfb96574d9b977d8121c Factuur - 2024108393 pdf jar
* │   ├── c0e73cc26a16a477e6de5e26ea1a61d3504fae6f77a278ae96f621a34405bdc9  aq jar
* │   ├── cc7632a505300c65c46bc3a0badaaa6b6a99abe148038ecf380ea04eaa6bc14c  client jar
* │   ├── dbaca1975b39161944950812b54c27ed62251a469f8dce82a743d246a6706968 FACTURE jar
* │   ├── e16f1a38e8ebe14b2243ab62dfcc0596c227987cc6d83b55ef58a046a9fbb2d2 celka jar
* │   ├── e3578b593437dd7edf5d8a575ad1b05131a067b78e07e1a4677dd5747bdcd056 Imagem jpg jar
* │   ├── e8cee7472d4d0816da9398e7b49fe742865dd7b629131d120ef3181e3f0849f2 newRat jar
* │   └── f820670f83310b4d6bb4683ebe140e06449fa40f385dda138c27fa6c47080878 jar
* └── d3effd483815a7de1e1288ab6f4fb673b44a129386ef461466472e22140d47f8  zip Downloader

**Malware Repo Links**

Over the past 15 years, as the blog has been around, many hosting providers have dropped support due to stricter no-malware policies. This has led to broken links, especially in older posts. If you find a broken link on contagiodump.blogspot.com (or contagiominidump.blogspot.com), just note the file name from the URL and search for it in the [Contagio Malware Storage](https://s3.amazonaws.com/contagiomobile.deependresearch.org/categories.html).

Posted by
Mila

at
[10:07 PM](https://contagiodump.blogspot.com/2024/09/2024-09-18-sambaspy-java-rat-samples.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=5289752234754575714&from=pencil "Edit Post")

#### 2 comments:

1. ![](//resources.blogblog.com/img/blank.gif)

   Anonymous[September 20, 2024 at 3:29 AM](https://contagiodump.blogspot.com/2024/09/2024-09-18-sambaspy-java-rat-samples.html?showComment=1726817362744#c698060307179111949)

   password

   Reply[Delete](https://www.blogger.com/comment/delete/7885177434994542510/698060307179111949)

   Replies

   Reply
2. ![](//resources.blogblog.com/img/blank.gif)

   Anonymous[September 20, 2024 at 9:48 PM](https://contagiodump.blogspot.com/2024/09/2024-09-18-sambaspy-java-rat-samples.html?showComment=1726883295692#c1425195420383222509)

   how can mail for you ? Pls give me your mail, tks u

   Reply[Delete](https://www.blogger.com/comment/delete/7885177434994542510/1425195420383222509)

   Replies

   Reply

Add comment

Load more...

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-09-19-unc1860-iran-apt-temple-of.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-09-18-earth-baxia-apt-ripcoy.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/5289752234754575714/comments/default)

[Home](http://contagiodump.blogspot.com/)

## Shared by

[Mila](https://www.blogger.com/profile/09472209631979859691)

[View my complete profile](https://www.blogger.com/profile/09472209631979859691)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQQ9CtYxjXxYmJEJrS45nRw7TUYzsz2hcu6zvZnjwA2rbA_BZoSLQsPHHlGrZG1ArdPgFtHEOhNDHhH6A2lTR32GNPWlZWBTDFfkRgOB33dXbRM3nTCTay0WRmQ6kJdKzXE-JNPHC6qqQ/s1600/%25D0%2596%25D0%25AE%25D0%259723_filtered+%2528Custom%2529.jpg)

## About contagio

Contagio is a collection of the historic malware samples, threats, observations, and analyses.

![No Putler](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieKJB9iR6r5eAoodbA436bn8bvNdqGGqtMdUxeCz8BQ2OUkOqMPPjigFgbuG9J0Q4VTraqwm4uT-fZ--Fcbswum1s2H7F6-lmZN2oqT51VHA6NziTxCaIfNCaXBAQQ80BvDJT1zNHONhsTaKRI_AjnYg6kORfoAlunUylRHoWiapLkUxBSeoa-rTzY/s618/NoPutler.png)

Malware samples are available for download by any responsible whitehat researcher.

By download...