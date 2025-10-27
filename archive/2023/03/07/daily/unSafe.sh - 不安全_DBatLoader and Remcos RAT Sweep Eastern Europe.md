---
title: DBatLoader and Remcos RAT Sweep Eastern Europe
url: https://buaq.net/go-152239.html
source: unSafe.sh - 不安全
date: 2023-03-07
fetch_date: 2025-10-04T08:47:26.379835
---

# DBatLoader and Remcos RAT Sweep Eastern Europe

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

![](https://8aqnet.cdn.bcebos.com/5cab9a8ce443e5bda7ab79ef1d669e97.jpg)

DBatLoader and Remcos RAT Sweep Eastern Europe

SentinelOne has been observing phishing campaigns that distribute the Remcos RAT using the DBatLoad
*2023-3-6 21:33:10
Author: [www.sentinelone.com(查看原文)](/jump-152239.htm)
阅读量:21
收藏*

---

SentinelOne has been observing [phishing](https://www.sentinelone.com/blog/phishing-revealing-vulnerable-targets/) campaigns that distribute the Remcos RAT using the DBatLoader malware loader to target predominantly Eastern European institutions and businesses. In this blog post, we summarize our observations on these campaigns to equip defenders with the information they need to protect against this threat.

DBatLoader is characterized by the abuse of public Cloud [infrastructure](https://www.netskope.com/blog/dbatloader-abusing-discord-to-deliver-warzone-rat) to host its malware staging component. The feature-rich RAT Remcos is actively used by threat actors with cybercriminal and espionage motivations. Threat actors typically distribute the RAT through phishing emails and stage it on systems using a variety of forms and methods.

Examples include the use of the [TrickGate](https://research.checkpoint.com/2023/following-the-scent-of-trickgate-6-year-old-packer-used-to-deploy-the-most-wanted-malware/) loader stored in archive files, malicious [ISO](https://www.malwarebytes.com/blog/threat-intelligence/2022/20221121-threat-intel-report-final.pdf) [images](https://www.socinvestigation.com/remcos-rat-new-ttps-detection-response/), and URLs to [VBScript](https://perception-point.io/blog/behind-the-attack-remcos-rat/) scripts embedded in pictures. Further, the Ukrainian CERT has recently [issued](https://cert.gov.ua/article/3804703) [reports](https://cert.gov.ua/article/3931296) on Remcos RAT phishing campaigns targeting Ukrainian state institutions for espionage purposes using password-protected archives as email attachments.

This report compliments the available information about recent phishing campaigns that distribute Remcos by highlighting the way in which DBatLoader stages the RAT on infected systems.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/DBatLoader-and-Remcos-RAT-Sweep-Eastern-Europe-By-Aleksandar-Milenkoski.jpg)

## DBatLoader and Remcos Phishing Emails

The [phishing](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) emails distributing DBatLoader and Remcos have attachments in the form of `tar.lz` archives that typically masquerade as financial documents, such as invoices or tender documentation. To make the emails look credible, we observed the threat actors using a variety of techniques.

From the recipient’s perspective, the phishing emails originate from institutions or business organizations related to the target such that sending an invoice would be realistic. The emails are typically sent to the sales departments of the targets or their main contact email addresses as disclosed online.

We observed emails sent from what seems to be compromised private email accounts and accounts from public email services that are also used by the targets and the legitimate institutions or organizations which are supposedly sending the email.

Many of the phishing emails we observed have been sent from email accounts with top-level domains of the same country as where the target is based. These emails typically do not contain any text accompanying the malicious attachment or contain text written in the language of the target’s country. In the cases where the threat actors are not masquerading the phishing emails as originating from an institution or business organization local to the target, the emails contain text written in English.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/DBatLoader_and_Remcos_RAT_Sweep_Eastern_Europe_-_Google_Docs.png)

Example phishing email

## DBatLoader Staging Remcos RAT

The `tar.lz` archives attached to phishing emails contain DBatLoader executables. These pack Remcos and usually masquerade as Microsoft Office, LibreOffice, or PDF documents using double extensions and/or application icons.

When a user decompresses the attachment and runs the executable within, DBatLoader downloads and executes an obfuscated second-stage payload data from a public Cloud location. We observed download links to Microsoft OneDrive and Google Drive sites (under the drive.google.com and onedrive.live.com domains) with varying lifetime spans, the longest of which was more than one month.

The Cloud file storage locations that were active while we investigated contained only the second-stage DBatLoader payload data and were registered to individuals. We have no knowledge at this point whether the threat actors have been using self-registered and/or compromised Microsoft OneDrive and Google Drive credentials to host DBatLoader payload.

The malware then creates and executes an initial Windows batch script in the `%Public%\Libraries` directory. This script abuses a known [method](https://www.bleepingcomputer.com/news/security/bypassing-windows-10-uac-with-mock-folders-and-dll-hijacking/) for bypassing Windows [User Account Control](https://learn.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) that involves the creation of mock trusted directories, such as `%SystemRoot%\System32`, by using trailing spaces. This enables the attackers to conduct elevated activities without alerting users.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/DBatLoader_and_Remcos_RAT_Sweep_Eastern_Europe_-_Google_Docs-2.png)

An initial batch script

The script creates the mock `%SystemRoot%\System32` trusted directory by issuing requests directly to the file system – note the prepended `\\?\` to the directory names. It then copies into this directory a `KDECO.bat` batch script, the legitimate `easinvoker.exe` (Exchange ActiveSync Invoker) executable, and a malicious `netutils.dll` DLL file, which DBatLoader had previously dropped in the `%Public%\Libraries` directory. The script then executes the `easinvoker.exe` copy and deletes the mock directory.

When it comes to the `netutils.dll` DLL, `easinvoker.exe` is [susceptible](https://www.wietzebeukema.nl/blog/hijacking-dlls-in-windows) to DLL hijacking enabling the execution of the malicious `netutils.dll` in its context. `easinvoker.exe` is an auto-elevated executable, meaning that Windows automatically elevates this process without issuing an UAC prompt if located in a trusted directory – the mock `%SystemRoot%\System32` directory ensures this criteria is fulfilled.

`easinvoker.exe` loads the malicious `netutils.dll`, which executes the `KDECO.bat` script.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/DBatLoader_and_Remcos_RAT_Sweep_Eastern_Europe_-_Google_Docs-3.png)

`netutils.dll` executes `KDECO.bat`

As an anti-detection measure, `KDECO.bat` adds the `C:\Users` directory to the Microsoft Defender exclusion list to exclude the directory from scanning.

```
powershell -WindowStyle Hidden -inputformat none -outputformat none -NonInteractive -Command "Add-MpPreference -ExclusionPath 'C:\Users'"
```

DBatLoader establishes persistence across system reboots by copying itself in the `%Public%\Libraries` directory and creating an autorun registry key under `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`. This key points to an Internet Shortcut file that executes the DBatLoader executable in `%Public%\Libraries`, which in turn executes Remcos through process injection.

![](https://www.sentinelone.com/wp-content/upload...