---
title: Airtell Router Scans, and Mislabeled usernames, (Wed, Aug 20th)
url: https://isc.sans.edu/diary/rss/32216
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-21
fetch_date: 2025-10-07T00:50:15.194672
---

# Airtell Router Scans, and Mislabeled usernames, (Wed, Aug 20th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32212)
* [next](/diary/32220)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Airtell Router Scans, and Mislabeled usernames](/forums/diary/Airtell%2BRouter%2BScans%2Band%2BMislabeled%2Busernames/32216/)

**Published**: 2025-08-20. **Last Updated**: 2025-08-20 15:27:19 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Airtell%2BRouter%2BScans%2Band%2BMislabeled%2Busernames/32216/#comments)

Looking at new usernames collected by our Cowrie honeypots, you will first of all notice a number of HTTP headers. It is very common for attackers to scan for web servers on ports that are covered by our Telnet honeypots. The result is that HTTP request headers end up in our username and password database.

This morning, I noticed another interestingly looking username: Airtel@123 [[1](https://isc.sans.edu/ssh_usernames.html?username=QWlydGVsQDEyMw%3D%3D)]. We do see it used with "passwords" like root, otx, and itmuser.

A quick Google search confirmed that "Airtel@123" is the password, and the username is likely "admin", which is not even in the list above. There is another odd thing the attacker may have overlooked here: Based on the documentation I could find, "Airtel@123" is not the telnet/ssh password for the Airtell Zerotouch router. Instead, it appears to be the Wifi default password. The login defaults to the less creative "admin"/"admin".

And while we are at it, here are a few more "interesting but useful" usernames and passwords I have seen:

'"username"&apos; - Maybe someone parsing a random password list that was HTML encoded? Or someone trying to XSS our site?

echo 'Connection established' - no, it wasn't. Likely a check to see if the login succeeded.

'"root"' - even double quotes got escaped correctly. I still think this is more bad parsing of a username list, and not an XSS attack.

usernane "$oot" and password "$dmin". Interesting... No idea if that will work, but anybody got any ideas why someone may try this?

For a full list of recent usernames, see <https://isc.sans.edu/data/allsshusernames.html>. Let me know if you spot anything interesting.

[1] <https://isc.sans.edu/ssh_usernames.html?username=QWlydGVsQDEyMw%3D%3D>

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [airtel](/tag.html?tag=airtel) [passwords](/tag.html?tag=passwords) [usernames](/tag.html?tag=usernames)

[0 comment(s)](/diary/Airtell%2BRouter%2BScans%2Band%2BMislabeled%2Busernames/32216/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32212)
* [next](/diary/32220)

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