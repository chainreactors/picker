---
title: Mirai Botnet and Gafgyt DDoS Team Up Against SOHO Routers., (Tue, Dec 6th)
url: https://isc.sans.edu/diary/rss/29304
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-07
fetch_date: 2025-10-04T00:43:10.793901
---

# Mirai Botnet and Gafgyt DDoS Team Up Against SOHO Routers., (Tue, Dec 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29300)
* [next](/diary/29314)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Mirai Botnet and Gafgyt DDoS Team Up Against SOHO Routers.](/forums/diary/Mirai%2BBotnet%2Band%2BGafgyt%2BDDoS%2BTeam%2BUp%2BAgainst%2BSOHO%2BRouters/29304/)

**Published**: 2022-12-06. **Last Updated**: 2022-12-06 15:42:01 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Mirai%2BBotnet%2Band%2BGafgyt%2BDDoS%2BTeam%2BUp%2BAgainst%2BSOHO%2BRouters/29304/#comments)

[This is a guest post submitted by Brock Perry [[LinkedIn](https://www.linkedin.com/in/bperry-otsec/)], one of our [sans.edu](http://sans.edu) undergraduate interns]

Since 2014, self-replicating variants of DDoS attacks against routers and Linux-based IoT devices have been rampant. Gafgyt botnets target vulnerable IoT devices and use them to launch large-scale distributed denial-of-service attacks. SOHO and IoT devices are ubiquitous, less likely to have secure configurations or routine patches, and more likely to be at the internet edge. Attacks against these devices are less likely to be identified by enterprise monitoring techniques, and compromise may go unnoticed. Unwitting users then become part of attack propagation.

![](https://isc.sans.edu/diaryimages/images/63qWGpqSFlwms8.png)

An attack on Sept 19th, 2022, followed this familiar pattern, seeking to exploit known vulnerabilities in devices from multiple vendors - including D-Link, eir, Huawei, Netgear, TP-Link, and routers using Realtek SDK.

### Connection

An attacker or compromised device made numerous attempts to connect to the target with weak ssh credentials before eventually authenticating.

![](https://isc.sans.edu/diaryimages/images/orMGY-cf0LeHST.png)

![](https://isc.sans.edu/diaryimages/images/gjNYqI6DxqcLyV.png)

### Payload Drop

Upon authenticating, the attack downloads and executes the xd.86 payload.

![](https://isc.sans.edu/diaryimages/images/ApWyBesipnkQau.png)

### Bot

The xd.86 botnet component searches out new targets. In the first 15 seconds, 1018 connection attempts are made to 115 unique addresses from an otherwise quiet system.

![](https://isc.sans.edu/diaryimages/images/dNwoRIckKBEcnD.png)
*Outbound Connection Attempts*

*![](https://isc.sans.edu/diaryimages/images/kl_YeZJA-SpO93.png)*

*Unique Destinations*

Destination ports reveal connections to standard HTTP ports and well-known ports used by Huawei (32715) and Oracle (7574).

![](https://isc.sans.edu/diaryimages/images/CkmlEEEmaheGdI.png)

### Compromise

![](https://isc.sans.edu/diaryimages/images/MR3rnELsY6Ljen.png)

Eleven attacks are apparent based on the strings from xd.86. When vulnerable devices are discovered, and authentication is successful, one of these 11 actions is carried out to propagate the attack further.

### Sources

[1] - [Attack Source - VirusTotal](https://www.virustotal.com/gui/ip-address/79.110.62.213/relations)
[2] - [Payload Source - Virus Total](https://www.virustotal.com/gui/ip-address/79.110.62.227/relations)
[3] - [Main Payload Reputation - Virus Total](https://www.virustotal.com/gui/file/d47eaac87456ac5929363eee7cffc57540f6130539967dd5cdaf0ddca04e1e94) - d47eaac87456ac5929363eee7cffc57540f6130539967dd5cdaf0ddca04e1e94
[4] - Secondary Payloads
[lol.sh](https://www.virustotal.com/gui/file/f0d12efb246fac3a93f2cab32924e202eddbe92e7d80ba8be3219f5aadf0551e) - f0d12efb246fac3a93f2cab32924e202eddbe92e7d80ba8be3219f5aadf0551e
[xd.mips](https://www.virustotal.com/gui/file/19e9baefa16cef3bede1d8b58992fe2e3d857c4fd38a102bf06c577a25502d60/details) - 19e9baefa16cef3bede1d8b58992fe2e3d857c4fd38a102bf06c577a25502d60
[xd.arm7](https://www.virustotal.com/gui/file/9069ff0e1c75cae1f7b2db10c244004c84791f4f81eb4c11ee53b7b07fa06f96/details) - 9069ff0e1c75cae1f7b2db10c244004c84791f4f81eb4c11ee53b7b07fa06f96
[5] - [Bot with Strings in Common](https://github.com/AlmDev/Xenon/blob/master/main.c)

Keywords:

[0 comment(s)](/diary/Mirai%2BBotnet%2Band%2BGafgyt%2BDDoS%2BTeam%2BUp%2BAgainst%2BSOHO%2BRouters/29304/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29300)
* [next](/diary/29314)

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