---
title: Some updates to our data feeds, (Tue, Feb 4th)
url: https://isc.sans.edu/diary/rss/31650
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-05
fetch_date: 2025-10-06T20:37:31.844569
---

# Some updates to our data feeds, (Tue, Feb 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31646)
* [next](/diary/31654)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Some updates to our data feeds](/forums/diary/Some%2Bupdates%2Bto%2Bour%2Bdata%2Bfeeds/31650/)

**Published**: 2025-02-04. **Last Updated**: 2025-02-04 16:01:03 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Some%2Bupdates%2Bto%2Bour%2Bdata%2Bfeeds/31650/#comments)

We have offered several different data feeds via our API or other means. However, we are often not very good at documenting what these feeds are all about. Currently, I am in the process of fixing the [documentation](https://isc.sans.edu/datafeeddocs.html) around these data feeds.

These data feeds are used to augment our data, but may also be helpful to add "color to your logs", which is how I see most of this data being used. Many data feeds do not contain lists of IPs that should be classified as malicious. For example, we attempt to collect IP addresses of public NTP servers. These are usually part of "pool.ntp.org". We are collecting them because they have triggered false positives. Knowing that an IP address is associated with a public NTP server in case you see odd traffic from or to port 123 is helpful.

Just last week, I came across another resource that I found helpful: rosti.bin.re extracts IoCs from various sources like news articles and blog posts. I added this data to our "IP Info" page to provide this useful context in case you are searching for an IP.

The data we produce is published under a "Creative Commons" license. You may use the data for free if you acknowledge the source and do not resell the data. We do not offer commercial licenses, but if you ask nicely and do not play stupid vendor tricks, we will sometimes allow commercial use. Using the data to help you secure your network is always okay, even if the network is commercial. All data is provided "as is" and we are not responsible if you break your network, lose your job, or start a nuclear war by replacing your dead man switch with our API.

So why do we not make these lists simple "blocklists" for your firewall? In my opinion, most of these lists are stupid, and ours would not be any better. I am not able to tell you what IPs you should block. Many of these IPs exploit well-known vulnerabilities. Spend your time fixing the vulnerability. We will never have a list of all IPs exploiting a particular vulnerability, and the list will never be free of false positives. Consume the data responsibly. We are not going to help you waste time or money. If you need help with that, please contact your enterprise security vendor.

We do, however, always like your data :). The best way to say "Thank You" is to run a honeypot and feed us data. We also appreciate feedback and suggestions for other data sources. Please use our [contact page](/contact.html) to provide feedback. We would particularly like to hear how you use our data.

[Initial data feed documentation](/datafeeddocs.html)

[Creative Commons License](https://creativecommons.org/licenses/by-nc-sa/4.0/)

[Documentation for our API](/api)

[Example "IP Info" Page](https://isc.sans.edu/ipinfo/198.199.82.43) (note: you may just enter an IPv4 address into the search box at the top of the page)

I realize the "IP Info" page does not look great. But before you call my baby ugly, send me a suggestion/mockup how to fix it.

![Screen shot of Internet Storm Center IP Info page for 198.199.82.43](https://isc.sans.edu/diaryimages/images/Screenshot%202025-02-04%20at%2010_55_02%E2%80%AFAM.png)---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Some%2Bupdates%2Bto%2Bour%2Bdata%2Bfeeds/31650/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31646)
* [next](/diary/31654)

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