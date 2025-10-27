---
title: Scattered Spider Related Domain Names, (Thu, Jul 31st)
url: https://isc.sans.edu/diary/rss/32162
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-01
fetch_date: 2025-10-07T00:49:46.489228
---

# Scattered Spider Related Domain Names, (Thu, Jul 31st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32158)
* [next](/diary/32166)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Scattered Spider Related Domain Names](/forums/diary/Scattered%2BSpider%2BRelated%2BDomain%2BNames/32162/)

**Published**: 2025-07-31. **Last Updated**: 2025-07-31 17:56:10 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scattered%2BSpider%2BRelated%2BDomain%2BNames/32162/#comments)

This week, CISA updated its advisory on Scattered Spider. Scattered Spider is a threat actor using social engineering tricks to access target networks. The techniques used by Scattered Spider replicate those used by other successful actors, such as Lapsus$. Social engineering does not require a lot of technical tools; creativity is key, and defenses have a hard time keeping up with the techniques used by these threat actors.

For this diary, I want to "zoom in" on one update noted in this week's CISA report. CISA noted that Scattered Spider is using the following domain name patterns:

> targetsname-cms[.]com
> targetsname-helpdesk[.]com
> oktalogin-targetcompany[.]com

Using our "recent domain" API, we can run a quick check on some of these. Let's start by getting the latest (yesterday's) domains:

> `curl -o recent.json 'https://isc.sans.edu/api/recentdomains/?json'`

How many entries do we have so far?

> % jq length recent.json
> 117782

This is low, but not all domain names have been processed yet. Now we will look for the patterns from the CISA report. I first checked "oktalogin", which I figured was the most specific text, but I found nothing. Next, I checked "helpdesk" (I omitted the .com as I figured they may use different TLDs depending on the target):

> `% jq '.[] | select(.domainname | contains ("helpdesk")) | .domainname' recent.json
> "360aihelpdesk.com"
> "ai360helpdesk.com"
> "helpdesk-academy.net"
> "helpdesk-direct.online"
> "helpdesk-guardprotect.com"
> "helpdesk-software-29.online"
> "helpdesk-truist.com"
> "helpdeskmaintenanceinc.online"
> "helpdeskmicrosoft.com"`

We got a few nice domain names here. I highlighted them in red and bold above. Truist appears to be an obvious target. Looking for other domains that contain the word "Truist":

> `% jq '.[] | select(.domainname | contains ("truist")) | .domainname' recent.json
> "altruistonline.shop"
> "cdn-truist.com"
> "helpdesk-truist.com"`

The first one (altruistonline.shop) is likely unrelated. But cdn-truist.com could be interesting. They do not resolve to an IP address. However, the "cdn-" pattern was not in the report, so it may be a new pattern used by Scattered Spiders or similar gangs.

A couple of lessons learned:

* You should monitor for your brand name being used to register new URLs. You can use commercial services, our API as shown above, or what I consider the "secret weapon": TLS transparency logs. Facebook has a nice free one that includes common variations and IDN lookalikes.
* Do not take reports, like CISA's, too literally. They are well-researched, but that comes at the cost of being outdated. Threat actors will also change their MOU after a high-profile report is released. Look for the basic patterns, not the exact strings.

Note the fact that "Truist" is in the list may indicate that they are a target, but does not show that they fell victim to an attack. I do not see any evidence that the domain names have been used so far.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-07-31%20at%201_55_14%E2%80%AFPM.png)

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [scattered spider domains](/tag.html?tag=scattered spider domains)

[0 comment(s)](/diary/Scattered%2BSpider%2BRelated%2BDomain%2BNames/32162/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32158)
* [next](/diary/32166)

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