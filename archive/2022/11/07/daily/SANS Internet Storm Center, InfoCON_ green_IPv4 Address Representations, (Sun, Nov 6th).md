---
title: IPv4 Address Representations, (Sun, Nov 6th)
url: https://isc.sans.edu/diary/rss/29224
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-07
fetch_date: 2025-10-03T21:52:55.065391
---

# IPv4 Address Representations, (Sun, Nov 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29222)
* [next](/diary/29230)

# [IPv4 Address Representations](/forums/diary/IPv4%2BAddress%2BRepresentations/29224/)

**Published**: 2022-11-06. **Last Updated**: 2022-11-06 12:57:12 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/IPv4%2BAddress%2BRepresentations/29224/#comments)

A reader asked for help with this [maldoc](https://bazaar.abuse.ch/sample/8d2703900fc859896a72e9ad7f9a395559dd9da5dbd0d87ca1dc57b21b32ebf0/). Not with the analysis itself, but how to understand where the URL is pointing to.

This is the URL they extracted:

![](https://isc.sans.edu/diaryimages/images/20221106-110840.png)

It contains [userinfo and a host](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax):

![](https://isc.sans.edu/diaryimages/images/20221106-110210.png)

This URL analysis can also be done with CyberChef, using the Parse URI operation:

![](https://isc.sans.edu/diaryimages/images/20221106-110922.png)

So the host is just a number. An integer.

That integer is an IPv4 address. [According to Wikipedia](https://en.wikipedia.org/wiki/IPv4#Address_representations):

> IPv4 addresses may be represented in any notation expressing a 32-bit integer value.

There is no CyberChef operation to convert this value, but it can be done with a short Python script, that you can run online in one of the many [online Python interpreters](https://www.google.com/search?q=online+Python):

![](https://isc.sans.edu/diaryimages/images/20221106-112823.png)

> import ipaddress
> print(ipaddress.IPv4Address(fill in your IPv4 address))

Maybe someone can code a new CyberChef operation that parses the many IPv4 address representations. This [blog post](https://www.hacksparrow.com/networking/many-faces-of-ip-address.html) on IPv4 address representations is a good starting point.

(I started to adapt some existing CyberChef operations and code new ones).

Update: I started writing a new "Normalise IPv4 Address" operation:

![](https://isc.sans.edu/diaryimages/images/20221106-135340.png)

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/IPv4%2BAddress%2BRepresentations/29224/#comments)

* [previous](/diary/29222)
* [next](/diary/29230)

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