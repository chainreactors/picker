---
title: Google Presentations Abused for Phishing, (Fri, Jan 30th)
url: https://isc.sans.edu/diary/rss/32668
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-30
fetch_date: 2026-01-31T04:05:17.372229
---

# Google Presentations Abused for Phishing, (Fri, Jan 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32662)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Google Presentations Abused for Phishing](/forums/diary/Google%2BPresentations%2BAbused%2Bfor%2BPhishing/32668/)

**Published**: 2026-01-30. **Last Updated**: 2026-01-30 17:56:10 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Google%2BPresentations%2BAbused%2Bfor%2BPhishing/32668/#comments)

Charlie, one of our readers, has forwarded an interesting phishing email. The email was sent to users of the Vivladi Webmail service. While not overly convincing, the email is likely sufficient to trick a non-empty group of users:

![](https://isc.sans.edu/diaryimages/images/vivaldiphish1.png)

The e-mail gets more interesting as the user clicks on the link. The link points to Google Documents and displays a slide show:

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-01-30%20at%2012_31_30%E2%80%AFPM.png)

Usually, Google Docs displays a footer notice that warns viewers about phishing sites and offers a "reporting" link if a page is used for phishing. Bots are missing in this case. At first, I suspected some HTML/JavaScript/CSS tricks, but it turns out that this isn't a bug; it is a feature!

Usually, if a user shares slides, the document opens in an "edit" window. This can be avoided by replacing "edit" with "preview" in the URL, but the footer still makes it obvious that this is a set of slides. To remove the footer, the slides have to be "published," and the resulting link must be shared. When publishing, the slides will auto-advance. But for a one-slide slideshow, this isn't an issue. There is also a setting to delay the advance. Here are some sample links:

[These links point to a simple sample presentation I created, not the phishing version.]

Normal Share:

https://docs.google.com/presentation/d/1Quzd6bbuPlIcTOorlUDzSuJCXiOyqBTSHczo6hnXcac/edit?usp=sharing

Preview Share:

https://docs.google.com/presentation/d/1Quzd6bbuPlIcTOorlUDzSuJCXiOyqBTSHczo6hnXcac/preview?usp=sharing

Publish Share:

https://docs.google.com/presentation/d/e/2PACX-1vRaoBusJAaIoVcNbGsfVyE0OuTP1dS-2Po9lpAN9GGy2EkbZG\_oR9maZDS7cq2xW\_QeiF8he457hq3\_/pub?start=false&loop=false&delayms=30000

The URL parameters in the last link do not start the presentations, nor loop them, and delay the next slide by 30 seconds.

The Vivaldi webmail phishing ended up on a "classic" phishing login form that was created using Square. So far, this form is still visible at

hxxps [:] //vivaldiwebmailaccountsservices[.]weeblysite[.]com

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-01-30%20at%2012_41_24%E2%80%AFPM.png)???????

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [google slides phishing](/tag.html?tag=google slides phishing)

[0 comment(s)](/diary/Google%2BPresentations%2BAbused%2Bfor%2BPhishing/32668/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32662)

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