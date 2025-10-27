---
title: CMLoot - Find Interesting Files Stored On (System Center) Configuration Manager (SCCM/CM) SMB Shares
url: https://buaq.net/go-156580.html
source: unSafe.sh - 不安全
date: 2023-04-03
fetch_date: 2025-10-04T11:29:42.399078
---

# CMLoot - Find Interesting Files Stored On (System Center) Configuration Manager (SCCM/CM) SMB Shares

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

CMLoot - Find Interesting Files Stored On (System Center) Configuration Manager (SCCM/CM) SMB Shares

CMLoot was created to easily find interesting files stored on System Center Configuration Ma
*2023-4-2 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-156580.htm)
阅读量:30
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhFSLaLAZqe89F2iVkjmBZbsBb6vYzgjyJxBb1LxZegDE0kl49MC1i_IOjsm7vLQhPHVFBHDIYES9-Ik_cIzqYdTJEPM4tu5k4SjvnGG8PiBdcxTPWpV8kwg41QNLffDqVKV7io6G0g8hFliIBV5LGNoqgwdPmReofbqkEnIptq9gaBtDy12MZofIHvCw=w640-h320)](https://blogger.googleusercontent.com/img/a/AVvXsEhFSLaLAZqe89F2iVkjmBZbsBb6vYzgjyJxBb1LxZegDE0kl49MC1i_IOjsm7vLQhPHVFBHDIYES9-Ik_cIzqYdTJEPM4tu5k4SjvnGG8PiBdcxTPWpV8kwg41QNLffDqVKV7io6G0g8hFliIBV5LGNoqgwdPmReofbqkEnIptq9gaBtDy12MZofIHvCw)

CMLoot was created to easily find interesting files stored on System Center Configuration Manager (SCCM/CM) SMB shares. The shares are used for distributing software to Windows clients in Windows enterprise environments and can contains scripts/configuration files with passwords, [certificates](https://www.kitploit.com/search/label/Certificates "certificates") (pfx), etc. Most SCCM deployments are configured to allow all users to read the files on the shares, sometimes it is limited to computer accounts.

The Content Library of SCCM/CM have a "complex" (annoying) file structure which CMLoot will untangle for you: [https://techcommunity.microsoft.com/t5/configuration-manager-archive/understanding-the-configuration-manager-content-library/ba-p/273349](https://techcommunity.microsoft.com/t5/configuration-manager-archive/understanding-the-configuration-manager-content-library/ba-p/273349 "https://techcommunity.microsoft.com/t5/configuration-manager-archive/understanding-the-configuration-manager-content-library/ba-p/273349")

Essentially the DataLib folder contains .INI files, the .INI file are named the original filename + .INI. The .INI file contains a hash of the file, and the file itself is stored in the FileLib in format of <folder name: 4 first chars of the hash>\fullhash.

### CM Access Accounts

It is possible to apply Access control to packages in CM. This however only protects the folder for the file descriptor (DataLib), not the actual file itself. CMLoot will during inventory record any package that it can't access (Access denied) to the file \_noaccess.txt. Invoke-CMLootHunt can then use this file to enumerate the actual files that the access control is trying to protect.

### OPSEC

Windows [Defender](https://www.kitploit.com/search/label/Defender "Defender") for Endpoint (EDR) or other security mechanisms might trigger because the script parses a lot of files over SMB.

### HOWTO

Find CM servers by searching for them in [Active Directory](https://www.kitploit.com/search/label/Active%20Directory "Active Directory") or by fetching this reqistry key on a workstation with System Center installed:

```
(Get-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\SMS\DP -Name ManagementPoints).ManagementPoints
```

There may be multiple CM servers deployed and they can contain different files so be sure to find all of them.

Then you need to create an inventory file which is just a text file containing references to file descriptors (.INI). The following command will parse all .INI files on the SCCM server to create a list of files available.

```
PS> Invoke-CMLootInventory -SCCMHost sccm01.domain.local -Outfile sccmfiles.txt
```

Then use the inventory file created above to download files of interest:

Select files using GridView (Milage may vary with large inventory files):

```
PS> Invoke-CMLootDownload -InventoryFile .\sccmfiles.txt -GridSelect
```

Download a single file, by coping a line in the inventory text:

```
PS> Invoke-CMLootDownload -SingleFile \\sccm\SCCMContentLib$\DataLib\SC100001.1\x86\MigApp.xml
```

Download all files with a certain file extension:

```
PS> Invoke-CMLootDownload -InventoryFile .\sccmfiles.txt -Extension ps1
```

Files will by default download to CMLootOut in the folder from which you execute the script, can be changed with -OutFolder parameter. Files are saved in the format of (folder: filext)\(first 4 chars of hash>\_original filename).

Hunt for files that CMLootInventory found inaccessible:

```
Invoke-CMLootHunt -SCCMHost sccm -NoAccessFile sccmfiles_noaccess.txt
```

Bulk extract MSI files:

```
Invoke-CMLootExtract -Path .\CMLootOut\msi
```

### DEMO

Run inventory, [scanning](https://www.kitploit.com/search/label/Scanning "scanning") available files: [![](https://blogger.googleusercontent.com/img/a/AVvXsEhFSLaLAZqe89F2iVkjmBZbsBb6vYzgjyJxBb1LxZegDE0kl49MC1i_IOjsm7vLQhPHVFBHDIYES9-Ik_cIzqYdTJEPM4tu5k4SjvnGG8PiBdcxTPWpV8kwg41QNLffDqVKV7io6G0g8hFliIBV5LGNoqgwdPmReofbqkEnIptq9gaBtDy12MZofIHvCw=w640-h320)](https://blogger.googleusercontent.com/img/a/AVvXsEhFSLaLAZqe89F2iVkjmBZbsBb6vYzgjyJxBb1LxZegDE0kl49MC1i_IOjsm7vLQhPHVFBHDIYES9-Ik_cIzqYdTJEPM4tu5k4SjvnGG8PiBdcxTPWpV8kwg41QNLffDqVKV7io6G0g8hFliIBV5LGNoqgwdPmReofbqkEnIptq9gaBtDy12MZofIHvCw)

Select files using GridSelect: [![](https://blogger.googleusercontent.com/img/a/AVvXsEjKB3zCMsTGk55AROP0t42_v424gr9LgmFd6L0T6HuYuAjSNIXhq2tLeCboRBx7jJueLFy3Th8H0Lz8PHWpPeBLofsymchTr_1dG88m-SSSeyf60fFkGwtFHbP1TZzUBaH_ayrjUcunRnisuMROh85d92tULCS-F6GBUg1A79BJ35VPAiJyofFem_MtZg=w640-h348)](https://blogger.googleusercontent.com/img/a/AVvXsEjKB3zCMsTGk55AROP0t42_v424gr9LgmFd6L0T6HuYuAjSNIXhq2tLeCboRBx7jJueLFy3Th8H0Lz8PHWpPeBLofsymchTr_1dG88m-SSSeyf60fFkGwtFHbP1TZzUBaH_ayrjUcunRnisuMROh85d92tULCS-F6GBUg1A79BJ35VPAiJyofFem_MtZg)

Download all extensions: [![](https://blogger.googleusercontent.com/img/a/AVvXsEixM9Uxm0fnebQ7LjpnntAyXSsmOMjCReu6bMeUHdRoZjOzmtdDGqJSKvlLB0hM7Qj_qFYA_lhyg5_kKNzV48O79lywvgA4Ecl8pFuQPFmrZuu7Eopv65sKIzpRtORTzpp9ZnyBp1Kk8b1ceN0h8jGuCUAdiCj9bCxJD0mdDrQXe0eVh05gGjgg0ImMaA=w640-h320)](https://blogger.googleusercontent.com/img/a/AVvXsEixM9Uxm0fnebQ7LjpnntAyXSsmOMjCReu6bMeUHdRoZjOzmtdDGqJSKvlLB0hM7Qj_qFYA_lhyg5_kKNzV48O79lywvgA4Ecl8pFuQPFmrZuu7Eopv65sKIzpRtORTzpp9ZnyBp1Kk8b1ceN0h8jGuCUAdiCj9bCxJD0mdDrQXe0eVh05gGjgg0ImMaA)

Hunt "inaccessible" files and MSI extract: [![](https://blogger.googleusercontent.com/img/a/AVvXsEiTo1u7OSDhck1uNS8tNuVnlJqSyFqEagAHGQyO-ngCbdjyFJQOxkOfFVPY3EUVo8CU-kLTWV99uNINw5kmUG9y5ejw8oqapmipglnyQYS4DAryAlwt2if5t77Horov2nvXtRYV8WWoZP8iA0zHEK1z6lRDIuDt96ZcDPPOQEFGYZh5V0u_3_FQZnHDKg=w640-h342)](https://blogger.googleusercontent.com/img/a/AVvXsEiTo1u7OSDhck1uNS8tNuVnlJqSyFqEagAHGQyO-ngCbdjyFJQOxkOfFVPY3EUVo8CU-kLTWV99uNINw5kmUG9y5ejw8oqapmipglnyQYS4DAryAlwt2if5t77Horov2nvXtRYV8WWoZP8iA0zHEK1z6lRDIuDt96ZcDPPOQEFGYZh5V0u_3_FQZnHDKg)

### Author

Tomas Rzepka / WithSecure

CMLoot - Find Interesting Files Stored On (System Center) Configuration Manager (SCCM/CM) SMB Shares
![CMLoot - Find Interesting Files Stored On (System Center) Configuration Manager (SCCM/CM) SMB Shares](https://blogger.googleusercontent.com/img/a/AVvXsEhFSLaLAZqe89F2iVkjmBZbsBb6vYzgjyJxBb1LxZegDE0kl49MC1i_IOjsm7vLQhPHVFBHDIYES9-Ik_cIzqYdTJEPM4tu5k4SjvnGG8PiBdcxTPWpV8kwg41QNLffDqVKV7io6G0g8hFliIBV5LGNoqgwdPmReofbqkEnIptq9gaBtDy12MZofIHvCw=s72-w640-c-h320)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/04/cmloot-find-interesting-files-stored-on.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)