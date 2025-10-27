---
title: Password Cracking &#x26; Energy: More Dedails, (Sun, Sep 8th)
url: https://isc.sans.edu/diary/rss/31242
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-09
fetch_date: 2025-10-06T18:24:50.039846
---

# Password Cracking &#x26; Energy: More Dedails, (Sun, Sep 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31240)
* [next](/diary/31248)

# [Password Cracking & Energy: More Dedails](/forums/diary/Password%2BCracking%2BEnergy%2BMore%2BDedails/31242/)

**Published**: 2024-09-08. **Last Updated**: 2024-09-08 15:24:37 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Password%2BCracking%2BEnergy%2BMore%2BDedails/31242/#comments)

Here are more details on the power consumption of my desktop computer when I crack passwords (cfr diary entry "[Quickie: Password Cracking & Energy](https://isc.sans.edu/diary/Quickie%2BPassword%2BCracking%2BEnergy/31122)").

The vertical scale of this chart is expressed in Watts:

![](https://isc.sans.edu/diaryimages/images/20240908-165651.png)

1. 0 Watt: my desktop computer is turned off
2. 76 Watt average: my desktop computer is turned on & idling
3. 151 Watt average: hashcat is running in dictionary attack mode cracking SHA256 hashes
4. 445 Watt average: hashcat is running in brute-force attack mode cracking SHA256 hashes

The most power is required (445 Watt) when hashcat is using the GPU ( NVIDIA GeForce RTX 3080) in brute-force attack mode. For comparison, 445 Watt average continuous is enough to heat my office in winter to a nice & comfy temperature, I don't need central heating in that room when hashcat is running for many hours.

You might wonder if 445 Watt is enough for that, given that electrical heaters typically come in 1000+ Watt models. But electrical heaters don't consume electrical power constantly to heat a room, they have a thermostat that shuts of current flow regularly when the desired room temperature is reached. They are more powerfull so that they can heat up a room faster. While my desktop computer requires 445 Watt continuously when cracking with the GPU.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Password%2BCracking%2BEnergy%2BMore%2BDedails/31242/#comments)

* [previous](/diary/31240)
* [next](/diary/31248)

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