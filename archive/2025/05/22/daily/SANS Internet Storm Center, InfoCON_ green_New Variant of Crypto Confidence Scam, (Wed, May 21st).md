---
title: New Variant of Crypto Confidence Scam, (Wed, May 21st)
url: https://isc.sans.edu/diary/rss/31968
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-22
fetch_date: 2025-10-06T22:31:59.913682
---

# New Variant of Crypto Confidence Scam, (Wed, May 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31964)
* [next](/diary/31972)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [New Variant of Crypto Confidence Scam](/forums/diary/New%2BVariant%2Bof%2BCrypto%2BConfidence%2BScam/31968/)

**Published**: 2025-05-21. **Last Updated**: 2025-05-21 15:26:09 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[4 comment(s)](/diary/New%2BVariant%2Bof%2BCrypto%2BConfidence%2BScam/31968/#comments)

In February, we had a few diaries about crypto wallet scams. We saw these scams use YouTube comments, but they happened via other platforms and messaging systems, not just YouTube [1]. The scam was a bit convoluted: The scammer posted the secret key to their crypto wallet. Usually, this would put their crypto wallet at risk of being emptied. But the wallet they used came with a twist: A second key was required. The scammer counted on the victim paying the transaction fee, which the scammer would receive, before attempting to withdraw the funds.

This is a classic "confidence scheme" or "advance fee" scheme. The victim believes they are scamming the attacker out of their money. Instead, they are being robbed. These types of scams are amazingly successful in real life and online. They rely on greedy victims attempting to get something for free (or cheap).

I recently started seeing a new variation of this scam, this time mostly via X direct messages:

![screen shot of direct message showing account credentials.](https://isc.sans.edu/diaryimages/images/Screenshot%202025-05-21%20at%2010_59_43%E2%80%AFAM.png)

Just like before, the attacker is offering access to their crypto account. The victim is enticed to log in to the account, and there is indeed a substantial amount in this account:

![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-05-21%20at%2011_01_41%E2%80%AFAM.png)

Next, I, of course, want to transfer the money! But this is where the problem starts. To transfer any money from the wallet, I must provide a "KEY." I do not have that key :(. But there is a solution! I could register an account!

![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-05-21%20at%2011_14_24%E2%80%AFAM.png)

I went to register an account and now attempted to "transfer" the tokens instead of "withdrawing" them. This is where the next snag hits: You must be a "VIP" member of the site, which isn't cheap!

![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-05-21%20at%2011_16_04%E2%80%AFAM.png)

The minimum fee of $50 was more than I wanted to throw away on an obvious scam.

I suspect that, in this case, whoever runs this site (aeiang.com) is the one receiving the money. Overall, I find these scams quite over-complicated. But maybe all this filters victims for those who are greedy enough to fall for this scam. The website does not state who is behind it and uses a generic GMail address for customer support ([[email protected]](/cdn-cgi/l/email-protection)).

[1] https://isc.sans.edu/diary/Crypto+Wallet+Scam/31646
[2] https://isc.sans.edu/diary/Crypto+Wallet+Scam+Not+For+Free/31666

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [crypto](/tag.html?tag=crypto) [scam](/tag.html?tag=scam)

[4 comment(s)](/diary/New%2BVariant%2Bof%2BCrypto%2BConfidence%2BScam/31968/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31964)
* [next](/diary/31972)

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