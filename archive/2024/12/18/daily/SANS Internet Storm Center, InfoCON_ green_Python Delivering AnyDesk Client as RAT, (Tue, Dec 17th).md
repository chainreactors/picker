---
title: Python Delivering AnyDesk Client as RAT, (Tue, Dec 17th)
url: https://isc.sans.edu/diary/rss/31524
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-18
fetch_date: 2025-10-06T19:45:02.725092
---

# Python Delivering AnyDesk Client as RAT, (Tue, Dec 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31520)
* [next](/diary/31528)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Python Delivering AnyDesk Client as RAT](/forums/diary/Python%2BDelivering%2BAnyDesk%2BClient%2Bas%2BRAT/31524/)

**Published**: 2024-12-17. **Last Updated**: 2024-12-17 07:57:04 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Python%2BDelivering%2BAnyDesk%2BClient%2Bas%2BRAT/31524/#comments)

RATs or “Remote Access Tools” are very popular these days. From an attacker’s point of view, it’s a great way to search and exfiltrate interesting data but also to pivot internally in the network. Besides malicious RATs, they are legit tools that are used in many organisations to perform “remote administration”. Well-known tools are: VNC, TeamViewer, AnyDesk and much more!

Yesterday, I found an interesting piece of Python script that will install AnyDesk[[1](https://anydesk.com/en)] on the victim’s computer. Even better, it reconfigures the tool if it is already installed. The script, called “an5.py” has a low VT score (6/63)[[2](https://www.virustotal.com/gui/file/ef9a19e2b1c1c9d41d6b43ea3836993d004782de86e5b9c9f9b02292e50c904a)]. Note that the script is compatible with Windows and Linux victims.

The script uses the following process to install and opens AnyDesk:

![](https://isc.sans.edu/diaryimages/images/isc-20241217-1.png)

In case of a regular deployment, AnyDesk does not setup an unattended password but it’s technically possible to implement this by adding the following lines in the configuration:

```

ad.anynet.pwd_hash=967adedce518105664c46e21fd4edb02270506a307ea7242fa78c1cf80baec9d
ad.anynet.pwd_salt=351535afd2d98b9a3a0e14905a60a345
ad.anynet.token_salt=e43673a2a77ed68fa6e8074167350f8f
```

If these lines (ad.anynet.\*) already exist in the discovered configuration file, they are overwritten. Otherwise, they are just added.

Once AnyDesk has been installed and reconfigured, it is restarted and victim's details are exfiltrated to the attacker:

![](https://isc.sans.edu/diaryimages/images/isc-20241217-2.png)

The C2 server is hxxp://95[.]164[.]17[.]24:1224 but it seems down at the moment. Why reinvent the wheel if you can use a cool remote access tool?

[1] <https://anydesk.com/en>
[2] <https://www.virustotal.com/gui/file/ef9a19e2b1c1c9d41d6b43ea3836993d004782de86e5b9c9f9b02292e50c904a>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Access](/tag.html?tag=Access) [Malware](/tag.html?tag=Malware) [RAT](/tag.html?tag=RAT) [AnyDesk](/tag.html?tag=AnyDesk) [Python](/tag.html?tag=Python)

[0 comment(s)](/diary/Python%2BDelivering%2BAnyDesk%2BClient%2Bas%2BRAT/31524/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31520)
* [next](/diary/31528)

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