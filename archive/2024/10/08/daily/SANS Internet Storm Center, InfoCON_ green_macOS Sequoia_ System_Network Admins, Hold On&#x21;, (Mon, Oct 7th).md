---
title: macOS Sequoia: System/Network Admins, Hold On&#x21;, (Mon, Oct 7th)
url: https://isc.sans.edu/diary/rss/31330
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-08
fetch_date: 2025-10-06T18:53:40.490413
---

# macOS Sequoia: System/Network Admins, Hold On&#x21;, (Mon, Oct 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31326)
* [next](/diary/31334)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [macOS Sequoia: System/Network Admins, Hold On!](/forums/diary/macOS%2BSequoia%2BSystemNetwork%2BAdmins%2BHold%2BOn/31330/)

**Published**: 2024-10-07. **Last Updated**: 2024-10-07 15:58:48 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/macOS%2BSequoia%2BSystemNetwork%2BAdmins%2BHold%2BOn/31330/#comments)

It's always tempting to install the latest releases of your preferred software and operating systems. After all, that's the message we pass to our beloved users: "Patch, patch, and patch again!". Last week, I was teaching for SANS and decided to not upgrade my MacBook to macOS 15.0 (Sequoia). Today, I had nothing critical scheduled and made the big jump. Upgrading the operating system is always stressful but everything ran smoothly. So far so good...

Later, I started to do my regular geek tasks and connected to several SSH hosts. After a random amount of time, I noticed the following error for many connections:

```

ssh_dispatch_run_fatal: Connection to x.x.x.x port 22: Connection corrupted
```

This happened multiple times. I started to google for some users' feedback and experiences. It seems to be a problem faced by many people. What I've read:

* It happens randomly
* It affects IPv4 / IPv6
* Not related to an SSH client (term, iTerm2, same)
* People who upgraded to 15.0.1 have less frequent disconnections but the problem is not solved yet
* Some recommendations (worked for some users)
  + Disable the macOS firewall
  + Turn off "Limit IP address tracking
  + Disable private rotating MAC
  + Disable tools like LittleSnitch

There is no "magic recipe" to fix the issue. On my Mac, disabling the address tracking did the job. I've now an SSH session open for 2h+.

Many forums are covering this topic. The most complete one I found is on the Apple support forum[[1](https://discussions.apple.com/thread/255761702?sortBy=rank&page=1)]. In conclusion, if SSH is a critical protocol for you, maybe hold on before upgrading your macOS.

Tip: If you need to SSH to a host, be sure to start your shell in a "screen" (or Byobu, ... ) session[[2](https://ss64.com/bash/screen.html)] to not lose your work.

[1] <https://discussions.apple.com/thread/255761702?sortBy=rank&page=1>
[2] <https://ss64.com/bash/screen.html>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Connection](/tag.html?tag=Connection) [Corrupted](/tag.html?tag=Corrupted) [macOS](/tag.html?tag=macOS) [Sequoia](/tag.html?tag=Sequoia) [SSH](/tag.html?tag=SSH)

[0 comment(s)](/diary/macOS%2BSequoia%2BSystemNetwork%2BAdmins%2BHold%2BOn/31330/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31326)
* [next](/diary/31334)

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