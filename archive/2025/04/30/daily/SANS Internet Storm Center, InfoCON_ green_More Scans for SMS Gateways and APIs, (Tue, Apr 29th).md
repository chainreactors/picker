---
title: More Scans for SMS Gateways and APIs, (Tue, Apr 29th)
url: https://isc.sans.edu/diary/rss/31902
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-30
fetch_date: 2025-10-06T22:07:05.322128
---

# More Scans for SMS Gateways and APIs, (Tue, Apr 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31896)
* [next](/diary/31904)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [More Scans for SMS Gateways and APIs](/forums/diary/More%2BScans%2Bfor%2BSMS%2BGateways%2Band%2BAPIs/31902/)

**Published**: 2025-04-29. **Last Updated**: 2025-04-29 15:25:05 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/More%2BScans%2Bfor%2BSMS%2BGateways%2Band%2BAPIs/31902/#comments)

Last week, I wrote about scans for Teltonika Networks SMS Gateways. Attackers are always looking for cheap (free) ways to send SMS messages and gain access to not-blocklisted numbers. So, I took a closer look at similar scans we have seen.

There are numerous ways to send SMS messages; using a hardware SMS gateway is probably one of the more fancy ways to do so. Most websites use messaging services. For example, we do see scans for SMS plugins for WordPress:

These scans look for style sheet files (.css) that are part of the respective plugins. It is fair to assume that if the respective style sheet is present, the attacker will attempt to obtain access to the site:

> `/wp-content/plugins/sms-alert/css/admin.css
> /wp-content/plugins/mediaburst-email-to-sms/css/clockwork.css
> /wp-content/plugins/verification-sms-targetsms/css/targetvr-style.css
> /wp-content/plugins/wp-sms/assets/css/admin-bar.css
> /wp-content/plugins/textme-sms-integration/css/textme.css
> /wp-content/plugins/sms-alert/css/admin.css`

We also got a few odd, maybe broken, scans like:

> `/api/v1/livechat/sms-incoming/%%target%%/wp-content/themes/twentytwentyone/assets/css/print.css
> /api/v1/livechat/sms-incoming/%%target%%/wp-content/themes/twentytwentyone/assets/js/responsive-embeds.js`

The "%%target%%" part was likely supposed to be replaced with a directory name.

And we have scans for some configuration files that may contain credentials for SMS services like:

> `/twilio/.config/bin/aws/lib/.env
> /twilio-labs/configure-env
> /twillio_creds.php
> /twilio/.secrets
> /sms_config.json
> /sms/actuator/env
> /sms/env`

And many similar URLs.

Scans also look for likely API endpoints used to send SMS messages. I am not sure if they are associated with a particular product or software:

> `/sms/api/
> /api/v1/livechat/sms-incoming/twilio
> /sms.py
> /Sms_Bomber.exe`

SMS\_bomber.exe is a script designed to send mass SMS messages [1]. The scans may attempt to identify copies left behind by other attackers.

SMS\_bomber also suggests the use of a proxy, and we have some scans that are looking for proxies to find websites used to send SMS:

> `https://sms-activate.org`

Not properly securing SMS gateways or credentials used to connect to SMS services could result in significant costs if an attacker abuses the service. It may also make the phone number unusable, as telecom providers and end users will block it. This may also result in reputational damage, and you will likely have to use a different phone number after it has been abused.

[1] https://github.com/iAditya-Nanda/SMS\_Bomber

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [sms](/tag.html?tag=sms)

[0 comment(s)](/diary/More%2BScans%2Bfor%2BSMS%2BGateways%2Band%2BAPIs/31902/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31896)
* [next](/diary/31904)

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