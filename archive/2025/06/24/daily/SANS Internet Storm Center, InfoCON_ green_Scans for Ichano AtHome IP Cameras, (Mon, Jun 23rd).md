---
title: Scans for Ichano AtHome IP Cameras, (Mon, Jun 23rd)
url: https://isc.sans.edu/diary/rss/32062
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-24
fetch_date: 2025-10-06T22:55:23.823611
---

# Scans for Ichano AtHome IP Cameras, (Mon, Jun 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32058)
* [next](/diary/32068)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Scans for Ichano AtHome IP Cameras](/forums/diary/Scans%2Bfor%2BIchano%2BAtHome%2BIP%2BCameras/32062/)

**Published**: 2025-06-23. **Last Updated**: 2025-06-23 15:33:55 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2BIchano%2BAtHome%2BIP%2BCameras/32062/#comments)

![athome camera logo](https://isc.sans.edu/diaryimages/images/Screenshot%202025-06-23%20at%205_18_09%E2%80%AFPM.png)Ichano's "AtHome Camera" is a bit of a different approach to home surveillance cameras [1]. Instead of a hardware camera solution, this product is a software solution that turns existing devices like computers and tablets into webcams. The software implements features we know from similar IP camera devices. It enabled streaming of images and remote access to features like motion detection and alerting.

Back in 2017, a hard-coded username and password vulnerability was identified in the product (CVE-2017-17761) [2]. It is kind of odd that it took so long for this username to show up in scans against our honeypots, but I noticed it on June 18th. The password attempted is "123", as outlined in CVE-2017-17761. It is not clear if this issue was ever fixed by Ichano.

IP addresses scanning for this username and password combination are also scanning for other typical "IoT" default usernames and passwords, with usernames like "root", "admin", "gast", "gpon" and others.

Some of the IP addresses actively scanning:

104.155.29.102,  Google Cloud, US
110.233.163.181, Biglobe, Japan
110.233.163.180, Biglobe, Japan
123.210.143.28,  Telstra, Australia
139.135.69.203,  DITO TELECOMMUNITY, Philippines
153.237.47.226,  Open Computer Network, Japan
178.242.192.55,  TURKCELL, Turkey
185.248.13.240,  ATLANTISNET, Turkey
220.107.154.153  Open Computer Network, Japan

Nothing specifically special or exciting about these IPs as far as I can tell.

[1] https://www.ichano.com/
[2] https://www.exploit-db.com/exploits/44048

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Scans%2Bfor%2BIchano%2BAtHome%2BIP%2BCameras/32062/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32058)
* [next](/diary/32068)

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