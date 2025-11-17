---
title: &#x26;#xa;Finger.exe &#x26; ClickFix, (Sun, Nov 16th)
url: https://isc.sans.edu/diary/rss/32492
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-16
fetch_date: 2025-11-17T03:12:51.483331
---

# &#x26;#xa;Finger.exe &#x26; ClickFix, (Sun, Nov 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32488)

# [Finger.exe & ClickFix](/forums/diary/Fingerexe%2BClickFix/32492/)

**Published**: 2025-11-16. **Last Updated**: 2025-11-16 07:27:55 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Fingerexe%2BClickFix/32492/#comments)

The finger.exe command is used in [ClickFix attacks](https://www.bleepingcomputer.com/news/security/decades-old-finger-protocol-abused-in-clickfix-malware-attacks/).

finger is a very old UNIX command, that was converted to a Windows executable years ago, and is part of Windows since then.

In the ClickFix attacks, it is used to retrieve a malicious script via the finger protocol.

We wrote about finger.exe about 3 years ago: "[Finger.exe LOLBin](https://isc.sans.edu/diary/29298)".

What you need to know:

* finger communication takes place over TCP
* the finger protocol uses TCP port 79 and there is no way to change this port
* finger.exe is not proxy aware

So if you are in a corporate environment with an explicit proxy (and blocking all Internet facing communication that doesn't go through the proxy), the finger.exe command won't be able to communicate.

And if you have a transparent proxy, finger.exe will be able to communicate provided the proxy allows TCP connections to port 79.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Fingerexe%2BClickFix/32492/#comments)

* [previous](/diary/32488)

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