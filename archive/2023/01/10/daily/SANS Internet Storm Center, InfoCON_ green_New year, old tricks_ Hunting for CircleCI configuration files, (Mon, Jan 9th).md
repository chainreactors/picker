---
title: New year, old tricks: Hunting for CircleCI configuration files, (Mon, Jan 9th)
url: https://isc.sans.edu/diary/rss/29416
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-10
fetch_date: 2025-10-04T03:27:35.152964
---

# New year, old tricks: Hunting for CircleCI configuration files, (Mon, Jan 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29412)
* [next](/diary/29420)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [New year, old tricks: Hunting for CircleCI configuration files](/forums/diary/New%2Byear%2Bold%2Btricks%2BHunting%2Bfor%2BCircleCI%2Bconfiguration%2Bfiles/29416/)

**Published**: 2023-01-09. **Last Updated**: 2023-01-09 16:33:54 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/New%2Byear%2Bold%2Btricks%2BHunting%2Bfor%2BCircleCI%2Bconfiguration%2Bfiles/29416/#comments)

I have written before about attackers looking for exposed configuration files. Configuration files often include credentials or other sensitive information.Today, I noticed some scans for a files called "/.circleci/config.yml". Given the recent breach at CircleCI, I dug in a bit deeper.

Spoiler alert: This is not related to the breach. Sometimes organizations lose credentials all by themselves without any third party help.

This configu file is indeed "interesting" if it can be found. For the pre-cloud native people around here: Compare it to a Makefile. It describes how to build a certain project using CircleCI, and it may contain credentials as needed. For example, see the example from https://circleci.com/docs/sample-config/ :

![](https://isc.sans.edu/diaryimages/images/Screenshot%202023-01-09%20at%2011_17_55%20AM.png)

Scans for the file have been ongoing at a low level for a [while now](https://isc.sans.edu/weblogs/urlhistory.html?url=%2F.circleci%2Fconfig.yml)

![](https://isc.sans.edu/diaryimages/images/Screenshot%202023-01-09%20at%2011_22_03%20AM.png)

Including scans for these related URLs:

> /.circleci/ssh-config
> /.circleci/config.yml
> /.circleci/circle.yml
> /config/database.yml.circleci
> /.circleci/

Currently, these 2 IPs are searching for .circleci/config.yml

[139.99.120.65](/ipinfo.html?ip=139.99.120.65) and [139.99.123.180](/ipinfo.html?ip=139.99.123.180) .

Both are located at OVH, a cloud provider known for harboring many compromised systems. But otherwise, the IPs are not very remarkable. The IPs are scanning for various other configuration files and vulnerabilities. For example:

> /wp-config.php.back
> /php\_info.php
> /.env.bak
> /.config
> /config.json
> (42 similar once today alone)

In short: If you leave your configuration files in your document root exposed: They will be found!

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/New%2Byear%2Bold%2Btricks%2BHunting%2Bfor%2BCircleCI%2Bconfiguration%2Bfiles/29416/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29412)
* [next](/diary/29420)

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