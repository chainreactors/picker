---
title: Show me All Your Windows&#x21;, (Fri, Aug 11th)
url: https://isc.sans.edu/diary/rss/30116
source: SANS Internet Storm Center, InfoCON: green
date: 2023-08-12
fetch_date: 2025-10-04T12:02:40.280308
---

# Show me All Your Windows&#x21;, (Fri, Aug 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30112)
* [next](/diary/30118)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Show me All Your Windows!](/forums/diary/Show%2Bme%2BAll%2BYour%2BWindows/30116/)

**Published**: 2023-08-11. **Last Updated**: 2023-08-11 08:55:40 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Show%2Bme%2BAll%2BYour%2BWindows/30116/#comments)

It's a key point for attackers to implement anti-debugging and anti-analysis techniques. Anti-debugging means the malware will try to detect if it's being debugged (executed in a debugger or its execution is slower than expected). Anti-analysis refers to techniques to detect if the malware is detonated in a sandbox or by a malware analyst. In such cases, tools run in parallel with the malware to collect live data (packets, API calls, files, or registry activity).

The Microsoft API set is fantastic because it contains many helpful API calls for attackers. Today I found a malicious Python script that (ab)uses one of them: GetWindowText()[[1](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowtexta)]. This API call is very powerful when used in combination with EnumWindows()[[2](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-enumwindows)]. EnumWindows() will list all top-level windows opened on the screen and pass the handle to each window to a callback function that will check the window title via GetWindowText().

That's what has been implemented in the Python script:

![](https://isc.sans.edu/diaryimages/images/isc-20230811-1.png)

The script used the ctype library to use Windows API calls. EnumWindows() is called in a loop; for each window found, the callback function winEnumHandler() is called. The window title is extracted and compared to a nice list of well-known tools used by malware analysts.

The malware will not silently exit if a suspicious window is found. Instead, it will link the process to the window and try to kill it using GetWindowThreatProcessId()[[3](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid)]!

Another good example of API calls group that reveals a specific technique used by attackers! The script (SHA256:c8a5262e89751f231060a6740447062e34c5393a17f67d0c4eb52c7f911f3bd2) has a VT score of 6/60[[4](https://www.virustotal.com/gui/file/c8a5262e89751f231060a6740447062e34c5393a17f67d0c4eb52c7f911f3bd2)].

[1] <https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowtexta>
[2] <https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-enumwindows>
[3] <https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid>
[4] <https://www.virustotal.com/gui/file/c8a5262e89751f231060a6740447062e34c5393a17f67d0c4eb52c7f911f3bd2>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [GetWindowTitle](/tag.html?tag=GetWindowTitle) [Python](/tag.html?tag=Python) [Window](/tag.html?tag=Window) [Enumeration](/tag.html?tag=Enumeration)

[0 comment(s)](/diary/Show%2Bme%2BAll%2BYour%2BWindows/30116/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/30112)
* [next](/diary/30118)

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