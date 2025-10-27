---
title: Why is My Cat Using Baidu&#x3f; And Other IoT DNS Oddities, (Wed, Oct 26th)
url: https://isc.sans.edu/diary/rss/29188
source: SANS Internet Storm Center, InfoCON: green
date: 2022-10-27
fetch_date: 2025-10-03T21:04:31.194155
---

# Why is My Cat Using Baidu&#x3f; And Other IoT DNS Oddities, (Wed, Oct 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29182)
* [next](/diary/29192)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Why is My Cat Using Baidu? And Other IoT DNS Oddities](/forums/diary/Why%2Bis%2BMy%2BCat%2BUsing%2BBaidu%2BAnd%2BOther%2BIoT%2BDNS%2BOddities/29188/)

**Published**: 2022-10-26. **Last Updated**: 2022-10-26 13:09:23 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/Why%2Bis%2BMy%2BCat%2BUsing%2BBaidu%2BAnd%2BOther%2BIoT%2BDNS%2BOddities/29188/#comments)

![image of beautiful cat.](https://isc.sans.edu/diaryimages/images/IMG_0873.jpeg)My cat, Gluon, is having a problem. Last year, a new cat, Einstein, invaded her property, and since then, she has no longer ventured outside after some unfortunate encounters with Einstein. Gluon now spends most of her time inside doing cat stuff like grooming and sleeping; unfortunately, she has gained an unhealthy amount of weight. To help, we got her an automated cat feeder to better control her food intake. The cat feeder is sporting not just the obligatory WiFi and Cloud/App connectivity but also a camera, so it was immediately moved to our "IoT" network.

The IoT network is pretty much locked down and closely monitored. So I soon noticed these DNS queries originating from the cat feeder:

> `0    catfeeder → dnsserver    DNS 73 Standard query 0x0002 A baidu.com
> 301    catfeeder → dnsserver    DNS 73 Standard query 0x0002 A baidu.com
> 602    catfeeder → dnsserver    DNS 73 Standard query 0x0002 A baidu.com`

About every 5 minutes (300 seconds), the cat feeder attempts to resolve "baidu.com." Why baidu.com? What is my cat trying to search for?

After investigating this on different devices showing similar behavior, I finally figured out that some networking libraries use "baidu.com" for internet connectivity checks. Even if the DNS lookup succeeds, there is no actual outbound connection in this case. The device is happy as long as an IP address is returned.

But why baidu.com and not google.com or '8.8.8.8' (or bing.com)? This is likely due to these devices and some libraries manufactured and coded in China. First of all, "Baidu" is more commonly used than "Google", and due to the censorship regime, which may not only block DNS lookups for Google but may also use these DNS lookups to identify non-regime-conform behavior not to get Chinese users into trouble, they may opt for the use of Baidu which works fine globally.

There is another interesting issue with these DNS queries. Let's look at the DNS query IDs:

> `% tshark -nr sessions.pcap -T fields -e 'dns.id' | sort -u
> 0x0002`

So all the queries use the same query id (I have also seen "1" and "3"). This is a known issue with many IoT devices using specific networking libraries. For example, the uClibc and uClibc-ng libraries were recently found to have vulnerabilities like this.

As for the cat feeder, I haven't been able to verify which library it uses, and it does have; however, an open telnet server to be compliant with the minimum number of vulnerability rules for IoT devices. Not sure if anybody has an idea what the username or password would be. The login prompt:

> `ipc login:`

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[2 comment(s)](/diary/Why%2Bis%2BMy%2BCat%2BUsing%2BBaidu%2BAnd%2BOther%2BIoT%2BDNS%2BOddities/29188/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29182)
* [next](/diary/29192)

### Comments

Sounds like your cat could be hunting for RATs.

#### Mace

#### Oct 26th 2022 2 years ago

very cute cat

#### for fun

#### Oct 29th 2022 2 years ago

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