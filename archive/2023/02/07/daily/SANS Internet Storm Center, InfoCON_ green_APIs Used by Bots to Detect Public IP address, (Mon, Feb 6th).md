---
title: APIs Used by Bots to Detect Public IP address, (Mon, Feb 6th)
url: https://isc.sans.edu/diary/rss/29516
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-07
fetch_date: 2025-10-04T05:53:52.447499
---

# APIs Used by Bots to Detect Public IP address, (Mon, Feb 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29512)
* [next](/diary/29518)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [APIs Used by Bots to Detect Public IP address](/forums/diary/APIs%2BUsed%2Bby%2BBots%2Bto%2BDetect%2BPublic%2BIP%2Baddress/29516/)

**Published**: 2023-02-06. **Last Updated**: 2023-02-06 16:22:38 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[7 comment(s)](/diary/APIs%2BUsed%2Bby%2BBots%2Bto%2BDetect%2BPublic%2BIP%2Baddress/29516/#comments)

Many of the bots I am observing attempt to detect the infected system's public ("WAN") IP address. Most of these systems are assumed to be behind NAT. To detect the external IP address, these bots use various public APIs. It may be helpful to detect these requests. Many use unique host names. This will make detecting the request in DNS logs easy even if TLS is not intercepted.

Note that there is useful software using these APIs. Do not just block them. But keeping an eye on who is sending these requests can be useful

Here are a few I remember seeing. The list I have seen isn't very long, making it easy to detect. Let me know if there are others:

* http://ip-api.com/json/
* http://api64.ipify.org
* http://api.ipify.org
* https://ip.seeip.org
* http://checkip.dyndns.org
* https://ipapi.co/ip/

Some of these APIs will block commonly abused user agents like 'curl' or 'pylib.' This will block many of the common bots from using the specific APIs (and they typically do not bother to specify a user agent but instead use a different API without restrictions).

There are some other websites that malware could use with a bit of screen scraping, but I have not seen malware use them. And as you are looking through your logs: Requests for "wanipcn.xml" are not related to looking up the WAN IP address. These requests attempt to exploit an older Realtek SDK vulnerability.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [ip address public wan](/tag.html?tag=ip address public wan)

[7 comment(s)](/diary/APIs%2BUsed%2Bby%2BBots%2Bto%2BDetect%2BPublic%2BIP%2Baddress/29516/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29512)
* [next](/diary/29518)

### Comments

So while you wouldn't block them you would advocate monitoring them. What would be your next step once you identify an internal source?

#### jc

#### Feb 6th 2023 2 years ago

Another DNS name to add to the list:

ip-info.ff.avast.com

Interestingly, CAPE Sandbox has a signature for this: https://www.capesandbox.com/analysis/360850/

#### ibell63

#### Feb 6th 2023 2 years ago

@JC : Nuke the entire site from orbit. It's the only way to be sure.

#### DomDeVitto

#### Feb 6th 2023 2 years ago

One more for the checklist: https://showextip.azurewebsites.net/

#### DomDeVitto

#### Feb 6th 2023 2 years ago

Though I can't think of an example piece of malware using it, I'd imagine a lot of innocent sites coding the client IP into initial responses, eg cookies, or Location: redirects with ?& parameters.

#### DomMcIntyreDeVitto

#### Feb 6th 2023 2 years ago

ifconfig.io is easy to remember and accessing "https://www.google.com/search?q=what+is+my+ip" with curl (no UA string modifications) you will get a 403 HTTP response with your client IP included :)

#### ID

#### Feb 7th 2023 2 years ago

Plain text
https://checkip.amazonaws.com

JSON
https://ipinfo.io

Both work with http:// prefix. On 5G connection the output may differ though, depending on how clever your 5G ISP / MTiM is.

ipinfo.io is even shorter than ifconfig.io, but it would normally require a free or paid subscription. For low volumes of requests it will work without API token

#### Wang Wei

#### Feb 8th 2023 2 years ago

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