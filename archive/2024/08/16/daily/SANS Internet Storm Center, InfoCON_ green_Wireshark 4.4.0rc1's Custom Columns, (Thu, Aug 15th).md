---
title: Wireshark 4.4.0rc1's Custom Columns, (Thu, Aug 15th)
url: https://isc.sans.edu/diary/rss/31174
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-16
fetch_date: 2025-10-06T18:05:36.970158
---

# Wireshark 4.4.0rc1's Custom Columns, (Thu, Aug 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31170)
* [next](/diary/31182)

# [Wireshark 4.4.0rc1's Custom Columns](/forums/diary/Wireshark%2B440rc1s%2BCustom%2BColumns/31174/)

**Published**: 2024-08-15. **Last Updated**: 2024-08-15 08:27:12 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Wireshark%2B440rc1s%2BCustom%2BColumns/31174/#comments)

In diary entry "[A Wireshark Lua Dissector for Fixed Field Length Protocols](https://isc.sans.edu/diary/A%2BWireshark%2BLua%2BDissector%2Bfor%2BFixed%2BField%2BLength%2BProtocols/30976)", I show how to use a protocol dissector I wrote in Lua to parse TCP data.

Wireshark 4.4.0 Release Candidate 1 [was released](https://www.wireshark.org/news/20240814.html), and it allows us to use field expressions as custom columns.

This means that some of the functionality that had to be implemented with a dissector, can now just be configured.

Take this example of fields Function, Direction, Counter, DataLength and Data, as defined with my custom Lua dissector:

![](https://isc.sans.edu/diaryimages/images/20240603-123246.png)

Similar fields can now be configured via field expressions and custom columns:

![](https://isc.sans.edu/diaryimages/images/20240815-100920.png)

By adding custom columns and field expressions.

For example, the field Function is the first byte of the TCP payload: tcp.payload[0]

![](https://isc.sans.edu/diaryimages/images/20240815-100954.png)

Another example: field Counter is the third and fourth byte of the TCP payload: tcp.payload[2:2]

![](https://isc.sans.edu/diaryimages/images/20240815-101021.png)

As you can see, the column values are displayed as bytes (hexadecimal).

I have not found a way to convert this to decimal integers.

If you have a solution, please post a comment.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Wireshark%2B440rc1s%2BCustom%2BColumns/31174/#comments)

* [previous](/diary/31170)
* [next](/diary/31182)

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