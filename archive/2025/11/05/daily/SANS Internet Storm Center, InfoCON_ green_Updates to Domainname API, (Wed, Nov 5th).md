---
title: Updates to Domainname API, (Wed, Nov 5th)
url: https://isc.sans.edu/diary/rss/32452
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-05
fetch_date: 2025-11-06T03:15:34.573856
---

# Updates to Domainname API, (Wed, Nov 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32448)
* [next](/diary/32454)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Updates to Domainname API](/forums/diary/Updates%2Bto%2BDomainname%2BAPI/32452/)

**Published**: 2025-11-05. **Last Updated**: 2025-11-05 16:17:17 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Updates%2Bto%2BDomainname%2BAPI/32452/#comments)

For several years, we have offered a "new domain" list of recently registered (or, more accurately, recently discovered) domains. This list is offered via our API (<https://isc.sans.edu/api>). However, the size of the list has been causing issues, resulting in a "cut-off" list being returned. To resolve this issue, I updated the API call. It is sort of backward compatible, but it will not allow you to retrieve the full list. Additionally, we offer a simple "static file" containing the complete list. This file should be used whenever possible instead of the API.

To retrieve the full list, updated hourly, use:

> <https://isc.sans.edu/feeds/domaindata.json.gz>

We also offer past versions of this list for the last few days. For example:

> <https://isc.sans.edu/feeds/domaindata.2025-11-01.json.gz>

I have not decided yet how long to keep these historic lists. The same data can be retrieved via the API request below. Likely, I will keep the last week as a "precompiled" list.

For the API, you may now retrieve partial copies of the list. The full URL for the API is:

> https://isc.sans.edu/api/recentdomains/[date]/[searchstring]/[start]/[count]

For example:

> https://isc.sans.edu/api/recentdomains/2025-11-05/sans/0/1000?json

Will return all domains found today (November 5th) that contain the string "sans". The first 1,000 matches are returned.

**date**: The date in "YYYY-MM-DD" format. The word "today" can be used instead of the current date if you only want the most recent data. The default is "today".
**searchstring**: only domains containing this string will be returned. Use "+" as a wildcard to get all domains. This defaults to returning any domain.
**start:**The number of the record to start with (defaults to 0)
**count:** How many records to return (defaults to all records)

In return, you will receive XML by default, but you may easily switch to other formats by adding, for example, "?json" to the end of the URL, which will return JSON.

The data returned remains the same:

> `{
>     "domainname": "applewood-artisans.com",
>     "ip": null,
>     "type": null,
>     "firstseen": "2025-11-04",
>     "score": 0,
>     "scorereason": "High entropy: 3.57 (+0.36)"
>   },`

**domainname:** The domain name
**ip**: IPv4 address (if available)
**type**: currently not used
**firstseen**: Date the domain name was first seen
**score**: The "anomaly score"
**scorereason**: reason behind the score

One of the sources of this data is the Certificate Transparency logs. It is possible that we will see new certificates for older domains that have not yet made it into our list of "existing" domains. As a result, you will see some older domains listed as "new" because they were not previously included in our feeds.

Regarding all our data: Use it at your own risk. The data is provided on a best-effort basis at no cost. Commercial use is permitted as long as the data is attributed to us and not resold. We do not recommend using the data as a block list. Instead, use it to "add color to your logs". The data may provide some useful context for other data you collect.

Why do we have a somewhat unusual API, rather than a more standard-compliant REST, GraphQL, or even SOAP API? Well, the API predates these standards (except for SOAP... and do you really want me to use SOAP?). At one point, we may offer something closer to whatever the REST standard will look like at the time, but don't hold your breath; there are a few other projects I want to complete first.

Feedback and bug reports are always welcome.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [api domain names](/tag.html?tag=api domain names)

[0 comment(s)](/diary/Updates%2Bto%2BDomainname%2BAPI/32452/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32448)
* [next](/diary/32454)

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