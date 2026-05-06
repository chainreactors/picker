---
title: SSL.com rotates their root certificate today, (Tue, May 5th)
url: https://isc.sans.edu/diary/rss/32956
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-05
fetch_date: 2026-05-06T05:09:40.682652
---

# SSL.com rotates their root certificate today, (Tue, May 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Rob VandenBrink](/handler_list.html#rob-vandenbrink "Rob VandenBrink")

Threat Level: [green](/infocon.html)

* [previous](/diary/32954)

Click HERE to learn more about classes Rob is teaching for SANS

# [SSL.com rotates their root certificate today](/forums/diary/SSLcom%2Brotates%2Btheir%2Broot%2Bcertificate%2Btoday/32956/)

**Published**: 2026-05-05. **Last Updated**: 2026-05-05 11:39:45 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 2)

[0 comment(s)](/diary/SSLcom%2Brotates%2Btheir%2Broot%2Bcertificate%2Btoday/32956/#comments)

I just got an email from SSL.com last night, they are rotating  out their root certificate today (May 5,2026).  This is normal, business as usual stuff for a CA, but certificates get used for all kinds of things, and sometimes they aren't used like they should be, so sometimes hiccups happen.

If you are using them for basic cert+website stuff, there's no need to worry.  But if you go past that basic implementation, you should read their note to make sure that this change won't be affecting any of your services.  Even if you don't use ssl.com, it's a good read, as every certificate expires, which means that everyone's root cert rotates out eventually - so forewarned if forearmed and all that ..

In particular (from the email):

* *If you have pinned trust anchors, custom trust stores, or certificate validation logic tied to the 2016 roots, please audit those configurations promptly to avoid disruptions.*
* *Use cross-certificates. If you need backward compatibility with the 2016 root hierarchy during the transition, cross-certificates can bridge the gap.*
* *Migrate to dedicated Client Certificates. These are purpose-built for client authentication and are unaffected by Google Chrome's upcoming server authentication requirements, which impact SSL/TLS certificates with the ClientAuth EKU.*

Their full post is here:

https://www.ssl.com/article/what-ssls-root-migration-means-for-you

===============
Rob VandenBrink
[[email protected]](/cdn-cgi/l/email-protection)

Keywords:

[0 comment(s)](/diary/SSLcom%2Brotates%2Btheir%2Broot%2Bcertificate%2Btoday/32956/#comments)

Click HERE to learn more about classes Rob is teaching for SANS

* [previous](/diary/32954)

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