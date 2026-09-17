---
title: Scans Targeting Hospitality Applications, (Wed, Sep 16th)
url: https://isc.sans.edu/diary/rss/33344
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-16
fetch_date: 2026-09-17T06:59:52.316572
---

# Scans Targeting Hospitality Applications, (Wed, Sep 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/33340)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Scans Targeting Hospitality Applications](/forums/diary/Scans%2BTargeting%2BHospitality%2BApplications/33344/)

**Published**: 2026-09-16. **Last Updated**: 2026-09-16 18:44:04 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2BTargeting%2BHospitality%2BApplications/33344/#comments)

Earlier today, I noted an odd request showing up in our "First Seen" report:

```

GET /PIAF-HMS/ HTTP/1.1
Host: [redacted]
User-Agent: Farez-Sorter/1.0
Accept-Encoding: gzip
```

This request is linked to a rather old application, a "PBX in a Flash Hospitality Management System" [1]. The last update, the addition of a license file, happened 10 years ago, and I would consider the project abandoned. However, I also noted a new vulnerability reported a couple of months ago: An SQL injection issue. A quick scan of the code shows many more, and the author does not believe in input validation at all. I am also not seeing any authentication and access control, but I have a suspicion that this code may never have been used, and may be intended more as a lab/experiment to test some Asterix PBX integration. With that, I was about to move on.

However, looking at the somewhat odd user agent, I found a few other similar requests:

> `/admin/
> /admin/config.php
> /ucp/
> /hms/
> /hotel/`

The scans started yesterday and have been continuing today. The only source IP for the scans is [94.102.49.125](/ipinfo.html?ip=94.102.49.125). This IP address is associated with IP Volume ( AS202425), which is often considered a bulletproof hoster. Hotels are often "soft targets" for attackers seeking to steal valuable personal data. In some cases, they have been compromised to launch MitM attacks against guests. The focus on PBX systems is interesting, and maybe there are some tricks that could be played on guests if an attacker can appear to call from "inside" the property.

Please let me know if you have some insight as to what is going on here.

[1] https://github.com/claudiopizzillo/PIAF-HMS

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Scans%2BTargeting%2BHospitality%2BApplications/33344/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33340)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)