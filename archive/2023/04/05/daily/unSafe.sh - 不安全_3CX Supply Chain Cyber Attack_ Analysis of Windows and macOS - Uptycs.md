---
title: 3CX Supply Chain Cyber Attack: Analysis of Windows and macOS - Uptycs
url: https://buaq.net/go-157023.html
source: unSafe.sh - 不安全
date: 2023-04-05
fetch_date: 2025-10-04T11:29:14.842621
---

# 3CX Supply Chain Cyber Attack: Analysis of Windows and macOS - Uptycs

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

![](https://8aqnet.cdn.bcebos.com/f9d1d0823d5b7fca5ddaa5b609eb4a81.jpg)

3CX Supply Chain Cyber Attack: Analysis of Windows and macOS - Uptycs

Research by: Tejaswini Sandapolla, Pratik Jeware and Karthickkumar KSupply chain attacks ha
*2023-4-4 23:39:1
Author: [www.uptycs.com(查看原文)](/jump-157023.htm)
阅读量:36
收藏*

---

*Research by: Tejaswini Sandapolla, Pratik Jeware and Karthickkumar K*

Supply chain attacks have increased in recent years. A watershed incident occurred in [December 2020](https://www.google.com/url?q=https://www.uptycs.com/blog/detecting-the-solarwinds-supply-chain-attack-using-osquery-and-uptycs&sa=D&source=docs&ust=1680617054040333&usg=AOvVaw0oyPwGTku3F5Tvh1r3m9tx) when SolarWinds customers were infiltrated through malicious code snuck into the software. The 3CX desktop apps for Windows and macOS—used for voice and video conferencing—are the targets of a recent similar attack that affected millions of users worldwide.

In this attack the threat actor employed a [DLL side-loading](https://attack.mitre.org/techniques/T1574/002/) technique to target the legitimate 3CXDesktopApp signed binary. The attack [has been observed](https://www.reddit.com/r/crowdstrike/comments/125r3uu/20230329_situational_awareness_crowdstrike/) on Windows and macOS systems.

The attackers use the DLL side-loading method to execute malicious code and to evade detection mechanisms. This technique involves loading a malicious DLL file through a legitimate process, allowing the attacker to bypass security measures and execute their code. This technique is a popular tactic among advanced threat actors and poses a significant risk to organizations if not properly addressed.

This article will examine how the attacker infected both Windows and macOS operating systems using dynamic linked libraries (DLL/Dylib). For Uptycs customers, we list hunting queries and YARA rules to inventory affected systems and identify historical activity at the bottom of this post.

## **Windows Platform**

### Infection Flow

Figure 1 below illustrates the malicious operation on the Windows platform.

![3CX Supply Chain Cyber Attack: Infection flow on Windows](https://lh6.googleusercontent.com/pDkHcMeRrLA9KC9w9Gh3-JIqeVM5PEsi77UqlsbywW_Pbizxn7W3LEEYU8BHB8LBssP41Gbf_111C-CLO7nMWz86oLsXGCeSPYCwYSLkcWLnTSCWnWq43FbrrnKzBckyvBuyoF3UYr-ltVMDqgeHnxw)

*Figure 1: Infection flow on Windows*

### Technical Analysis

Once the user executes the 3CXDesktopApp MSI file installer it will begin to install all the associated files on the targeted machine in the directory C:\Users\<username>\AppData\Local\Programs\3CXDesktopApp, as shown in Figure 2.

![3CX Supply Chain Cyber Attack: Installed location of MSI execution](https://lh5.googleusercontent.com/zCZlreI3CO9dskty9QezEghKx9yrkuc0gE5GVEb3xq10Yj4L75O4aNKpHpyFXparYJ8trRN0p2ETjBPfnb6fheBu2zTs3AnMxfVj5F9hQYl6SG8yn-JGZ_mayx09JamqDnpJ9e52Y2m6fSh2jqw8dEY)

*Figure 2: Installed location of MSI execution*

The folder named "app" contains the malicious DLLs as shown in Figure 3.

![3CX Supply Chain Cyber Attack: Folder with malicious DLLs](https://lh6.googleusercontent.com/tLK9xp5JG9wU24E-H0HIO3Y9gsblnKjefOudBRC2Nw-fLtZhnVrbxP4gNZJrv42yrVgo7RD2cIMwe1vqtQW3MCmEa0hmzRu6xbdEdxVpttghQyhXSxO_IGzXFGok86IlTVykmM5Y2JTbYBDdS6AxJcc)

*Figure 3: Folder with malicious DLLs*

When the file named "3CXDesktopApp.exe" is executed, it first loads a malicious file called "ffmpeg.dll". This DLL file contains an RC4 key and decryption loop. Then, it loads a second malicious DLL file named "d3dcompiler\_47.dll", which contains encrypted data.

The attacker then uses the RC4 algorithm to decrypt the data from the "d3dcompiler\_47.dll" file. This results in the retrieval of a shellcode and a binary called "Payload1".

![3CX Supply Chain Cyber Attack: RC4 algorithm used to decrypt data from the DLL](https://lh3.googleusercontent.com/5nPvL1IM8dTPPzQ5X0X0EmMEeEzfd3EDxTakFbmi4tareV7IahcYNT6Ezy6tupgg7DaViIV755RYhn_6nnsbvs-3veSDOBzs6RO5znI-0PMaEWYX2-6xVhaqWZ80bszjC4EhQTvA1iQIJdVUYGSVKhM)

*Figure 4: RC4 algorithm used to decrypt data from the DLL*

### Payload1

The DLL binary is a 64-bit file with a single export function name “DllGetClassObject”.

#### System information

The attacker obtains the [MachineGuid by using the RegQueryValueExA](https://attack.mitre.org/techniques/T1012/) function and examining the registry path SOFTWARE\Microsoft\Cryptography.

![3CX Supply Chain Cyber Attack: Gathering MachineGuid](https://lh6.googleusercontent.com/KWQ8dJq7c-5Gcmgik-M87IghpRWc8yYdJTxE5ew03HcAInHj23_a-OAUQWXU-OmnPgyRJ4Pvp_hJuJqwrvve11VNauTz-vV0GDtlg88ONT1QC8RB0BEML6hQPP1ZkRLguoDIlUufhmJ-r_yp7SEmljs)

*Figure 5: Gathering MachineGuid*

Payload1 is designed to download an icon file from a Git project.

![3CX Supply Chain Cyber Attack: Payload1 is designed to download an icon file from a Git project. Here is a download request](https://lh4.googleusercontent.com/ct89cYzXOirD1fKDopWouwQYvMpk8rDribQKnlXxcae7CyV825aBg8EjP4YLv-CZIsW7XZzJbGeEwgvhAAlkOcHyeZWwkfW7bVRwAheLneZ0az_8WraDTE4ZkfGDXsRxQjNdJ802ktd2ajGXb7sv-2g)

*Figure 6: Download request*

At the time of analysis, the GitHub files were no longer available on Git. However, we were able to obtain the icon file from open-source. Upon examining the icon file, it was discovered that the attacker had appended base64-encoded and AES-GCM encrypted data at the end of the downloaded icon image. This appended data after decryption might connect to a C2 domain which would further download payload2.

![3CX Supply Chain Cyber Attack: appended data after decryption might connect to a C2 domain which would further download payload2 - note the icon at the end in this image](https://lh5.googleusercontent.com/5pJrtXWgDIug1Rcu4DOqlJwUEr2PpfzgZi9-gryWZnL1ba_k7_U9sRFNhucEg8pS-LmOkawnR6tAw-nc1FgLpUhTv1wJt0mxIrMVHXsCgsXP8g5YnbBXRWTFKVjdvp3ITZIkB_ObIv2VfuaJz7ErneU)

*Figure 7: Icon image at the end*

### Payload2

We also investigated the subsequent payload (payload2). This payload is a 64-bit DLL binary file that contains only one export function named "DllGetClassObject".

It has been designed to retrieve the HostName, DomainName, and OS version information from the victim's machine using the NetWkstaGetInfo() and RtlGetVersion() Windows APIs.

![3CX Supply Chain Cyber Attack: Payload2 grabbing system information](https://lh4.googleusercontent.com/0s7CcwnnNoFofT4P9L-dVaW1A32TfNsx5fWQw89hsxlf3YhsIgpoche-33WAaFP26RhYsTjKhVPRz2ADuCCQ-NNnoiYhXIzVUG46YUb8AjvQJMRx_GiE3cOkwDpsmdnNf_js_ELeKyOfXZgbzCDVk-U)

*Figure 8: Grabbed system information*

The stealer has been observed targeting popular web browsers such as Chrome, Microsoft Edge, Brave, and Firefox with the goal of extracting sensitive data from the victim's browsing history and the “places.sqlite” database.

In order to achieve this, the stealer runs a specific query to retrieve the latest 500 browsing details from the victim's machine. All the collected information is shared with the attacker server.

SQL query:

SELECT url, title FROM urls ORDER BY id DESC LIMIT 500

SELECT url, title FROM moz\_places ORDER BY id DESC LIMIT 500

![3CX Supply Chain Cyber Attack: The stealer extracting sensitive data from the victim's browsing history and from the “places.sqlite” database. View of it reading browser information](https://lh3.googleusercontent.com/M9SDouCFsa_bqEGbUAGUA8vpdyaFa0aN7oLL4aEmBa8H1N4AN7aQ9b7mvQj0KlvJ4B_APQGWLe5Q7HXfbCko4nuHereXY4OTXlr_0CDOdDIvaN0h01qEX4RkfXHmJBHh6mhStc9bYN_lEIdcl5MIWa0)

*Figure 9: Reading browser information*

The attackers had also infected the macOS 3CX app. The analysis below details the macOS version of compromised 3CXDesktopApp.

## **m...