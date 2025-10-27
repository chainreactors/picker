---
title: 2024-09-12 SUPERSHELL + 2023-03-13 SHELLBOT Targeting Linux SSH servers Samples
url: https://contagiodump.blogspot.com/2024/09/2024-09-12-supershell-2023-03-13.html
source: contagio
date: 2024-09-14
fetch_date: 2025-10-06T18:30:14.787068
---

# 2024-09-12 SUPERSHELL + 2023-03-13 SHELLBOT Targeting Linux SSH servers Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Thursday, September 12, 2024

### [2024-09-12 SUPERSHELL + 2023-03-13 SHELLBOT Targeting Linux SSH servers Samples](https://contagiodump.blogspot.com/2024/09/2024-09-12-supershell-2023-03-13.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfg6tGtXoQkxZ3dpFO4MMYJPpaE16CgzEZIbG9rzc5XXmZLVM9m6DnPx3fn32lzx-yiw9SvZ7uakTBzhkDf_CDDoeOci87Y1SIY7H4F2hRlCPahVHuIYqxH9UyX-XoVgOH-5xLb9Rd_Guk3asTD_8tPlqxTeZz33Y3ug4RF7Ej_0eidKguiX7ZCt-hGJA/w257-h266/Preview%202024-09-12%2021.07.42.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfg6tGtXoQkxZ3dpFO4MMYJPpaE16CgzEZIbG9rzc5XXmZLVM9m6DnPx3fn32lzx-yiw9SvZ7uakTBzhkDf_CDDoeOci87Y1SIY7H4F2hRlCPahVHuIYqxH9UyX-XoVgOH-5xLb9Rd_Guk3asTD_8tPlqxTeZz33Y3ug4RF7Ej_0eidKguiX7ZCt-hGJA/s965/Preview%202024-09-12%2021.07.42.png)

2024-09-12 Ahnlab: SuperShell malware targeting Linux SSH servers

* SuperShell is a sophisticated backdoor malware targeting Linux SSH servers, written in the Go language, which allows cross-platform functionality on Linux, Windows, and Android. Created by a Chinese-speaking developer, it operates as a reverse shell, enabling attackers to execute commands remotely on the compromised systems. The attack begins with brute force and dictionary attacks against SSH servers, using weak credentials like "root/password" and "root/123456qwerty." Once access is gained, attackers execute a series of commands to download and install SuperShell, leveraging tools like wget, curl, tftp, and FTP, with download sources often hosted on compromised servers.

* SuperShell's obfuscation adds complexity, but it can still be identified through specific internal strings and its runtime behavior. The malware's installation process is versatile, targeting directories like /tmp, /var/run, /mnt, and /root, with commands often including clean-up actions to remove traces post-installation (rm -r \*). Typically, the payload involves downloading a script or binary, which is then executed with elevated permissions using chmod +x followed by execution (./ssh1). This pattern is consistently observed across multiple commands, highlighting the malware's redundancy and persistence in ensuring successful deployment.
* Additionally, the attackers often deploy XMRig, a Monero cryptocurrency miner, alongside SuperShell, hinting at a dual-purpose attack: maintaining persistent control over the system while generating illicit cryptocurrency.

