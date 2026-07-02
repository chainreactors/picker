---
title: Why Ask Credentials If There Are Secret Codes&#x3f;, (Wed, Jul 1st)
url: https://isc.sans.edu/diary/rss/33118
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-01
fetch_date: 2026-07-02T05:58:18.207295
---

# Why Ask Credentials If There Are Secret Codes&#x3f;, (Wed, Jul 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33114)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [Why Ask Credentials If There Are Secret Codes?](/forums/diary/Why%2BAsk%2BCredentials%2BIf%2BThere%2BAre%2BSecret%2BCodes/33118/)

**Published**: 2026-07-01. **Last Updated**: 2026-07-01 05:10:20 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Why%2BAsk%2BCredentials%2BIf%2BThere%2BAre%2BSecret%2BCodes/33118/#comments)

This morning, an interesting phishing email hit my mailbox. It targets Metamask[[1](https://metamask.io)], a cryptocurrency wallet, available as a browser extension and a mobile app, that lets users store, send, and receive crypto money. It’s pretty popular, so a juicy target for criminals. In February, I already mentioned a campaign against them[[2](https://isc.sans.edu/diary/Fake%2BIncident%2BReport%2BUsed%2Bin%2BPhishing%2BCampaign/32722)].

Today’s email was different and used another approach. Most services that we use daily ask us to implement a 2nd authentication factor. That makes simple credentials useless if you can’t interact with the victim and grab the temporary token, code, …

But most services also offer a “password recovery” process. In the case of Metamask, it’s based on your secret security phrase that you created during the account creation process[[3](https://support.metamask.io/configure/wallet/how-can-i-reset-my-password/)]. That’s exactly the target of this phishing campaign. They ask you to provide this secret phrase.

First, they put some pressure on you, pretending that your wallet is at risk:

![](https://isc.sans.edu/diaryimages/images/isc-20260701-1.png)

Then, they ask you to provide your secret phrase:

![](https://isc.sans.edu/diaryimages/images/isc-20260701-2.png)

The campaing relies on the domain captchasolve[.]help that has been registered two days ago.

[1] <https://metamask.io>
[2] [https://isc.sans.edu/diary/Fake+Incident+Report+Used+in+Phishing+Campaign/32722](https://isc.sans.edu/diary/Fake%2BIncident%2BReport%2BUsed%2Bin%2BPhishing%2BCampaign/32722)
[3] <https://support.metamask.io/configure/wallet/how-can-i-reset-my-password/>

**Xavier Mertens (@xme)**
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://raw.githubusercontent.com/xme/pgp/refs/heads/main/public.key)

Keywords: [Phrase](/tag.html?tag=Phrase) [Secret](/tag.html?tag=Secret) [Wallet](/tag.html?tag=Wallet) [Metamask](/tag.html?tag=Metamask) [Phishing](/tag.html?tag=Phishing)

[0 comment(s)](/diary/Why%2BAsk%2BCredentials%2BIf%2BThere%2BAre%2BSecret%2BCodes/33118/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33114)

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