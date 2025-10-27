---
title: Attacks against Teltonika Networks SMS Gateways, (Thu, Apr 24th)
url: https://isc.sans.edu/diary/rss/31888
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-25
fetch_date: 2025-10-06T22:07:08.274959
---

# Attacks against Teltonika Networks SMS Gateways, (Thu, Apr 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31880)
* [next](/diary/31892)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Attacks against Teltonika Networks SMS Gateways](/forums/diary/Attacks%2Bagainst%2BTeltonika%2BNetworks%2BSMS%2BGateways/31888/)

**Published**: 2025-04-24. **Last Updated**: 2025-04-24 14:57:37 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Attacks%2Bagainst%2BTeltonika%2BNetworks%2BSMS%2BGateways/31888/#comments)

![Image of Teltonika RUT956 SMS Gateway](https://isc.sans.edu/diaryimages/images/200px-RUT956_K_v1.png)Ever wonder where all the SMS spam comes from? If you are trying to send SMS "at scale," there are a few options: You could sign up for a messaging provider like Twilio, the AWS SNS service, or several similar services. These services offer easily scriptable and affordable ways to send SMS messages. We have [previously covered](https://isc.sans.edu/diary/27782) how attackers attempt to steal related credentials to use these services even cheaper (for free!).

But if you are not into cloud or SaaS, maybe you instead like to send your own SMS messages directly? Or would you like to become the next Twilio? In this case, special SMS gateways are available. One company making these gateways is [Teltonika Networks](https://teltonika-networks.com/). They offer a wide range of products to send and receive SMS, including devices for IoT remote management and enterprise SMS gateways.

But of course, you need to authenticate to send SMS messages. Nobody wants complex login credentials and passwords. Teltonika offers simple default credentials: "user1" as user name, and "user\_pass" as password.

I am surprised it took so long for us to see some scans for these well known credentials. For example:

> `/cgi-bin/sms_send?username=user1&password=user_pass&number=00966549306573&text=test`

This request will send an SMS "test" to 00966549306573, a number in Saudi Arabia. Oddly enough, I ever so often see Saudi Arabian numbers used in SMS related scans.

Here are a few other passwords I have seen, all for the user "user1":

> `1234
> admin
> p8xr6tINNA0eGBIY
> root
> rut9xx
> teltonika
> test
> user1`

The long "random" password is interesting. It was used several times, and I am not sure if that is some kind of "support" backdoor. The "rut9xx" password makes sense as the model numbers for the industrial Teltonika gateways start with "RUT", like RUT140, RUT901, RUT906...,

Numbers I have seen as a recipient:

> `00966549306573 (Saudi Arabia)
> 0032493855785& (Belgium)`

As usual, change default passwords, particularly for more professional equipment like this: Throw it back at the vendor (HARD!) if it comes with a default password.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [sms](/tag.html?tag=sms) [teltonika](/tag.html?tag=teltonika)

[0 comment(s)](/diary/Attacks%2Bagainst%2BTeltonika%2BNetworks%2BSMS%2BGateways/31888/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31880)
* [next](/diary/31892)

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