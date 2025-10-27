---
title: Scans for Moodle Learning Platform Following Recent Update, (Wed, Sep 4th)
url: https://isc.sans.edu/diary/rss/31230
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-05
fetch_date: 2025-10-06T18:35:36.639745
---

# Scans for Moodle Learning Platform Following Recent Update, (Wed, Sep 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31224)
* [next](/diary/31232)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Scans for Moodle Learning Platform Following Recent Update](/forums/diary/Scans%2Bfor%2BMoodle%2BLearning%2BPlatform%2BFollowing%2BRecent%2BUpdate/31230/)

**Published**: 2024-09-04. **Last Updated**: 2024-09-04 14:37:39 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2BMoodle%2BLearning%2BPlatform%2BFollowing%2BRecent%2BUpdate/31230/#comments)

![](https://isc.sans.edu/diaryimages/images/Screenshot%202024-09-04%20at%207_34_11%E2%80%AFAM.png)On August 10th, the popular learning platform "Moodle" released an update fixing [CVE-2024-43425](/vuln.html?cve=2024-43425). RedTeam Pentesting found the vulnerability and published a detailed [blog post](https://blog.redteam-pentesting.de/2024/moodle-rce/) late last week. The blog post demonstrates in detail how a user with the "trainer" role could execute arbitrary code on the server. A trainer would have to publish a "calculated question". These questions are generated dynamically by evaluating a formula. Sadly, the formula was evaluated using PHP's "eval" command. As pointed out by RedTeam Pentesting, "eval" is a very dangerous command to use and should be avoided if at all possible. This applies not only to PHP but to most languages (also see my [video](https://www.youtube.com/watch?v=7QDO3pZbum8) about command injection vulnerabilities). As I usually say: "eval is only one letter away from evil".

The exploit does require the attacker to be able to publish questions. However, Moodle is used by larger organizations like Universities. An attacker may be able to obtain credentials as a "trainer" via brute forcing or credential stuffing.

I got pointed to "Moodle" after seeing this URL in our "First Seen" list of newly accessed URLs:

> `/lib/ajax/service.php?info=tool_mobile_get_public_config&lang=en`

This "public config" may return additional details in some cases, but from my tests with a demo instance of Moodle, it only returns:

> `{"error":"Coding error detected, it must be fixed by a programmer: Invalid json in request: Syntax error","errorcode":"codingerror","stacktrace":null,"debuginfo":null,"reproductionlink":null}`

At least this URL could be used to find Moodle instances and probe them later with more specific exploits. I will have to add this case to our honeypot responses to get more details. These scans are not new, but we had only individual scans (one or two per day) so they never passed our threshold as "significant". Only yesterday did they pass the "line".

But in the meantime:

1. Keep Moodle up to date (they do have a decent chart outlining support timeframes for different versions)
2. Audit the "trainer" accounts, not just because of the vulnerability, but in general, they can cause damage to the system.
3. Let me know if you have additional insight into Moodle. Is there something else that this URL could trigger?

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Scans%2Bfor%2BMoodle%2BLearning%2BPlatform%2BFollowing%2BRecent%2BUpdate/31230/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31224)
* [next](/diary/31232)

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