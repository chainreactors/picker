---
title: Getting a Better Handle on International Domain Names and Punycode, (Tue, Aug 26th)
url: https://isc.sans.edu/diary/rss/32234
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-27
fetch_date: 2025-10-07T00:50:06.580307
---

# Getting a Better Handle on International Domain Names and Punycode, (Tue, Aug 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32228)
* [next](/diary/32238)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Getting a Better Handle on International Domain Names and Punycode](/forums/diary/Getting%2Ba%2BBetter%2BHandle%2Bon%2BInternational%2BDomain%2BNames%2Band%2BPunycode/32234/)

**Published**: 2025-08-26. **Last Updated**: 2025-08-26 16:34:11 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Getting%2Ba%2BBetter%2BHandle%2Bon%2BInternational%2BDomain%2BNames%2Band%2BPunycode/32234/#comments)

International domain names (IDN) continue to be an interesting topic. For the most part, they are probably less of an issue than some people make them out to be, given that popular browsers like Google Chrome are pretty selective in displaying them. But on the other hand, they are still used legitimately or not, and keeping a handle on them is interesting.

When analyzing DNS traffic, you should see the Punycode encoding for these domain names. Punycode is defined in [RFC 3492](https://datatracker.ietf.org/doc/html/rfc3492) [1]. Punycode encoded domain names start with "xn--", making identifying them easy.

Several anomalies may happen with Punnycode; luckily, some Python modules can help us identify them.

1 - Invalid Punycode

The Punycode standard is complex, and you may end up with invalid Punycode domains.

2 - Mixed Script

That is the most interesting issue. You are detecting if a domain name mixes different languages. There is no easy way to identify the "language"; instead, we are using the "Script". The Latin script can be used for most European languages. The "Script" identifies a group of languages using the same characters. In Python, the "unicodedata2" module can be used to determine the script of a particular character.

The Python "unicodedata2" module can be used to look up the Unicode name of a character, and the first word in a Unicode name identifies the script the character is a part of. Mixing different scripts in a domain name is suspect as legit international domain names should only use one language.

You can find a quick Python implementation on GitHub: <https://github.com/jullrich/idntest>

[1] <https://datatracker.ietf.org/doc/html/rfc3492>

Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Getting%2Ba%2BBetter%2BHandle%2Bon%2BInternational%2BDomain%2BNames%2Band%2BPunycode/32234/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32228)
* [next](/diary/32238)

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