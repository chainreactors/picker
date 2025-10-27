---
title: Wireshark 4.4's IP Address Functions, (Mon, Sep 9th)
url: https://isc.sans.edu/diary/rss/31250
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-10
fetch_date: 2025-10-06T18:32:11.560946
---

# Wireshark 4.4's IP Address Functions, (Mon, Sep 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31248)
* [next](/diary/31254)

# [Wireshark 4.4's IP Address Functions](/forums/diary/Wireshark%2B44s%2BIP%2BAddress%2BFunctions/31250/)

**Published**: 2024-09-09. **Last Updated**: 2024-09-09 11:35:46 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Wireshark%2B44s%2BIP%2BAddress%2BFunctions/31250/#comments)

New IP address functions have been added in Wireshark 4.4 (if you use Wireshark on Windows, there's a [bug in release 4.4.0: the DLL with these functions is missing](https://gitlab.com/wireshark/wireshark/-/issues/20030), it will be included in release 4.4.1; all is fine with Linux and Mac versions of Wireshark).

These are the functions:

![](https://isc.sans.edu/diaryimages/images/20240909-125512.png)

They are explained in the [Wireshark filter manual](https://www.wireshark.org/docs/man-pages/wireshark-filter.html) under "Functions".

Function ip\_rfc1918, for example, returns True when the argument of this function is a private use IPv4 address. It can be used as a display filter, like this:

![](https://isc.sans.edu/diaryimages/images/20240909-131014.png)

These functions can also be used in [custom columns](https://isc.sans.edu/diary/Wireshark%2B440rc1s%2BCustom%2BColumns/31174), like function ip\_special\_name that returns the IP special-purpose block name as a string:

![](https://isc.sans.edu/diaryimages/images/20240909-132638.png)

![](https://isc.sans.edu/diaryimages/images/20240909-132706.png)

To summarize: these functions were introduced with Wireshark release 4.4, but this will not work only if you are using Windows version 4.4.0. I used release candicate 4.4.1 to take these screenshots, as the missing dll (ipaddress.dll) is present in that package.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Wireshark%2B44s%2BIP%2BAddress%2BFunctions/31250/#comments)

* [previous](/diary/31248)
* [next](/diary/31254)

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