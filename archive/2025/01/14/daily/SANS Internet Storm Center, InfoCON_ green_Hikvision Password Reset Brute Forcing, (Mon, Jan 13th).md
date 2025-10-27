---
title: Hikvision Password Reset Brute Forcing, (Mon, Jan 13th)
url: https://isc.sans.edu/diary/rss/31586
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-14
fetch_date: 2025-10-06T20:13:19.736995
---

# Hikvision Password Reset Brute Forcing, (Mon, Jan 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31582)
* [next](/diary/31590)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Hikvision Password Reset Brute Forcing](/forums/diary/Hikvision%2BPassword%2BReset%2BBrute%2BForcing/31586/)

**Published**: 2025-01-13. **Last Updated**: 2025-01-13 20:41:00 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Hikvision%2BPassword%2BReset%2BBrute%2BForcing/31586/#comments)

One common pattern in password resets is sending a one-time password to the user to enable them to reset their password. The flow usually looks like:

1. User Requests a password reset
2. The user enters an e-mail address or phone number that is already registered with the application
3. The application may ask for a password reset question
4. The user now receives a random code that is entered into the password reset page
5. finally, the user can reset their password

Overall, this approach is not terrible. It is similar to sending a one-time password reset link via email but avoids the issue of the user having to click on a link (which may be difficult with some mobile applications). This reset method tends to work better with users using mobile phones as they may be able to receive the code via SMS. Or, if they use a "fat" email client on a desktop, they can easily type the code into the mobile device.

But there is a critical issue that is often overlooked:

The page verifying the code MUST implement some basic brute force protection. Otherwise, it tends to be easy to brute force the code, which is often just a five or six-digit number. Of course, this assumes that the code is random! More about this later.

This has been an issue a few times already. Facebook, for example, suffered from this weakness last year. Only a limited number of attempts should be allowed to implement some brute force protection, and the time the code is valid should be constrained. In my opinion, for an "average" site, five attempts and 30 minutes seem reasonable.

One reminder that this is still an issue came today from our "First Seen URLs" page. While not an actual "First Seen" URL, the URL

> /PSIA/Custom/HIK/userCheck

![](https://isc.sans.edu/diaryimages/images/Screenshot%202025-01-13%20at%203_37_28%E2%80%AFPM.png)had a bit of a breakout with more users than normal reporting honeypot hits for this URL.

An exploit for the Hikvision issue has been available since 2018 when Rasmus Moorats published a blog with some code showing how to exploit the vulnerability [1]. Rasmus even went a significant step further. With access to the firmware, he could decompile it, and reverse engineer the function used to create the reset code. Turns out that the code was not random at all, but instead derived from the UPNP data. This data can be retrieved without authentication. You do not necessarily have to be on the same network, but an HTTP request for /upnpdevicedesc.xml is all it takes.

[1] https://nns.ee/blog/2018/08/01/hikvision-keygen.html

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [reset](/tag.html?tag=reset) [password](/tag.html?tag=password) [hikvision](/tag.html?tag=hikvision)

[0 comment(s)](/diary/Hikvision%2BPassword%2BReset%2BBrute%2BForcing/31586/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31582)
* [next](/diary/31590)

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