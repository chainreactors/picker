---
title: New tool: immutable.py, (Sat, Jan 18th)
url: https://isc.sans.edu/diary/rss/31598
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-19
fetch_date: 2025-10-06T20:11:22.317027
---

# New tool: immutable.py, (Sat, Jan 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31596)
* [next](/diary/31600)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

# [New tool: immutable.py](/forums/diary/New%2Btool%2Bimmutablepy/31598/)

**Published**: 2025-01-18. **Last Updated**: 2025-01-18 04:51:13 UTC
**by** [Tools](/handler_list.html#tools) (Version: 1)

[0 comment(s)](/diary/New%2Btool%2Bimmutablepy/31598/#comments)

When performing triage on a Linux system you suspect might be compromised, there are many aspects of the system that you may want to look at. In [SANS FOR577](https://www.sans.org/cyber-security-courses/linux-threat-hunting-incident-response/), we talk about some existing tools and even writing your own bash script to collect triage data. In a case I worked a year or so ago, the attacker installed an LD\_PRELOAD rootkit, which was itself pretty interesting, but one aspect that was a little unusual in this case was that they also set the immutable bit on /etc/ld.so.preload. I've used the find command to find suid and guid binaries and scripts, but it is a bit more of a pain to find files with the immutable bit. So, I wrote by a Python [script](https://raw.githubusercontent.com/clausing/scripts/refs/heads/master/immutable.py) that takes one or more file or directory names and returns the names of any that have the immutable bit. You can also add a switch to search recursively and another to return full path rather than relative (the default). I figured I can't be the only person who ever needed a tool like this, so I've added it to my [GitHub script repo](https://github.com/clausing/scripts).

![](https://isc.sans.edu/diaryimages/images/2025-01-17%2023_34_20-leibnitz-ovpn%20-%20SecureCRT.png)

![](https://isc.sans.edu/diaryimages/images/2025-01-17%2023_33_08-leibnitz-ovpn%20-%20SecureCRT.png)

As with all of my tools/scripts, if you have have questions or suggestions you can e-mail me at my address below or on the handlers list.

References:

<https://www.sans.org/cyber-security-courses/linux-threat-hunting-incident-response/>

<https://raw.githubusercontent.com/clausing/scripts/refs/heads/master/immutable.py>

<https://github.com/clausing/scripts>

---------------
Jim Clausing, GIAC GSE #26
jclausing --at-- isc [dot] sans (dot) edu

Keywords: [tools](/tag.html?tag=tools) [python](/tag.html?tag=python) [linux](/tag.html?tag=linux)

[0 comment(s)](/diary/New%2Btool%2Bimmutablepy/31598/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

* [previous](/diary/31596)
* [next](/diary/31600)

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