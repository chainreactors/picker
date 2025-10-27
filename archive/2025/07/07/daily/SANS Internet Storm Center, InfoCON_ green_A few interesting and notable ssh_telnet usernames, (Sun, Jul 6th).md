---
title: A few interesting and notable ssh/telnet usernames, (Sun, Jul 6th)
url: https://isc.sans.edu/diary/rss/32080
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-07
fetch_date: 2025-10-06T23:26:22.846619
---

# A few interesting and notable ssh/telnet usernames, (Sun, Jul 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32068)
* [next](/diary/32084)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [A few interesting and notable ssh/telnet usernames](/forums/diary/A%2Bfew%2Binteresting%2Band%2Bnotable%2Bsshtelnet%2Busernames/32080/)

**Published**: 2025-07-06. **Last Updated**: 2025-07-06 15:29:31 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/A%2Bfew%2Binteresting%2Band%2Bnotable%2Bsshtelnet%2Busernames/32080/#comments)

Just looked at our telnet/ssh honeypot data, and found some interesting new usernames that  attackers attempted to use:

**"`notachancethisisreal`"**

This username is likely used to detect Cowrie (and other) honeypots. Cowrie is often configured to accept logins randomly. No matter the username/password combination used, the login will succeed every few times. This is supposed to provide the illusion of a more "real" system, not just allowing some common default password, and not allowing each login to succeed. The password used with the username is "`[nopasswordforme73baby](https://isc.sans.edu/ssh_passwords.html?pw=bm9wYXNzd29yZGZvcm1lNzNiYWJ5).`" Likely to pick a password that is highly unlikely to be used in a real system.

Any login that succeeds with this username and password will indicate that the system is a honeypot. So far, we have only had 31 login attempts with this username and password, all on July 1st.

**`"scadaadmin"`**

The name says it: It looks like they are looking for SCADA systems. The password used with this username is "[P@$$W0rd](https://isc.sans.edu/ssh_passwords.html?pw=UEAkJFcwcmQ%3D)". The password has been used "forever" and is popular, but the username is new.

The username appears to be associated with "Rapid SCADA" systems, according to some AI results, but I was not able to confirm this in the manuals. Maybe just a hallucination. However, the default password is either 12345 or blank. They are looking for users who have tried to be more secure. I am not sure how they ended up with P@$$W0rd. They also appear to use "admin" and "12345" as default credentials. It isn't a serious SCADA system if it doesn't have simple default credentials like this.

**`"gpu001", "gpu002"`**

These appear to be common hostnames for network-accessible GPUs, but I wasn't able to confirm that these are actual usernames often used for these systems. But attackers are always out for more GPU/CPU power, so they may just give this a try hoping for the best. There are a few passwords that are used with these usernames, like '7777777', 'gpu001@2025', and '1111111'.

See anything else that is new and interesting? Or have any insight into the three usernames I listed above? Let me know! (see contact link on the left).

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [gpu](/tag.html?tag=gpu) [scada](/tag.html?tag=scada) [ssh](/tag.html?tag=ssh) [telnet](/tag.html?tag=telnet)

[0 comment(s)](/diary/A%2Bfew%2Binteresting%2Band%2Bnotable%2Bsshtelnet%2Busernames/32080/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32068)
* [next](/diary/32084)

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