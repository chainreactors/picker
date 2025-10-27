---
title: Ancient TP-Link Backdoor Discovered by Attackers, (Sun, Nov 17th)
url: https://isc.sans.edu/diary/rss/31442
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-18
fetch_date: 2025-10-06T19:15:20.786548
---

# Ancient TP-Link Backdoor Discovered by Attackers, (Sun, Nov 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31438)
* [next](/diary/31446)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Ancient TP-Link Backdoor Discovered by Attackers](/forums/diary/Ancient%2BTPLink%2BBackdoor%2BDiscovered%2Bby%2BAttackers/31442/)

**Published**: 2024-11-17. **Last Updated**: 2024-11-17 07:07:48 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Ancient%2BTPLink%2BBackdoor%2BDiscovered%2Bby%2BAttackers/31442/#comments)

There are so many vulnerabilities in commonly used routers that attackers often leave many easily exploited vulnerabilities untouched, as they already have plenty of vulnerabilities to exploit.

Looking today at our "[First Seen URL](https://isc.sans.edu/weblogs/firstseenurls.html)" page, I noticed this odd URL:

> `/userRpmNatDebugRpm26525557/start_art.html`

The URL is very "specific" in including a number, and at first, I suspected a web shell placed by an attacker. But turns out, this backdoor comes (came?) preinstalled in many TP-Link routers.

One reason that this has not been exploited more so far is likely the fact that the original discovery was published in a bit an obscure place [https://sekurak.pl/tp-link-httptftp-backdoor/] and didn't include a lot of details, other than run-through showing how to exploit the vulnerability.

The issue was originally discovered over ten years ago. It is not clear if it was ever patched. The discoverer of the vulnerability does indicate that they (after some false starts) made contact with TP-Link. There appears to be no CVE number assigned to the vulnerability.

Another reason this backdoor is a bit more difficult to exploit than other vulnerabilities is the need for a TFTP server. As explained in the blog post above, sending a request to the URL initiates a tftp request from the router to the IP address sending the request. The tftp request will retrieve a file, "nart.out". The file will alter be executed.

I just hope TP-Link has fixed the issue after 12 years, and vulnerable routers are either no longer operational after such a long time or have been patched (or at least secured to the point that the admin web page is not accessible from the internet).

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [backdoor](/tag.html?tag=backdoor) [tplink](/tag.html?tag=tplink)

[1 comment(s)](/diary/Ancient%2BTPLink%2BBackdoor%2BDiscovered%2Bby%2BAttackers/31442/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31438)
* [next](/diary/31446)

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