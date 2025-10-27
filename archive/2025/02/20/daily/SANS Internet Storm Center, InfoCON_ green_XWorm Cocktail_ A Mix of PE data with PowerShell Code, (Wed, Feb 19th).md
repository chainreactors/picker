---
title: XWorm Cocktail: A Mix of PE data with PowerShell Code, (Wed, Feb 19th)
url: https://isc.sans.edu/diary/rss/31700
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-20
fetch_date: 2025-10-06T20:50:00.342300
---

# XWorm Cocktail: A Mix of PE data with PowerShell Code, (Wed, Feb 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31692)
* [next](/diary/31704)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [XWorm Cocktail: A Mix of PE data with PowerShell Code](/forums/diary/XWorm%2BCocktail%2BA%2BMix%2Bof%2BPE%2Bdata%2Bwith%2BPowerShell%2BCode/31700/)

**Published**: 2025-02-19. **Last Updated**: 2025-02-19 07:39:49 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/XWorm%2BCocktail%2BA%2BMix%2Bof%2BPE%2Bdata%2Bwith%2BPowerShell%2BCode/31700/#comments)

While hunting, I spent some time trying to deobfuscate a malicious file discovered on VT. It triggered my PowerShell rule. At the end, I found two files that look close together:

* 7c2f2a9a6078d37ee241e43f392f825630016c8ca8416bfd12cd27501b6876d1 (Score: 3/61)[[1](https://www.virustotal.com/gui/file/7c2f2a9a6078d37ee241e43f392f825630016c8ca8416bfd12cd27501b6876d1)]
* d0b448d4de707a9fb611166278065afa2c52029234f7876158c8dd4798f08f9f (Score: 1/62)[[2](https://www.virustotal.com/gui/file/d0b448d4de707a9fb611166278065afa2c52029234f7876158c8dd4798f08f9f)]

They are identified as “data files,” and their upload names are, respectively, “XClient.exe” and “XingCode Unblocker 2025.exe". XignCode is anti-cheat software primarily used in online games to prevent cheating, hacking, and the use of unauthorized third-party tools. Note the typo in the file name!

When you open the file, you see this:

![](https://isc.sans.edu/diaryimages/images/isc-20250219-1.png)

You can spot a PowerShell function at the beginning that is used to deobfuscate data (un-Base64, decompress, ...). You can also read the classic string "This program cannot be run in DOS mode.". Between binary data, you can also easily see some code. A lot of characters are encoded using "join" operations. By example:

```

PS C:\Users\REM> -join[char[]]((503-426),(-4550+4640),(71128-5595))
MZ?
```

This is the very beginning of the PE file locate just after the initial function. Other pieces of code are based on a mix of small mathematical operations combined with logical operands. By example:

```

PS C:\Users\REM> ((((((((((((((((((8657-Bxor-8656)-Band2*(8657-Band-8656))-Band((8657-Bxor-8656)-Bor2*(8657-Band-8656)))-Band(((8657-Bxor-8656)-Band2*(8657-Band-8656))-Bor((8657-Bxor-8656)-Bor2*(8657-Band-8656))))+((((8657-Bxor-8656)-Band2*(8657-Band-8656))-Band((8657-Bxor-8656)-Bor2*(8657-Band-8656)))-Bor(((8657-Bxor-8656)-Band2*(8657-Band-8656))-Bor((8657-Bxor-8656)-Bor2*(8657-Band-8656)))))+0)-0)))+0)-0)))+0)-0))))
1
```

Normally, PowerShell should ignore the non-readable characters but, if you try to execute this file with PowerShell in a sandbox, it miserably fails due to "bad" characters here and there. I tried to write a small script to deobfuscate all the pieces of code described above but the PE file was still corrupted.

If you extract ASCII strings from the files, you'll get a lot of interesting strings but Unicode strings are more interesting:

```

remnux@remnux:/mnt/hgfs/MalwareZoo/20250215$ strings --encoding=l 7c2f2a9a6078d37ee241e43f392f825630016c8ca8416bfd12cd27501b6876d1
```

Here are the most interesting strings:

```

schtasks.exe
/create /f /RL HIGHEST /sc minute /mo 1 /tn "
/create /f /sc minute /mo 1 /tn "
SOFTWARE\Microsoft\Windows\CurrentVersion\Run
.lnk
WScript.Shell
CreateShortcut
TargetPath
WorkingDirectory
Save
 [XWorm V5.6]
New Clinet :
UserName :
OSFullName :
USB :
CPU :
GPU :
RAM :
Groub :
https://api.telegram.org/bot
/sendMessage?chat_id=
&text=
powershell.exe
-ExecutionPolicy Bypass Add-MpPreference -ExclusionPath '
-ExecutionPolicy Bypass Add-MpPreference -ExclusionProcess '
http://ip-api.com/line/?fields=hosting
Select * from Win32_ComputerSystem
VirtualBox
SbieDll.dll
\root\SecurityCenter2
Select * from AntivirusProduct
SELECT * FROM Win32_VideoController
PING!
pong
shutdown.exe /f /s /t 0
RunShell
StartDDos
StopDDos
StartReport
StopReport
Xchat
Hosts
\drivers\etc\hosts
Modified successfully!
sendPlugin
savePlugin
RemovePlugins
Plugins Removed!
OfflineGet
RunRecovery
Recovery
RunOptions
POST / HTTP/1.1
schtasks
/delete /f  /tn "
.bat
@echo off
timeout 3 > NUL
DEL "
" /f /q
ToUpper
Space
[SPACE]
)eturn
[ENTER]
)scape
[ESC]
LControlKey
)CTRL]
RControlKey
RShiftKey
[Shift]
LShiftKey
Back
)Back]
LWin
)WIN]
)Tab]
Capital
[CAPSLOCK: OFF]
[CAPSLOCK: ON]
```

It's crystal clear that the malware is a copy of XWorm[[3](https://any.run/report/add19a9db4730f41575fb951e9aec6dcf35d8db2cb94cba896667881467e6fd5/8d974012-b880-482f-a35f-68a0808a2e33)].

I'm curious about the obfuscation tool/technique used in these files. If you know how to process them without error, let me know!

[1] <https://www.virustotal.com/gui/file/7c2f2a9a6078d37ee241e43f392f825630016c8ca8416bfd12cd27501b6876d1>
[2] <https://www.virustotal.com/gui/file/d0b448d4de707a9fb611166278065afa2c52029234f7876158c8dd4798f08f9f>
[3] <https://any.run/report/add19a9db4730f41575fb951e9aec6dcf35d8db2cb94cba896667881467e6fd5/8d974012-b880-482f-a35f-68a0808a2e33>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [XWorm](/tag.html?tag=XWorm) [PowerShell](/tag.html?tag=PowerShell) [Malware](/tag.html?tag=Malware) [Obfuscation](/tag.html?tag=Obfuscation)

[0 comment(s)](/diary/XWorm%2BCocktail%2BA%2BMix%2Bof%2BPE%2Bdata%2Bwith%2BPowerShell%2BCode/31700/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31692)
* [next](/diary/31704)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)