---
title: Securing Firebase: Lessons Re-Learned from the Tea Breach, (Wed, Jul 30th)
url: https://isc.sans.edu/diary/rss/32158
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-31
fetch_date: 2025-10-06T23:53:32.139405
---

# Securing Firebase: Lessons Re-Learned from the Tea Breach, (Wed, Jul 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32154)
* [next](/diary/32162)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Securing Firebase: Lessons Re-Learned from the Tea Breach](/forums/diary/Securing%2BFirebase%2BLessons%2BReLearned%2Bfrom%2Bthe%2BTea%2BBreach/32158/)

**Published**: 2025-07-30. **Last Updated**: 2025-07-30 20:19:26 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Securing%2BFirebase%2BLessons%2BReLearned%2Bfrom%2Bthe%2BTea%2BBreach/32158/#comments)

Today we are trying something a bit different (again). Brandon Evans, senior instructor with SANS, contributed the video below, talking a bit about the breach of the Tea App, and how to prevent and detect this vulnerability.

Firebase is a very popular database developed by Google. It easily ties in with modern web and mobile applications. Sadly, as so often, it comes with some configuration challenges out of the box.

As a traditional ("old school") web developer, it would have never crossed my mind to allow users to connect directly to my backend database. But modern tools like Firebase often encourage just that. All security controls must now reside in the database itself, and many modern, in particular "NoSQL" databases, are lacking the fine-grained access control rules we learned to love in traditional SQL databases. This leads to applications that may implement detailed access control rules, but they become meaningless once the user connects directly to the database, bypassing any application-specific controls. Flawed applications often rely on client-based access control "tricks" that are easily bypassed.

Sadly, this is not just a vibe-coding issue. Developers have been able to code defective applications without the help of AI, and this is not only a bad, but also a sad, pattern found in many modern applications using tools like Firebase.

Fixing this issue is not necessarily hard. Start by implementing strong Firebase rules, or avoid these tools in favor of backend data stores with stronger access controls out of the box. If you do rely on specific strong configurations, make sure they are verified as part of your CI/CD pipeline. And as always, lock down your cloud configuration. Firebase does inherit GCP IAM policies.

More details from Brandon Evans are in the video below.

You can reach Brandon at bevans-at-sans.org or check out his classes at <https://sans.org/brandonevans>

![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-07-30%20at%203_51_52%E2%80%AFPM.png)

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [firebase](/tag.html?tag=firebase) [tea](/tag.html?tag=tea)

[0 comment(s)](/diary/Securing%2BFirebase%2BLessons%2BReLearned%2Bfrom%2Bthe%2BTea%2BBreach/32158/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32154)
* [next](/diary/32162)

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