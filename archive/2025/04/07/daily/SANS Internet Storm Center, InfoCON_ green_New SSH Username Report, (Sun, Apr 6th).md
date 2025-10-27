---
title: New SSH Username Report, (Sun, Apr 6th)
url: https://isc.sans.edu/diary/rss/31830
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-07
fetch_date: 2025-10-06T22:04:42.462967
---

# New SSH Username Report, (Sun, Apr 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31824)
* [next](/diary/31834)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [New SSH Username Report](/forums/diary/New%2BSSH%2BUsername%2BReport/31830/)

**Published**: 2025-04-06. **Last Updated**: 2025-04-06 19:52:07 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/New%2BSSH%2BUsername%2BReport/31830/#comments)

As you may have noticed by some of my recent diaries, I have spent a bit more time on ssh and telnet credentials. These credentials are collected by Cowrie, the amazing full features SSH and Telnet honeypot maintained by Michel Oosterhof. Cowrie is installed as a component if you install our DShield honeypot.

One very simple way to find "interesting" things is to look at what is new. To allow you to explore yourself, I added an "[SSH/Telnet Username Summary](https://isc.sans.edu/data/allsshusernames.html)". The report lists all usernames we observed in the last 30 days, and if we saw them at least five times. These numbers may, of course, change. There is also a simple JSON formatted report you may download to play with: <https://isc.sans.edu/sshallusernames.json>

So let's take a quick look at "what's new":

* ysoperator: Looks familiar, but can't remember where I saw it. Google is of little help here.
* uery: Maybe a typo, and should be "query"?
* tamatiek: Appears to be a Japanese name?
* shughes: I guess this is for "S Hughes". Many systems use the first initial and last name as username. There are a few more like that that I will skip here
* dbmasteruser: Something a bit more interesting. Likely supposed to refer to a database administrator account.

And there is one I think was funny: /usr/share/wordlists/logins.txt . Yes, the filename and path. I suspect the user didn't know yet how to run the brute force script and passed the filename instead of the username. There are a few I consider typos: "atascientist" (I suspect "datascientist"), "ackupadmin" (backupadmin?). Could also be a tool that swallows the first letter of the username if the username is not provided correctly.

I am working on a similar list of passwords. But there are a lot more different passwords than usernames making that a bit more challenging. Let me know if there are any additional details I should add.

Lesson: Attackers make mistakes too, and there are no real "safe" usernames.

![List of recently seen "new" usernames](https://isc.sans.edu/diaryimages/images/Screenshot%202025-04-06%20at%203_49_50%E2%80%AFPM.png)

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [report](/tag.html?tag=report) [username](/tag.html?tag=username) [telnet](/tag.html?tag=telnet) [ssh](/tag.html?tag=ssh)

[0 comment(s)](/diary/New%2BSSH%2BUsername%2BReport/31830/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31824)
* [next](/diary/31834)

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