---
title: Increasing Searches for ZIP Files, (Thu, Aug 28th)
url: https://isc.sans.edu/diary/rss/32242
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-29
fetch_date: 2025-10-07T00:49:39.519522
---

# Increasing Searches for ZIP Files, (Thu, Aug 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32238)
* [next](/diary/32246)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Increasing Searches for ZIP Files](/forums/diary/Increasing%2BSearches%2Bfor%2BZIP%2BFiles/32242/)

**Published**: 2025-08-28. **Last Updated**: 2025-08-28 14:57:38 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Increasing%2BSearches%2Bfor%2BZIP%2BFiles/32242/#comments)

I noticed recently that we have more and more requests for ZIP files in our web honeypot logs. Over the last year, we have had a substantial increase in these requests.

[![graph showing a substantial inrease in requests ](https://isc.sans.edu/diaryimages/images/Screenshot%202025-08-28%20at%209_37_34%E2%80%AFAM.png)](https://isc.sans.edu/diaryimages/images/Screenshot%202025-08-28%20at%209_37_34%E2%80%AFAM.png)

Here are some of the most common URLs requested so far this year:

| url | c |
| --- | --- |
| /backup.zip | 10977 |
| /web.zip | 9701 |
| /www.zip | 9414 |
| /html.zip | 9361 |
| /data.zip | 9047 |
| /src.zip | 8938 |
| /bin.zip | 8816 |
| /old.zip | 8790 |
| /upload.zip | 8700 |
| /source.zip | 8131 |

The URLs are not specific to any vulnerability. Instead, they are likely filenames selected by administrators for ad-hoc backup files.

And the list of URLs tested is getting longer and longer. Here are some that showed up for the first time today:

| url | firstseen | count |
| --- | --- | --- |
| /modules.zip | 2025-08-26 | 18 |
| /env.production.zip | 2025-08-26 | 16 |
| /cmd.zip | 2025-08-26 | 16 |
| /session\_data.zip | 2025-08-26 | 16 |
| /composer.lock.zip | 2025-08-26 | 16 |
| /pkg.zip | 2025-08-26 | 16 |
| /cloud-config.zip | 2025-08-26 | 15 |
| /ssh\_keys.zip | 2025-08-26 | 15 |
| /hooks.zip | 2025-08-26 | 15 |
| /composer.json.zip | 2025-08-26 | 14 |

Of course, one should never have "random" backup zip files exposed on a web server like this. But we all know it happens. Your best defense is likely to first of all try to prevent downloading of zip files, if that is an option, but adjust the web server configuration. Secondly, you should monitor the document root directories for any rogue zip files.

Ultimately, good change control should be your defense to prevent files like this from being dropped on a web server by either system administrators or developers.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Increasing%2BSearches%2Bfor%2BZIP%2BFiles/32242/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32238)
* [next](/diary/32246)

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