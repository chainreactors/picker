---
title: Changes in SSL and TLS support in 2024, (Mon, Dec 30th)
url: https://isc.sans.edu/diary/rss/31550
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-31
fetch_date: 2025-10-06T19:42:10.524703
---

# Changes in SSL and TLS support in 2024, (Mon, Dec 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31548)
* [next](/diary/31552)

# [Changes in SSL and TLS support in 2024](/forums/diary/Changes%2Bin%2BSSL%2Band%2BTLS%2Bsupport%2Bin%2B2024/31550/)

**Published**: 2024-12-30. **Last Updated**: 2024-12-30 11:21:15 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/Changes%2Bin%2BSSL%2Band%2BTLS%2Bsupport%2Bin%2B2024/31550/#comments)

With the end of the year quickly approaching, it is undoubtedly a good time to take a look at what has changed during the past 12 months. One security-related area, which deserves special attention in this context, is related to the use of different versions of SSL and TLS on various servers on the internet, since information about support for these protocols can provide us with a good informal indicator for the overall “level of security” on the global network as a whole.

This is true especially when it comes to web servers, since there are a lot of them, and the continued support for deprecated[[1](https://en.wikipedia.org/wiki/Transport_Layer_Security#History_and_development)] versions of the aforementioned cryptographic protocols (i.e., SSL 2.0, SSL 3.0, TLS 1.0 and TLS 1.1) on a specific web server shows quite well that the server is not configured in line with current security best practices (and it gives a good indication that it probably lacks important updates and patches as well).

In order to show how the support for various SSL/TLS versions has changed, we will use data gathered from [Shodan](https://www.shodan.io/), mostly using my TriOp tool[[2](https://isc.sans.edu/diary/27034)].

Going by this data, Shodan scans detected between 124 and 166 million web servers accessible from the internet during the course of the year. Or – to be more specific – the scans detected these numbers of public IP addresses responding to traffic on port 443. And while most (though not all) of these IP addresses have hosted a web server of some sort, in some cases, these servers were only very simple ones, intended only to display a configuration interface of a specific device (e.g., a SOHO router).

In any case, as you can see from the following chart, support for TLS 1.3 on web servers has increased significantly during 2024 – from approximately 25% at the beginning of the year to over 30% at the end. TLS 1.2 has seen similar increase (from 38% to nearly 44%), while support for TLS 1.1 and TLS 1.0 has stayed nearly the same throughout the year (around 22%).

[![](https://isc.sans.edu/diaryimages/images/24-12-30-tls.png)](https://isc.sans.edu/diaryimages/images/24-12-30-tls.png)

While overall support for SSLv3 has also remained largely unchanged throughout the year (~1.43%), support for SSLv2 has decreased a little (from ~0.3% to ~0.25%).

[![](https://isc.sans.edu/diaryimages/images/24-12-30-ssl.png)](https://isc.sans.edu/diaryimages/images/24-12-30-ssl.png)

One additional type of systems that deserves a short mention when discussing SSL and TLS support are e-mail servers. As a security community we generally tend to focus more on the use of cryptographic protocols to protect web traffic, but their use to protect e-mail communication is arguably just as important (though their use in this area is generally much more opportunistic in its nature).

The good news, when it comes to e-mail, is that support for TLS 1.3 has grown to be approximately the same as support for TLS 1.0 and TLS 1.1 on all three relevant ports (TCP/25, TCP/465 and TCP/587) – i.e., TLS 1.3 now seems to be supported by approximately 30% of SMTP servers on the internet.

Detailed overview of the changes in SSL/TLS support on e-mail servers can be seen in the following charts from [Shodan Trends](https://trends.shodan.io/).

[![](https://isc.sans.edu/diaryimages/images/24-12-30-e-mail-25.png)](https://isc.sans.edu/diaryimages/images/24-12-30-e-mail-25.png)

[![](https://isc.sans.edu/diaryimages/images/24-12-30-e-mail-465.png)](https://isc.sans.edu/diaryimages/images/24-12-30-e-mail-465.png)

[![](https://isc.sans.edu/diaryimages/images/24-12-30-e-mail-587.png)](https://isc.sans.edu/diaryimages/images/24-12-30-e-mail-587.png)

While it seems that some SSL 3.0 and even SSL 2.0-enabled systems will remain with us for the foreseeable future, it is clear that the overall SSL/TLS situation has certainly improved in the past 12 months. Let us hope that this trend will continue in 2025…

[1] <https://en.wikipedia.org/wiki/Transport_Layer_Security#History_and_development>
[2] <https://isc.sans.edu/diary/27034>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[0 comment(s)](/diary/Changes%2Bin%2BSSL%2Band%2BTLS%2Bsupport%2Bin%2B2024/31550/#comments)

* [previous](/diary/31548)
* [next](/diary/31552)

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