[2023-03-13 Ahnlab: ShellBot Malware Being Distributed to Linux SSH Servers](https://asec.ahnlab.com/en/49769/)

* On March 13, 2023, ASEC reported that ShellBot, a Perl-based DDoS bot, is actively targeting Linux SSH servers. The malware exploits weak SSH credentials through brute-force attacks, gaining access to deploy its payload. Once installed, ShellBot connects to a Command and Control (C&C) server via the IRC protocol, enabling attackers to issue commands, steal data, and launch DDoS attacks.
* Initial Access: Attackers scan for servers with open SSH ports (port 22) and use brute-force tools to guess weak or default credentials.
* Installation: After gaining access, ShellBot is deployed, often achieving persistence by modifying startup scripts or cron jobs.
* IRC Protocol: ShellBot uses the IRC protocol for C&C communication, allowing it to receive commands like executing remote tasks or launching DDoS attacks without needing a custom C&C infrastructure.
* Customization: ShellBot is highly customizable, with variants like "LiGhT’s Modded perlbot v2" offering different capabilities and attack methods tailored by various threat actors.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme.](https://s3.amazonaws.com/contagio.deependresearch.org/crime/2024-09-12%2B_%2B2023-03-13%2B%2BSUPERSHELL%2B%2B%2BSHELLBOT%2BLinux.zip)

**File Information**

* **├── SHELLBOT**
* │   ├── 2220783661db230d0808a5750060950688e2618d462ccbe07f54408154c227c1 .pl
* │   ├── b7d62d1a145ddda241e624ef94ab31fcca1a13f79e130d0a704586e35745282a .pl
* │   ├── e476b9c07fcd80824d4eafce0e826ae1c12706ca6215eb6e3995468374bb8a76 .pl
* │   └── f5a26a68344c1ffd136ba73dec9d08f61212872cdba33bd4d7d32733a72e4ed5 .pl
* │   ├── Other Shellbot samples
* │   │   ├── 0857f90be97326ff45f17ec3f6ce60d9a0f6d8faed34e48527fde5ec30bd5a0d
* │   │   ├── 0c1673e442b945a0aecf60d3970e924b16bd72d46e257bd72927821e4ebbc9ca
* │   │   ├── 1f3c279ea684d5cbdc7004819bf15a160f70b2c79c4affd309f9ab3ad957045b
* │   │   ├── 5ba1d0efb313ccc20e3d5f2476a3db811e15c80c3f1ac73b7a02d80c5c49c728
* │   │   ├── a26de5b607e3a66af8b7db2c13bcd1c658817649c699f8731db6f237c3c5b1ce
* │   │   └── cb80570332e3e32037f426e835d05bdcd276e9e5acfd439027d788dd64dcb47d
* **└── SUPERSHELL**
* ├── 157bea84012ca8b8dc6c0eabf80db1f0256eafccf4047d3e4e90c50ed42e69ff ssh1.sh
* ├── 23dbfb99fc6c4fcfc279100c4b6481a7fd3f0b061b8d915604efa2ba37c8ddfa setup c3pool miner.sh
* └── cf5a7b7c71564a5eef77cc5297b9ffd6cd021eb44c0901ea3957cb2397b43e15 ssh1

**Malware Repo Links**

Over the past 15 years, as the blog has been around, many hosting providers have dropped support due to stricter no-malware policies. This has led to broken links, especially in older posts. If you find a broken link on contagiodump.blogspot.com (or contagiominidump.blogspot.com), just note the file name from the URL and search for it in the [Contagio Malware Storage](https://s3.amazonaws.com/contagiomobile.deependresearch.org/categories.html).

Posted by
Mila

at
[9:10 PM](https://contagiodump.blogspot.com/2024/09/2024-09-12-supershell-2023-03-13.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=7885177434994542510&postID=6209990081386172403&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

[Newer Post](https://contagiodump.blogspot.com/2024/09/2024-08-18-raptor-train-nosedive-mirai.html "Newer Post")

[Older Post](https://contagiodump.blogspot.com/2024/09/2024-09-19-x-worm-phishing-samples.html "Older Post")
[Home](https://contagiodump.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://contagiodump.blogspot.com/feeds/6209990081386172403/comments/default)

[Home](http://contagiodump.blogspot.com/)

## Shared by

[Mila](https://www.blogger.com/profile/09472209631979859691)

[View my complete profile](https://www.blogger.com/profile/09472209631979859691)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQQ9CtYxjXxYmJEJrS45nRw7TUYzsz2hcu6zvZnjwA2rbA_BZoSLQsPHHlGrZG1ArdPgFtHEOhNDHhH6A2lTR32GNPWlZWBTDFfkRgOB33dXbRM3nTCTay0WRmQ6kJdKzXE-JNPHC6qqQ/s1600/%25D0%2596%25D0%25AE%25D0%259723_filtered+%2528Custom%2529.jpg)

## About contagio

Contagio is a collection of the historic malware samples, threats, observations, and analyses.

![No Putler](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieKJB9iR6r5eAoodbA436bn8bvNdqGGqtMdUxeCz8BQ2OUkOqMPPjigFgbuG9J0Q4VTraqwm4uT-fZ--Fcbswum1s2H7F6-lmZN2oqT51VHA6NziTxCaIfNCaXBAQQ80BvDJT1zNHONhsTaKRI_AjnYg6kORfoAlunUylRHoWiapLkUxBSeoa-rTzY/s618/NoPutler.png)

Malware samples are available for download by any responsible whitehat researcher.

By downloading the samples, anyone waives all rights to claim pu...