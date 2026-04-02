---
title: Malicious Script That Gets Rid of ADS, (Wed, Apr 1st)
url: https://isc.sans.edu/diary/rss/32854
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-01
fetch_date: 2026-04-02T04:31:29.909016
---

# Malicious Script That Gets Rid of ADS, (Wed, Apr 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32850)
* [next](/diary/32856)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [Malicious Script That Gets Rid of ADS](/forums/diary/Malicious%2BScript%2BThat%2BGets%2BRid%2Bof%2BADS/32854/)

**Published**: 2026-04-01. **Last Updated**: 2026-04-01 20:09:43 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Malicious%2BScript%2BThat%2BGets%2BRid%2Bof%2BADS/32854/#comments)

Today, most malware are called “fileless” because they try to reduce their footprint on the infected computer filesystem to the bare minimum. But they need to write something… think about persistence. They can use the registry as an alternative storage location.

But some scripts still rely on files that are executed at boot time. For example, via a “Run” key:

```

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v csgh4Pbzclmp /t REG_SZ /d "\"%APPDATA%\Microsoft\Windows\Templates\dwm.cmd\"" /f >nul 2>&1
```

The file located in %APPDATA% will be executed at boot time.

From the attacker’s point of view, there is a problem: The original script copies itself:

```

copy /Y "%~f0" "%APPDATA%\Microsoft\Windows\Templates\dwm.cmd" >nul 2>&1
```

Just after the copy operation, a PowerShell one-liner is executed:

```

powershell -w h -c "try{Remove-Item -Path '%APPDATA%\Microsoft\Windows\Templates\dwm.cmd:Zone.Identifier' -Force -ErrorAction SilentlyContinue}catch{}" >nul 2>&1
```

PowerShell will try to remove the alternate-data-stream (ADS) “:Zone.Identifier” that Windows adds during file operations. The :Zone.Identifier indicates the source of the file (0 = My Computer, 1 = Local intranet, 2 = Trusted sites, 3 = Internet, 4 = Restricted sites). It's not clear if a "copy" will drop or conserver the ADS. I did not find an official Microsoft documentation but, if you ask to a LLM, it will tell you that they are not preserved. They are wrong!

In my Windows 10 lab, I downloaded a copy of BinaryNinja. An ADS was added to the file. After a copy to "test.ext", the new file has still the ADS!

![](https://isc.sans.edu/diaryimages/images/isc-20260401-1.png)By removing the ADS, the malicious script makes the file look less suspicious if the system is scanned to search for "downloaded" files (a classic operation performed in DFIR investigations).

For the story, the script will later invoke another PowerShell that will drop a DonutLoader on the victim's computer.

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [ADS](/tag.html?tag=ADS) [File](/tag.html?tag=File) [Zone](/tag.html?tag=Zone) [PowerShell](/tag.html?tag=PowerShell) [Copy](/tag.html?tag=Copy)

[0 comment(s)](/diary/Malicious%2BScript%2BThat%2BGets%2BRid%2Bof%2BADS/32854/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/32850)
* [next](/diary/32856)

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