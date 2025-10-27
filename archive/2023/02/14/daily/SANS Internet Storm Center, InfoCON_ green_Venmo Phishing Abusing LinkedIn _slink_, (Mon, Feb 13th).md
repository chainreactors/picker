---
title: Venmo Phishing Abusing LinkedIn "slink", (Mon, Feb 13th)
url: https://isc.sans.edu/diary/rss/29542
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-14
fetch_date: 2025-10-04T06:33:35.501546
---

# Venmo Phishing Abusing LinkedIn "slink", (Mon, Feb 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29538)
* [next](/diary/29544)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Venmo Phishing Abusing LinkedIn "slink"](/forums/diary/Venmo%2BPhishing%2BAbusing%2BLinkedIn%2Bslink/29542/)

**Published**: 2023-02-13. **Last Updated**: 2023-02-13 17:53:56 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Venmo%2BPhishing%2BAbusing%2BLinkedIn%2Bslink/29542/#comments)

Recently, I have seen more and more phishing for Venmo credentials. Venmo does use SMS messages as a "second factor" to confirm logins from new devices but does not appear to offer additional robust authentication options. The 4-digit SMS PIN and the lack of additional account security may make Venmo users an attractive target.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202023-02-13%20at%2010_57_45%20AM(1).png)

Thanks to Charles for the latest example. The email isn't all that remarkable. It uses the threat of an unauthorized transaction to create urgency and trigger a click. The initial link leads to a valid LinkedIn URL:

> `https[:]//www[.]linkedin[.]com/slink?code=edEeg35T*mwmw918508`

This "trick" to use "slink"s has been documented at least as far back as 2016. LinkedIn last year in reply to an article by Brian Krebs, stated that they police these links for links to known malicious sites. However, the site this link redirects to has been marked malicious by Safe Browsing for at least half a day. You need to be a LinkedIn business customer to use a "slink" with LinkedIn. It is unclear if the attacker used a compromised LinkedIn account or if they set up an account of their own. I did not see a simple way to look up the "owner" of an slink.

The next step leads to a compromised and likely abandoned WordPress site:

> `https://transpfunerario.com/wp-css.php?eaea`

The victim is immediately redirected again to the actual phishing site:

> https[:]//scrtld[.]5e2e9c52158bba90e8ceecf7c-13618[.]sites[.]k-hosting[.]co[.]uk/account/sign-in?key=0762e7ca08a5a93a659bffb6558407d7

k-hosting.co.uk is operated by the low-cost hosting company Krystal.

The phishing, in this case, attempts to capture not just the username and password of the user but also credit card and bank information.

Due to the use of LinkedIn, the Venmo phishing email and link was not flagged as malicious. A user would only be blocked from the imposter's website due to safe browsing blocking the redirect site. LinkedIn and Krystal were notified of the malicious use of their services.

[1] https://krebsonsecurity.com/2022/02/how-phishers-are-slinking-their-links-into-linkedin/
[2] https://www.avanan.com/blog/shortened-linkedin-url-used-for-phishing

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [venmo](/tag.html?tag=venmo) [linkedin](/tag.html?tag=linkedin) [slink](/tag.html?tag=slink)

[0 comment(s)](/diary/Venmo%2BPhishing%2BAbusing%2BLinkedIn%2Bslink/29542/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29538)
* [next](/diary/29544)

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