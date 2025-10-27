---
title: PPLcontrol - Controlling Windows PP(L)s
url: https://buaq.net/go-172151.html
source: unSafe.sh - 不安全
date: 2023-07-17
fetch_date: 2025-10-04T11:51:09.899020
---

# PPLcontrol - Controlling Windows PP(L)s

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

![](https://8aqnet.cdn.bcebos.com/e494ff4b244c7f48d3a127af05f21eeb.jpg)

PPLcontrol - Controlling Windows PP(L)s

This tool allows you to list protected processes, get the protection level of a specific pro
*2023-7-16 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-172151.htm)
阅读量:39
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCVW_aQlUOUcJ-1hu-Lfmu37YQkP155xR1Ss1FG1cTgwtdJWkqYypXoK-FkNadmmmLxwp83-fyakvI7nOluK-G5gPLUZjUywtcH2NMFA4XKLbzYBZk04C7aZM-aqJfnhkooYR1_pbm35auMGYDfDsvV82Ewov86uYC3V7sfiE_Y9GxpdS7U8SJrExiixtM/w640-h418/h36.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCVW_aQlUOUcJ-1hu-Lfmu37YQkP155xR1Ss1FG1cTgwtdJWkqYypXoK-FkNadmmmLxwp83-fyakvI7nOluK-G5gPLUZjUywtcH2NMFA4XKLbzYBZk04C7aZM-aqJfnhkooYR1_pbm35auMGYDfDsvV82Ewov86uYC3V7sfiE_Y9GxpdS7U8SJrExiixtM/s490/h36.png)

This tool allows you to list protected processes, get the protection level of a specific process, or set an arbitrary protection level. For more information, you can read this blog post: [Debugging Protected Processes](https://itm4n.github.io/debugging-protected-processes/ "Debugging Protected Processes").

## Usage

### 1. Download the MSI driver

You can get a copy of the MSI driver `RTCore64.sys` here: [PPLKiller/driver](https://github.com/RedCursorSecurityConsulting/PPLKiller/tree/master/driver "PPLKiller/driver").

### 2. Install the MSI driver

**Disclaimer:** it goes without saying that you should never install this driver on your host machine. **Use a VM!**

```
sc.exe create RTCore64 type= kernel start= auto binPath= C:\PATH\TO\RTCore64.sys DisplayName= "Micro - Star MSI Afterburner"
```

### 3. Use PPLcontrol

List protected processes.

Get the protection level of a specific process.

Set an arbitrary protection level.

```
PPLcontrol.exe set 1234 PPL WinTcb
```

Protect a non-protected process with an arbitrary protection level. This will also automatically adjust the signature levels accordingly.

```
PPLcontrol.exe protect 1234 PPL WinTcb
```

Unprotect a protected process. This will set the protection level to `0` (*i.e.* `None`) and the EXE/DLL signature levels to `0` (*i.e.* `Unchecked`).

```
PPLcontrol.exe unprotect 1234
```

### 4. Uninstall the driver

```
net stop RTCore64
sc.exe delete RTCore64
```

## Use cases

### Debugging a protected process with WinDbg

WinDbg just needs to open the target process, so you can use PPLcontrol to set an arbitrary protection level on your `windbg.exe` process.

1. Get the PID of the `windbg.exe` process.
2. Use PPLcontrol to set an arbitrary protection level.

Console 1 24,840 K C:\Temp>PPLcontrol.exe protect 1232 PPL WinTcb [+] The [Protection](https://www.kitploit.com/search/label/Protection "Protection") 'PPL-WinTcb' was set on the process with PID 1232, previous protection was: 'None-None'. [+] The Signature level 'WindowsTcb' and the Section signature level 'Windows' were set on the process with PID 1232." dir="auto">

```
C:\Temp>tasklist | findstr /i windbg
windbg.exe                    1232 Console                    1     24,840 K
C:\Temp>PPLcontrol.exe protect 1232 PPL WinTcb
[+] The Protection 'PPL-WinTcb' was set on the process with PID 1232, previous protection was: 'None-None'.
[+] The Signature level 'WindowsTcb' and the Section signature level 'Windows' were set on the process with PID 1232.
```

### Inspecting a protected process with API Monitor

In addition to opening the target process, API monitor injects a DLL into it. Therefore, setting an arbitrary protection level on your `apimonitor.exe` process won't suffice. Since the injected DLL is not properly signed for this purpose, the Section signature flag of the target process will likely prevent it from being loaded. However, you can temporarily disable the protection on the target process, start monitoring it, and restore the protection right after.

```
Failed to load module in target process - Error: 577, Windows cannot verify the digital signature for this file. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source.
```

1. Get the PID of the target process.
2. Use PPLcontrol to get the protection level of the target process.
3. Unprotect the process.
4. Start monitoring the process with API Monitor.
5. Restore the protection of the target process.

```
C:\Temp>tasklist | findstr /i target
target.exe                    1337 Services                   1     14,160 K
C:\Temp>PPLcontrol.exe get 1337
[+] The process with PID 1337 is a PPL with the Signer type 'WinTcb' (6).
C:\Temp>PPLcontrol.exe unprotect 1337
[+] The process with PID 1337 is no longer a PP(L).

C:\Temp>PPLcontrol.exe protect 1337 PPL WinTcb
[+] The Protection 'PPL-WinTcb' was set on the process with PID 1337, previous protection was: 'None-None'.
[+] The Signature level 'WindowsTcb' and the Section signature level 'Windows' were set on the process with PID 1337.
```

## Build

1. Open the solution in Visual Studio.
2. Select `Release/x64` (`x86` is not supported and will probably never be).
3. Build solution

## Credit

* [@aceb0nd](https://twitter.com/aceb0nd "@aceb0nd") for the tool [PPLKiller](https://github.com/RedCursorSecurityConsulting/PPLKiller "PPLKiller")
* [@aionescu](https://twitter.com/aionescu "@aionescu") for the article [Protected Processes Part 3: Windows PKI Internals (Signing Levels, Scenarios, Root Keys, EKUs & Runtime Signers)](https://www.alex-ionescu.com/?p=146 "Protected Processes Part 3: Windows PKI Internals (Signing Levels, Scenarios, Root Keys, EKUs & Runtime Signers)")

文章来源: http://www.kitploit.com/2023/07/pplcontrol-controlling-windows-ppls.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)