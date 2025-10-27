---
title: More Exotic Excel Files Dropping AgentTesla, (Wed, Aug 23rd)
url: https://isc.sans.edu/diary/rss/30150
source: SANS Internet Storm Center, InfoCON: green
date: 2023-08-24
fetch_date: 2025-10-04T12:02:29.856461
---

# More Exotic Excel Files Dropping AgentTesla, (Wed, Aug 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30146)
* [next](/diary/30152)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [More Exotic Excel Files Dropping AgentTesla](/forums/diary/More%2BExotic%2BExcel%2BFiles%2BDropping%2BAgentTesla/30150/)

**Published**: 2023-08-23. **Last Updated**: 2023-08-23 07:22:57 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/More%2BExotic%2BExcel%2BFiles%2BDropping%2BAgentTesla/30150/#comments)

Excel is an excellent target for attackers. The Microsoft Office suite is installed on millions of computers, and people trust these files. If we have the classic xls, xls, xlsm file extensions, Excel supports many others! Just check your local registry:

![](https://isc.sans.edu/diaryimages/images/isc-20230823-1.PNG)

Attackers like to use more “exotic” extensions to increase chances of evading simple and stupid rules at mail gateways. This time, the extension used was “.xlam”. I spotted several emails (probably from the same campaign) that delivered .xlam files to potential victims.

An XLAM file is a macro-enabled add-in used to add new features to Excel. The icon looks like Excel and should make the user confident to open it:

![](https://isc.sans.edu/diaryimages/images/isc-20230823-3.png)

Once loaded, you can see the add-on in Excel:

![](https://isc.sans.edu/diaryimages/images/isc-20230823-2.PNG)

The add-on has the following SHA256: 72006dfd34f5b043e6763b16ff8399382e69ad356e8c6b9e71ec908674dab55c and a VT score of 30/56[[1](https://www.virustotal.com/gui/file/72006dfd34f5b043e6763b16ff8399382e69ad356e8c6b9e71ec908674dab55c)].

If you read “macro-enabled”, it’s not classic VBA macro, but this add-on contains an exploit for the good old Equation Editor ([CVE-:2017-1182](/vuln.html?cve=:2017-1182)). If successfully exploited, the add-on will download a malicious VBS script and execute it:

```

C:\Windows\System32\WScript.exe" "C:\Users\user01\AppData\Roaming\oldgyyudi.vbs"
```

The URL from where the script is downloaded is http://80[.]76[.]51[.]248/afk.vbs

The script has the following SHA256: d93c28f9ceeac993f652f976e12eba842716d571370bcdb2dd912965aa6274fb (unknown on VT at this time) and is pretty well obfuscated. Here is an example of a function that reverses a string:

```

Escola = drRgvLwPScMUPVCgWhShgMSmjRqaWCUXzUCPCcDqXCNWRLWXvdWLpQmrjqdvCWZzRcUiWUrawWCsywwLLVsoBPeWDkNtPrWMEMEPZlGYBLWZMhMmMMZVWgeCwhgXq
Escola = eKRiX(eKRiX(eKRiX(Escola)))
[...]

Function eKRiX(iNcPxLbcdBdHlsOAcdpbduplKWscQhRhriWZpuxAGtjteLbDKxgbQjArhOoIuccrMKcNHRiJWiuBxLOUbKyUuLcboDKKbzuhLJCTwrTtcOspGRMunLiIoOogKuiencc)
qArcGzUDayYkTOOcTWLZccaLRrsnUkODDkkHOcpTDMaUNzsXrXTnHUTYLCqrOfyGNJkRLUQnMLOQNWUnKOGkMWUTNJYZLiUZfNzHyccKMKwINzNLYNINsrKBWzsDi =
    Chr(83)&Chr(116)&Chr(114)&Chr(82)&Chr(101)&Chr(118)&Chr(101)&Chr(114)&Chr(115)&Chr(101)
nnUTLnLIujuBNUwLIOWkWRfBJwUWcrGrIawtWSLIShigAikDLGDwKWLmrGcvRaoIUUPcgOaklvOcDQGiLyaiKLoLeDUGkpPfQkKaimahWwOfgGUcuLaveqcDWObduPr =
    "eKRiX = "
nnUTLnLIujuBNUwLIOWkWRfBJwUWcrGrIawtWSLIShigAikDLGDwKWLmrGcvRaoIUUPcgOaklvOcDQGiLyaiKLoLeDUGkpPfQkKaimahWwOfgGUcuLaveqcDWObduPr =     nnUTLnLIujuBNUwLIOWkWRfBJwUWcrGrIawtWSLIShigAikDLGDwKWLmrGcvRaoIUUPcgOaklvOcDQGiLyaiKLoLeDUGkpPfQkKaimahWwOfgGUcuLaveqcDWObduPr +
 qArcGzUDayYkTOOcTWLZccaLRrsnUkODDkkHOcpTDMaUNzsXrXTnHUTYLCqrOfyGNJkRLUQnMLOQNWUnKOGkMWUTNJYZLiUZfNzHyccKMKwINzNLYNINsrKBWzsDi
nnUTLnLIujuBNUwLIOWkWRfBJwUWcrGrIawtWSLIShigAikDLGDwKWLmrGcvRaoIUUPcgOaklvOcDQGiLyaiKLoLeDUGkpPfQkKaimahWwOfgGUcuLaveqcDWObduPr = nnUTLnLIujuBNUwLIOWkWRfBJwUWcrGrIawtWSLIShigAikDLGDwKWLmrGcvRaoIUUPcgOaklvOcDQGiLyaiKLoLeDUGkpPfQkKaimahWwOfgGUcuLaveqcDWObduPr + "(iNcPxLbcdBdHlsOAcdpbduplKWscQhRhriWZpuxAGtjteLbDKxgbQjArhOoIuccrMKcNHRiJWiuBxLOUbKyUuLcboDKKbzuhLJCTwrTtcOspGRMunLiIoOogKuiencc)"
execute(nnUTLnLIujuBNUwLIOWkWRfBJwUWcrGrIawtWSLIShigAikDLGDwKWLmrGcvRaoIUUPcgOaklvOcDQGiLyaiKLoLeDUGkpPfQkKaimahWwOfgGUcuLaveqcDWObduPr)
End Function
```

The variable Escola will contain the string "Startup".

The next payload is downloaded from http://80[.]76[.]515.]248/afrique.txt, which returns a Base64-encoded string (reversed) that is decoded as a PE file (SHA256: e45d91008eb19ecc3c9e6aab13339bc327c2c61b97215b0d2cc98c23b0db057a). This is an AgenTesla with the following config:

```

{
    "rule": "AgentTeslaV4",
    "family": "agenttesla",
    "credentials": [
        {
            "host": "mail.worlorderbillions.top",
            "port": 587,
            "email_to": "absach@worlorderbillions[.]top",
            "password": “xxxxxxxxxxxxxxxxx”,
            "protocol": "smtp",
            "username": "absach@worlorderbillions[.]top"
        }
    ]
}
```

[1] <https://www.virustotal.com/gui/file/72006dfd34f5b043e6763b16ff8399382e69ad356e8c6b9e71ec908674dab55c>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Addon](/tag.html?tag=Addon) [XLAM](/tag.html?tag=XLAM) [Excel](/tag.html?tag=Excel) [AgentTesla](/tag.html?tag=AgentTesla) [Malware](/tag.html?tag=Malware) [VBS](/tag.html?tag=VBS) [Script](/tag.html?tag=Script)

[0 comment(s)](/diary/More%2BExotic%2BExcel%2BFiles%2BDropping%2BAgentTesla/30150/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/30146)
* [next](/diary/30152)

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