---
title: Crypto Wallet Scam: Not For Free, (Sat, Feb 8th)
url: https://isc.sans.edu/diary/rss/31666
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-09
fetch_date: 2025-10-06T20:37:53.556732
---

# Crypto Wallet Scam: Not For Free, (Sat, Feb 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31664)
* [next](/diary/31668)

# [Crypto Wallet Scam: Not For Free](/forums/diary/Crypto%2BWallet%2BScam%2BNot%2BFor%2BFree/31666/)

**Published**: 2025-02-08. **Last Updated**: 2025-02-08 18:47:03 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[2 comment(s)](/diary/Crypto%2BWallet%2BScam%2BNot%2BFor%2BFree/31666/#comments)

I did some research into multisig wallets (cfr "[Crypto Wallet Scam](https://isc.sans.edu/diary/Crypto%2BWallet%2BScam/31646)"), and discovered that setting up such a wallet on the TRON network comes with a cost: about $23.

First I used the TronLink extension to create a wallet:

![](https://isc.sans.edu/diaryimages/images/20250208-191625.png)

Then I went to that wallet on Tronscan, and selected the Permissions tab:

![](https://isc.sans.edu/diaryimages/images/20250208-192949.png)

And there I added a new permission (giving all operations to another wallet) and deleted the original permission:

![](https://isc.sans.edu/diaryimages/images/20250208-193106.png)

And when I saved my changes, and got this prompt:

![](https://isc.sans.edu/diaryimages/images/20250208-192505.png)

You can't create a multisig wallet by changing permissions for free: it costs 100 TRX, that's about $23.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[2 comment(s)](/diary/Crypto%2BWallet%2BScam%2BNot%2BFor%2BFree/31666/#comments)

* [previous](/diary/31664)
* [next](/diary/31668)

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