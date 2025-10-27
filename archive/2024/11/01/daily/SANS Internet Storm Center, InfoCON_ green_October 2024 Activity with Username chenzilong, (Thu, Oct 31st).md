---
title: October 2024 Activity with Username chenzilong, (Thu, Oct 31st)
url: https://isc.sans.edu/diary/rss/31400
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-01
fetch_date: 2025-10-06T19:30:57.353945
---

# October 2024 Activity with Username chenzilong, (Thu, Oct 31st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31398)
* [next](/diary/31404)

# [October 2024 Activity with Username chenzilong](/forums/diary/October%2B2024%2BActivity%2Bwith%2BUsername%2Bchenzilong/31400/)

**Published**: 2024-10-31. **Last Updated**: 2024-10-31 00:16:09 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/October%2B2024%2BActivity%2Bwith%2BUsername%2Bchenzilong/31400/#comments)

After reviewing the *Top 10 Not So Common SSH Usernames and Passwords* [[1](https://isc.sans.edu/diary/The%2BTop%2B10%2BNot%2BSo%2BCommon%2BSSH%2BUsernames%2Band%2BPasswords/31360)] published by Johannes 2 weeks ago, I noticed activity by one in his list that we don't really know what it is. Beginning 12 October 2024, my DShield sensor started storing one of the usernames mentioned in his diary that I had never seen before (I have over a year of data). The username chenzilong has been used with 5 different passwords including, some combination with the same username. So far, this account activity has been used with 302 different IPs.

![](https://isc.sans.edu/diaryimages/images/chenzilong_pic1.PNG)

Some of the activity appears to have succeeded to login the DShield sensor but it appears to just login and leave, no other activity noted. It only appears to be testing.

![](https://isc.sans.edu/diaryimages/images/chenzilong_pic2.PNG)

Reviewing each of the 25 IPs with successfully login, the bot (I'm assuming it is), didn't execute any commands after each successful login. This was no data transferred.

This picture shows the ASN traffic distribution with ASN 45102 (Alibaba US Technology) being the most active during that period.

![](https://isc.sans.edu/diaryimages/images/chenzilong_ASN_pic1.PNG)

[1] https://isc.sans.edu/diary/The+Top+10+Not+So+Common+SSH+Usernames+and+Passwords/31360
[2] https://github.com/bruneaug/DShield-SIEM/tree/main

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [chenzilong](/tag.html?tag=chenzilong) [DShield](/tag.html?tag=DShield) [ELK](/tag.html?tag=ELK) [infosec](/tag.html?tag=infosec) [password](/tag.html?tag=password) [SIEM](/tag.html?tag=SIEM)

[0 comment(s)](/diary/October%2B2024%2BActivity%2Bwith%2BUsername%2Bchenzilong/31400/#comments)

* [previous](/diary/31398)
* [next](/diary/31404)

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