---
title: Security related Docker containers, (Wed, Oct 2nd)
url: https://isc.sans.edu/diary/rss/31318
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-03
fetch_date: 2025-10-06T18:55:34.231627
---

# Security related Docker containers, (Wed, Oct 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31314)
* [next](/diary/31320)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

# [Security related Docker containers](/forums/diary/Security%2Brelated%2BDocker%2Bcontainers/31318/)

**Published**: 2024-10-02. **Last Updated**: 2024-10-02 18:03:00 UTC
**by** [Jim Clausing](/handler_list.html#jim-clausing) (Version: 1)

[0 comment(s)](/diary/Security%2Brelated%2BDocker%2Bcontainers/31318/#comments)

Over the last 9 months or so, I've been putting together some docker containers that I find useful in my day-to-day malware analysis and forensicating. I have been putting them up on [hub.docker.com](https://hub.docker.com) and decided, I might as well let others know they were there. In a couple of cases, I just found it easier to create a docker container than try to remember to switch in and out of a Python virtualenv. In a couple of other cases, it avoids issues I've had with conflicting version of installed packages. In every case, I'm tracking new releases so I can update my containers when new releases come out and I usually do so within a couple of days of the new release. The ones that I have up at the moment are the following:

[clausing/flare-floss](https://hub.docker.com/repository/docker/clausing/flare-floss/general)

[clausing/capa](https://hub.docker.com/repository/docker/clausing/capa/general)

[clausing/hayabusa](https://hub.docker.com/repository/docker/clausing/hayabusa/general)

[clausing/takajo](https://hub.docker.com/repository/docker/clausing/takajo/general)

[clausing/chainsaw](https://hub.docker.com/repository/docker/clausing/chainsaw/general)

[clausing/yara](https://hub.docker.com/repository/docker/clausing/yara/general)

[clausing/uac](https://hub.docker.com/repository/docker/clausing/uac/general)

[clausing/dfir-unfurl](https://hub.docker.com/repository/docker/clausing/chainsaw/general)

The USAGE portion of each page should give enough info on how to run thems (and what directories to map into the container). Hopefully, some of the rest of you will find these useful.

---------------
Jim Clausing, GIAC GSE #26
jclausing --at-- isc [dot] sans (dot) edu

Keywords: [docker](/tag.html?tag=docker)

[0 comment(s)](/diary/Security%2Brelated%2BDocker%2Bcontainers/31318/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Malware Analysis Tools and Techniques](https://www.sans.org/event/tokyo-autumn-2025/course/reverse-engineering-malware-malware-analysis-tools-techniques) | Online | Japan Standard Time | Oct 20th - Oct 25th 2025 |

* [previous](/diary/31314)
* [next](/diary/31320)

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