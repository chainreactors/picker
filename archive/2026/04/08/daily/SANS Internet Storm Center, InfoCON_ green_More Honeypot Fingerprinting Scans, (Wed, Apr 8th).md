---
title: More Honeypot Fingerprinting Scans, (Wed, Apr 8th)
url: https://isc.sans.edu/diary/rss/32878
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-08
fetch_date: 2026-04-09T04:32:25.335661
---

# More Honeypot Fingerprinting Scans, (Wed, Apr 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32874)
* [next](/diary/32880)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [More Honeypot Fingerprinting Scans](/forums/diary/More%2BHoneypot%2BFingerprinting%2BScans/32878/)

**Published**: 2026-04-08. **Last Updated**: 2026-04-08 14:23:28 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/More%2BHoneypot%2BFingerprinting%2BScans/32878/#comments)

One question that often comes up when I talk about honeypots: Are attackers able to figure out if they are connected to a honeypot? The answer is pretty simple: Yes!

Most "medium interaction" honeypots, like the one we are using, are just simulating various systems. These simulations are incomplete. For example, we are using the "Cowrie" honeypot to emulate SSH and telnet servers. Once an attacker is connected, any package they are installing will appear to install. In the past, I have written about attackers attempting to install bogus packages. If the install appears to succeed, the attacker knows they are connected to a honeypot. Some attackers look for SSH artifacts, such as the number and types of ciphers supported by SSH.

Today, I noticed one attacker, (IP address [45.135.194.48](/ipinfo.html?ip=45.135.194.48)), using another common trick: Cowrie will often allow attackers to connect "randomly". The effect is that various username and password combinations appear to work. In this case, the attacker used usernames and passwords that are highly unlikely to work. If they succeed, they know they are connected to a honeypot. Here are some of the usernames and passwords used:

| username | password |
| --- | --- |
| admin | definitely\_not\_valid\_creds |
| honeypot | indexer |
| honeypotter | imaginegettingindexed |
| xXhoneypotXx | P@ssw0rd1337! |
| youjustgotindexed | getindexedretard |

Will we do anything to block these types of requests? Maybe... I am not sure it is important enough to "hide" honeypots. One advantage we have is that many of our honeypots are connected to home networks with dynamic IPs. As a result, any IP address list an attacker will create is somewhat ephemeral. Secondly, we are mostly interested in internet-wide scans. We are not going to detect targeted attacks or zero days.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [fingerprint](/tag.html?tag=fingerprint) [honeypot](/tag.html?tag=honeypot)

[0 comment(s)](/diary/More%2BHoneypot%2BFingerprinting%2BScans/32878/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32874)
* [next](/diary/32880)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)