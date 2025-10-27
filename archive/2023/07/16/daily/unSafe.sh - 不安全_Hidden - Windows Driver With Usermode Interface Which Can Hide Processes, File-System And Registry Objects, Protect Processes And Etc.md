---
title: Hidden - Windows Driver With Usermode Interface Which Can Hide Processes, File-System And Registry Objects, Protect Processes And Etc
url: https://buaq.net/go-172129.html
source: unSafe.sh - 不安全
date: 2023-07-16
fetch_date: 2025-10-04T11:50:56.254317
---

# Hidden - Windows Driver With Usermode Interface Which Can Hide Processes, File-System And Registry Objects, Protect Processes And Etc

* [unSafe.sh - õĖŹÕ«ēÕģ©](https://unsafe.sh)
* [µłæńÜäµöČĶŚÅ](/user/collects)
* [õ╗ŖµŚźńāŁµ”£](/?hot=true)
* [Õģ¼õ╝ŚÕÅĘµ¢ćń½Ā](/?gzh=true)
* [Õ»╝Ķł¬](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [ń╝¢ńĀü/Ķ¦ŻńĀü](/encode)
* [µ¢ćõ╗Čõ╝ĀĶŠō](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
ķ╗æÕż£µ©ĪÕ╝Å

![](https://8aqnet.cdn.bcebos.com/a4784dad3e19a13b0baa5e4d3a7f45f6.jpg)

Hidden - Windows Driver With Usermode Interface Which Can Hide Processes, File-System And Registry Objects, Protect Processes And Etc

Hidden has been developed like a solution for reverse engineering and researching tasks. Thi
*2023-7-15 20:30:0
Author: [www.kitploit.com(µ¤źń£ŗÕÄ¤µ¢ć)](/jump-172129.htm)
ķśģĶ»╗ķćÅ:32
µöČĶŚÅ*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCsqGpqHUKim518QHj01UN4ho_HL9P234nMwoOxKPBZhD2-2w5Sb-_aAkquNrwdNDvWeCAfBigOrXzeZSu7hIvK1CTTVXYjx_cZ6xetq5OUA1JVTwWR7FG-OwR0OkFHhnMI58mh3gCX9-c3i5Zh0cGJFT4sXmJ_IUUg44qRFuvIrOxa55n7twzqir60lbT/w636-h640/h77.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCsqGpqHUKim518QHj01UN4ho_HL9P234nMwoOxKPBZhD2-2w5Sb-_aAkquNrwdNDvWeCAfBigOrXzeZSu7hIvK1CTTVXYjx_cZ6xetq5OUA1JVTwWR7FG-OwR0OkFHhnMI58mh3gCX9-c3i5Zh0cGJFT4sXmJ_IUUg44qRFuvIrOxa55n7twzqir60lbT/s348/h77.png)

Hidden has been developed like a solution for [reverse engineering](https://www.kitploit.com/search/label/Reverse%20Engineering "reverse engineering") and researching tasks. This is a [windows driver](https://www.kitploit.com/search/label/Windows%20Driver "windows driver") with a usermode interface which is used for hiding specific environment on your windows machine, like installed RCE programs (ex. procmon, wireshark), vm [infrastructure](https://www.kitploit.com/search/label/Infrastructure "infrastructure") (ex. vmware tools) and etc.

## Features

* hide registry keys and values
* hide files and directories
* hide processes (*experimental, might be not stable*)
* protect specific processes
* exclude specific processes from hiding and [protection](https://www.kitploit.com/search/label/Protection "protection") features
* usermode interface (lib and cli) for working with a driver

and so on

## System requirements

Windows Vista and above, x86 and x64

## Recommended build environment

* Visual Studio 2019
* Windows Driver Kit 10

## Building

Following guide explains how to make a release win32 build

1. Open Hidden.sln using Visual Studio
2. Build **Hidden Package** project with configurations Release, Win32
3. Open build results folder **<ProjectDir>\Release**

## Installing

1. Disable a digital signature enforcement on a test machine (bcdedit /set TESTSIGNING ON) and reboot it
2. Copy files from **<ProjectDir>\Release\Hidden Package** to a test machine
3. Right mouse click on **Hidden.inf** and choose **Install**
4. Start a driver (sc start hidden)
5. Make sure service is running (sc query hidden)

Important: Keep in mind that the driver bitness have to be the same to an OS bitness

## Hiding

A [command line](https://www.kitploit.com/search/label/Command%20Line "command line") tool **hiddencli** is used for managing a driver. You are able to use it for hiding and unhiding objects, changing a driver state and so on.

To hide a file try the command

```
hiddencli /hide file c:\Windows\System32\calc.exe
```

Want to hide a directory? No problems

```
hiddencli /hide dir "c:\Program Files\VMWare"
```

Registry key?

```
hiddencli /hide regkey "HKCU\Software\VMware, Inc."
```

Maybe a process?

By a process image name?

```
hiddencli /hide image apply:forall c:\Windows\Explorer.EXE
```

To get a full help just type

Hidden - Windows Driver With Usermode Interface Which Can Hide Processes, File-System And Registry Objects, Protect Processes And Etc
![Hidden - Windows Driver With Usermode Interface Which Can Hide Processes, File-System And Registry Objects, Protect Processes And Etc](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCsqGpqHUKim518QHj01UN4ho_HL9P234nMwoOxKPBZhD2-2w5Sb-_aAkquNrwdNDvWeCAfBigOrXzeZSu7hIvK1CTTVXYjx_cZ6xetq5OUA1JVTwWR7FG-OwR0OkFHhnMI58mh3gCX9-c3i5Zh0cGJFT4sXmJ_IUUg44qRFuvIrOxa55n7twzqir60lbT/s72-w636-c-h640/h77.png)
Reviewed by Zion3R
on
8:30ŌĆ»AM
Rating: 5

µ¢ćń½ĀµØźµ║É: http://www.kitploit.com/2023/07/hidden-windows-driver-with-usermode.html
 Õ”éµ£ēõŠĄµØāĶ»ĘĶüöń│╗:admin#unsafe.sh

© [unSafe.sh - õĖŹÕ«ēÕģ©](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [Õ«ēÕģ©ķ®¼Õģŗ](https://aq.mk)
* [µś¤ķÖģķ╗æÕ«ó](https://xj.hk)
* [T00ls](https://t00ls.net)