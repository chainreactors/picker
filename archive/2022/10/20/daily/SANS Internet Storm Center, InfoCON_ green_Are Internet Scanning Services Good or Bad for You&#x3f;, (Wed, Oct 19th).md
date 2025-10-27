---
title: Are Internet Scanning Services Good or Bad for You&#x3f;, (Wed, Oct 19th)
url: https://isc.sans.edu/diary/rss/29164
source: SANS Internet Storm Center, InfoCON: green
date: 2022-10-20
fetch_date: 2025-10-03T20:25:25.600961
---

# Are Internet Scanning Services Good or Bad for You&#x3f;, (Wed, Oct 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29160)
* [next](/diary/29168)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Are Internet Scanning Services Good or Bad for You?](/forums/diary/Are%2BInternet%2BScanning%2BServices%2BGood%2Bor%2BBad%2Bfor%2BYou/29164/)

**Published**: 2022-10-19. **Last Updated**: 2022-10-19 12:12:13 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Are%2BInternet%2BScanning%2BServices%2BGood%2Bor%2BBad%2Bfor%2BYou/29164/#comments)

I'm in Luxembourg to attend the first edition of the CTI Summit[[1](https://cti-summit.org/)]. There was an interesting keynote performed by Patrice Auffret[[2](https://twitter.com/patriceauffret)], the founder of Onyphe, about "Ethical Internet Scanning in 2022". They are plenty of online scanners that work 24x7 to build a map of the Internet. They scan the entire IP addresses space and look for interesting devices, vulnerabilities, etc. Big players are Shodan, Onyphe, Censys, ZoomEye, etc.

Today, scanning is accepted by most network owners and, if you don't agree to be scanned, you've no alternative and have to live with. Welcome to the wild Internet! Personal opinion, if you are still taking care of such scans in 2022, you are putting resources on the wrong threat. Of course, there is a difference between a "simple" scan against your public IP addresses and a complete scan of your web applications (that may reveal an upcoming attack).

If we have to live with this services, they must have an ethic and respect some rules like:

* Explain the purpose of the scanner on the website
* Allow to an opt-out ("don't scan me anymore)
* Provide abuse contacts
* Provides lists of IP addresses used to scan
* Implement good & relevant reverse DNS records
* Handle abuse requests
* Don’t fuzz, just use standard packets/protocols
* Scan slowly (no DoS)
* Use fixed IP addresses (no trashable ones)
* Remove collected data upon request

The question that arises is: "To scan or not to scan?". Are these scanners useful? The response is "yes". They help to have a better overview of the Internet and, by example, how many devices are affected by a specific specific vulnerability. You must also know that attackers will, anyway, scan you. Why not take some advantages and also use these scanners? Buy an account, use the provided REST API and query information about your domains and our IP addresses. This will give you a better visibility about your footprint ("what you're exposing on the Internet").

If you're interested in detecting these scanners, we provide you a feed with interesting information[[3](https://isc.sans.edu/api/threatcategory/research/)].

[1] [https://cti-summit.org](https://cti-summit.org/)
[2] <https://twitter.com/patriceauffret>
[3] <https://isc.sans.edu/api/threatcategory/research/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Scanner](/tag.html?tag=Scanner) [Onyphe](/tag.html?tag=Onyphe) [Port scan](/tag.html?tag=Port scan) [Internet](/tag.html?tag=Internet) [Scan](/tag.html?tag=Scan) [Shodan](/tag.html?tag=Shodan)

[0 comment(s)](/diary/Are%2BInternet%2BScanning%2BServices%2BGood%2Bor%2BBad%2Bfor%2BYou/29164/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29160)
* [next](/diary/29168)

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