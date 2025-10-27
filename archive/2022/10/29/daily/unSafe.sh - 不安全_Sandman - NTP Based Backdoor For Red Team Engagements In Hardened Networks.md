---
title: Sandman - NTP Based Backdoor For Red Team Engagements In Hardened Networks
url: https://buaq.net/go-133134.html
source: unSafe.sh - 不安全
date: 2022-10-29
fetch_date: 2025-10-03T21:11:26.854077
---

# Sandman - NTP Based Backdoor For Red Team Engagements In Hardened Networks

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

![](https://8aqnet.cdn.bcebos.com/f525043d196f8d0d9e5b27e94f0f33d8.jpg)

Sandman - NTP Based Backdoor For Red Team Engagements In Hardened Networks

Sandman is a backdoor that is meant to work on hardened networks during red team engagements
*2022-10-28 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-133134.htm)
阅读量:45
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgojLgd6sJR_TeNcazI5aPkQwckwIr_3-PCUhF6PXGkwVB9Lej80_ciLS0tK2LrUGVDOPl2C-j8eoYpcZGdT0zyklHu1IjRZmdWysuVBw91kmbQ2kWZR2nJ_7lhea417b22apQ-kXEU3QYNCvk-XcuA_N23Peog566GqAvQlCU9YPmqBisQeUr9jgVFsA=w640-h388)](https://blogger.googleusercontent.com/img/a/AVvXsEgojLgd6sJR_TeNcazI5aPkQwckwIr_3-PCUhF6PXGkwVB9Lej80_ciLS0tK2LrUGVDOPl2C-j8eoYpcZGdT0zyklHu1IjRZmdWysuVBw91kmbQ2kWZR2nJ_7lhea417b22apQ-kXEU3QYNCvk-XcuA_N23Peog566GqAvQlCU9YPmqBisQeUr9jgVFsA)

Sandman is a [backdoor](https://www.kitploit.com/search/label/Backdoor "backdoor") that is meant to work on hardened networks during [red team](https://www.kitploit.com/search/label/Red%20Team "red team") engagements.

Sandman works as a stager and leverages NTP (a protocol to sync time & date) to get and run an arbitrary **shellcode** from a pre-defined server.

Since NTP is a protocol that is overlooked by many defenders resulting in wide network accessibility.

## Usage

### SandmanServer (Usage)

Run on windows / \*nix machine:

```
python3 sandman_server.py "Network Adapter" "Payload Url" "optional: ip to spoof"
```

* Network Adapter: The adapter that you want the server to listen on (for example [Ethernet](https://www.kitploit.com/search/label/Ethernet "Ethernet") for Windows, eth0 for \*nix).
* Payload Url: The URL to your shellcode, it could be your agent (for example, [CobaltStrike](https://www.kitploit.com/search/label/CobaltStrike "CobaltStrike") or meterpreter) or another stager.
* IP to Spoof: If you want to spoof a legitimate IP address (for example, time.microsoft.com's IP address).

### SandmanBackdoor (Usage)

To start, you can compile the SandmanBackdoor as [mentioned below](https://github.com/Idov31/Sandman#setup "mentioned below"), because it is a single lightweight C# executable you can execute it via ExecuteAssembly, run it as an NTP provider or just execute/inject it.

### SandmanBackdoorTimeProvider (Usage)

To use it, you will need to follow simple steps:

* Add the following registry value:

```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpClient" /v DllName /t REG_SZ /d "C:\Path\To\TheDll.dll"
```

* Restart the w32time service:

```
sc stop w32time
```

**NOTE: Make sure you are compiling with the x64 option and not any CPU option!**

## Capabilities

* Getting and executing an arbitrary payload from an attacker's controlled server.
* Can work on hardened networks since NTP is usually allowed in FW.
* Impersonating a legitimate NTP server via IP spoofing.

## Setup

### SandmanServer (Setup)

* Python 3.9
* The [requirements](https://www.kitploit.com/search/label/Requirements "requirements") are specified in the [requirements](https://github.com/Idov31/Sandman/blob/master/SandmanServer/requirements.txt "requirements") file.

### SandmanBackdoor (Setup)

To compile the backdoor I used Visual Studio 2022, but as mentioned in the [usage section](https://github.com/Idov31/Sandman#usage "usage section") it can be compiled with both VS2022 and CSC. You can compile it either using the USE\_SHELLCODE and use Orca's shellcode or without USE\_SHELLCODE to use WebClient.

### SandmanBackdoorTimeProvider (Setup)

To compile the backdoor I used Visual Studio 2022, you will also need to install [DllExport](https://github.com/3F/DllExport "DllExport") (via Nuget or any other way) to compile it. You can compile it either using the USE\_SHELLCODE and use Orca's shellcode or without USE\_SHELLCODE to use WebClient.

## IOCs

* A shellcode is injected into RuntimeBroker.
* Suspicious NTP communication starts with a known magic header.
* YARA rule.

## Contributes

* [Orca](https://github.com/ORCx41/ "Orca") for the shellcode.
* Special thanks to [Tim McGuffin](https://twitter.com/NotMedic "Tim McGuffin") for the [time provider idea](https://twitter.com/NotMedic/status/1561354598744473601 "time provider idea").

Thanks to those who already contributed and I'll happily accept contributions, make a pull request and I will review it!

Sandman - NTP Based Backdoor For Red Team Engagements In Hardened Networks
![Sandman - NTP Based Backdoor For Red Team Engagements In Hardened Networks](https://blogger.googleusercontent.com/img/a/AVvXsEgojLgd6sJR_TeNcazI5aPkQwckwIr_3-PCUhF6PXGkwVB9Lej80_ciLS0tK2LrUGVDOPl2C-j8eoYpcZGdT0zyklHu1IjRZmdWysuVBw91kmbQ2kWZR2nJ_7lhea417b22apQ-kXEU3QYNCvk-XcuA_N23Peog566GqAvQlCU9YPmqBisQeUr9jgVFsA=s72-w640-c-h388)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/10/sandman-ntp-based-backdoor-for-red-team.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)