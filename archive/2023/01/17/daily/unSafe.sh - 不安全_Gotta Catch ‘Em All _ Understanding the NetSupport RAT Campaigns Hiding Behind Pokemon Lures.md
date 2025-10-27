---
title: Gotta Catch ‘Em All | Understanding the NetSupport RAT Campaigns Hiding Behind Pokemon Lures
url: https://buaq.net/go-145793.html
source: unSafe.sh - 不安全
date: 2023-01-17
fetch_date: 2025-10-04T04:01:58.931625
---

# Gotta Catch ‘Em All | Understanding the NetSupport RAT Campaigns Hiding Behind Pokemon Lures

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

![](https://8aqnet.cdn.bcebos.com/7eea11950b44569753ff3cc5874aab77.jpg)

Gotta Catch ‘Em All | Understanding the NetSupport RAT Campaigns Hiding Behind Pokemon Lures

Researchers at ASEC recently reported on a NetSupport RAT campaign that utilizes Pokemon as the soc
*2023-1-16 22:28:35
Author: [www.sentinelone.com(查看原文)](/jump-145793.htm)
阅读量:37
收藏*

---

Researchers at [ASEC](https://asec.ahnlab.com/en/45312/) recently reported on a NetSupport RAT campaign that utilizes Pokemon as the social engineering lure. Threat actors staged a malicious website, hosting a Pokemon-based NFT game, offering both a fun and financially rewarding experience. In reality, those drawn into the site are coerced into downloading the trojanized NetSupport RAT client, allowing attackers full access to their device.

NetSupport RAT has been observed [in](https://izoologic.com/2020/05/28/microsoft-alerts-netsupport-manager-rat-phishing-attacks/) [numerous](https://blog.cyble.com/2022/09/21/netsupport-rat-distributed-via-socgholish/) [attacks](https://www.sentinelone.com/labs/socgholish-diversifies-and-expands-its-malware-staging-infrastructure-to-counter-defenders/) on enterprise environments over the years, and Pokemon is just the latest in a long line of creative lures used to distribute and drop NetSupport RAT. It is frequently used by cybercriminals as a ‘quick solution’ in lieu of implementing something more bespoke.

In this post, we provide an overview of NetSupport RAT and discuss the technical details of a recent campaign.

![](https://www.sentinelone.com/wp-content/uploads/2023/01/Gotta-Catch-Em-All-Understanding-the-NetSupport-RAT-Campaigns-Hiding-Behind-Pokemon-Lures.jpg)

## Background

NetSupport RAT is based on NetSupport Manager, a legitimate tool which is frequently used by bad actors for malicious purposes in ways similar to [TeamViewer](https://www.sentinelone.com/blog/ciso-essentials-how-remote-access-trojans-affect-the-enterprise/). NetSupport Manager, used maliciously or otherwise, provides full and complete control over the target device. Once the client has been installed, attackers can access, acquire, and manipulate any data on the device (exfiltrate data, execute additional payloads). In addition, the software allows at least the following:

* Real-time screen monitoring, optimized for monitoring multiple devices
* Taking control or redirect user screens
* Capturing screenshots, audio, video

Malicious versions are constantly being sold or rented out via underground crime marketplaces.

![NetSupport Manager RAT offered for rental](https://www.sentinelone.com/wp-content/uploads/2023/01/NetSupportRAT_2.jpg)

NetSupport Manager RAT offered for rental

As NetSupport Manager is a legitimate tool that has a long history of development, it is highly attractive to attackers as it can be relied on to work ‘out of the box’. Additionally, it is thoroughly documented and actively supported: benefits that are less likely with custom-built malware that provides similar functionality such as Andromeda, Nanocore, CirenegRAT, Dark Comet and others.

Malicious use of NetSupport Manager (*aka* NetSupport RAT) has been observed since at least late 2017. The use of “legitimate” or COTS (Commercial off the Shelf) tools is highly beneficial to attackers when attempting to achieve the greatest degree of stealth. Custom-written malware can often be detected by some layer of protection, such as EPP and EDR tools, so it is often advantageous to utilize a legitimate tool, even if it takes some creativity to deliver the remote software client.

ASEC reported that the NetSupport RAT droppers were delivered via [phishing emails](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) that entice targets to install a “Pokemon card game”. On doing so, the victim unknowingly installs the NetSupport RAT, a doctored version of the NetSupport Manager client (`client32.exe`) that gives the attacker immediate and direct control of the infected device. While this specific attack was centered around the Pokemon theme, other phishing lures are known to be used.

Some recent NetSupport RAT campaigns utilize `.ISO` files as droppers. This allows the attackers to evade certain types of detection. This technique has been used by [ransomware actors](https://www.youtube.com/watch?v=9HKVdnvnGto) as well such as by both Maze and Ragnar Locker.

When opened, the ISO files will contain either the NetSupport RAT installer (with configs/support files) or a [.LNK file](https://www.sentinelone.com/labs/who-needs-macros-threat-actors-pivot-to-abusing-explorer-and-other-lolbins-via-windows-shortcuts/) redirecting the victim to said installer.

## Technical Details

A typical example of this kind of `.ISO` file is the sample `CLF_security.iso` (`288603f501926756c236e368a1fdc7d128f4f9a1`).

![NetSupport RAT ISO file](https://www.sentinelone.com/wp-content/uploads/2023/01/NetSupportRAT_4.jpg)

This particular `.ISO` contains an embedded `.EXE` file (`CLFSECUR.EXE`) which is then utilized to drop and execute the installer for NetSupport RAT.

Sample `4233ff7941da62b86fc2c2d92be0572c9ab534c8` has been observed in multiple ISO files masquerading as legitimate software, including:

* CodeTwo Exchange Manager
* PCFresh 2022 SDK Tools
* Google Chrome
* Google Crash Handler
* Steelray Project Setup
* BrowserRenew.iso
* CLFsecurity.ISO
* Cloudflare\_security\_setup.iso

![](https://www.sentinelone.com/wp-content/uploads/2023/01/NetSupportRAT_3.jpg)

The RAT installation is disguised to look similar to a Google Chrome installation.

![](https://www.sentinelone.com/wp-content/uploads/2023/01/NetSupportRAT_10.jpg)

![NetSupport RAT Install disguised as Google Chrome setup.](https://www.sentinelone.com/wp-content/uploads/2023/01/NetSupportRAT_5.jpg)

NetSupport RAT installer disguised as Google Chrome setup.

The sample is obfuscated via the Babadeda [crypter](https://attack.mitre.org/techniques/T1027/). When executed, a [base64](https://www.sentinelone.com/blog/guide-encode-decoded-base64/) encoded string is used to specify various parameters including sessionID and other critical values to the NetSupport connection.

![Base64 encoded RAT execution command](https://www.sentinelone.com/wp-content/uploads/2023/01/NetSupportRAT_7.jpg)

Base64 encoded RAT execution command

The command decodes to look similar to the following:

![NetSupport RAT decoded command](https://www.sentinelone.com/wp-content/uploads/2023/01/NetSupportRAT_9.jpg)

NetSupport RAT decoded command

Persistence for the RAT is achieved via registry entry, and a shortcut to the installed RAT executable is written to the Startup folder. For example:

```
~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\NetSupport.url
```

In this case, the shortcut links to `\AppData\Roaming\Steelray Project Viewer`. In addition, the sample generates a scheduled task with multiple triggers.

![NetSupport RAT Persistence via Scheduled Task](https://www.sentinelone.com/wp-content/uploads/2023/01/NetSupportRAT_8.jpg)

NetSupport RAT Persistence via Scheduled Task

![Install directory of NetSupport RAT](https://www.sentinelone.com/wp-content/uploads/2023/01/NetSupportRAT_1.jpg)

Install directory of NetSupport RAT

The RAT performs a number of discovery operations to understand its host environment. Network adapter details are pulled via `GetAdaptersAddresses`. Additional data is gleaned via [WMI queries](https://www.sentinelone.com/labs/labscon-replay-blasting-event-driven-cornucopia-wmi-based-user-space-attacks-blind-siems-and-edrs/) such as:

```
SELECT * FROM Win32_ComputerSystem
SELECT * FROM Win32_System...