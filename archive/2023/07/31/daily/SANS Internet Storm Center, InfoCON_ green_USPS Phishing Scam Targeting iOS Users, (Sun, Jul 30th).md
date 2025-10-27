---
title: USPS Phishing Scam Targeting iOS Users, (Sun, Jul 30th)
url: https://isc.sans.edu/diary/rss/30078
source: SANS Internet Storm Center, InfoCON: green
date: 2023-07-31
fetch_date: 2025-10-04T11:52:55.144133
---

# USPS Phishing Scam Targeting iOS Users, (Sun, Jul 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30076)
* [next](/diary/30084)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [USPS Phishing Scam Targeting iOS Users](/forums/diary/USPS%2BPhishing%2BScam%2BTargeting%2BiOS%2BUsers/30078/)

**Published**: 2023-07-30. **Last Updated**: 2023-07-30 15:33:55 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[5 comment(s)](/diary/USPS%2BPhishing%2BScam%2BTargeting%2BiOS%2BUsers/30078/#comments)

Phishing scams have frequently arrived as an SMS message (sometimes called "Smishing"). SMS messages are easy and cheap to send, and we have documented how attackers like to scan for exposed credentials for services like Twilio to make it even cheaper.

But today, I received a message on my Apple devices that didn't arrive as an green SMS, but instead as a blue iMessage

![](https://isc.sans.edu/diaryimages/images/Screenshot%202023-07-30%20at%2011_00_15%20AM.png)

As I always do, I clicked on the link on my Mac. But I was immediately redirected to the legitimate USPS page (usps.com). It didn't matter if I used Safari or Chrome on macOS. So I tried Safari on my iPhone and was directed to the phishing page.

![](https://isc.sans.edu/diaryimages/images/IMG_1889.png)

The page appears to attempt to collect credit card numbers. I didn't feel charitable enough to provide a real credit card number, so I am unsure if it would ask for any additional information.

The main domain (deliverocy.com) does not resolve. I did try a few other hostnames (FedEx, www, ups...), but no other hostname was resolved. +639468743057 is a number in the Philippines. I did try a Facetime call, but nobody picked up :(

The site's '/admin' URL presents a login screen for some kind of admin system. The background image appears to come from "Ghostblade". The admin part of the site did not restrict the user-agent like the phishing part of the site.

![](https://isc.sans.edu/diaryimages/images/IMG_1893.png)

Restricting access to the phishing site to specific user agents may help in keeping the phishing site up. A casual test of the URL will only redirect to the legitimate USPS website, which may trick an ISP's abuse department into believing that this is not a phishing page.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[5 comment(s)](/diary/USPS%2BPhishing%2BScam%2BTargeting%2BiOS%2BUsers/30078/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/30076)
* [next](/diary/30084)

### Comments

It has been interesting watching the evolution of this one. I started receiving texts like this in mid to late June. It used to respond to a sandbox service, and then stopped, and presented the real USPS page. I guess because the sandbox service didn't support mobile.

https://www.joesandbox.com/analysis/1261719
https://www.joesandbox.com/analysis/1274709

#### phydroxide

#### Jul 31st 2023 2 years ago

It has been interesting watching the evolution of this one. I started receiving texts like this in mid to late June. It used to respond to a sandbox service, and then stopped, and presented the real USPS page. I guess because the sandbox service didn't support mobile.

https://www.joesandbox.com/analysis/1261719
https://www.joesandbox.com/analysis/1274709

#### phydroxide

#### Jul 31st 2023 2 years ago

It has been interesting watching the evolution of this one. I started receiving texts like this in mid to late June. It used to respond to a sandbox service, and then stopped, and presented the real USPS page. I guess because the sandbox service didn't support mobile.

https://www.joesandbox.com/analysis/1261719
https://www.joesandbox.com/analysis/1274709

#### phydroxide

#### Jul 31st 2023 2 years ago

It has been interesting watching the evolution of this one. I started receiving texts like this in mid to late June. It used to respond to a sandbox service, and then stopped, and presented the real USPS page. I guess because the sandbox service didn't support mobile.

https://www.joesandbox.com/analysis/1261719
https://www.joesandbox.com/analysis/1274709

#### phydroxide

#### Jul 31st 2023 2 years ago

Sorry for the spam. I clicked again when the page was unresponsive.
Love the podcast. I think I've listened to every one published for the past 2 years at this point. I almost never miss catching it in the morning.

#### phydroxide

#### Jul 31st 2023 2 years ago

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