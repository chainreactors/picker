---
title: Scans for "adminer", (Wed, Mar 18th)
url: https://isc.sans.edu/diary/rss/32808
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-18
fetch_date: 2026-03-19T04:20:58.405059
---

# Scans for "adminer", (Wed, Mar 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32804)
* [next](/diary/32810)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Scans for "adminer"](/forums/diary/Scans%2Bfor%2Badminer/32808/)

**Published**: 2026-03-18. **Last Updated**: 2026-03-18 13:18:24 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2Badminer/32808/#comments)

A very popular target of attackers scanning our honeypots is "phpmyadmin". phpMyAdmin is a script first released in the late 90s, before many security concepts had been discovered. It's rich history of vulnerabilities made it a favorite target. Its alternative, "adminer", began appearing about a decade later (https://www.adminer.org). One of its main "selling" points was simplicity. Adminer is just a single PHP file. It requires no configuration. Copy it to your server, and you are ready to go. "adminer" has a much better security record and claims to prioritize security in its development.

So how does it deal with configurations for database connection parameters? The simple answer: It does not. Instead of using its own authentication or access control, Adminer simply asks the user to enter the SQL username and password they want to use to connect to the database. This is certainly not a terrible idea. Let the database deal with it! SQL databases have robust access controls, so there is no need to reinvent the wheel. Not having to store database credentials in a secrets file also removes several security headaches.

But... these credentials are, of course, still subject to brute-forcing. Adminer thought about that, and only allows 30 login attempts in 30 minutes. One may argue that this is "generous", but they thought about it. The main weakness likely represents users using weak passwords and relying on SQL authentication; there is no easy way to implement two-factor authentication. Adminer mitigates some of these issues with security plugins that implement OTP protection and other security features.

This likely explains why attackers are scanning for it, and they have been scanning quite aggressively lately:

![Graph of adminer scan volume](https://isc.sans.edu/diaryimages/images/Screenshot%202026-03-18%20at%208_56_32%E2%80%AFAM.png)

The increase in the number of URLs scanned is noteworthy. In phpMyAdmin scans, attackers often attempt to find obfuscated URLs used to host phpMyAdmin, such as "/pma/". For Adminer, attackers are scanning for different versions of the file. The filename released by Adminer includes the version number and the language or database type. For example, "adminer-5.4.2-mysql-en.php" is the English version for MySQL.

In short: Do not forget to read the security advice provided by Adminer, and you probably do not want to open Adminer to the internet.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [mysql](/tag.html?tag=mysql) [adminer](/tag.html?tag=adminer) [database](/tag.html?tag=database)

[0 comment(s)](/diary/Scans%2Bfor%2Badminer/32808/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32804)
* [next](/diary/32810)

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